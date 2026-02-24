# Diseño PDP (Product Detail Page) - Ficha de Producto

## Objetivo
Proporcionar información completa del producto con diseño orientado a conversión, destacando CTAs claros y contenido que facilite la decisión de compra.

## Layout Principal

### Estructura de la Página
```
+----------------------------------------------------------+
|                    HEADER/NAVIGATION                      |
+----------------------------------------------------------+
|                                                           |
|  BREADCRUMB: Inicio > Categoría > Producto               |
|                                                           |
+----------------------------------------------------------+
|                                                           |
|  +-------------------+  +-----------------------------+  |
|  |                   |  | INFORMACIÓN PRINCIPAL       |  |
|  |   GALERÍA DE      |  | - Marca y Nombre            |  |
|  |   IMÁGENES        |  | - SKU y Rating              |  |
|  |                   |  | - Precio y Disponibilidad   |  |
|  |                   |  | - Cantidad                  |  |
|  |                   |  | - CTAs (Comprar/Carrito)    |  |
|  |                   |  | - Compartir/Favoritos       |  |
|  +-------------------+  +-----------------------------+  |
|                                                           |
+----------------------------------------------------------+
|                                                           |
|  TABS: [Descripción] [Especificaciones] [Reseñas]       |
|                                                           |
+----------------------------------------------------------+
|                                                           |
|  PRODUCTOS RELACIONADOS / COMPRADOS JUNTOS               |
|                                                           |
+----------------------------------------------------------+
|                    FOOTER                                 |
+----------------------------------------------------------+
```

## Componentes Detallados

### 1. Breadcrumb (Migas de Pan)
```
Inicio > Herramientas Eléctricas > Taladros > Taladro Inalámbrico Bosch 18V
```
- Todos los niveles son clickeables
- Última parte (producto actual) no es link
- Formato rich snippet para SEO

### 2. Galería de Imágenes

#### Componente Principal (Izquierda)
```
+--------------------------------+
|  [< >]                         |
|                                |
|                                |
|        IMAGEN PRINCIPAL        |
|           600x600              |
|                                |
|                                |
|  [🔍 Zoom]                     |
+--------------------------------+
|  [▪️] [▪️] [▪️] [▪️] [▪️]       |
|  Thumbnails (5-10 imágenes)   |
+--------------------------------+
```

**Funcionalidades**:
- **Imagen principal**: 600x600px (desktop)
- **Navegación**: Flechas prev/next
- **Thumbnails**: Scroll horizontal si hay más de 5
- **Zoom**: 
  - Click para modal con imagen grande (1200x1200)
  - Hover para zoom in-place (opcional)
- **Video**: Si disponible, mostrar como thumbnail
- **Badge**: "OFERTA", "NUEVO", "AGOTADO"

**Lightbox Modal** (al hacer zoom):
```
+--------------------------------------------------+
|                                              [X] |
|                                                  |
|                                                  |
|              IMAGEN AMPLIADA                     |
|                1200x1200                         |
|                                                  |
|                                                  |
|              [< imagen X de N >]                 |
|                                                  |
+--------------------------------------------------+
```

### 3. Información Principal del Producto (Derecha)

#### 3.1 Header del Producto
```
MARCA BOSCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Taladro Inalámbrico Bosch GSR 18V-55
Professional, Batería Li-ion, 55Nm de Torque

SKU: BSH-GSR-18V-55         [♡ Favoritos]
[★★★★☆] 4.5 (127 reseñas)   [↗️ Compartir]
```

**Elementos**:
- **Marca**: Destacada, link a productos de la marca
- **Nombre del producto**: H1, SEO-friendly
- **Descripción corta**: Características clave
- **SKU**: Código único del producto
- **Rating**: Estrellas visuales + promedio + número de reseñas (link a sección)
- **Iconos de acción**: Favoritos (corazón) y Compartir

#### 3.2 Precio y Disponibilidad
```
+------------------------------------------+
| $3,499.00                                |
| Precio anterior: $4,200.00 (-17%)       |
|                                          |
| ✓ En stock - Envío gratis              |
| 📦 Llega mañana si compras en 2h 15m   |
|                                          |
| 💳 6 cuotas sin interés de $583.17      |
| [Ver opciones de pago]                  |
+------------------------------------------+
```

**Elementos**:
- **Precio actual**: Grande, destacado
- **Precio anterior**: Si hay descuento, mostrar tachado con % ahorro
- **Stock**: 
  - ✓ En stock (verde)
  - ⚠️ Últimas unidades (naranja)
  - ✗ Agotado (rojo) → mostrar "Avísame cuando esté disponible"
- **Envío**: Información de envío gratis o costo
- **Tiempo de entrega**: Estimación basada en ubicación
- **Financiamiento**: Cuotas disponibles (si aplica)

#### 3.3 Variantes y Atributos (si aplica)
```
Voltaje: ○ 12V  ● 18V  ○ 20V

Incluye batería: ● Sí  ○ Solo herramienta

Color: 🔵 Azul  ⚫ Negro
```

**Funcionalidad**:
- Radio buttons para opciones únicas
- Checkboxes para múltiples selecciones
- Actualización dinámica de precio/disponibilidad

#### 3.4 Selector de Cantidad
```
Cantidad:  [-]  [  2  ]  [+]

(Máximo 10 unidades por cliente)
```

**Validaciones**:
- Mínimo: 1
- Máximo: Stock disponible o límite por cliente
- Increment/decrement buttons
- Input numérico editable

#### 3.5 Botones CTA (Call to Action)

**Layout**:
```
+------------------------------------------+
| [    🛒 AGREGAR AL CARRITO    ]         |
| [    💳 COMPRAR AHORA         ]         |
+------------------------------------------+
|                                          |
| [+ Agregar a lista de deseos]           |
| [⚖️ Comparar con otros productos]        |
+------------------------------------------+
```

**Botones Principales**:

1. **Agregar al Carrito**
   - Color: Primario (azul/verde según branding)
   - Acción: Agrega producto y muestra confirmación
   - Estado disabled si no hay stock

2. **Comprar Ahora**
   - Color: Secundario (naranja/rojo)
   - Acción: Agrega producto y redirige a checkout
   - Atajo para compra rápida

**Botones Secundarios**:
- Lista de deseos
- Comparar productos (si hay módulo)
- Consultar con un asesor

#### 3.6 Información Adicional (Trust Badges)
```
+------------------------------------------+
| ✓ Garantía oficial de 2 años           |
| ✓ Devolución gratis en 30 días         |
| ✓ Envío gratis en compras +$1,000      |
| ✓ Atención al cliente 24/7              |
+------------------------------------------+
```

#### 3.7 Compartir y Social
```
Compartir: [f] [t] [📧] [📋 Copiar link]
```

### 4. Tabs de Contenido

#### Tab 1: Descripción
```
+----------------------------------------------------------+
| DESCRIPCIÓN                                               |
+----------------------------------------------------------+
|                                                           |
| El Taladro Inalámbrico Bosch GSR 18V-55 Professional    |
| es ideal para trabajos de perforación y atornillado      |
| intensivos. Su potente motor sin escobillas ofrece...    |
|                                                           |
| Características destacadas:                              |
| • Motor sin escobillas de alta eficiencia                |
| • Sistema de control electrónico de velocidad            |
| • Luz LED integrada para áreas oscuras                   |
| • Diseño ergonómico con empuñadura Softgrip              |
|                                                           |
| [Ver descripción completa ▼]                             |
+----------------------------------------------------------+
```

**Contenido**:
- Descripción detallada del producto
- Beneficios principales
- Casos de uso
- Contenido del paquete
- Formato: HTML enriquecido (negritas, listas, imágenes)

#### Tab 2: Especificaciones Técnicas
```
+----------------------------------------------------------+
| ESPECIFICACIONES TÉCNICAS                                 |
+----------------------------------------------------------+
|                                                           |
| Generales                                                |
| ├─ Marca:              Bosch                             |
| ├─ Modelo:             GSR 18V-55                        |
| ├─ SKU:                BSH-GSR-18V-55                    |
| └─ Garantía:           2 años                            |
|                                                           |
| Motor y Potencia                                         |
| ├─ Voltaje:            18V                               |
| ├─ Velocidad:          0-550 / 0-1,750 rpm              |
| ├─ Torque máximo:      55 Nm                             |
| └─ Tipo de motor:      Sin escobillas                    |
|                                                           |
| Batería                                                  |
| ├─ Tipo:               Li-ion                            |
| ├─ Capacidad:          2.0 Ah                            |
| └─ Tiempo de carga:    30 minutos                        |
|                                                           |
| Dimensiones y Peso                                       |
| ├─ Peso:               1.4 kg                            |
| ├─ Largo:              195 mm                            |
| └─ Ancho:              75 mm                             |
|                                                           |
| [📥 Descargar ficha técnica PDF]                         |
+----------------------------------------------------------+
```

**Formato**:
- Tabla estructurada por categorías
- Expandible/colapsable por sección
- Opción de descargar PDF
- Schema markup para SEO

#### Tab 3: Reseñas y Valoraciones
```
+----------------------------------------------------------+
| RESEÑAS Y VALORACIONES                                    |
+----------------------------------------------------------+
|                                                           |
| Calificación promedio                                    |
|                                                           |
|     4.5 ★                                                |
|     Basado en 127 reseñas                                |
|                                                           |
| Distribución:                                            |
| 5★ ████████████████████████░░░░░░ 85 reseñas (67%)      |
| 4★ ████████░░░░░░░░░░░░░░░░░░░░░░ 28 reseñas (22%)      |
| 3★ ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░  8 reseñas (6%)       |
| 2★ █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  4 reseñas (3%)       |
| 1★ █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  2 reseñas (2%)       |
|                                                           |
| [✍️ Escribir reseña]                                     |
|                                                           |
+----------------------------------------------------------+
| Filtrar: [Todas] [5★] [4★] [3★] [2★] [1★]               |
| Ordenar: [Más recientes ▼]                               |
+----------------------------------------------------------+
|                                                           |
| ★★★★★ Excelente herramienta                             |
| Por: Carlos M. | 15 de enero 2026 | ✓ Compra verificada  |
|                                                           |
| El taladro es muy potente y la batería dura bastante.   |
| Lo uso para trabajos profesionales y no me ha           |
| decepcionado. Muy recomendable.                          |
|                                                           |
| [👍 Útil (23)] [Reportar]                                |
|                                                           |
+----------------------------------------------------------+
```

**Elementos**:
- Resumen de calificación con gráfico
- Distribución de estrellas
- Botón para escribir reseña
- Filtros por calificación
- Ordenamiento (recientes, útiles, etc.)
- Reseñas individuales con:
  - Estrellas, título, autor, fecha
  - Badge "Compra verificada"
  - Texto de la reseña
  - Imágenes del usuario (si aplica)
  - Botones útil/no útil
  - Respuesta del vendedor (si aplica)

### 5. Sección: Productos Relacionados

```
+----------------------------------------------------------+
| PRODUCTOS RELACIONADOS                                    |
+----------------------------------------------------------+
|                                                           |
| [←] [Producto 1] [Producto 2] [Producto 3] [Producto 4] [→] |
|                                                           |
+----------------------------------------------------------+
```

**Lógica**:
- Misma categoría
- Misma marca
- Precio similar
- Carrusel horizontal (4-6 productos visibles)
- Cards simplificadas (imagen, nombre, precio, rating)

### 6. Sección: Frecuentemente Comprados Juntos

```
+----------------------------------------------------------+
| FRECUENTEMENTE COMPRADOS JUNTOS                           |
+----------------------------------------------------------+
|                                                           |
| [Img Producto]  +  [Img Accesorio 1]  +  [Img Accesorio 2] |
| Este producto      Baterías 18V         Estuche          |
| $3,499.00          $899.00              $399.00          |
|                                                           |
| Precio total: $4,797.00                                  |
| Ahorras: $500.00 (10%)                                   |
|                                                           |
| ☑ Taladro Bosch (Este producto)                          |
| ☑ Baterías adicionales 18V                               |
| ☑ Estuche de transporte                                  |
|                                                           |
| [Agregar los 3 al carrito]                               |
+----------------------------------------------------------+
```

### 7. Sección: Preguntas y Respuestas (Opcional)

```
+----------------------------------------------------------+
| PREGUNTAS Y RESPUESTAS                                    |
+----------------------------------------------------------+
|                                                           |
| [❓ Hacer una pregunta]                                   |
|                                                           |
| P: ¿Incluye el maletín de transporte?                   |
| R: No, el maletín se vende por separado (SKU: BSH-MAL-01) |
|    Por: Vendedor | 10 de enero 2026                      |
|    [👍 Útil (15)]                                         |
|                                                           |
| [Ver todas las preguntas (23)]                           |
+----------------------------------------------------------+
```

## Responsive Design

### Desktop (>1024px)
- Layout de 2 columnas (galería 50% + info 50%)
- Todos los elementos visibles
- Galería con zoom avanzado

### Tablet (768px - 1024px)
- Layout de 2 columnas ajustado
- Galería más pequeña
- CTAs más compactos

### Mobile (<768px)
- Layout de 1 columna
- Galería primero (fullwidth)
- Info sticky en bottom (precio + CTA)
- Tabs colapsables
```
+--------------------------------+
|                                |
|   GALERÍA                      |
|   (swipeable)                  |
|                                |
+--------------------------------+
| Nombre                         |
| ★★★★☆ (127)                    |
| $3,499.00                      |
| [Agregar] [Comprar]            |
+--------------------------------+
```

**Sticky Bottom Bar** (al hacer scroll):
```
+--------------------------------+
| $3,499.00  [Agregar] [Comprar] |
+--------------------------------+
```

## Estados y Feedback

### Producto Agregado al Carrito
```
+------------------------------------------+
| ✓ Producto agregado al carrito          |
|                                          |
| Taladro Bosch GSR 18V-55                |
| Cantidad: 2                              |
|                                          |
| [Ir al carrito]  [Seguir comprando]     |
+------------------------------------------+
```

### Producto Agotado
```
+------------------------------------------+
| ✗ Producto temporalmente agotado        |
|                                          |
| [✉️ Avísame cuando esté disponible]     |
|                                          |
| Ver productos similares:                |
| [Producto A] [Producto B] [Producto C]  |
+------------------------------------------+
```

### Error de Carga
```
+------------------------------------------+
| ⚠️ No pudimos cargar el producto        |
|                                          |
| [Reintentar]                            |
+------------------------------------------+
```

## Integración con Odoo

### Endpoints Necesarios

```python
# Obtener producto individual
GET /shop/product/<id>
Response:
{
  "id": 123,
  "name": "Taladro Bosch GSR 18V-55",
  "sku": "BSH-GSR-18V-55",
  "brand": "Bosch",
  "price": 3499.00,
  "list_price": 4200.00,
  "description": "...",
  "description_sale": "...",
  "images": [...],
  "variants": [...],
  "attributes": {...},
  "stock_qty": 15,
  "rating": 4.5,
  "reviews_count": 127,
  "shipping_info": {...}
}

# Agregar al carrito
POST /shop/cart/add
Body: {
  "product_id": 123,
  "qty": 2,
  "variant_id": null
}

# Productos relacionados
GET /shop/product/<id>/related

# Reseñas
GET /shop/product/<id>/reviews?page=1&limit=10
POST /shop/product/<id>/reviews
```

### Módulos Odoo Requeridos

- `website_sale`: E-commerce base
- `product`: Gestión de productos
- `stock`: Inventario y disponibilidad
- `website_sale_wishlist`: Lista de deseos
- `website_sale_comparison`: Comparación de productos
- `portal_rating`: Sistema de reseñas
- `delivery`: Información de envíos

## Accesibilidad (A11Y)

- **Navegación por teclado**: Completa
- **Focus visible**: Orden lógico de tabulación
- **Alt text**: Todas las imágenes descriptivas
- **ARIA labels**: Botones de acción, ratings
- **Screen readers**: Anuncios de cambios (stock, precio)
- **Contraste**: WCAG AA compliance
- **Zoom text**: Responsive hasta 200%

## SEO Optimizations

### Meta Tags
```html
<title>Taladro Inalámbrico Bosch GSR 18V-55 | Ferretería XYZ</title>
<meta name="description" content="Compra el Taladro Bosch GSR 18V-55 con batería Li-ion, 55Nm torque. Envío gratis. Garantía 2 años.">
<link rel="canonical" href="https://example.com/producto/taladro-bosch-gsr-18v-55">
```

### Schema Markup (JSON-LD)
```json
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "Taladro Inalámbrico Bosch GSR 18V-55",
  "image": [...],
  "description": "...",
  "sku": "BSH-GSR-18V-55",
  "brand": {
    "@type": "Brand",
    "name": "Bosch"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/producto/...",
    "priceCurrency": "USD",
    "price": "3499.00",
    "priceValidUntil": "2026-12-31",
    "availability": "https://schema.org/InStock",
    "seller": {
      "@type": "Organization",
      "name": "Ferretería XYZ"
    }
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "127"
  },
  "review": [...]
}
```

### OpenGraph Tags (Social Sharing)
```html
<meta property="og:title" content="Taladro Inalámbrico Bosch GSR 18V-55">
<meta property="og:description" content="Potente taladro profesional con batería 18V">
<meta property="og:image" content="https://example.com/images/product-social.jpg">
<meta property="og:url" content="https://example.com/producto/taladro-bosch-gsr-18v-55">
<meta property="og:type" content="product">
<meta property="product:price:amount" content="3499.00">
<meta property="product:price:currency" content="USD">
```

## Métricas de Éxito (KPIs)

1. **Conversión**:
   - Add-to-cart rate (objetivo: >5%)
   - Purchase conversion rate (objetivo: >2%)

2. **Engagement**:
   - Tiempo promedio en página (objetivo: >2 min)
   - Scroll depth (objetivo: >75% ven specs)
   - Click en galería/zoom (objetivo: >40%)

3. **Social Proof**:
   - Tasa de lectura de reseñas
   - Tasa de envío de reseñas

4. **Technical**:
   - Tiempo de carga (objetivo: <2s)
   - Bounce rate (objetivo: <40%)
   - Error rate en agregar al carrito (objetivo: <1%)

## Notas de Implementación

### Prioridad 1 (MVP):
- Galería de imágenes con zoom
- Información básica (nombre, precio, SKU)
- Stock y disponibilidad
- CTA "Agregar al carrito"
- Descripción y especificaciones
- Breadcrumb

### Prioridad 2:
- Sistema de reseñas
- Productos relacionados
- Lista de deseos
- Compartir en redes
- Variantes del producto

### Prioridad 3:
- Comprar ahora (fast checkout)
- Frecuentemente comprados juntos
- Preguntas y respuestas
- Comparar productos
- Notificaciones de stock
