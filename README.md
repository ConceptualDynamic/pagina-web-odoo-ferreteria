# Página Web Odoo Ferretería

Proyecto para construir y operar una web de ferretería en Odoo.

## Objetivo
Implementar un sitio transaccional y escalable en Odoo, con catálogo, checkout, SEO base, integraciones y operación post-lanzamiento.

## Funcionalidades implementadas

### Fase 3: Catálogo y carga inicial de productos

#### Importación de productos
Sistema de importación y normalización de catálogo con control de duplicados y validación de calidad.

**Uso:**
```bash
# Validar datos sin importar
python3 scripts/import_products.py data/product_template.csv --validate-only

# Importar y normalizar productos
python3 scripts/import_products.py data/product_template.csv -o data/products_normalized.json
```

**Características:**
- ✅ Validación de campos requeridos (SKU, nombre, categoría, precio, stock, estado)
- ✅ Detección automática de SKUs duplicados
- ✅ Normalización de datos (formato, mayúsculas/minúsculas, espacios)
- ✅ Validación de tipos de datos (precios numéricos, stock entero)
- ✅ Validación de formato de SKU (alfanumérico con guiones)
- ✅ Reportes de validación detallados con errores y advertencias
- ✅ Exportación a JSON para integración con Odoo

Ver documentación completa en [`docs/04-catalogo-y-datos.md`](docs/04-catalogo-y-datos.md)

## Enlaces
- Repositorio: https://github.com/ConceptualDynamic/pagina-web-odoo-ferreteria
- Planner (Plan): Software Development

## Estructura documental
- `docs/01-alcance-kpis.md`
- `docs/02-roadmap-fases.md`
- `docs/03-arquitectura-informacion.md`
- `docs/04-catalogo-y-datos.md`
- `docs/05-diseno-ux-ui.md`
- `docs/06-pagos-envios-impuestos.md`
- `docs/07-seo-y-contenido.md`
- `docs/08-integraciones.md`
- `docs/09-qa.md`
- `docs/10-go-live-y-monitoreo.md`
- `docs/11-matriz-github-planner.md`

## Convención de seguimiento (Opción 3)
GitHub Project = hub de producto/roadmap técnico.
Planner = ejecución operativa diaria.
