# Fase 4: Diseño Home + Institucionales

## Objetivo
Construir las páginas clave de contenido institucional y la página principal (Home) del sitio web de ferretería en Odoo, con enfoque en conversión, usabilidad y experiencia de usuario.

## Páginas a Implementar

### 1. Home (Página Principal)

#### Objetivo de Conversión
- Mostrar productos destacados y ofertas
- Facilitar acceso rápido a categorías principales
- Generar confianza mediante elementos institucionales
- Capturar leads mediante CTAs estratégicos

#### Estructura de Secciones

**1.1 Hero Section**
- Banner principal rotativo (3-5 slides)
- Contenido: Ofertas destacadas, productos nuevos, promociones temporales
- CTA principal: "Ver Ofertas" / "Comprar Ahora"
- Elementos visuales: Imágenes de alta calidad, overlays con texto legible
- Altura recomendada: 450-600px desktop, 300-400px mobile

**1.2 Categorías Destacadas**
- Grid de 6-8 categorías principales con imágenes
- Layout: 4 columnas desktop, 2 columnas tablet, 1 columna mobile
- Elementos por categoría:
  - Imagen representativa
  - Nombre de categoría
  - Cantidad de productos (opcional)
  - Enlace directo a PLP

**1.3 Productos Destacados**
- Carrusel de productos más vendidos/nuevos
- 8-12 productos visibles mediante scroll horizontal
- Información por producto:
  - Imagen principal
  - Nombre
  - Precio (con descuento si aplica)
  - Badge de "Nuevo" / "Oferta" si corresponde
  - Botón "Agregar al carrito" / "Ver detalle"

**1.4 Beneficios / Propuesta de Valor**
- 3-4 columnas con íconos
- Ejemplos:
  - Envío gratis en compras superiores a $X
  - Garantía en productos
  - Atención personalizada
  - Devoluciones fáciles

**1.5 Marcas Destacadas**
- Logos de marcas principales (6-12 marcas)
- Layout responsivo: 6 columnas desktop, 3-4 tablet, 2 mobile
- Opción de enlazar a página de marca o filtro de productos

**1.6 Testimonios / Reseñas** (opcional para MVP)
- 2-3 testimonios de clientes
- Nombre, valoración estrellada, texto breve

**1.7 Newsletter / Lead Capture**
- Formulario simple: Email + Botón suscribir
- Copy: "Recibe ofertas exclusivas y novedades"
- Integración con módulo CRM de Odoo

**1.8 Footer Informativo**
- Links a páginas institucionales
- Información de contacto
- Redes sociales
- Métodos de pago aceptados

#### Consideraciones UX
- Tiempo de carga objetivo: < 3 segundos
- Lazy loading de imágenes
- Scroll suave entre secciones
- CTAs visibles sin hacer scroll (above the fold)
- Diseño mobile-first

---

### 2. Nosotros (Quiénes Somos)

#### Objetivo
Generar confianza mostrando historia, valores y equipo de la ferretería.

#### Estructura de Contenido

**2.1 Header de Página**
- Título: "Quiénes Somos" / "Nosotros"
- Subtítulo breve con propuesta de valor
- Imagen hero representativa (equipo, tienda física, etc.)

**2.2 Nuestra Historia**
- Texto narrativo (200-400 palabras)
- Origen de la ferretería
- Años en el mercado
- Evolución y crecimiento
- Imagen de apoyo (histórica o instalaciones)

**2.3 Misión, Visión y Valores**
- Layout de 3 columnas o tarjetas
- **Misión**: Para qué existe la empresa
- **Visión**: Hacia dónde va
- **Valores**: 3-5 valores fundamentales (ej: calidad, servicio, confianza)

**2.4 Nuestro Equipo** (opcional para MVP)
- Grid de miembros clave
- Foto, nombre, cargo
- Breve descripción

**2.5 Certificaciones y Reconocimientos** (si aplica)
- Logos de certificaciones
- Premios o reconocimientos
- Membresías en asociaciones

**2.6 CTA Final**
- "Conoce nuestros productos"
- "Contáctanos"

#### Consideraciones de Contenido
- Tono: Profesional pero cercano
- Incluir datos concretos (años, clientes, proyectos)
- Fotografías reales preferiblemente sobre stock

---

### 3. Contacto

#### Objetivo
Facilitar múltiples canales de comunicación con los clientes.

#### Estructura de Contenido

**3.1 Header de Página**
- Título: "Contáctanos"
- Subtítulo: "Estamos para ayudarte"

**3.2 Formulario de Contacto**
- Campos:
  - Nombre completo (requerido)
  - Email (requerido, con validación)
  - Teléfono (opcional)
  - Asunto (select con opciones predefinidas)
  - Mensaje (textarea, requerido)
  - Checkbox aceptación de privacidad
  - Botón "Enviar mensaje"
- Integración con Odoo CRM (crear lead automáticamente)
- Confirmación visual al enviar
- Email de confirmación automático

**3.3 Información de Contacto**
- Layout de tarjetas o lista con íconos
- **Dirección física**: 
  - Dirección completa
  - Horarios de atención
- **Teléfono(s)**:
  - Número(s) de contacto
  - WhatsApp (si aplica)
- **Email**:
  - Email general
  - Emails por departamento (ventas, soporte)
- **Redes sociales**:
  - Links a perfiles activos

**3.4 Mapa de Ubicación**
- Integración con Google Maps
- Marcador en ubicación exacta
- Opción "Cómo llegar"

**3.5 Horarios de Atención**
- Tabla o lista clara
- Días y horas
- Notas especiales (festivos, horario extendido)

**3.6 Canales Alternativos**
- Widget de WhatsApp (flotante)
- Chat en vivo (si está disponible)
- FAQ link: "¿Tienes preguntas frecuentes?"

#### Validaciones y UX
- Validación en tiempo real de campos
- Mensajes de error claros
- Protección anti-spam (reCAPTCHA o similar)
- Respuesta automática confirmando recepción

---

### 4. FAQs (Preguntas Frecuentes)

#### Objetivo
Resolver dudas comunes y reducir carga de atención al cliente.

#### Estructura de Contenido

**4.1 Header de Página**
- Título: "Preguntas Frecuentes"
- Subtítulo: "Encuentra respuestas rápidas"
- Buscador de FAQs (opcional para MVP)

**4.2 Organización por Categorías**
Usar acordeón o tabs para organizar preguntas por tema:

**Categoría 1: Compras y Pedidos**
- ¿Cómo puedo realizar un pedido?
- ¿Cuáles son los métodos de pago aceptados?
- ¿Puedo modificar o cancelar mi pedido?
- ¿Emiten factura?
- ¿Hay un monto mínimo de compra?

**Categoría 2: Envíos y Entregas**
- ¿Cuáles son los tiempos de entrega?
- ¿Cuál es el costo de envío?
- ¿Hacen envíos a todo el país?
- ¿Puedo recoger mi pedido en tienda?
- ¿Cómo puedo rastrear mi pedido?

**Categoría 3: Productos**
- ¿Todos los productos tienen garantía?
- ¿Qué hago si recibo un producto defectuoso?
- ¿Manejan productos de todas las marcas?
- ¿Los precios incluyen IVA?
- ¿Tienen stock de todos los productos publicados?

**Categoría 4: Devoluciones y Cambios**
- ¿Cuál es la política de devoluciones?
- ¿En cuánto tiempo puedo devolver un producto?
- ¿Quién cubre el costo del envío de devolución?
- ¿Cómo solicito un cambio?

**Categoría 5: Cuenta y Seguridad**
- ¿Cómo creo una cuenta?
- ¿Es seguro comprar en el sitio?
- ¿Cómo recupero mi contraseña?
- ¿Cómo actualizo mi información de perfil?

**4.3 Implementación Técnica**
- Componente acordeón (collapse/expand)
- Animaciones suaves
- URL amigable para cada pregunta (anchor links)
- Esquema Schema.org FAQPage para SEO

**4.4 CTA Final**
- "¿No encontraste lo que buscabas?"
- Botón a página de Contacto
- Link a chat o WhatsApp

---

### 5. Políticas

#### Objetivo
Establecer términos claros y cumplir requisitos legales.

#### Estructura de Contenido

**5.1 Navegación de Políticas**
Tabs o menú lateral para navegación entre documentos:
- Términos y Condiciones
- Política de Privacidad
- Política de Devoluciones
- Política de Envíos
- Política de Cookies (si aplica)

**5.2 Términos y Condiciones**
Secciones típicas:
1. Aceptación de términos
2. Uso del sitio web
3. Registro y cuenta de usuario
4. Precios y pagos
5. Disponibilidad de productos
6. Procesamiento de pedidos
7. Limitación de responsabilidad
8. Modificación de términos
9. Ley aplicable y jurisdicción
10. Contacto

**5.3 Política de Privacidad**
Conforme a regulaciones locales (GDPR, LGPD, etc.):
1. Información que recopilamos
2. Cómo usamos la información
3. Compartir información con terceros
4. Cookies y tecnologías de seguimiento
5. Derechos del usuario
6. Seguridad de datos
7. Cambios a la política
8. Contacto del responsable de datos

**5.4 Política de Devoluciones**
1. Plazo para devoluciones (ej: 30 días)
2. Condiciones del producto para devolución
3. Proceso para solicitar devolución
4. Reembolsos: método y tiempo
5. Productos no retornables
6. Cambios por defectos de fábrica

**5.5 Política de Envíos**
1. Zonas de cobertura
2. Tiempos estimados de entrega
3. Costos de envío por zona
4. Envío gratis (condiciones si aplica)
5. Proceso de empaque y preparación
6. Responsabilidad en el transporte
7. Qué hacer si el pedido no llega

**5.6 Política de Cookies** (si aplica)
1. Qué son las cookies
2. Cookies que utilizamos
3. Cookies de terceros (Analytics, publicidad)
4. Cómo gestionar cookies
5. Más información

**5.7 Consideraciones Legales**
- Lenguaje claro pero formalmente legal
- Fecha de última actualización visible
- Versión versionada
- Opción de descargar PDF
- Consultar con asesoría legal para contenido específico

---

## Especificaciones Técnicas - Odoo Website

### Módulos de Odoo Requeridos
- `website`: Core del sitio web
- `website_sale`: Funcionalidad de e-commerce
- `website_crm`: Formularios de contacto integrados con CRM
- `website_blog`: Opcional para contenido (si se añade blog en futuro)

### Implementación en Odoo

#### Crear Páginas en Odoo Website
```xml
<!-- Ejemplo de estructura para página Nosotros -->
<odoo>
    <data>
        <record id="page_nosotros" model="website.page">
            <field name="name">Nosotros</field>
            <field name="url">/nosotros</field>
            <field name="is_published" eval="True"/>
            <field name="view_id" ref="view_nosotros_template"/>
        </record>
        
        <record id="view_nosotros_template" model="ir.ui.view">
            <field name="name">Nosotros - Template</field>
            <field name="type">qweb</field>
            <field name="key">ferreteria_web.nosotros_template</field>
            <field name="arch" type="xml">
                <t t-name="ferreteria_web.nosotros_template">
                    <t t-call="website.layout">
                        <div id="wrap" class="oe_structure">
                            <!-- Contenido de página -->
                        </div>
                    </t>
                </t>
            </field>
        </record>
    </data>
</odoo>
```

#### Menú Principal
Configurar en Odoo Website:
- Inicio → `/`
- Productos → `/shop`
- Marcas → `/shop/brands` (custom)
- Ofertas → `/shop/ofertas` (custom o filtro)
- Nosotros → `/nosotros`
- Contacto → `/contacto`

#### Formularios de Contacto
Utilizar `website_crm.contactus_form` o crear formulario personalizado:
```xml
<form action="/contacto/submit" method="post" class="s_website_form">
    <div class="form-group">
        <input type="text" class="form-control" name="name" required="required" placeholder="Nombre"/>
    </div>
    <div class="form-group">
        <input type="email" class="form-control" name="email" required="required" placeholder="Email"/>
    </div>
    <!-- Más campos -->
    <button type="submit" class="btn btn-primary">Enviar</button>
</form>
```

#### Snippets Reutilizables
Crear snippets en el editor web de Odoo para:
- Hero banners
- Grids de categorías
- Carruseles de productos
- Bloques de testimonios
- CTAs

---

## Diseño Responsive

### Breakpoints
- **Mobile**: < 768px
- **Tablet**: 768px - 1024px
- **Desktop**: > 1024px
- **Large Desktop**: > 1440px

### Adaptaciones Móviles Clave

**Home**
- Hero: Altura reducida, texto más grande
- Categorías: 1-2 columnas máximo
- Productos: Carrusel táctil
- Menú: Hamburger menu

**Formularios**
- Inputs a ancho completo
- Tamaño de fuente > 16px (evita zoom iOS)
- Botones grandes (min 44x44px táctiles)

**Navegación**
- Menú sticky en scroll
- Breadcrumbs ocultos en mobile (opcional)
- Back to top button

---

## Criterios de Aceptación

### Funcionales
- [x] Todas las páginas accesibles mediante menú principal
- [x] Formulario de contacto envía emails y crea leads en CRM
- [x] Home muestra productos desde catálogo real de Odoo
- [x] Todas las páginas tienen meta tags básicos (title, description)
- [x] Links internos funcionan correctamente

### UX/UI
- [x] Diseño consistente con paleta de colores corporativa
- [x] Tipografía legible (min 14px body text)
- [x] Contraste adecuado (WCAG AA mínimo)
- [x] Imágenes optimizadas (< 200KB por imagen)
- [x] Responsive en dispositivos móviles y tablets

### Rendimiento
- [x] Tiempo de carga < 3 segundos (LCP)
- [x] Core Web Vitals en rango "Good"
- [x] Imágenes con lazy loading
- [x] CSS y JS minificados

### SEO Básico
- [x] URLs amigables (slug readable)
- [x] Meta title único por página (< 60 caracteres)
- [x] Meta description por página (< 160 caracteres)
- [x] Headings jerárquicos (H1 único, H2, H3)
- [x] Alt text en todas las imágenes

---

## Plan de Contenido

### Responsabilidades
**Cliente debe proveer:**
- Textos institucionales (Nosotros, Políticas)
- Imágenes corporativas (equipo, instalaciones)
- Logos de marcas y certificaciones
- Información de contacto actual
- FAQs específicas del negocio

**Equipo técnico debe:**
- Implementar estructura de páginas
- Configurar formularios y validaciones
- Integrar con módulos Odoo
- Aplicar diseño responsive
- Optimizar rendimiento

---

## Testing

### Checklist de QA
- [ ] Navegación entre todas las páginas
- [ ] Formulario de contacto envía correctamente
- [ ] Emails de confirmación se reciben
- [ ] Leads aparecen en CRM de Odoo
- [ ] Responsive en Chrome/Firefox/Safari móvil
- [ ] Velocidad de carga aceptable
- [ ] Sin errores de consola JavaScript
- [ ] Links rotos (usar herramienta de crawler)
- [ ] Validación HTML (W3C Validator)

### Navegadores y Dispositivos
**Navegadores:**
- Chrome (últimas 2 versiones)
- Firefox (últimas 2 versiones)
- Safari (últimas 2 versiones)
- Edge (última versión)

**Dispositivos:**
- iPhone (Safari iOS)
- Android (Chrome)
- iPad / Tablet Android
- Desktop (1920x1080, 1366x768)

---

## Entregables

1. **Páginas implementadas en staging de Odoo:**
   - Home funcional con todos los componentes
   - Nosotros completa
   - Contacto con formulario operativo
   - FAQs organizadas por categorías
   - Políticas legales completas

2. **Documentación:**
   - Screenshots de cada página (desktop y mobile)
   - Manual de edición de contenido para cliente
   - Guía de uso del website builder de Odoo

3. **Assets:**
   - Imágenes optimizadas subidas a Odoo
   - Logos y recursos gráficos organizados
   - Paleta de colores y tipografía documentada

4. **Configuración:**
   - Menú principal configurado
   - Formularios integrados con CRM
   - Redirecciones (si aplica)
   - Google Analytics ID configurado (si está disponible)

---

## Notas de Implementación

### Buenas Prácticas Odoo
- Usar `t-call` para reutilizar templates
- Aprovechar snippets del website builder
- Mantener XML estructurado y comentado
- Usar clases Bootstrap 4 nativas de Odoo
- No sobrescribir assets core innecesariamente

### Consideraciones de Mantenimiento
- Contenido editable desde interfaz web (no hardcoded)
- Cliente puede modificar textos sin código
- Imágenes gestionables desde Media Library
- Versioning de cambios importantes

### Próximos Pasos (Fase 5+)
- Integración con sistema de pagos
- Configuración de métodos de envío
- Optimización SEO avanzada
- A/B testing en Home
- Analytics y seguimiento de conversiones

---

## Referencias

- [Odoo Website Builder Documentation](https://www.odoo.com/documentation/16.0/applications/websites.html)
- [Odoo eCommerce Module](https://www.odoo.com/documentation/16.0/applications/websites/ecommerce.html)
- [Bootstrap 4 Documentation](https://getbootstrap.com/docs/4.6/)
- [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/WCAG21/quickref/)
- [Google Page Speed Insights](https://pagespeed.web.dev/)

---

**Fecha de creación**: 2026-02-24  
**Última actualización**: 2026-02-24  
**Estado**: En desarrollo - Fase 4
