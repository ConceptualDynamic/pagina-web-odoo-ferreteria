# -*- coding: utf-8 -*-

from odoo import fields, models


class PaymentProvider(models.Model):
    _inherit = 'payment.provider'
    
    code = fields.Selection(
        selection_add=[('store_payment', 'Pago en tienda')],
        ondelete={'store_payment': 'set default'}
    )
    
    store_instructions = fields.Html(
        string='Instrucciones para pago en tienda',
        help='Mensaje que verá el cliente al seleccionar pago en tienda'
    )
