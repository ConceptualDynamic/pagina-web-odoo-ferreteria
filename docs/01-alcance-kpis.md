# Alcance y KPIs

## 1) Objetivo del proyecto
Construir una tienda online de ferretería en Odoo que permita:
- Venta transaccional B2C y atención B2B ligera (cotización/contacto).
- Descubrimiento rápido de productos técnicos mediante filtros.
- Operación estable desde el día 1 (inventario, pagos, envíos, analítica).

## 2) Alcance funcional del MVP
### Incluye
- Home comercial orientada a conversión.
- Catálogo (categorías + subcategorías + marcas).
- Listado de productos (PLP) con filtros y ordenamiento.
- Detalle de producto (PDP) con especificaciones técnicas.
- Carrito y checkout en Odoo Website/eCommerce.
- Páginas institucionales: Nosotros, Contacto, FAQs, Políticas.
- SEO técnico base (metadatos, sitemap, robots, URLs limpias).
- Integración analítica inicial (GA4 + eventos críticos).

### No incluye (fase posterior)
- Marketplace multi-vendedor.
- Reglas complejas B2B por contrato.
- Motor de recomendaciones avanzado con IA.
- Integración con ERP externo distinto a Odoo.

## 3) Alcance técnico
- Plataforma: Odoo (website + eCommerce).
- Entornos: desarrollo, staging, producción.
- Gobierno de cambios: GitHub (issues/PR) + Planner (ejecución diaria).
- Seguridad mínima: HTTPS, roles, backups y auditoría básica.

## 4) KPIs de negocio (90 días post go-live)
- Tasa de conversión eCommerce: objetivo inicial 0.8%–1.8% (ajustable por tráfico real).
- Ticket promedio (AOV): definir baseline en semana 2 y crecer +10% al día 90.
- Ingresos por canal web: baseline en primer mes; meta de crecimiento mensual.
- Tasa de abandono de checkout: mantener < 70% en etapa inicial (con mejora continua).
- Leads B2B desde formularios/WhatsApp: línea base + tendencia semanal.

## 5) KPIs de operación digital
- Velocidad: LCP < 3.0s en móvil (páginas clave).
- Estabilidad: error rate checkout < 2%.
- Disponibilidad: > 99.5% mensual.
- Calidad de catálogo: > 95% SKUs con ficha completa.
- Tiempo de respuesta comercial: < 2h en horario operativo.

## 6) KPI owners (responsables sugeridos)
- Conversión/AOV: Product Owner + Marketing.
- Rendimiento técnico: Líder técnico Odoo.
- Calidad de datos: Responsable catálogo.
- Leads y atención: Comercial/Customer Success.

## 7) Criterios de aceptación del MVP
- Flujo completo “buscar → comprar → pagar → confirmar” funcional en staging y producción.
- Catálogo mínimo publicado con datos consistentes.
- Eventos analíticos críticos capturando correctamente.
- Checklists de QA y Go-live firmados por responsables.

## 8) Riesgos clave y mitigación
- Datos incompletos de productos → plantilla obligatoria + validación previa a publicación.
- Fricción en checkout → pruebas E2E por dispositivo y método de pago.
- Lentitud por imágenes pesadas → compresión, formatos optimizados y lazy loading.
- Desalineación entre negocio y técnico → ritual semanal de priorización.
