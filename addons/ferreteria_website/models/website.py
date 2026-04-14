# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Website(models.Model):
    """Extensión del modelo Website para configuraciones de ferretería."""
    
    _inherit = 'website'

    # === CONFIGURACIÓN DE CONTACTO ===
    whatsapp_number = fields.Char(
        string='Número WhatsApp',
        help='Número de WhatsApp para contacto (incluir código de país, ej: +521234567890)'
    )
    
    whatsapp_message = fields.Char(
        string='Mensaje Inicial WhatsApp',
        default='Hola, me interesa información sobre sus productos.',
        help='Mensaje predeterminado al abrir WhatsApp'
    )
    
    show_whatsapp_button = fields.Boolean(
        string='Mostrar Botón WhatsApp',
        default=True,
        help='Mostrar botón flotante de WhatsApp'
    )
    
    # === CONFIGURACIÓN DE TIENDA ===
    store_phone = fields.Char(
        string='Teléfono de Tienda'
    )
    
    store_email = fields.Char(
        string='Email de Tienda'
    )
    
    store_address = fields.Text(
        string='Dirección de Tienda'
    )
    
    store_hours = fields.Text(
        string='Horario de Atención',
        help='Horario de atención al cliente'
    )
    
    # === CONFIGURACIÓN DE ENVÍO ===
    free_shipping_threshold = fields.Float(
        string='Umbral de Envío Gratis',
        default=0.0,
        help='Monto mínimo de compra para envío gratuito (0 = sin envío gratis)'
    )
    
    pickup_available = fields.Boolean(
        string='Retiro en Tienda Disponible',
        default=True,
        help='Permitir retiro en tienda física'
    )
    
    # === CONFIGURACIÓN SEO ===
    ga4_measurement_id = fields.Char(
        string='GA4 Measurement ID',
        help='ID de medición de Google Analytics 4 (ej: G-XXXXXXXXXX)'
    )
    
    gtm_container_id = fields.Char(
        string='GTM Container ID',
        help='ID del contenedor de Google Tag Manager (ej: GTM-XXXXXXX)'
    )
    
    # === CONFIGURACIÓN VISUAL ===
    primary_color = fields.Char(
        string='Color Primario',
        default='#FF6B00',
        help='Color primario de la marca (hexadecimal)'
    )
    
    secondary_color = fields.Char(
        string='Color Secundario',
        default='#1E3A5F',
        help='Color secundario de la marca (hexadecimal)'
    )
    
    accent_color = fields.Char(
        string='Color de Acento',
        default='#28A745',
        help='Color de acento para CTAs (hexadecimal)'
    )

    def get_whatsapp_url(self, message=None):
        """Genera la URL de WhatsApp para el botón de contacto."""
        self.ensure_one()
        if not self.whatsapp_number:
            return False
        
        number = self.whatsapp_number.replace('+', '').replace(' ', '').replace('-', '')
        msg = message or self.whatsapp_message or ''
        
        from urllib.parse import quote
        return f'https://wa.me/{number}?text={quote(msg)}'
    
    def get_featured_categories(self, limit=8):
        """Obtiene las categorías destacadas para la página principal."""
        self.ensure_one()
        return self.env['product.category'].search([
            ('is_featured', '=', True),
            ('parent_id', '!=', False),  # Solo subcategorías
        ], order='display_order, name', limit=limit)
    
    def get_featured_brands(self, limit=12):
        """Obtiene las marcas destacadas para la página principal."""
        self.ensure_one()
        return self.env['product.brand'].search([
            ('is_featured', '=', True),
        ], order='name', limit=limit)
