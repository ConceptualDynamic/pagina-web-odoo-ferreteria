# Pagos, envíos e impuestos
Configuración de métodos de pago, envío/retiro y reglas fiscales/precios.
Prueba end-to-end obligatoria antes de go-live.

## 1. Métodos de pago

### 1.1 Proveedores de pago recomendados para ferretería
- **Tarjetas de crédito/débito**: MercadoPago, Stripe, PayU (según región)
- **Transferencia bancaria**: Configuración manual con validación post-pago
- **Pago en tienda**: Para retiro en sucursal
- **PSE** (Colombia): Pagos bancarios en línea

### 1.2 Configuración en Odoo
```
Ventas → Configuración → Métodos de pago
```

#### 1.2.1 Tarjetas de crédito/débito
- **Módulo**: `payment_mercadopago` o `payment_stripe`
- **Configuración**:
  - API Keys (sandbox y producción)
  - Moneda por defecto
  - País de operación
  - Comisiones y fees
  - Mensajes de confirmación personalizados

#### 1.2.2 Transferencia bancaria
- **Módulo**: `payment_transfer`
- **Configuración**:
  - Datos bancarios de la ferretería
  - Instrucciones de pago
  - Tiempo de espera para validación (24-48h)
  - Estados de pedido (pendiente de pago → pagado)

#### 1.2.3 Pago en tienda
- **Módulo**: Personalización custom
- **Flujo**:
  1. Cliente selecciona "Pago en tienda"
  2. Pedido se crea con estado "pendiente de pago"
  3. Cliente recibe código de pedido
  4. Cliente paga en sucursal y presenta código
  5. Staff marca pedido como pagado

### 1.3 Validaciones y seguridad
- **Tokenización**: Nunca almacenar datos de tarjetas en Odoo
- **PCI DSS**: Usar proveedores certificados
- **3D Secure**: Activar autenticación adicional
- **Fraud detection**: Revisar pedidos sospechosos
- **Webhooks**: Configurar notificaciones de estado de pago

## 2. Métodos de envío

### 2.1 Opciones de envío
- **Retiro en tienda**: Sin costo, cliente recoge en sucursal
- **Envío estándar**: 3-5 días hábiles
- **Envío express**: 1-2 días hábiles (para productos urgentes)
- **Envío a obra**: Para pedidos grandes a sitios de construcción

### 2.2 Configuración en Odoo
```
Inventario → Configuración → Métodos de envío
```

#### 2.2.1 Retiro en tienda
- **Módulo**: Nativo Odoo + personalización
- **Configuración**:
  - Almacén de origen
  - Horarios de retiro
  - Tiempo de preparación (ej: 2 horas)
  - Instrucciones de retiro
  - Notificación cuando está listo

#### 2.2.2 Integración con transportistas
- **Opciones**: Coordinadora, Servientrega, Inter Rapidísimo (Colombia)
- **Módulo**: `delivery_fedex`, `delivery_ups` o custom
- **Configuración**:
  - Credenciales de API
  - Tabla de tarifas por peso/volumen
  - Zonas de cobertura
  - Embalaje y dimensiones
  - Tracking automático

### 2.3 Cálculo de costos de envío
```python
# Reglas basadas en:
- Peso total del pedido
- Volumen de productos
- Zona geográfica (ciudad, departamento)
- Valor del pedido (envío gratis > $X)
- Tipo de producto (materiales peligrosos, frágiles)
```

### 2.4 Restricciones y reglas
- **Productos pesados**: Solo retiro en tienda o envío a obra
- **Productos peligrosos**: Restricciones de transportista
- **Zonas remotas**: Costos adicionales o no disponible
- **Mínimo de compra**: Para envío gratis o disponibilidad

## 3. Impuestos y precios

### 3.1 Configuración fiscal
```
Contabilidad → Configuración → Posiciones fiscales
```

#### 3.1.1 IVA (Colombia como ejemplo)
- **IVA General**: 19% (mayoría de productos)
- **IVA Reducido**: 5% (algunos productos específicos)
- **IVA Exento**: 0% (ciertos materiales)
- **IVA Excluido**: Productos no sujetos

#### 3.1.2 Retención en la fuente
- **Personas naturales**: No aplica (compras minoristas)
- **Personas jurídicas**: Configurar según régimen
- **Grandes contribuyentes**: Retención automática

### 3.2 Precios y descuentos

#### 3.2.1 Estrategia de precios
- **Precio base**: Costo + margen
- **Precio público**: Incluye IVA
- **Precio mayorista**: Descuento por volumen
- **Precio B2B**: Precios especiales para empresas

#### 3.2.2 Descuentos programados
```
Ventas → Productos → Listas de precios
```
- **Descuentos por volumen**: Escala según cantidad
- **Descuentos por categoría**: Ofertas en familia de productos
- **Descuentos temporales**: Campañas promocionales
- **Cupones**: Códigos de descuento personalizados

### 3.3 Redondeos y visualización
- **Redondeo**: A centavos o múltiplos de 10/50/100
- **Formato**: Símbolo de moneda según región
- **Desglose**: Subtotal + impuestos + envío = Total

## 4. Flujo de checkout E2E

### 4.1 Pasos del checkout
```
1. Carrito de compras → Ver resumen
2. Información de contacto → Email, teléfono
3. Dirección de envío → Autocompletar, validar
4. Método de envío → Calcular costos
5. Método de pago → Seleccionar y procesar
6. Confirmación → Número de pedido, instrucciones
7. Seguimiento → Estado del pedido
```

### 4.2 Optimizaciones UX
- **Guest checkout**: Comprar sin registro (opcional)
- **Autocompletado**: Direcciones, datos personales
- **Validación en tiempo real**: Formularios
- **Indicador de progreso**: Pasos del checkout
- **Recuperación de carrito**: Email automático
- **One-click checkout**: Para clientes recurrentes

### 4.3 Casos especiales

#### 4.3.1 Productos con disponibilidad mixta
- Algunos en stock → Envío inmediato
- Otros bajo pedido → Envío cuando estén todos listos
- Opción: Enviar en múltiples entregas

#### 4.3.2 Validaciones pre-checkout
- **Stock disponible**: Verificar antes de procesar
- **Límites de compra**: Por producto o categoría
- **Restricciones geográficas**: Productos no enviables
- **Mínimo de compra**: Para ciertos métodos de pago

## 5. Integración técnica

### 5.1 Módulos Odoo requeridos
```
- website_sale: Tienda online base
- payment_*: Proveedores de pago
- delivery: Métodos de envío
- sale_management: Gestión de pedidos
- stock: Inventario
- account: Contabilidad e impuestos
```

### 5.2 Personalizaciones custom
```python
# Crear módulo: ferreteria_checkout
__manifest__.py
models/
  - sale_order.py (validaciones)
  - delivery_carrier.py (cálculos custom)
  - payment_transaction.py (lógica de pago)
views/
  - checkout_template.xml
  - payment_form.xml
controllers/
  - checkout_controller.py
static/
  - checkout.js (validaciones frontend)
  - checkout.css
```

### 5.3 APIs y webhooks
- **Payment provider webhooks**: Estados de transacción
- **Shipping API**: Tracking y tarifas
- **Tax API**: Consulta de tasas actualizadas
- **Email notifications**: Confirmaciones y actualizaciones

## 6. Testing E2E

### 6.1 Escenarios de prueba obligatorios

#### 6.1.1 Checkout exitoso
- [ ] Compra con tarjeta de crédito → Pago aprobado
- [ ] Compra con transferencia → Instrucciones recibidas
- [ ] Compra con retiro en tienda → Confirmación correcta

#### 6.1.2 Casos de error
- [ ] Tarjeta rechazada → Mensaje claro, permitir reintentar
- [ ] Stock insuficiente → Notificar antes de pago
- [ ] Zona sin cobertura → Ofrecer alternativas
- [ ] Timeout de pago → Recuperar sesión

#### 6.1.3 Cálculos correctos
- [ ] Subtotal de productos
- [ ] Descuentos aplicados correctamente
- [ ] Impuestos según posición fiscal
- [ ] Costo de envío según destino
- [ ] Total final correcto

#### 6.1.4 Emails y notificaciones
- [ ] Confirmación de pedido
- [ ] Instrucciones de pago (si aplica)
- [ ] Actualización de estado
- [ ] Tracking de envío
- [ ] Pedido listo para retiro

### 6.2 Herramientas de testing
- **Odoo test suite**: Unit tests para modelos
- **Selenium/Playwright**: Tests E2E automatizados
- **Postman/cURL**: Tests de API
- **Sandbox de pagos**: Ambiente de prueba sin cobros reales

### 6.3 Checklist pre-go-live
- [ ] Credenciales de producción configuradas
- [ ] SSL/HTTPS activo en todo el checkout
- [ ] Logs de error monitoreados
- [ ] Respaldos automáticos habilitados
- [ ] Plan de rollback definido
- [ ] Soporte técnico disponible
- [ ] Documentación para staff completada

## 7. Monitoreo post-lanzamiento

### 7.1 Métricas clave
- **Tasa de abandono de carrito**: Por paso del checkout
- **Tasa de aprobación de pagos**: Por método
- **Tiempo de checkout**: Promedio desde carrito hasta confirmación
- **Errores técnicos**: Logs de fallos de pago/envío
- **Customer satisfaction**: Feedback post-compra

### 7.2 Optimización continua
- Analizar puntos de fricción en checkout
- Mejorar mensajes de error
- Ajustar costos de envío según datos reales
- Añadir nuevos métodos de pago según demanda
- Optimizar velocidad de carga del checkout

## 8. Documentación para operaciones

### 8.1 Manual de usuario interno
- Cómo procesar un pedido manualmente
- Cómo validar un pago por transferencia
- Cómo modificar un pedido en curso
- Cómo procesar una devolución/reembolso
- Cómo manejar excepciones de envío

### 8.2 FAQs para clientes
- Métodos de pago aceptados
- Tiempos de entrega por zona
- Costos de envío
- Política de devoluciones
- Cómo hacer seguimiento del pedido
- Contacto para soporte

## Anexos

### A. Ejemplo de configuración de pago
```xml
<!-- payment_mercadopago configuration -->
<record id="payment_provider_mercadopago" model="payment.provider">
    <field name="name">MercadoPago</field>
    <field name="code">mercadopago</field>
    <field name="state">enabled</field>
    <field name="company_id" ref="base.main_company"/>
    <field name="mercadopago_access_token">ACCESS_TOKEN</field>
    <field name="fees_active">True</field>
    <field name="fees_dom_var">2.5</field>
</record>
```

### B. Ejemplo de método de envío
```xml
<!-- Delivery method configuration -->
<record id="delivery_retiro_tienda" model="delivery.carrier">
    <field name="name">Retiro en tienda</field>
    <field name="delivery_type">fixed</field>
    <field name="fixed_price">0.0</field>
    <field name="product_id" ref="product_product_delivery"/>
</record>
```

### C. Ejemplo de posición fiscal
```xml
<!-- Tax configuration -->
<record id="fiscal_position_colombia" model="account.fiscal.position">
    <field name="name">Colombia</field>
    <field name="country_id" ref="base.co"/>
    <field name="auto_apply">True</field>
</record>
```
