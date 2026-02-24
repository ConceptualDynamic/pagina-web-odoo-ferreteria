# Guía de Monitoreo Técnico

Esta guía complementa `10-go-live-y-monitoreo.md` con detalles técnicos específicos para el monitoreo de la plataforma Odoo.

## 1. Health checks y endpoints

### 1.1 Endpoints a monitorear

#### Endpoint principal (Home)
```
GET https://[tu-dominio]/
Esperado: HTTP 200
Tiempo respuesta: < 2s
```

#### Endpoint de catálogo
```
GET https://[tu-dominio]/shop
Esperado: HTTP 200
Verificar: Productos cargando correctamente
```

#### Endpoint de API (si aplica)
```
GET https://[tu-dominio]/api/health
Esperado: HTTP 200, JSON con status: "ok"
```

#### Búsqueda
```
GET https://[tu-dominio]/shop?search=herramienta
Esperado: HTTP 200
Verificar: Resultados de búsqueda
```

### 1.2 Health check script

Crear un script simple para verificar endpoints críticos:

```bash
#!/bin/bash
# health-check.sh

DOMAIN="https://tu-dominio.com"
ENDPOINTS=("/" "/shop" "/contactus")

echo "=== Health Check $(date) ==="

for endpoint in "${ENDPOINTS[@]}"; do
    URL="${DOMAIN}${endpoint}"
    HTTP_CODE=$(curl -o /dev/null -s -w "%{http_code}" -m 10 "$URL")
    RESPONSE_TIME=$(curl -o /dev/null -s -w "%{time_total}" -m 10 "$URL")
    
    if [ "$HTTP_CODE" -eq 200 ]; then
        echo "✅ $endpoint: OK (${HTTP_CODE}) - ${RESPONSE_TIME}s"
    else
        echo "❌ $endpoint: FAILED (${HTTP_CODE}) - ${RESPONSE_TIME}s"
    fi
done
```

### 1.3 Configuración de uptime monitors

**UptimeRobot (gratuito):**
1. Crear cuenta en uptimerobot.com
2. Agregar monitores HTTP(s) para:
   - Home: `https://[dominio]/`
   - Shop: `https://[dominio]/shop`
   - Checkout: `https://[dominio]/shop/checkout`
3. Configurar intervalo: 5 minutos
4. Alertas a: Email, SMS, Slack

**Configuración de alerta:**
- Enviar alerta después de: 2 fallos consecutivos
- Canales: Email + Slack/WhatsApp

## 2. Monitoreo de logs

### 2.1 Logs de Odoo

#### Ubicación típica:
```
/var/log/odoo/odoo-server.log
```

#### Revisar errores:
```bash
# Últimos 100 errores
tail -n 100 /var/log/odoo/odoo-server.log | grep -i "error"

# Errores en las últimas 24h
grep -i "error" /var/log/odoo/odoo-server.log | grep "$(date -d '1 day ago' '+%Y-%m-%d')"

# Monitoreo en tiempo real
tail -f /var/log/odoo/odoo-server.log | grep -i "error\|warning\|critical"
```

#### Patrones a buscar:
- `ERROR`: Errores de aplicación
- `WARNING`: Advertencias que pueden escalar
- `CRITICAL`: Problemas críticos
- `psycopg2`: Errores de base de datos
- `MemoryError`: Problemas de memoria
- `Traceback`: Stack traces de excepciones

### 2.2 Logs del servidor web

#### Nginx:
```bash
# Access log
tail -f /var/log/nginx/access.log

# Error log
tail -f /var/log/nginx/error.log

# Códigos de error 5xx
grep " 5[0-9][0-9] " /var/log/nginx/access.log
```

#### Apache:
```bash
# Access log
tail -f /var/log/apache2/access.log

# Error log
tail -f /var/log/apache2/error.log
```

### 2.3 Análisis de logs

#### Errores más frecuentes:
```bash
grep -i "error" /var/log/odoo/odoo-server.log | \
  awk '{print $NF}' | sort | uniq -c | sort -nr | head -20
```

#### Páginas con más errores 404:
```bash
grep " 404 " /var/log/nginx/access.log | \
  awk '{print $7}' | sort | uniq -c | sort -nr | head -20
```

#### IPs con más requests:
```bash
awk '{print $1}' /var/log/nginx/access.log | \
  sort | uniq -c | sort -nr | head -20
```

## 3. Monitoreo de base de datos

### 3.1 Conexiones PostgreSQL

```bash
# Ver conexiones activas
sudo -u postgres psql -c "SELECT count(*) FROM pg_stat_activity;"

# Ver queries lentas (>5s)
sudo -u postgres psql -c "
  SELECT pid, now() - pg_stat_activity.query_start AS duration, query 
  FROM pg_stat_activity 
  WHERE (now() - pg_stat_activity.query_start) > interval '5 seconds'
  AND state = 'active';
"
```

### 3.2 Tamaño de base de datos

```bash
# Tamaño total
sudo -u postgres psql -c "
  SELECT pg_database.datname, 
         pg_size_pretty(pg_database_size(pg_database.datname)) AS size
  FROM pg_database 
  ORDER BY pg_database_size(pg_database.datname) DESC;
"

# Tablas más grandes
sudo -u postgres psql -d [nombre_db] -c "
  SELECT relname, pg_size_pretty(pg_total_relation_size(relid))
  FROM pg_catalog.pg_statio_user_tables 
  ORDER BY pg_total_relation_size(relid) DESC 
  LIMIT 10;
"
```

## 4. Monitoreo de recursos del sistema

### 4.1 Uso de CPU y memoria

```bash
# Procesos de Odoo
ps aux | grep odoo

# Uso de CPU
top -b -n 1 | grep odoo

# Uso de memoria
free -h
```

### 4.2 Espacio en disco

```bash
# Espacio disponible
df -h

# Archivos grandes
du -sh /* | sort -h

# Archivos en directorio de Odoo
du -sh /opt/odoo/* | sort -h
```

### 4.3 Alertas automáticas

Crear script de monitoreo de recursos:

```bash
#!/bin/bash
# resource-monitor.sh

CPU_THRESHOLD=80
MEM_THRESHOLD=85
DISK_THRESHOLD=90

# CPU
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
if (( $(echo "$CPU_USAGE > $CPU_THRESHOLD" | bc -l) )); then
    echo "⚠️ CPU usage high: ${CPU_USAGE}%"
fi

# Memory
MEM_USAGE=$(free | grep Mem | awk '{print ($3/$2) * 100.0}')
if (( $(echo "$MEM_USAGE > $MEM_THRESHOLD" | bc -l) )); then
    echo "⚠️ Memory usage high: ${MEM_USAGE}%"
fi

# Disk
DISK_USAGE=$(df -h / | tail -1 | awk '{print $5}' | sed 's/%//')
if [ "$DISK_USAGE" -gt "$DISK_THRESHOLD" ]; then
    echo "⚠️ Disk usage high: ${DISK_USAGE}%"
fi
```

## 5. Monitoreo de Google Analytics 4

### 5.1 Verificación de eventos

En GA4 Realtime:
1. Abrir GA4 → Realtime
2. Verificar eventos:
   - `page_view`
   - `view_item` (ver producto)
   - `add_to_cart`
   - `begin_checkout`
   - `purchase`

### 5.2 Debug mode

Activar DebugView en GA4:
```javascript
// En consola del navegador
gtag('config', 'G-XXXXXXXXXX', {
  'debug_mode': true
});
```

### 5.3 Google Tag Assistant

1. Instalar extensión "Tag Assistant" de Chrome
2. Navegar el sitio
3. Verificar que tags se disparan correctamente

## 6. Monitoreo de rendimiento

### 6.1 Lighthouse CI

```bash
# Instalar
npm install -g @lhci/cli

# Ejecutar
lhci autorun --collect.url=https://tu-dominio.com/
```

### 6.2 WebPageTest

1. Ir a webpagetest.org
2. Ingresar URL
3. Seleccionar ubicación y dispositivo
4. Ejecutar test
5. Revisar métricas: TTFB, FCP, LCP, CLS

### 6.3 Google PageSpeed Insights

```bash
# Via API
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://tu-dominio.com/&strategy=mobile"
```

## 7. Configuración de alertas

### 7.1 Slack webhook

```bash
#!/bin/bash
# send-slack-alert.sh

WEBHOOK_URL="https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
MESSAGE="$1"

curl -X POST -H 'Content-type: application/json' \
  --data "{\"text\":\"🚨 Alerta: ${MESSAGE}\"}" \
  $WEBHOOK_URL
```

### 7.2 Email via SMTP

```bash
#!/bin/bash
# send-email-alert.sh

SUBJECT="Alerta del sistema"
MESSAGE="$1"
TO="admin@ejemplo.com"

echo "$MESSAGE" | mail -s "$SUBJECT" "$TO"
```

### 7.3 Cron jobs para monitoreo

```bash
# Editar crontab
crontab -e

# Agregar:
# Health check cada 5 minutos
*/5 * * * * /opt/scripts/health-check.sh >> /var/log/health-check.log 2>&1

# Resource monitor cada 15 minutos
*/15 * * * * /opt/scripts/resource-monitor.sh >> /var/log/resource-monitor.log 2>&1

# Log analysis cada hora
0 * * * * /opt/scripts/analyze-logs.sh >> /var/log/log-analysis.log 2>&1
```

## 8. Dashboard recomendado

### 8.1 Métricas en tiempo real

Crear un dashboard simple con:
- **Status**: Verde/Amarillo/Rojo
- **Uptime**: Porcentaje últimas 24h
- **Response time**: Promedio última hora
- **Error rate**: Errores/minuto
- **Active users**: GA4 realtime
- **Server resources**: CPU, RAM, Disk

### 8.2 Herramientas de dashboard

**Opción 1: Grafana**
- Open source
- Integra con múltiples fuentes
- Alertas configurables

**Opción 2: Datadog**
- SaaS, plan gratuito disponible
- Fácil de configurar
- APM incluido

**Opción 3: Dashboard personalizado**
- Simple HTML + JavaScript
- Consume APIs de uptime monitors
- Autorefresco cada minuto

## 9. Checklist de verificación diaria

Durante las 72h post-lanzamiento:

### Mañana (9:00 AM)
- [ ] Revisar uptime de últimas 12h
- [ ] Verificar logs de errores
- [ ] Comprobar backups
- [ ] Revisar GA4 realtime
- [ ] Verificar transacciones completadas

### Mediodía (1:00 PM)
- [ ] Revisar alertas recibidas
- [ ] Verificar espacio en disco
- [ ] Comprobar carga del servidor
- [ ] Revisar quejas de usuarios

### Tarde (6:00 PM)
- [ ] Consolidar métricas del día
- [ ] Documentar incidencias
- [ ] Planificar acciones para mañana
- [ ] Verificar status de integraciones

### Noche (11:00 PM)
- [ ] Review final del día
- [ ] Configurar alertas para la noche
- [ ] Backup de logs del día

## 10. Contactos de emergencia

Mantener lista actualizada:

| Rol | Nombre | Teléfono | Email | Disponibilidad |
|-----|--------|----------|-------|----------------|
| Tech Lead | [NOMBRE] | [TEL] | [EMAIL] | 24/7 |
| DevOps | [NOMBRE] | [TEL] | [EMAIL] | 24/7 |
| Backend Dev | [NOMBRE] | [TEL] | [EMAIL] | 8am-10pm |
| Hosting Provider | [NOMBRE] | [TEL] | [EMAIL] | 24/7 |
| Payment Gateway | [SOPORTE] | [TEL] | [EMAIL] | 24/7 |

---

**Nota:** Ajustar rutas, dominios y comandos según la configuración específica del servidor y la instalación de Odoo.
