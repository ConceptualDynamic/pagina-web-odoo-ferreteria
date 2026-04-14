# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ProductCategory(models.Model):
    """Extensión de categorías de productos para ferretería."""
    
    _inherit = 'product.category'

    # === CAMPOS SEO ===
    website_description = fields.Html(
        string='Descripción Web',
        translate=True,
        help='Texto introductorio para la página de categoría'
    )
    
    seo_title = fields.Char(
        string='Título SEO',
        translate=True,
        help='Título para motores de búsqueda (máx. 60 caracteres)'
    )
    
    seo_description = fields.Text(
        string='Meta Descripción SEO',
        translate=True,
        help='Descripción para motores de búsqueda (máx. 160 caracteres)'
    )
    
    # === CAMPOS VISUALES ===
    category_image = fields.Binary(
        string='Imagen de Categoría',
        attachment=True,
        help='Imagen principal para mostrar en el sitio web'
    )
    
    category_icon = fields.Char(
        string='Icono',
        help='Clase de icono (ej: fa-wrench, fa-bolt)'
    )
    
    banner_image = fields.Binary(
        string='Banner',
        attachment=True,
        help='Imagen de banner para la página de categoría'
    )
    
    # === CAMPOS DE NAVEGACIÓN ===
    is_featured = fields.Boolean(
        string='Destacada',
        default=False,
        help='Mostrar en la página principal'
    )
    
    display_order = fields.Integer(
        string='Orden de Visualización',
        default=10,
        help='Orden en menús y listados (menor = primero)'
    )
    
    show_in_mega_menu = fields.Boolean(
        string='Mostrar en Mega Menú',
        default=True,
        help='Incluir esta categoría en el mega menú de navegación'
    )
    
    # === CAMPOS DE ATRIBUTOS ===
    filter_attribute_ids = fields.Many2many(
        'product.attribute',
        'category_filter_attribute_rel',
        'category_id',
        'attribute_id',
        string='Atributos de Filtro',
        help='Atributos a mostrar como filtros en esta categoría'
    )
    
    # === CAMPOS COMPUTADOS ===
    product_count_website = fields.Integer(
        string='Productos Publicados',
        compute='_compute_product_count_website'
    )
    
    @api.depends('product_count')
    def _compute_product_count_website(self):
        """Cuenta productos publicados en el sitio web."""
        for category in self:
            category.product_count_website = self.env['product.template'].search_count([
                ('categ_id', 'child_of', category.id),
                ('website_published', '=', True),
            ])
    
    def get_subcategories_for_menu(self):
        """Obtiene subcategorías para mostrar en el menú."""
        self.ensure_one()
        return self.search([
            ('parent_id', '=', self.id),
            ('show_in_mega_menu', '=', True),
        ], order='display_order, name')
