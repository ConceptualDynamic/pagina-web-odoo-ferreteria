# 🚀 Guía Rápida de Go-Live

> **Referencia rápida para el día del lanzamiento**

## ⏰ Timeline del Go-Live

### T-24h: PRE-LANZAMIENTO
```
✓ Ejecutar checklist completo
✓ Backup completo de DB y archivos
✓ Verificar restauración de backup
✓ Notificar al equipo
✓ Confirmar disponibilidad del equipo técnico
```

### T-1h: PREPARACIÓN FINAL
```
✓ Último backup
✓ Verificar variables de entorno
✓ Confirmar credenciales de producción
✓ Preparar scripts de deployment
✓ Abrir canales de comunicación
```

### T=0: LANZAMIENTO
```
✓ Ejecutar deployment
✓ Activar modo mantenimiento (si aplica)
✓ Cambios de DNS/configuración
✓ Desactivar modo mantenimiento
```

### T+15min: VALIDACIÓN INMEDIATA
```
✓ Sitio carga correctamente
✓ Flujo de compra funcional
✓ Integraciones respondiendo
✓ Logs sin errores críticos
```

### T+1h: SMOKE TESTS
```
✓ Suite de tests críticos
✓ Métricas de rendimiento
✓ Primera transacción real
✓ Confirmar go-live exitoso
```

---

## 📋 Checklist Ultra-Rápido

### Antes del Lanzamiento
- [ ] ✅ Backup completo realizado
- [ ] 🔐 HTTPS funcionando
- [ ] 🛒 Carrito funcional
- [ ] 💳 Pagos en producción
- [ ] 📧 Emails funcionando
- [ ] 📱 Responsive verificado
- [ ] ⚡ Rendimiento < 3s
- [ ] 🔒 Certificado SSL válido

### Durante el Lanzamiento
- [ ] 🚀 Deployment ejecutado
- [ ] ✓ Sitio accesible
- [ ] ✓ Sin errores en logs
- [ ] ✓ Primera compra exitosa

### Post-Lanzamiento (Primera Hora)
- [ ] 📊 Dashboard de monitoreo activo
- [ ] 👁️ Logs monitoreados
- [ ] 📞 Equipo en standby
- [ ] 📱 Alertas configuradas

---

## 🚨 Criterios de ROLLBACK Inmediato

Ejecutar rollback SI:
- ❌ Uptime < 95% en primera hora
- ❌ Checkout no funcional (> 3 reportes)
- ❌ Pasarela de pagos fallando
- ❌ Pérdida de datos
- ❌ Brecha de seguridad

---

## 📞 Contactos de Emergencia

### Equipo Técnico
```
Líder Técnico:     [Nombre] - [Tel] - [Email]
DevOps:            [Nombre] - [Tel] - [Email]
Backend Dev:       [Nombre] - [Tel] - [Email]
```

### Proveedores Críticos
```
Hosting:           [Proveedor] - [Soporte 24/7]
Pagos:             [Proveedor] - [Soporte]
Odoo Partner:      [Proveedor] - [Soporte]
```

---

## 🔧 Comandos Útiles

### Verificar Estado
```bash
# Validación automática
./scripts/validate-pre-launch.sh https://tu-sitio.com

# Check manual de sitio
curl -I https://tu-sitio.com

# Ver logs en tiempo real (Odoo)
tail -f /var/log/odoo/odoo-server.log
```

### Backup Rápido
```bash
# Backup de base de datos
pg_dump nombre_bd > backup_pre_golive_$(date +%Y%m%d_%H%M).sql

# Backup de archivos
tar -czf backup_files_$(date +%Y%m%d_%H%M).tar.gz /ruta/odoo/filestore
```

### Rollback Rápido
```bash
# 1. Activar modo mantenimiento
# 2. Restaurar DB desde backup
psql nombre_bd < backup_pre_golive_YYYYMMDD_HHMM.sql

# 3. Restaurar archivos
tar -xzf backup_files_YYYYMMDD_HHMM.tar.gz -C /

# 4. Reiniciar servicios
sudo systemctl restart odoo
sudo systemctl restart nginx

# 5. Desactivar modo mantenimiento
```

---

## 📊 URLs de Monitoreo

### Herramientas
```
Uptime Monitor:     https://...
Dashboard Métricas: https://...
Error Tracking:     https://...
Analytics:          https://...
```

### Páginas a Vigilar
```
✓ Home:           /
✓ Shop:           /shop
✓ Producto:       /shop/product/[sample]
✓ Carrito:        /shop/cart
✓ Checkout:       /shop/checkout
```

---

## 🎯 Métricas Objetivo (Primeras 24h)

| Métrica | Objetivo |
|---------|----------|
| **Uptime** | > 99.5% |
| **Tiempo Respuesta** | < 2s |
| **Errores 5xx** | 0 |
| **Tasa Conversión** | > X% |
| **Tickets Críticos** | 0 |

---

## 📱 Protocolo de Comunicación

### Canal Principal
- **Slack/Teams**: #golive-ferreteria
- **Updates cada**: 1h (primeras 6h), luego cada 4h

### Template de Update
```
🕐 [HH:MM] - Update Go-Live

✅ Estado: Operativo / Con incidencias / Crítico
📊 Uptime: XX.XX%
⚡ Rendimiento: XXXms
💰 Órdenes: XX
🐛 Incidencias: XX (X críticas)

Próximo update: [HH:MM]
```

### Escalamiento
```
Nivel 1: Developer en turno
Nivel 2: Líder Técnico
Nivel 3: CTO/Gerencia
```

---

## ✅ Criterios de Éxito

### Lanzamiento Exitoso
- ✓ Sitio online sin interrupciones
- ✓ Primera compra completada
- ✓ No errores críticos en logs
- ✓ Equipo reporta sin incidencias

### Transición a Operación Normal
- ✓ 72h de monitoreo completados
- ✓ Uptime > 99.5%
- ✓ Todas las incidencias cerradas
- ✓ Reporte de estabilización aprobado

---

## 📚 Documentos de Referencia

- **Checklist Completo**: [docs/GO-LIVE-CHECKLIST.md](GO-LIVE-CHECKLIST.md)
- **Dashboard 72h**: [docs/MONITORING-DASHBOARD-72H.md](MONITORING-DASHBOARD-72H.md)
- **Guía Detallada**: [docs/10-go-live-y-monitoreo.md](10-go-live-y-monitoreo.md)

---

## 💡 Tips del Día del Lanzamiento

1. **Mantén la calma** - Has preparado todo, confía en tu checklist
2. **Comunica constantemente** - Updates regulares al equipo
3. **Documenta todo** - Anota cualquier incidencia o decisión
4. **No hagas cambios no planeados** - Solo deploy lo acordado
5. **Equipo disponible** - Ten al equipo técnico en standby
6. **Celebra los hitos** - Primera compra, primera hora, etc.

---

**¡Éxito en el lanzamiento! 🚀**
