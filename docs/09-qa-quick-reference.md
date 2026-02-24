# Guía Rápida de QA - Fase 8

## 📋 Documentos Principales

1. **09-qa.md** - Checklist completo con todos los casos de prueba
2. **09-qa-ejecucion-guia.md** - Guía paso a paso para ejecutar QA (plan de 5 días)
3. **09-qa-incidencias-template.md** - Template para registrar bugs/issues
4. **09-qa-metricas-rendimiento.md** - Medición de performance y Core Web Vitals
5. **09-qa-compatibilidad-matriz.md** - Testing de navegadores y dispositivos
6. **09-qa-acta-signoff.md** - Documento de aprobación final

## 🎯 Prioridades de Testing

### Día 1: Funcional Desktop
- Home, navegación, búsqueda
- Catálogo (PLP) con filtros
- Detalle de producto (PDP)
- Carrito y checkout
- Páginas institucionales

### Día 2: Móvil y Tablet
- iOS (Safari, Chrome)
- Android (Chrome, Samsung Internet)
- iPad y tablets Android
- Orientaciones portrait y landscape

### Día 3: Rendimiento y Técnico
- PageSpeed Insights
- Core Web Vitals (LCP, FID, CLS)
- GTmetrix
- SEO básico
- Seguridad
- Accesibilidad

### Día 4: Compatibilidad y Re-tests
- Chrome, Firefox, Safari, Edge
- Re-testear fixes
- Validar regresiones

### Día 5: Reporte y Sign-off
- Compilar resultados
- Reunión de revisión
- Firma de acta

## 🔴 Bloqueadores de Go-Live (Críticos)

Estos DEBEN estar en ✅ para lanzar:

- [ ] **Cero incidencias críticas abiertas**
- [ ] **Checkout funciona sin errores**
- [ ] **Pagos procesan correctamente**
- [ ] **Home y PLP cargan en < 3 segundos**
- [ ] **Responsive en móvil y tablet**
- [ ] **No vulnerabilidades de seguridad**
- [ ] **HTTPS funcional**

## 📊 Métricas Clave

### Core Web Vitals (Objetivos)
- **LCP** < 2.5s
- **FID** < 100ms
- **CLS** < 0.1

### PageSpeed Insights
- **Mobile**: > 70/100 (mínimo aceptable)
- **Desktop**: > 80/100 (mínimo aceptable)

### Tiempos de Carga
- Home: < 3s
- PLP: < 3s
- PDP: < 2s
- Búsqueda: < 1s

## 🐛 Clasificación de Incidencias

### Crítica 🔴
- Bloquea compra/checkout
- Pérdida de datos
- Vulnerabilidad de seguridad
- Sitio no carga

**Acción**: Fix inmediato, bloquea go-live

### Alta 🟠
- Funcionalidad importante rota
- UX muy afectada
- Workaround difícil

**Acción**: Fix antes de go-live o plan post-launch

### Media 🟡
- Funcionalidad menor afectada
- Problema estético notable
- Workaround disponible

**Acción**: Puede postergarse con plan

### Baja 🟢
- Problema cosmético
- No afecta funcionalidad

**Acción**: Backlog para futuras releases

## 🔧 Herramientas Esenciales

### Performance
- Google PageSpeed Insights: https://pagespeed.web.dev/
- GTmetrix: https://gtmetrix.com/
- Chrome DevTools > Lighthouse

### Accesibilidad
- WAVE: https://wave.webaim.org/
- axe DevTools (extensión Chrome)

### Seguridad
- SSL Labs: https://www.ssllabs.com/ssltest/
- Security Headers: https://securityheaders.com/

### Responsive Testing
- Chrome DevTools (Device Mode)
- BrowserStack (multi-dispositivo)
- Dispositivos físicos

## 📝 Flujos Críticos a Testear

### 1. Flujo de Compra Completo
1. Home → Buscar producto
2. Ver resultados (PLP)
3. Click en producto (PDP)
4. Agregar al carrito
5. Ver carrito
6. Proceder a checkout
7. Ingresar datos de envío
8. Seleccionar método de envío
9. Ingresar datos de pago
10. Confirmar orden
11. Ver confirmación
12. Recibir email

### 2. Navegación y Búsqueda
1. Home → Menú categorías
2. Navegar por categoría
3. Aplicar filtros
4. Usar búsqueda
5. Ver sugerencias
6. Click en sugerencia

### 3. Usuario Registrado
1. Crear cuenta
2. Login
3. Ver perfil
4. Editar datos
5. Ver historial de órdenes
6. Logout

## 📱 Resoluciones a Testear

### Móvil
- 320px (iPhone SE)
- 375px (iPhone 8)
- 390px (iPhone 14)
- 412px (Android)

### Tablet
- 768px (iPad)
- 810px (Android Tablet)
- 820px (iPad Pro)

### Desktop
- 1366px (Laptop)
- 1920px (Desktop HD)

## ✅ Checklist Rápido de Pre-Launch

Antes de aprobar go-live, verificar:

- [ ] Todos los tests funcionales pasaron
- [ ] Testing móvil completado sin bloqueantes
- [ ] Métricas de rendimiento aceptables
- [ ] SEO básico configurado
- [ ] Seguridad validada (HTTPS, formularios)
- [ ] Compatibilidad con navegadores principales
- [ ] Incidencias documentadas
- [ ] Plan de acción para items pendientes
- [ ] Acta de sign-off firmada
- [ ] Comunicación a stakeholders completada

## 🚨 Qué Hacer Si...

### Encuentras un bug crítico
1. Stop testing en esa área
2. Documentar inmediatamente (screenshot/video)
3. Comunicar al Tech Lead
4. Registrar en sistema de tracking
5. No continuar hasta tener fix

### Encuentras un bug menor
1. Documentar con detalle
2. Continuar testing
3. Reportar al final de la sesión
4. Priorizar según criterios

### No puedes reproducir un bug
1. Documentar intento de reproducción
2. Pedir a otro tester que intente
3. Si persiste, marcar como "No reproducible"
4. Agregar notas sobre condiciones

### Test toma más tiempo del planeado
1. Completar área crítica actual
2. Comunicar delay al equipo
3. Re-priorizar items restantes
4. Considerar extender timeline o posponer items no críticos

## 📞 Contactos Clave

**Tech Lead**: [Nombre] - [Email/Slack]  
**QA Lead**: [Nombre] - [Email/Slack]  
**Project Manager**: [Nombre] - [Email/Slack]  
**Product Owner**: [Nombre] - [Email/Slack]

## 📚 Referencias Rápidas

### Navegadores y Versiones Soportadas
- Chrome 120+
- Firefox 121+
- Safari 17+
- Edge 120+
- Chrome Mobile (Android)
- Safari Mobile (iOS)

### URLs de Ambientes
- **Staging**: [URL]
- **Pre-producción**: [URL]
- **Documentación**: [URL]

### Credenciales de Test
- **Usuario Admin**: [usuario] / [password]
- **Usuario Regular**: [usuario] / [password]
- **Tarjetas de Test**: [ver doc de pagos]

## 💡 Tips y Mejores Prácticas

1. **Siempre usa datos de prueba**, no datos reales
2. **Toma screenshots** de todo bug encontrado
3. **Documenta pasos exactos** para reproducir
4. **Prueba en modo incógnito** para evitar cache
5. **Limpia cookies** entre pruebas si es necesario
6. **Verifica en móvil real**, no solo simulador
7. **Testea con diferentes velocidades de conexión**
8. **No asumas que algo funciona**, verifica todo
9. **Comunica progreso** diariamente
10. **Pide ayuda** si encuentras algo confuso

## 🎯 Definición de "Done" para QA

QA está completo cuando:
- ✅ 100% de checklist ejecutado
- ✅ Todos los bugs documentados
- ✅ Bugs críticos resueltos y verificados
- ✅ Métricas de performance medidas
- ✅ Reporte de QA completado
- ✅ Acta de sign-off firmada
- ✅ Handover a equipo de go-live realizado

---

**Última actualización**: Fase 8 - QA Integral  
**Versión**: 1.0  

*¿Preguntas? Contacta al QA Lead o consulta la documentación completa en `docs/09-qa.md`*
