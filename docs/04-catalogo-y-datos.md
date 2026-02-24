# Catálogo y datos

## Plantilla maestra de productos

La plantilla maestra define la estructura de datos para todos los productos del catálogo.

### Campos requeridos

| Campo | Tipo | Descripción | Validación |
|-------|------|-------------|------------|
| `sku` | String | Código único del producto | Alfanumérico, guiones y guiones bajos permitidos |
| `name` | String | Nombre del producto | Máximo 200 caracteres |
| `category` | String | Categoría principal | Requerido |
| `subcategory` | String | Subcategoría | Opcional |
| `brand` | String | Marca del producto | Opcional |
| `price` | Numeric | Precio en COP | Mayor o igual a 0 |
| `stock` | Integer | Cantidad disponible | Mayor o igual a 0 |
| `unit` | String | Unidad de medida | Ej: unidad, galón, metro |
| `short_description` | String | Descripción breve | Para listados |
| `long_description` | Text | Descripción detallada | Para página de producto |
| `image_url` | String | URL de imagen principal | Formato URL válido |
| `status` | String | Estado del producto | active, inactive, discontinued |

### Normas de calidad de datos

1. **SKU único**: Cada producto debe tener un SKU único sin duplicados
2. **Formato consistente**: Los SKU deben seguir el formato `[A-Z0-9_-]+`
3. **Precios válidos**: Todos los precios deben ser numéricos y no negativos
4. **Stock controlado**: El stock debe ser un valor entero
5. **Imágenes**: Todos los productos activos deben tener al menos una imagen

### Control de duplicados

El sistema de importación incluye detección automática de duplicados por SKU:
- Detecta SKUs repetidos antes de la importación
- Reporta las líneas donde se encuentran los duplicados
- Bloquea la importación hasta que se resuelvan los duplicados

### Proceso de importación

1. **Preparar datos**: Usar la plantilla CSV en `data/product_template.csv`
2. **Validar**: Ejecutar `python3 scripts/import_products.py <archivo.csv> --validate-only`
3. **Importar**: Ejecutar `python3 scripts/import_products.py <archivo.csv> -o <salida.json>`
4. **Verificar**: Revisar el reporte de importación y archivo de salida

### Estructura de archivos

```
data/
├── product_template.csv          # Plantilla con productos de ejemplo
└── products_normalized.json      # Productos normalizados listos para Odoo

scripts/
└── import_products.py            # Script de importación y validación
```
