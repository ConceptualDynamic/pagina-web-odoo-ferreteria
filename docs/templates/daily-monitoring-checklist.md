# Checklist Diario de Monitoreo Post-Lanzamiento

**Fecha:** _______________  
**Día del monitoreo:** ___ / 3 (72h)  
**Responsable:** _______________  
**Turno:** ☐ Mañana  ☐ Tarde  ☐ Noche

---

## 1. Verificación de disponibilidad

| Hora | Endpoint | Status HTTP | Tiempo respuesta | ✓ |
|------|----------|-------------|------------------|---|
| __:__ | Home (/) | ___ | ___s | ☐ |
| __:__ | Shop (/shop) | ___ | ___s | ☐ |
| __:__ | Producto ejemplo | ___ | ___s | ☐ |
| __:__ | Carrito (/shop/cart) | ___ | ___s | ☐ |
| __:__ | Checkout | ___ | ___s | ☐ |
| __:__ | Contacto | ___ | ___s | ☐ |

**Uptime últimas 24h:** ____%  
**Incidencias de disponibilidad:** ☐ Ninguna  ☐ Ver detalles abajo

---

## 2. Revisión de logs

### 2.1 Odoo logs
```
Comando: tail -n 100 /var/log/odoo/odoo-server.log | grep -i "error"
```

| Hora revisión | Errores nuevos | Severidad | Acción tomada | ✓ |
|---------------|----------------|-----------|---------------|---|
| __:__ | ___ | Baja/Media/Alta | ___ | ☐ |

**Errores críticos:** ☐ Ninguno  ☐ Ver sección de incidencias

### 2.2 Web server logs
```
Comando: grep " 5[0-9][0-9] " /var/log/nginx/access.log | tail -20
```

| Hora revisión | Errores 5xx | Páginas afectadas | ✓ |
|---------------|-------------|-------------------|---|
| __:__ | ___ | ___ | ☐ |

---

## 3. Métricas de negocio (Google Analytics)

### 3.1 Tráfico actual
- **Usuarios activos ahora:** ___
- **Sesiones hoy:** ___
- **Páginas vistas hoy:** ___
- **Tasa de rebote:** ___%

### 3.2 Conversión
- **Carritos creados:** ___
- **Checkouts iniciados:** ___
- **Transacciones completadas:** ___
- **Tasa de conversión:** ___%
- **Ticket promedio:** $___

### 3.3 Verificación de eventos
☐ `page_view` registrándose  
☐ `view_item` funcionando  
☐ `add_to_cart` funcionando  
☐ `begin_checkout` funcionando  
☐ `purchase` funcionando  

---

## 4. Estado de integraciones

| Integración | Status | Última verificación | Observaciones | ✓ |
|-------------|--------|---------------------|---------------|---|
| Google Analytics 4 | ☐ OK ☐ Falla | __:__ | ___ | ☐ |
| CRM | ☐ OK ☐ Falla | __:__ | ___ | ☐ |
| Pasarela de pago | ☐ OK ☐ Falla | __:__ | ___ | ☐ |
| WhatsApp/Chat | ☐ OK ☐ Falla | __:__ | ___ | ☐ |
| Email transaccional | ☐ OK ☐ Falla | __:__ | ___ | ☐ |

---

## 5. Recursos del servidor

### 5.1 Uso de recursos
```
Comandos:
- CPU: top -b -n 1 | grep odoo
- RAM: free -h
- Disco: df -h
```

| Recurso | Uso actual | Threshold | Status | ✓ |
|---------|------------|-----------|--------|---|
| CPU | __% | < 80% | ☐ OK ☐ ⚠️ | ☐ |
| RAM | __% | < 85% | ☐ OK ☐ ⚠️ | ☐ |
| Disco | __% | < 90% | ☐ OK ☐ ⚠️ | ☐ |

### 5.2 Base de datos
```
Comando: sudo -u postgres psql -c "SELECT count(*) FROM pg_stat_activity;"
```

- **Conexiones activas:** ___
- **Queries lentas (>5s):** ___

☐ Todo normal  
☐ Requiere atención (ver detalles)

---

## 6. Pruebas funcionales spot-check

### 6.1 Usuario visitante
☐ Home carga correctamente  
☐ Búsqueda funciona  
☐ Filtros en catálogo funcionan  
☐ Producto se puede ver  
☐ Agregar al carrito funciona  

### 6.2 Proceso de compra (hasta checkout)
☐ Carrito muestra productos  
☐ Actualizar cantidad funciona  
☐ Eliminar producto funciona  
☐ Checkout inicia correctamente  
☐ Formulario de datos funciona  

**Nota:** No completar compra real, solo verificar hasta antes de pago

### 6.3 Formularios
☐ Contacto envía correctamente  
☐ Newsletter suscribe  
☐ Cotización funciona  

---

## 7. Feedback de usuarios

### 7.1 Canales revisados
☐ Emails de soporte  
☐ WhatsApp/Chat  
☐ Redes sociales  
☐ Teléfono  

### 7.2 Resumen
- **Mensajes recibidos:** ___
- **Quejas:** ___
- **Consultas:** ___
- **Elogios:** ___

### 7.3 Problemas reportados por usuarios
1. _________________________________
2. _________________________________
3. _________________________________

---

## 8. Incidencias del turno

| # | Hora | Severidad | Descripción | Acción tomada | Estado | ✓ |
|---|------|-----------|-------------|---------------|--------|---|
| 1 | __:__ | 1/2/3/4 | ___ | ___ | Abierta/Resuelta | ☐ |
| 2 | __:__ | 1/2/3/4 | ___ | ___ | Abierta/Resuelta | ☐ |
| 3 | __:__ | 1/2/3/4 | ___ | ___ | Abierta/Resuelta | ☐ |

**Incidencias críticas (Sev 1) que requieren escalamiento:**  
☐ Ninguna  
☐ Ver incidencia #___ - **Escalado a:** _______________

---

## 9. Acciones realizadas

### 9.1 Mantenimiento preventivo
- [ ] _________________________________
- [ ] _________________________________

### 9.2 Optimizaciones
- [ ] _________________________________
- [ ] _________________________________

### 9.3 Configuraciones ajustadas
- [ ] _________________________________
- [ ] _________________________________

---

## 10. Alertas recibidas

| Hora | Sistema | Tipo de alerta | Acción | ✓ |
|------|---------|----------------|--------|---|
| __:__ | ___ | ___ | ___ | ☐ |
| __:__ | ___ | ___ | ___ | ☐ |

☐ Sin alertas en este turno

---

## 11. Tareas pendientes para próximo turno

### Prioridad Alta
1. _________________________________
2. _________________________________
3. _________________________________

### Prioridad Media
1. _________________________________
2. _________________________________

### Seguimiento requerido
- [ ] _________________________________
- [ ] _________________________________

---

## 12. Observaciones generales

_____________________________________________________________________________

_____________________________________________________________________________

_____________________________________________________________________________

_____________________________________________________________________________

---

## 13. Sign-off del turno

**Responsable:** ___________________________  
**Firma:** ___________________________  
**Hora de finalización:** ___:___  

**Estado general del sistema:**  
☐ Estable - Sin problemas  
☐ Estable - Con observaciones menores  
☐ Inestable - Requiere atención  
☐ Crítico - Problemas graves activos  

**Próximo responsable notificado:** ☐ Sí  ☐ No  
**Documentación actualizada:** ☐ Sí  ☐ No  

---

## Anexo: Comandos rápidos de referencia

```bash
# Health check
curl -I https://tu-dominio.com/

# Últimos errores Odoo
tail -n 50 /var/log/odoo/odoo-server.log | grep ERROR

# Errores nginx
grep " 5[0-9][0-9] " /var/log/nginx/access.log | tail -20

# Uso de recursos
top -b -n 1 | head -20
free -h
df -h

# Conexiones DB
sudo -u postgres psql -c "SELECT count(*) FROM pg_stat_activity;"

# Reiniciar Odoo (¡solo si es necesario!)
sudo systemctl restart odoo
sudo systemctl status odoo
```
