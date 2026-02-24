# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    customer_type = fields.Selection([
        ('individual', 'Persona Natural'),
        ('company', 'Empresa'),
    ], string='Tipo de cliente', default='individual')
    
    coupon_code = fields.Char(string='Código de cupón')
    discount_amount = fields.Monetary(
        string='Descuento por cupón',
        compute='_compute_discount_amount',
        store=True
    )
    
    @api.depends('coupon_code', 'amount_untaxed')
    def _compute_discount_amount(self):
        """Calcular descuento basado en cupón"""
        for order in self:
            order.discount_amount = 0.0
            if order.coupon_code:
                # Buscar cupón válido
                # En implementación real, usar modelo de cupones
                # Por ahora, ejemplo simple
                if order.coupon_code == 'FERRETERIA10':
                    order.discount_amount = order.amount_untaxed * 0.10
                elif order.coupon_code == 'FERRETERIA20':
                    order.discount_amount = order.amount_untaxed * 0.20
    
    @api.constrains('order_line')
    def _check_stock_availability(self):
        """Verificar disponibilidad de stock antes de confirmar"""
        for order in self:
            for line in order.order_line:
                product = line.product_id
                if product.type == 'product':  # Solo productos almacenables
                    available_qty = product.qty_available - product.outgoing_qty
                    if available_qty < line.product_uom_qty:
                        raise ValidationError(
                            f'Stock insuficiente para {product.name}.\n'
                            f'Disponible: {available_qty:.0f} unidades\n'
                            f'Solicitado: {line.product_uom_qty:.0f} unidades'
                        )
    
    def _check_heavy_products(self):
        """Verificar si el pedido contiene productos pesados"""
        heavy_threshold = 30.0  # kg
        for line in self.order_line:
            if line.product_id.weight > heavy_threshold:
                return True
        return False
    
    def action_confirm(self):
        """Confirmar pedido con validaciones adicionales"""
        self._check_stock_availability()
        
        # Enviar email de confirmación personalizado
        for order in self:
            if order.state == 'draft':
                template = self.env.ref(
                    'ferreteria_checkout.email_template_order_confirmation',
                    raise_if_not_found=False
                )
                if template:
                    template.send_mail(order.id, force_send=True)
        
        return super(SaleOrder, self).action_confirm()
    
    def _get_delivery_methods(self):
        """Filtrar métodos de envío según características del pedido"""
        methods = super()._get_delivery_methods()
        
        # Si hay productos muy pesados, solo permitir retiro en tienda
        if self._check_heavy_products():
            methods = methods.filtered(
                lambda m: m.delivery_type == 'fixed' and m.fixed_price == 0
            )
        
        return methods
