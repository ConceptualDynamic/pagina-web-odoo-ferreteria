# Pagos, envíos e impuestos

## 1) Objetivo
Habilitar una operación de compra robusta, sin ambigüedades de precio, entrega o fiscalidad.

## 2) Pagos
### Configuración mínima
- Método principal (pasarela online).
- Método alterno (transferencia/contraentrega si aplica).
- Estados de pago claros (pendiente, aprobado, rechazado).

### Controles
- Validar moneda y redondeos.
- Manejo de reintentos y errores de pago.
- Notificaciones de confirmación al cliente.

## 3) Envíos y retiro
- Modalidades: envío a domicilio y retiro en tienda (si aplica).
- Reglas por zona geográfica y peso/volumen.
- SLA de entrega visible antes de pagar.
- Costos de envío transparentes en carrito/checkout.

## 4) Impuestos y reglas de precios
- Definir impuestos por tipo de producto/región.
- Verificar cálculo en carrito y orden final.
- Validar escenarios con y sin exenciones (si aplica).

## 5) Casos críticos a probar (E2E)
1. Compra normal con pago aprobado.
2. Pago rechazado y recuperación del carrito.
3. Envío vs retiro con costos distintos.
4. Producto con impuesto diferencial.
5. Cupón/descuento (si existe) + cálculo final correcto.

## 6) Criterios de aceptación
- Totales consistentes en todas las etapas.
- Confirmación de orden y pago trazables.
- Reglas de envío/impuestos sin discrepancias.

## 7) Riesgos y mitigación
- Descuadres por redondeo → pruebas con múltiples combinaciones.
- Fallas en webhook de pasarela → reintento + alertas.
- Reglas fiscales incompletas → validación previa con responsable contable.
