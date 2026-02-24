# Scripts de Validación y Automatización

Este directorio contiene scripts útiles para validar y automatizar tareas relacionadas con el go-live y mantenimiento del sitio.

## 📋 Scripts Disponibles

### validate-pre-launch.sh

Script de validación automática para ejecutar antes del go-live. Realiza checks básicos de conectividad, seguridad, rendimiento y SEO.

#### Requisitos
- `curl` - Para hacer peticiones HTTP
- `openssl` - Para validar certificados SSL
- `bc` - Para cálculos matemáticos
- `grep` - Para búsqueda de patrones
- `sed` - Para procesamiento de texto

**Nota**: Estos comandos están disponibles por defecto en la mayoría de sistemas Linux/Unix. En macOS, todos los comandos requeridos están preinstalados.

#### Uso

```bash
# Dar permisos de ejecución (solo primera vez)
chmod +x scripts/validate-pre-launch.sh

# Ejecutar validación
./scripts/validate-pre-launch.sh https://tu-sitio-odoo.com
```

#### Ejemplo de salida

```
╔═══════════════════════════════════════════════════════════╗
║         VALIDACIÓN PRE-LAUNCH - FERRETERÍA ODOO           ║
╚═══════════════════════════════════════════════════════════╝

URL del sitio: https://miferreteria.com
Fecha: 2026-02-24 15:30:45

═══════════════════════════════════════════════════
  1. CONECTIVIDAD Y HTTPS
═══════════════════════════════════════════════════

✓ Sitio accesible
✓ URL usa HTTPS
✓ Certificado SSL válido
✓ Redirección HTTP → HTTPS configurada

...

═══════════════════════════════════════════════════
                  RESUMEN FINAL
═══════════════════════════════════════════════════

  Validaciones exitosas: 18
  Advertencias: 3
  Validaciones fallidas: 0
  Total de checks: 21

  Tasa de éxito: 85%

╔═══════════════════════════════════════════════════════╗
║  ⚠ SITIO ACEPTABLE PARA GO-LIVE                      ║
║    Revisar advertencias antes de lanzar              ║
╚═══════════════════════════════════════════════════════╝
```

#### Validaciones Realizadas

1. **Conectividad y HTTPS**
   - Accesibilidad del sitio
   - Uso de HTTPS
   - Validez del certificado SSL
   - Redirección HTTP → HTTPS

2. **Páginas Críticas**
   - Home page
   - Catálogo/Shop
   - Contacto
   - Términos y Condiciones
   - Política de Privacidad

3. **Rendimiento**
   - Tiempo de carga de Home
   - Time to First Byte (TTFB)

4. **Headers de Seguridad**
   - Strict-Transport-Security
   - X-Frame-Options
   - X-Content-Type-Options
   - Content-Security-Policy

5. **SEO Básico**
   - Meta title personalizado
   - Meta description
   - Meta viewport (responsive)
   - robots.txt
   - sitemap.xml

6. **Contenido Mixto**
   - Detección de recursos HTTP en páginas HTTPS

#### Códigos de Salida

- `0` - Validación exitosa o aceptable (sin errores críticos)
- `1` - Validación fallida (hay errores críticos que deben corregirse)

#### Integración con CI/CD

Puedes integrar este script en tu pipeline de CI/CD:

```yaml
# Ejemplo para GitHub Actions
- name: Pre-launch validation
  run: |
    chmod +x scripts/validate-pre-launch.sh
    ./scripts/validate-pre-launch.sh https://staging.miferreteria.com
```

```yaml
# Ejemplo para GitLab CI
pre-launch-check:
  script:
    - chmod +x scripts/validate-pre-launch.sh
    - ./scripts/validate-pre-launch.sh https://staging.miferreteria.com
```

## 🔧 Desarrollo de Nuevos Scripts

Si necesitas agregar más scripts de validación o automatización:

1. Crear el script en este directorio
2. Hacerlo ejecutable: `chmod +x scripts/tu-script.sh`
3. Documentarlo en este README
4. Seguir las convenciones:
   - Usar bash como shell
   - Incluir encabezado con descripción y uso
   - Implementar manejo de errores (`set -e`)
   - Proporcionar mensajes claros de salida
   - Usar códigos de salida apropiados

## 📚 Documentación Relacionada

- [Go-Live Checklist](../docs/GO-LIVE-CHECKLIST.md)
- [Guía de Go-Live y Monitoreo](../docs/10-go-live-y-monitoreo.md)
- [Dashboard de Monitoreo 72h](../docs/MONITORING-DASHBOARD-72H.md)

## 🆘 Soporte

Si encuentras problemas con algún script:

1. Verifica que tienes todas las dependencias instaladas
2. Revisa los permisos de ejecución del script
3. Consulta la documentación completa en `docs/`
4. Abre un issue en el repositorio describiendo el problema
