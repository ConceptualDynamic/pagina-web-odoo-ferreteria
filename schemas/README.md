# Esquemas y Plantillas de Producto

Este directorio contiene las plantillas maestras y ejemplos para la definición de productos del catálogo de ferretería.

## Archivos

### `product-template.json`
Esquema JSON Schema (draft-07) que define la estructura completa de un producto.

**Uso**:
- Validación automática de datos de productos
- Integración con sistemas externos
- Documentación de estructura de datos
- Generación de formularios

**Validación**:
```bash
# Validar un producto contra el schema
ajv validate -s product-template.json -d product-example.json
```

### `product-example.json`
Ejemplo completo de un producto (Martillo Stanley 16oz) con todos los campos poblados.

**Uso**:
- Referencia para crear nuevos productos
- Testing de integraciones
- Ejemplo para capacitación del equipo

### `product-template.csv`
Plantilla CSV para carga masiva de productos con los campos más comunes.

**Uso**:
- Importación en Excel/Google Sheets
- Carga masiva a Odoo
- Intercambio con proveedores

**Campos incluidos**:
- Identificación: SKU, nombre, marca, modelo
- Categorización: categoría principal y subcategoría
- Precios: precio base, moneda, IVA
- Stock: cantidad, unidad, bodega
- Imágenes: URL principal y texto alternativo
- Descripciones: corta y larga
- Atributos: material, color, garantía
- Estado: status, is_featured

**Nota**: El CSV contiene un subconjunto de campos. Para estructura completa, usar JSON.

## Documentación

Para documentación detallada sobre cómo usar las plantillas, ver:
- [`../docs/PLANTILLA-PRODUCTO.md`](../docs/PLANTILLA-PRODUCTO.md) - Guía completa
- [`../docs/04-catalogo-y-datos.md`](../docs/04-catalogo-y-datos.md) - Contexto general

## Validación de Datos

### Requisitos Mínimos
Un producto válido debe tener:
1. SKU único (formato: `XXX-####-YYY`)
2. Nombre (3-200 caracteres)
3. Categoría principal y subcategoría
4. Precio base > 0
5. Stock >= 0
6. Imagen principal
7. Descripción corta
8. Estado válido

### Herramientas de Validación

**Validar formato JSON**:
```bash
python3 -m json.tool product-example.json
```

**Validar contra schema**:
```bash
npm install -g ajv-cli
ajv validate -s product-template.json -d product-example.json
```

**Validar CSV**:
```bash
# Verificar estructura
csvlint product-template.csv
```

## Uso en Código

### Python
```python
import json

# Cargar schema
with open('schemas/product-template.json') as f:
    schema = json.load(f)

# Validar producto
from jsonschema import validate
validate(instance=product_data, schema=schema)
```

### JavaScript/Node.js
```javascript
const Ajv = require('ajv');
const schema = require('./schemas/product-template.json');

const ajv = new Ajv();
const validate = ajv.compile(schema);

const valid = validate(productData);
if (!valid) console.log(validate.errors);
```

### Odoo (Python)
```python
import json

def validate_product_data(product_dict):
    """Valida datos de producto contra el schema"""
    schema_path = '/path/to/schemas/product-template.json'
    with open(schema_path) as f:
        schema = json.load(f)
    
    from jsonschema import validate, ValidationError
    try:
        validate(instance=product_dict, schema=schema)
        return True
    except ValidationError as e:
        _logger.error(f"Validation error: {e.message}")
        return False
```

## Creación de Productos

### Desde JSON
1. Copiar `product-example.json`
2. Modificar con datos del nuevo producto
3. Validar contra `product-template.json`
4. Importar a Odoo

### Desde CSV
1. Abrir `product-template.csv` en Excel/Sheets
2. Agregar filas con nuevos productos
3. Validar datos (formatos, rangos)
4. Importar a Odoo vía módulo de importación

### Desde API
```bash
curl -X POST https://ferreteria.example.com/api/products \
  -H "Content-Type: application/json" \
  -d @product-example.json
```

## Buenas Prácticas

1. **Siempre validar** antes de importar a producción
2. **Usar ejemplos** como punto de partida
3. **Documentar atributos custom** en la categoría correspondiente
4. **Mantener consistencia** en nomenclatura
5. **Revisar duplicados** antes de crear SKUs nuevos

## Soporte

Para preguntas sobre las plantillas:
1. Revisar la documentación completa en `docs/PLANTILLA-PRODUCTO.md`
2. Consultar los ejemplos en este directorio
3. Contactar al equipo de producto

## Versionamiento

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 1.0 | 2026-02-24 | Versión inicial - Schema JSON, ejemplo y CSV |
