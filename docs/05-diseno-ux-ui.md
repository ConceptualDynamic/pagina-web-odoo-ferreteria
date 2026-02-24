# Diseño UX/UI
Home orientada a conversión, páginas institucionales y experiencia PLP/PDP.
Criterios de consistencia visual y usabilidad móvil.

## Documentos de Diseño Detallados

### Fase 4: Diseño de Tienda (PLP/PDP)

#### PLP - Product Listing Page (Listado de Productos)
Página de listado de productos con filtros avanzados y experiencia de navegación optimizada.

**Documento detallado**: [`fase-4-plp-design.md`](./fase-4-plp-design.md)

**Componentes principales**:
- Layout responsivo con sidebar de filtros
- Filtros por categoría, marca, precio y disponibilidad
- Grid de productos con vista Grid/List
- Tarjetas de producto con información clave
- Sistema de ordenamiento múltiple
- Paginación avanzada

**Características clave**:
- Breadcrumb para navegación
- Filtros activos con chips removibles
- Vista móvil con drawer de filtros
- Skeleton loaders para mejor UX
- Integración con módulos Odoo: `website_sale`, `website_sale_comparison`, `website_sale_wishlist`

---

#### PDP - Product Detail Page (Ficha de Producto)
Página de detalle del producto diseñada para maximizar conversión.

**Documento detallado**: [`fase-4-pdp-design.md`](./fase-4-pdp-design.md)

**Componentes principales**:
- Galería de imágenes con zoom y lightbox
- Información completa del producto (nombre, SKU, precio, stock)
- CTAs destacados (Agregar al carrito, Comprar ahora)
- Tabs de contenido (Descripción, Especificaciones, Reseñas)
- Productos relacionados y comprados juntos
- Trust badges y garantías

**Características clave**:
- Diseño responsive con sticky CTA en móvil
- Sistema de reseñas y valoraciones
- Schema markup para SEO
- OpenGraph tags para compartir en redes
- Integración con módulos Odoo: `website_sale`, `portal_rating`, `stock`, `delivery`

---

#### Guía de Implementación Técnica
Para desarrolladores que implementarán estos diseños en Odoo.

**Documento detallado**: [`fase-4-implementation-guide.md`](./fase-4-implementation-guide.md)

**Contenido**:
- Estructura de archivos del módulo custom
- Templates QWeb completos para PLP y PDP
- Controladores Python personalizados
- Estilos SCSS con variables y mixins
- JavaScript para interacciones
- Endpoints de API necesarios
- Guías de accesibilidad y SEO

---

## Principios de Diseño

### Consistencia Visual
- Paleta de colores coherente en todas las páginas
- Tipografía consistente con jerarquía clara
- Espaciado y grid system unificado
- Iconografía consistente (Font Awesome)

### Usabilidad Móvil (Mobile-First)
- Diseño responsive desde 320px
- Touch targets mínimo 44x44px
- Navegación simplificada en móvil
- CTAs accesibles con pulgar
- Carga optimizada de imágenes

### Conversión
- CTAs claros y destacados
- Menos fricción en el proceso de compra
- Trust badges y garantías visibles
- Información de envío clara
- Sistema de reseñas para social proof

### Accesibilidad (WCAG AA)
- Contraste de color 4.5:1 mínimo
- Navegación por teclado completa
- Labels ARIA apropiados
- Soporte para lectores de pantalla
- Focus visible en elementos interactivos

### Performance
- Lazy loading de imágenes
- Minimización de assets (CSS/JS)
- Cache de recursos estáticos
- Compresión de imágenes
- Skeleton screens para loading states
