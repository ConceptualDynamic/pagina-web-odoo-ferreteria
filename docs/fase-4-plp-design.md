# Diseño PLP (Product Listing Page) - Página de Listado de Productos

## Objetivo
Crear una experiencia de navegación eficiente que permita a los usuarios explorar el catálogo de productos con filtros intuitivos y visualización clara.

## Layout Principal

### Estructura de la Página
```
+----------------------------------------------------------+
|                    HEADER/NAVIGATION                      |
+----------------------------------------------------------+
|                                                           |
|  BREADCRUMB: Inicio > Categoría > Subcategoría          |
|                                                           |
+-------------+--------------------------------------------+
|             |                                            |
|  FILTROS    |           PRODUCTOS                        |
|  SIDEBAR    |           - Barra de herramientas          |
|             |           - Grid de productos              |
|             |           - Paginación                     |
|             |                                            |
+-------------+--------------------------------------------+
|                    FOOTER                                 |
+----------------------------------------------------------+
```

## Componentes

### 1. Breadcrumb (Migas de Pan)
- **Ubicación**: Superior, debajo del header
- **Formato**: `Inicio > Categoría Principal > Subcategoría`
- **Interactividad**: Cada nivel es clickeable
- **Objetivo**: Mejorar navegación y SEO

### 2. Barra de Herramientas (Toolbar)
**Elementos**:
- **Contador de resultados**: "Mostrando X productos"
- **Vista**: Toggles para Grid (3 columnas) / List (línea completa)
- **Ordenamiento**: Dropdown con opciones:
  - Relevancia (default)
  - Precio: Menor a Mayor
  - Precio: Mayor a Menor
  - Nombre: A-Z
  - Nombre: Z-A
  - Más Nuevos
  - Más Vendidos (si disponible)

### 3. Panel de Filtros (Sidebar Izquierdo)

#### 3.1 Categorías
- **Tipo**: Árbol colapsable
- **Funcionalidad**: 
  - Expandir/colapsar subcategorías
  - Checkbox para selección múltiple
  - Contador de productos por categoría
- **Ejemplo**:
  ```
  ☐ Herramientas Manuales (245)
    ☐ Martillos (45)
    ☐ Destornilladores (67)
    ☐ Llaves (89)
  ☐ Herramientas Eléctricas (189)
    ☐ Taladros (56)
    ☐ Amoladoras (34)
  ```

#### 3.2 Marcas
- **Tipo**: Checkboxes con búsqueda
- **Funcionalidad**:
  - Campo de búsqueda si hay más de 10 marcas
  - Mostrar primeras 10, botón "Ver más" para resto
  - Contador de productos por marca
- **Ejemplo**:
  ```
  🔍 Buscar marca...
  ☐ Bosch (67)
  ☐ DeWalt (45)
  ☐ Makita (38)
  ☐ Stanley (92)
  [+ Ver más marcas]
  ```

#### 3.3 Rango de Precio
- **Tipo**: Slider doble
- **Funcionalidad**:
  - Slider visual para seleccionar rango
  - Inputs numéricos editables (min/max)
  - Botón "Aplicar"
- **Formato**: $ 0 ----●══●---- $ 999,999
- **Inputs**: 
  ```
  Precio mínimo: [___________]
  Precio máximo: [___________]
  [Aplicar]
  ```

#### 3.4 Disponibilidad
- **Tipo**: Checkboxes
- **Opciones**:
  ```
  ☐ En stock (345)
  ☐ Bajo pedido (67)
  ```

#### 3.5 Atributos Adicionales (según categoría)
Ejemplos dinámicos por categoría:
- **Herramientas Eléctricas**:
  - Voltaje: 12V, 18V, 20V, 110V, 220V
  - Tipo de batería: Litio, Ni-Cd
- **Pinturas**:
  - Tipo: Interior, Exterior, Esmalte
  - Presentación: 1L, 4L, 20L

#### 3.6 Botón Limpiar Filtros
- **Ubicación**: Parte inferior del panel
- **Funcionalidad**: Resetear todos los filtros aplicados
- **Texto**: "Limpiar filtros"

### 4. Filtros Activos (Chips)
**Ubicación**: Entre toolbar y grid de productos
**Formato**: Chips con X para remover
```
Categoría: Taladros [x]  |  Marca: Bosch [x]  |  $500 - $2,000 [x]  |  Limpiar todo
```

### 5. Grid de Productos

#### Vista Grid (3 columnas en desktop)
**Tarjeta de Producto**:
```
+-------------------------+
|                         |
|      [IMAGEN]           |
|      250x250            |
|                         |
+-------------------------+
| Marca Producto          |
| Nombre del Producto     |
| SKU: ABC123             |
|                         |
| $XX,XXX.XX              |
| [●●●●○] (23 reseñas)    |
|                         |
| [Agregar al carrito]    |
| [♡ Favoritos]           |
+-------------------------+
```

**Elementos de la Tarjeta**:
- **Imagen**: 
  - Tamaño: 250x250px
  - Hover: Zoom sutil (1.05x)
  - Badge si aplica: "OFERTA", "NUEVO", "AGOTADO"
- **Marca**: Texto pequeño, color secundario
- **Nombre**: 2 líneas máximo, truncar con "..."
- **SKU**: Texto pequeño, gris
- **Precio**: 
  - Grande y destacado
  - Si hay descuento: precio anterior tachado + precio con descuento
- **Rating**: Estrellas + número de reseñas
- **Botón CTA**: 
  - Primario: "Agregar al carrito"
  - Si sin stock: "Consultar disponibilidad"
- **Favoritos**: Icono de corazón, toggle

#### Vista Lista (1 columna)
```
+-------+------------------------------------------------------+
| IMG   | Marca Producto                                      |
| 150px | Nombre del Producto - Descripción corta             |
|       | SKU: ABC123                                          |
|       | $XX,XXX.XX | [●●●●○] (23) | [Agregar] [♡]       |
+-------+------------------------------------------------------+
```

### 6. Paginación

**Ubicación**: Inferior del grid
**Formato**:
```
Mostrando 1-24 de 245 productos

[←] [1] [2] [3] ... [10] [→]

Mostrar por página: [24 ▼] [48] [96]
```

**Opciones**:
- Botones anterior/siguiente
- Números de página (máximo 7 visibles)
- Selector de productos por página (24, 48, 96)

## Responsive Design

### Desktop (>1024px)
- Sidebar de filtros visible
- Grid de 3 columnas
- Todas las funcionalidades visibles

### Tablet (768px - 1024px)
- Sidebar colapsable con botón "Filtros"
- Grid de 2 columnas
- Toolbar simplificado

### Mobile (<768px)
- Filtros en modal/drawer deslizante
- Grid de 1 columna
- Ordenamiento en dropdown
- Botón flotante "Filtros" (badge con número de filtros activos)

## Estados de Carga

### Loading Inicial
- Skeleton screens para tarjetas
- Shimmer effect en filtros

### Sin Resultados
```
+-------------------------------------------------+
|          🔍                                     |
|     No encontramos productos                   |
|     que coincidan con tu búsqueda              |
|                                                 |
|     Intenta:                                   |
|     • Eliminar algunos filtros                 |
|     • Verificar la ortografía                  |
|     • Usar términos más generales              |
|                                                 |
|     [Limpiar filtros]                          |
+-------------------------------------------------+
```

### Error de Carga
```
+-------------------------------------------------+
|          ⚠️                                     |
|     Hubo un problema al cargar los productos   |
|                                                 |
|     [Reintentar]                               |
+-------------------------------------------------+
```

## Interacciones y Microanimaciones

1. **Hover en tarjeta**: Sombra elevada + zoom imagen
2. **Click en filtro**: Fade-in de productos actualizados
3. **Agregar al carrito**: 
   - Feedback visual (✓ Agregado)
   - Animación de producto volando al carrito
4. **Favoritos**: Animación de corazón llenándose

## Integración con Odoo

### Endpoints Necesarios
```
GET /shop/products
  ?category=<id>
  &brand=<id>
  &price_min=<value>
  &price_max=<value>
  &in_stock=<bool>
  &sort=<field>
  &page=<num>
  &limit=<num>

Response:
{
  "products": [...],
  "total_count": 245,
  "page": 1,
  "limit": 24,
  "filters": {
    "categories": [...],
    "brands": [...],
    "price_range": {"min": 0, "max": 50000},
    "attributes": [...]
  }
}
```

### Módulos Odoo Requeridos
- `website_sale`: Funcionalidad base de e-commerce
- `website_sale_comparison`: Comparar productos
- `website_sale_wishlist`: Lista de deseos
- `stock`: Gestión de inventario para disponibilidad

## Accesibilidad (A11Y)

- **Navegación por teclado**: Tab, Enter, Espaciado
- **Screen readers**: Labels ARIA apropiados
- **Contraste**: Cumplir WCAG AA (4.5:1)
- **Foco visible**: Outline claro en elementos interactivos
- **Anuncios**: Live regions para cambios dinámicos

## SEO Considerations

- **URLs amigables**: `/productos/herramientas-electricas/taladros`
- **Meta tags**: Título y descripción dinámicos por categoría
- **Schema markup**: Product, BreadcrumbList
- **Canonical**: Evitar contenido duplicado con filtros
- **Paginación**: rel="next" / rel="prev" en páginas múltiples

## Métricas de Éxito

- Tasa de conversión por categoría
- Uso de filtros (cuáles son más usados)
- Productos más vistos
- Tiempo en página
- Bounce rate por categoría
- Add-to-cart rate
