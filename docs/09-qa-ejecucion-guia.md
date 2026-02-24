# Guía de Ejecución de QA - Fase 8

## Pre-requisitos

### Ambiente de Pruebas
- [ ] Ambiente de staging configurado y accesible
- [ ] Datos de prueba cargados (productos, categorías, precios)
- [ ] Usuarios de prueba creados
- [ ] Métodos de pago en modo sandbox/test
- [ ] Integración de envíos en modo test

### Herramientas Necesarias
- [ ] Navegadores instalados (Chrome, Firefox, Safari, Edge)
- [ ] Dispositivos móviles disponibles (iOS, Android)
- [ ] Acceso a herramientas de performance (PageSpeed, GTmetrix)
- [ ] Herramientas de accessibility (WAVE, axe DevTools)
- [ ] Sistema de registro de incidencias (GitHub Issues, Planner)

### Documentación
- [ ] Requisitos funcionales (Fases 1-7)
- [ ] Diseño UI/UX aprobado
- [ ] Flujos de usuario definidos
- [ ] Checklist de QA (09-qa.md)

## Día 1: QA Funcional Desktop

### Sesión Mañana (4 horas)
**9:00 - 10:30**: Navegación y Home
- Ejecutar checklist 1.1 (Página de Inicio)
- Ejecutar checklist 1.7 (Búsqueda y Navegación)
- Registrar incidencias encontradas

**10:30 - 10:45**: Break

**10:45 - 13:00**: Catálogo y Productos
- Ejecutar checklist 1.2 (Catálogo y PLP)
- Ejecutar checklist 1.3 (PDP)
- Probar diferentes categorías y filtros
- Registrar incidencias encontradas

### Sesión Tarde (4 horas)
**14:00 - 16:00**: Carrito y Checkout
- Ejecutar checklist 1.4 (Carrito de Compras)
- Ejecutar checklist 1.5 (Checkout y Pagos)
- Probar diferentes flujos de compra
- Registrar incidencias encontradas

**16:00 - 16:15**: Break

**16:15 - 18:00**: Páginas Institucionales
- Ejecutar checklist 1.6 (Páginas Institucionales)
- Revisar contenido y formularios
- Registrar incidencias encontradas

**18:00 - 18:30**: Compilar reporte del día
- Consolidar incidencias encontradas
- Priorizar issues críticos y altos
- Comunicar bloqueadores al equipo

## Día 2: QA Móvil y Tablet

### Sesión Mañana (4 horas)
**9:00 - 9:30**: Setup y preparación
- Configurar dispositivos de prueba
- Verificar conectividad
- Revisar incidencias del día anterior

**9:30 - 11:30**: Testing Móvil (iPhone/Android)
- Ejecutar checklist 2.1 (Responsividad General)
- Ejecutar checklist 2.2 (Navegación Móvil)
- Probar en diferentes tamaños de pantalla
- Registrar incidencias móvil-específicas

**11:30 - 11:45**: Break

**11:45 - 13:00**: Testing Móvil (Formularios y Checkout)
- Ejecutar checklist 2.3 (Formularios Móviles)
- Ejecutar checklist 2.4 (Checkout Móvil)
- Completar flujo de compra en móvil
- Registrar incidencias

### Sesión Tarde (4 horas)
**14:00 - 16:00**: Testing Tablet (iPad/Android Tablet)
- Repetir checklists 2.1 a 2.4 en tablets
- Verificar layout intermedio
- Probar orientación portrait y landscape
- Registrar incidencias tablet-específicas

**16:00 - 16:15**: Break

**16:15 - 18:00**: Testing Navegadores Móviles
- Ejecutar checklist 7.2 (Navegadores Móvil)
- Probar Safari iOS, Chrome Android, Samsung Internet
- Documentar diferencias entre navegadores
- Registrar incidencias de compatibilidad

**18:00 - 18:30**: Compilar reporte del día
- Consolidar incidencias móvil/tablet
- Priorizar issues
- Actualizar registro de incidencias

## Día 3: QA de Rendimiento, SEO y Accesibilidad

### Sesión Mañana (4 horas)
**9:00 - 11:00**: Testing de Rendimiento
- Ejecutar checklist 3.1 (Tiempos de Carga)
- Ejecutar checklist 3.2 (Optimización de Recursos)
- Ejecutar checklist 3.3 (Core Web Vitals)
- Usar PageSpeed Insights en páginas clave
- Usar GTmetrix para análisis detallado
- Usar Lighthouse para auditoría completa
- Documentar métricas y screenshots
- Identificar cuellos de botella

**11:00 - 11:15**: Break

**11:15 - 13:00**: Testing de SEO
- Ejecutar checklist 4.1 (Meta Tags)
- Ejecutar checklist 4.2 (Contenido)
- Ejecutar checklist 4.3 (Técnico)
- Verificar sitemap.xml
- Verificar robots.txt
- Revisar URLs y estructura
- Documentar issues SEO

### Sesión Tarde (4 horas)
**14:00 - 16:00**: Testing de Accesibilidad
- Ejecutar checklist 6.1 (WCAG 2.1 Nivel AA)
- Ejecutar checklist 6.2 (Lectores de Pantalla)
- Usar WAVE para análisis
- Usar axe DevTools para auditoría
- Probar navegación por teclado
- Verificar contraste de colores
- Documentar issues de accesibilidad

**16:00 - 16:15**: Break

**16:15 - 18:00**: Testing de Seguridad
- Ejecutar checklist 5.1 (Formularios)
- Ejecutar checklist 5.2 (Autenticación)
- Ejecutar checklist 5.3 (Pagos)
- Verificar HTTPS
- Usar SSL Labs para análisis SSL
- Revisar headers de seguridad
- Documentar vulnerabilidades

**18:00 - 18:30**: Compilar reporte del día
- Consolidar métricas de rendimiento
- Consolidar issues SEO, accesibilidad, seguridad
- Actualizar registro de incidencias

## Día 4: Compatibilidad de Navegadores y Re-tests

### Sesión Mañana (4 horas)
**9:00 - 12:00**: Testing de Compatibilidad
- Ejecutar checklist 7.1 (Navegadores Desktop)
- Probar en Chrome, Firefox, Safari, Edge
- Verificar funcionalidad core en cada navegador
- Documentar diferencias y bugs específicos
- Registrar incidencias de compatibilidad

**12:00 - 13:00**: Revisión de Incidencias
- Revisar todas las incidencias registradas
- Validar severidades asignadas
- Confirmar duplicados
- Consolidar registro

### Sesión Tarde (4 horas)
**14:00 - 17:00**: Re-testing de Fixes
- Re-testear incidencias marcadas como resueltas
- Verificar que no se crearon regresiones
- Actualizar estados en registro de incidencias
- Cerrar incidencias validadas

**17:00 - 18:00**: Preparación de Reporte Final
- Compilar métricas finales
- Preparar screenshots y evidencias
- Redactar resumen ejecutivo
- Preparar presentación de resultados

## Día 5: Reporte Final y Sign-off

### Sesión Mañana (4 horas)
**9:00 - 11:00**: Finalización de Reporte
- Completar todos los entregables
- Organizar documentación
- Preparar acta de sign-off
- Revisar criterios de go-live

**11:00 - 13:00**: Reunión de Revisión con Equipo
- Presentar resultados de QA
- Revisar incidencias críticas/altas
- Discutir plan para incidencias pendientes
- Tomar decisiones sobre go-live

### Sesión Tarde (3 horas)
**14:00 - 16:00**: Ajustes Finales
- Incorporar feedback de reunión
- Actualizar documentación
- Finalizar acta de sign-off
- Preparar handover a Fase 9

**16:00 - 17:00**: Sign-off Formal
- Reunión de aprobación con stakeholders
- Firma de acta de QA
- Autorización para go-live
- Comunicación de resultados

## Mejores Prácticas Durante la Ejecución

### Registro de Incidencias
1. **Ser específico**: Incluir pasos exactos para reproducir
2. **Incluir contexto**: Navegador, dispositivo, versión, configuración
3. **Adjuntar evidencias**: Screenshots, videos, logs
4. **Priorizar correctamente**: Usar criterios de severidad definidos
5. **Actualizar estados**: Mantener registro actualizado en tiempo real

### Comunicación
1. **Daily updates**: Compartir progreso diario con el equipo
2. **Bloqueadores inmediatos**: Comunicar issues críticos inmediatamente
3. **Claridad**: Usar lenguaje claro y profesional
4. **Evidencias**: Siempre respaldar con screenshots o videos

### Eficiencia
1. **Seguir el plan**: No improvisar el orden de testing
2. **Timeboxing**: Respetar los tiempos asignados
3. **Paralelización**: Si hay múltiples testers, dividir trabajo
4. **Herramientas**: Usar herramientas automatizadas cuando sea posible

### Calidad
1. **No asumir**: Probar todo lo que está en la checklist
2. **Pensar como usuario**: Probar flujos reales de usuario
3. **Edge cases**: No solo happy path, probar escenarios extremos
4. **Regresión**: Verificar que fixes no rompan otras funcionalidades

## Criterios de Éxito de QA

### Cobertura
- ✅ 100% de checklist funcional ejecutada
- ✅ Todas las páginas clave testeadas
- ✅ Todos los flujos críticos validados
- ✅ Testing en todos los navegadores/dispositivos objetivo

### Calidad
- ✅ Cero incidencias críticas abiertas
- ✅ Plan de acción para todas las incidencias altas
- ✅ Métricas de rendimiento documentadas
- ✅ Reporte completo y profesional

### Proceso
- ✅ Incidencias registradas con evidencias
- ✅ Comunicación clara con equipo
- ✅ Stakeholders informados
- ✅ Acta de sign-off firmada

## Plantilla de Reporte Diario

```
REPORTE QA - DÍA [X]
Fecha: [DD/MM/YYYY]
Tester: [Nombre]

ACTIVIDADES COMPLETADAS:
- [Lista de checklists ejecutados]
- [Áreas testeadas]

INCIDENCIAS NUEVAS:
- Críticas: [X]
- Altas: [X]
- Medias: [X]
- Bajas: [X]

BLOQUEADORES:
- [Descripción de bloqueadores si los hay]

PROGRESO:
[X]% del plan de testing completado

PRÓXIMAS ACTIVIDADES:
- [Plan para día siguiente]

NOTAS/OBSERVACIONES:
- [Cualquier observación relevante]
```

## Recursos Adicionales

### Links Útiles
- PageSpeed Insights: https://pagespeed.web.dev/
- GTmetrix: https://gtmetrix.com/
- WAVE: https://wave.webaim.org/
- SSL Labs: https://www.ssllabs.com/ssltest/
- Can I Use: https://caniuse.com/

### Documentos de Referencia
- `09-qa.md` - Checklist completo de QA
- `09-qa-incidencias-template.md` - Template para registro
- `01-alcance-kpis.md` - Objetivos del proyecto
- `05-diseno-ux-ui.md` - Diseño aprobado

---

**Última actualización**: Fase 8 - QA Integral  
**Responsable**: QA Lead
