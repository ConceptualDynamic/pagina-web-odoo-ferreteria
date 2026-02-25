# Go-live y monitoreo

## 1) Objetivo
Realizar lanzamiento controlado, con capacidad de reacción rápida durante la ventana crítica inicial.

## 2) Checklist pre-release
- DNS/SSL verificados.
- Backups y plan de rollback listos.
- Configuración de pagos/envíos/impuestos validada.
- Catálogo MVP publicado y revisado.
- Analítica y eventos críticos activos.
- Contacto/soporte operativo.

## 3) Plan de lanzamiento
- Ventana de despliegue definida (evitar horas pico).
- Roles en war-room (técnico, negocio, soporte).
- Comunicación interna de salida.

## 4) Monitoreo 72h
### Indicadores de salud
- Disponibilidad del sitio.
- Errores de checkout/pago.
- Tiempo de carga páginas clave.
- Volumen de pedidos y leads.

### Cadencia de revisión
- Día 1: seguimiento continuo.
- Día 2: cortes cada 4 horas.
- Día 3: cortes cada 8 horas.

## 5) Gestión de incidentes
- Clasificación S1–S4.
- Escalamiento inmediato de S1.
- Registro de causa raíz y acciones correctivas.

## 6) Cierre de estabilización
- Informe de 72h con:
  - métricas observadas,
  - incidentes y resolución,
  - backlog post-lanzamiento (quick wins + mejoras estructurales).
