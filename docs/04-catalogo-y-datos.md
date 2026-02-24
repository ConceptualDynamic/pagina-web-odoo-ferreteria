# Catálogo y datos

## Plantilla Maestra de Producto

La plantilla maestra define la estructura estándar para todos los productos del catálogo.

**Documentación completa**: Ver [`PLANTILLA-PRODUCTO.md`](./PLANTILLA-PRODUCTO.md)

### Componentes Principales

1. **Identificación**
   - SKU único (formato: `XXX-####-YYY`)
   - Nombre y slug
   - Marca y modelo

2. **Categorización**
   - Categoría principal
   - Subcategoría
   - Tags para búsqueda

3. **Precios**
   - Precio base sin impuestos
   - IVA (19% estándar)
   - Precios de oferta (opcional)

4. **Stock e Inventario**
   - Cantidad disponible
   - Unidad de medida
   - Stock mínimo/máximo
   - Tiempo de reabastecimiento

5. **Imágenes**
   - Imagen principal (1200x1200px)
   - Galería (hasta 10 imágenes)
   - Thumbnail (300x300px)
   - Texto alternativo

6. **Descripciones**
   - Corta (max 250 caracteres)
   - Larga (max 5000 caracteres)
   - Especificaciones técnicas

7. **Atributos**
   - Dimensiones y peso
   - Material y color
   - Garantía
   - Certificaciones

8. **SEO**
   - Meta título (max 60 caracteres)
   - Meta descripción (max 160 caracteres)
   - Keywords

## Archivos de Referencia

- **Esquema JSON**: `schemas/product-template.json` - Definición completa del esquema
- **Ejemplo**: `schemas/product-example.json` - Producto de ejemplo completo
- **Documentación**: `docs/PLANTILLA-PRODUCTO.md` - Guía detallada de uso

## Normas de Calidad de Datos

### Campos Obligatorios Mínimos
1. SKU único
2. Nombre descriptivo
3. Categoría y subcategoría
4. Precio base
5. Stock
6. Imagen principal
7. Descripción corta
8. Estado

### Control de Duplicados

**Reglas**:
- SKU único por producto
- Combinación marca+modelo única
- Verificación por nombre similar

**Proceso**:
1. Validar SKU antes de crear
2. Buscar productos similares
3. Confirmar especificaciones
4. Validar imágenes

### Validaciones

**Automáticas**:
- Formato de SKU: `^[A-Z]{3}-[0-9]{4}-[A-Z0-9]{3}$`
- Precio > 0
- Stock >= 0
- URLs válidas
- Longitudes de texto

**Manuales**:
- Ortografía
- Coherencia técnica
- Imágenes correctas
- Precios competitivos
- Categorización adecuada

## Integración Odoo

La plantilla está diseñada para mapear directamente a los campos de Odoo Product Template:

| Campo Template | Campo Odoo |
|----------------|------------|
| sku | default_code |
| name | name |
| category.main | categ_id |
| price.base | list_price |
| stock.quantity | qty_available |
| images.main | image_1920 |
| description.long | description_sale |
| status | active |

## Categorías Principales

1. Herramientas Manuales
2. Herramientas Eléctricas
3. Materiales de Construcción
4. Plomería
5. Electricidad
6. Pintura
7. Ferretería General
8. Seguridad Industrial
9. Jardinería
10. Adhesivos y Químicos
