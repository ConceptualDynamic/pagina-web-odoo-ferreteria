# Quick Start - Fase 4 Implementación
## Guía Rápida para Desarrolladores

---

## Resumen

Esta fase implementa las páginas principales del sitio web de ferretería:
- **Home**: Página principal optimizada para conversión
- **Nosotros**: Página institucional sobre la empresa
- **Contacto**: Formulario de contacto + información
- **FAQs**: Preguntas frecuentes por categorías
- **Políticas**: Términos, privacidad, devoluciones, envíos

---

## Pasos de Implementación

### 1. Pre-requisitos

```bash
# Verificar módulos Odoo instalados
# Acceder a Odoo > Apps
- website
- website_sale
- website_crm
- website_form
```

### 2. Crear Módulo Custom

```bash
# Estructura mínima
ferreteria_web/
├── __init__.py
├── __manifest__.py
├── views/
│   ├── page_home.xml
│   ├── page_nosotros.xml
│   ├── page_contacto.xml
│   ├── page_faqs.xml
│   └── page_politicas.xml
├── data/
│   ├── website_pages.xml
│   └── website_menu.xml
└── static/
    └── src/
        ├── css/custom.css
        └── js/custom.js
```

### 3. Implementar Páginas

**Opción A: Desde código (recomendado para desarrollo inicial)**
1. Copiar ejemplos de `docs/04-fase4-guia-implementacion-odoo.md`
2. Adaptar contenido con datos del cliente de `docs/04-fase4-plantilla-contenido-cliente.md`
3. Crear archivos XML en `views/`
4. Registrar páginas en `data/website_pages.xml`

**Opción B: Desde interfaz Odoo (recomendado para ajustes)**
1. Website > Site > Pages > New Page
2. Usar Website Builder (drag & drop)
3. Crear estructura con snippets
4. Guardar y publicar

### 4. Configurar Menú

```xml
<!-- data/website_menu.xml -->
<record id="menu_home" model="website.menu">
    <field name="name">Inicio</field>
    <field name="url">/</field>
    <field name="sequence">10</field>
</record>
<!-- Repetir para otras páginas -->
```

### 5. Estilos y Assets

```xml
<!-- views/assets.xml -->
<template id="assets_frontend" inherit_id="website.assets_frontend">
    <xpath expr="." position="inside">
        <link rel="stylesheet" href="/ferreteria_web/static/src/css/custom.css"/>
    </xpath>
</template>
```

### 6. Instalar Módulo

```bash
./odoo-bin -c odoo.conf -d database_name -i ferreteria_web
```

---

## Checklist de Implementación

### Home
- [ ] Hero section con banners rotativos
- [ ] Grid de categorías (6-8)
- [ ] Productos destacados (integrados con catálogo)
- [ ] Sección de beneficios (4 columnas)
- [ ] Marcas destacadas (logos)
- [ ] Newsletter (formulario)
- [ ] Responsive en mobile/tablet

### Nosotros
- [ ] Hero con imagen
- [ ] Historia (texto + imagen)
- [ ] Misión, Visión, Valores (3 cards)
- [ ] Equipo (opcional)
- [ ] CTAs al final

### Contacto
- [ ] Formulario funcional conectado a CRM
- [ ] Validaciones de campos
- [ ] Información de contacto completa
- [ ] Mapa de Google Maps
- [ ] Página de agradecimiento
- [ ] Email de confirmación (opcional)

### FAQs
- [ ] Organizadas por categorías (5 mínimo)
- [ ] Acordeón funcional (collapse/expand)
- [ ] Mínimo 15-20 preguntas
- [ ] CTA a contacto al final

### Políticas
- [ ] Navegación lateral/tabs
- [ ] Términos y Condiciones
- [ ] Política de Privacidad
- [ ] Política de Devoluciones
- [ ] Política de Envíos
- [ ] Fechas de actualización visibles

---

## Testing

### Funcional
```bash
# Navegación
✓ Menú funciona en todos los links
✓ Todas las páginas cargan sin errores

# Formulario de contacto
✓ Validaciones funcionan
✓ Se crea lead en CRM al enviar
✓ Redirección a página de gracias
✓ Email de confirmación enviado (opcional)
```

### Responsive
```bash
✓ Mobile (< 768px): Layout 1 columna
✓ Tablet (768-1024px): Layout adaptado
✓ Desktop (> 1024px): Layout completo
```

### Performance
```bash
# Usar Google PageSpeed Insights
✓ LCP < 2.5s
✓ FID < 100ms
✓ CLS < 0.1
```

### Cross-browser
```bash
✓ Chrome (últimas 2 versiones)
✓ Firefox (últimas 2 versiones)
✓ Safari (últimas 2 versiones)
✓ Edge (última versión)
```

---

## Comandos Útiles Odoo

```bash
# Instalar módulo
./odoo-bin -c odoo.conf -d db_name -i ferreteria_web

# Actualizar módulo
./odoo-bin -c odoo.conf -d db_name -u ferreteria_web

# Modo debug
./odoo-bin -c odoo.conf --dev=all

# Regenerar assets (si CSS/JS no actualiza)
# Website > Configuration > Settings > Regenerate Assets Bundles

# Ver logs
tail -f /var/log/odoo/odoo.log
```

---

## Troubleshooting Común

### Problema: Página no se muestra
```bash
# Solución 1: Verificar que esté publicada
Website > Site > Pages > [Tu página] > ✓ Published

# Solución 2: Actualizar módulo
./odoo-bin -u ferreteria_web

# Solución 3: Limpiar caché navegador
Ctrl + Shift + Delete (Chrome/Firefox)
```

### Problema: Estilos no se aplican
```bash
# Solución: Regenerar assets
Website > Settings > Regenerate Assets
# O en modo desarrollador: Assets > Debug > Regenerate
```

### Problema: Formulario no envía
```bash
# Verificar:
1. CSRF token presente
2. website_crm instalado
3. Action correcto en form
4. Campos con name correcto
5. Ver logs de Odoo para errores
```

### Problema: Imágenes no cargan
```bash
# Verificar:
1. Ruta correcta: /module_name/static/src/img/file.jpg
2. Archivo existe en filestore
3. Permisos de lectura
4. Usar Media Library para gestionar
```

---

## Assets Necesarios del Cliente

**Antes de implementar, solicitar:**

1. **Textos:**
   - [ ] Plantilla de contenido completada
   - [ ] Políticas legales revisadas

2. **Imágenes:**
   - [ ] Hero banners (3 mínimo, 1920x800px)
   - [ ] Categorías (6-8, 600x600px)
   - [ ] Nosotros (2-3 fotos institucionales)
   - [ ] Logo principal (SVG o PNG HD)
   - [ ] Logos de marcas (6-12 logos)

3. **Información:**
   - [ ] Datos de contacto verificados
   - [ ] Horarios actualizados
   - [ ] Coordenadas GPS para mapa
   - [ ] FAQs específicas del negocio

---

## Documentación de Referencia

📄 Documentos principales:
- `docs/04-fase4-diseno-home-institucionales.md` - Especificaciones completas
- `docs/04-fase4-guia-implementacion-odoo.md` - Guía técnica detallada
- `docs/04-fase4-especificaciones-diseno-visual.md` - Sistema de diseño
- `docs/04-fase4-plantilla-contenido-cliente.md` - Template para cliente

🔗 Enlaces útiles:
- [Odoo Website Docs](https://www.odoo.com/documentation/16.0/applications/websites.html)
- [Bootstrap 4 Docs](https://getbootstrap.com/docs/4.6/)
- [Font Awesome Icons](https://fontawesome.com/v5/search)

---

## Entregables de Fase 4

Al completar esta fase, debes entregar:

- [x] Todas las páginas implementadas en staging
- [x] Formulario de contacto funcional
- [x] Menú de navegación configurado
- [x] Diseño responsive verificado
- [x] Assets optimizados (imágenes < 200KB)
- [ ] Screenshots de cada página (desktop + mobile)
- [ ] Manual de edición para cliente
- [ ] QA completado (checklist arriba)

---

## Próximos Pasos (Fase 5)

Después de completar Fase 4:
1. Implementar PLP/PDP (listados y fichas de producto)
2. Configurar filtros y búsqueda de productos
3. Optimizar experiencia de navegación de catálogo

---

**Última actualización:** 2026-02-24  
**Contacto para soporte técnico:** _[Especificar]_
