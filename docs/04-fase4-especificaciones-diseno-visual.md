# Especificaciones de Diseño Visual - Fase 4
## Sistema de Diseño para Ferretería Web

---

## 1. Paleta de Colores

### Colores Primarios

```
Principal (Primary):
- Hex: #2563EB (Azul profesional)
- RGB: rgb(37, 99, 235)
- Uso: Botones principales, enlaces, elementos destacados

Secundario (Secondary):
- Hex: #DC2626 (Rojo ferretería)
- RGB: rgb(220, 38, 38)
- Uso: Ofertas, descuentos, CTAs de urgencia

Neutro Oscuro (Dark):
- Hex: #1F2937
- RGB: rgb(31, 41, 55)
- Uso: Textos principales, headers

Neutro Claro (Light):
- Hex: #F9FAFB
- RGB: rgb(249, 250, 251)
- Uso: Fondos alternativos, secciones
```

### Colores de Estado

```
Éxito (Success):
- Hex: #10B981 (Verde)
- Uso: Confirmaciones, productos disponibles

Advertencia (Warning):
- Hex: #F59E0B (Amarillo/Naranja)
- Uso: Últimas unidades, alertas

Error (Danger):
- Hex: #EF4444 (Rojo)
- Uso: Errores, campos inválidos

Info (Info):
- Hex: #3B82F6 (Azul claro)
- Uso: Información adicional, tooltips
```

### Escala de Grises

```
Gray-50:  #F9FAFB
Gray-100: #F3F4F6
Gray-200: #E5E7EB
Gray-300: #D1D5DB
Gray-400: #9CA3AF
Gray-500: #6B7280
Gray-600: #4B5563
Gray-700: #374151
Gray-800: #1F2937
Gray-900: #111827
```

---

## 2. Tipografía

### Fuentes

**Familia Primaria (Títulos y Body):**
```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 
             'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
```

**Familia Secundaria (Números y Precios):**
```css
font-family: 'Roboto', Arial, sans-serif;
```

### Escala Tipográfica

```
Display 1 (Hero principal):
- Tamaño: 64px / 4rem
- Peso: 700 (Bold)
- Line height: 1.1
- Uso: Títulos hero principales

Display 2 (Hero secundario):
- Tamaño: 48px / 3rem
- Peso: 700 (Bold)
- Line height: 1.2
- Uso: Títulos de página

H1 (Heading 1):
- Tamaño: 36px / 2.25rem
- Peso: 700 (Bold)
- Line height: 1.25
- Uso: Títulos principales de sección

H2 (Heading 2):
- Tamaño: 30px / 1.875rem
- Peso: 600 (Semi-bold)
- Line height: 1.3
- Uso: Subtítulos importantes

H3 (Heading 3):
- Tamaño: 24px / 1.5rem
- Peso: 600 (Semi-bold)
- Line height: 1.4
- Uso: Títulos de bloques

H4 (Heading 4):
- Tamaño: 20px / 1.25rem
- Peso: 600 (Semi-bold)
- Line height: 1.4
- Uso: Títulos menores

Body Large (Lead):
- Tamaño: 18px / 1.125rem
- Peso: 400 (Regular)
- Line height: 1.75
- Uso: Texto introductorio

Body (Regular):
- Tamaño: 16px / 1rem
- Peso: 400 (Regular)
- Line height: 1.6
- Uso: Texto general

Body Small:
- Tamaño: 14px / 0.875rem
- Peso: 400 (Regular)
- Line height: 1.5
- Uso: Texto secundario, meta información

Caption:
- Tamaño: 12px / 0.75rem
- Peso: 400 (Regular)
- Line height: 1.5
- Uso: Disclaimers, notas al pie
```

### Responsive Typography

```css
/* Mobile (< 768px) */
Display 1: 36px / 2.25rem
Display 2: 30px / 1.875rem
H1: 28px / 1.75rem
H2: 24px / 1.5rem
H3: 20px / 1.25rem
Body: 16px / 1rem (sin cambio)

/* Tablet (768px - 1024px) */
Display 1: 48px / 3rem
Display 2: 40px / 2.5rem
H1: 32px / 2rem
H2: 28px / 1.75rem
H3: 22px / 1.375rem
Body: 16px / 1rem (sin cambio)
```

---

## 3. Espaciado y Grid

### Sistema de Espaciado (Base 8px)

```
Espaciado mínimo: 4px  (0.25rem)
Espaciado pequeño: 8px  (0.5rem)
Espaciado regular: 16px (1rem)
Espaciado mediano: 24px (1.5rem)
Espaciado grande: 32px (2rem)
Espaciado XL: 48px (3rem)
Espaciado XXL: 64px (4rem)
Espaciado 3XL: 96px (6rem)
```

### Grid System

**Desktop (>= 1024px):**
```
Container max-width: 1280px
Columnas: 12
Gutter: 24px
Margen lateral: 32px
```

**Tablet (768px - 1023px):**
```
Container: 100%
Columnas: 12 (flex)
Gutter: 20px
Margen lateral: 24px
```

**Mobile (< 768px):**
```
Container: 100%
Columnas: 4-6 (flex)
Gutter: 16px
Margen lateral: 16px
```

---

## 4. Componentes UI

### Botones

**Botón Primario:**
```css
background: #2563EB;
color: #FFFFFF;
padding: 12px 24px;
border-radius: 6px;
font-size: 16px;
font-weight: 600;
box-shadow: 0 1px 3px rgba(0,0,0,0.1);
transition: all 0.2s ease;

/* Hover */
background: #1D4ED8;
box-shadow: 0 4px 6px rgba(0,0,0,0.15);
```

**Botón Secundario:**
```css
background: transparent;
color: #2563EB;
border: 2px solid #2563EB;
padding: 10px 22px;
border-radius: 6px;

/* Hover */
background: #2563EB;
color: #FFFFFF;
```

**Botón Tamaños:**
- Small: padding 8px 16px, font-size 14px
- Medium: padding 12px 24px, font-size 16px (default)
- Large: padding 16px 32px, font-size 18px

**Botón Estados:**
```css
/* Disabled */
opacity: 0.5;
cursor: not-allowed;

/* Loading */
opacity: 0.7;
cursor: wait;
/* Agregar spinner */
```

### Cards

```css
background: #FFFFFF;
border-radius: 8px;
box-shadow: 0 1px 3px rgba(0,0,0,0.1);
padding: 24px;
transition: box-shadow 0.3s ease;

/* Hover */
box-shadow: 0 10px 25px rgba(0,0,0,0.1);
transform: translateY(-2px);
```

### Inputs y Forms

```css
/* Input de texto */
padding: 12px 16px;
border: 1px solid #D1D5DB;
border-radius: 6px;
font-size: 16px;
background: #FFFFFF;

/* Focus */
border-color: #2563EB;
box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
outline: none;

/* Error */
border-color: #EF4444;

/* Disabled */
background: #F3F4F6;
cursor: not-allowed;
```

### Badges y Tags

```css
/* Badge */
padding: 4px 12px;
border-radius: 9999px;
font-size: 12px;
font-weight: 600;

/* Badge Success */
background: #D1FAE5;
color: #065F46;

/* Badge Warning */
background: #FEF3C7;
color: #92400E;

/* Badge Danger */
background: #FEE2E2;
color: #991B1B;
```

---

## 5. Iconografía

### Sistema de Íconos

**Librería:** Font Awesome 5 Free (incluida en Odoo)

**Tamaños:**
```
Pequeño: 16px / 1rem
Regular: 20px / 1.25rem
Mediano: 24px / 1.5rem
Grande: 32px / 2rem
XL: 48px / 3rem
```

**Íconos Principales:**
```
Carrito: fa-shopping-cart
Usuario: fa-user
Búsqueda: fa-search
Menú móvil: fa-bars
Teléfono: fa-phone
Email: fa-envelope
Ubicación: fa-map-marker-alt
WhatsApp: fab fa-whatsapp
Facebook: fab fa-facebook
Instagram: fab fa-instagram
Check/Éxito: fa-check-circle
Error: fa-times-circle
Info: fa-info-circle
Envío: fa-shipping-fast
Garantía: fa-shield-alt
```

---

## 6. Imágenes y Media

### Formatos y Optimización

**Formato recomendado:**
- Fotos/Hero: WebP (fallback JPG)
- Logos/Íconos: SVG
- Fotos de productos: JPG optimizado

**Tamaños máximos:**
- Hero Banner: 1920x800px, < 200KB
- Producto grid: 600x600px, < 80KB
- Thumbnails: 300x300px, < 30KB
- Logos: SVG o PNG 200x80px

**Aspect Ratios:**
- Hero: 16:9 o 21:9
- Productos: 1:1 (cuadrado)
- Categorías: 4:3
- Blog/Contenido: 16:9

### Lazy Loading

```html
<img src="placeholder.jpg" 
     data-src="imagen-real.jpg" 
     loading="lazy" 
     alt="Descripción"/>
```

---

## 7. Animaciones y Transiciones

### Timing Functions

```css
/* Suave (General) */
transition: all 0.3s ease;

/* Rápida (Hover, Click) */
transition: all 0.2s ease;

/* Lenta (Carruseles) */
transition: all 0.6s ease-in-out;
```

### Animaciones Comunes

**Fade In:**
```css
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
animation: fadeIn 0.5s ease;
```

**Slide Up:**
```css
@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
animation: slideUp 0.5s ease;
```

**Hover Scale:**
```css
transition: transform 0.3s ease;
&:hover {
    transform: scale(1.05);
}
```

---

## 8. Sombras (Shadows)

```css
/* Sombra pequeña (Cards) */
box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);

/* Sombra mediana (Cards hover) */
box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);

/* Sombra grande (Modals) */
box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);

/* Sombra XL (Dropdowns) */
box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
```

---

## 9. Breakpoints

```css
/* Extra Small (Mobile) */
@media (max-width: 575.98px) { }

/* Small (Mobile landscape) */
@media (min-width: 576px) and (max-width: 767.98px) { }

/* Medium (Tablet) */
@media (min-width: 768px) and (max-width: 991.98px) { }

/* Large (Tablet landscape / Desktop) */
@media (min-width: 992px) and (max-width: 1199.98px) { }

/* Extra Large (Desktop) */
@media (min-width: 1200px) { }

/* XXL (Large Desktop) */
@media (min-width: 1400px) { }
```

---

## 10. Estados de Interacción

### Hover
```css
cursor: pointer;
transition: all 0.2s ease;
/* Cambio de color, sombra o escala */
```

### Focus (Accesibilidad)
```css
outline: none;
box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.2);
```

### Active (Click)
```css
transform: scale(0.98);
```

### Disabled
```css
opacity: 0.5;
cursor: not-allowed;
pointer-events: none;
```

---

## 11. Layout de Páginas

### Home Page

```
┌─────────────────────────────────┐
│        Header + Menú            │
├─────────────────────────────────┤
│        Hero Banner              │
│      (Full width, ~600px)       │
├─────────────────────────────────┤
│    Categorías Destacadas        │
│     (Grid 4 columnas)           │
├─────────────────────────────────┤
│    Productos Destacados         │
│      (Carrusel horizontal)      │
├─────────────────────────────────┤
│       Beneficios                │
│     (Grid 4 columnas)           │
├─────────────────────────────────┤
│    Marcas Destacadas            │
│     (Grid 6 logos)              │
├─────────────────────────────────┤
│      Newsletter                 │
├─────────────────────────────────┤
│         Footer                  │
└─────────────────────────────────┘
```

### Nosotros

```
┌─────────────────────────────────┐
│        Header + Menú            │
├─────────────────────────────────┤
│      Hero con Imagen            │
├─────────────────────────────────┤
│   Historia (2 columnas)         │
│   Texto + Imagen                │
├─────────────────────────────────┤
│   Misión, Visión, Valores       │
│      (3 cards)                  │
├─────────────────────────────────┤
│       CTA Section               │
├─────────────────────────────────┤
│         Footer                  │
└─────────────────────────────────┘
```

### Contacto

```
┌─────────────────────────────────┐
│        Header + Menú            │
├─────────────────────────────────┤
│       Page Header               │
├─────────────────────────────────┤
│    Formulario   │  Info          │
│   (60%)         │  Contacto      │
│                 │  (40%)         │
├─────────────────────────────────┤
│      Mapa de Ubicación          │
│        (Full width)             │
├─────────────────────────────────┤
│         Footer                  │
└─────────────────────────────────┘
```

---

## 12. Accesibilidad (WCAG 2.1)

### Contraste de Colores

**Mínimo AA:**
- Texto normal: 4.5:1
- Texto grande (>18px): 3:1

**Combinaciones Aprobadas:**
- #2563EB sobre #FFFFFF: ✓ (4.54:1)
- #FFFFFF sobre #2563EB: ✓ (4.54:1)
- #1F2937 sobre #FFFFFF: ✓ (16.05:1)

### Interactividad

- Todos los elementos interactivos > 44x44px (táctiles)
- Focus visible en navegación por teclado
- Alt text en todas las imágenes
- Labels en todos los inputs
- ARIA labels donde sea necesario

### Navegación por Teclado

- Tab: Navegar adelante
- Shift+Tab: Navegar atrás
- Enter/Space: Activar elemento
- Escape: Cerrar modals/dropdowns

---

## 13. Performance

### Métricas Objetivo

```
First Contentful Paint (FCP): < 1.8s
Largest Contentful Paint (LCP): < 2.5s
Time to Interactive (TTI): < 3.8s
Cumulative Layout Shift (CLS): < 0.1
First Input Delay (FID): < 100ms
```

### Optimizaciones

- Minificar CSS y JS
- Lazy loading de imágenes
- Usar WebP con fallback
- Cargar fuentes de forma asíncrona
- Reducir JavaScript innecesario
- Implementar caché de navegador

---

## 14. Diseño Mobile-First

### Principios

1. Diseñar primero para mobile (320px+)
2. Progressive enhancement para desktop
3. Touch targets mínimo 44x44px
4. Menú hamburger en mobile
5. Stacking vertical en mobile
6. Fuentes >= 16px para evitar zoom iOS

### Patrones Responsive

**Navegación:**
- Desktop: Horizontal top menu
- Mobile: Hamburger menu + drawer

**Grids:**
- Desktop: 4-6 columnas
- Tablet: 2-3 columnas
- Mobile: 1-2 columnas

**Formularios:**
- Desktop: 2 columnas
- Mobile: 1 columna, full width

---

## 15. Recursos de Diseño

### Herramientas Recomendadas

- **Diseño:** Figma, Adobe XD
- **Prototipado:** Figma, InVision
- **Iconos:** Font Awesome, Heroicons
- **Imágenes:** Unsplash, Pexels
- **Optimización:** TinyPNG, Squoosh

### Referencias

- Material Design: https://material.io/design
- Tailwind CSS: https://tailwindcss.com/docs
- Bootstrap 4: https://getbootstrap.com/docs/4.6/
- Odoo UI: https://www.odoo.com/documentation/16.0/developer/howtos/website_themes.html

---

## 16. Checklist de Diseño

### Antes de Implementar
- [ ] Paleta de colores definida
- [ ] Tipografía seleccionada
- [ ] Componentes diseñados
- [ ] Wireframes aprobados
- [ ] Mockups desktop y mobile
- [ ] Prototype interactivo (opcional)

### Durante Implementación
- [ ] Seguir sistema de diseño
- [ ] Usar clases consistentes
- [ ] Mantener espaciado uniforme
- [ ] Validar contraste de colores
- [ ] Probar en múltiples dispositivos

### Después de Implementar
- [ ] Validar accesibilidad
- [ ] Probar performance
- [ ] Cross-browser testing
- [ ] QA de diseño vs mockup
- [ ] Documentar desviaciones

---

**Fecha de creación**: 2026-02-24  
**Última actualización**: 2026-02-24  
**Versión**: 1.0  
**Estado**: Definición completa
