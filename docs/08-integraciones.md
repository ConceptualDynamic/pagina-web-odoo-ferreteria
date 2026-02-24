# Integraciones

Conectar analítica (GA4), gestión de leads (CRM) y canal de contacto directo (WhatsApp/chat) para garantizar trazabilidad completa del usuario desde la visita hasta la conversión.

## 1. Google Analytics 4 (GA4)

### 1.1 Objetivo
Rastrear comportamiento del usuario, conversiones, y métricas clave del negocio para optimización continua.

### 1.2 Configuración Base

#### Instalación del Tag
```html
<!-- Google tag (gtag.js) - Colocar en <head> de todas las páginas -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX', {
    'send_page_view': true,
    'cookie_flags': 'SameSite=None;Secure'
  });
</script>
```

**Alternativa**: Implementar vía Google Tag Manager (GTM) para mayor flexibilidad.

#### Variables de configuración Odoo
Crear parámetro del sistema `website.google_analytics_key` o configurar en ajustes del sitio web.

### 1.3 Eventos de E-commerce (Enhanced E-commerce)

#### Eventos Requeridos

| Evento | Descripción | Cuándo disparar |
|--------|-------------|-----------------|
| `view_item_list` | Ver listado de productos | Carga de PLP (Product Listing Page) |
| `view_item` | Ver detalle de producto | Carga de PDP (Product Detail Page) |
| `add_to_cart` | Agregar al carrito | Click en botón "Agregar al carrito" |
| `remove_from_cart` | Remover del carrito | Click en eliminar producto del carrito |
| `begin_checkout` | Iniciar checkout | Acceso a página de checkout |
| `add_shipping_info` | Información de envío | Completar datos de envío |
| `add_payment_info` | Información de pago | Seleccionar método de pago |
| `purchase` | Compra completada | Confirmación de pedido |
| `view_promotion` | Ver promoción | Carga de banner/oferta |
| `select_promotion` | Click en promoción | Click en banner/oferta |

#### Ejemplo: Evento view_item
```javascript
gtag('event', 'view_item', {
  currency: 'COP',
  value: 150000,
  items: [{
    item_id: 'SKU-001',
    item_name: 'Taladro Percutor 13mm',
    item_category: 'Herramientas Eléctricas',
    item_category2: 'Taladros',
    item_brand: 'Bosch',
    price: 150000,
    quantity: 1
  }]
});
```

#### Ejemplo: Evento purchase
```javascript
gtag('event', 'purchase', {
  transaction_id: 'SO-2024-001',
  value: 285000,
  tax: 54000,
  shipping: 15000,
  currency: 'COP',
  items: [{
    item_id: 'SKU-001',
    item_name: 'Taladro Percutor 13mm',
    item_category: 'Herramientas Eléctricas',
    price: 150000,
    quantity: 1
  }, {
    item_id: 'SKU-002',
    item_name: 'Set de Brocas 20pcs',
    item_category: 'Accesorios',
    price: 35000,
    quantity: 3
  }]
});
```

### 1.4 Eventos Personalizados

| Evento | Descripción | Parámetros |
|--------|-------------|------------|
| `search` | Búsqueda de productos | `search_term` |
| `filter_products` | Aplicar filtros | `filter_type`, `filter_value` |
| `contact_form_submit` | Envío de formulario de contacto | `form_type` |
| `phone_click` | Click en número telefónico | `location` |
| `whatsapp_click` | Click en botón de WhatsApp | `location` |

### 1.5 User Properties
Definir propiedades del usuario para segmentación:
- `customer_type`: 'guest', 'registered', 'b2b'
- `lifetime_value`: Valor total de compras
- `order_count`: Número de pedidos completados

### 1.6 Implementación en Odoo

**Opción A: Módulo website_sale**
- Extender templates `product`, `shop`, `cart`, `checkout`
- Agregar snippets JS con eventos GA4 en momentos clave

**Opción B: Módulo personalizado**
```python
# __manifest__.py
{
    'name': 'Website GA4 Integration',
    'depends': ['website', 'website_sale'],
    'data': [
        'views/website_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'website_ga4/static/src/js/ga4_events.js',
        ],
    },
}
```

### 1.7 Validación
- [ ] Tag GA4 presente en todas las páginas
- [ ] Eventos de e-commerce se disparan correctamente (verificar en DebugView de GA4)
- [ ] Transaction ID único en cada compra
- [ ] Valores y monedas correctos
- [ ] User ID asociado cuando usuario está logueado

---

## 2. Integración CRM (Gestión de Leads)

### 2.1 Objetivo
Capturar y gestionar leads desde formularios de contacto, cotización, y acciones de alto interés para seguimiento comercial.

### 2.2 Origen de Leads

| Fuente | Descripción | Campos Capturados |
|--------|-------------|-------------------|
| Formulario de Contacto | Página /contacto | Nombre, email, teléfono, empresa, mensaje |
| Solicitud de Cotización | Botón en PDP o carrito | Nombre, email, teléfono, productos de interés, cantidad |
| Registro de Usuario | Crear cuenta | Nombre, email, teléfono, tipo de cliente (retail/B2B) |
| Newsletter | Suscripción a boletín | Email, nombre (opcional) |
| Chat/WhatsApp | Conversación iniciada | Nombre, teléfono/email, consulta |

### 2.3 Integración con Odoo CRM

Odoo incluye módulo **CRM** nativo. La integración es directa:

#### Crear Lead desde Formulario Web
```python
# Controller example
from odoo import http
from odoo.http import request

class WebsiteForm(http.Controller):
    @http.route('/contacto/submit', type='http', auth='public', website=True)
    def contact_form_submit(self, **post):
        # Crear lead en CRM
        lead = request.env['crm.lead'].sudo().create({
            'name': f"Web - {post.get('name')}",
            'contact_name': post.get('name'),
            'email_from': post.get('email'),
            'phone': post.get('phone'),
            'description': post.get('message'),
            'type': 'opportunity',
            'source_id': request.env.ref('utm.utm_source_website').id,
            'medium_id': request.env.ref('utm.utm_medium_website').id,
            'team_id': 1,  # ID del equipo de ventas
            'user_id': False,  # Asignar automáticamente o dejar sin asignar
        })
        
        # Enviar email de confirmación al cliente
        template = request.env.ref('website_crm.email_template_contact_confirmation')
        template.sudo().send_mail(lead.id, force_send=True)
        
        return request.render('website.contactus_thanks')
```

#### Formulario de Cotización desde Producto
```xml
<!-- Template en PDP -->
<form action="/shop/quote/submit" method="POST" class="js_quote_form">
    <input type="hidden" name="product_id" t-att-value="product.id"/>
    <input type="hidden" name="product_name" t-att-value="product.name"/>
    <div class="form-group">
        <input type="text" name="name" class="form-control" placeholder="Nombre completo" required="1"/>
    </div>
    <div class="form-group">
        <input type="email" name="email" class="form-control" placeholder="Email" required="1"/>
    </div>
    <div class="form-group">
        <input type="tel" name="phone" class="form-control" placeholder="Teléfono" required="1"/>
    </div>
    <div class="form-group">
        <input type="number" name="quantity" class="form-control" placeholder="Cantidad" value="1" min="1"/>
    </div>
    <button type="submit" class="btn btn-primary">Solicitar Cotización</button>
</form>
```

### 2.4 Campos UTM para Tracking de Origen

Agregar parámetros UTM en todos los formularios:
```html
<input type="hidden" name="utm_source" t-att-value="request.httprequest.args.get('utm_source', '')"/>
<input type="hidden" name="utm_medium" t-att-value="request.httprequest.args.get('utm_medium', '')"/>
<input type="hidden" name="utm_campaign" t-att-value="request.httprequest.args.get('utm_campaign', '')"/>
```

Odoo CRM automáticamente asocia estos valores al lead.

### 2.5 Automatizaciones Recomendadas

En Odoo CRM, configurar:
1. **Email automático** al crear lead: "Hemos recibido tu consulta"
2. **Asignación automática** por equipo/región
3. **Recordatorios** si lead no ha sido contactado en 24h
4. **Scoring** basado en: productos consultados, tamaño de empresa, respuestas en formulario

### 2.6 Integración con Sistemas Externos (Opcional)

Si se usa CRM externo (Salesforce, HubSpot, etc.):
- Webhook al crear lead en Odoo → API del CRM externo
- Sincronización bidireccional vía middleware (ej: Zapier, Make)

### 2.7 Validación
- [ ] Formularios crean leads en Odoo CRM
- [ ] Campos mapeados correctamente
- [ ] UTM parameters capturados
- [ ] Email de confirmación enviado al cliente
- [ ] Lead asignado al equipo/vendedor correcto
- [ ] Dashboard CRM muestra leads web

---

## 3. Canal de Contacto (WhatsApp/Chat)

### 3.1 Objetivo
Proveer canal directo de comunicación con clientes potenciales y existentes para consultas rápidas, soporte y cierre de ventas.

### 3.2 Opciones de Implementación

#### Opción A: WhatsApp Web (Simple)
Widget flotante que abre WhatsApp Web o app.

**Implementación:**
```html
<!-- Botón flotante de WhatsApp -->
<a href="https://wa.me/573001234567?text=Hola,%20tengo%20una%20consulta%20sobre%20productos" 
   class="whatsapp-float" 
   target="_blank"
   onclick="gtag('event', 'whatsapp_click', {'location': 'floating_button'});">
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
  box-shadow: 2px 2px 3px #999;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: 0.3s;
}
.whatsapp-float:hover {
  background-color: #128c7e;
  color: #FFF;
}
</style>
```

**Números de contacto por contexto:**
- Ventas generales: +57 300 123 4567
- Soporte técnico: +57 300 123 4568
- Proyectos B2B: +57 300 123 4569

**Mensaje pre-rellenado dinámico:**
```javascript
// En PDP
const productName = document.querySelector('.product-name').innerText;
const whatsappUrl = `https://wa.me/573001234567?text=Hola,%20me%20interesa%20${encodeURIComponent(productName)}`;
document.querySelector('.whatsapp-product-btn').href = whatsappUrl;
```

#### Opción B: WhatsApp Business API (Avanzado)
Requiere cuenta de WhatsApp Business y proveedor verificado (Twilio, MessageBird, etc.).

**Ventajas:**
- Mensajes automáticos (templates aprobados por WhatsApp)
- Integración con CRM
- Múltiples agentes
- Chatbot inicial

**Integración con Odoo:**
- Módulo de terceros: [WhatsApp Connector for Odoo](https://apps.odoo.com/)
- API REST → Webhook en Odoo → crear lead/ticket

#### Opción C: Chat en Vivo (Odoo Live Chat)
Odoo incluye módulo **Live Chat** nativo.

**Configuración:**
1. Instalar módulo `im_livechat`
2. Crear canal "Soporte Web Ferretería"
3. Asignar operadores
4. Insertar snippet de chat en website

**Personalización:**
```xml
<!-- Template override -->
<template id="livechat_button" inherit_id="im_livechat.loader">
    <xpath expr="//div[@class='o_livechat_button']" position="attributes">
        <attribute name="data-welcome-message">¡Hola! ¿En qué puedo ayudarte hoy?</attribute>
        <attribute name="data-default-username">Asesor de Ferretería</attribute>
    </xpath>
</template>
```

**Automatización:**
- Mensaje de bienvenida automático
- Si usuario abandona carrito → trigger de chat proactivo
- Horario de atención: mostrar mensaje fuera de horario

### 3.3 Decisión Recomendada

| Criterio | WhatsApp Web | WhatsApp Business API | Odoo Live Chat |
|----------|--------------|----------------------|----------------|
| Costo | Gratis | Medio/Alto | Incluido en Odoo |
| Implementación | Muy fácil | Compleja | Fácil |
| Escalabilidad | Baja | Alta | Media |
| Integración CRM | Manual | Automática | Automática |
| Múltiples agentes | No | Sí | Sí |
| Histórico | No | Sí | Sí |

**Recomendación MVP:**
1. **WhatsApp Web** (botón flotante) - Fase 7
2. **Odoo Live Chat** - Fase 7 (si se requiere chat en tiempo real)
3. **WhatsApp Business API** - Post-lanzamiento (escalamiento)

### 3.4 Integración con CRM

Cada conversación importante debe generar un lead/oportunidad:

**Proceso:**
1. Cliente contacta vía WhatsApp/Chat
2. Agente califica la consulta
3. Si es lead comercial → Crear manualmente en CRM o automatizar
4. Vincular conversación al lead (adjuntar captura o resumen)

**Automatización con Zapier/Make (ejemplo):**
- Trigger: Nuevo mensaje en WhatsApp Business
- Acción: Crear lead en Odoo vía API REST

### 3.5 Métricas a Monitorear
- Número de conversaciones iniciadas/día
- Tiempo promedio de respuesta
- Tasa de conversión: conversación → lead → venta
- Satisfacción del cliente (CSAT)

### 3.6 Validación
- [ ] Botón de WhatsApp visible en todas las páginas
- [ ] Número de teléfono correcto y formato internacional
- [ ] Mensaje pre-rellenado funciona correctamente
- [ ] Click en WhatsApp dispara evento GA4
- [ ] Live Chat (si aplica) funciona en horario de atención
- [ ] Conversaciones se registran en CRM

---

## 4. Trazabilidad de Eventos y Leads

### 4.1 Flujo Completo

```
Usuario Anónimo
    ↓
[Landing Page] → GA4: page_view + utm_params
    ↓
[Navega Catálogo] → GA4: view_item_list, view_item
    ↓
[Agrega al Carrito] → GA4: add_to_cart
    ↓
[Inicia Checkout] → GA4: begin_checkout
    ↓
OPCIÓN A: Completa Compra → GA4: purchase → CRM: Oportunidad Ganada
    ↓
OPCIÓN B: Abandona → Formulario de Cotización → CRM: Lead con productos de interés
    ↓
OPCIÓN C: Click en WhatsApp → GA4: whatsapp_click → Conversación → CRM: Lead manual
```

### 4.2 Dashboard Unificado (Recomendado)

Crear vista en Odoo que combine:
- **Tráfico Web** (GA4 via API o Looker Studio embedded)
- **Leads Activos** (Odoo CRM)
- **Conversaciones** (WhatsApp/Chat)
- **Ventas Completadas** (Odoo Sales)

**Herramientas:**
- Odoo Studio para dashboards personalizados
- Google Looker Studio + Odoo connector
- Tableau / Power BI (empresarial)

### 4.3 Atribución de Conversiones

Vincular venta con fuente original:
- **UTM Source/Medium/Campaign** en el lead
- **GA4 Client ID** almacenado en contacto/lead (opcional)
- **First Touch** vs **Last Touch** attribution

**Ejemplo de implementación:**
```python
# Al crear sale.order
order.write({
    'utm_source_id': lead.source_id.id,
    'utm_medium_id': lead.medium_id.id,
    'utm_campaign_id': lead.campaign_id.id,
})
```

### 4.4 Reportes Clave

1. **Reporte de Conversión por Canal**
   - Orgánico, Paid Search, Social, Directo, Referral
   - Tasa de conversión: visitas → leads → ventas

2. **Reporte de Productos Más Consultados**
   - GA4: view_item + add_to_cart sin purchase
   - Insights para estrategia comercial

3. **Reporte de Abandono de Carrito**
   - begin_checkout sin purchase
   - Valor potencial perdido
   - Estrategia de recuperación (email, WhatsApp)

---

## 5. Checklist de Implementación

### Fase 7.1: Google Analytics 4
- [ ] Crear cuenta GA4 y property
- [ ] Obtener Measurement ID (G-XXXXXXXXXX)
- [ ] Implementar gtag.js en todas las páginas (o GTM)
- [ ] Configurar eventos de e-commerce básicos
- [ ] Configurar eventos personalizados (search, filters, contact)
- [ ] Configurar User ID (si usuario registrado)
- [ ] Probar en GA4 DebugView
- [ ] Verificar transacciones aparecen en GA4 > Monetización

### Fase 7.2: Integración CRM
- [ ] Verificar módulo CRM instalado en Odoo
- [ ] Crear equipos de ventas (Retail, B2B, Soporte)
- [ ] Implementar formulario de contacto → crear lead
- [ ] Implementar formulario de cotización en PDP → crear lead
- [ ] Capturar UTM parameters en formularios
- [ ] Configurar email automático de confirmación
- [ ] Configurar asignación automática de leads
- [ ] Probar flujo completo: formulario → lead → email

### Fase 7.3: Canal de Contacto
- [ ] Decidir: WhatsApp Web, WhatsApp Business API, o Live Chat
- [ ] Implementar botón flotante de WhatsApp (opción simple)
- [ ] Configurar mensaje pre-rellenado dinámico
- [ ] Disparar evento GA4 al click en WhatsApp
- [ ] (Opcional) Configurar Odoo Live Chat
- [ ] (Opcional) Integrar WhatsApp Business API
- [ ] Documentar proceso de gestión de conversaciones → CRM
- [ ] Capacitar equipo en herramientas de chat

### Fase 7.4: Validación y Monitoreo
- [ ] Ejecutar pruebas end-to-end de todos los flujos
- [ ] Verificar trazabilidad: página → evento GA4 → lead CRM
- [ ] Validar datos correctos en GA4 (transaction_id, values)
- [ ] Validar leads en CRM con UTM correcto
- [ ] Configurar alertas en GA4 para anomalías
- [ ] Documentar procesos de seguimiento diario
- [ ] Capacitar equipo en lectura de dashboards

---

## 6. Consideraciones Técnicas

### 6.1 GDPR y Consentimiento de Cookies
- Implementar banner de cookies (Odoo tiene módulos disponibles)
- No disparar GA4 hasta que usuario acepte cookies
- Opción de opt-out

### 6.2 Rendimiento
- Cargar gtag.js de forma asíncrona
- Eventos GA4 no deben bloquear interacción del usuario
- Lazy load de widgets de chat si afectan First Contentful Paint

### 6.3 Testing
- **GA4**: Usar modo Debug, verificar eventos en tiempo real
- **CRM**: Crear leads de prueba, verificar asignación y emails
- **WhatsApp/Chat**: Probar en diferentes dispositivos y navegadores

### 6.4 Mantenimiento
- Revisar semanalmente eventos GA4 rotos (cambios en DOM)
- Auditar mensualmente leads duplicados en CRM
- Actualizar números de WhatsApp y horarios de atención

---

## 7. Recursos y Referencias

### Documentación Oficial
- [GA4 E-commerce Events](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce)
- [Odoo CRM Documentation](https://www.odoo.com/documentation/17.0/applications/sales/crm.html)
- [WhatsApp Business API](https://developers.facebook.com/docs/whatsapp)
- [Odoo Live Chat](https://www.odoo.com/documentation/17.0/applications/websites/livechat.html)

### Módulos Odoo Recomendados
- `website_sale` (base)
- `crm` (CRM nativo)
- `im_livechat` (Live Chat)
- `website_crm` (Formularios → CRM)
- `utm` (UTM tracking)

### Herramientas de Testing
- [GA4 DebugView](https://support.google.com/analytics/answer/7201382)
- [Google Tag Assistant](https://tagassistant.google.com/)
- [Odoo Debug Mode](https://www.odoo.com/documentation/17.0/developer/reference/frontend/framework.html#debug-mode)
