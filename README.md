# Página Web Odoo Ferretería

Proyecto para construir y operar una web de ferretería en Odoo.

## Objetivo
Implementar un sitio transaccional y escalable en Odoo, con catálogo, checkout, SEO base, integraciones y operación post-lanzamiento.

## Enlaces
- Repositorio: https://github.com/ConceptualDynamic/pagina-web-odoo-ferreteria
- Planner (Plan): Software Development

## Estructura del Proyecto

### Documentación
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
- `docs/PLANTILLA-PRODUCTO.md` - Guía completa de la plantilla maestra de productos

### Esquemas y Plantillas
- `schemas/product-template.json` - JSON Schema del modelo de datos de producto
- `schemas/product-example.json` - Ejemplo completo de producto
- `schemas/product-template.csv` - Plantilla CSV para carga masiva
- `schemas/README.md` - Documentación de esquemas

## Plantilla Maestra de Producto

La plantilla maestra define la estructura estándar para todos los productos del catálogo de ferretería.

**Inicio rápido**:
- 📖 Leer [`docs/PLANTILLA-PRODUCTO.md`](docs/PLANTILLA-PRODUCTO.md)
- 🔍 Ver ejemplo en [`schemas/product-example.json`](schemas/product-example.json)
- 📊 Usar plantilla CSV en [`schemas/product-template.csv`](schemas/product-template.csv)

**Componentes principales**:
- SKU único (formato: `XXX-####-YYY`)
- Categorización (10 categorías principales)
- Precios (base + IVA + ofertas)
- Stock e inventario
- Imágenes (principal + galería)
- Descripciones (corta + larga + técnica)
- Atributos y especificaciones
- SEO y metadatos

## Convención de seguimiento (Opción 3)
GitHub Project = hub de producto/roadmap técnico.
Planner = ejecución operativa diaria.
