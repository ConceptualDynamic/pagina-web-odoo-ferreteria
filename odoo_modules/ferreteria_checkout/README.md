# Módulo Ferretería Checkout

Módulo personalizado de Odoo para el proceso de checkout de la ferretería online.

## Descripción

Este módulo extiende la funcionalidad estándar de `website_sale` de Odoo para proporcionar un proceso de checkout adaptado a las necesidades de una ferretería, incluyendo:

- Validación de stock en tiempo real
- Campos personalizados (tipo de cliente, documento de identidad)
- Método de pago "Pago en tienda"
- Sistema de cupones de descuento
- Restricciones de envío basadas en peso y tipo de producto
- Emails de confirmación personalizados
- Múltiples métodos de envío con cálculo dinámico

## Características principales

### 1. Tipos de cliente
- Persona Natural
- Empresa

### 2. Métodos de pago
- **Pago en tienda**: Sin costo, pago al recoger el pedido
- **Transferencia bancaria**: Con instrucciones de pago
- **Tarjetas de crédito**: Integración con MercadoPago/Stripe (configuración adicional requerida)

### 3. Métodos de envío
- **Retiro en tienda**: Gratuito, preparación en 2 horas
- **Envío estándar**: 3-5 días, hasta 30kg
- **Envío express**: 1-2 días, hasta 15kg

### 4. Validaciones
- Stock disponible antes de checkout
- Productos pesados (>30kg) solo retiro en tienda
- Formato de documento de identidad
- Campos requeridos en formulario

### 5. Sistema de cupones
- Descuentos por código promocional
- Aplicación automática en el total

## Instalación

### Prerequisitos
- Odoo 16.0 o superior
- Módulos base: `website_sale`, `sale_management`, `stock`, `delivery`, `payment`, `account`

### Pasos de instalación

1. Copiar el módulo al directorio de addons de Odoo:
```bash
cp -r ferreteria_checkout /path/to/odoo/addons/
```

2. Actualizar la lista de módulos:
```bash
odoo-bin -c /etc/odoo/odoo.conf -d ferreteria -u all
```

3. Instalar el módulo desde la interfaz de Odoo:
```
Apps → Buscar "Ferretería Checkout" → Instalar
```

## Configuración

### 1. Configurar datos de la empresa
```
Ajustes → Empresas → Mi empresa
```
- Completar dirección física
- Teléfonos de contacto
- Email de notificaciones

### 2. Configurar métodos de pago

#### Transferencia bancaria
```
Website → Configuración → Métodos de pago → Transferencia bancaria
```
- Activar
- Agregar instrucciones con datos bancarios

#### Pago en tienda
Ya viene configurado con el módulo. Revisar en:
```
Website → Configuración → Métodos de pago → Pago en tienda
```

### 3. Configurar impuestos
```
Contabilidad → Configuración → Impuestos
```
- Crear impuestos según legislación local (ej: IVA 19%)
- Asignar impuestos a productos

### 4. Verificar métodos de envío
Los métodos vienen preconfigurados:
```
Inventario → Configuración → Métodos de envío
```
- Retiro en tienda
- Envío estándar (basado en peso)
- Envío express (basado en peso)

Ajustar precios y reglas según necesidad.

## Uso

### Para clientes

1. **Agregar productos al carrito**
2. **Ir al checkout**
   - Seleccionar tipo de cliente
   - Ingresar documento de identidad
   - Completar información de contacto y envío
3. **Aplicar cupón** (opcional)
4. **Seleccionar método de envío**
5. **Seleccionar método de pago**
6. **Confirmar pedido**
7. **Recibir email de confirmación**

### Para administradores

#### Ver pedidos
```
Ventas → Pedidos → Pedidos
```

#### Procesar pago en tienda
1. Cliente llega a tienda con número de pedido
2. Buscar pedido en sistema
3. Procesar pago
4. Marcar como pagado
5. Entregar productos

#### Gestionar cupones
Los cupones están hardcoded en el modelo. Para producción, implementar modelo de cupones completo.

Códigos de ejemplo:
- `FERRETERIA10`: 10% de descuento
- `FERRETERIA20`: 20% de descuento

## Estructura del módulo

```
ferreteria_checkout/
├── __init__.py
├── __manifest__.py
├── controllers/
│   ├── __init__.py
│   └── checkout_controller.py
├── models/
│   ├── __init__.py
│   ├── sale_order.py
│   ├── payment_provider.py
│   ├── delivery_carrier.py
│   └── product_template.py
├── views/
│   ├── checkout_templates.xml
│   ├── payment_templates.xml
│   ├── sale_order_views.xml
│   └── product_template_views.xml
├── data/
│   ├── email_templates.xml
│   ├── payment_provider_data.xml
│   └── delivery_carrier_data.xml
├── static/
│   └── src/
│       ├── js/
│       │   └── checkout_validation.js
│       └── css/
│           └── checkout.css
├── security/
│   └── ir.model.access.csv
└── tests/
    └── (tests to be implemented)
```

## Personalización

### Agregar nuevo método de pago

1. Extender modelo `payment.provider`:
```python
class PaymentProvider(models.Model):
    _inherit = 'payment.provider'
    
    code = fields.Selection(
        selection_add=[('nuevo_metodo', 'Nuevo método')],
        ondelete={'nuevo_metodo': 'set default'}
    )
```

2. Crear template de vista
3. Implementar controlador de procesamiento

### Modificar cálculo de envío

Editar método en `delivery_carrier.py`:
```python
def _get_price_available(self, order):
    # Lógica personalizada
    pass
```

### Cambiar validación de stock

Editar método en `sale_order.py`:
```python
def _check_stock_availability(self):
    # Nueva lógica
    pass
```

## Testing

### Tests unitarios
```bash
odoo-bin -c /etc/odoo/odoo.conf -d ferreteria --test-enable --stop-after-init -i ferreteria_checkout
```

### Tests E2E
Ejecutar con Selenium/Playwright según documentación en `docs/06.1-implementacion-checkout.md`

## Solución de problemas

### Error: "Stock insuficiente"
- Verificar cantidad disponible en producto
- Actualizar inventario
- Revisar movimientos de stock pendientes

### Error: "Método de pago no disponible"
- Verificar que el método esté habilitado
- Revisar configuración de país
- Verificar credenciales de API (si aplica)

### Email no se envía
- Verificar configuración de servidor SMTP en Odoo
- Revisar logs de Odoo
- Verificar template de email existe

## Contribuir

Para contribuir al módulo:
1. Fork del repositorio
2. Crear branch con feature
3. Implementar cambios
4. Agregar tests
5. Crear Pull Request

## Licencia

LGPL-3

## Soporte

Para soporte:
- GitHub Issues: https://github.com/ConceptualDynamic/pagina-web-odoo-ferreteria/issues
- Email: support@ferreteria.com

## Changelog

### v16.0.1.0.0 (2024-02-24)
- Release inicial
- Checkout personalizado
- Métodos de pago y envío
- Sistema de cupones
- Validaciones de stock
- Emails personalizados
