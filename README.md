# Página Web Odoo Ferretería

Proyecto para construir y operar una web de ferretería en Odoo.

## Objetivo
Implementar un sitio transaccional y escalable en Odoo, con catálogo, checkout, SEO base, integraciones y operación post-lanzamiento.

## 🚀 Quick Start

### Requisitos
- Odoo 17.0 (Community o Enterprise)
- Python 3.10+
- PostgreSQL 14+

### Instalación del Módulo

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/ConceptualDynamic/pagina-web-odoo-ferreteria.git
   ```

2. Copiar el módulo a los addons de Odoo:
   ```bash
   cp -r addons/ferreteria_website /path/to/odoo/addons/
   ```

3. Actualizar la lista de módulos e instalar:
   ```bash
   ./odoo-bin -u base -d your_database
   ```

4. En Odoo, ir a **Aplicaciones** → Buscar "Ferretería" → **Instalar**

## 📁 Estructura del Proyecto

```
pagina-web-odoo-ferreteria/
├── README.md
├── addons/
│   └── ferreteria_website/     # Módulo principal de Odoo
│       ├── __manifest__.py
│       ├── models/             # Modelos extendidos
│       ├── views/              # Vistas de backend
│       ├── templates/          # Templates de website
│       ├── static/             # CSS, JS, imágenes
│       ├── data/               # Datos iniciales
│       └── security/           # Reglas de seguridad
├── docs/                       # Documentación del proyecto
│   ├── 01-alcance-kpis.md
│   ├── 02-roadmap-fases.md
│   └── ...
└── .github/                    # Workflows y templates
```

## ✨ Características

### Gestión de Productos
- Campos técnicos extendidos (especificaciones, garantía, documentación)
- Sistema de marcas con logos
- Control de calidad de datos del catálogo
- Productos compatibles para cross-sell

### Experiencia de Compra
- Catálogo con filtros avanzados (marca, potencia, voltaje, uso)
- Fichas de producto optimizadas con SEO
- Checkout mejorado con indicador de envío gratis
- Opción de retiro en tienda

### Marketing y Analytics
- Integración nativa con Google Analytics 4
- Google Tag Manager
- Datos estructurados JSON-LD
- Botón flotante de WhatsApp

### Páginas Institucionales
- Nosotros
- Contacto (con formulario y WhatsApp)
- FAQ
- Políticas (envíos, devoluciones, privacidad)

## 📚 Documentación

| Documento | Descripción |
|-----------|-------------|
| [01-alcance-kpis.md](docs/01-alcance-kpis.md) | Alcance del proyecto y KPIs |
| [02-roadmap-fases.md](docs/02-roadmap-fases.md) | Roadmap por fases |
| [03-arquitectura-informacion.md](docs/03-arquitectura-informacion.md) | Arquitectura de información |
| [04-catalogo-y-datos.md](docs/04-catalogo-y-datos.md) | Gestión del catálogo |
| [05-diseno-ux-ui.md](docs/05-diseno-ux-ui.md) | Diseño UX/UI |
| [06-pagos-envios-impuestos.md](docs/06-pagos-envios-impuestos.md) | Pagos, envíos e impuestos |
| [07-seo-y-contenido.md](docs/07-seo-y-contenido.md) | SEO y contenido |
| [08-integraciones.md](docs/08-integraciones.md) | Integraciones |
| [09-qa.md](docs/09-qa.md) | Plan de QA |
| [10-go-live-y-monitoreo.md](docs/10-go-live-y-monitoreo.md) | Go-live y monitoreo |
| [11-matriz-github-planner.md](docs/11-matriz-github-planner.md) | Matriz GitHub-Planner |

Para documentación detallada del módulo, ver [addons/ferreteria_website/README.md](addons/ferreteria_website/README.md).

## 🔧 Configuración

Después de instalar, configurar en **Sitio Web → Configuración → Ajustes**:

1. **WhatsApp**: Número y mensaje predeterminado
2. **Información de tienda**: Dirección, teléfono, horario
3. **Envíos**: Umbral de envío gratis, retiro en tienda
4. **Analytics**: GA4 Measurement ID, GTM Container ID
5. **Colores**: Paleta de colores de marca

## 📊 Roadmap

- [x] **Fase 0**: Descubrimiento y alcance
- [x] **Fase 1**: Setup técnico (módulo base)
- [ ] **Fase 2**: Arquitectura de información y navegación
- [ ] **Fase 3**: Catálogo y carga de datos
- [ ] **Fase 4**: Diseño UX/UI
- [ ] **Fase 5**: Checkout, pagos, envíos e impuestos
- [ ] **Fase 6**: SEO y contenido
- [ ] **Fase 7**: Integraciones
- [ ] **Fase 8**: QA integral
- [ ] **Fase 9**: Go-live y monitoreo

## 🔗 Enlaces

- Repositorio: https://github.com/ConceptualDynamic/pagina-web-odoo-ferreteria
- Planner (Plan): Software Development

## 📝 Convención de seguimiento

- **GitHub Project** = hub de producto/roadmap técnico
- **Planner** = ejecución operativa diaria

## 📄 Licencia

LGPL-3.0
