# -*- coding: utf-8 -*-
{
    'name': 'Ferretería Website',
    'version': '17.0.1.0.0',
    'category': 'Website/Website',
    'summary': 'Tienda online de ferretería con catálogo técnico y checkout optimizado',
    'description': """
Ferretería Website - Módulo de eCommerce
========================================

Este módulo implementa una tienda online de ferretería con las siguientes características:

**Catálogo de Productos:**
- Categorías técnicas (herramientas, tornillería, pintura, etc.)
- Filtros avanzados por marca, precio, potencia
- Fichas técnicas detalladas
- Búsqueda con sinónimos

**eCommerce:**
- Carrito y checkout optimizado
- Múltiples métodos de pago
- Envío a domicilio y retiro en tienda
- Cálculo de impuestos

**SEO y Marketing:**
- URLs amigables
- Metadatos optimizados
- Integración con Google Analytics 4
- WhatsApp para contacto

**Páginas Institucionales:**
- Nosotros
- Contacto
- FAQ
- Políticas
    """,
    'author': 'Conceptual Dynamic',
    'website': 'https://github.com/ConceptualDynamic/pagina-web-odoo-ferreteria',
    'license': 'LGPL-3',
    'depends': [
        'website',
        'website_sale',
        'website_sale_stock',
        'sale_management',
        'stock',
        'contacts',
        'crm',
        'website_crm',
    ],
    'data': [
        # Security
        'security/ferreteria_security.xml',
        'security/ir.model.access.csv',
        # Data
        'data/product_category_data.xml',
        'data/product_attribute_data.xml',
        'data/website_menu_data.xml',
        # Views
        'views/product_template_views.xml',
        'views/website_snippets.xml',
        # Templates
        'templates/website_templates.xml',
        'templates/product_templates.xml',
        'templates/checkout_templates.xml',
        'templates/page_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'ferreteria_website/static/src/css/ferreteria.css',
            'ferreteria_website/static/src/js/ferreteria.js',
        ],
    },
    'demo': [],
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
