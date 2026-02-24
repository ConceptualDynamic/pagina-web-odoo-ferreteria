# SEO y contenido

## 1. Metadatos Técnicos

### 1.1 Meta Tags Esenciales
Cada página debe incluir los siguientes meta tags:

**Meta Tags Básicos:**
```html
<title>[Título específico de página] | Ferretería [Nombre]</title>
<meta name="description" content="[Descripción única de 150-160 caracteres]">
<meta name="keywords" content="ferretería, herramientas, construcción, [palabras clave específicas]">
<meta name="robots" content="index, follow">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta charset="UTF-8">
```

**Open Graph (OG) Tags para Redes Sociales:**
```html
<meta property="og:title" content="[Título específico de página]">
<meta property="og:description" content="[Descripción de 150-160 caracteres]">
<meta property="og:image" content="[URL imagen destacada, min 1200x630px]">
<meta property="og:url" content="[URL canónica de la página]">
<meta property="og:type" content="website"> <!-- "product" para PDPs -->
<meta property="og:site_name" content="Ferretería [Nombre]">
<meta property="og:locale" content="es_CO"> <!-- Ajustar según país -->
```

**Twitter Card Tags:**
```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="[Título específico de página]">
<meta name="twitter:description" content="[Descripción de 150-160 caracteres]">
<meta name="twitter:image" content="[URL imagen destacada]">
```

**Tags Adicionales para Productos (PDP):**
```html
<meta property="product:price:amount" content="[precio]">
<meta property="product:price:currency" content="COP"> <!-- Ajustar según moneda -->
<meta property="product:availability" content="in stock"> <!-- o "out of stock" -->
<meta property="product:brand" content="[marca del producto]">
```

### 1.2 Configuración por Tipo de Página

**Homepage:**
- Title: "Ferretería [Nombre] | Herramientas y Materiales de Construcción"
- Description: "La mejor ferretería con herramientas profesionales, materiales de construcción y productos de calidad. Envíos a toda Colombia. ¡Compra online ahora!"

**PLP (Product Listing Page - Categoría):**
- Title: "[Categoría] | Ferretería [Nombre]"
- Description: "Encuentra los mejores [categoría] en Ferretería [Nombre]. Amplio catálogo, precios competitivos y envío rápido."

**PDP (Product Detail Page):**
- Title: "[Nombre del Producto] | [Marca] | Ferretería [Nombre]"
- Description: "[Nombre del producto] de [marca]. [Características principales]. Compra online con envío rápido."

**Páginas Institucionales:**
- Nosotros: "Nosotros | Ferretería [Nombre]"
- Contacto: "Contacto | Ferretería [Nombre]"
- FAQs: "Preguntas Frecuentes | Ferretería [Nombre]"

## 2. URLs Amigables (SEO-Friendly)

### 2.1 Estructura de URLs
```
https://[dominio].com/
https://[dominio].com/productos/
https://[dominio].com/productos/[categoria]/
https://[dominio].com/productos/[categoria]/[subcategoria]/
https://[dominio].com/p/[nombre-producto-slug]
https://[dominio].com/marcas/[marca]/
https://[dominio].com/ofertas/
https://[dominio].com/nosotros/
https://[dominio].com/contacto/
https://[dominio].com/faqs/
```

### 2.2 Reglas para URLs
- Usar minúsculas
- Usar guiones (-) en lugar de guiones bajos (_)
- Evitar caracteres especiales (tildes convertir a vocal normal)
- Máximo 60 caracteres
- Incluir palabras clave relevantes
- Evitar parámetros innecesarios (?id=123)

**Ejemplos:**
- ❌ Malo: `/producto.php?id=123&cat=herramientas`
- ✅ Bueno: `/p/taladro-electrico-bosch-750w`

## 3. Sitemap.xml

### 3.1 Configuración de Sitemap
Crear archivo `sitemap.xml` en raíz del dominio:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <!-- Homepage -->
  <url>
    <loc>https://[dominio].com/</loc>
    <lastmod>2026-02-24</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  
  <!-- Páginas de Categorías -->
  <url>
    <loc>https://[dominio].com/productos/herramientas-electricas/</loc>
    <lastmod>2026-02-24</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  
  <!-- Páginas de Productos -->
  <url>
    <loc>https://[dominio].com/p/taladro-electrico-bosch-750w/</loc>
    <lastmod>2026-02-20</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  
  <!-- Páginas Institucionales -->
  <url>
    <loc>https://[dominio].com/nosotros/</loc>
    <lastmod>2026-02-15</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
</urlset>
```

### 3.2 Prioridades Sugeridas
- Homepage: 1.0
- Categorías principales: 0.8
- Subcategorías: 0.7
- Productos: 0.6
- Páginas institucionales: 0.5
- Blog/noticias: 0.4

### 3.3 Frecuencia de Actualización
- Homepage: weekly
- Categorías: weekly
- Productos: monthly (o weekly si hay cambios frecuentes de stock/precio)
- Páginas estáticas: monthly

## 4. Robots.txt

### 4.1 Configuración de robots.txt
Crear archivo `robots.txt` en raíz del dominio:

```
# robots.txt para Ferretería [Nombre]

User-agent: *
Allow: /
Disallow: /admin/
Disallow: /carrito/
Disallow: /checkout/
Disallow: /mi-cuenta/
Disallow: /api/
Disallow: /*?*sessionid=
Disallow: /*?*sort=
Disallow: /*?*filter=

# Sitemap
Sitemap: https://[dominio].com/sitemap.xml

# Crawl-delay para bots específicos (opcional)
User-agent: Googlebot
Crawl-delay: 0

User-agent: Bingbot
Crawl-delay: 1
```

### 4.2 URLs a Bloquear
- Panel de administración
- Procesos de checkout
- Área de cliente/cuenta
- APIs internas
- URLs con parámetros de sesión o filtros temporales

## 5. Optimización de Imágenes

### 5.1 Especificaciones Técnicas
**Imágenes de Productos:**
- Formato: WebP (fallback a JPG)
- Tamaño principal: 800x800px
- Thumbnails: 200x200px
- Zoom: 1200x1200px
- Peso máximo: 150KB (principal), 30KB (thumbnails)
- Calidad: 80-85%

**Imágenes de Banner/Hero:**
- Formato: WebP (fallback a JPG)
- Desktop: 1920x600px
- Mobile: 800x800px
- Peso máximo: 200KB
- Calidad: 85%

**Imágenes de Categoría:**
- Formato: WebP (fallback a JPG)
- Tamaño: 400x400px
- Peso máximo: 80KB
- Calidad: 80%

### 5.2 Atributos Alt y Title
```html
<!-- Productos -->
<img src="taladro-bosch-750w.webp" 
     alt="Taladro eléctrico Bosch 750W con cable"
     title="Taladro Bosch 750W - Ferretería [Nombre]"
     width="800" 
     height="800"
     loading="lazy">

<!-- Categorías -->
<img src="categoria-herramientas.webp" 
     alt="Categoría de herramientas eléctricas"
     title="Herramientas Eléctricas - Ferretería [Nombre]"
     loading="lazy">
```

### 5.3 Lazy Loading
- Implementar lazy loading para todas las imágenes excepto las above-the-fold
- Usar atributo `loading="lazy"` en imágenes
- Considerar usar Intersection Observer API para control fino

### 5.4 Responsive Images
```html
<picture>
  <source media="(min-width: 768px)" 
          srcset="producto-desktop.webp" 
          type="image/webp">
  <source media="(min-width: 768px)" 
          srcset="producto-desktop.jpg" 
          type="image/jpeg">
  <source srcset="producto-mobile.webp" 
          type="image/webp">
  <img src="producto-mobile.jpg" 
       alt="[Descripción del producto]"
       loading="lazy">
</picture>
```

## 6. Contenido Comercial Mínimo Viable

### 6.1 Homepage

**Hero Section:**
- Título principal: "La Ferretería de Confianza para Profesionales y Hogar"
- Subtítulo: "Herramientas de calidad, precios justos y envío rápido"
- CTA principal: "Ver Productos" (botón destacado)
- CTA secundario: "Ofertas del Mes"

**Sección de Valor:**
```
¿Por qué elegirnos?

✓ Amplio Catálogo
Más de [X] productos en herramientas, materiales y accesorios

✓ Marcas Reconocidas
Trabajamos con las mejores marcas del mercado

✓ Envío Rápido
Despachos en 24-48 horas a toda Colombia

✓ Atención Personalizada
Asesoría experta para tus proyectos

✓ Precios Competitivos
Garantizamos los mejores precios del mercado

✓ Compra Segura
Pago seguro y múltiples formas de pago
```

**Categorías Destacadas:**
- Herramientas Eléctricas
- Herramientas Manuales
- Materiales de Construcción
- Pintura y Acabados
- Electricidad y Iluminación
- Plomería y Grifería

**Productos Destacados:**
- Mostrar 8-12 productos más vendidos o en oferta
- Incluir: imagen, nombre, precio, disponibilidad, botón "Ver más"

**Call to Action Final:**
- "¿Necesitas asesoría? Contáctanos"
- Botón de WhatsApp o formulario de contacto

### 6.2 Páginas de Categoría (PLP)

**Estructura del Contenido:**
```
[Nombre de Categoría]

[Descripción breve de 2-3 párrafos sobre la categoría]

En Ferretería [Nombre] encontrarás la más amplia selección de [categoría] 
para profesionales y aficionados. Contamos con las mejores marcas como 
[Marca 1], [Marca 2], [Marca 3] y más.

Nuestro catálogo incluye:
• [Subcategoría 1]
• [Subcategoría 2]
• [Subcategoría 3]
• [Subcategoría 4]

[Grid de productos con filtros]

---

[Sección informativa adicional al final - SEO]
Todo lo que necesitas saber sobre [categoría]

[Contenido educativo de 200-300 palabras sobre la categoría, 
usos, recomendaciones, etc.]
```

**Ejemplo para "Herramientas Eléctricas":**
```
Herramientas Eléctricas

Descubre nuestra amplia gama de herramientas eléctricas profesionales 
para construcción, carpintería y proyectos de bricolaje. Taladros, 
sierras, lijadoras, amoladoras y más de las marcas más confiables 
del mercado.

En Ferretería [Nombre] trabajamos con marcas líderes como Bosch, Makita, 
DeWalt y Black+Decker, garantizando calidad, durabilidad y el mejor 
rendimiento para tus proyectos.

Nuestro catálogo incluye:
• Taladros y atornilladores
• Sierras eléctricas y caladoras
• Lijadoras y pulidoras
• Amoladoras y esmeriladoras
• Martillos y taladros percutores
• Herramientas multifunción

[Productos]

---

Guía de Compra: Herramientas Eléctricas

Las herramientas eléctricas son indispensables para cualquier trabajo 
de construcción, remodelación o carpintería. Al elegir tu herramienta, 
considera la potencia necesaria, la frecuencia de uso y el tipo de 
material con el que trabajarás.

Para uso profesional, recomendamos herramientas con mayor potencia 
y durabilidad. Para proyectos caseros ocasionales, las líneas de 
bricolaje ofrecen excelente relación calidad-precio.

Todas nuestras herramientas cuentan con garantía del fabricante y 
soporte técnico. Compra con confianza en Ferretería [Nombre].
```

### 6.3 Páginas de Producto (PDP)

**Estructura del Contenido:**
```
[Nombre del Producto] - [Marca]

[Galería de imágenes]

Precio: $[precio]
SKU: [código]
Disponibilidad: [En stock / Bajo pedido]

[Descripción breve - 2-3 líneas]

[Botón CTA: "Agregar al Carrito"]
[Botón secundario: "Consultar por WhatsApp"]

---

Características Principales:
• [Característica 1]
• [Característica 2]
• [Característica 3]
• [Característica 4]

---

Descripción Detallada:

[Descripción completa del producto de 3-4 párrafos, incluyendo:
- Uso y aplicaciones
- Ventajas y beneficios
- Especificaciones técnicas
- Información sobre la marca]

---

Especificaciones Técnicas:
| Característica | Valor |
|---------------|-------|
| Marca | [marca] |
| Modelo | [modelo] |
| Potencia | [potencia] |
| Voltaje | [voltaje] |
| Peso | [peso] |
| Dimensiones | [dimensiones] |
| Garantía | [período garantía] |

---

Productos Relacionados:
[4-6 productos relacionados o complementarios]
```

### 6.4 Página "Nosotros"

```
Nosotros

Sobre Ferretería [Nombre]

Somos una ferretería comprometida con ofrecer productos de calidad, 
precios justos y un servicio excepcional para profesionales y proyectos 
del hogar.

Nuestra Misión
Proveer las mejores herramientas y materiales de construcción, 
respaldados por asesoría experta y un servicio al cliente de excelencia.

Nuestra Visión
Ser la ferretería de referencia en [ciudad/región], reconocida por 
nuestra calidad, variedad y compromiso con nuestros clientes.

Nuestros Valores:
• Calidad: Trabajamos solo con productos y marcas confiables
• Servicio: Atención personalizada y asesoría profesional
• Confianza: Transparencia y honestidad en cada transacción
• Innovación: Incorporamos tecnología para mejorar tu experiencia

[Historia de la empresa - 2-3 párrafos]

Por qué Elegirnos:
✓ [X] años de experiencia en el sector
✓ Más de [X] clientes satisfechos
✓ [X]+ productos en catálogo
✓ Envíos a toda Colombia
✓ Asesoría técnica especializada
✓ Garantía en todos nuestros productos

Contáctanos
[Información de contacto, horarios, dirección física si aplica]
```

### 6.5 Página de Contacto

```
Contacto

¿Tienes preguntas? Estamos aquí para ayudarte

Formulario de Contacto:
- Nombre completo
- Email
- Teléfono
- Asunto
- Mensaje
[Botón: Enviar Mensaje]

---

Otros Canales de Atención:

📱 WhatsApp: [número]
📧 Email: contacto@[dominio].com
📞 Teléfono: [número]

Horario de Atención:
Lunes a Viernes: 8:00 AM - 6:00 PM
Sábados: 9:00 AM - 2:00 PM
Domingos: Cerrado

---

Preguntas Frecuentes:
¿Tienes una pregunta rápida? Consulta nuestras [FAQs]
```

### 6.6 Página de FAQs

```
Preguntas Frecuentes

Sobre Pedidos

¿Cómo puedo realizar un pedido?
[Respuesta]

¿Cuáles son los métodos de pago disponibles?
[Respuesta]

¿Puedo modificar o cancelar mi pedido?
[Respuesta]

---

Sobre Envíos

¿Cuánto tarda el envío?
[Respuesta]

¿Cuál es el costo de envío?
[Respuesta]

¿Hacen envíos a todo el país?
[Respuesta]

---

Sobre Productos

¿Los productos tienen garantía?
[Respuesta]

¿Puedo devolver un producto?
[Respuesta]

¿Cómo sé si un producto está disponible?
[Respuesta]

---

¿No encontraste tu respuesta?
Contáctanos a través de [WhatsApp/Email/Teléfono]
```

## 7. Structured Data (Schema.org)

### 7.1 Schema para Organización
```json
{
  "@context": "https://schema.org",
  "@type": "HardwareStore",
  "name": "Ferretería [Nombre]",
  "image": "https://[dominio].com/logo.png",
  "url": "https://[dominio].com",
  "telephone": "[teléfono]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[dirección]",
    "addressLocality": "[ciudad]",
    "addressRegion": "[departamento]",
    "postalCode": "[código postal]",
    "addressCountry": "CO"
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "08:00",
      "closes": "18:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Saturday",
      "opens": "09:00",
      "closes": "14:00"
    }
  ],
  "priceRange": "$$"
}
```

### 7.2 Schema para Productos
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "[Nombre del Producto]",
  "image": "[URL imagen principal]",
  "description": "[Descripción del producto]",
  "sku": "[SKU]",
  "brand": {
    "@type": "Brand",
    "name": "[Marca]"
  },
  "offers": {
    "@type": "Offer",
    "url": "[URL del producto]",
    "priceCurrency": "COP",
    "price": "[precio]",
    "availability": "https://schema.org/InStock",
    "seller": {
      "@type": "Organization",
      "name": "Ferretería [Nombre]"
    }
  }
}
```

### 7.3 Schema para Breadcrumbs
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Inicio",
      "item": "https://[dominio].com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Productos",
      "item": "https://[dominio].com/productos"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Herramientas Eléctricas",
      "item": "https://[dominio].com/productos/herramientas-electricas"
    }
  ]
}
```

## 8. Performance y Core Web Vitals

### 8.1 Métricas Objetivo
- **LCP (Largest Contentful Paint)**: < 2.5s
- **FID (First Input Delay)**: < 100ms
- **CLS (Cumulative Layout Shift)**: < 0.1

### 8.2 Optimizaciones Técnicas
- Minificación de CSS y JavaScript
- Compresión GZIP/Brotli
- CDN para assets estáticos
- Cache del navegador (mínimo 1 año para assets versionados)
- Preload para recursos críticos
- DNS prefetch para dominios externos

## 9. Implementación en Odoo

### 9.1 Módulos Recomendados
- **website_seo**: Gestión de SEO en Odoo
- **website_canonical_url**: URLs canónicas
- **website_google_analytics**: Google Analytics
- **website_sitemap**: Generación automática de sitemap

### 9.2 Configuración SEO por Defecto
```python
# En configuración de sitio web
{
    'website_meta_title': 'Ferretería [Nombre] | Herramientas y Materiales',
    'website_meta_description': 'La mejor ferretería con herramientas...',
    'website_meta_keywords': 'ferretería, herramientas, construcción',
    'website_meta_og_img': '/web/image/website/1/logo',
    'website_meta_twitter_card': 'summary_large_image',
}
```

### 9.3 Template SEO para Productos
```xml
<!-- En template de producto -->
<t t-call="website.layout">
  <t t-set="additional_title" t-value="product.name"/>
  <t t-set="meta_description" t-value="product.description_sale[:160]"/>
  <t t-set="meta_image" t-value="product.image_1920"/>
  
  <!-- Contenido del producto -->
</t>
```

## 10. Checklist de Implementación

### 10.1 Configuración Inicial
- [ ] Configurar dominio y certificado SSL (HTTPS)
- [ ] Instalar y configurar módulos SEO de Odoo
- [ ] Configurar Google Search Console
- [ ] Configurar Google Analytics / Google Tag Manager
- [ ] Crear y verificar robots.txt
- [ ] Crear y enviar sitemap.xml

### 10.2 Meta Tags
- [ ] Implementar meta tags básicos en todas las páginas
- [ ] Implementar Open Graph tags
- [ ] Implementar Twitter Card tags
- [ ] Configurar meta tags dinámicos para productos
- [ ] Verificar meta tags con herramientas (Screaming Frog, etc.)

### 10.3 URLs
- [ ] Configurar estructura de URLs amigables
- [ ] Implementar redirects 301 si hay URLs antiguas
- [ ] Configurar URLs canónicas
- [ ] Verificar que no haya URLs duplicadas

### 10.4 Contenido
- [ ] Redactar y publicar contenido de homepage
- [ ] Redactar descripciones para categorías principales
- [ ] Redactar página "Nosotros"
- [ ] Redactar página de Contacto
- [ ] Crear FAQs básicas
- [ ] Redactar políticas (privacidad, términos, devoluciones)

### 10.5 Imágenes
- [ ] Optimizar todas las imágenes (WebP + fallback)
- [ ] Agregar atributos alt y title
- [ ] Implementar lazy loading
- [ ] Configurar imágenes responsive
- [ ] Comprimir y optimizar peso de imágenes

### 10.6 Structured Data
- [ ] Implementar schema de Organization
- [ ] Implementar schema de Product
- [ ] Implementar schema de Breadcrumbs
- [ ] Validar structured data con Google Rich Results Test

### 10.7 Performance
- [ ] Minificar CSS y JavaScript
- [ ] Configurar compresión (GZIP/Brotli)
- [ ] Configurar cache del navegador
- [ ] Implementar CDN si es necesario
- [ ] Optimizar Core Web Vitals

### 10.8 Testing
- [ ] Verificar responsive design (móvil, tablet, desktop)
- [ ] Test de velocidad (PageSpeed Insights, GTmetrix)
- [ ] Test de usabilidad móvil (Google Mobile-Friendly Test)
- [ ] Verificar indexación en Google Search Console
- [ ] Revisar errores en Search Console

## 11. Monitoreo y Mantenimiento

### 11.1 Herramientas de Monitoreo
- Google Search Console (errores, indexación, rendimiento)
- Google Analytics (tráfico, conversiones, comportamiento)
- PageSpeed Insights (performance)
- Screaming Frog (auditorías técnicas)

### 11.2 KPIs SEO a Seguir
- Posicionamiento de palabras clave objetivo
- Tráfico orgánico (sesiones, usuarios)
- Tasa de rebote
- Tiempo en sitio
- Páginas indexadas
- Errores de rastreo
- Core Web Vitals

### 11.3 Tareas de Mantenimiento
- Actualizar sitemap.xml mensualmente (automático en Odoo)
- Revisar y corregir errores en Search Console semanalmente
- Actualizar contenido de categorías trimestralmente
- Optimizar nuevas imágenes antes de publicar
- Revisar performance mensualmente

## 12. Próximos Pasos (Post-MVP)

- Implementar blog para contenido educativo
- Crear guías de compra por categoría
- Implementar sistema de reviews y ratings
- Agregar videos de productos
- Crear contenido para long-tail keywords
- Implementar estrategia de link building
- Crear landing pages para campañas específicas
