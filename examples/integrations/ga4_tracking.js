/**
 * Google Analytics 4 - E-commerce Event Tracking
 * Implementación para Odoo Website
 * 
 * @description Script para rastrear eventos de e-commerce en GA4
 * @requires gtag.js cargado en la página
 */

// Configuración
const GA4_MEASUREMENT_ID = 'G-XXXXXXXXXX'; // Reemplazar con ID real
const CURRENCY = 'COP';

// Helper: Formatear producto para GA4
function formatProductForGA4(product) {
    return {
        item_id: product.id || product.sku,
        item_name: product.name,
        item_category: product.category,
        item_category2: product.subcategory || '',
        item_brand: product.brand || '',
        price: parseFloat(product.price),
        quantity: parseInt(product.quantity) || 1,
        discount: parseFloat(product.discount) || 0
    };
}

// 1. Ver listado de productos (PLP)
function trackViewItemList(products, listName = 'Búsqueda de productos') {
    if (typeof gtag === 'undefined') {
        console.warn('gtag no está definido');
        return;
    }
    
    const items = products.map(formatProductForGA4);
    
    gtag('event', 'view_item_list', {
        item_list_name: listName,
        items: items
    });
}

// 2. Ver detalle de producto (PDP)
function trackViewItem(product) {
    if (typeof gtag === 'undefined') return;
    
    gtag('event', 'view_item', {
        currency: CURRENCY,
        value: parseFloat(product.price),
        items: [formatProductForGA4(product)]
    });
}

// 3. Agregar al carrito
function trackAddToCart(product) {
    if (typeof gtag === 'undefined') return;
    
    gtag('event', 'add_to_cart', {
        currency: CURRENCY,
        value: parseFloat(product.price) * parseInt(product.quantity),
        items: [formatProductForGA4(product)]
    });
}

// 4. Remover del carrito
function trackRemoveFromCart(product) {
    if (typeof gtag === 'undefined') return;
    
    gtag('event', 'remove_from_cart', {
        currency: CURRENCY,
        value: parseFloat(product.price) * parseInt(product.quantity),
        items: [formatProductForGA4(product)]
    });
}

// 5. Iniciar checkout
function trackBeginCheckout(cartItems, cartTotal) {
    if (typeof gtag === 'undefined') return;
    
    const items = cartItems.map(formatProductForGA4);
    
    gtag('event', 'begin_checkout', {
        currency: CURRENCY,
        value: parseFloat(cartTotal),
        items: items
    });
}

// 6. Agregar información de envío
function trackAddShippingInfo(cartItems, cartTotal, shippingTier) {
    if (typeof gtag === 'undefined') return;
    
    const items = cartItems.map(formatProductForGA4);
    
    gtag('event', 'add_shipping_info', {
        currency: CURRENCY,
        value: parseFloat(cartTotal),
        shipping_tier: shippingTier,
        items: items
    });
}

// 7. Agregar información de pago
function trackAddPaymentInfo(cartItems, cartTotal, paymentType) {
    if (typeof gtag === 'undefined') return;
    
    const items = cartItems.map(formatProductForGA4);
    
    gtag('event', 'add_payment_info', {
        currency: CURRENCY,
        value: parseFloat(cartTotal),
        payment_type: paymentType,
        items: items
    });
}

// 8. Compra completada
function trackPurchase(orderData) {
    if (typeof gtag === 'undefined') return;
    
    const items = orderData.items.map(formatProductForGA4);
    
    gtag('event', 'purchase', {
        transaction_id: orderData.orderId,
        value: parseFloat(orderData.total),
        tax: parseFloat(orderData.tax),
        shipping: parseFloat(orderData.shipping),
        currency: CURRENCY,
        coupon: orderData.coupon || '',
        items: items
    });
}

// Eventos personalizados
function trackSearch(searchTerm) {
    if (typeof gtag === 'undefined') return;
    
    gtag('event', 'search', {
        search_term: searchTerm
    });
}

function trackFilterProducts(filterType, filterValue) {
    if (typeof gtag === 'undefined') return;
    
    gtag('event', 'filter_products', {
        filter_type: filterType,
        filter_value: filterValue
    });
}

function trackContactForm(formType) {
    if (typeof gtag === 'undefined') return;
    
    gtag('event', 'contact_form_submit', {
        form_type: formType
    });
}

function trackWhatsAppClick(location) {
    if (typeof gtag === 'undefined') return;
    
    gtag('event', 'whatsapp_click', {
        location: location,
        method: 'whatsapp'
    });
}

function trackPhoneClick(location) {
    if (typeof gtag === 'undefined') return;
    
    gtag('event', 'phone_click', {
        location: location,
        method: 'phone'
    });
}

// Auto-inicialización para eventos comunes
(function() {
    'use strict';
    
    // Detectar página actual y disparar evento apropiado
    if (typeof odoo !== 'undefined' && odoo.csrf_token) {
        
        // PLP: Product Listing Page
        if (document.querySelector('.oe_product_cart')) {
            const products = [];
            document.querySelectorAll('.oe_product_cart').forEach(function(elem) {
                const productId = elem.getAttribute('data-product-id');
                const productName = elem.querySelector('.o_wsale_product_title')?.textContent.trim();
                const productPrice = elem.querySelector('.oe_currency_value')?.textContent.trim();
                
                if (productId && productName && productPrice) {
                    products.push({
                        id: productId,
                        name: productName,
                        price: productPrice,
                        quantity: 1
                    });
                }
            });
            
            if (products.length > 0) {
                trackViewItemList(products, document.title);
            }
        }
        
        // PDP: Product Detail Page
        if (document.querySelector('#product_detail')) {
            const productId = document.querySelector('input[name="product_id"]')?.value;
            const productName = document.querySelector('h1[itemprop="name"]')?.textContent.trim();
            const productPrice = document.querySelector('.oe_price .oe_currency_value')?.textContent.trim();
            const productCategory = document.querySelector('.breadcrumb .active')?.textContent.trim();
            
            if (productId && productName && productPrice) {
                trackViewItem({
                    id: productId,
                    name: productName,
                    price: productPrice,
                    category: productCategory,
                    quantity: 1
                });
            }
        }
        
        // Checkout: Begin Checkout
        if (document.querySelector('#wrapwrap.oe_website_sale #o-carousel-product')) {
            // Esta es la página de checkout
            const cartItems = [];
            document.querySelectorAll('.o_cart_product').forEach(function(elem) {
                const productId = elem.querySelector('input[name^="product_id"]')?.value;
                const productName = elem.querySelector('.o_cart_product_name')?.textContent.trim();
                const productPrice = elem.querySelector('.text-danger .oe_currency_value')?.textContent.trim();
                const quantity = elem.querySelector('input[name="quantity"]')?.value;
                
                if (productId && productName && productPrice) {
                    cartItems.push({
                        id: productId,
                        name: productName,
                        price: productPrice,
                        quantity: quantity || 1
                    });
                }
            });
            
            const cartTotal = document.querySelector('#order_total .oe_currency_value')?.textContent.trim();
            
            if (cartItems.length > 0 && cartTotal) {
                trackBeginCheckout(cartItems, cartTotal);
            }
        }
    }
    
    // Event listeners para botones
    document.addEventListener('DOMContentLoaded', function() {
        
        // Botón agregar al carrito
        document.querySelectorAll('a[href^="/shop/cart/update"]').forEach(function(btn) {
            btn.addEventListener('click', function(e) {
                const productId = this.getAttribute('data-product-id');
                const productName = this.closest('.oe_product').querySelector('.o_wsale_product_title')?.textContent.trim();
                const productPrice = this.closest('.oe_product').querySelector('.oe_currency_value')?.textContent.trim();
                
                if (productId && productName && productPrice) {
                    trackAddToCart({
                        id: productId,
                        name: productName,
                        price: productPrice,
                        quantity: 1
                    });
                }
            });
        });
        
        // Búsqueda
        document.querySelectorAll('form[action="/shop"] input[name="search"]').forEach(function(input) {
            input.closest('form').addEventListener('submit', function() {
                const searchTerm = input.value.trim();
                if (searchTerm) {
                    trackSearch(searchTerm);
                }
            });
        });
        
        // WhatsApp clicks
        document.querySelectorAll('a[href*="wa.me"], a[href*="whatsapp"]').forEach(function(link) {
            link.addEventListener('click', function() {
                const location = this.className || 'unknown';
                trackWhatsAppClick(location);
            });
        });
        
        // Formularios de contacto
        document.querySelectorAll('form[action*="contact"], form[action*="quote"]').forEach(function(form) {
            form.addEventListener('submit', function() {
                const formType = this.getAttribute('id') || this.getAttribute('class') || 'generic';
                trackContactForm(formType);
            });
        });
    });
})();

// Exportar funciones para uso manual
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        trackViewItemList,
        trackViewItem,
        trackAddToCart,
        trackRemoveFromCart,
        trackBeginCheckout,
        trackAddShippingInfo,
        trackAddPaymentInfo,
        trackPurchase,
        trackSearch,
        trackFilterProducts,
        trackContactForm,
        trackWhatsAppClick,
        trackPhoneClick
    };
}
