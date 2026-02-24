# Arquitectura de información

## 1. Estructura del menú principal

### 1.1 Navegación primaria
El menú principal del sitio estará compuesto por los siguientes elementos de nivel superior:

| Elemento | Descripción | Tipo |
|----------|-------------|------|
| **Inicio** | Página de inicio del sitio | Página estática |
| **Productos** | Catálogo completo con categorías | Mega menú desplegable |
| **Marcas** | Listado de marcas disponibles | Página dinámica |
| **Ofertas** | Promociones y descuentos vigentes | Página dinámica |
| **Nosotros** | Información institucional | Página estática |
| **Contacto** | Formulario de contacto y ubicaciones | Página estática |

### 1.2 Mega menú de "Productos"
El menú de productos se desplegará mostrando las categorías principales organizadas en columnas:

```
PRODUCTOS
├─ Herramientas Manuales
│  ├─ Llaves y Dados
│  ├─ Destornilladores
│  ├─ Martillos y Mazos
│  ├─ Alicates y Pinzas
│  └─ Sierras Manuales
│
├─ Herramientas Eléctricas
│  ├─ Taladros
│  ├─ Lijadoras
│  ├─ Sierras Eléctricas
│  ├─ Amoladoras
│  └─ Atornilladores
│
├─ Materiales de Construcción
│  ├─ Cemento y Mortero
│  ├─ Ladrillos y Bloques
│  ├─ Arena y Grava
│  ├─ Yeso y Masilla
│  └─ Impermeabilizantes
│
├─ Pinturas y Acabados
│  ├─ Pinturas Interiores
│  ├─ Pinturas Exteriores
│  ├─ Barnices y Lacas
│  ├─ Brochas y Rodillos
│  └─ Accesorios de Pintura
│
├─ Plomería
│  ├─ Tuberías y Conexiones
│  ├─ Llaves y Grifos
│  ├─ Sanitarios
│  ├─ Tanques y Cisternas
│  └─ Accesorios de Baño
│
├─ Electricidad
│  ├─ Cables y Conductores
│  ├─ Interruptores y Tomacorrientes
│  ├─ Tableros Eléctricos
│  ├─ Iluminación
│  └─ Extensiones y Regletas
│
├─ Ferretería General
│  ├─ Tornillería y Clavos
│  ├─ Cerraduras y Candados
│  ├─ Bisagras y Herrajes
│  ├─ Adhesivos y Selladores
│  └─ Cintas y Amarres
│
└─ Jardinería y Exterior
   ├─ Herramientas de Jardín
   ├─ Mangueras y Aspersores
   ├─ Fertilizantes y Tierra
   ├─ Macetas y Contenedores
   └─ Iluminación Exterior
```

### 1.3 Navegación secundaria
Elementos adicionales en el header:

- **Barra de búsqueda**: Búsqueda inteligente con autocompletado
- **Mi Cuenta**: Login/Registro y perfil de usuario
- **Carrito**: Resumen de productos seleccionados
- **Wishlist**: Lista de deseos (opcional fase 2)

### 1.4 Footer
Estructura del pie de página:

| Columna | Enlaces |
|---------|---------|
| **Productos** | Todas las Categorías, Nuevos Productos, Ofertas Especiales |
| **Atención al Cliente** | FAQs, Política de Devoluciones, Términos y Condiciones, Política de Privacidad |
| **Sobre Nosotros** | Quiénes Somos, Nuestras Tiendas, Trabaja con Nosotros |
| **Contacto** | Teléfono, Email, WhatsApp, Horarios de Atención |
| **Síguenos** | Facebook, Instagram, YouTube, LinkedIn |

## 2. Sitemap completo

### 2.1 Estructura jerárquica del sitio

```
/                                    (Home)
│
├─ /productos                        (Catálogo General - PLP)
│  │
│  ├─ /productos/herramientas-manuales
│  │  ├─ /productos/herramientas-manuales/llaves-dados
│  │  ├─ /productos/herramientas-manuales/destornilladores
│  │  ├─ /productos/herramientas-manuales/martillos-mazos
│  │  ├─ /productos/herramientas-manuales/alicates-pinzas
│  │  └─ /productos/herramientas-manuales/sierras-manuales
│  │
│  ├─ /productos/herramientas-electricas
│  │  ├─ /productos/herramientas-electricas/taladros
│  │  ├─ /productos/herramientas-electricas/lijadoras
│  │  ├─ /productos/herramientas-electricas/sierras-electricas
│  │  ├─ /productos/herramientas-electricas/amoladoras
│  │  └─ /productos/herramientas-electricas/atornilladores
│  │
│  ├─ /productos/materiales-construccion
│  │  ├─ /productos/materiales-construccion/cemento-mortero
│  │  ├─ /productos/materiales-construccion/ladrillos-bloques
│  │  ├─ /productos/materiales-construccion/arena-grava
│  │  ├─ /productos/materiales-construccion/yeso-masilla
│  │  └─ /productos/materiales-construccion/impermeabilizantes
│  │
│  ├─ /productos/pinturas-acabados
│  │  ├─ /productos/pinturas-acabados/pinturas-interiores
│  │  ├─ /productos/pinturas-acabados/pinturas-exteriores
│  │  ├─ /productos/pinturas-acabados/barnices-lacas
│  │  ├─ /productos/pinturas-acabados/brochas-rodillos
│  │  └─ /productos/pinturas-acabados/accesorios-pintura
│  │
│  ├─ /productos/plomeria
│  │  ├─ /productos/plomeria/tuberias-conexiones
│  │  ├─ /productos/plomeria/llaves-grifos
│  │  ├─ /productos/plomeria/sanitarios
│  │  ├─ /productos/plomeria/tanques-cisternas
│  │  └─ /productos/plomeria/accesorios-bano
│  │
│  ├─ /productos/electricidad
│  │  ├─ /productos/electricidad/cables-conductores
│  │  ├─ /productos/electricidad/interruptores-tomacorrientes
│  │  ├─ /productos/electricidad/tableros-electricos
│  │  ├─ /productos/electricidad/iluminacion
│  │  └─ /productos/electricidad/extensiones-regletas
│  │
│  ├─ /productos/ferreteria-general
│  │  ├─ /productos/ferreteria-general/tornilleria-clavos
│  │  ├─ /productos/ferreteria-general/cerraduras-candados
│  │  ├─ /productos/ferreteria-general/bisagras-herrajes
│  │  ├─ /productos/ferreteria-general/adhesivos-selladores
│  │  └─ /productos/ferreteria-general/cintas-amarres
│  │
│  └─ /productos/jardineria-exterior
│     ├─ /productos/jardineria-exterior/herramientas-jardin
│     ├─ /productos/jardineria-exterior/mangueras-aspersores
│     ├─ /productos/jardineria-exterior/fertilizantes-tierra
│     ├─ /productos/jardineria-exterior/macetas-contenedores
│     └─ /productos/jardineria-exterior/iluminacion-exterior
│
├─ /producto/[slug]                  (PDP - Página de detalle de producto)
│
├─ /marcas                           (Listado de marcas)
│  └─ /marcas/[marca-slug]           (Productos por marca)
│
├─ /ofertas                          (Ofertas y promociones)
│
├─ /carrito                          (Carrito de compras)
│
├─ /checkout                         (Proceso de checkout)
│  ├─ /checkout/informacion          (Datos del cliente)
│  ├─ /checkout/envio                (Método de envío)
│  └─ /checkout/pago                 (Método de pago)
│
├─ /mi-cuenta                        (Área de usuario)
│  ├─ /mi-cuenta/perfil              (Datos personales)
│  ├─ /mi-cuenta/pedidos             (Historial de pedidos)
│  ├─ /mi-cuenta/direcciones         (Direcciones guardadas)
│  └─ /mi-cuenta/wishlist            (Lista de deseos)
│
├─ /nosotros                         (Quiénes somos)
│
├─ /contacto                         (Formulario de contacto)
│
├─ /tiendas                          (Ubicaciones físicas)
│
├─ /faqs                             (Preguntas frecuentes)
│
├─ /politica-privacidad              (Política de privacidad)
│
├─ /terminos-condiciones             (Términos y condiciones)
│
├─ /politica-devoluciones            (Política de devoluciones)
│
├─ /envios                           (Información de envíos)
│
└─ /metodos-pago                     (Métodos de pago aceptados)
```

### 2.2 Tipos de páginas y prioridad

| Tipo de Página | Cantidad Estimada | Prioridad | Fase |
|----------------|-------------------|-----------|------|
| Home | 1 | Alta | MVP |
| PLP (Product Listing Page) | 48 (8 categorías + 40 subcategorías) | Alta | MVP |
| PDP (Product Detail Page) | Variable (~500-5000 productos) | Alta | MVP |
| Páginas Estáticas | ~10 | Media | MVP |
| Páginas de Usuario | ~4 | Media | Post-MVP |
| Checkout | ~3 | Alta | MVP |

## 3. Árbol de categorías y subcategorías

### 3.1 Taxonomía completa de productos

#### Categoría 1: Herramientas Manuales
```yaml
herramientas-manuales:
  nombre: "Herramientas Manuales"
  descripcion: "Herramientas de mano para todo tipo de trabajos"
  icono: "tool-icon"
  orden: 1
  subcategorias:
    - llaves-dados:
        nombre: "Llaves y Dados"
        descripcion: "Llaves fijas, ajustables, dados y accesorios"
        atributos_filtro: ["Tamaño", "Material", "Tipo de llave"]
        orden: 1
    - destornilladores:
        nombre: "Destornilladores"
        descripcion: "Destornilladores planos, phillips, torx y especiales"
        atributos_filtro: ["Tipo de punta", "Tamaño", "Material del mango"]
        orden: 2
    - martillos-mazos:
        nombre: "Martillos y Mazos"
        descripcion: "Martillos de uña, bola, mazos de goma y más"
        atributos_filtro: ["Peso", "Tipo", "Material de cabeza"]
        orden: 3
    - alicates-pinzas:
        nombre: "Alicates y Pinzas"
        descripcion: "Alicates universales, de corte, pinzas de presión"
        atributos_filtro: ["Tipo", "Tamaño", "Aislamiento"]
        orden: 4
    - sierras-manuales:
        nombre: "Sierras Manuales"
        descripcion: "Serruchos, arcos de sierra, seguetas"
        atributos_filtro: ["Tipo", "Longitud de hoja", "Dientes por pulgada"]
        orden: 5
```

#### Categoría 2: Herramientas Eléctricas
```yaml
herramientas-electricas:
  nombre: "Herramientas Eléctricas"
  descripcion: "Herramientas eléctricas para profesionales y hogar"
  icono: "power-tool-icon"
  orden: 2
  subcategorias:
    - taladros:
        nombre: "Taladros"
        descripcion: "Taladros de impacto, percusión y estándar"
        atributos_filtro: ["Potencia (W)", "Voltaje", "Tipo", "Portabrocas"]
        orden: 1
    - lijadoras:
        nombre: "Lijadoras"
        descripcion: "Lijadoras orbitales, de banda y rotativas"
        atributos_filtro: ["Tipo", "Potencia", "Velocidad"]
        orden: 2
    - sierras-electricas:
        nombre: "Sierras Eléctricas"
        descripcion: "Sierras circulares, caladoras, ingletadoras"
        atributos_filtro: ["Tipo", "Potencia", "Profundidad de corte"]
        orden: 3
    - amoladoras:
        nombre: "Amoladoras"
        descripcion: "Amoladoras angulares y rectas"
        atributos_filtro: ["Diámetro de disco", "Potencia", "RPM"]
        orden: 4
    - atornilladores:
        nombre: "Atornilladores"
        descripcion: "Atornilladores eléctricos e inalámbricos"
        atributos_filtro: ["Voltaje", "Par de apriete", "Tipo de batería"]
        orden: 5
```

#### Categoría 3: Materiales de Construcción
```yaml
materiales-construccion:
  nombre: "Materiales de Construcción"
  descripcion: "Materiales básicos para obra y construcción"
  icono: "construction-icon"
  orden: 3
  subcategorias:
    - cemento-mortero:
        nombre: "Cemento y Mortero"
        descripcion: "Cemento portland, mortero premezclado"
        atributos_filtro: ["Tipo", "Peso", "Uso recomendado"]
        orden: 1
    - ladrillos-bloques:
        nombre: "Ladrillos y Bloques"
        descripcion: "Ladrillos, bloques de concreto y arcilla"
        atributos_filtro: ["Material", "Tamaño", "Resistencia"]
        orden: 2
    - arena-grava:
        nombre: "Arena y Grava"
        descripcion: "Agregados para construcción"
        atributos_filtro: ["Tipo", "Granulometría", "Presentación"]
        orden: 3
    - yeso-masilla:
        nombre: "Yeso y Masilla"
        descripcion: "Yesos y masillas para acabados"
        atributos_filtro: ["Tipo", "Uso", "Peso"]
        orden: 4
    - impermeabilizantes:
        nombre: "Impermeabilizantes"
        descripcion: "Productos para impermeabilización"
        atributos_filtro: ["Tipo", "Aplicación", "Rendimiento"]
        orden: 5
```

#### Categoría 4: Pinturas y Acabados
```yaml
pinturas-acabados:
  nombre: "Pinturas y Acabados"
  descripcion: "Pinturas, barnices y accesorios para pintar"
  icono: "paint-icon"
  orden: 4
  subcategorias:
    - pinturas-interiores:
        nombre: "Pinturas Interiores"
        descripcion: "Pinturas para muros y techos interiores"
        atributos_filtro: ["Acabado", "Rendimiento", "Color base"]
        orden: 1
    - pinturas-exteriores:
        nombre: "Pinturas Exteriores"
        descripcion: "Pinturas resistentes para exteriores"
        atributos_filtro: ["Acabado", "Rendimiento", "Resistencia"]
        orden: 2
    - barnices-lacas:
        nombre: "Barnices y Lacas"
        descripcion: "Barnices para madera y lacas"
        atributos_filtro: ["Tipo", "Acabado", "Base"]
        orden: 3
    - brochas-rodillos:
        nombre: "Brochas y Rodillos"
        descripcion: "Herramientas de aplicación de pintura"
        atributos_filtro: ["Tipo", "Tamaño", "Material"]
        orden: 4
    - accesorios-pintura:
        nombre: "Accesorios de Pintura"
        descripcion: "Charolas, extensiones, cintas, cubetas"
        atributos_filtro: ["Tipo", "Material"]
        orden: 5
```

#### Categoría 5: Plomería
```yaml
plomeria:
  nombre: "Plomería"
  descripcion: "Productos para instalaciones hidráulicas"
  icono: "plumbing-icon"
  orden: 5
  subcategorias:
    - tuberias-conexiones:
        nombre: "Tuberías y Conexiones"
        descripcion: "Tuberías PVC, cobre, conexiones"
        atributos_filtro: ["Material", "Diámetro", "Tipo"]
        orden: 1
    - llaves-grifos:
        nombre: "Llaves y Grifos"
        descripcion: "Grifería para baño y cocina"
        atributos_filtro: ["Tipo", "Material", "Acabado"]
        orden: 2
    - sanitarios:
        nombre: "Sanitarios"
        descripcion: "WC, lavabos, mingitorios"
        atributos_filtro: ["Tipo", "Material", "Color"]
        orden: 3
    - tanques-cisternas:
        nombre: "Tanques y Cisternas"
        descripcion: "Almacenamiento de agua"
        atributos_filtro: ["Capacidad", "Material", "Tipo"]
        orden: 4
    - accesorios-bano:
        nombre: "Accesorios de Baño"
        descripcion: "Toalleros, jaboneras, accesorios"
        atributos_filtro: ["Tipo", "Material", "Acabado"]
        orden: 5
```

#### Categoría 6: Electricidad
```yaml
electricidad:
  nombre: "Electricidad"
  descripcion: "Material eléctrico para instalaciones"
  icono: "electric-icon"
  orden: 6
  subcategorias:
    - cables-conductores:
        nombre: "Cables y Conductores"
        descripcion: "Cables eléctricos de diferentes calibres"
        atributos_filtro: ["Calibre", "Tipo", "Longitud"]
        orden: 1
    - interruptores-tomacorrientes:
        nombre: "Interruptores y Tomacorrientes"
        descripcion: "Apagadores, contactos, placas"
        atributos_filtro: ["Tipo", "Voltaje", "Color"]
        orden: 2
    - tableros-electricos:
        nombre: "Tableros Eléctricos"
        descripcion: "Centros de carga, breakers"
        atributos_filtro: ["Capacidad", "Espacios", "Tipo"]
        orden: 3
    - iluminacion:
        nombre: "Iluminación"
        descripcion: "Focos, lámparas, luminarias"
        atributos_filtro: ["Tipo", "Potencia", "Base"]
        orden: 4
    - extensiones-regletas:
        nombre: "Extensiones y Regletas"
        descripcion: "Extensiones eléctricas y multicontactos"
        atributos_filtro: ["Longitud", "Número de salidas", "Voltaje"]
        orden: 5
```

#### Categoría 7: Ferretería General
```yaml
ferreteria-general:
  nombre: "Ferretería General"
  descripcion: "Artículos generales de ferretería"
  icono: "hardware-icon"
  orden: 7
  subcategorias:
    - tornilleria-clavos:
        nombre: "Tornillería y Clavos"
        descripcion: "Tornillos, clavos, tuercas, rondanas"
        atributos_filtro: ["Tipo", "Material", "Medida"]
        orden: 1
    - cerraduras-candados:
        nombre: "Cerraduras y Candados"
        descripcion: "Cerraduras de pomo, cilindro, candados"
        atributos_filtro: ["Tipo", "Material", "Seguridad"]
        orden: 2
    - bisagras-herrajes:
        nombre: "Bisagras y Herrajes"
        descripcion: "Bisagras, herrajes para puertas y muebles"
        atributos_filtro: ["Tipo", "Tamaño", "Material"]
        orden: 3
    - adhesivos-selladores:
        nombre: "Adhesivos y Selladores"
        descripcion: "Pegamentos, silicones, selladores"
        atributos_filtro: ["Tipo", "Uso", "Presentación"]
        orden: 4
    - cintas-amarres:
        nombre: "Cintas y Amarres"
        descripcion: "Cintas adhesivas, de enmascarar, amarres"
        atributos_filtro: ["Tipo", "Ancho", "Material"]
        orden: 5
```

#### Categoría 8: Jardinería y Exterior
```yaml
jardineria-exterior:
  nombre: "Jardinería y Exterior"
  descripcion: "Herramientas y productos para jardín"
  icono: "garden-icon"
  orden: 8
  subcategorias:
    - herramientas-jardin:
        nombre: "Herramientas de Jardín"
        descripcion: "Palas, rastrillos, tijeras de podar"
        atributos_filtro: ["Tipo", "Material", "Uso"]
        orden: 1
    - mangueras-aspersores:
        nombre: "Mangueras y Aspersores"
        descripcion: "Mangueras de riego, aspersores, accesorios"
        atributos_filtro: ["Tipo", "Longitud", "Material"]
        orden: 2
    - fertilizantes-tierra:
        nombre: "Fertilizantes y Tierra"
        descripcion: "Abonos, tierra, sustratos"
        atributos_filtro: ["Tipo", "Uso", "Peso"]
        orden: 3
    - macetas-contenedores:
        nombre: "Macetas y Contenedores"
        descripcion: "Macetas, materos, jardineras"
        atributos_filtro: ["Material", "Tamaño", "Forma"]
        orden: 4
    - iluminacion-exterior:
        nombre: "Iluminación Exterior"
        descripcion: "Luminarias para jardín y exterior"
        atributos_filtro: ["Tipo", "Potencia", "Protección IP"]
        orden: 5
```

### 3.2 Metadatos de categorías

Cada categoría y subcategoría incluirá:

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| **slug** | URL amigable | `herramientas-manuales` |
| **nombre** | Título visible | `Herramientas Manuales` |
| **descripcion** | Texto descriptivo corto | `Herramientas de mano para todo tipo de trabajos` |
| **descripcion_larga** | Texto SEO (opcional) | Párrafo extendido con keywords |
| **meta_title** | Título SEO | `Herramientas Manuales - Ferretería` |
| **meta_description** | Descripción SEO | `Amplio catálogo de herramientas manuales...` |
| **imagen_destacada** | Banner de categoría | URL de imagen |
| **icono** | Icono para menú | Código de icono o SVG |
| **orden** | Orden de visualización | 1, 2, 3... |
| **activo** | Estado de publicación | true/false |
| **fecha_creacion** | Timestamp de creación | ISO 8601 |
| **fecha_modificacion** | Última actualización | ISO 8601 |

### 3.3 Filtros y atributos

#### Filtros globales (aplicables a todas las categorías):
- **Marca**: Listado de fabricantes
- **Rango de precio**: Slider con min/max
- **Disponibilidad**: En stock, Agotado, Preventa
- **Calificación**: Estrellas (1-5)
- **Descuento**: Con oferta, Sin oferta

#### Filtros específicos por categoría:
Cada categoría tiene atributos particulares según el tipo de producto (ver definiciones en 3.1)

### 3.4 Breadcrumbs (Migas de pan)

Estructura de navegación por niveles:

```
Home > Productos > [Categoría] > [Subcategoría] > [Producto]

Ejemplos:
Home > Productos > Herramientas Eléctricas > Taladros
Home > Productos > Pinturas y Acabados > Pinturas Interiores > Pintura Vinílica Blanca 19L
Home > Marcas > DeWalt
Home > Ofertas
```

## 4. Patrones de navegación

### 4.1 Flujos principales de usuario

#### Flujo 1: Búsqueda de producto específico
```
Home → Barra de búsqueda → Resultados → PDP → Agregar al carrito → Checkout
```

#### Flujo 2: Exploración por categoría
```
Home → Menú Productos → Categoría → Subcategoría → PDP → Agregar al carrito
```

#### Flujo 3: Búsqueda por marca
```
Home → Marcas → Marca específica → Listado de productos → PDP
```

#### Flujo 4: Navegación por ofertas
```
Home → Ofertas → Productos en oferta → PDP → Agregar al carrito
```

### 4.2 Elementos de navegación contextual

- **Productos relacionados**: En PDP, mostrar productos similares
- **Productos vistos recientemente**: En sidebar o footer
- **Productos más vendidos**: Por categoría
- **Sugerencias basadas en navegación**: Historial de categorías visitadas

### 4.3 Navegación móvil

- **Menú hamburguesa**: Acceso a navegación principal
- **Sticky header**: Header fijo al hacer scroll
- **Barra de búsqueda prominente**: Fácil acceso
- **Bottom navigation bar** (opcional): Accesos rápidos a Home, Categorías, Carrito, Cuenta

## 5. Consideraciones de implementación en Odoo

### 5.1 Módulos de Odoo requeridos
- `website`: Base del sitio web
- `website_sale`: E-commerce
- `product`: Gestión de productos
- `product_public_category`: Categorías públicas
- `website_sale_management`: Gestión avanzada

### 5.2 Estructura de datos en Odoo

#### Modelo: product.public.category
Campos principales del modelo estándar de Odoo:
```python
# Campos básicos
name = fields.Char('Name', required=True, translate=True)
parent_id = fields.Many2one('product.public.category', string='Parent Category', index=True)
sequence = fields.Integer('Sequence', default=10)

# Campos para sitio web
website_description = fields.Html('Category Description', sanitize_attributes=False, translate=True)
image = fields.Binary('Image', attachment=True)

# Campos adicionales estándar
child_id = fields.One2many('product.public.category', 'parent_id', string='Children Categories')
parents_and_self = fields.Many2many('product.public.category', compute='_compute_parents_and_self')
```

#### Configuración de menús
Usar el editor de sitio web de Odoo para:
- Crear menú principal con website.menu
- Configurar mega menú con snippet personalizado
- Establecer URLs amigables con website.page

### 5.3 SEO y URLs

#### Patrón de URLs:
- Categorías: `/shop/category/[slug]`
- Productos: `/shop/product/[slug]`
- Marcas: `/shop/brand/[slug]` (requiere módulo personalizado)

#### Configuración SEO por página:
- Meta title personalizado
- Meta description optimizada
- Canonical URLs
- Schema.org markup (Product, BreadcrumbList)

## 6. Próximos pasos

1. **Validar taxonomía**: Revisar con stakeholders las categorías propuestas
2. **Crear estructura en Odoo**: Implementar categorías y subcategorías
3. **Diseñar mega menú**: Crear snippet personalizado para Odoo
4. **Configurar URLs**: Establecer slugs y redirecciones
5. **Implementar breadcrumbs**: Template personalizado
6. **Testing de navegación**: Validar flujos en diferentes dispositivos
