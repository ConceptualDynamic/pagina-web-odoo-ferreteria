"""
WhatsApp Integration Templates for Odoo Website
Templates y snippets para integrar WhatsApp como canal de contacto
"""

# ========================================
# OPCIÓN 1: Botón Flotante Simple (HTML/CSS/JS)
# ========================================

WHATSAPP_FLOAT_BUTTON_HTML = """
<!-- Botón flotante de WhatsApp -->
<a href="https://wa.me/573001234567?text=Hola,%20tengo%20una%20consulta" 
   class="whatsapp-float" 
   target="_blank"
   id="whatsapp-float-btn"
   rel="noopener noreferrer">
  <i class="fa fa-whatsapp"></i>
</a>
"""

WHATSAPP_FLOAT_BUTTON_CSS = """
/* Estilos para botón flotante de WhatsApp */
.whatsapp-float {
    position: fixed;
    width: 60px;
    height: 60px;
    bottom: 40px;
    right: 40px;
    background-color: #25d366;
    color: #FFF;
    border-radius: 50px;
    text-align: center;
    font-size: 30px;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
    z-index: 1000;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
    text-decoration: none;
}

.whatsapp-float:hover {
    background-color: #128c7e;
    color: #FFF;
    transform: scale(1.1);
    box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.4);
}

.whatsapp-float i {
    margin: 0;
    line-height: 60px;
}

/* Responsive: ocultar en mobile si es necesario */
@media (max-width: 768px) {
    .whatsapp-float {
        width: 50px;
        height: 50px;
        font-size: 24px;
        bottom: 20px;
        right: 20px;
    }
}

/* Animación de pulso (opcional) */
@keyframes pulse {
    0% {
        box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7);
    }
    70% {
        box-shadow: 0 0 0 15px rgba(37, 211, 102, 0);
    }
    100% {
        box-shadow: 0 0 0 0 rgba(37, 211, 102, 0);
    }
}

.whatsapp-float.pulse {
    animation: pulse 2s infinite;
}
"""

WHATSAPP_FLOAT_BUTTON_JS = """
// JavaScript para botón de WhatsApp dinámico
(function() {
    'use strict';
    
    // Configuración
    const CONFIG = {
        phoneNumber: '573001234567', // Número con código de país sin +
        defaultMessage: 'Hola, tengo una consulta',
        trackGA4: true,
        addPulseAnimation: true
    };
    
    // Generar URL de WhatsApp
    function generateWhatsAppURL(message) {
        message = message || CONFIG.defaultMessage;
        return `https://wa.me/${CONFIG.phoneNumber}?text=${encodeURIComponent(message)}`;
    }
    
    // Actualizar mensaje según contexto de página
    function updateWhatsAppButton() {
        const btn = document.getElementById('whatsapp-float-btn');
        if (!btn) return;
        
        let customMessage = CONFIG.defaultMessage;
        
        // Página de producto
        const productName = document.querySelector('h1[itemprop="name"]')?.textContent.trim();
        if (productName) {
            customMessage = `Hola, me interesa ${productName}`;
        }
        
        // Página de categoría
        const categoryName = document.querySelector('.breadcrumb .active')?.textContent.trim();
        if (categoryName && !productName) {
            customMessage = `Hola, busco productos en ${categoryName}`;
        }
        
        // Carrito con productos
        const cartItems = document.querySelectorAll('.o_cart_product');
        if (cartItems.length > 0) {
            customMessage = `Hola, tengo ${cartItems.length} producto(s) en mi carrito y quisiera consultar`;
        }
        
        // Actualizar href
        btn.href = generateWhatsAppURL(customMessage);
        
        // Agregar animación de pulso (opcional)
        if (CONFIG.addPulseAnimation) {
            btn.classList.add('pulse');
        }
    }
    
    // Trackear click en GA4
    function trackWhatsAppClick() {
        if (!CONFIG.trackGA4 || typeof gtag === 'undefined') return;
        
        gtag('event', 'whatsapp_click', {
            location: window.location.pathname,
            method: 'whatsapp',
            button_type: 'floating'
        });
    }
    
    // Inicialización
    document.addEventListener('DOMContentLoaded', function() {
        updateWhatsAppButton();
        
        // Event listener para tracking
        const btn = document.getElementById('whatsapp-float-btn');
        if (btn) {
            btn.addEventListener('click', trackWhatsAppClick);
        }
    });
})();
"""

# ========================================
# OPCIÓN 2: Widget con Múltiples Agentes
# ========================================

WHATSAPP_MULTI_AGENT_HTML = """
<!-- Widget de WhatsApp con múltiples opciones -->
<div id="whatsapp-widget" class="whatsapp-widget">
    <div class="whatsapp-widget-header" onclick="toggleWhatsAppWidget()">
        <i class="fa fa-whatsapp"></i>
        <span>¿Necesitas ayuda?</span>
        <i class="fa fa-chevron-down toggle-icon"></i>
    </div>
    <div class="whatsapp-widget-body" style="display: none;">
        <div class="whatsapp-agent">
            <img src="/web/image/hr.employee/1/avatar_128" alt="Ventas" class="agent-avatar">
            <div class="agent-info">
                <strong>Ventas</strong>
                <small>Productos y cotizaciones</small>
            </div>
            <a href="https://wa.me/573001234567?text=Hola,%20necesito%20información%20de%20productos" 
               class="btn btn-sm btn-success whatsapp-chat-btn" 
               target="_blank"
               data-department="ventas">
                <i class="fa fa-whatsapp"></i> Chatear
            </a>
        </div>
        <div class="whatsapp-agent">
            <img src="/web/image/hr.employee/2/avatar_128" alt="Soporte" class="agent-avatar">
            <div class="agent-info">
                <strong>Soporte Técnico</strong>
                <small>Ayuda con pedidos</small>
            </div>
            <a href="https://wa.me/573001234568?text=Hola,%20necesito%20soporte%20técnico" 
               class="btn btn-sm btn-success whatsapp-chat-btn" 
               target="_blank"
               data-department="soporte">
                <i class="fa fa-whatsapp"></i> Chatear
            </a>
        </div>
        <div class="whatsapp-agent">
            <img src="/web/image/hr.employee/3/avatar_128" alt="B2B" class="agent-avatar">
            <div class="agent-info">
                <strong>Ventas B2B</strong>
                <small>Proyectos empresariales</small>
            </div>
            <a href="https://wa.me/573001234569?text=Hola,%20soy%20empresa%20y%20necesito%20cotización" 
               class="btn btn-sm btn-success whatsapp-chat-btn" 
               target="_blank"
               data-department="b2b">
                <i class="fa fa-whatsapp"></i> Chatear
            </a>
        </div>
        <div class="whatsapp-widget-footer">
            <small>Horario: Lun-Vie 8am-6pm, Sáb 9am-2pm</small>
        </div>
    </div>
</div>

<style>
.whatsapp-widget {
    position: fixed;
    bottom: 40px;
    right: 40px;
    width: 320px;
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 2px 20px rgba(0, 0, 0, 0.2);
    z-index: 1000;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

.whatsapp-widget-header {
    background: #25d366;
    color: #fff;
    padding: 15px;
    border-radius: 10px 10px 0 0;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 10px;
}

.whatsapp-widget-header i.fa-whatsapp {
    font-size: 24px;
}

.whatsapp-widget-header .toggle-icon {
    margin-left: auto;
    transition: transform 0.3s;
}

.whatsapp-widget-header.open .toggle-icon {
    transform: rotate(180deg);
}

.whatsapp-widget-body {
    padding: 10px;
    max-height: 400px;
    overflow-y: auto;
}

.whatsapp-agent {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px;
    border-bottom: 1px solid #eee;
}

.whatsapp-agent:last-child {
    border-bottom: none;
}

.agent-avatar {
    width: 45px;
    height: 45px;
    border-radius: 50%;
    object-fit: cover;
}

.agent-info {
    flex: 1;
}

.agent-info strong {
    display: block;
    font-size: 14px;
}

.agent-info small {
    color: #666;
    font-size: 12px;
}

.whatsapp-chat-btn {
    white-space: nowrap;
}

.whatsapp-widget-footer {
    text-align: center;
    padding: 10px;
    background: #f5f5f5;
    border-radius: 0 0 10px 10px;
    color: #666;
}

@media (max-width: 768px) {
    .whatsapp-widget {
        width: calc(100% - 40px);
        right: 20px;
        left: 20px;
    }
}
</style>

<script>
function toggleWhatsAppWidget() {
    const widget = document.getElementById('whatsapp-widget');
    const header = widget.querySelector('.whatsapp-widget-header');
    const body = widget.querySelector('.whatsapp-widget-body');
    
    if (body.style.display === 'none') {
        body.style.display = 'block';
        header.classList.add('open');
    } else {
        body.style.display = 'none';
        header.classList.remove('open');
    }
}

// Trackear clicks en GA4
document.querySelectorAll('.whatsapp-chat-btn').forEach(function(btn) {
    btn.addEventListener('click', function() {
        const department = this.getAttribute('data-department');
        if (typeof gtag !== 'undefined') {
            gtag('event', 'whatsapp_click', {
                location: window.location.pathname,
                department: department,
                button_type: 'multi_agent'
            });
        }
    });
});
</script>
"""

# ========================================
# OPCIÓN 3: Template Odoo QWeb
# ========================================

ODOO_QWEB_TEMPLATE = """
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <!-- Template para botón flotante de WhatsApp -->
    <template id="whatsapp_float_button" name="WhatsApp Float Button">
        <t t-set="whatsapp_phone" t-value="website.whatsapp_phone or '573001234567'"/>
        <t t-set="whatsapp_message" t-value="'Hola, tengo una consulta desde ' + website.name"/>
        
        <a t-attf-href="https://wa.me/#{whatsapp_phone}?text=#{url_encode(whatsapp_message)}" 
           class="whatsapp-float" 
           target="_blank"
           rel="noopener noreferrer"
           t-att-data-phone="whatsapp_phone">
            <i class="fa fa-whatsapp"></i>
        </a>
        
        <style>
            .whatsapp-float {
                position: fixed;
                width: 60px;
                height: 60px;
                bottom: 40px;
                right: 40px;
                background-color: #25d366;
                color: #FFF;
                border-radius: 50px;
                text-align: center;
                font-size: 30px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
                z-index: 1000;
                display: flex;
                align-items: center;
                justify-content: center;
                transition: all 0.3s ease;
                text-decoration: none;
            }
            .whatsapp-float:hover {
                background-color: #128c7e;
                color: #FFF;
                transform: scale(1.1);
            }
        </style>
    </template>
    
    <!-- Snippet para agregar en products -->
    <template id="product_whatsapp_button" name="Product WhatsApp Button" inherit_id="website_sale.product">
        <xpath expr="//div[@id='product_details']//a[@id='add_to_cart']" position="after">
            <a t-attf-href="https://wa.me/#{website.whatsapp_phone or '573001234567'}?text=Me interesa #{product.name}" 
               class="btn btn-outline-success btn-lg mt-2" 
               target="_blank">
                <i class="fa fa-whatsapp"></i> Consultar por WhatsApp
            </a>
        </xpath>
    </template>
    
    <!-- Agregar campo en configuración de website -->
    <record id="view_website_form_whatsapp" model="ir.ui.view">
        <field name="name">website.form.whatsapp</field>
        <field name="model">website</field>
        <field name="inherit_id" ref="website.view_website_form"/>
        <field name="arch" type="xml">
            <xpath expr="//group[@name='website_info']" position="inside">
                <field name="whatsapp_phone" placeholder="+57 300 1234567"/>
                <field name="whatsapp_enabled" widget="boolean_toggle"/>
            </xpath>
        </field>
    </record>
</odoo>
"""

# ========================================
# OPCIÓN 4: Modelo de Python para Website
# ========================================

ODOO_PYTHON_MODEL = """
# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Website(models.Model):
    _inherit = 'website'
    
    whatsapp_enabled = fields.Boolean(
        string='WhatsApp Enabled',
        default=True,
        help='Enable WhatsApp integration on website'
    )
    
    whatsapp_phone = fields.Char(
        string='WhatsApp Phone',
        help='Phone number with country code (e.g., 573001234567)'
    )
    
    whatsapp_message_template = fields.Text(
        string='Default Message Template',
        default='Hola, tengo una consulta',
        help='Default message when clicking WhatsApp button'
    )
    
    def _get_whatsapp_url(self, custom_message=None):
        '''
        Generate WhatsApp URL with optional custom message
        '''
        self.ensure_one()
        if not self.whatsapp_enabled or not self.whatsapp_phone:
            return '#'
        
        from werkzeug.urls import url_encode
        message = custom_message or self.whatsapp_message_template
        
        return f"https://wa.me/{self.whatsapp_phone}?text={url_encode({'': message})[1:]}"
"""

# ========================================
# Notas de Implementación
# ========================================

IMPLEMENTATION_NOTES = """
==============================================
NOTAS DE IMPLEMENTACIÓN - WhatsApp Integration
==============================================

1. CONFIGURACIÓN INICIAL
   - Obtener número de WhatsApp Business (verificado y con perfil completo)
   - Formato: Código país + número sin espacios ni símbolos (ej: 573001234567)
   - Configurar respuestas rápidas en WhatsApp Business

2. MENSAJES PRE-RELLENADOS RECOMENDADOS
   - Home: "Hola, quisiera información sobre sus productos"
   - PDP: "Hola, me interesa [NOMBRE_PRODUCTO]"
   - Carrito: "Hola, tengo productos en mi carrito y quisiera consultar"
   - Contacto: "Hola, quisiera ponerme en contacto"

3. HORARIOS DE ATENCIÓN
   - Mostrar claramente el horario de respuesta
   - Mensaje automático fuera de horario (WhatsApp Business)
   - Ejemplo: "Lun-Vie 8am-6pm, Sáb 9am-2pm"

4. MÚLTIPLES DEPARTAMENTOS
   Si se manejan varios números:
   - Ventas: +57 300 1234567
   - Soporte: +57 300 1234568
   - B2B: +57 300 1234569
   
   Usar widget multi-agente o botones contextuales

5. INTEGRACIÓN CON CRM
   Proceso manual recomendado:
   a) Cliente contacta por WhatsApp
   b) Agente evalúa intención comercial
   c) Si es lead válido → Crear manualmente en CRM o usar automatización
   d) Adjuntar captura de conversación al lead
   
   Proceso automático (avanzado):
   - WhatsApp Business API + Webhook
   - Crear lead automáticamente con contexto de mensaje
   - Requiere proveedor verificado (Twilio, MessageBird, etc.)

6. TRACKING GA4
   Evento recomendado:
   gtag('event', 'whatsapp_click', {
       location: window.location.pathname,
       department: 'ventas',
       button_type: 'floating'
   });

7. MEJORES PRÁCTICAS
   - No abusar de mensajes pre-rellenados muy largos
   - Mantener botón visible pero no invasivo
   - Probar en diferentes dispositivos (móvil abre app, desktop abre web)
   - Responder rápidamente para no perder leads
   - Medir tasa de conversión: click → conversación → lead → venta

8. ALTERNATIVAS
   - Odoo Live Chat (nativo, integrado con CRM)
   - Facebook Messenger
   - Telegram
   - Chat híbrido (Live Chat con fallback a WhatsApp)

9. VALIDACIÓN
   ✓ Botón visible en todas las páginas
   ✓ Click abre WhatsApp correctamente
   ✓ Número de teléfono correcto
   ✓ Mensaje pre-rellenado funciona
   ✓ Evento GA4 se dispara
   ✓ Responsive (móvil y desktop)
   ✓ Horario de atención visible
"""

if __name__ == '__main__':
    print(IMPLEMENTATION_NOTES)
