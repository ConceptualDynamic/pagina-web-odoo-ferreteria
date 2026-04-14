# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    """Extensión del modelo de productos para ferretería."""
    
    _inherit = 'product.template'

    # === CAMPOS TÉCNICOS ===
    technical_specs = fields.Html(
        string='Especificaciones Técnicas',
        translate=True,
        help='Especificaciones técnicas detalladas del producto'
    )
    
    short_description = fields.Text(
        string='Descripción Corta',
        translate=True,
        help='Descripción breve para listados (máx. 160 caracteres)'
    )
    
    # === CAMPOS DE MARCA ===
    brand_id = fields.Many2one(
        'product.brand',
        string='Marca',
        help='Marca del producto'
    )
    
    model_name = fields.Char(
        string='Modelo',
        help='Número de modelo del fabricante'
    )
    
    # === CAMPOS DE LOGÍSTICA ===
    package_weight = fields.Float(
        string='Peso del Paquete (kg)',
        help='Peso total incluyendo empaque'
    )
    
    package_length = fields.Float(
        string='Largo del Paquete (cm)'
    )
    
    package_width = fields.Float(
        string='Ancho del Paquete (cm)'
    )
    
    package_height = fields.Float(
        string='Alto del Paquete (cm)'
    )
    
    # === CAMPOS SEO ===
    seo_keywords = fields.Char(
        string='Palabras Clave SEO',
        help='Palabras clave separadas por coma para SEO'
    )
    
    # === CAMPOS DE GARANTÍA ===
    warranty_months = fields.Integer(
        string='Garantía (meses)',
        default=12,
        help='Período de garantía en meses'
    )
    
    warranty_description = fields.Text(
        string='Descripción de Garantía',
        translate=True
    )
    
    # === CAMPOS DE USO ===
    recommended_use = fields.Selection([
        ('home', 'Hogar'),
        ('professional', 'Profesional'),
        ('industrial', 'Industrial'),
        ('all', 'Todos los usos'),
    ], string='Uso Recomendado', default='all')
    
    # === CAMPOS DE COMPATIBILIDAD ===
    compatible_product_ids = fields.Many2many(
        'product.template',
        'product_compatibility_rel',
        'product_id',
        'compatible_id',
        string='Productos Compatibles',
        help='Productos compatibles o accesorios relacionados'
    )
    
    # === CAMPOS DE DOCUMENTACIÓN ===
    datasheet_url = fields.Char(
        string='URL Ficha Técnica',
        help='Enlace a ficha técnica PDF'
    )
    
    manual_url = fields.Char(
        string='URL Manual',
        help='Enlace a manual de usuario PDF'
    )
    
    # === CAMPOS COMPUTADOS ===
    has_complete_data = fields.Boolean(
        string='Datos Completos',
        compute='_compute_has_complete_data',
        store=True,
        help='Indica si el producto tiene todos los datos mínimos para publicación'
    )
    
    @api.depends('name', 'list_price', 'categ_id', 'image_1920', 'short_description')
    def _compute_has_complete_data(self):
        """Verifica si el producto tiene los datos mínimos para publicación."""
        for product in self:
            product.has_complete_data = all([
                product.name,
                product.list_price > 0,
                product.categ_id,
                product.image_1920,
                product.short_description,
            ])
    
    @api.constrains('short_description')
    def _check_short_description_length(self):
        """Valida que la descripción corta no exceda 160 caracteres."""
        for product in self:
            if product.short_description and len(product.short_description) > 160:
                raise ValidationError(
                    _('La descripción corta no debe exceder 160 caracteres. '
                      'Longitud actual: %s') % len(product.short_description)
                )
    
    def action_check_catalog_quality(self):
        """Acción para verificar la calidad de los datos del catálogo."""
        incomplete_products = self.filtered(lambda p: not p.has_complete_data)
        if incomplete_products:
            return {
                'type': 'ir.actions.act_window',
                'name': _('Productos con Datos Incompletos'),
                'res_model': 'product.template',
                'view_mode': 'tree,form',
                'domain': [('id', 'in', incomplete_products.ids)],
                'context': {'search_default_filter_incomplete': 1},
            }
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Catálogo Completo'),
                'message': _('Todos los productos tienen datos completos.'),
                'type': 'success',
                'sticky': False,
            }
        }


class ProductBrand(models.Model):
    """Modelo para marcas de productos."""
    
    _name = 'product.brand'
    _description = 'Marca de Producto'
    _order = 'name'

    name = fields.Char(
        string='Nombre',
        required=True,
        translate=True
    )
    
    code = fields.Char(
        string='Código',
        help='Código interno de la marca'
    )
    
    logo = fields.Binary(
        string='Logo',
        attachment=True
    )
    
    description = fields.Text(
        string='Descripción',
        translate=True
    )
    
    website_url = fields.Char(
        string='Sitio Web',
        help='URL del sitio web oficial de la marca'
    )
    
    is_featured = fields.Boolean(
        string='Destacada',
        default=False,
        help='Mostrar en sección de marcas destacadas'
    )
    
    product_count = fields.Integer(
        string='Productos',
        compute='_compute_product_count'
    )
    
    active = fields.Boolean(
        string='Activo',
        default=True
    )

    def _compute_product_count(self):
        """Calcula el número de productos por marca."""
        for brand in self:
            brand.product_count = self.env['product.template'].search_count([
                ('brand_id', '=', brand.id)
            ])
    
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'El nombre de la marca debe ser único.'),
    ]
