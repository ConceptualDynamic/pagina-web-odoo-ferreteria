# Integraciones

## 1) Objetivo
Conectar el sitio con analítica, captura comercial y operación para tomar decisiones basadas en datos.

## 2) Integraciones prioritarias MVP
- GA4 (medición web).
- Canal de contacto (WhatsApp/chat/formulario).
- CRM (registro y seguimiento de leads).

## 3) Eventos críticos (analítica)
- `view_item` (ver producto)
- `add_to_cart`
- `begin_checkout`
- `purchase`
- `generate_lead` (contacto/cotización)

## 4) Diseño de trazabilidad
- IDs de sesión/usuario (según privacidad).
- Relación lead ↔ fuente ↔ campaña.
- UTM preservadas en navegación y formularios.

## 5) Validación funcional de integraciones
- Evento dispara una sola vez en acción esperada.
- Datos llegan con parámetros mínimos correctos.
- Formulario/contacto crea registro consumible por comercial.

## 6) Riesgos frecuentes
- Eventos duplicados por mala instrumentación.
- Pérdida de UTMs entre páginas.
- Leads sin owner definido en CRM.

## 7) Mitigación
- Matriz de eventos con responsable por evento.
- QA de tracking en staging antes de producción.
- Alertas semanales de anomalías (caídas de eventos/leads).
