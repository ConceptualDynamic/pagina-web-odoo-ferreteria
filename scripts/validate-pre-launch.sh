#!/bin/bash

###############################################################################
# Script de Validación Pre-Launch - Ferretería Odoo
# 
# Este script realiza validaciones básicas antes del go-live
# Uso: ./validate-pre-launch.sh <URL_SITIO>
#
# Ejemplo: ./validate-pre-launch.sh https://miferreteria.com
###############################################################################

set -e

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Contadores
PASSED=0
FAILED=0
WARNINGS=0

# Función para imprimir encabezados
print_header() {
    echo -e "\n${BLUE}═══════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}  $1${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════${NC}\n"
}

# Función para checks exitosos
print_pass() {
    echo -e "${GREEN}✓${NC} $1"
    ((PASSED++))
}

# Función para checks fallidos
print_fail() {
    echo -e "${RED}✗${NC} $1"
    ((FAILED++))
}

# Función para advertencias
print_warn() {
    echo -e "${YELLOW}⚠${NC} $1"
    ((WARNINGS++))
}

# Verificar argumentos
if [ $# -eq 0 ]; then
    echo -e "${RED}Error: Debe proporcionar la URL del sitio${NC}"
    echo "Uso: $0 <URL_SITIO>"
    echo "Ejemplo: $0 https://miferreteria.com"
    exit 1
fi

SITE_URL=$1

# Remover trailing slash si existe
SITE_URL=${SITE_URL%/}

echo -e "${BLUE}"
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║         VALIDACIÓN PRE-LAUNCH - FERRETERÍA ODOO           ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo "URL del sitio: $SITE_URL"
echo "Fecha: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

###############################################################################
# 1. VALIDACIÓN DE CONECTIVIDAD Y HTTPS
###############################################################################

print_header "1. CONECTIVIDAD Y HTTPS"

# Check si el sitio está accesible
if curl -s -o /dev/null -w "%{http_code}" "$SITE_URL" | grep -q "200\|301\|302"; then
    print_pass "Sitio accesible"
else
    print_fail "Sitio no accesible o retorna código de error"
fi

# Check HTTPS
if [[ $SITE_URL == https://* ]]; then
    print_pass "URL usa HTTPS"
    
    # Verificar certificado SSL
    if echo | openssl s_client -servername "${SITE_URL#https://}" -connect "${SITE_URL#https://}:443" 2>/dev/null | grep -q "Verify return code: 0"; then
        print_pass "Certificado SSL válido"
    else
        print_fail "Certificado SSL inválido o con problemas"
    fi
else
    print_fail "URL no usa HTTPS"
fi

# Check redirección HTTP a HTTPS
HTTP_URL=$(echo "$SITE_URL" | sed 's/https/http/')
REDIRECT=$(curl -s -o /dev/null -w "%{redirect_url}" "$HTTP_URL")
if [[ $REDIRECT == https://* ]]; then
    print_pass "Redirección HTTP → HTTPS configurada"
else
    print_warn "No hay redirección automática de HTTP a HTTPS"
fi

###############################################################################
# 2. VALIDACIÓN DE PÁGINAS CRÍTICAS
###############################################################################

print_header "2. PÁGINAS CRÍTICAS"

# Lista de páginas a validar
declare -A PAGES=(
    ["Home"]="/"
    ["Catálogo o Shop"]="/shop"
    ["Contacto"]="/contactus"
    ["Términos y Condiciones"]="/terms"
    ["Política de Privacidad"]="/privacy"
)

for page_name in "${!PAGES[@]}"; do
    page_url="${SITE_URL}${PAGES[$page_name]}"
    http_code=$(curl -s -o /dev/null -w "%{http_code}" "$page_url")
    
    if [ "$http_code" == "200" ]; then
        print_pass "$page_name accesible (HTTP $http_code)"
    elif [ "$http_code" == "301" ] || [ "$http_code" == "302" ]; then
        print_warn "$page_name redirige (HTTP $http_code)"
    else
        print_fail "$page_name no accesible (HTTP $http_code)"
    fi
done

###############################################################################
# 3. VALIDACIÓN DE RENDIMIENTO
###############################################################################

print_header "3. RENDIMIENTO"

# Tiempo de carga de la home page
load_time=$(curl -s -o /dev/null -w "%{time_total}" "$SITE_URL")
load_time_ms=$(echo "$load_time * 1000" | bc)
load_time_int=${load_time_ms%.*}

if [ "$load_time_int" -lt 2000 ]; then
    print_pass "Tiempo de carga de Home: ${load_time}s (< 2s) ⚡"
elif [ "$load_time_int" -lt 3000 ]; then
    print_warn "Tiempo de carga de Home: ${load_time}s (2-3s)"
else
    print_fail "Tiempo de carga de Home: ${load_time}s (> 3s) - Muy lento"
fi

# Time to first byte
ttfb=$(curl -s -o /dev/null -w "%{time_starttransfer}" "$SITE_URL")
ttfb_ms=$(echo "$ttfb * 1000" | bc)
ttfb_int=${ttfb_ms%.*}

if [ "$ttfb_int" -lt 500 ]; then
    print_pass "TTFB (Time to First Byte): ${ttfb}s (< 0.5s)"
elif [ "$ttfb_int" -lt 1000 ]; then
    print_warn "TTFB (Time to First Byte): ${ttfb}s (0.5-1s)"
else
    print_fail "TTFB (Time to First Byte): ${ttfb}s (> 1s)"
fi

###############################################################################
# 4. VALIDACIÓN DE HEADERS DE SEGURIDAD
###############################################################################

print_header "4. HEADERS DE SEGURIDAD"

# Obtener headers
HEADERS=$(curl -s -I "$SITE_URL")

# Strict-Transport-Security
if echo "$HEADERS" | grep -qi "Strict-Transport-Security"; then
    print_pass "Header Strict-Transport-Security presente"
else
    print_warn "Header Strict-Transport-Security ausente"
fi

# X-Frame-Options
if echo "$HEADERS" | grep -qi "X-Frame-Options"; then
    print_pass "Header X-Frame-Options presente"
else
    print_warn "Header X-Frame-Options ausente"
fi

# X-Content-Type-Options
if echo "$HEADERS" | grep -qi "X-Content-Type-Options"; then
    print_pass "Header X-Content-Type-Options presente"
else
    print_warn "Header X-Content-Type-Options ausente"
fi

# Content-Security-Policy
if echo "$HEADERS" | grep -qi "Content-Security-Policy"; then
    print_pass "Header Content-Security-Policy presente"
else
    print_warn "Header Content-Security-Policy ausente"
fi

###############################################################################
# 5. VALIDACIÓN SEO BÁSICO
###############################################################################

print_header "5. SEO BÁSICO"

# Descargar home page
HOME_HTML=$(curl -s "$SITE_URL")

# Verificar título
if echo "$HOME_HTML" | grep -q "<title>"; then
    TITLE=$(echo "$HOME_HTML" | grep -oP '(?<=<title>).*?(?=</title>)' | head -1)
    if [ -n "$TITLE" ] && [ "$TITLE" != "Home" ] && [ "$TITLE" != "Odoo" ]; then
        print_pass "Título personalizado presente: '$TITLE'"
    else
        print_warn "Título genérico o por defecto"
    fi
else
    print_fail "Tag <title> no encontrado"
fi

# Verificar meta description
if echo "$HOME_HTML" | grep -qi 'meta name="description"'; then
    print_pass "Meta description presente"
else
    print_warn "Meta description ausente"
fi

# Verificar meta viewport (responsive)
if echo "$HOME_HTML" | grep -qi 'meta name="viewport"'; then
    print_pass "Meta viewport presente (responsive)"
else
    print_warn "Meta viewport ausente"
fi

# Verificar robots.txt
if curl -s -o /dev/null -w "%{http_code}" "$SITE_URL/robots.txt" | grep -q "200"; then
    print_pass "robots.txt accesible"
else
    print_warn "robots.txt no encontrado"
fi

# Verificar sitemap.xml
if curl -s -o /dev/null -w "%{http_code}" "$SITE_URL/sitemap.xml" | grep -q "200"; then
    print_pass "sitemap.xml accesible"
else
    print_warn "sitemap.xml no encontrado"
fi

###############################################################################
# 6. VALIDACIÓN DE CONTENIDO MIXTO
###############################################################################

print_header "6. CONTENIDO MIXTO"

# Buscar recursos cargados por HTTP en página HTTPS
if [[ $SITE_URL == https://* ]]; then
    MIXED_CONTENT=$(echo "$HOME_HTML" | grep -o 'http://[^"]*' | head -5)
    
    if [ -z "$MIXED_CONTENT" ]; then
        print_pass "No se detectó contenido mixto (HTTP en HTTPS)"
    else
        print_fail "Contenido mixto detectado:"
        echo "$MIXED_CONTENT" | while read -r url; do
            echo "    → $url"
        done
    fi
fi

###############################################################################
# RESUMEN FINAL
###############################################################################

echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"
echo -e "${BLUE}                  RESUMEN FINAL${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"
echo ""

TOTAL=$((PASSED + FAILED + WARNINGS))

echo -e "  ${GREEN}Validaciones exitosas:${NC} $PASSED"
echo -e "  ${YELLOW}Advertencias:${NC} $WARNINGS"
echo -e "  ${RED}Validaciones fallidas:${NC} $FAILED"
echo -e "  ${BLUE}Total de checks:${NC} $TOTAL"
echo ""

# Calcular porcentaje de éxito
if [ $TOTAL -gt 0 ]; then
    SUCCESS_RATE=$((PASSED * 100 / TOTAL))
    echo -e "  ${BLUE}Tasa de éxito:${NC} ${SUCCESS_RATE}%"
    echo ""
fi

# Recomendación final
if [ $FAILED -eq 0 ] && [ $WARNINGS -lt 3 ]; then
    echo -e "${GREEN}╔═══════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║  ✓ SITIO LISTO PARA GO-LIVE                          ║${NC}"
    echo -e "${GREEN}╚═══════════════════════════════════════════════════════╝${NC}"
    exit 0
elif [ $FAILED -eq 0 ]; then
    echo -e "${YELLOW}╔═══════════════════════════════════════════════════════╗${NC}"
    echo -e "${YELLOW}║  ⚠ SITIO ACEPTABLE PARA GO-LIVE                      ║${NC}"
    echo -e "${YELLOW}║    Revisar advertencias antes de lanzar              ║${NC}"
    echo -e "${YELLOW}╚═══════════════════════════════════════════════════════╝${NC}"
    exit 0
else
    echo -e "${RED}╔═══════════════════════════════════════════════════════╗${NC}"
    echo -e "${RED}║  ✗ SITIO NO LISTO PARA GO-LIVE                        ║${NC}"
    echo -e "${RED}║    Corregir errores críticos antes de lanzar         ║${NC}"
    echo -e "${RED}╚═══════════════════════════════════════════════════════╝${NC}"
    exit 1
fi
