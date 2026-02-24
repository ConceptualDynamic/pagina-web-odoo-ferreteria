# Go-live y monitoreo
Checklist pre-release, despliegue controlado y monitoreo 72h con reporte final de estabilización.

## 1. Checklist pre-lanzamiento

### 1.1 Infraestructura y Seguridad
- [ ] Backup completo de la base de datos y archivos
- [ ] Certificado SSL activo y válido
- [ ] Firewall y reglas de seguridad configuradas
- [ ] Variables de entorno de producción verificadas
- [ ] Dominio y DNS correctamente configurados
- [ ] CDN configurado (si aplica)

### 1.2 Funcionalidad Core
- [ ] Catálogo de productos visible y funcionando
- [ ] Sistema de búsqueda operativo
- [ ] Carrito de compras funcionando
- [ ] Proceso de checkout completo
- [ ] Pasarela de pago funcionando (prueba real)
- [ ] Emails transaccionales enviándose correctamente
- [ ] Formularios de contacto operativos

### 1.3 Integraciones
- [ ] Google Analytics 4 rastreando correctamente
- [ ] CRM recibiendo leads
- [ ] WhatsApp/Chat conectado y funcionando
- [ ] Integración con sistema de inventario (si aplica)
- [ ] Webhooks configurados y probados

### 1.4 SEO y Contenido
- [ ] Meta tags en todas las páginas clave
- [ ] Sitemap.xml generado y enviado
- [ ] Robots.txt configurado
- [ ] URLs canónicas establecidas
- [ ] Imágenes con alt text
- [ ] Políticas legales publicadas (privacidad, términos, envíos, devoluciones)

### 1.5 Rendimiento y Monitoreo
- [ ] Tiempo de carga < 3 segundos en páginas clave
- [ ] Optimización de imágenes verificada
- [ ] Google Search Console configurado
- [ ] Herramientas de monitoreo activas (uptime, logs, errores)
- [ ] Plan de respaldo ante caídas definido

## 2. Estrategia de despliegue

### 2.1 Despliegue controlado
1. **Ventana de mantenimiento**: Programar en horario de menor tráfico
2. **Comunicación**: Notificar a stakeholders sobre el go-live
3. **Rollback plan**: Tener procedimiento documentado para revertir cambios
4. **Smoke tests**: Ejecutar pruebas básicas inmediatamente post-deploy

### 2.2 Fases de activación
1. **Soft launch** (0-24h): Acceso limitado, monitoreo intensivo
2. **Apertura gradual** (24-48h): Aumentar tráfico, seguir monitoreando
3. **Operación normal** (48-72h): Tráfico completo, monitoreo continuo

## 3. Monitoreo 72 horas

### 3.1 Métricas clave a monitorear

#### Disponibilidad y Rendimiento
- **Uptime**: Objetivo 99.9%
- **Tiempo de respuesta**: < 2s promedio
- **Tasa de error**: < 0.1%
- **Tiempo de carga páginas clave**: Home, PLP, PDP, Checkout

#### Funcionalidad del Negocio
- **Conversión de checkout**: % de carritos que completan compra
- **Errores en pasarela de pago**: Registro de fallas
- **Abandono de carrito**: Tasa y momento del abandono
- **Formularios enviados**: Contacto, cotizaciones

#### Tráfico y Comportamiento
- **Visitantes únicos**: Número y origen
- **Páginas vistas**: Más visitadas
- **Tasa de rebote**: Por página
- **Tiempo en sitio**: Promedio por sesión
- **Dispositivos**: Desktop vs Mobile vs Tablet

#### Integraciones
- **GA4**: Eventos registrándose correctamente
- **CRM**: Leads recibidos y procesados
- **Email**: Tasa de entrega de transaccionales
- **WhatsApp/Chat**: Mensajes recibidos y respondidos

### 3.2 Horarios de monitoreo

| Período | Frecuencia | Responsable | Acciones |
|---------|------------|-------------|----------|
| 0-8h | Cada 1 hora | Equipo técnico | Revisión completa de métricas |
| 8-24h | Cada 2 horas | Equipo técnico | Monitoreo de alertas y logs |
| 24-48h | Cada 4 horas | Equipo técnico | Revisión de tendencias |
| 48-72h | Cada 6 horas | Equipo técnico | Monitoreo preventivo |

### 3.3 Protocolo de respuesta ante incidencias

#### Severidad 1 (Crítica): Sitio caído o checkout no funciona
- **Tiempo de respuesta**: Inmediato
- **Acción**: Activar equipo completo, ejecutar rollback si es necesario
- **Comunicación**: Notificar a stakeholders cada 30 min

#### Severidad 2 (Alta): Funcionalidad importante afectada
- **Tiempo de respuesta**: < 1 hora
- **Acción**: Investigar y aplicar fix o workaround
- **Comunicación**: Notificar a stakeholders al inicio y resolución

#### Severidad 3 (Media): Problema menor que no afecta transacciones
- **Tiempo de respuesta**: < 4 horas
- **Acción**: Documentar y programar fix
- **Comunicación**: Incluir en reporte diario

#### Severidad 4 (Baja): Mejora o bug cosmético
- **Tiempo de respuesta**: < 24 horas
- **Acción**: Agregar al backlog
- **Comunicación**: Incluir en reporte de 72h

## 4. Herramientas de monitoreo recomendadas

### 4.1 Uptime y Disponibilidad
- UptimeRobot / Pingdom / StatusCake
- Configurar alertas por email/SMS/Slack

### 4.2 Logs y Errores
- Odoo logs (revisar diariamente)
- Logs del servidor web (nginx/apache)
- Logs de la base de datos

### 4.3 Analytics y Comportamiento
- Google Analytics 4
- Hotjar / Microsoft Clarity (mapas de calor)
- Google Search Console

### 4.4 Rendimiento
- Google PageSpeed Insights
- GTmetrix / WebPageTest
- Lighthouse CI

## 5. Checklist de cierre 72h

- [ ] Reporte de estabilización completado
- [ ] Todas las incidencias críticas resueltas
- [ ] Incidencias menores documentadas y priorizadas
- [ ] Métricas baseline documentadas
- [ ] Aprendizajes y mejoras identificadas
- [ ] Transición a operación normal ejecutada
- [ ] Documentación actualizada con hallazgos
- [ ] Reunión de cierre con stakeholders
- [ ] Sign-off formal del go-live

## 6. Referencias

- Template de reporte: `docs/templates/post-launch-monitoring-report.md`
- KPIs objetivo: `docs/01-alcance-kpis.md`
- Plan de contingencia: Contactar a equipo técnico lead
