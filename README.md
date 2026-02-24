# Página Web Odoo Ferretería

Proyecto para construir y operar una web de ferretería en Odoo.

## Objetivo
Implementar un sitio transaccional y escalable en Odoo, con catálogo, checkout, SEO base, integraciones y operación post-lanzamiento.

## Enlaces
- Repositorio: https://github.com/ConceptualDynamic/pagina-web-odoo-ferreteria
- Planner (Plan): Software Development

## Estructura documental
- `docs/01-alcance-kpis.md` - Alcance del proyecto y KPIs
- `docs/02-roadmap-fases.md` - Roadmap por fases del proyecto
- `docs/03-arquitectura-informacion.md` - Arquitectura de información y navegación
- `docs/04-catalogo-y-datos.md` - Catálogo y gestión de datos de productos
- `docs/05-diseno-ux-ui.md` - Diseño UX/UI y experiencia de usuario
- `docs/06-pagos-envios-impuestos.md` - Configuración de pagos, envíos e impuestos
- `docs/07-seo-y-contenido.md` - SEO y estrategia de contenido
- `docs/08-integraciones.md` - Integraciones con sistemas externos
- `docs/09-qa.md` - Quality Assurance y testing
- `docs/10-go-live-y-monitoreo.md` - Go-live y monitoreo post-lanzamiento
- `docs/11-matriz-github-planner.md` - Vínculo GitHub Project ↔ Planner

### Fase 4: Diseño de Tienda (PLP/PDP)
- `docs/fase-4-resumen-ejecutivo.md` - **Resumen ejecutivo de la Fase 4**
- `docs/fase-4-plp-design.md` - Especificaciones detalladas de Product Listing Page
- `docs/fase-4-pdp-design.md` - Especificaciones detalladas de Product Detail Page
- `docs/fase-4-implementation-guide.md` - Guía técnica de implementación en Odoo

## Convención de seguimiento (Opción 3)
GitHub Project = hub de producto/roadmap técnico.
Planner = ejecución operativa diaria.

## Estado del Proyecto

### Fases Completadas
- ✅ Fase 0: Descubrimiento y alcance
- ⏳ Fase 1: Setup técnico Odoo
- ⏳ Fase 2: Arquitectura y navegación
- ⏳ Fase 3: Catálogo y carga
- 🚧 Fase 4: Diseño páginas clave (En progreso)
  - ✅ Especificaciones PLP/PDP completadas
  - ⏳ Implementación pendiente

### Issues Activos
Ver [GitHub Issues](https://github.com/ConceptualDynamic/pagina-web-odoo-ferreteria/issues) para estado actualizado.

## Inicio Rápido

### Para Desarrolladores

1. **Leer documentación base**:
   - Comenzar con `docs/02-roadmap-fases.md` para entender el alcance
   - Revisar `docs/05-diseno-ux-ui.md` para principios de diseño

2. **Implementar Fase 4 (PLP/PDP)**:
   - Leer `docs/fase-4-resumen-ejecutivo.md` para overview
   - Revisar diseños en `docs/fase-4-plp-design.md` y `docs/fase-4-pdp-design.md`
   - Seguir `docs/fase-4-implementation-guide.md` para implementación técnica

3. **Configurar entorno Odoo**:
   ```bash
   # Instalar dependencias según docs/02-roadmap-fases.md
   # Activar módulos necesarios (ver fase-4-implementation-guide.md)
   ```

### Para Project Managers

1. **Seguimiento de progreso**:
   - GitHub Issues para estado técnico
   - Planner para tareas operativas diarias
   - Ver `docs/11-matriz-github-planner.md` para convenciones

2. **Criterios de aceptación**:
   - Ver sección "Criterios de Aceptación" en cada documento de fase
   - PR pequeños y enfocados
   - Tests/lint pasando
   - Documentación actualizada

## Contribuir

1. Cada Issue debe tener:
   - Título con formato `[Fase X] Descripción`
   - Link a tarea de Planner
   - Criterios de aceptación claros

2. Cada PR debe:
   - Ser pequeño y enfocado
   - Pasar tests y linting
   - Actualizar documentación relevante
   - Vincular al Issue correspondiente

## Contacto

Para dudas o soporte:
- Crear un Issue en GitHub
- Revisar documentación en `/docs`
- Contactar al equipo via Planner
