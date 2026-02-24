# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class FerreteriaCheckout(WebsiteSale):
    
    @http.route(['/shop/checkout'], type='http', auth="public", website=True, sitemap=False)
    def checkout(self, **post):
        """Extender checkout con validaciones personalizadas"""
        order = request.website.sale_get_order()
        
        # Verificar stock antes de mostrar checkout
        if order:
            try:
                order._check_stock_availability()
            except Exception as e:
                request.session['sale_last_order_id'] = None
                return request.redirect('/shop/cart?error=stock_unavailable')
        
        return super(FerreteriaCheckout, self).checkout(**post)
    
    @http.route(['/shop/apply_coupon'], type='json', auth="public", methods=['POST'], website=True)
    def apply_coupon(self, coupon_code):
        """Aplicar código de cupón"""
        order = request.website.sale_get_order()
        if not order:
            return {'error': 'No hay pedido activo'}
        
        # Validar y aplicar cupón
        order.coupon_code = coupon_code
        order._compute_discount_amount()
        
        if order.discount_amount > 0:
            return {
                'success': True,
                'discount': order.discount_amount,
                'message': f'Cupón aplicado: descuento de ${order.discount_amount:,.0f}'
            }
        else:
            return {
                'success': False,
                'message': 'Cupón inválido o expirado'
            }
    
    @http.route(['/shop/check_delivery_availability'], type='json', auth="public", methods=['POST'], website=True)
    def check_delivery_availability(self, address_data):
        """Verificar disponibilidad de envío a dirección específica"""
        order = request.website.sale_get_order()
        if not order:
            return {'available': False, 'message': 'No hay pedido activo'}
        
        # Verificar si hay productos pesados
        if order._check_heavy_products():
            return {
                'available': True,
                'methods': ['pickup'],
                'message': 'Su pedido contiene productos pesados. Solo disponible retiro en tienda.'
            }
        
        # En producción, aquí se integraría con API de transportista
        # para verificar cobertura de zona
        return {
            'available': True,
            'methods': ['pickup', 'standard', 'express'],
            'message': 'Todos los métodos de envío disponibles'
        }
