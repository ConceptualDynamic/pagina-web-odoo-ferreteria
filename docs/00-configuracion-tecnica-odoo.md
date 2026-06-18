# Configuración Técnica Odoo

## Descripción
Este documento define la configuración técnica base para la instancia de Odoo que soportará la página web de ferretería.

## Requisitos de Sistema

### Versión de Odoo
- **Versión recomendada**: Odoo 17 (última versión estable)
- **Edición**: Odoo Enterprise o Community (según licenciamiento)

### Requisitos de Servidor
- **Sistema Operativo**: Ubuntu 22.04 LTS o superior
- **Python**: 3.10 o superior
- **PostgreSQL**: 14 o superior
- **Memoria RAM**: Mínimo 4GB (recomendado 8GB para producción)
- **Almacenamiento**: Mínimo 20GB disponibles
- **Procesador**: 2+ cores recomendado

## Módulos Requeridos

### Módulos Core (Obligatorios)

#### 1. Website (`website`)
- **Propósito**: Construcción y gestión del sitio web
- **Características clave**:
  - Editor visual de páginas
  - Gestión de menús y navegación
  - Bloques de construcción (snippets)
  - SEO básico
  - Formularios de contacto

#### 2. eCommerce (`website_sale`)
- **Propósito**: Tienda en línea y carrito de compras
- **Características clave**:
  - Catálogo de productos en línea
  - Carrito de compras
  - Checkout y proceso de pago
  - Gestión de órdenes en línea
  - Variantes de producto
  - Promociones y cupones

#### 3. Inventory (`stock`)
- **Propósito**: Gestión de inventario y almacenes
- **Características clave**:
  - Control de stock
  - Múltiples almacenes
  - Trazabilidad de productos
  - Gestión de ubicaciones
  - Reglas de reabastecimiento

#### 4. Sales (`sale`)
- **Propósito**: Gestión de ventas y cotizaciones
- **Características clave**:
  - Cotizaciones y órdenes de venta
  - Gestión de clientes
  - Equipos de ventas
  - Reportes de ventas
  - Integración con inventario

#### 5. CRM (`crm`)
- **Propósito**: Gestión de relaciones con clientes
- **Características clave**:
  - Pipeline de oportunidades
  - Gestión de leads
  - Actividades y seguimiento
  - Reportes de conversión
  - Integración con formularios web

### Módulos Complementarios Recomendados

- `website_blog`: Blog corporativo
- `website_sale_wishlist`: Lista de deseos
- `website_sale_delivery`: Métodos de envío
- `payment`: Pasarelas de pago
- `contacts`: Gestión de contactos
- `product`: Gestión de productos

## Pasos de Instalación

### 1. Preparación del Entorno

```bash
# Actualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar dependencias
sudo apt install -y python3-pip python3-dev libxml2-dev libxslt1-dev \
  libldap2-dev libsasl2-dev libjpeg-dev zlib1g-dev libpq-dev

# Instalar PostgreSQL
sudo apt install -y postgresql postgresql-client

# Crear usuario de base de datos
sudo -u postgres createuser -s odoo
```

### 2. Instalación de Odoo

#### Opción A: Instalación desde Paquete (Recomendado para producción)
```bash
# Descargar e instalar Odoo
wget https://nightly.odoo.com/17.0/nightly/deb/odoo_17.0.latest_all.deb
sudo dpkg -i odoo_17.0.latest_all.deb
sudo apt-get install -f
```

#### Opción B: Instalación desde Código Fuente
```bash
# Clonar repositorio
git clone https://www.github.com/odoo/odoo --depth 1 --branch 17.0 /opt/odoo

# Instalar dependencias Python
pip3 install -r /opt/odoo/requirements.txt

# Crear usuario del sistema
sudo useradd -m -U -r -d /opt/odoo -s /bin/bash odoo
```

### 3. Configuración de Base de Datos

```bash
# Crear base de datos para la ferretería
sudo -u postgres createdb ferreteria_db

# Configurar permisos
sudo -u postgres psql -c "ALTER USER odoo WITH PASSWORD 'password_seguro';"
```

### 4. Configuración de Odoo

Crear archivo de configuración `/etc/odoo/odoo.conf`:

```ini
[options]
; Configuración básica
admin_passwd = admin_password_change_me
db_host = localhost
db_port = 5432
db_user = odoo
db_password = password_seguro
db_name = ferreteria_db

; Directorios
addons_path = /usr/lib/python3/dist-packages/odoo/addons
data_dir = /var/lib/odoo

; Servidor
http_port = 8069
xmlrpc_port = 8069

; Logging
logfile = /var/log/odoo/odoo-server.log
log_level = info

; Workers (para producción)
workers = 4
max_cron_threads = 2

; Límites
limit_time_cpu = 600
limit_time_real = 1200
limit_memory_hard = 2684354560
limit_memory_soft = 2147483648
```

### 5. Inicio de Odoo

```bash
# Iniciar servicio
sudo systemctl start odoo
sudo systemctl enable odoo

# Verificar estado
sudo systemctl status odoo

# Ver logs
sudo tail -f /var/log/odoo/odoo-server.log
```

## Activación de Módulos

### Acceso Inicial

1. Abrir navegador en `http://localhost:8069` (o la IP del servidor)
2. Crear base de datos si es necesario
3. Iniciar sesión como administrador

### Instalación de Módulos Core

#### Método 1: Desde la Interfaz Web

1. Ir a **Apps** en el menú principal
2. Buscar y hacer clic en "Install" para cada módulo:
   - Website
   - eCommerce
   - Inventory
   - Sales
   - CRM

#### Método 2: Línea de Comandos

```bash
# Instalar todos los módulos requeridos de una vez
sudo -u odoo odoo -d ferreteria_db -i website,website_sale,stock,sale,crm --stop-after-init
```

### Secuencia de Instalación Recomendada

1. **Sales Management** (`sale`) - Base para eCommerce
2. **CRM** (`crm`) - Gestión de leads
3. **Inventory** (`stock`) - Control de inventario
4. **Website** (`website`) - Plataforma web
5. **eCommerce** (`website_sale`) - Tienda en línea

## Validación del Entorno

### Checklist de Validación

- [ ] Odoo instalado y servicio activo
- [ ] Base de datos PostgreSQL creada y accesible
- [ ] Acceso web funcionando en puerto 8069
- [ ] Módulo Website instalado y configurado
- [ ] Módulo eCommerce instalado y configurado
- [ ] Módulo Inventory instalado y configurado
- [ ] Módulo Sales instalado y configurado
- [ ] Módulo CRM instalado y configurado
- [ ] Sin errores en logs del sistema
- [ ] Página de inicio accesible

### Comandos de Verificación

```bash
# Verificar servicio Odoo
sudo systemctl status odoo

# Verificar conexión a base de datos
sudo -u postgres psql -d ferreteria_db -c "SELECT version();"

# Verificar módulos instalados
sudo -u odoo odoo shell -d ferreteria_db -c /etc/odoo/odoo.conf << EOF
import odoo
env = odoo.api.Environment.manage()
with env.cursor() as cr:
    env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
    modules = env['ir.module.module'].search([
        ('name', 'in', ['website', 'website_sale', 'stock', 'sale', 'crm']),
        ('state', '=', 'installed')
    ])
    for module in modules:
        print(f"{module.name}: {module.state}")
EOF

# Verificar logs de errores
sudo grep -i error /var/log/odoo/odoo-server.log | tail -20
```

### Tests Funcionales Manuales

1. **Website**:
   - ✓ Acceder a la página de inicio
   - ✓ Editar una página con el editor visual
   - ✓ Publicar cambios

2. **eCommerce**:
   - ✓ Ver catálogo de productos
   - ✓ Agregar producto al carrito
   - ✓ Procesar checkout (modo test)

3. **Inventory**:
   - ✓ Crear un producto con stock
   - ✓ Ver movimientos de inventario
   - ✓ Configurar almacén

4. **Sales**:
   - ✓ Crear cotización
   - ✓ Confirmar orden de venta
   - ✓ Ver reporte de ventas

5. **CRM**:
   - ✓ Crear oportunidad
   - ✓ Mover en pipeline
   - ✓ Convertir a cliente

## Configuración Inicial Post-Instalación

### Datos de Empresa

1. Ir a **Settings > General Settings > Company Information**
2. Configurar:
   - Nombre de la empresa
   - Dirección
   - Teléfono
   - Email
   - Logo
   - Timezone: America/Bogota (o según ubicación)

### Configuración de Website

1. **Settings > Website > Configuration**
   - Nombre del sitio
   - Dominio
   - Idioma por defecto: Español
   - Favicon

2. **Website > Configuration > Settings**
   - Habilitar multi-idioma si es necesario
   - Configurar Google Analytics (opcional)
   - Configurar cookies policy

### Configuración de eCommerce

1. **Website > eShop > Products**
   - Crear categorías de productos
   - Configurar atributos (color, tamaño, etc.)

2. **Website > Configuration > Settings > Shop - Products**
   - Layout del catálogo
   - Configurar opciones de checkout

### Configuración de Inventory

1. **Inventory > Configuration > Warehouses**
   - Configurar almacén principal
   - Definir ubicaciones

2. **Inventory > Configuration > Settings**
   - Habilitar trazabilidad (si aplica)
   - Configurar rutas de entrega

### Configuración de Sales

1. **Sales > Configuration > Settings**
   - Términos y condiciones
   - Configurar equipos de ventas
   - Lista de precios

### Configuración de CRM

1. **CRM > Configuration > Sales Teams**
   - Crear equipo de ventas web
   - Definir pipeline de oportunidades

2. **CRM > Configuration > Lead Generation**
   - Configurar reglas de asignación

## Seguridad

### Recomendaciones de Seguridad

1. **Cambiar contraseña master de Odoo**
   ```ini
   admin_passwd = your_strong_password_here
   ```

2. **Configurar firewall**
   ```bash
   sudo ufw allow 22/tcp
   sudo ufw allow 80/tcp
   sudo ufw allow 443/tcp
   sudo ufw enable
   ```

3. **Configurar HTTPS con Let's Encrypt**
   ```bash
   sudo apt install certbot python3-certbot-nginx
   sudo certbot --nginx -d tudominio.com
   ```

4. **Limitar acceso a la base de datos**
   - Restringir conexiones PostgreSQL a localhost
   - Usar contraseñas fuertes

5. **Configurar proxy reverso (Nginx)**
   ```nginx
   server {
       listen 80;
       server_name tudominio.com;
       
       location / {
           proxy_pass http://localhost:8069;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

## Monitoreo

### Logs a Monitorear

- `/var/log/odoo/odoo-server.log` - Logs de aplicación
- `/var/log/postgresql/` - Logs de base de datos
- `/var/log/nginx/` - Logs de proxy (si aplica)

### Métricas Clave

- Uso de CPU y memoria
- Conexiones a base de datos
- Tiempo de respuesta del servidor
- Espacio en disco

## Respaldo

### Estrategia de Backup

```bash
# Backup de base de datos
sudo -u postgres pg_dump ferreteria_db > backup_$(date +%Y%m%d).sql

# Backup de filestore
tar -czf filestore_backup_$(date +%Y%m%d).tar.gz /var/lib/odoo/filestore/

# Automatizar con cron
# 0 2 * * * /path/to/backup-script.sh
```

## Soporte y Documentación

- **Documentación oficial**: https://www.odoo.com/documentation/17.0/
- **Foros de comunidad**: https://www.odoo.com/forum
- **GitHub Odoo**: https://github.com/odoo/odoo

## Criterio de Aceptación

✅ **Entorno funcional logrado cuando**:
- Todos los módulos core están instalados y activos
- No hay errores críticos en logs
- Se puede acceder a la interfaz web
- Cada módulo pasa sus tests funcionales básicos
- La configuración inicial está completa

## Próximos Pasos

Una vez completada la configuración técnica:
1. Proceder con [Fase 2] Arquitectura y navegación (#2)
2. Configurar estructura de datos (#4)
3. Iniciar carga de catálogo (#5)
