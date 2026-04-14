# Ferretería Website - Módulo Odoo

Módulo personalizado de Odoo para implementar una tienda online de ferretería con catálogo técnico, checkout optimizado e integraciones de marketing.

## 📋 Requisitos

- Odoo 17.0 (Community o Enterprise)
- Módulos de Odoo requeridos:
  - `website`
  - `website_sale`
  - `website_sale_stock`
  - `sale_management`
  - `stock`
  - `contacts`
  - `crm`
  - `website_crm`

## 🚀 Instalación

1. Copiar la carpeta `ferreteria_website` al directorio de addons de Odoo:
   ```bash
   cp -r addons/ferreteria_website /path/to/odoo/addons/
   ```

2. Actualizar la lista de módulos en Odoo:
   ```bash
   ./odoo-bin -u base -d your_database
   ```

3. Ir a Aplicaciones → Buscar "Ferretería" → Instalar

## 📦 Características

### Gestión de Productos
- **Campos extendidos**: Especificaciones técnicas, marca, modelo, garantía
- **Descripciones cortas**: Optimizadas para SEO (máx. 160 caracteres)
- **Control de calidad**: Validación de datos completos antes de publicar
- **Productos compatibles**: Relación many2many para cross-sell

### Marcas
- Modelo dedicado para gestión de marcas
- Logo, descripción y sitio web
- Marcas destacadas para mostrar en homepage
- Contador de productos por marca

### Categorías Mejoradas
- Campos SEO (título, meta descripción)
- Iconos FontAwesome
- Control de visualización en menú
- Orden de visualización personalizable

### Diseño Web
- **Templates personalizados**: Home, PLP, PDP, checkout, páginas institucionales
- **Snippets**: Categorías destacadas, marcas, beneficios, banner de promoción
- **Responsive**: Diseño mobile-first
- **WhatsApp**: Botón flotante configurable

### SEO y Analytics
- Integración nativa con Google Analytics 4
- Google Tag Manager
- Datos estructurados JSON-LD para productos
- Meta tags optimizados
- Eventos de eCommerce tracking

### Checkout
- Indicador de envío gratis
- Opción de retiro en tienda
- Pasos de progreso visual
- Mensajes de confirmación mejorados

## ⚙️ Configuración

### Configuración del Website

Ir a **Sitio Web → Configuración → Ajustes**:

1. **WhatsApp**
   - Número de WhatsApp (con código de país)
   - Mensaje predeterminado
   - Mostrar/ocultar botón

2. **Información de Tienda**
   - Teléfono, email, dirección
   - Horario de atención

3. **Envíos**
   - Umbral de envío gratis
   - Activar retiro en tienda

4. **Analytics**
   - GA4 Measurement ID
   - GTM Container ID

5. **Colores**
   - Color primario
   - Color secundario
   - Color de acento

### Configuración de Categorías

Las categorías se crean automáticamente al instalar el módulo:
- Herramientas Manuales
- Herramientas Eléctricas
- Tornillería y Fijaciones
- Pintura y Accesorios
- Plomería
- Electricidad
- Seguridad Industrial
- Jardinería

Para personalizar, ir a **Sitio Web → eCommerce → Categorías de Productos**.

### Configuración de Marcas

Ir a **Ventas → Catálogo → Marcas** para:
- Crear/editar marcas
- Subir logos
- Marcar como destacadas

### Configuración de Atributos

Los atributos de filtrado se crean automáticamente:
- Marca
- Potencia
- Voltaje
- Material
- Medida
- Color
- Uso Recomendado

Para agregar valores, ir a **Sitio Web → eCommerce → Atributos de Productos**.

## 📁 Estructura del Módulo

```
ferreteria_website/
├── __init__.py
├── __manifest__.py
├── README.md
├── data/
│   ├── product_attribute_data.xml
│   ├── product_category_data.xml
│   └── website_menu_data.xml
├── models/
│   ├── __init__.py
│   ├── product_category.py
│   ├── product_template.py
│   └── website.py
├── security/
│   ├── ferreteria_security.xml
│   └── ir.model.access.csv
├── static/
│   ├── description/
│   └── src/
│       ├── css/
│       │   └── ferreteria.css
│       ├── img/
│       └── js/
│           └── ferreteria.js
├── templates/
│   ├── checkout_templates.xml
│   ├── page_templates.xml
│   ├── product_templates.xml
│   └── website_templates.xml
└── views/
    ├── product_template_views.xml
    └── website_snippets.xml
```

## 🔧 Personalización

### Colores

Los colores se pueden personalizar mediante CSS variables:

```css
:root {
    --ferreteria-primary: #FF6B00;
    --ferreteria-secondary: #1E3A5F;
    --ferreteria-accent: #28A745;
}
```

O desde la configuración del website (campos `primary_color`, `secondary_color`, `accent_color`).

### Templates

Para extender templates, crear un nuevo módulo que herede de los templates existentes:

```xml
<template id="my_extension" inherit_id="ferreteria_website.product_ferreteria">
    <xpath expr="//div[@id='product_details']" position="inside">
        <!-- Contenido adicional -->
    </xpath>
</template>
```

## 📊 Eventos de Analytics

El módulo trackea automáticamente los siguientes eventos de GA4:

| Evento | Descripción |
|--------|-------------|
| `page_view` | Vista de página |
| `view_item` | Vista de producto |
| `add_to_cart` | Agregar al carrito |
| `begin_checkout` | Iniciar checkout |
| `purchase` | Compra completada |
| `contact` | Click en WhatsApp |
| `filter_applied` | Uso de filtros |

## 🛡️ Seguridad

### Grupos de Usuarios

- **Ferretería: Gestor de Catálogo**: Puede gestionar productos, categorías y marcas
- **Ferretería: Administrador**: Acceso completo a configuración

### Permisos de Marcas

- Usuarios públicos: Solo lectura de marcas activas
- Usuarios del portal: Solo lectura de marcas activas
- Usuarios internos: Solo lectura
- Gestores de catálogo: CRUD completo

## 🐛 Troubleshooting

### Error al instalar
- Verificar que todos los módulos dependientes estén instalados
- Ejecutar actualización de módulos: `./odoo-bin -u all -d database`

### Imágenes no cargan
- Verificar permisos de la carpeta `static`
- Limpiar caché del navegador

### Analytics no trackea
- Verificar que GA4 Measurement ID esté configurado
- Revisar consola del navegador por errores de JavaScript

## 📝 Changelog

### v17.0.1.0.0
- Versión inicial
- Modelos extendidos de producto y categoría
- Sistema de marcas
- Templates de producto, checkout y páginas institucionales
- Integración con GA4 y GTM
- Snippets para Website Builder
- Botón flotante de WhatsApp

## 📄 Licencia

LGPL-3.0

## 👥 Autores

- Conceptual Dynamic
- https://github.com/ConceptualDynamic/pagina-web-odoo-ferreteria
