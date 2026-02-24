# -*- coding: utf-8 -*-
"""
Odoo CRM Integration - Lead Capture from Website Forms
Controlador para capturar leads desde formularios web
"""

from odoo import http
from odoo.http import request
import json
import logging

_logger = logging.getLogger(__name__)


class WebsiteCRMController(http.Controller):
    """Controller para manejar formularios web que generan leads en CRM"""
    
    @http.route('/contacto/submit', type='http', auth='public', website=True, methods=['POST'], csrf=True)
    def contact_form_submit(self, **post):
        """
        Procesar formulario de contacto y crear lead en CRM
        
        Campos esperados:
        - name: Nombre completo
        - email: Email
        - phone: Teléfono
        - company: Empresa (opcional)
        - message: Mensaje/consulta
        - utm_source, utm_medium, utm_campaign: Parámetros de tracking
        """
        try:
            # Validar campos requeridos
            if not post.get('name') or not post.get('email'):
                return request.render('website.404')
            
            # Buscar o crear UTM source
            source_id = self._get_or_create_utm_source(post.get('utm_source', 'website'))
            medium_id = self._get_or_create_utm_medium(post.get('utm_medium', 'organic'))
            campaign_id = None
            if post.get('utm_campaign'):
                campaign_id = self._get_or_create_utm_campaign(post.get('utm_campaign'))
            
            # Crear lead en CRM
            lead_vals = {
                'name': f"Web - Contacto: {post.get('name')}",
                'contact_name': post.get('name'),
                'email_from': post.get('email'),
                'phone': post.get('phone', ''),
                'partner_name': post.get('company', ''),
                'description': post.get('message', ''),
                'type': 'lead',  # o 'opportunity' si se quiere directamente como oportunidad
                'source_id': source_id,
                'medium_id': medium_id,
                'campaign_id': campaign_id,
                'team_id': self._get_sales_team_id(),
                'user_id': False,  # Sin asignar inicialmente, o aplicar regla de asignación
                'priority': '0',  # Baja por defecto
            }
            
            lead = request.env['crm.lead'].sudo().create(lead_vals)
            _logger.info(f"Lead creado desde formulario web: {lead.id} - {lead.name}")
            
            # Enviar email de confirmación al cliente
            self._send_confirmation_email(lead)
            
            # Trackear evento en GA4 (si está integrado)
            if request.website.google_analytics_key:
                request.website._ga_track_event('generate_lead', {
                    'currency': 'COP',
                    'value': 0,
                    'lead_source': 'contact_form'
                })
            
            # Redirigir a página de gracias
            return request.render('website_crm_lead_capture.contactus_thanks', {
                'lead': lead
            })
            
        except Exception as e:
            _logger.error(f"Error creando lead desde formulario de contacto: {str(e)}")
            return request.render('website.404')
    
    @http.route('/shop/quote/submit', type='http', auth='public', website=True, methods=['POST'], csrf=True)
    def quote_request_submit(self, **post):
        """
        Procesar solicitud de cotización y crear oportunidad en CRM
        
        Campos esperados:
        - product_id: ID del producto
        - product_name: Nombre del producto
        - name: Nombre del cliente
        - email: Email
        - phone: Teléfono
        - quantity: Cantidad deseada
        - message: Mensaje adicional (opcional)
        """
        try:
            # Validar campos requeridos
            if not all([post.get('name'), post.get('email'), post.get('product_id')]):
                return request.render('website.404')
            
            product_id = int(post.get('product_id'))
            product = request.env['product.product'].sudo().browse(product_id)
            
            if not product.exists():
                return request.render('website.404')
            
            quantity = int(post.get('quantity', 1))
            estimated_value = product.list_price * quantity
            
            # Crear descripción detallada
            description = f"""
Solicitud de cotización desde web

Producto: {product.name} (SKU: {product.default_code or 'N/A'})
Cantidad: {quantity}
Precio unitario lista: ${product.list_price:,.2f} COP
Valor estimado: ${estimated_value:,.2f} COP

Mensaje del cliente:
{post.get('message', 'Sin mensaje adicional')}
            """.strip()
            
            # UTM tracking
            source_id = self._get_or_create_utm_source(post.get('utm_source', 'website'))
            medium_id = self._get_or_create_utm_medium(post.get('utm_medium', 'quote_request'))
            campaign_id = None
            if post.get('utm_campaign'):
                campaign_id = self._get_or_create_utm_campaign(post.get('utm_campaign'))
            
            # Crear oportunidad en CRM
            opportunity_vals = {
                'name': f"Web - Cotización: {product.name} - {post.get('name')}",
                'contact_name': post.get('name'),
                'email_from': post.get('email'),
                'phone': post.get('phone', ''),
                'description': description,
                'type': 'opportunity',
                'source_id': source_id,
                'medium_id': medium_id,
                'campaign_id': campaign_id,
                'team_id': self._get_sales_team_id(),
                'user_id': False,
                'priority': '1',  # Media - es una solicitud explícita de cotización
                'expected_revenue': estimated_value,
            }
            
            opportunity = request.env['crm.lead'].sudo().create(opportunity_vals)
            _logger.info(f"Oportunidad creada desde solicitud de cotización: {opportunity.id}")
            
            # Enviar email de confirmación
            self._send_quote_confirmation_email(opportunity, product, quantity)
            
            # Trackear evento en GA4
            if request.website.google_analytics_key:
                request.website._ga_track_event('generate_lead', {
                    'currency': 'COP',
                    'value': estimated_value,
                    'lead_source': 'quote_request',
                    'items': [{
                        'item_id': product.default_code or str(product.id),
                        'item_name': product.name,
                        'price': product.list_price,
                        'quantity': quantity
                    }]
                })
            
            return request.render('website_crm_lead_capture.quote_thanks', {
                'opportunity': opportunity,
                'product': product,
                'quantity': quantity
            })
            
        except Exception as e:
            _logger.error(f"Error creando oportunidad desde solicitud de cotización: {str(e)}")
            return request.render('website.404')
    
    @http.route('/newsletter/subscribe', type='json', auth='public', website=True)
    def newsletter_subscribe(self, email, name=None):
        """
        Suscribir a newsletter y crear lead de bajo valor
        
        @param email: Email del suscriptor
        @param name: Nombre (opcional)
        @return: dict con status y mensaje
        """
        try:
            # Validar email
            if not email or '@' not in email:
                return {'status': 'error', 'message': 'Email inválido'}
            
            # Buscar si ya existe contacto con este email
            existing_partner = request.env['res.partner'].sudo().search([
                ('email', '=', email)
            ], limit=1)
            
            if existing_partner:
                # Ya existe, solo suscribir a mailing list
                mailing_list = request.env.ref('website_crm_lead_capture.mailing_list_newsletter', raise_if_not_found=False)
                if mailing_list:
                    request.env['mailing.contact'].sudo().create({
                        'name': existing_partner.name,
                        'email': email,
                        'list_ids': [(4, mailing_list.id)],
                    })
                return {'status': 'success', 'message': '¡Suscripción exitosa!'}
            
            # Crear nuevo lead
            lead_vals = {
                'name': f"Web - Newsletter: {name or email}",
                'contact_name': name or '',
                'email_from': email,
                'type': 'lead',
                'source_id': self._get_or_create_utm_source('website'),
                'medium_id': self._get_or_create_utm_medium('newsletter'),
                'team_id': self._get_sales_team_id(),
                'priority': '0',
                'description': 'Suscrito a newsletter desde website'
            }
            
            lead = request.env['crm.lead'].sudo().create(lead_vals)
            _logger.info(f"Lead creado desde newsletter: {lead.id}")
            
            # Agregar a lista de correo
            mailing_list = request.env.ref('website_crm_lead_capture.mailing_list_newsletter', raise_if_not_found=False)
            if mailing_list:
                request.env['mailing.contact'].sudo().create({
                    'name': name or email,
                    'email': email,
                    'list_ids': [(4, mailing_list.id)],
                })
            
            return {'status': 'success', 'message': '¡Gracias por suscribirte!'}
            
        except Exception as e:
            _logger.error(f"Error en suscripción a newsletter: {str(e)}")
            return {'status': 'error', 'message': 'Ocurrió un error. Intenta nuevamente.'}
    
    # ========== Métodos auxiliares ==========
    
    def _get_or_create_utm_source(self, source_name):
        """Obtener o crear UTM Source"""
        utm_source = request.env['utm.source'].sudo().search([
            ('name', '=', source_name)
        ], limit=1)
        
        if not utm_source:
            utm_source = request.env['utm.source'].sudo().create({
                'name': source_name
            })
        
        return utm_source.id
    
    def _get_or_create_utm_medium(self, medium_name):
        """Obtener o crear UTM Medium"""
        utm_medium = request.env['utm.medium'].sudo().search([
            ('name', '=', medium_name)
        ], limit=1)
        
        if not utm_medium:
            utm_medium = request.env['utm.medium'].sudo().create({
                'name': medium_name
            })
        
        return utm_medium.id
    
    def _get_or_create_utm_campaign(self, campaign_name):
        """Obtener o crear UTM Campaign"""
        utm_campaign = request.env['utm.campaign'].sudo().search([
            ('name', '=', campaign_name)
        ], limit=1)
        
        if not utm_campaign:
            utm_campaign = request.env['utm.campaign'].sudo().create({
                'name': campaign_name
            })
        
        return utm_campaign.id
    
    def _get_sales_team_id(self):
        """Obtener ID del equipo de ventas por defecto"""
        sales_team = request.env['crm.team'].sudo().search([
            ('use_leads', '=', True)
        ], limit=1)
        
        return sales_team.id if sales_team else False
    
    def _send_confirmation_email(self, lead):
        """Enviar email de confirmación al cliente"""
        try:
            template = request.env.ref('website_crm_lead_capture.email_template_contact_confirmation', raise_if_not_found=False)
            if template:
                template.sudo().send_mail(lead.id, force_send=True)
        except Exception as e:
            _logger.warning(f"No se pudo enviar email de confirmación: {str(e)}")
    
    def _send_quote_confirmation_email(self, opportunity, product, quantity):
        """Enviar email de confirmación de cotización"""
        try:
            template = request.env.ref('website_crm_lead_capture.email_template_quote_confirmation', raise_if_not_found=False)
            if template:
                # Pasar contexto adicional para el template
                ctx = {
                    'product': product,
                    'quantity': quantity,
                }
                template.sudo().with_context(ctx).send_mail(opportunity.id, force_send=True)
        except Exception as e:
            _logger.warning(f"No se pudo enviar email de confirmación de cotización: {str(e)}")
