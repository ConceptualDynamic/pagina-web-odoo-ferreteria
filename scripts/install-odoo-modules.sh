#!/bin/bash
# ==================================================
# Script de Instalación de Módulos Odoo
# Ferretería Web - Fase 1
# ==================================================
# 
# Este script instala y valida los módulos core de Odoo
# requeridos para el sitio web de ferretería.
#
# Uso:
#   sudo ./install-odoo-modules.sh [db_name] [odoo_user]
#
# Ejemplo:
#   sudo ./install-odoo-modules.sh ferreteria_db odoo
#

set -e

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuración
DB_NAME="${1:-ferreteria_db}"
ODOO_USER="${2:-odoo}"
MODULES="website,website_sale,stock,sale,crm"
LOG_FILE="/tmp/odoo-install-$(date +%Y%m%d-%H%M%S).log"

# Funciones de ayuda
print_header() {
    echo -e "${BLUE}================================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}================================================${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Banner
print_header "Instalación de Módulos Odoo - Ferretería Web"
echo ""
print_info "Base de datos: $DB_NAME"
print_info "Usuario Odoo: $ODOO_USER"
print_info "Módulos: $MODULES"
print_info "Log file: $LOG_FILE"
echo ""

# Verificar si se está ejecutando como root
if [ "$EUID" -ne 0 ]; then 
    print_error "Este script debe ejecutarse como root o con sudo"
    exit 1
fi

# Verificar si Odoo está instalado
print_header "1. Verificando instalación de Odoo"
if ! command -v odoo &> /dev/null; then
    print_error "Odoo no está instalado en el sistema"
    print_info "Por favor, instalar Odoo antes de ejecutar este script"
    exit 1
fi
print_success "Odoo encontrado"

# Verificar versión de Odoo
ODOO_VERSION=$(sudo -u $ODOO_USER odoo --version 2>&1 | head -n 1)
print_info "Versión: $ODOO_VERSION"

# Verificar si la base de datos existe
print_header "2. Verificando base de datos"
if sudo -u postgres psql -lqt | cut -d \| -f 1 | grep -qw $DB_NAME; then
    print_success "Base de datos '$DB_NAME' encontrada"
else
    print_error "Base de datos '$DB_NAME' no existe"
    print_info "Crear la base de datos con: sudo -u postgres createdb $DB_NAME"
    exit 1
fi

# Verificar conexión a la base de datos
if sudo -u postgres psql -d $DB_NAME -c "SELECT 1" &> /dev/null; then
    print_success "Conexión a base de datos exitosa"
else
    print_error "No se puede conectar a la base de datos"
    exit 1
fi

# Instalar módulos
print_header "3. Instalando módulos core"
print_info "Esto puede tomar varios minutos..."
echo ""

if sudo -u $ODOO_USER odoo -d $DB_NAME -i $MODULES --stop-after-init --logfile=$LOG_FILE 2>&1; then
    print_success "Instalación completada"
else
    print_error "Error durante la instalación"
    print_info "Revisar el log: $LOG_FILE"
    exit 1
fi

# Verificar instalación de módulos
print_header "4. Verificando módulos instalados"
echo ""

VERIFICATION_SCRIPT=$(cat << 'EOF'
import sys
modules_to_check = ['website', 'website_sale', 'stock', 'sale', 'crm']
env = self.env
all_ok = True
for module_name in modules_to_check:
    module = env['ir.module.module'].search([('name', '=', module_name)])
    if module and module.state == 'installed':
        print(f"✅ {module_name}: Instalado")
    else:
        state = module.state if module else "no encontrado"
        print(f"❌ {module_name}: {state}")
        all_ok = False
sys.exit(0 if all_ok else 1)
EOF
)

if echo "$VERIFICATION_SCRIPT" | sudo -u $ODOO_USER odoo shell -d $DB_NAME 2>&1 | grep -E "✅|❌"; then
    print_success "Verificación completada"
else
    print_warning "Algunos módulos pueden no estar instalados correctamente"
fi

echo ""

# Resumen final
print_header "5. Resumen de Instalación"
echo ""
print_info "Fecha: $(date)"
print_info "Base de datos: $DB_NAME"
print_info "Log completo: $LOG_FILE"
echo ""

# Mostrar errores si hay
if grep -i "error\|exception" $LOG_FILE > /dev/null 2>&1; then
    print_warning "Se encontraron errores en el log. Revisar:"
    print_info "grep -i error $LOG_FILE"
    echo ""
fi

print_success "Instalación finalizada"
echo ""
print_info "Próximos pasos:"
echo "  1. Acceder a http://[servidor]:8069"
echo "  2. Iniciar sesión como administrador"
echo "  3. Verificar que todos los módulos estén activos"
echo "  4. Completar configuración inicial de cada módulo"
echo "  5. Ejecutar checklist de validación: config/checklist-validacion.md"
echo ""

# Mostrar acceso web
print_header "Acceso al Sistema"
echo ""
print_info "URL: http://localhost:8069 (o IP del servidor)"
print_info "Base de datos: $DB_NAME"
echo ""

exit 0
