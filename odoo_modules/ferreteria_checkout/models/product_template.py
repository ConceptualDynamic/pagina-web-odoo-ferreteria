# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    is_heavy_product = fields.Boolean(
        string='Producto pesado',
        compute='_compute_is_heavy',
        store=True,
        help='Se marca automáticamente si el peso supera 30kg'
    )
    
    shipping_restrictions = fields.Selection([
        ('none', 'Sin restricciones'),
        ('pickup_only', 'Solo retiro en tienda'),
        ('special_handling', 'Requiere manejo especial'),
        ('fragile', 'Frágil'),
        ('hazardous', 'Material peligroso'),
    ], string='Restricciones de envío', default='none')
    
    @api.depends('weight')
    def _compute_is_heavy(self):
        """Marcar productos pesados automáticamente"""
        for product in self:
            product.is_heavy_product = product.weight > 30.0
