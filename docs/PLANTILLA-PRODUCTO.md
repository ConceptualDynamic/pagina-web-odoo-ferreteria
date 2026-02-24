# Plantilla Maestra de Producto - Catálogo Ferretería

## Introducción

Este documento define la plantilla maestra (master template) para los datos de productos del catálogo de la ferretería en Odoo. La plantilla está diseñada para garantizar consistencia, calidad de datos y facilitar la integración con sistemas externos.

## Ubicación de Archivos

- **Esquema JSON**: `schemas/product-template.json`
- **Ejemplo de producto**: `schemas/product-example.json`
- **Documentación**: Este archivo

## Estructura de Datos

### 1. Identificación del Producto

#### SKU (Stock Keeping Unit)
- **Formato**: `XXX-####-YYY`
  - XXX: Código de categoría (3 letras mayúsculas)
  - ####: Número secuencial (4 dígitos)
  - YYY: Código identificador (3 caracteres alfanuméricos)
- **Ejemplo**: `FER-0001-MRT`
- **Reglas**:
  - Único por producto
  - Inmutable una vez asignado
  - No reutilizable para productos descontinuados

#### Códigos de Categoría Recomendados
- `HMA` - Herramientas Manuales
- `HEL` - Herramientas Eléctricas
- `MTC` - Materiales de Construcción
- `PLO` - Plomería
- `ELE` - Electricidad
- `PIN` - Pintura
- `FGE` - Ferretería General
- `SEG` - Seguridad Industrial
- `JAR` - Jardinería
- `ADH` - Adhesivos y Químicos

### 2. Información Básica

- **name**: Nombre descriptivo del producto (3-200 caracteres)
- **slug**: URL amigable generada automáticamente del nombre
- **brand**: Marca del producto
- **model**: Modelo o referencia del fabricante

### 3. Categorización

```json
{
  "category": {
    "main": "Categoría principal",
    "subcategory": "Subcategoría específica",
    "tags": ["etiqueta1", "etiqueta2"]
  }
}
```

**Categorías Principales Disponibles**:
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

### 4. Precios

```json
{
  "price": {
    "base": 25000,           // Precio base sin impuestos
    "currency": "COP",       // Moneda (COP o USD)
    "tax_rate": 19,          // IVA en porcentaje
    "sale_price": 22000,     // Precio de oferta (opcional)
    "discount_percentage": 12,
    "valid_from": "2026-01-01T00:00:00Z",
    "valid_until": "2026-03-31T23:59:59Z"
  }
}
```

**Reglas de Precios**:
- El precio base debe ser mayor a 0
- El IVA estándar en Colombia es 19%
- Si hay `sale_price`, debe ser menor que el precio con impuestos
- Las fechas de validez son opcionales pero recomendadas para ofertas

### 5. Stock e Inventario

```json
{
  "stock": {
    "quantity": 150,          // Cantidad total en bodega
    "unit": "unidad",         // Unidad de medida
    "warehouse": "BOG-PRINCIPAL",
    "reserved": 10,           // Reservado en pedidos
    "available": 140,         // Disponible = quantity - reserved
    "min_stock": 20,          // Stock mínimo para reorden
    "max_stock": 500,         // Stock máximo recomendado
    "lead_time_days": 7       // Días de reabastecimiento
  }
}
```

**Unidades de Medida Soportadas**:
- `unidad` - Para items individuales
- `par` - Para productos vendidos en pares
- `kg` - Kilogramos
- `m` - Metros
- `m2` - Metros cuadrados
- `m3` - Metros cúbicos
- `litro` - Litros
- `galón` - Galones
- `caja` - Cajas
- `paquete` - Paquetes

### 6. Imágenes

```json
{
  "images": {
    "main": "URL de imagen principal",
    "gallery": ["URL1", "URL2", "URL3"],
    "thumbnail": "URL de miniatura",
    "alt_text": "Texto alternativo para SEO y accesibilidad"
  }
}
```

**Especificaciones de Imágenes**:
- **Imagen Principal**: 1200x1200px, formato JPG/PNG, max 500KB
- **Galería**: Hasta 10 imágenes adicionales, mismas especificaciones
- **Thumbnail**: 300x300px, formato JPG/PNG, max 100KB
- **Alt Text**: Descripción clara para SEO y accesibilidad (requerido)

**Mejores Prácticas**:
- Fondo blanco o transparente para consistencia
- Mostrar el producto desde múltiples ángulos
- Incluir imágenes de uso/aplicación cuando sea relevante
- Nombres de archivo descriptivos: `producto-marca-modelo-vista.jpg`

### 7. Descripciones

```json
{
  "description": {
    "short": "Descripción corta (max 250 caracteres)",
    "long": "Descripción detallada (max 5000 caracteres)",
    "technical": "Especificaciones técnicas"
  }
}
```

**Guías de Contenido**:
- **Short**: Para listados y vista previa (1-2 frases)
- **Long**: Descripción completa con beneficios y características
- **Technical**: Especificaciones técnicas en formato estructurado

### 8. Atributos y Especificaciones

```json
{
  "attributes": {
    "dimensions": {
      "length": 33,    // cm
      "width": 12,     // cm
      "height": 3,     // cm
      "weight": 0.6    // kg
    },
    "material": "Acero forjado",
    "color": "Negro/Amarillo",
    "warranty_months": 12,
    "country_of_origin": "USA",
    "certifications": ["ANSI", "ISO 9001"],
    "custom": {
      // Atributos específicos de categoría
    }
  }
}
```

### 9. SEO y Metadatos

```json
{
  "seo": {
    "meta_title": "Título SEO (max 60 caracteres)",
    "meta_description": "Descripción SEO (max 160 caracteres)",
    "keywords": ["palabra1", "palabra2", "palabra3"]
  }
}
```

**Mejores Prácticas SEO**:
- Incluir marca y modelo en el título
- Meta description debe ser persuasiva y clara
- Keywords relevantes sin keyword stuffing
- URL slug amigable y descriptivo

### 10. Estado y Clasificación

```json
{
  "status": "active",           // active, inactive, discontinued, coming_soon, out_of_stock
  "is_featured": true,          // Producto destacado
  "is_new": false,              // Producto nuevo
  "is_bestseller": true,        // Más vendido
  "requires_assembly": false,   // Requiere ensamblaje
  "requires_installation": false, // Requiere instalación
  "hazardous_material": false   // Material peligroso
}
```

## Normas de Calidad de Datos

### Campos Obligatorios Mínimos
Para que un producto sea válido y publicable, debe tener:
1. ✓ SKU único y válido
2. ✓ Nombre descriptivo
3. ✓ Categoría principal y subcategoría
4. ✓ Precio base y moneda
5. ✓ Cantidad de stock y unidad
6. ✓ Al menos una imagen principal
7. ✓ Descripción corta
8. ✓ Estado del producto

### Control de Duplicados

**Reglas de Duplicación**:
1. Un SKU solo puede existir una vez en el sistema
2. Combinación de (brand + model) debe ser única
3. Si el nombre es idéntico, verificar que sean productos diferentes

**Proceso de Validación**:
1. Verificar SKU único antes de crear
2. Buscar productos similares por nombre y marca
3. Validar que las imágenes sean del producto correcto
4. Confirmar precios y especificaciones

### Validación de Datos

**Validaciones Automáticas**:
- SKU formato: `^[A-Z]{3}-[0-9]{4}-[A-Z0-9]{3}$`
- Slug formato: `^[a-z0-9]+(?:-[a-z0-9]+)*$`
- Precio base > 0
- Stock quantity >= 0
- URLs de imágenes válidas (formato URI)
- Longitud de textos dentro de límites

**Validaciones Manuales Recomendadas**:
- Revisar ortografía en descripciones
- Verificar coherencia de especificaciones técnicas
- Confirmar que las imágenes corresponden al producto
- Validar precios contra competencia
- Revisar categorización correcta

## Integración con Odoo

### Mapeo de Campos Odoo
```
product-template.json → Odoo Product Template
├── sku → default_code
├── name → name
├── category.main → categ_id
├── price.base → list_price
├── stock.quantity → qty_available
├── images.main → image_1920
├── description.long → description_sale
└── status → active (boolean)
```

### Campos Calculados
- `available` = `quantity` - `reserved`
- `final_price` = `base` * (1 + `tax_rate`/100)
- `discount_amount` = `base` - `sale_price`

## Proceso de Carga de Productos

### 1. Preparación
- Recopilar información del producto del proveedor
- Validar calidad de imágenes
- Preparar descripciones según guías

### 2. Creación
- Generar SKU único según formato
- Completar todos los campos obligatorios
- Agregar atributos específicos de categoría
- Cargar imágenes al CDN

### 3. Validación
- Ejecutar validación automática contra schema
- Revisar duplicados
- Verificar calidad de contenido
- Confirmar precios y stock

### 4. Publicación
- Marcar status como "active"
- Asignar a categorías apropiadas
- Configurar productos relacionados
- Activar en Odoo

## Ejemplos de Uso

### Producto Simple (Herramienta)
Ver: `schemas/product-example.json`

### Producto con Variantes (Tornillos)
```json
{
  "sku": "FER-0050-TOR",
  "name": "Tornillos Autoperforantes 8x1",
  "attributes": {
    "custom": {
      "head_type": "Phillips",
      "thread_type": "Coarse",
      "material": "Zinc Plated Steel",
      "package_quantity": 100
    }
  }
}
```

### Producto a Granel (Pintura)
```json
{
  "sku": "PIN-0100-LAT",
  "name": "Pintura Látex Blanca Premium",
  "stock": {
    "quantity": 500,
    "unit": "galón"
  },
  "attributes": {
    "custom": {
      "coverage_sqm_per_liter": 12,
      "dry_time_hours": 2,
      "coats_recommended": 2,
      "finish": "Mate"
    }
  }
}
```

## Mantenimiento de Datos

### Actualizaciones Periódicas
- **Precios**: Revisar mensualmente o según inflación
- **Stock**: Actualizar diariamente desde sistema de inventario
- **Imágenes**: Actualizar si el producto cambia empaque/diseño
- **Descripciones**: Revisar trimestralmente para SEO

### Auditoría de Calidad
- Ejecutar validaciones semanalmente
- Identificar productos con datos incompletos
- Revisar productos sin ventas en 3 meses
- Actualizar productos descontinuados

## Soporte y Contacto

Para dudas sobre la plantilla de productos:
- Revisar este documento
- Consultar ejemplos en `schemas/product-example.json`
- Contactar al equipo de producto

## Historial de Cambios

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 1.0 | 2026-02-24 | Versión inicial de plantilla maestra |

---

**Nota**: Esta plantilla es parte de la Fase 3 del proyecto y debe mantenerse actualizada según las necesidades del negocio y feedback del equipo.
