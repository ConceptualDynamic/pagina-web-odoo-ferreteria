/**
 * Ferretería Website - JavaScript principal
 * ==========================================
 * Funcionalidades de frontend para el sitio web de ferretería.
 */

odoo.define('ferreteria_website.main', function (require) {
    'use strict';

    const publicWidget = require('web.public.widget');
    const ajax = require('web.ajax');

    /**
     * Widget para tracking de eventos de eCommerce
     */
    publicWidget.registry.FerreteriaAnalytics = publicWidget.Widget.extend({
        selector: '#wrapwrap',
        events: {
            'click .js_add_cart': '_onAddToCart',
            'click .a-submit': '_onBeginCheckout',
        },

        /**
         * @override
         */
        start: function () {
            this._super.apply(this, arguments);
            this._trackPageView();
            this._trackProductView();
        },

        /**
         * Track page view
         */
        _trackPageView: function () {
            if (typeof gtag !== 'undefined') {
                gtag('event', 'page_view', {
                    page_location: window.location.href,
                    page_path: window.location.pathname,
                    page_title: document.title
                });
            }
        },

        /**
         * Track product view on PDP
         */
        _trackProductView: function () {
            const productDetail = document.querySelector('#product_detail');
            if (productDetail && typeof gtag !== 'undefined') {
                const productData = {
                    item_id: productDetail.dataset.productId,
                    item_name: productDetail.dataset.productName,
                    price: parseFloat(productDetail.dataset.productPrice) || 0,
                    item_category: productDetail.dataset.productCategory || '',
                    item_brand: productDetail.dataset.productBrand || ''
                };
                
                // Get currency from page or default to website currency
                const currency = productDetail.dataset.productCurrency || 
                                 document.querySelector('[data-website-currency]')?.dataset.websiteCurrency || 
                                 'USD';

                gtag('event', 'view_item', {
                    currency: currency,
                    value: productData.price,
                    items: [productData]
                });
            }
        },

        /**
         * Track add to cart event
         */
        _onAddToCart: function (ev) {
            const $btn = $(ev.currentTarget);
            const $productCard = $btn.closest('.oe_product_cart, #product_detail');
            
            if ($productCard.length && typeof gtag !== 'undefined') {
                const productData = this._getProductData($productCard);
                
                // Get currency from page or default to website currency
                const currency = $productCard.data('product-currency') || 
                                 $('[data-website-currency]').data('websiteCurrency') || 
                                 'USD';
                
                gtag('event', 'add_to_cart', {
                    currency: currency,
                    value: productData.price,
                    items: [productData]
                });
            }
        },

        /**
         * Track begin checkout event
         */
        _onBeginCheckout: function (ev) {
            const $form = $(ev.currentTarget).closest('form');
            if ($form.attr('action') === '/shop/cart' && typeof gtag !== 'undefined') {
                gtag('event', 'begin_checkout');
            }
        },

        /**
         * Extract product data from element
         */
        _getProductData: function ($element) {
            return {
                item_id: $element.data('product-id') || '',
                item_name: $element.find('[itemprop="name"]').text().trim() || '',
                price: parseFloat($element.find('.oe_price .oe_currency_value').text().replace(/[^0-9.]/g, '')) || 0,
                item_category: $element.data('product-category') || '',
                item_brand: $element.data('product-brand') || ''
            };
        }
    });

    /**
     * Widget para búsqueda mejorada
     */
    publicWidget.registry.FerreteriaSearch = publicWidget.Widget.extend({
        selector: '.o_searchbar_form',
        events: {
            'input input[name="search"]': '_onSearchInput',
            'focus input[name="search"]': '_onSearchFocus',
            'blur input[name="search"]': '_onSearchBlur'
        },

        /**
         * @override
         */
        start: function () {
            this._super.apply(this, arguments);
            this.$searchInput = this.$('input[name="search"]');
            this._searchTimeout = null;
        },

        /**
         * Debounced search input handler
         */
        _onSearchInput: function (ev) {
            clearTimeout(this._searchTimeout);
            const query = ev.currentTarget.value;
            
            if (query.length >= 3) {
                this._searchTimeout = setTimeout(() => {
                    this._performSearch(query);
                }, 300);
            }
        },

        /**
         * Handle search focus
         */
        _onSearchFocus: function () {
            this.$el.addClass('focused');
        },

        /**
         * Handle search blur
         */
        _onSearchBlur: function () {
            setTimeout(() => {
                this.$el.removeClass('focused');
            }, 200);
        },

        /**
         * Perform AJAX search (placeholder for future implementation)
         */
        _performSearch: function (query) {
            // Future: implement autocomplete suggestions
            console.log('Searching for:', query);
        }
    });

    /**
     * Widget para lazy loading de imágenes
     */
    publicWidget.registry.FerreteriaLazyLoad = publicWidget.Widget.extend({
        selector: '.oe_product_cart img, #product_detail img',

        /**
         * @override
         */
        start: function () {
            this._super.apply(this, arguments);
            this._initLazyLoad();
        },

        /**
         * Initialize intersection observer for lazy loading
         */
        _initLazyLoad: function () {
            if ('IntersectionObserver' in window) {
                const imageObserver = new IntersectionObserver((entries, observer) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            const img = entry.target;
                            if (img.dataset.src) {
                                img.src = img.dataset.src;
                                img.classList.add('loaded');
                                observer.unobserve(img);
                            }
                        }
                    });
                });

                this.$el.each(function() {
                    if (this.dataset.src) {
                        imageObserver.observe(this);
                    }
                });
            }
        }
    });

    /**
     * Widget para el botón de WhatsApp
     */
    publicWidget.registry.FerreteriaWhatsApp = publicWidget.Widget.extend({
        selector: '.ferreteria-whatsapp-btn',
        events: {
            'click': '_onWhatsAppClick'
        },

        /**
         * Track WhatsApp button click
         */
        _onWhatsAppClick: function () {
            if (typeof gtag !== 'undefined') {
                gtag('event', 'contact', {
                    method: 'whatsapp',
                    event_category: 'engagement',
                    event_label: 'WhatsApp Button Click'
                });
            }
        }
    });

    /**
     * Widget para filtros de producto mejorados
     */
    publicWidget.registry.FerreteriaFilters = publicWidget.Widget.extend({
        selector: '#products_grid_before',
        events: {
            'change .css_attribute_color input': '_onFilterChange',
            'change select': '_onFilterChange'
        },

        /**
         * Handle filter change with loading indicator
         */
        _onFilterChange: function (ev) {
            const $target = $(ev.currentTarget);
            
            // Add loading state
            this.$el.addClass('loading');
            
            // Track filter usage
            if (typeof gtag !== 'undefined') {
                gtag('event', 'filter_applied', {
                    event_category: 'ecommerce',
                    event_label: $target.attr('name') || 'unknown'
                });
            }
        }
    });

    /**
     * Widget para el carrito sticky
     */
    publicWidget.registry.FerreteriaStickyCart = publicWidget.Widget.extend({
        selector: '#wrap',

        /**
         * @override
         */
        start: function () {
            this._super.apply(this, arguments);
            this._initStickyElements();
        },

        /**
         * Initialize sticky behavior
         */
        _initStickyElements: function () {
            const $stickyCart = this.$('#cart_total');
            if ($stickyCart.length && window.innerWidth >= 992) {
                const offsetTop = $stickyCart.offset().top;
                
                $(window).on('scroll.stickyCart', () => {
                    if ($(window).scrollTop() > offsetTop - 100) {
                        $stickyCart.addClass('sticky');
                    } else {
                        $stickyCart.removeClass('sticky');
                    }
                });
            }
        },

        /**
         * @override
         */
        destroy: function () {
            $(window).off('scroll.stickyCart');
            this._super.apply(this, arguments);
        }
    });

    /**
     * Utility: Format currency
     * Uses browser locale detection for proper formatting
     */
    function formatCurrency(amount, currency, locale) {
        // Try to detect locale from document or use browser default
        const detectedLocale = locale || 
                               document.documentElement.lang || 
                               navigator.language || 
                               'en-US';
        return new Intl.NumberFormat(detectedLocale, {
            style: 'currency',
            currency: currency || 'USD'
        }).format(amount);
    }

    /**
     * Utility: Show notification
     */
    function showNotification(message, type) {
        type = type || 'info';
        const $notification = $('<div>')
            .addClass('ferreteria-notification ferreteria-notification-' + type)
            .text(message)
            .appendTo('body');
        
        setTimeout(() => {
            $notification.addClass('show');
        }, 100);
        
        setTimeout(() => {
            $notification.removeClass('show');
            setTimeout(() => $notification.remove(), 300);
        }, 3000);
    }

    return {
        FerreteriaAnalytics: publicWidget.registry.FerreteriaAnalytics,
        FerreteriaSearch: publicWidget.registry.FerreteriaSearch,
        FerreteriaLazyLoad: publicWidget.registry.FerreteriaLazyLoad,
        FerreteriaWhatsApp: publicWidget.registry.FerreteriaWhatsApp,
        FerreteriaFilters: publicWidget.registry.FerreteriaFilters,
        FerreteriaStickyCart: publicWidget.registry.FerreteriaStickyCart,
        formatCurrency: formatCurrency,
        showNotification: showNotification
    };
});
