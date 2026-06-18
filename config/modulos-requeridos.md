# Módulos Odoo Requeridos - Ferretería Web

Este archivo documenta los módulos de Odoo que deben estar instalados y configurados para el funcionamiento completo del sitio web de ferretería.

## Módulos Core (Obligatorios)

### 1. Website (website)
**Estado**: ⚠️ Pendiente de instalación  
**Versión**: 17.0  
**Dependencias**: base, web  
**Propósito**: Plataforma base para el sitio web

**Configuración requerida**:
- Nombre del sitio: "Ferretería [Nombre]"
- Dominio: [A configurar]
- Idioma: Español (es_CO o es_MX)
- Tema: Default Odoo Website Theme

**Validación**:
```bash
# Verificar instalación
sudo -u odoo odoo shell -d ferreteria_db << EOF
env['ir.module.module'].search([('name', '=', 'website'), ('state', '=', 'installed')])
EOF
```

### 2. eCommerce (website_sale)
**Estado**: ⚠️ Pendiente de instalación  
**Versión**: 17.0  
**Dependencias**: website, sale, payment  
**Propósito**: Tienda en línea y carrito de compras

**Configuración requerida**:
- Catálogo de productos habilitado
- Carrito de compras habilitado
- Checkout simplificado
- Términos y condiciones configurados

**Validación**:
```bash
# Verificar instalación
sudo -u odoo odoo shell -d ferreteria_db << EOF
env['ir.module.module'].search([('name', '=', 'website_sale'), ('state', '=', 'installed')])
EOF
```

### 3. Inventory (stock)
**Estado**: ⚠️ Pendiente de instalación  
**Versión**: 17.0  
**Dependencias**: product, base  
**Propósito**: Gestión de inventario y almacenes

**Configuración requerida**:
- Almacén principal configurado
- Ubicaciones de stock definidas
- Reglas de reabastecimiento
- Trazabilidad habilitada

**Validación**:
```bash
# Verificar instalación y configuración de almacén
sudo -u odoo odoo shell -d ferreteria_db << EOF
env['stock.warehouse'].search([])
EOF
```

### 4. Sales (sale)
**Estado**: ⚠️ Pendiente de instalación  
**Versión**: 17.0  
**Dependencias**: product, base  
**Propósito**: Gestión de ventas y cotizaciones

**Configuración requerida**:
- Equipo de ventas "Ventas Web" creado
- Términos de pago configurados
- Lista de precios configurada
- Secuencia de órdenes configurada

**Validación**:
```bash
# Verificar instalación y equipo de ventas
sudo -u odoo odoo shell -d ferreteria_db << EOF
env['crm.team'].search([('name', '=', 'Ventas Web')])
EOF
```

### 5. CRM (crm)
**Estado**: ⚠️ Pendiente de instalación  
**Versión**: 17.0  
**Dependencias**: sales_team, mail  
**Propósito**: Gestión de leads y oportunidades

**Configuración requerida**:
- Pipeline de ventas configurado
- Etapas de oportunidades definidas
- Formularios web conectados
- Reglas de asignación automática

**Validación**:
```bash
# Verificar instalación y pipeline
sudo -u odoo odoo shell -d ferreteria_db << EOF
env['crm.stage'].search([])
EOF
```

## Módulos Complementarios (Recomendados)

### 6. Website Blog (website_blog)
**Estado**: 🔵 Opcional  
**Propósito**: Blog corporativo para contenido y SEO

### 7. Website Wishlist (website_sale_wishlist)
**Estado**: 🔵 Opcional  
**Propósito**: Lista de deseos de clientes

### 8. Delivery Methods (website_sale_delivery)
**Estado**: 🟡 Recomendado  
**Propósito**: Métodos de envío en checkout

### 9. Payment Providers (payment)
**Estado**: 🔴 Obligatorio para producción  
**Propósito**: Integración con pasarelas de pago

### 10. Contacts (contacts)
**Estado**: ✅ Incluido con base  
**Propósito**: Gestión de contactos y clientes

### 11. Product (product)
**Estado**: ✅ Incluido con sale/stock  
**Propósito**: Gestión de productos

## Checklist de Instalación

```
[ ] 1. Verificar versión de Odoo (17.0)
[ ] 2. Instalar módulo Website
[ ] 3. Instalar módulo Sales
[ ] 4. Instalar módulo CRM
[ ] 5. Instalar módulo Inventory
[ ] 6. Instalar módulo eCommerce
[ ] 7. Verificar dependencias instaladas
[ ] 8. Configurar Website básico
[ ] 9. Configurar catálogo eCommerce
[ ] 10. Configurar almacén principal
[ ] 11. Configurar equipo de ventas
[ ] 12. Configurar pipeline CRM
[ ] 13. Ejecutar tests de validación
[ ] 14. Documentar credenciales y accesos
```

## Script de Instalación Automática

```bash
#!/bin/bash
# install-modules.sh
# Script para instalar todos los módulos requeridos

DB_NAME="ferreteria_db"
ODOO_USER="odoo"
MODULES="website,website_sale,stock,sale,crm"

echo "Instalando módulos core de Odoo para ferretería..."
echo "Base de datos: $DB_NAME"
echo "Módulos: $MODULES"

# Instalar módulos
sudo -u $ODOO_USER odoo -d $DB_NAME -i $MODULES --stop-after-init --logfile=/tmp/odoo-install.log

# Verificar instalación
echo ""
echo "Verificando instalación de módulos..."
sudo -u $ODOO_USER odoo shell -d $DB_NAME << 'EOF'
import odoo
env = odoo.api.Environment.manage()
modules_to_check = ['website', 'website_sale', 'stock', 'sale', 'crm']
with env.cursor() as cr:
    env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
    for module_name in modules_to_check:
        module = env['ir.module.module'].search([('name', '=', module_name)])
        if module:
            status = "✅ Instalado" if module.state == 'installed' else "❌ No instalado"
            print(f"{module_name}: {status} (Estado: {module.state})")
        else:
            print(f"{module_name}: ❌ Módulo no encontrado")
EOF

echo ""
echo "Instalación completada. Revisar /tmp/odoo-install.log para detalles."
```

## Orden de Instalación Recomendado

Es importante instalar los módulos en el siguiente orden para evitar conflictos de dependencias:

1. **Base y Web** (ya instalados por defecto)
2. **Product** (se instala automáticamente con sale/stock)
3. **Sales Management (sale)** - Base para eCommerce
4. **CRM (crm)** - Gestión de leads
5. **Inventory (stock)** - Control de stock
6. **Website (website)** - Plataforma web
7. **eCommerce (website_sale)** - Tienda en línea (instala automáticamente payment)

## Post-Instalación

Después de instalar los módulos, realizar las siguientes configuraciones:

### 1. Configuración de Empresa
```
Settings > General Settings > Company Information
- Nombre: [Nombre de la ferretería]
- Dirección completa
- Teléfono
- Email
- Logo corporativo
```

### 2. Configuración de Website
```
Website > Configuration > Settings
- Domain: [dominio.com]
- Default Language: Spanish
- Homepage: Configurar página de inicio
```

### 3. Configuración de eCommerce
```
Website > eShop > Products
- Crear categorías principales
- Configurar atributos de producto
- Configurar variantes (color, tamaño, etc.)
```

### 4. Configuración de Inventory
```
Inventory > Configuration > Warehouses
- Almacén Principal
- Ubicaciones de stock
- Rutas de entrega
```

### 5. Configuración de Sales
```
Sales > Configuration
- Payment Terms
- Price Lists
- Sales Teams
```

### 6. Configuración de CRM
```
CRM > Configuration
- Sales Teams
- Lead Stages
- Lead Assignment Rules
```

## Tests de Validación

Ejecutar los siguientes tests manuales para validar la instalación:

### Test 1: Website Básico
```
1. Acceder a http://[servidor]:8069
2. Verificar que se muestra la página de inicio
3. Acceder al editor de páginas
4. Crear una página de prueba
5. Publicar la página
```

### Test 2: eCommerce
```
1. Ir a Shop
2. Ver listado de productos
3. Agregar un producto al carrito
4. Proceder al checkout
5. Verificar proceso hasta confirmación
```

### Test 3: Inventory
```
1. Ir a Inventory
2. Crear un producto nuevo con stock
3. Verificar movimientos de inventario
4. Realizar ajuste de inventario
```

### Test 4: Sales
```
1. Ir a Sales
2. Crear una cotización
3. Confirmar orden de venta
4. Ver en reportes
```

### Test 5: CRM
```
1. Ir a CRM
2. Crear una oportunidad
3. Moverla a través del pipeline
4. Convertir a cliente
```

## Solución de Problemas

### Error: Módulo no encontrado
```bash
# Actualizar lista de módulos
sudo -u odoo odoo -d ferreteria_db -u base --stop-after-init
```

### Error: Dependencias faltantes
```bash
# Verificar dependencias
sudo -u odoo odoo shell -d ferreteria_db << EOF
env['ir.module.module'].search([('name', '=', 'nombre_modulo')]).dependencies_id
EOF
```

### Error en instalación
```bash
# Ver logs detallados
tail -f /var/log/odoo/odoo-server.log | grep ERROR
```

## Referencias

- [Documentación oficial Odoo 17](https://www.odoo.com/documentation/17.0/)
- [Módulo Website](https://www.odoo.com/documentation/17.0/applications/websites/website.html)
- [Módulo eCommerce](https://www.odoo.com/documentation/17.0/applications/websites/ecommerce.html)
- [Módulo Inventory](https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory.html)
- [Módulo Sales](https://www.odoo.com/documentation/17.0/applications/sales/sales.html)
- [Módulo CRM](https://www.odoo.com/documentation/17.0/applications/sales/crm.html)

## Estado Actual

**Última actualización**: 2026-02-24  
**Estado general**: ⚠️ Pendiente de instalación  
**Responsable**: Equipo técnico  
**Próxima revisión**: Post-instalación

## Notas

- Todos los módulos deben estar en versión 17.0
- Verificar compatibilidad antes de actualizar
- Mantener backup antes de cambios mayores
- Documentar todas las personalizaciones
