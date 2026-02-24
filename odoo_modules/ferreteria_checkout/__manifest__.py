# -*- coding: utf-8 -*-
{
    'name': 'Ferretería - Checkout Personalizado',
    'version': '16.0.1.0.0',
    'category': 'Website/Website',
    'summary': 'Personalización del proceso de checkout para ferretería',
    'description': """
        Módulo personalizado para el checkout de la ferretería online.
        
        Características:
        * Validación de stock en tiempo real
        * Campos adicionales para tipo de cliente y documento
        * Método de pago "Pago en tienda"
        * Cálculo de descuentos por volumen
        * Restricciones de envío por tipo de producto
        * Emails personalizados de confirmación
        * Integración con transportistas locales
    """,
    'author': 'Conceptual Dynamic',
    'website': 'https://github.com/ConceptualDynamic/pagina-web-odoo-ferreteria',
    'license': 'LGPL-3',
    'depends': [
        'website_sale',
        'sale_management',
        'stock',
        'delivery',
        'payment',
        'account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/email_templates.xml',
        'data/payment_provider_data.xml',
        'data/delivery_carrier_data.xml',
        'views/checkout_templates.xml',
        'views/payment_templates.xml',
        'views/sale_order_views.xml',
        'views/product_template_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'ferreteria_checkout/static/src/js/checkout_validation.js',
            'ferreteria_checkout/static/src/css/checkout.css',
        ],
    },
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
