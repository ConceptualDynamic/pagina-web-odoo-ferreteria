# ✅ Checklist Go-Live - Ferretería Odoo

> **Instrucciones**: Marcar cada ítem como completado antes de proceder al lanzamiento.  
> **Responsable de validación**: _______________  
> **Fecha objetivo de go-live**: _______________  
> **Fecha real de go-live**: _______________

---

## 🔧 PRE-LANZAMIENTO (T-24h)

### Infraestructura y Configuración
- [ ] Servidor de producción configurado y funcionando
- [ ] SSL/TLS activo con certificado válido (verificar en https://www.ssllabs.com)
- [ ] DNS configurado apuntando a producción
- [ ] Variables de entorno de producción revisadas y correctas
- [ ] Backup automático configurado
- [ ] Backup manual pre-lanzamiento completado (fecha: _______)
- [ ] Restauración de backup validada

### Aplicación Odoo
- [ ] Odoo actualizado a última versión estable
- [ ] Módulos requeridos instalados y actualizados
- [ ] Tema/diseño aplicado correctamente
- [ ] Configuración de empresa completada (nombre, logo, dirección, contacto)
- [ ] Usuarios y permisos configurados
- [ ] Modo debug desactivado en producción

### Base de Datos
- [ ] Datos de productos cargados y verificados
- [ ] Precios actualizados
- [ ] Inventario inicial configurado
- [ ] Categorías de productos organizadas
- [ ] Imágenes de productos optimizadas y cargadas
- [ ] Datos de prueba eliminados

---

## 🌐 VALIDACIÓN FUNCIONAL

### Navegación y Páginas Core
- [ ] Home page carga sin errores
- [ ] Menú de navegación funcional
- [ ] Búsqueda de productos operativa
- [ ] Filtros de catálogo funcionando
- [ ] Paginación de resultados correcta

### Catálogo de Productos
- [ ] Lista de productos (PLP) muestra correctamente
- [ ] Detalle de producto (PDP) con toda la información
- [ ] Imágenes de productos cargan correctamente
- [ ] Variantes de productos (si aplica) funcionan
- [ ] Stock disponible se muestra correctamente
- [ ] Botón "Agregar al carrito" funcional

### Carrito y Checkout
- [ ] Agregar productos al carrito funciona
- [ ] Modificar cantidades en carrito funciona
- [ ] Eliminar productos del carrito funciona
- [ ] Cupones de descuento funcionan (si aplica)
- [ ] Cálculo de subtotal correcto
- [ ] Cálculo de impuestos correcto
- [ ] Cálculo de envío correcto
- [ ] Total final correcto
- [ ] Proceso de checkout fluye sin errores
- [ ] Validación de formularios correcta
- [ ] Creación de cuenta de usuario funciona
- [ ] Login de usuarios funciona

### Pasarela de Pagos
- [ ] Pasarela configurada en modo PRODUCCIÓN
- [ ] Credenciales de producción verificadas
- [ ] Pago con tarjeta de crédito funciona
- [ ] Pago con tarjeta de débito funciona
- [ ] Otros métodos de pago configurados (transferencia, etc.)
- [ ] Confirmación de pago llega al cliente (email)
- [ ] Orden se registra correctamente en Odoo

### Envíos
- [ ] Opciones de envío disponibles
- [ ] Cálculo de costo de envío correcto
- [ ] Direcciones de envío se guardan correctamente
- [ ] Integración con proveedor de envíos (si aplica)

### Comunicaciones
- [ ] Email de confirmación de orden funciona
- [ ] Email de registro de usuario funciona
- [ ] Email de recuperación de contraseña funciona
- [ ] Formulario de contacto envía emails
- [ ] Templates de email con diseño corporativo

### Páginas de Contenido
- [ ] Página "Acerca de" publicada
- [ ] FAQs actualizadas
- [ ] Política de privacidad publicada
- [ ] Términos y condiciones publicados
- [ ] Política de devoluciones publicada
- [ ] Información de envío publicada
- [ ] Página de contacto con información correcta

---

## 📱 RESPONSIVE Y CROSS-BROWSER

### Desktop
- [ ] Chrome (última versión) - Windows
- [ ] Firefox (última versión) - Windows
- [ ] Safari (última versión) - macOS
- [ ] Edge (última versión) - Windows

### Mobile
- [ ] Chrome Mobile - Android (verificar en dispositivo real)
- [ ] Safari Mobile - iOS (verificar en dispositivo real)
- [ ] Responsive: 320px width (móvil pequeño)
- [ ] Responsive: 768px width (tablet)

### Funcionalidad Mobile
- [ ] Menú hamburguesa funcional
- [ ] Carrito accesible en móvil
- [ ] Checkout completable en móvil
- [ ] Formularios utilizables en móvil
- [ ] Botones suficientemente grandes (touch-friendly)

---

## 🚀 RENDIMIENTO

### Tiempos de Carga
- [ ] Home page < 3 segundos
- [ ] PLP < 3 segundos
- [ ] PDP < 2 segundos
- [ ] Checkout < 2 segundos

### Optimizaciones
- [ ] Imágenes optimizadas (WebP, lazy loading)
- [ ] CSS minificado
- [ ] JavaScript minificado
- [ ] Caché del navegador configurado
- [ ] CDN configurado (si aplica)
- [ ] Compresión GZIP/Brotli activa

### Testing de Rendimiento
- [ ] Google PageSpeed Insights > 80 (móvil)
- [ ] Google PageSpeed Insights > 90 (desktop)
- [ ] GTmetrix Grade A o B

---

## 🔒 SEGURIDAD

### HTTPS y Certificados
- [ ] HTTPS forzado en todo el sitio
- [ ] Redirección automática HTTP → HTTPS
- [ ] Certificado SSL válido y no expira pronto
- [ ] Sin advertencias de contenido mixto

### Headers de Seguridad
- [ ] X-Frame-Options configurado
- [ ] X-Content-Type-Options configurado
- [ ] Content-Security-Policy configurado
- [ ] Strict-Transport-Security configurado

### Autenticación y Sesiones
- [ ] Sesiones seguras (HttpOnly, Secure flags)
- [ ] Contraseñas hasheadas correctamente
- [ ] Rate limiting en formularios
- [ ] Protección CSRF activa
- [ ] Protección contra SQL injection
- [ ] Protección contra XSS

### Datos Sensibles
- [ ] No hay credenciales en código fuente
- [ ] No hay API keys expuestas en frontend
- [ ] Variables de entorno en archivo .env (no en Git)
- [ ] Información sensible no en logs públicos

---

## 🔍 SEO Y ANALÍTICA

### SEO Básico
- [ ] Meta títulos únicos en páginas clave (Home, PLP, PDP)
- [ ] Meta descripciones en páginas clave
- [ ] URLs amigables (sin parámetros raros)
- [ ] Estructura de headings correcta (H1, H2, H3)
- [ ] Texto alternativo (alt) en imágenes
- [ ] Sitemap.xml generado y accesible
- [ ] Robots.txt configurado
- [ ] Canonical tags configurados

### Open Graph y Social
- [ ] Open Graph tags para compartir en redes
- [ ] Twitter Card configurado
- [ ] Favicon configurado

### Analítica
- [ ] Google Analytics instalado (o alternativa)
- [ ] Google Tag Manager configurado (si aplica)
- [ ] Eventos de conversión configurados
- [ ] Google Search Console verificado
- [ ] Facebook Pixel instalado (si aplica)

---

## 🔗 INTEGRACIONES

### Pasarela de Pagos
- [ ] Modo sandbox desactivado
- [ ] Modo producción activado
- [ ] Webhook configurado y recibiendo eventos
- [ ] Logs de transacciones funcionando

### Proveedores de Envío
- [ ] API de envíos en modo producción
- [ ] Credenciales de producción configuradas
- [ ] Prueba de cotización de envío exitosa
- [ ] Prueba de generación de guía exitosa (si aplica)

### ERP/Inventario
- [ ] Sincronización de productos funcionando
- [ ] Actualización de inventario en tiempo real
- [ ] Sincronización de órdenes funcionando

### Email Marketing
- [ ] Integración con plataforma de email (Mailchimp, etc.)
- [ ] Suscripción a newsletter funcionando
- [ ] Sincronización de contactos activa

---

## 📊 MONITOREO Y LOGS

### Herramientas de Monitoreo
- [ ] Uptime monitoring configurado (UptimeRobot, Pingdom)
- [ ] Alertas de downtime configuradas
- [ ] Dashboard de métricas accesible
- [ ] Logs centralizados configurados

### Configuración de Logs
- [ ] Logs de aplicación activados
- [ ] Logs de errores activados
- [ ] Rotación de logs configurada
- [ ] Notificaciones de errores críticos

---

## 📋 CONTENIDO Y LEGAL

### Contenido
- [ ] Todos los textos revisados (sin "Lorem ipsum")
- [ ] Información de contacto correcta
- [ ] Horarios de atención actualizados
- [ ] Precios finales verificados
- [ ] Promociones activas configuradas

### Legal y Compliance
- [ ] Política de privacidad conforme a GDPR/leyes locales
- [ ] Términos y condiciones revisados por legal
- [ ] Política de cookies implementada (si aplica)
- [ ] Banner de cookies funcional (si aplica)
- [ ] Aviso de protección de datos (si aplica en tu país)

---

## 🧪 TESTING FINAL

### Tests Funcionales
- [ ] Suite de tests automatizados ejecutada (si existe)
- [ ] Tests manuales de regresión completados
- [ ] Flujo de compra completo probado 3 veces
- [ ] Diferentes métodos de pago probados
- [ ] Diferentes opciones de envío probadas

### Tests de Usuario
- [ ] UAT (User Acceptance Testing) completado
- [ ] Feedback de beta testers incorporado
- [ ] Pruebas con clientes reales (beta cerrada)

---

## 📞 PREPARACIÓN DEL EQUIPO

### Comunicación
- [ ] Equipo técnico notificado de fecha y hora de go-live
- [ ] Equipo de soporte al cliente capacitado
- [ ] Plan de comunicación externa preparado
- [ ] Anuncios en redes sociales programados

### Disponibilidad
- [ ] Equipo técnico disponible durante lanzamiento
- [ ] Contactos de emergencia compartidos
- [ ] Plan de escalamiento definido
- [ ] Horarios de guardia asignados (primeras 72h)

### Documentación
- [ ] Runbook operativo actualizado
- [ ] Procedimientos de rollback documentados
- [ ] FAQs para soporte al cliente preparadas
- [ ] Guías de usuario disponibles

---

## 🚨 PLAN DE CONTINGENCIA

### Rollback
- [ ] Procedimiento de rollback documentado
- [ ] Criterios para ejecutar rollback definidos
- [ ] Backup pre-lanzamiento disponible
- [ ] Tiempo estimado de rollback: _____ minutos

### Contactos de Emergencia
- [ ] Lista de contactos actualizada
- [ ] Proveedor de hosting: ________________
- [ ] Proveedor de pagos: ________________
- [ ] Odoo Partner: ________________

---

## ✅ APROBACIÓN FINAL

### Firmas de Aprobación
- [ ] **Líder Técnico**: ________________ Fecha: ______
- [ ] **QA Lead**: ________________ Fecha: ______
- [ ] **Product Owner**: ________________ Fecha: ______
- [ ] **Stakeholder/Cliente**: ________________ Fecha: ______

### Criterios de GO/NO-GO
- [ ] **Todos los ítems críticos completados** (sin excepciones)
- [ ] **Ítems no completados documentados** con justificación
- [ ] **Riesgos identificados y mitigados**
- [ ] **Equipo listo y disponible**

---

## 🎯 DECISIÓN FINAL

**Estado**: [ ] ✅ GO-LIVE APROBADO | [ ] ❌ NO-GO (posponer)

**Fecha y hora de lanzamiento confirmada**: _______________

**Notas finales**:
_______________________________________________
_______________________________________________
_______________________________________________

---

**Versión del documento**: 1.0  
**Última actualización**: 2026-02-24  
**Responsable**: Equipo de Desarrollo ConceptualDynamic
