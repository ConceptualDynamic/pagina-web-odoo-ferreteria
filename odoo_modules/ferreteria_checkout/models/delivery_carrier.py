# -*- coding: utf-8 -*-

from odoo import api, fields, models


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'
    
    requires_heavy_handling = fields.Boolean(
        string='Requiere manejo especial',
        help='Marcar si este método de envío puede manejar productos pesados'
    )
    
    max_weight = fields.Float(
        string='Peso máximo (kg)',
        help='Peso máximo que puede transportar este método'
    )
    
    preparation_time = fields.Float(
        string='Tiempo de preparación (horas)',
        help='Tiempo estimado de preparación del pedido',
        default=2.0
    )
    
    @api.model
    def _get_available_carriers(self, order):
        """Filtrar transportistas según características del pedido"""
        carriers = super()._get_available_carriers(order)
        
        # Calcular peso total del pedido
        total_weight = sum(line.product_id.weight * line.product_uom_qty 
                          for line in order.order_line)
        
        # Filtrar por peso máximo
        available_carriers = carriers.filtered(
            lambda c: not c.max_weight or c.max_weight >= total_weight
        )
        
        return available_carriers
