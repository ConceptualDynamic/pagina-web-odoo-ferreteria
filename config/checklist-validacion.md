# Checklist de Validación - Entorno Odoo Funcional

Este documento proporciona un checklist completo para validar que la instancia de Odoo está correctamente configurada y todos los módulos requeridos están funcionando.

## Fecha de Validación: __________
## Responsable: __________
## Versión Odoo: __________

---

## 1. Instalación Base del Sistema

### 1.1 Servidor y Dependencias
- [ ] Ubuntu 22.04 LTS (o superior) instalado
- [ ] Python 3.10+ instalado y configurado
- [ ] PostgreSQL 14+ instalado y ejecutándose
- [ ] Todas las dependencias del sistema instaladas
- [ ] Usuario del sistema 'odoo' creado

**Comando de verificación**:
```bash
python3 --version
psql --version
systemctl status postgresql
```

### 1.2 Instalación de Odoo
- [ ] Odoo 17.0 instalado
- [ ] Servicio Odoo configurado
- [ ] Servicio Odoo ejecutándose
- [ ] Odoo inicia automáticamente con el sistema

**Comando de verificación**:
```bash
systemctl status odoo
sudo -u odoo odoo --version
```

### 1.3 Base de Datos
- [ ] Base de datos 'ferreteria_db' creada
- [ ] Usuario PostgreSQL 'odoo' configurado
- [ ] Permisos de base de datos correctos
- [ ] Conexión a base de datos funcional

**Comando de verificación**:
```bash
sudo -u postgres psql -d ferreteria_db -c "SELECT version();"
```

---

## 2. Configuración de Odoo

### 2.1 Archivo de Configuración
- [ ] Archivo /etc/odoo/odoo.conf existe
- [ ] Contraseña maestra (admin_passwd) cambiada
- [ ] Configuración de base de datos correcta
- [ ] Rutas de addons configuradas
- [ ] Configuración de workers apropiada
- [ ] Configuración de límites de recursos

**Comando de verificación**:
```bash
cat /etc/odoo/odoo.conf | grep -E "db_name|admin_passwd|workers"
```

### 2.2 Acceso Web
- [ ] Puerto 8069 accesible
- [ ] Interfaz web carga correctamente
- [ ] Login funciona correctamente
- [ ] No hay errores de JavaScript en consola del navegador

**URL de prueba**: http://[servidor]:8069

### 2.3 Logs y Monitoreo
- [ ] Archivo de log configurado
- [ ] Logs se escriben correctamente
- [ ] No hay errores críticos en logs
- [ ] Rotación de logs configurada

**Comando de verificación**:
```bash
tail -50 /var/log/odoo/odoo-server.log | grep -i error
```

---

## 3. Módulos Core Instalados

### 3.1 Website (website)
- [ ] Módulo instalado
- [ ] Estado: 'installed'
- [ ] Sin errores en instalación
- [ ] Homepage accesible
- [ ] Editor visual funciona

**Validación funcional**:
1. Ir a Website > Site > Homepage
2. Clic en "Edit"
3. Agregar un bloque de texto
4. Guardar cambios
5. Verificar cambios en frontend

**Estado**: ⬜ No instalado | ⬜ Instalado | ⬜ Configurado | ✅ Validado

### 3.2 eCommerce (website_sale)
- [ ] Módulo instalado
- [ ] Estado: 'installed'
- [ ] Página Shop accesible
- [ ] Carrito de compras funciona
- [ ] Checkout funciona

**Validación funcional**:
1. Ir a /shop
2. Agregar producto al carrito
3. Ver carrito
4. Iniciar checkout
5. Completar formulario (modo test)

**Estado**: ⬜ No instalado | ⬜ Instalado | ⬜ Configurado | ✅ Validado

### 3.3 Inventory (stock)
- [ ] Módulo instalado
- [ ] Estado: 'installed'
- [ ] Almacén principal creado
- [ ] Ubicaciones configuradas
- [ ] Movimientos de stock funcionan

**Validación funcional**:
1. Ir a Inventory
2. Crear producto con stock
3. Hacer ajuste de inventario
4. Ver historial de movimientos
5. Verificar cantidad actualizada

**Estado**: ⬜ No instalado | ⬜ Instalado | ⬜ Configurado | ✅ Validado

### 3.4 Sales (sale)
- [ ] Módulo instalado
- [ ] Estado: 'installed'
- [ ] Equipo de ventas configurado
- [ ] Puede crear cotizaciones
- [ ] Puede confirmar órdenes

**Validación funcional**:
1. Ir a Sales
2. Crear nueva cotización
3. Agregar productos
4. Confirmar cotización
5. Ver orden de venta creada

**Estado**: ⬜ No instalado | ⬜ Instalado | ⬜ Configurado | ✅ Validado

### 3.5 CRM (crm)
- [ ] Módulo instalado
- [ ] Estado: 'installed'
- [ ] Pipeline configurado
- [ ] Puede crear oportunidades
- [ ] Etapas funcionan correctamente

**Validación funcional**:
1. Ir a CRM
2. Crear nueva oportunidad
3. Mover entre etapas
4. Agregar actividades
5. Verificar seguimiento

**Estado**: ⬜ No instalado | ⬜ Instalado | ⬜ Configurado | ✅ Validado

---

## 4. Configuración Inicial

### 4.1 Datos de Empresa
- [ ] Nombre de empresa configurado
- [ ] Dirección configurada
- [ ] Teléfono configurado
- [ ] Email configurado
- [ ] Logo corporativo subido
- [ ] Timezone configurado (America/Bogota)

**Ubicación**: Settings > General Settings > Company Information

### 4.2 Configuración de Website
- [ ] Nombre del sitio configurado
- [ ] Dominio configurado (o pendiente)
- [ ] Idioma español configurado
- [ ] Favicon subido
- [ ] Homepage personalizada
- [ ] Menú principal configurado

**Ubicación**: Website > Configuration > Settings

### 4.3 Configuración de eCommerce
- [ ] Categorías de productos creadas
- [ ] Layout de catálogo configurado
- [ ] Opciones de checkout configuradas
- [ ] Términos y condiciones agregados
- [ ] Políticas de privacidad agregadas

**Ubicación**: Website > eShop > Products

### 4.4 Configuración de Inventory
- [ ] Almacén principal configurado
- [ ] Ubicaciones de stock definidas
- [ ] Rutas de entrega configuradas
- [ ] Reglas de reabastecimiento (si aplica)

**Ubicación**: Inventory > Configuration > Warehouses

### 4.5 Configuración de Sales
- [ ] Equipo de ventas "Ventas Web" creado
- [ ] Términos de pago configurados
- [ ] Lista de precios configurada
- [ ] Secuencias de órdenes configuradas

**Ubicación**: Sales > Configuration

### 4.6 Configuración de CRM
- [ ] Pipeline de oportunidades configurado
- [ ] Etapas definidas
- [ ] Reglas de asignación configuradas (si aplica)
- [ ] Equipo de ventas asociado

**Ubicación**: CRM > Configuration

---

## 5. Integración Entre Módulos

### 5.1 Website ↔ eCommerce
- [ ] Productos visibles en Shop
- [ ] Carrito funciona desde website
- [ ] Checkout integrado
- [ ] Órdenes se crean en Sales

### 5.2 eCommerce ↔ Inventory
- [ ] Stock visible en productos web
- [ ] Compras web afectan inventario
- [ ] Reglas de disponibilidad funcionan

### 5.3 eCommerce ↔ Sales
- [ ] Órdenes web crean Sales Orders
- [ ] Clientes web registrados en Contacts
- [ ] Flujo de orden completo funciona

### 5.4 Sales ↔ CRM
- [ ] Oportunidades convertibles a cotizaciones
- [ ] Clientes sincronizados
- [ ] Pipeline refleja ventas

---

## 6. Seguridad

### 6.1 Configuración de Seguridad
- [ ] Contraseña maestra cambiada
- [ ] Contraseña de BD segura
- [ ] Acceso a base de datos restringido
- [ ] Firewall configurado
- [ ] HTTPS configurado (producción)
- [ ] Certificado SSL válido (producción)

### 6.2 Usuarios y Permisos
- [ ] Usuario administrador configurado
- [ ] Contraseña administrador segura
- [ ] Usuarios adicionales creados (si aplica)
- [ ] Grupos de acceso configurados
- [ ] Permisos por módulo validados

---

## 7. Performance y Recursos

### 7.1 Recursos del Sistema
- [ ] Uso de CPU normal (<80%)
- [ ] Uso de RAM normal (<80%)
- [ ] Espacio en disco suficiente (>5GB libre)
- [ ] Base de datos optimizada

**Comando de verificación**:
```bash
top -bn1 | grep odoo
df -h
```

### 7.2 Performance Web
- [ ] Página carga en <3 segundos
- [ ] No hay errores 500
- [ ] Imágenes optimizadas
- [ ] Cache configurado

### 7.3 Workers y Procesos
- [ ] Número de workers apropiado
- [ ] Workers funcionando correctamente
- [ ] No hay workers muertos
- [ ] Logs sin errores de workers

---

## 8. Respaldo y Recuperación

### 8.1 Sistema de Backups
- [ ] Script de backup creado
- [ ] Backup de base de datos funciona
- [ ] Backup de filestore funciona
- [ ] Backups automatizados (cron)
- [ ] Ubicación de backups segura
- [ ] Retención de backups definida

### 8.2 Prueba de Restauración
- [ ] Backup restaurado exitosamente (test)
- [ ] Datos íntegros después de restauración
- [ ] Procedimiento documentado

---

## 9. Documentación

### 9.1 Documentación Técnica
- [ ] Configuración documentada
- [ ] Credenciales registradas (seguro)
- [ ] Arquitectura documentada
- [ ] Procedimientos de mantenimiento

### 9.2 Documentación de Usuario
- [ ] Manual de usuario básico (si aplica)
- [ ] Guía de administración
- [ ] Contactos de soporte

---

## 10. Tests Finales End-to-End

### 10.1 Flujo Completo de Compra
- [ ] Usuario visita homepage
- [ ] Navega a catálogo
- [ ] Busca producto
- [ ] Agrega al carrito
- [ ] Procede a checkout
- [ ] Completa información
- [ ] Confirma orden
- [ ] Recibe confirmación
- [ ] Orden aparece en backend
- [ ] Stock se actualiza
- [ ] Email de confirmación (si configurado)

### 10.2 Flujo Completo de Lead
- [ ] Usuario llena formulario de contacto
- [ ] Lead se crea en CRM
- [ ] Lead es asignado
- [ ] Lead avanza en pipeline
- [ ] Lead se convierte a oportunidad
- [ ] Oportunidad se convierte a cotización
- [ ] Cotización se confirma

---

## 11. Criterios de Aceptación

### Criterio 1: Instalación Completa
✅ Todos los módulos core instalados sin errores

- [ ] Website: ✅ Instalado y funcional
- [ ] eCommerce: ✅ Instalado y funcional
- [ ] Inventory: ✅ Instalado y funcional
- [ ] Sales: ✅ Instalado y funcional
- [ ] CRM: ✅ Instalado y funcional

### Criterio 2: Configuración Básica
✅ Configuración inicial completada

- [ ] Empresa configurada
- [ ] Módulos configurados
- [ ] Integraciones funcionando

### Criterio 3: Entorno Funcional
✅ Sistema operativo y accesible

- [ ] Web accesible
- [ ] Sin errores críticos
- [ ] Performance aceptable
- [ ] Tests end-to-end exitosos

### Criterio 4: Documentación
✅ Documentación completa y actualizada

- [ ] Configuración documentada
- [ ] Procedimientos documentados
- [ ] Credenciales guardadas

---

## 12. Problemas Identificados

### Problemas Críticos (Bloqueantes)
```
[Ninguno / Describir aquí]
```

### Problemas Mayores (No bloqueantes pero importantes)
```
[Ninguno / Describir aquí]
```

### Problemas Menores (Mejoras)
```
[Ninguno / Describir aquí]
```

---

## 13. Resultado Final

**Estado General**: 
- [ ] ✅ APROBADO - Entorno funcional y listo
- [ ] ⚠️ APROBADO CON RESERVAS - Funcional con problemas menores
- [ ] ❌ RECHAZADO - Problemas críticos identificados

**Comentarios adicionales**:
```
[Agregar comentarios aquí]
```

**Firmado por**: __________  
**Fecha**: __________  
**Próxima revisión**: __________

---

## 14. Siguiente Pasos

Después de aprobar esta validación:

1. [ ] Marcar issue #1 como completado
2. [ ] Iniciar [Fase 2] Arquitectura y navegación (#2)
3. [ ] Iniciar configuración de estructura de datos (#4)
4. [ ] Documentar lecciones aprendidas
5. [ ] Actualizar README principal

---

## Referencias

- Documento de configuración técnica: `/docs/00-configuracion-tecnica-odoo.md`
- Archivo de configuración: `/config/odoo.conf.template`
- Módulos requeridos: `/config/modulos-requeridos.md`
- Documentación Odoo: https://www.odoo.com/documentation/17.0/

---

**Notas**:
- Este checklist debe ser completado por el equipo técnico responsable
- Mantener evidencias (screenshots, logs) de las validaciones
- Actualizar este documento según cambios en el entorno
