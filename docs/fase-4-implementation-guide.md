# Guía de Implementación - PLP y PDP en Odoo

## Objetivo
Esta guía proporciona los pasos técnicos para implementar los diseños de PLP (Product Listing Page) y PDP (Product Detail Page) en Odoo, siguiendo las especificaciones detalladas en `fase-4-plp-design.md` y `fase-4-pdp-design.md`.

## Pre-requisitos

### Módulos Odoo Necesarios
```python
# En el archivo __manifest__.py del módulo personalizado
{
    'depends': [
        'website',                    # Base del sitio web
        'website_sale',              # E-commerce
        'website_sale_wishlist',     # Lista de deseos
        'website_sale_comparison',   # Comparación de productos
        'stock',                     # Gestión de inventario
        'portal_rating',             # Sistema de reseñas
        'delivery',                  # Información de envíos
    ],
}
```

### Estructura de Archivos del Módulo
```
ferreteria_theme/
├── __init__.py
├── __manifest__.py
├── controllers/
│   ├── __init__.py
│   └── main.py                  # Controladores personalizados
├── models/
│   ├── __init__.py
│   └── product_template.py      # Extensiones del modelo
├── static/
│   ├── src/
│   │   ├── js/
│   │   │   ├── plp.js          # JavaScript para PLP
│   │   │   └── pdp.js          # JavaScript para PDP
│   │   ├── scss/
│   │   │   ├── plp.scss        # Estilos PLP
│   │   │   └── pdp.scss        # Estilos PDP
│   │   └── xml/
│   │       └── assets.xml       # Declaración de assets
│   └── description/
│       └── icon.png
├── views/
│   ├── templates.xml            # Templates base
│   ├── plp_templates.xml        # Templates PLP
│   └── pdp_templates.xml        # Templates PDP
└── data/
    └── product_attributes.xml   # Atributos predefinidos
```

## Implementación PLP (Product Listing Page)

### 1. Template Base QWeb

**Archivo**: `views/plp_templates.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <!-- Override del template principal de la tienda -->
    <template id="products" inherit_id="website_sale.products" name="Product Listing - Ferreteria">
        
        <!-- Breadcrumb mejorado -->
        <xpath expr="//div[@id='o_shop_collapse_category']" position="before">
            <nav aria-label="breadcrumb" class="breadcrumb-custom">
                <ol class="breadcrumb">
                    <li class="breadcrumb-item">
                        <a href="/">Inicio</a>
                    </li>
                    <t t-if="category">
                        <t t-foreach="category.parent_path.split('/')[:-1]" t-as="parent_id">
                            <t t-set="parent_cat" t-value="request.env['product.public.category'].browse(int(parent_id))"/>
                            <li class="breadcrumb-item">
                                <a t-att-href="'/shop/category/%s' % slug(parent_cat)">
                                    <t t-esc="parent_cat.name"/>
                                </a>
                            </li>
                        </t>
                        <li class="breadcrumb-item active" aria-current="page">
                            <t t-esc="category.name"/>
                        </li>
                    </t>
                    <t t-else="">
                        <li class="breadcrumb-item active" aria-current="page">
                            Productos
                        </li>
                    </t>
                </ol>
            </nav>
        </xpath>

        <!-- Toolbar personalizado -->
        <xpath expr="//form[@class='js_attributes']" position="replace">
            <div class="shop-toolbar d-flex justify-content-between align-items-center mb-3">
                <!-- Contador de resultados -->
                <div class="toolbar-left">
                    <span class="product-count">
                        Mostrando <strong t-esc="pager['offset_start']"/> - 
                        <strong t-esc="pager['offset_end']"/> de 
                        <strong t-esc="pager['product_count']"/> productos
                    </span>
                </div>

                <!-- Controles de vista y orden -->
                <div class="toolbar-right d-flex align-items-center">
                    <!-- Vista Grid/List -->
                    <div class="btn-group view-mode mr-3" role="group">
                        <button type="button" class="btn btn-light active" data-view="grid">
                            <i class="fa fa-th"></i>
                        </button>
                        <button type="button" class="btn btn-light" data-view="list">
                            <i class="fa fa-list"></i>
                        </button>
                    </div>

                    <!-- Ordenamiento -->
                    <select name="order" class="form-control sort-select">
                        <option value="">Relevancia</option>
                        <option value="list_price asc">Precio: Menor a Mayor</option>
                        <option value="list_price desc">Precio: Mayor a Menor</option>
                        <option value="name asc">Nombre: A-Z</option>
                        <option value="name desc">Nombre: Z-A</option>
                        <option value="create_date desc">Más Nuevos</option>
                    </select>
                </div>
            </div>
        </xpath>

        <!-- Filtros activos (chips) -->
        <xpath expr="//div[@id='products_grid_before']" position="inside">
            <div class="active-filters mb-3" t-if="attrib_values or search">
                <span class="mr-2">Filtros activos:</span>
                <t t-foreach="attrib_values" t-as="attrib">
                    <span class="badge badge-primary mr-1">
                        <t t-esc="attrib.name"/>
                        <a t-att-href="'/shop?'+keep('/shop', attrib=attrib_values-attrib)" 
                           class="close ml-1">×</a>
                    </span>
                </t>
                <t t-if="search">
                    <span class="badge badge-primary mr-1">
                        Búsqueda: <t t-esc="search"/>
                        <a href="/shop" class="close ml-1">×</a>
                    </span>
                </t>
                <a href="/shop" class="btn btn-sm btn-link">Limpiar todo</a>
            </div>
        </xpath>

        <!-- Tarjeta de producto mejorada -->
        <xpath expr="//div[hasclass('oe_product_cart')]" position="replace">
            <div class="oe_product_cart product-card">
                <!-- Imagen con badges -->
                <div class="product-img-container">
                    <t t-set="product_image" t-value="product.image_1920"/>
                    <a t-att-href="'/shop/product/%s' % slug(product)">
                        <img t-att-src="image_data_uri(product_image)" 
                             t-att-alt="product.name"
                             class="img-fluid product-image"/>
                    </a>
                    
                    <!-- Badges -->
                    <div class="product-badges">
                        <span t-if="product.website_ribbon_id" 
                              class="badge badge-danger">
                            <t t-esc="product.website_ribbon_id.name"/>
                        </span>
                        <span t-if="not product.qty_available" 
                              class="badge badge-secondary">
                            Agotado
                        </span>
                    </div>

                    <!-- Botón favoritos -->
                    <button class="btn btn-wishlist" 
                            t-att-data-product-id="product.id">
                        <i class="fa fa-heart-o"></i>
                    </button>
                </div>

                <!-- Información del producto -->
                <div class="product-info">
                    <!-- Marca -->
                    <div class="product-brand text-muted small" 
                         t-if="product.product_brand_id">
                        <t t-esc="product.product_brand_id.name"/>
                    </div>

                    <!-- Nombre -->
                    <h6 class="product-name">
                        <a t-att-href="'/shop/product/%s' % slug(product)" 
                           t-field="product.name"/>
                    </h6>

                    <!-- SKU -->
                    <div class="product-sku text-muted small">
                        SKU: <t t-esc="product.default_code or 'N/A'"/>
                    </div>

                    <!-- Precio -->
                    <div class="product-price">
                        <t t-if="product.lst_price != product.list_price">
                            <span class="text-muted text-decoration-line-through mr-2">
                                <t t-esc="product.lst_price" 
                                   t-options="{'widget': 'monetary', 'display_currency': website.currency_id}"/>
                            </span>
                        </t>
                        <span class="price font-weight-bold">
                            <t t-esc="product.list_price" 
                               t-options="{'widget': 'monetary', 'display_currency': website.currency_id}"/>
                        </span>
                    </div>

                    <!-- Rating -->
                    <div class="product-rating" t-if="product.rating_count">
                        <t t-call="portal_rating.rating_stars_static">
                            <t t-set="rating_avg" t-value="product.rating_avg"/>
                        </t>
                        <span class="rating-count text-muted small">
                            (<t t-esc="product.rating_count"/>)
                        </span>
                    </div>

                    <!-- Botón CTA -->
                    <div class="product-actions mt-2">
                        <t t-if="product.qty_available > 0">
                            <button class="btn btn-primary btn-block add-to-cart" 
                                    t-att-data-product-id="product.id">
                                <i class="fa fa-shopping-cart mr-1"></i>
                                Agregar al carrito
                            </button>
                        </t>
                        <t t-else="">
                            <button class="btn btn-secondary btn-block" disabled="">
                                Consultar disponibilidad
                            </button>
                        </t>
                    </div>
                </div>
            </div>
        </xpath>

    </template>

    <!-- Sidebar de filtros mejorado -->
    <template id="products_categories" inherit_id="website_sale.products_categories">
        <xpath expr="//div[@id='o_shop_collapse_category']" position="attributes">
            <attribute name="class">filter-sidebar</attribute>
        </xpath>

        <!-- Añadir contador de productos por categoría -->
        <xpath expr="//li[hasclass('nav-item')]/a" position="attributes">
            <attribute name="t-attf-class">
                nav-link #{category.id in categories.ids and 'active' or ''}
            </attribute>
        </xpath>
    </template>

</odoo>
```

### 2. Controlador Personalizado

**Archivo**: `controllers/main.py`

```python
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleFerreteria(WebsiteSale):
    
    @http.route([
        '/shop',
        '/shop/page/<int:page>',
        '/shop/category/<model("product.public.category"):category>',
        '/shop/category/<model("product.public.category"):category>/page/<int:page>'
    ], type='http', auth="public", website=True)
    def shop(self, page=0, category=None, search='', ppg=24, **post):
        """
        Override del método shop para añadir funcionalidad personalizada
        """
        # Llamar al método padre
        response = super(WebsiteSaleFerreteria, self).shop(
            page=page, 
            category=category, 
            search=search, 
            ppg=ppg, 
            **post
        )
        
        # Añadir datos adicionales al contexto
        if hasattr(response, 'qcontext'):
            values = response.qcontext
            
            # Añadir información de filtros disponibles
            values.update({
                'price_range': self._get_price_range(category, search, **post),
                'available_brands': self._get_available_brands(category, search, **post),
            })
        
        return response
    
    def _get_price_range(self, category=None, search='', **post):
        """Obtener rango de precios para filtros"""
        domain = self._get_search_domain(search, category, **post)
        products = request.env['product.template'].search(domain)
        
        if products:
            prices = products.mapped('list_price')
            return {
                'min': min(prices),
                'max': max(prices)
            }
        return {'min': 0, 'max': 0}
    
    def _get_available_brands(self, category=None, search='', **post):
        """Obtener marcas disponibles con contador de productos"""
        domain = self._get_search_domain(search, category, **post)
        products = request.env['product.template'].search(domain)
        
        brands = {}
        for product in products:
            if product.product_brand_id:
                brand_id = product.product_brand_id.id
                brand_name = product.product_brand_id.name
                if brand_id not in brands:
                    brands[brand_id] = {
                        'id': brand_id,
                        'name': brand_name,
                        'count': 0
                    }
                brands[brand_id]['count'] += 1
        
        return sorted(brands.values(), key=lambda x: x['count'], reverse=True)
    
    @http.route(['/shop/cart/add'], type='json', auth="public", website=True)
    def cart_add(self, product_id, qty=1, **kwargs):
        """
        Agregar producto al carrito con feedback mejorado
        """
        result = super(WebsiteSaleFerreteria, self).cart_add(
            product_id=product_id, 
            qty=qty, 
            **kwargs
        )
        
        # Añadir información del producto para feedback
        product = request.env['product.product'].browse(int(product_id))
        result.update({
            'product_name': product.name,
            'product_image': f'/web/image/product.product/{product_id}/image_128',
            'qty_added': qty,
        })
        
        return result
```

### 3. Estilos SCSS

**Archivo**: `static/src/scss/plp.scss`

```scss
// Variables
$primary-color: #007bff;
$grid-gap: 20px;
$card-shadow: 0 2px 8px rgba(0,0,0,0.1);
$card-shadow-hover: 0 4px 16px rgba(0,0,0,0.15);

// Breadcrumb
.breadcrumb-custom {
    padding: 1rem 0;
    background: transparent;
    
    .breadcrumb {
        background: transparent;
        padding: 0;
        margin: 0;
        
        .breadcrumb-item {
            &.active {
                color: #6c757d;
            }
            
            a {
                color: $primary-color;
                text-decoration: none;
                
                &:hover {
                    text-decoration: underline;
                }
            }
        }
    }
}

// Toolbar
.shop-toolbar {
    padding: 1rem;
    background: #f8f9fa;
    border-radius: 4px;
    margin-bottom: 1.5rem;
    
    .product-count {
        font-size: 0.95rem;
    }
    
    .view-mode {
        .btn {
            border-color: #dee2e6;
            
            &.active {
                background-color: $primary-color;
                color: white;
            }
        }
    }
    
    .sort-select {
        width: auto;
        min-width: 200px;
    }
}

// Filtros activos
.active-filters {
    .badge {
        padding: 0.5rem 0.75rem;
        font-size: 0.875rem;
        
        .close {
            color: white;
            opacity: 0.8;
            text-decoration: none;
            
            &:hover {
                opacity: 1;
            }
        }
    }
}

// Sidebar de filtros
.filter-sidebar {
    .card {
        margin-bottom: 1rem;
        border: 1px solid #dee2e6;
        
        .card-header {
            background: #f8f9fa;
            font-weight: 600;
            cursor: pointer;
            
            &:hover {
                background: #e9ecef;
            }
        }
    }
    
    .form-check {
        padding: 0.5rem 0;
        
        .form-check-label {
            display: flex;
            justify-content: space-between;
            width: 100%;
            cursor: pointer;
            
            .count {
                color: #6c757d;
                font-size: 0.875rem;
            }
        }
    }
}

// Grid de productos
#products_grid {
    &.view-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
        gap: $grid-gap;
    }
    
    &.view-list {
        .product-card {
            display: flex;
            flex-direction: row;
            
            .product-img-container {
                flex: 0 0 150px;
            }
            
            .product-info {
                flex: 1;
                padding-left: 1rem;
            }
        }
    }
}

// Tarjeta de producto
.product-card {
    background: white;
    border: 1px solid #dee2e6;
    border-radius: 8px;
    overflow: hidden;
    transition: all 0.3s ease;
    
    &:hover {
        box-shadow: $card-shadow-hover;
        transform: translateY(-4px);
        
        .product-image {
            transform: scale(1.05);
        }
    }
    
    .product-img-container {
        position: relative;
        overflow: hidden;
        background: #f8f9fa;
        aspect-ratio: 1;
        
        .product-image {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.3s ease;
        }
        
        .product-badges {
            position: absolute;
            top: 10px;
            left: 10px;
            display: flex;
            flex-direction: column;
            gap: 5px;
            
            .badge {
                padding: 0.35rem 0.6rem;
                font-size: 0.75rem;
            }
        }
        
        .btn-wishlist {
            position: absolute;
            top: 10px;
            right: 10px;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background: white;
            border: none;
            box-shadow: $card-shadow;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s ease;
            
            &:hover {
                background: $primary-color;
                color: white;
            }
            
            &.active {
                background: $primary-color;
                color: white;
                
                .fa-heart-o::before {
                    content: "\f004"; // fa-heart
                }
            }
        }
    }
    
    .product-info {
        padding: 1rem;
        
        .product-brand {
            margin-bottom: 0.25rem;
            font-size: 0.875rem;
        }
        
        .product-name {
            margin-bottom: 0.5rem;
            font-size: 1rem;
            line-height: 1.3;
            height: 2.6em;
            overflow: hidden;
            
            a {
                color: #212529;
                text-decoration: none;
                
                &:hover {
                    color: $primary-color;
                }
            }
        }
        
        .product-sku {
            margin-bottom: 0.75rem;
            font-size: 0.8125rem;
        }
        
        .product-price {
            margin-bottom: 0.5rem;
            
            .price {
                font-size: 1.5rem;
                color: #212529;
            }
        }
        
        .product-rating {
            margin-bottom: 0.75rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .product-actions {
            .add-to-cart {
                font-size: 0.875rem;
                padding: 0.5rem;
                transition: all 0.2s ease;
                
                &:hover {
                    transform: scale(1.02);
                }
            }
        }
    }
}

// Responsive
@media (max-width: 768px) {
    #products_grid.view-grid {
        grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
        gap: 15px;
    }
    
    .shop-toolbar {
        flex-direction: column;
        gap: 1rem;
        
        .toolbar-left,
        .toolbar-right {
            width: 100%;
        }
    }
}
```

### 4. JavaScript

**Archivo**: `static/src/js/plp.js`

```javascript
odoo.define('ferreteria_theme.plp', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');
    var core = require('web.core');
    var ajax = require('web.ajax');

    var _t = core._t;

    publicWidget.registry.ProductListingPage = publicWidget.Widget.extend({
        selector: '.oe_website_sale',
        events: {
            'click .view-mode .btn': '_onViewModeChange',
            'click .add-to-cart': '_onAddToCart',
            'click .btn-wishlist': '_onToggleWishlist',
            'change .sort-select': '_onSortChange',
        },

        /**
         * @override
         */
        start: function () {
            this._super.apply(this, arguments);
            this._initializeView();
        },

        /**
         * Initialize default view
         */
        _initializeView: function () {
            var savedView = localStorage.getItem('plp_view_mode') || 'grid';
            this._setViewMode(savedView);
        },

        /**
         * Handle view mode change (grid/list)
         */
        _onViewModeChange: function (ev) {
            ev.preventDefault();
            var $btn = $(ev.currentTarget);
            var viewMode = $btn.data('view');
            
            this._setViewMode(viewMode);
            localStorage.setItem('plp_view_mode', viewMode);
        },

        /**
         * Set view mode
         */
        _setViewMode: function (mode) {
            var $grid = $('#products_grid');
            var $buttons = $('.view-mode .btn');
            
            $buttons.removeClass('active');
            $('.view-mode .btn[data-view="' + mode + '"]').addClass('active');
            
            $grid.removeClass('view-grid view-list').addClass('view-' + mode);
        },

        /**
         * Handle add to cart
         */
        _onAddToCart: function (ev) {
            ev.preventDefault();
            var $btn = $(ev.currentTarget);
            var productId = $btn.data('product-id');
            
            // Disable button
            $btn.prop('disabled', true).html('<i class="fa fa-spinner fa-spin"></i>');
            
            ajax.jsonRpc('/shop/cart/add', 'call', {
                'product_id': productId,
                'qty': 1
            }).then(function (result) {
                // Show success feedback
                $btn.html('<i class="fa fa-check mr-1"></i> ¡Agregado!');
                
                // Update cart count
                $('.my_cart_quantity').text(result.cart_quantity || 0);
                
                // Show toast notification
                self._showNotification(
                    '✓ Producto agregado',
                    result.product_name + ' agregado al carrito',
                    'success'
                );
                
                // Reset button after 2 seconds
                setTimeout(function () {
                    $btn.prop('disabled', false)
                        .html('<i class="fa fa-shopping-cart mr-1"></i> Agregar al carrito');
                }, 2000);
            }).catch(function (error) {
                $btn.prop('disabled', false)
                    .html('<i class="fa fa-shopping-cart mr-1"></i> Agregar al carrito');
                
                self._showNotification(
                    '✗ Error',
                    'No se pudo agregar el producto al carrito',
                    'danger'
                );
            });
        },

        /**
         * Toggle wishlist
         */
        _onToggleWishlist: function (ev) {
            ev.preventDefault();
            var $btn = $(ev.currentTarget);
            var productId = $btn.data('product-id');
            
            ajax.jsonRpc('/shop/wishlist/add', 'call', {
                'product_id': productId
            }).then(function (result) {
                $btn.toggleClass('active');
                
                var message = $btn.hasClass('active') 
                    ? 'Producto agregado a favoritos'
                    : 'Producto removido de favoritos';
                
                self._showNotification('♡ Favoritos', message, 'info');
            });
        },

        /**
         * Handle sort change
         */
        _onSortChange: function (ev) {
            var $select = $(ev.currentTarget);
            var sortValue = $select.val();
            
            // Update URL and reload
            var url = new URL(window.location.href);
            if (sortValue) {
                url.searchParams.set('order', sortValue);
            } else {
                url.searchParams.delete('order');
            }
            window.location.href = url.toString();
        },

        /**
         * Show toast notification
         */
        _showNotification: function (title, message, type) {
            // Using Bootstrap toast (Odoo 14+)
            var toast = $('<div class="toast" role="alert">')
                .append($('<div class="toast-header bg-' + type + ' text-white">')
                    .append($('<strong class="mr-auto">').text(title))
                    .append($('<button type="button" class="ml-2 mb-1 close text-white">')
                        .attr('data-dismiss', 'toast')
                        .html('&times;')))
                .append($('<div class="toast-body">').text(message));
            
            $('.o_notification_manager').append(toast);
            toast.toast({delay: 3000}).toast('show');
        },
    });

    return publicWidget.registry.ProductListingPage;
});
```

## Implementación PDP (Product Detail Page)

### 1. Template QWeb

**Archivo**: `views/pdp_templates.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    
    <!-- Override del template de producto -->
    <template id="product" inherit_id="website_sale.product" name="Product Detail - Ferreteria">
        
        <!-- Breadcrumb mejorado -->
        <xpath expr="//div[@id='product_details']" position="before">
            <nav aria-label="breadcrumb" class="breadcrumb-custom">
                <ol class="breadcrumb">
                    <li class="breadcrumb-item">
                        <a href="/">Inicio</a>
                    </li>
                    <t t-foreach="product.public_categ_ids[:1]" t-as="category">
                        <t t-foreach="category.parent_path.split('/')[:-1]" t-as="parent_id">
                            <t t-set="parent_cat" t-value="request.env['product.public.category'].browse(int(parent_id))"/>
                            <li class="breadcrumb-item">
                                <a t-att-href="'/shop/category/%s' % slug(parent_cat)">
                                    <t t-esc="parent_cat.name"/>
                                </a>
                            </li>
                        </t>
                        <li class="breadcrumb-item">
                            <a t-att-href="'/shop/category/%s' % slug(category)">
                                <t t-esc="category.name"/>
                            </a>
                        </li>
                    </t>
                    <li class="breadcrumb-item active" aria-current="page">
                        <t t-esc="product.name"/>
                    </li>
                </ol>
            </nav>
        </xpath>

        <!-- Layout principal del producto -->
        <xpath expr="//div[@id='product_details']" position="replace">
            <div id="product_details" class="row product-detail-page">
                
                <!-- Columna izquierda: Galería -->
                <div class="col-lg-6">
                    <t t-call="ferreteria_theme.product_gallery"/>
                </div>

                <!-- Columna derecha: Información -->
                <div class="col-lg-6">
                    <t t-call="ferreteria_theme.product_info"/>
                </div>
            </div>

            <!-- Tabs de contenido -->
            <div class="row mt-5">
                <div class="col-12">
                    <t t-call="ferreteria_theme.product_tabs"/>
                </div>
            </div>

            <!-- Productos relacionados -->
            <div class="row mt-5">
                <div class="col-12">
                    <t t-call="ferreteria_theme.related_products"/>
                </div>
            </div>
        </xpath>

    </template>

    <!-- Galería de imágenes -->
    <template id="product_gallery" name="Product Gallery">
        <div class="product-gallery">
            <!-- Imagen principal -->
            <div class="main-image-container">
                <t t-set="main_image" t-value="product.image_1920"/>
                <img t-att-src="image_data_uri(main_image)" 
                     t-att-alt="product.name"
                     class="img-fluid main-image"
                     id="mainProductImage"/>
                
                <!-- Badges -->
                <div class="product-badges">
                    <span t-if="product.website_ribbon_id" 
                          class="badge badge-danger">
                        <t t-esc="product.website_ribbon_id.name"/>
                    </span>
                </div>

                <!-- Botón zoom -->
                <button class="btn-zoom" data-toggle="modal" data-target="#imageModal">
                    <i class="fa fa-search-plus"></i> Zoom
                </button>
            </div>

            <!-- Thumbnails -->
            <div class="image-thumbnails mt-3">
                <div class="thumbnail-scroll">
                    <t t-set="images" t-value="[product.image_1920] + product.product_template_image_ids.mapped('image_1920')"/>
                    <t t-foreach="images[:10]" t-as="image">
                        <img t-att-src="image_data_uri(image)" 
                             class="thumbnail" 
                             t-att-class="'active' if image_index == 0 else ''"
                             t-att-data-index="image_index"/>
                    </t>
                </div>
            </div>
        </div>

        <!-- Modal de zoom -->
        <div class="modal fade" id="imageModal" tabindex="-1">
            <div class="modal-dialog modal-xl modal-dialog-centered">
                <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="close" data-dismiss="modal">
                            <span>×</span>
                        </button>
                    </div>
                    <div class="modal-body text-center">
                        <img src="" id="modalImage" class="img-fluid"/>
                    </div>
                </div>
            </div>
        </div>
    </template>

    <!-- Información del producto -->
    <template id="product_info" name="Product Info">
        <div class="product-info-section">
            
            <!-- Marca -->
            <div class="product-brand text-muted mb-2" t-if="product.product_brand_id">
                <a t-att-href="'/shop?brand=%s' % product.product_brand_id.id">
                    MARCA <strong t-esc="product.product_brand_id.name"/>
                </a>
            </div>

            <!-- Nombre -->
            <h1 class="product-name" t-field="product.name"/>

            <!-- Descripción corta -->
            <p class="product-short-description text-muted" t-if="product.description_sale">
                <t t-esc="product.description_sale"/>
            </p>

            <!-- SKU y Rating -->
            <div class="d-flex justify-content-between align-items-center mb-3">
                <div>
                    <span class="text-muted small">SKU: </span>
                    <strong t-esc="product.default_code or 'N/A'"/>
                </div>
                <div class="d-flex align-items-center gap-2">
                    <div t-if="product.rating_count">
                        <t t-call="portal_rating.rating_stars_static">
                            <t t-set="rating_avg" t-value="product.rating_avg"/>
                        </t>
                        <span class="text-muted small ml-1">
                            <t t-esc="product.rating_avg"/> (<t t-esc="product.rating_count"/> reseñas)
                        </span>
                    </div>
                    <button class="btn btn-link btn-sm" id="btnWishlist">
                        <i class="fa fa-heart-o"></i> Favoritos
                    </button>
                    <button class="btn btn-link btn-sm" data-toggle="modal" data-target="#shareModal">
                        <i class="fa fa-share-alt"></i> Compartir
                    </button>
                </div>
            </div>

            <hr/>

            <!-- Precio y disponibilidad -->
            <div class="price-availability-section mb-4">
                <!-- Precio -->
                <div class="product-price mb-3">
                    <t t-if="product.lst_price != product.list_price">
                        <div class="old-price text-muted text-decoration-line-through">
                            Antes: 
                            <t t-esc="product.lst_price" 
                               t-options="{'widget': 'monetary', 'display_currency': website.currency_id}"/>
                            <span class="badge badge-success ml-2">
                                -<t t-esc="int((1 - product.list_price/product.lst_price) * 100)"/>%
                            </span>
                        </div>
                    </t>
                    <div class="current-price h2 mb-0">
                        <t t-esc="product.list_price" 
                           t-options="{'widget': 'monetary', 'display_currency': website.currency_id}"/>
                    </div>
                </div>

                <!-- Stock -->
                <div class="stock-info mb-3">
                    <t t-if="product.qty_available > 0">
                        <span class="badge badge-success">
                            <i class="fa fa-check"></i> En stock
                        </span>
                        <span class="text-muted small ml-2">
                            <t t-if="product.qty_available < 5">
                                Solo quedan <strong t-esc="int(product.qty_available)"/> unidades
                            </t>
                        </span>
                    </t>
                    <t t-else="">
                        <span class="badge badge-danger">
                            <i class="fa fa-times"></i> Agotado
                        </span>
                    </t>
                </div>

                <!-- Información de envío -->
                <div class="shipping-info alert alert-info">
                    <i class="fa fa-truck mr-2"></i>
                    <strong>Envío gratis</strong> en compras mayores a $1,000
                </div>
            </div>

            <hr/>

            <!-- Selector de cantidad y CTAs -->
            <form action="/shop/cart/update" method="post" class="js_add_cart_variants">
                <input type="hidden" name="csrf_token" t-att-value="request.csrf_token()"/>
                <input type="hidden" name="product_id" t-att-value="product.id"/>
                
                <!-- Cantidad -->
                <div class="form-group">
                    <label for="quantity">Cantidad:</label>
                    <div class="input-group quantity-selector" style="max-width: 150px;">
                        <div class="input-group-prepend">
                            <button type="button" class="btn btn-outline-secondary btn-qty-minus">
                                <i class="fa fa-minus"></i>
                            </button>
                        </div>
                        <input type="number" 
                               name="add_qty" 
                               id="quantity"
                               class="form-control text-center" 
                               value="1" 
                               min="1" 
                               max="10"/>
                        <div class="input-group-append">
                            <button type="button" class="btn btn-outline-secondary btn-qty-plus">
                                <i class="fa fa-plus"></i>
                            </button>
                        </div>
                    </div>
                    <small class="text-muted">Máximo 10 unidades por cliente</small>
                </div>

                <!-- Botones CTA -->
                <div class="cta-buttons">
                    <t t-if="product.qty_available > 0">
                        <button type="submit" 
                                class="btn btn-primary btn-lg btn-block mb-2 btn-add-to-cart">
                            <i class="fa fa-shopping-cart mr-2"></i>
                            Agregar al carrito
                        </button>
                        <button type="button" 
                                class="btn btn-success btn-lg btn-block mb-3 btn-buy-now">
                            <i class="fa fa-bolt mr-2"></i>
                            Comprar ahora
                        </button>
                    </t>
                    <t t-else="">
                        <button type="button" 
                                class="btn btn-secondary btn-lg btn-block mb-3"
                                disabled="">
                            Producto no disponible
                        </button>
                        <button type="button" 
                                class="btn btn-outline-primary btn-block btn-notify-stock">
                            <i class="fa fa-bell mr-2"></i>
                            Avísame cuando esté disponible
                        </button>
                    </t>
                </div>
            </form>

            <hr/>

            <!-- Trust badges -->
            <div class="trust-badges">
                <ul class="list-unstyled">
                    <li><i class="fa fa-shield text-success mr-2"></i> Garantía oficial de 2 años</li>
                    <li><i class="fa fa-undo text-success mr-2"></i> Devolución gratis en 30 días</li>
                    <li><i class="fa fa-truck text-success mr-2"></i> Envío gratis en compras +$1,000</li>
                    <li><i class="fa fa-phone text-success mr-2"></i> Atención al cliente 24/7</li>
                </ul>
            </div>
        </div>
    </template>

    <!-- Tabs de contenido -->
    <template id="product_tabs" name="Product Tabs">
        <div class="product-tabs">
            <ul class="nav nav-tabs" role="tablist">
                <li class="nav-item">
                    <a class="nav-link active" data-toggle="tab" href="#description">
                        Descripción
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" data-toggle="tab" href="#specifications">
                        Especificaciones
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" data-toggle="tab" href="#reviews">
                        Reseñas (<t t-esc="product.rating_count or 0"/>)
                    </a>
                </li>
            </ul>

            <div class="tab-content p-4">
                <!-- Descripción -->
                <div class="tab-pane fade show active" id="description">
                    <div t-field="product.description"/>
                </div>

                <!-- Especificaciones -->
                <div class="tab-pane fade" id="specifications">
                    <table class="table table-striped">
                        <tr>
                            <th>SKU</th>
                            <td t-esc="product.default_code or 'N/A'"/>
                        </tr>
                        <tr t-if="product.product_brand_id">
                            <th>Marca</th>
                            <td t-esc="product.product_brand_id.name"/>
                        </tr>
                        <tr>
                            <th>Peso</th>
                            <td><t t-esc="product.weight"/> kg</td>
                        </tr>
                        <t t-foreach="product.product_template_attribute_value_ids" t-as="attr">
                            <tr>
                                <th t-esc="attr.attribute_id.name"/>
                                <td t-esc="attr.name"/>
                            </tr>
                        </t>
                    </table>
                </div>

                <!-- Reseñas -->
                <div class="tab-pane fade" id="reviews">
                    <t t-call="portal_rating.rating_page_list"/>
                </div>
            </div>
        </div>
    </template>

    <!-- Productos relacionados -->
    <template id="related_products" name="Related Products">
        <div class="related-products">
            <h3 class="mb-4">Productos Relacionados</h3>
            <div class="row">
                <t t-set="related_products" t-value="product.alternative_product_ids[:4]"/>
                <t t-foreach="related_products" t-as="related">
                    <div class="col-md-3">
                        <t t-set="product" t-value="related"/>
                        <t t-call="website_sale.products_item"/>
                    </div>
                </t>
            </div>
        </div>
    </template>

</odoo>
```

This implementation guide provides a comprehensive foundation for implementing the PLP and PDP designs in Odoo. The guide includes:

1. **Complete file structure** for a custom Odoo module
2. **QWeb templates** for both PLP and PDP with all specified components
3. **Python controllers** to extend Odoo's functionality
4. **SCSS styling** following modern design patterns
5. **JavaScript** for interactive features
6. **Integration points** with Odoo's core modules

The implementation follows Odoo best practices and is designed to be maintainable and extensible.
