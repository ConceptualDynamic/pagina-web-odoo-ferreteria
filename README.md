# Página Web Odoo Ferretería

Proyecto para construir y operar una web de ferretería en Odoo.

## Objetivo
Implementar un sitio transaccional y escalable en Odoo, con catálogo, checkout, SEO base, integraciones y operación post-lanzamiento.

## Enlaces
- Repositorio: https://github.com/ConceptualDynamic/pagina-web-odoo-ferreteria
- Planner (Plan): Software Development

## Estado del proyecto

### Fases completadas
- ✅ **Fase 5**: Checkout, pagos y envíos - Configuración E2E con validaciones, métodos de pago y envío personalizados

## Estructura documental

### Documentación general
- `docs/01-alcance-kpis.md` - Alcance del proyecto y KPIs
- `docs/02-roadmap-fases.md` - Roadmap por fases
- `docs/03-arquitectura-informacion.md` - Arquitectura de información
- `docs/04-catalogo-y-datos.md` - Catálogo y gestión de datos
- `docs/05-diseno-ux-ui.md` - Diseño UX/UI
- `docs/07-seo-y-contenido.md` - SEO y contenido
- `docs/08-integraciones.md` - Integraciones externas
- `docs/09-qa.md` - Quality Assurance
- `docs/10-go-live-y-monitoreo.md` - Go-live y monitoreo
- `docs/11-matriz-github-planner.md` - Matriz GitHub-Planner

### Documentación de Fase 5: Checkout
- `docs/06-pagos-envios-impuestos.md` - Guía completa de configuración
- `docs/06.1-implementacion-checkout.md` - Guía técnica de implementación
- `docs/06.2-testing-checklist.md` - Checklist de testing E2E

## Módulos Odoo

### `odoo_modules/ferreteria_checkout`
Módulo personalizado para el proceso de checkout con:
- Validación de stock en tiempo real
- Múltiples métodos de pago (transferencia, pago en tienda, tarjetas)
- Métodos de envío configurables (retiro, estándar, express)
- Sistema de cupones de descuento
- Restricciones por peso y tipo de producto
- Emails personalizados de confirmación
- Validaciones de formulario

Ver `odoo_modules/ferreteria_checkout/README.md` para más detalles.

## Instalación

### Prerequisitos
- Odoo 16.0 o superior
- Python 3.8+
- PostgreSQL 12+

### Instalar módulo de checkout
```bash
# Copiar módulo a directorio de addons
cp -r odoo_modules/ferreteria_checkout /path/to/odoo/addons/

# Actualizar lista de módulos
odoo-bin -c /etc/odoo/odoo.conf -d ferreteria -u all

# Instalar desde UI
# Apps → Buscar "Ferretería Checkout" → Instalar
```

## Configuración

Seguir las guías de configuración en:
1. `docs/06-pagos-envios-impuestos.md` - Configuración general
2. `docs/06.1-implementacion-checkout.md` - Implementación técnica

## Testing

Ejecutar checklist completo de testing E2E:
- Ver `docs/06.2-testing-checklist.md`

## Convención de seguimiento (Opción 3)
GitHub Project = hub de producto/roadmap técnico.
Planner = ejecución operativa diaria.
