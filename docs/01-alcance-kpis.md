# Alcance y KPIs

## 1. Objetivo del Sitio

### Objetivo Principal
Implementar un sitio web de comercio electrónico para ferretería, integrado con Odoo ERP, que permita a los clientes:
- Consultar catálogo de productos de ferretería (herramientas, materiales de construcción, suministros industriales)
- Realizar compras en línea de manera segura y eficiente
- Obtener información sobre productos, disponibilidad y precios en tiempo real
- Acceder a información de contacto y políticas de la empresa

### Objetivos Específicos
1. **Comercial**: Incrementar las ventas mediante un canal digital 24/7
2. **Operativo**: Automatizar el proceso de cotización y venta inicial
3. **Servicio**: Mejorar la experiencia del cliente con autoservicio digital
4. **Competitivo**: Posicionar la ferretería como una opción moderna y tecnológica

## 2. Alcance del MVP (Minimum Viable Product)

### 2.1. Páginas y Funcionalidades Core

#### Home (Página Principal)
- Hero section con mensaje principal y CTA
- Categorías destacadas de productos
- Productos destacados o en promoción
- Banner de beneficios (envío, garantía, servicio)
- Footer con enlaces rápidos

#### Catálogo de Productos
- **PLP (Product Listing Page)**:
  - Listado de productos por categoría
  - Filtros básicos (precio, marca, disponibilidad)
  - Ordenamiento (precio, nombre, relevancia)
  - Paginación
  - Vista de grid con imagen, nombre, precio y botón de compra
  
- **PDP (Product Detail Page)**:
  - Galería de imágenes del producto
  - Descripción detallada
  - Especificaciones técnicas
  - Precio y disponibilidad
  - Selector de cantidad
  - Botón "Agregar al carrito"
  - Productos relacionados

#### Carrito de Compras
- Visualización de productos agregados
- Modificación de cantidades
- Eliminación de productos
- Cálculo de subtotal
- Botón para proceder al checkout

#### Checkout (Proceso de Compra)
- Formulario de datos del cliente:
  - Información personal (nombre, email, teléfono)
  - Dirección de envío
  - Método de pago
- Resumen del pedido
- Confirmación de compra
- Generación de orden en Odoo

#### Páginas Informativas
- **Contacto**: Formulario de contacto, dirección física, teléfono, email
- **FAQs**: Preguntas frecuentes sobre envíos, devoluciones, productos
- **Políticas**:
  - Términos y condiciones
  - Política de privacidad
  - Política de devoluciones
  - Política de envíos

### 2.2. Integraciones Técnicas
- Sincronización con Odoo ERP:
  - Catálogo de productos
  - Inventario en tiempo real
  - Creación de órdenes de venta
  - Datos de clientes

### 2.3. Características Técnicas
- Diseño responsive (desktop, tablet, móvil)
- SEO básico (meta tags, sitemap, robots.txt)
- Performance optimizado (tiempo de carga < 3 segundos)
- Formularios con validación
- Manejo de errores básico

## 3. Exclusiones (Fuera del Alcance del MVP)

### 3.1. Funcionalidades Avanzadas NO Incluidas
- ❌ Sistema de cuentas de usuario registrado / login
- ❌ Historial de pedidos para clientes
- ❌ Wishlist o lista de deseos
- ❌ Comparador de productos
- ❌ Sistema de reseñas y calificaciones
- ❌ Chat en vivo o chatbot
- ❌ Blog o contenido editorial
- ❌ Newsletter o sistema de email marketing
- ❌ Programa de lealtad o puntos
- ❌ Promociones automáticas o cupones de descuento
- ❌ Checkout como invitado vs registrado (solo invitado en MVP)

### 3.2. Integraciones NO Incluidas
- ❌ Múltiples pasarelas de pago (solo una en MVP)
- ❌ Múltiples transportadoras (solo una o cálculo fijo)
- ❌ Integración con sistemas de facturación electrónica
- ❌ CRM externo
- ❌ Herramientas de analítica avanzada (más allá de Google Analytics básico)

### 3.3. Características Técnicas NO Incluidas
- ❌ PWA (Progressive Web App)
- ❌ Aplicación móvil nativa
- ❌ Búsqueda avanzada con IA
- ❌ Recomendaciones personalizadas
- ❌ Soporte multi-idioma
- ❌ Soporte multi-moneda
- ❌ CDN configurado

## 4. KPIs (Key Performance Indicators)

### 4.1. KPIs de Negocio

#### Conversión
- **Métrica**: Tasa de conversión (% de visitantes que completan compra)
- **Target MVP**: ≥ 1.5%
- **Medición**: Google Analytics / Odoo

#### Valor del Pedido
- **Métrica**: Ticket promedio por pedido
- **Target MVP**: ≥ $50 USD
- **Medición**: Odoo / Dashboard de ventas

#### Generación de Leads
- **Métrica**: Formularios de contacto completados
- **Target MVP**: ≥ 20 por mes
- **Medición**: Odoo / Sistema de formularios

### 4.2. KPIs Técnicos

#### Performance
- **Métrica**: Tiempo de carga (LCP - Largest Contentful Paint)
- **Target MVP**: < 3 segundos
- **Medición**: Google PageSpeed Insights / Lighthouse

#### Estabilidad
- **Métrica**: Tasa de error en checkout
- **Target MVP**: < 2%
- **Medición**: Logs de Odoo / Monitoring

#### Disponibilidad
- **Métrica**: Uptime del sitio
- **Target MVP**: ≥ 99%
- **Medición**: Herramienta de monitoreo (UptimeRobot, etc.)

### 4.3. KPIs de Experiencia de Usuario

#### Engagement
- **Métrica**: Páginas por sesión
- **Target MVP**: ≥ 3 páginas
- **Medición**: Google Analytics

#### Retención
- **Métrica**: Tasa de rebote
- **Target MVP**: < 60%
- **Medición**: Google Analytics

#### Usabilidad
- **Métrica**: Tasa de abandono de carrito
- **Target MVP**: < 70%
- **Medición**: Google Analytics / Odoo

## 5. Criterios de Aceptación del MVP

### 5.1. Funcionales
- ✅ Todas las páginas definidas están implementadas y funcionando
- ✅ El flujo de compra completo funciona end-to-end
- ✅ La integración con Odoo sincroniza correctamente
- ✅ Los formularios validan datos correctamente
- ✅ El sitio es responsive en móvil, tablet y desktop

### 5.2. No Funcionales
- ✅ El tiempo de carga es inferior a 3 segundos
- ✅ El sitio pasa validación de accesibilidad básica
- ✅ El sitio funciona en navegadores principales (Chrome, Firefox, Safari, Edge)
- ✅ Todos los enlaces y botones funcionan correctamente
- ✅ No hay errores de consola críticos

### 5.3. Documentación
- ✅ Documentación técnica de arquitectura
- ✅ Manual de usuario básico
- ✅ Guía de despliegue y configuración
- ✅ Documentación de integraciones

## 6. Supuestos y Dependencias

### Supuestos
1. Odoo ERP ya está configurado y operativo
2. Se cuenta con hosting y dominio disponibles
3. Los productos ya están cargados en Odoo
4. Se tiene acceso a credenciales de pasarela de pago
5. El contenido (textos, imágenes) será provisto por el cliente

### Dependencias
1. Acceso a instancia de Odoo (API y credenciales)
2. Definición de método de pago a integrar
3. Definición de política de envíos y costos
4. Aprobación de diseño visual por stakeholders
5. Catálogo de productos finalizado en Odoo

## 7. Timeline Estimado

Basado en el roadmap de 02-roadmap-fases.md, el MVP completo se estima en **9 fases**:
- **Fase 0**: Descubrimiento y alcance (actual)
- **Fases 1-9**: Implementación técnica progresiva

Tiempo estimado total: 8-12 semanas (dependiendo de recursos y complejidad)
