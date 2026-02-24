# Página Web Odoo Ferretería

Proyecto para construir y operar una web de ferretería en Odoo.

## Objetivo
Implementar un sitio transaccional y escalable en Odoo, con catálogo, checkout, SEO base, integraciones y operación post-lanzamiento.

## Enlaces
- Repositorio: https://github.com/ConceptualDynamic/pagina-web-odoo-ferreteria
- Planner (Plan): Software Development

## Estructura documental
- `docs/01-alcance-kpis.md`
- `docs/02-roadmap-fases.md`
- `docs/03-arquitectura-informacion.md`
- `docs/04-catalogo-y-datos.md`
- `docs/05-diseno-ux-ui.md`
- `docs/06-pagos-envios-impuestos.md`
- `docs/07-seo-y-contenido.md`
- `docs/08-integraciones.md`
- `docs/09-qa.md`
- `docs/10-go-live-y-monitoreo.md`
- `docs/11-matriz-github-planner.md`

## 🚀 Go-Live (Fase 9)

### Documentos de Go-Live
- **[Go-Live Checklist](docs/GO-LIVE-CHECKLIST.md)** - Lista completa de validaciones pre-lanzamiento
- **[Monitoring Dashboard 72h](docs/MONITORING-DASHBOARD-72H.md)** - Dashboard para monitoreo post-lanzamiento
- **[Guía completa](docs/10-go-live-y-monitoreo.md)** - Procedimientos detallados, plan de rollback y reporte de estabilización

### Script de Validación
```bash
# Ejecutar validación automática antes del go-live
./scripts/validate-pre-launch.sh https://tu-sitio-odoo.com
```

### Fases del Go-Live
1. **Pre-lanzamiento (T-24h)**: Ejecutar checklist completo y backup
2. **Lanzamiento (T=0)**: Despliegue controlado con validación inmediata
3. **Monitoreo 72h**: Seguimiento intensivo con dashboard de métricas
4. **Estabilización**: Reporte final y aprobación para operación continua

## Convención de seguimiento (Opción 3)
GitHub Project = hub de producto/roadmap técnico.
Planner = ejecución operativa diaria.
