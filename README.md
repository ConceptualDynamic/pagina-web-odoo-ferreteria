# Página Web Odoo Ferretería

Proyecto para construir y operar una web de ferretería en Odoo.

## Objetivo
Implementar un sitio transaccional y escalable en Odoo, con catálogo, checkout, SEO base, integraciones y operación post-lanzamiento.

## Enlaces
- Repositorio: https://github.com/ConceptualDynamic/pagina-web-odoo-ferreteria
- Planner (Plan): Software Development

## Estructura documental

### Documentos principales
- `docs/01-alcance-kpis.md` - Alcance del proyecto y KPIs de negocio
- `docs/02-roadmap-fases.md` - Roadmap de fases del proyecto
- `docs/03-arquitectura-informacion.md` - Arquitectura de información y navegación
- `docs/04-catalogo-y-datos.md` - Catálogo de productos y gestión de datos
- `docs/05-diseno-ux-ui.md` - Diseño UX/UI y páginas clave
- `docs/06-pagos-envios-impuestos.md` - Pagos, envíos e impuestos
- `docs/07-seo-y-contenido.md` - SEO y estrategia de contenido
- `docs/08-integraciones.md` - **Integraciones: GA4, CRM, WhatsApp/Chat** ⭐
- `docs/09-qa.md` - Quality Assurance y pruebas
- `docs/10-go-live-y-monitoreo.md` - Go-live y monitoreo
- `docs/11-matriz-github-planner.md` - Matriz GitHub-Planner

### Documentos de implementación
- `docs/checklist-integraciones.md` - Checklist de validación para Fase 7 ✓

### Ejemplos de código
- `examples/integrations/` - Ejemplos de implementación para integraciones
  - `README.md` - Guía de uso de ejemplos
  - `ga4_tracking.js` - Script completo de tracking GA4
  - `crm_lead_capture.py` - Controller Odoo para captura de leads
  - `whatsapp_integration.py` - Templates de integración WhatsApp
  - `config.json` - Configuración de referencia

## Convención de seguimiento (Opción 3)
GitHub Project = hub de producto/roadmap técnico.
Planner = ejecución operativa diaria.

## Fase 7: Integraciones (Completada)

La **Fase 7** se enfoca en conectar analítica, gestión de leads y canal de contacto directo:

### ✅ Implementado

1. **Google Analytics 4 (GA4)**
   - Guía completa de configuración e instalación
   - Schema de eventos de e-commerce (view_item, add_to_cart, purchase, etc.)
   - Eventos personalizados (search, filters, contact_form, whatsapp_click)
   - Script JavaScript listo para implementar (`ga4_tracking.js`)

2. **Integración CRM**
   - Captura de leads desde formularios web → Odoo CRM
   - Formulario de contacto general
   - Solicitud de cotización desde productos
   - Suscripción a newsletter
   - Tracking UTM para atribución de conversiones
   - Controller Python completo (`crm_lead_capture.py`)

3. **Canal de Contacto (WhatsApp/Chat)**
   - Botón flotante de WhatsApp (implementación simple)
   - Widget multi-agente para múltiples departamentos
   - Mensajes pre-rellenados contextuales
   - Templates QWeb para integración nativa con Odoo
   - Alternativa: Odoo Live Chat

### 📚 Documentación Entregada

- **Guía técnica completa**: `docs/08-integraciones.md` (541 líneas)
- **Checklist de validación**: `docs/checklist-integraciones.md` (522 líneas)
- **Ejemplos de código**: `examples/integrations/` (4 archivos, ~1700 líneas)
- **Configuración de referencia**: `examples/integrations/config.json`

### 🚀 Próximos Pasos

Para implementar las integraciones:

1. Revisar la documentación completa en `docs/08-integraciones.md`
2. Consultar ejemplos en `examples/integrations/README.md`
3. Adaptar código según necesidades específicas del proyecto
4. Seguir checklist de validación en `docs/checklist-integraciones.md`
5. Capacitar al equipo en el uso de herramientas (GA4, CRM, WhatsApp)

**Tiempo estimado de implementación:** 11-17 horas desarrollo + QA
