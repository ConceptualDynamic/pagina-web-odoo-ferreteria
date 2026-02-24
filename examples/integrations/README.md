# Ejemplos de Implementación - Integraciones

Este directorio contiene ejemplos de código y configuraciones para implementar las integraciones de Fase 7: GA4, CRM y WhatsApp/Chat.

## Estructura de Archivos

```
examples/integrations/
├── README.md                      # Este archivo
├── config.json                    # Configuración centralizada de integraciones
├── ga4_tracking.js               # Script completo de tracking GA4
├── crm_lead_capture.py           # Controller de Odoo para captura de leads
└── whatsapp_integration.py       # Templates y snippets de WhatsApp
```

## Guía de Uso

### 1. Google Analytics 4 (ga4_tracking.js)

**Propósito:** Rastrear eventos de e-commerce y personalizados en GA4.

**Instalación:**

1. Copiar el archivo `ga4_tracking.js` a tu módulo de Odoo:
   ```
   tu_modulo/static/src/js/ga4_tracking.js
   ```

2. Registrar el asset en `__manifest__.py`:
   ```python
   'assets': {
       'web.assets_frontend': [
           'tu_modulo/static/src/js/ga4_tracking.js',
       ],
   }
   ```

3. Editar el archivo y reemplazar:
   - `G-XXXXXXXXXX` con tu Measurement ID real
   - Ajustar `CURRENCY` si no es COP

4. Asegurar que gtag.js esté cargado antes en el template base:
   ```xml
   <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
   ```

**Uso Manual:**

```javascript
// Rastrear vista de producto manualmente
trackViewItem({
    id: '12345',
    name: 'Taladro Percutor',
    price: 150000,
    category: 'Herramientas Eléctricas',
    quantity: 1
});

// Rastrear compra manualmente
trackPurchase({
    orderId: 'SO-2024-001',
    total: 285000,
    tax: 54000,
    shipping: 15000,
    items: [/* array de productos */]
});
```

**Verificación:**
- Abrir Chrome DevTools → Console
- Ejecutar: `window.dataLayer`
- Verificar que el array contiene eventos
- Usar GA4 DebugView para ver eventos en tiempo real

---

### 2. CRM Lead Capture (crm_lead_capture.py)

**Propósito:** Capturar leads desde formularios web y crear registros en Odoo CRM.

**Instalación:**

1. Crear módulo personalizado de Odoo (si no existe):
   ```bash
   odoo scaffold website_crm_lead_capture /path/to/addons
   ```

2. Copiar el controller a:
   ```
   website_crm_lead_capture/controllers/main.py
   ```

3. Agregar dependencias en `__manifest__.py`:
   ```python
   'depends': ['website', 'website_sale', 'crm', 'utm'],
   ```

4. Crear templates de confirmación en `views/website_templates.xml`:
   ```xml
   <template id="contactus_thanks" name="Contact Us - Thank You">
       <t t-call="website.layout">
           <div class="container">
               <h1>¡Gracias por contactarnos!</h1>
               <p>Hemos recibido tu mensaje y te responderemos pronto.</p>
           </div>
       </t>
   </template>
   ```

5. Instalar módulo:
   ```bash
   odoo -u website_crm_lead_capture -d tu_database
   ```

**Endpoints disponibles:**

- `POST /contacto/submit` - Formulario de contacto general
- `POST /shop/quote/submit` - Solicitud de cotización desde producto
- `POST /newsletter/subscribe` (JSON) - Suscripción a newsletter

**Ejemplo de formulario HTML:**

```html
<form action="/contacto/submit" method="POST">
    <input type="hidden" name="csrf_token" t-att-value="request.csrf_token()"/>
    <input type="text" name="name" placeholder="Nombre completo" required="1"/>
    <input type="email" name="email" placeholder="Email" required="1"/>
    <input type="tel" name="phone" placeholder="Teléfono"/>
    <textarea name="message" placeholder="Tu mensaje"></textarea>
    
    <!-- UTM Tracking -->
    <input type="hidden" name="utm_source" t-att-value="request.httprequest.args.get('utm_source', '')"/>
    <input type="hidden" name="utm_medium" t-att-value="request.httprequest.args.get('utm_medium', '')"/>
    <input type="hidden" name="utm_campaign" t-att-value="request.httprequest.args.get('utm_campaign', '')"/>
    
    <button type="submit" class="btn btn-primary">Enviar</button>
</form>
```

**Verificación:**
- Enviar formulario de prueba
- Ir a Odoo: CRM → Leads
- Verificar que se creó el lead con datos correctos
- Verificar email de confirmación recibido

---

### 3. WhatsApp Integration (whatsapp_integration.py)

**Propósito:** Implementar botón flotante de WhatsApp y widget multi-agente.

**Opciones Disponibles:**

#### Opción A: Botón Flotante Simple (Recomendado para MVP)

1. Copiar HTML, CSS y JS de `WHATSAPP_FLOAT_BUTTON_*` al template base de tu website
2. Editar número de teléfono: `573001234567` → tu número real
3. Ajustar mensaje por defecto si es necesario

**Insertar en website layout:**

```xml
<template id="layout" inherit_id="website.layout">
    <xpath expr="//main" position="after">
        <!-- HTML del botón aquí -->
        <a href="https://wa.me/573001234567?text=Hola,%20tengo%20una%20consulta" 
           class="whatsapp-float" 
           target="_blank">
            <i class="fa fa-whatsapp"></i>
        </a>
        
        <style>
            /* CSS del botón aquí */
        </style>
        
        <script>
            // JavaScript del botón aquí
        </script>
    </xpath>
</template>
```

#### Opción B: Widget Multi-Agente

Para soporte de múltiples departamentos, usar el código en `WHATSAPP_MULTI_AGENT_HTML`.

1. Copiar HTML completo (ya incluye CSS y JS)
2. Editar números de teléfono para cada departamento
3. Ajustar avatares de agentes (usar imágenes reales)
4. Insertar antes del cierre de `</body>`

#### Opción C: Template QWeb de Odoo

Para integración nativa con Odoo:

1. Copiar código de `ODOO_QWEB_TEMPLATE` a `views/website_templates.xml`
2. Agregar campo `whatsapp_phone` al modelo Website:
   ```python
   # Copiar código de ODOO_PYTHON_MODEL
   ```
3. Configurar número en Odoo: Website → Configuration → Settings

**Verificación:**
- Botón visible en todas las páginas
- Click en móvil abre app de WhatsApp
- Click en desktop abre WhatsApp Web
- Mensaje pre-rellenado aparece correctamente
- Evento GA4 se dispara (verificar en DevTools)

---

## Configuración Centralizada (config.json)

El archivo `config.json` contiene configuración de referencia para todas las integraciones.

**NO es un archivo funcional** directamente, sino una guía de configuración. Usarlo como referencia para:

1. Verificar qué integraciones habilitar
2. Definir endpoints y teams de CRM
3. Configurar números de WhatsApp por departamento
4. Establecer horarios de atención
5. Configurar alertas de monitoreo

**Variables a personalizar:**

```json
{
  "ga4.measurement_id": "Tu Measurement ID real",
  "whatsapp.phone_numbers.sales": "Tu número de WhatsApp",
  "crm.lead_sources.contact_form.team_id": "ID del equipo en Odoo",
  // ... etc
}
```

---

## Flujo de Implementación Recomendado

### Fase 1: GA4 Básico
1. Crear cuenta GA4 y obtener Measurement ID
2. Implementar gtag.js en todas las páginas
3. Implementar `ga4_tracking.js`
4. Verificar eventos en DebugView
5. Configurar conversiones

**Tiempo estimado:** 2-4 horas

### Fase 2: CRM Lead Capture
1. Verificar módulo CRM instalado
2. Implementar controller `crm_lead_capture.py`
3. Crear templates de confirmación
4. Configurar equipos de ventas y UTM
5. Probar formularios end-to-end

**Tiempo estimado:** 4-6 horas

### Fase 3: WhatsApp/Chat
1. Obtener número de WhatsApp Business
2. Implementar botón flotante (Opción A simple)
3. Agregar tracking GA4 al click
4. Configurar mensajes contextuales (opcional)
5. Documentar proceso WhatsApp → CRM

**Tiempo estimado:** 2-3 horas

### Fase 4: Validación y Documentación
1. Ejecutar checklist de validación
2. Configurar alertas de monitoreo
3. Capacitar equipo
4. Actualizar privacy policy

**Tiempo estimado:** 3-4 horas

**Total estimado:** 11-17 horas de desarrollo + QA

---

## Recursos Adicionales

### Documentación
- [docs/08-integraciones.md](../../docs/08-integraciones.md) - Guía completa de integraciones
- [docs/checklist-integraciones.md](../../docs/checklist-integraciones.md) - Checklist de validación

### Herramientas de Testing
- [GA4 DebugView](https://analytics.google.com/analytics/web/#/debugview)
- [Google Tag Assistant](https://tagassistant.google.com/)
- [WhatsApp Click to Chat](https://wa.me/) - Generador de enlaces

### APIs y Referencias
- [GA4 E-commerce Events](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce)
- [Odoo CRM API](https://www.odoo.com/documentation/17.0/developer/reference/backend/orm.html)
- [WhatsApp Business API](https://developers.facebook.com/docs/whatsapp)

---

## Soporte y Preguntas

Para preguntas sobre implementación:
1. Revisar documentación en `docs/08-integraciones.md`
2. Consultar checklist en `docs/checklist-integraciones.md`
3. Contactar al equipo técnico

---

## Changelog

| Fecha | Versión | Cambios |
|-------|---------|---------|
| 2024-02-24 | 1.0 | Creación inicial de ejemplos para Fase 7 |

---

## Licencia

Estos ejemplos son proporcionados como guía de implementación para el proyecto pagina-web-odoo-ferreteria.
Código adaptable según necesidades específicas del proyecto.
