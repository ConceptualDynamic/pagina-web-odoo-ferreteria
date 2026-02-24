# Checklist de Validación - Fase 7: Integraciones

Este documento proporciona una lista de verificación completa para validar la implementación de las integraciones de GA4, CRM y WhatsApp/Chat.

## 1. Google Analytics 4 (GA4)

### 1.1 Instalación y Configuración Base

- [ ] **Cuenta GA4 creada**
  - Property configurada para el dominio correcto
  - Measurement ID obtenido (formato: G-XXXXXXXXXX)
  - Zona horaria configurada (Colombia: UTC-5)

- [ ] **Tag instalado correctamente**
  - Script gtag.js presente en `<head>` de todas las páginas
  - O configurado vía Google Tag Manager
  - Variable de configuración en Odoo (`website.google_analytics_key`)

- [ ] **Verificación técnica básica**
  - Tag se carga sin errores en consola del navegador
  - `dataLayer` array existe en `window.dataLayer`
  - DebugView de GA4 muestra eventos en tiempo real
  - Extensión Google Tag Assistant confirma instalación

### 1.2 Eventos de E-commerce

#### Eventos Básicos
- [ ] **view_item_list** - Ver listado de productos
  - Se dispara al cargar PLP (Product Listing Page)
  - Incluye array de productos con: item_id, item_name, price
  - Parámetro `item_list_name` presente

- [ ] **view_item** - Ver detalle de producto
  - Se dispara al cargar PDP (Product Detail Page)
  - Incluye: item_id, item_name, item_category, item_brand, price
  - Valor (`value`) del producto incluido

- [ ] **add_to_cart** - Agregar al carrito
  - Se dispara al hacer click en "Agregar al carrito"
  - Cantidad correcta incluida
  - Valor calculado correctamente (precio × cantidad)

- [ ] **remove_from_cart** - Remover del carrito
  - Se dispara al eliminar producto del carrito
  - Producto correcto identificado

- [ ] **begin_checkout** - Iniciar checkout
  - Se dispara al acceder a página de checkout
  - Lista completa de productos en carrito incluida
  - Valor total del carrito correcto

- [ ] **add_shipping_info** - Información de envío
  - Se dispara al completar datos de envío
  - `shipping_tier` incluido (ej: "domicilio", "punto_entrega")

- [ ] **add_payment_info** - Información de pago
  - Se dispara al seleccionar método de pago
  - `payment_type` incluido (ej: "tarjeta", "pse", "contraentrega")

- [ ] **purchase** - Compra completada
  - Se dispara SOLO en página de confirmación de pedido
  - `transaction_id` único (ej: ID del pedido en Odoo)
  - Valor, tax, shipping incluidos correctamente
  - Items con cantidades y precios correctos
  - Coupon incluido si se aplicó descuento

#### Validaciones de Datos
- [ ] **Moneda correcta**: Todos los eventos usan `currency: 'COP'`
- [ ] **Valores numéricos**: Precios, cantidades, totales son números, no strings
- [ ] **IDs únicos**: `item_id` corresponde a SKU o ID real del producto
- [ ] **Transaction ID único**: Cada compra tiene ID diferente, no se repiten

### 1.3 Eventos Personalizados

- [ ] **search** - Búsqueda de productos
  - Se dispara al enviar formulario de búsqueda
  - Parámetro `search_term` con término buscado

- [ ] **filter_products** - Aplicar filtros
  - Se dispara al aplicar filtro (marca, precio, categoría)
  - Parámetros: `filter_type`, `filter_value`

- [ ] **contact_form_submit** - Envío de formulario de contacto
  - Se dispara al enviar formulario
  - Parámetro `form_type` identifica tipo de formulario

- [ ] **whatsapp_click** - Click en botón de WhatsApp
  - Se dispara al hacer click en cualquier botón de WhatsApp
  - Parámetro `location` indica dónde estaba el botón

- [ ] **phone_click** - Click en número telefónico (si aplica)
  - Se dispara al hacer click en número de teléfono
  - Parámetro `location` indica contexto

### 1.4 User Properties

- [ ] **User ID** (opcional)
  - Configurado si usuario está logueado
  - ID corresponde a ID de partner en Odoo
  - Privacy policy actualizada mencionando User ID

- [ ] **Custom User Properties** (opcional)
  - `customer_type`: 'guest', 'registered', 'b2b'
  - `lifetime_value`: Valor acumulado de compras
  - `order_count`: Número de pedidos completados

### 1.5 Verificación en GA4

- [ ] **Tiempo Real**: Eventos aparecen en "Realtime" report
- [ ] **DebugView**: Eventos correctos en DebugView (con detalles completos)
- [ ] **Conversiones configuradas**: `purchase` marcado como conversión
- [ ] **Reportes**: Datos aparecen en reportes de E-commerce (puede tomar 24-48h)
- [ ] **Exploración**: Crear exploración personalizada funciona correctamente

### 1.6 Testing

- [ ] **Test end-to-end**: Flujo completo de compra dispara todos los eventos
  1. Buscar producto → `search`
  2. Ver listado → `view_item_list`
  3. Ver detalle → `view_item`
  4. Agregar al carrito → `add_to_cart`
  5. Ir a checkout → `begin_checkout`
  6. Completar envío → `add_shipping_info`
  7. Seleccionar pago → `add_payment_info`
  8. Confirmar pedido → `purchase`

- [ ] **Diferentes navegadores**: Chrome, Firefox, Safari, Edge
- [ ] **Dispositivos**: Desktop, tablet, móvil
- [ ] **Adblockers**: Verificar comportamiento con bloqueadores (informar que pueden bloquear)

---

## 2. Integración CRM

### 2.1 Configuración Base

- [ ] **Módulo CRM instalado** en Odoo
- [ ] **Equipos de ventas creados**
  - Ventas Retail
  - Ventas B2B (si aplica)
  - Soporte/Atención (si aplica)

- [ ] **UTM configurados**
  - UTM Source: website, google, facebook, etc.
  - UTM Medium: organic, cpc, social, email, etc.
  - UTM Campaign: campañas activas

### 2.2 Formularios → Leads

#### Formulario de Contacto
- [ ] **Formulario funcional** en página `/contacto`
- [ ] **Campos capturados**:
  - Nombre completo
  - Email
  - Teléfono
  - Empresa (opcional)
  - Mensaje

- [ ] **Lead creado en CRM** al enviar formulario
- [ ] **Datos mapeados correctamente**:
  - `name`: "Web - Contacto: [Nombre]"
  - `contact_name`: Nombre del cliente
  - `email_from`: Email
  - `phone`: Teléfono
  - `description`: Mensaje

- [ ] **UTM capturados**: source, medium, campaign presentes en lead
- [ ] **Equipo asignado**: Lead asignado al equipo correcto
- [ ] **Email de confirmación enviado** al cliente

#### Formulario de Cotización (desde PDP)
- [ ] **Botón "Solicitar Cotización"** visible en PDP
- [ ] **Formulario funcional** con campos:
  - Nombre
  - Email
  - Teléfono
  - Cantidad
  - Mensaje adicional (opcional)

- [ ] **Oportunidad creada en CRM** (no solo lead)
- [ ] **Datos de producto incluidos**:
  - Nombre del producto
  - SKU
  - Cantidad solicitada
  - Precio estimado

- [ ] **Expected revenue** calculado automáticamente
- [ ] **Prioridad más alta** que leads de contacto general
- [ ] **Email de confirmación** con resumen de solicitud

#### Newsletter / Suscripciones
- [ ] **Formulario de suscripción** funcional
- [ ] **Lead creado** con prioridad baja
- [ ] **Agregado a lista de correo** (Odoo Mass Mailing)
- [ ] **No duplicar** si email ya existe

### 2.3 Automatizaciones CRM

- [ ] **Email automático** al crear lead (template configurado)
- [ ] **Asignación automática** por equipo o regla
- [ ] **Recordatorio** si lead no contactado en 24h (opcional)
- [ ] **Scoring automático** (opcional, según criterios de negocio)

### 2.4 Validación de Datos

- [ ] **Leads sin duplicar** (validación por email)
- [ ] **UTM correctos** en todos los leads web
- [ ] **Source siempre es "Website"** para formularios web
- [ ] **Estados correctos**: Lead → Qualified → Opportunity → Won/Lost

### 2.5 Dashboard y Reportes

- [ ] **Vista Kanban** de leads funciona
- [ ] **Filtros por origen** (Web, Phone, Email, etc.)
- [ ] **Reporte de conversión** web leads → ventas
- [ ] **Gráficos de pipeline** muestran leads web

### 2.6 Testing End-to-End

- [ ] **Test formulario de contacto**:
  1. Completar formulario
  2. Verificar lead en CRM
  3. Verificar email de confirmación
  4. Verificar UTM si viene de campaña

- [ ] **Test solicitud de cotización**:
  1. Desde PDP, solicitar cotización
  2. Verificar oportunidad en CRM
  3. Verificar datos de producto correctos
  4. Verificar expected revenue
  5. Verificar email al cliente

- [ ] **Test newsletter**:
  1. Suscribirse
  2. Verificar lead en CRM
  3. Verificar en lista de mailing
  4. Intentar duplicar (debe prevenir)

---

## 3. Canal de Contacto (WhatsApp/Chat)

### 3.1 WhatsApp - Configuración

- [ ] **Número de WhatsApp Business** verificado y activo
- [ ] **Perfil completo** (foto, descripción, horarios, categoría)
- [ ] **Formato de número correcto**: +573001234567 o 573001234567

### 3.2 Implementación - Botón Flotante

- [ ] **Botón flotante visible** en todas las páginas
- [ ] **Posicionado correctamente** (esquina inferior derecha)
- [ ] **Diseño correcto**: Fondo verde (#25d366), icono de WhatsApp
- [ ] **Responsive**: Se adapta bien en móvil, tablet, desktop

- [ ] **Click abre WhatsApp**:
  - En móvil: Abre app de WhatsApp
  - En desktop: Abre WhatsApp Web
  - En ambos: Mensaje pre-rellenado aparece

### 3.3 Mensajes Pre-rellenados

- [ ] **Mensaje por defecto** funciona: "Hola, tengo una consulta"

- [ ] **Mensajes contextuales** (si implementados):
  - Home: "Hola, quisiera información sobre productos"
  - PDP: "Hola, me interesa [NOMBRE_PRODUCTO]"
  - Carrito: "Hola, tengo productos en carrito y quisiera consultar"
  - Categoría: "Hola, busco productos en [CATEGORÍA]"

- [ ] **Mensaje en español** y sin caracteres extraños al abrir

### 3.4 Widget Multi-Agente (si aplica)

- [ ] **Widget expandible** funciona correctamente
- [ ] **Múltiples opciones** visibles (Ventas, Soporte, B2B)
- [ ] **Cada opción** abre número correcto con mensaje apropiado
- [ ] **Fotos de agentes** (avatares) se cargan
- [ ] **Horarios de atención** visibles

### 3.5 Tracking GA4

- [ ] **Evento `whatsapp_click`** se dispara al hacer click
- [ ] **Parámetros correctos**:
  - `location`: URL actual o contexto
  - `button_type`: 'floating', 'multi_agent', 'product_page', etc.
  - `department`: si aplica (ventas, soporte, etc.)

- [ ] **Eventos visibles** en GA4 DebugView y Realtime

### 3.6 Odoo Live Chat (Alternativa)

Si se implementa Live Chat en lugar o además de WhatsApp:

- [ ] **Módulo `im_livechat` instalado**
- [ ] **Canal creado** con nombre apropiado
- [ ] **Operadores asignados** al canal
- [ ] **Widget visible** en website
- [ ] **Mensaje de bienvenida** personalizado
- [ ] **Horarios configurados**: Mensaje fuera de horario
- [ ] **Conversaciones guardadas** en historial
- [ ] **Integración con CRM**: Conversaciones → Leads (manual o automático)

### 3.7 Integración WhatsApp con CRM

- [ ] **Proceso documentado** para agentes:
  1. Cliente contacta por WhatsApp
  2. Agente evalúa intención comercial
  3. Si es lead → Crear en CRM manualmente
  4. Adjuntar resumen de conversación

- [ ] **Template de lead** desde WhatsApp en CRM:
  - Name: "WhatsApp - [Nombre cliente]"
  - Source: WhatsApp
  - Description: Resumen de consulta

- [ ] **Capacitación** a equipo sobre proceso

### 3.8 Testing Completo

- [ ] **Test desde móvil**:
  - Android: Abre app de WhatsApp
  - iOS: Abre app de WhatsApp
  - Mensaje pre-rellenado correcto

- [ ] **Test desde desktop**:
  - Chrome, Firefox, Safari, Edge
  - Abre WhatsApp Web
  - Mensaje pre-rellenado correcto

- [ ] **Test de diferentes páginas**:
  - Home → Mensaje genérico
  - PDP → Mensaje con nombre de producto
  - Carrito → Mensaje sobre carrito
  - Contacto → Mensaje sobre consulta

- [ ] **Test de tracking**:
  - Click en botón
  - Verificar evento en GA4 DebugView
  - Verificar parámetros correctos

---

## 4. Trazabilidad y Reportes

### 4.1 Flujo Completo de Usuario

Validar flujo completo de ejemplo:

```
Usuario anónimo → Landing Page (utm_source=google, utm_campaign=promo2024)
    ↓ GA4: page_view con UTM
Navega catálogo
    ↓ GA4: view_item_list, view_item
Agrega producto al carrito
    ↓ GA4: add_to_cart
Inicia checkout
    ↓ GA4: begin_checkout
Completa datos de envío
    ↓ GA4: add_shipping_info
Selecciona pago
    ↓ GA4: add_payment_info
Confirma pedido
    ↓ GA4: purchase
    ↓ CRM: Oportunidad ganada (si se capturó lead antes)
```

- [ ] **Todos los eventos se disparan** en orden correcto
- [ ] **UTM se mantienen** a lo largo de la sesión
- [ ] **Transaction ID único** en evento purchase
- [ ] **Venta vinculada** a lead original si existía

### 4.2 Atribución de Conversiones

- [ ] **UTM en Sale Order**: Pedido de venta tiene UTM del lead original
- [ ] **Dashboard de atribución**: Vista en Odoo o Looker Studio con:
  - Ventas por canal (Organic, Paid, Social, Direct)
  - ROI por campaña
  - Tasa de conversión por source/medium

### 4.3 Reportes Clave

- [ ] **Reporte: Conversión por Canal**
  - Tabla: Source → Sesiones → Leads → Ventas → Revenue
  - Métrica: Conversion rate, Revenue per session

- [ ] **Reporte: Productos Más Consultados (sin compra)**
  - GA4: `view_item` + `add_to_cart` sin `purchase`
  - Insight para estrategia comercial

- [ ] **Reporte: Abandono de Carrito**
  - GA4: `begin_checkout` sin `purchase`
  - Lista de productos abandonados
  - Valor potencial perdido

- [ ] **Dashboard CRM: Leads Web**
  - Filtro por source=Website
  - KPIs: Leads generados, conversion rate, tiempo promedio de cierre
  - Tendencia semanal/mensual

### 4.4 Alertas y Monitoreo

- [ ] **Alerta GA4**: Si eventos de purchase caen a 0 en un día
- [ ] **Alerta CRM**: Si no se crean leads web en 24h (indica fallo)
- [ ] **Revisión semanal**: Equipo revisa dashboard de conversión

---

## 5. Documentación y Capacitación

### 5.1 Documentación Técnica

- [ ] **README actualizado** con instrucciones de integración
- [ ] **Documento de arquitectura** incluye diagrama de integraciones
- [ ] **Códigos de ejemplo** disponibles en `/examples/integrations/`
- [ ] **Variables de entorno** documentadas (GA4 Measurement ID, WhatsApp phone)

### 5.2 Documentación de Usuario

- [ ] **Manual de operación** para equipo de ventas:
  - Cómo ver leads en CRM
  - Cómo responder leads web
  - Proceso de WhatsApp → CRM

- [ ] **Manual de análisis** para marketing:
  - Cómo acceder a GA4
  - Cómo interpretar reportes
  - Métricas clave a monitorear

### 5.3 Capacitación

- [ ] **Sesión de capacitación** realizada con equipo:
  - Demostración de integraciones
  - Flujos de trabajo en CRM
  - Interpretación de reportes GA4

- [ ] **Video tutorial** grabado (opcional pero recomendado)

---

## 6. Compliance y Privacidad

### 6.1 GDPR y Protección de Datos

- [ ] **Privacy Policy actualizada** mencionando:
  - Uso de Google Analytics
  - Cookies de tracking
  - Captura de datos en formularios
  - Uso de User ID (si aplica)

- [ ] **Banner de cookies** implementado
  - Opción de aceptar/rechazar
  - GA4 no se carga hasta aceptación
  - Persistencia de preferencia

- [ ] **Opción de opt-out** de tracking disponible

### 6.2 Términos y Condiciones

- [ ] **Términos actualizados** mencionando:
  - Uso de WhatsApp como canal de contacto
  - Tratamiento de datos en CRM

---

## 7. Rendimiento y Optimización

### 7.1 Performance

- [ ] **Lighthouse Score** no empeoró significativamente:
  - Performance > 80
  - Best Practices > 90

- [ ] **Scripts asíncronos**: gtag.js carga de forma asíncrona (no bloquea)
- [ ] **WhatsApp widget**: No afecta First Contentful Paint
- [ ] **Lazy load** de recursos de terceros si es posible

### 7.2 Mantenimiento

- [ ] **Proceso de revisión mensual** definido:
  - Auditar eventos GA4 funcionando
  - Revisar leads duplicados en CRM
  - Actualizar números de WhatsApp si cambian

- [ ] **Alertas automáticas** configuradas para detectar fallos

---

## 8. Checklist de Go-Live

Antes de considerar la Fase 7 completada:

- [ ] ✅ **GA4 instalado y validado** en producción
- [ ] ✅ **Todos los eventos de e-commerce** funcionando
- [ ] ✅ **Formularios web → CRM** funcionando
- [ ] ✅ **WhatsApp/Chat funcional** y trackeado
- [ ] ✅ **Trazabilidad end-to-end** validada
- [ ] ✅ **Dashboard de reportes** configurado
- [ ] ✅ **Equipo capacitado** en herramientas
- [ ] ✅ **Documentación completa** entregada
- [ ] ✅ **Testing en múltiples dispositivos/navegadores** exitoso
- [ ] ✅ **Privacy policy y cookies** actualizados
- [ ] ✅ **Alertas de monitoreo** configuradas

---

## Notas Finales

- Este checklist debe ser revisado item por item antes de cerrar la Fase 7
- Cualquier item que no aplique debe ser marcado como N/A con justificación
- Items críticos (marcados con ⚠️ en documentación) deben ser completados sin excepción
- Items opcionales pueden ser pospuestos para post-lanzamiento si se documenta

**Responsables de validación:**
- Técnico: [Nombre]
- Marketing/Analytics: [Nombre]
- Comercial/CRM: [Nombre]
- QA: [Nombre]

**Fecha de validación:** __________

**Firma de aprobación:** __________
