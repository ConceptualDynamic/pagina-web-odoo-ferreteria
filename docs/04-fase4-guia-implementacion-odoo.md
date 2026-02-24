# Guía de Implementación Técnica - Fase 4
## Páginas Home e Institucionales en Odoo

---

## Requisitos Previos

### Módulos Odoo Necesarios
Verificar que estén instalados y actualizados:
```bash
# Módulos core
- website (16.0+)
- website_sale
- website_crm
- website_form
- portal

# Módulos recomendados
- website_blog (si se planea blog futuro)
- website_livechat (para chat en vivo)
```

### Configuración Base
- Base de datos Odoo configurada
- Tema instalado (puede ser tema default o personalizado)
- Dominio configurado (si es producción/staging)
- SSL activo

---

## Estructura del Módulo Personalizado

### Crear Módulo Custom

```bash
# Estructura de directorios
ferreteria_web/
├── __init__.py
├── __manifest__.py
├── controllers/
│   ├── __init__.py
│   └── main.py
├── models/
│   ├── __init__.py
│   └── website.py
├── static/
│   ├── src/
│   │   ├── css/
│   │   │   └── custom.css
│   │   ├── js/
│   │   │   └── custom.js
│   │   └── img/
│   └── description/
│       └── icon.png
├── views/
│   ├── templates.xml
│   ├── page_home.xml
│   ├── page_nosotros.xml
│   ├── page_contacto.xml
│   ├── page_faqs.xml
│   ├── page_politicas.xml
│   ├── snippets.xml
│   └── assets.xml
└── data/
    ├── website_menu.xml
    └── website_pages.xml
```

### __manifest__.py

```python
# -*- coding: utf-8 -*-
{
    'name': 'Ferretería Web - Páginas Institucionales',
    'version': '1.0.0',
    'category': 'Website',
    'summary': 'Páginas Home e institucionales para sitio web de ferretería',
    'description': """
        Módulo que implementa:
        - Página Home optimizada para conversión
        - Páginas institucionales (Nosotros, Contacto, FAQs, Políticas)
        - Integración con CRM para formularios
        - Diseño responsive y optimizado para SEO
    """,
    'author': 'Conceptual Dynamic',
    'website': 'https://www.conceptualdynamic.com',
    'depends': [
        'website',
        'website_sale',
        'website_crm',
        'website_form',
    ],
    'data': [
        'data/website_pages.xml',
        'data/website_menu.xml',
        'views/templates.xml',
        'views/page_home.xml',
        'views/page_nosotros.xml',
        'views/page_contacto.xml',
        'views/page_faqs.xml',
        'views/page_politicas.xml',
        'views/snippets.xml',
        'views/assets.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'ferreteria_web/static/src/css/custom.css',
            'ferreteria_web/static/src/js/custom.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
```

---

## Implementación de Páginas

### 1. Página Home

**data/website_pages.xml**
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data>
        <!-- Página Home -->
        <record id="page_home" model="website.page">
            <field name="name">Home</field>
            <field name="url">/</field>
            <field name="website_published" eval="True"/>
            <field name="is_published" eval="True"/>
            <field name="view_id" ref="view_home_template"/>
        </record>
    </data>
</odoo>
```

**views/page_home.xml**
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <template id="view_home_template" name="Home Page">
        <t t-call="website.layout">
            <div id="wrap" class="oe_structure oe_empty">
                
                <!-- Hero Section -->
                <section class="s_banner o_cc o_cc3 pt96 pb96" data-snippet="s_banner">
                    <div class="container">
                        <div class="row align-items-center">
                            <div class="col-lg-6">
                                <h1 class="display-3">Ferretería de Confianza</h1>
                                <p class="lead">
                                    Encuentra todo lo que necesitas para tus proyectos.
                                    Calidad, variedad y los mejores precios.
                                </p>
                                <a href="/shop" class="btn btn-primary btn-lg">Ver Productos</a>
                            </div>
                            <div class="col-lg-6">
                                <img src="/ferreteria_web/static/src/img/hero-banner.jpg" 
                                     alt="Ferretería" 
                                     class="img-fluid"/>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Categorías Destacadas -->
                <section class="s_features pt64 pb64 bg-light">
                    <div class="container">
                        <div class="row mb-4">
                            <div class="col-12 text-center">
                                <h2>Categorías Principales</h2>
                                <p class="text-muted">Explora nuestro catálogo por categoría</p>
                            </div>
                        </div>
                        <div class="row">
                            <!-- Categoría 1 -->
                            <div class="col-lg-3 col-md-4 col-sm-6 mb-4">
                                <a href="/shop?category=herramientas" class="text-decoration-none">
                                    <div class="card h-100 shadow-sm hover-shadow">
                                        <img src="/ferreteria_web/static/src/img/cat-herramientas.jpg" 
                                             class="card-img-top" 
                                             alt="Herramientas"/>
                                        <div class="card-body text-center">
                                            <h5 class="card-title">Herramientas</h5>
                                            <p class="text-muted small">Ver productos</p>
                                        </div>
                                    </div>
                                </a>
                            </div>
                            <!-- Repetir para más categorías -->
                        </div>
                    </div>
                </section>

                <!-- Productos Destacados -->
                <section class="s_products_featured pt64 pb64">
                    <div class="container">
                        <div class="row mb-4">
                            <div class="col-12 text-center">
                                <h2>Productos Destacados</h2>
                                <p class="text-muted">Los más vendidos de esta semana</p>
                            </div>
                        </div>
                        <t t-call="website_sale.products">
                            <t t-set="products" t-value="request.env['product.template'].search([
                                ('website_published', '=', True),
                                ('is_published', '=', True)
                            ], limit=8, order='website_sequence, name')"/>
                        </t>
                    </div>
                </section>

                <!-- Beneficios -->
                <section class="s_features pt64 pb64 bg-light">
                    <div class="container">
                        <div class="row text-center">
                            <div class="col-lg-3 col-md-6 mb-4">
                                <div class="feature-box">
                                    <i class="fa fa-shipping-fast fa-3x text-primary mb-3"></i>
                                    <h5>Envío Gratis</h5>
                                    <p class="text-muted">En compras superiores a $500</p>
                                </div>
                            </div>
                            <div class="col-lg-3 col-md-6 mb-4">
                                <div class="feature-box">
                                    <i class="fa fa-shield-alt fa-3x text-primary mb-3"></i>
                                    <h5>Garantía</h5>
                                    <p class="text-muted">Todos nuestros productos</p>
                                </div>
                            </div>
                            <div class="col-lg-3 col-md-6 mb-4">
                                <div class="feature-box">
                                    <i class="fa fa-headset fa-3x text-primary mb-3"></i>
                                    <h5>Atención Personalizada</h5>
                                    <p class="text-muted">Asesoría experta</p>
                                </div>
                            </div>
                            <div class="col-lg-3 col-md-6 mb-4">
                                <div class="feature-box">
                                    <i class="fa fa-undo fa-3x text-primary mb-3"></i>
                                    <h5>Devoluciones Fáciles</h5>
                                    <p class="text-muted">30 días para devolución</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Newsletter -->
                <section class="s_newsletter pt64 pb64">
                    <div class="container">
                        <div class="row justify-content-center">
                            <div class="col-lg-6 text-center">
                                <h3>Suscríbete a nuestro Newsletter</h3>
                                <p class="text-muted mb-4">Recibe ofertas exclusivas y novedades</p>
                                <form method="post" action="/website_form/crm.lead" 
                                      class="s_website_form" 
                                      data-model_name="crm.lead">
                                    <div class="input-group mb-3">
                                        <input type="email" 
                                               class="form-control" 
                                               name="email_from" 
                                               placeholder="Tu email" 
                                               required="required"/>
                                        <input type="hidden" name="type" value="lead"/>
                                        <input type="hidden" name="description" value="Suscripción newsletter"/>
                                        <button class="btn btn-primary" type="submit">
                                            Suscribirse
                                        </button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </section>

            </div>
        </t>
    </template>
</odoo>
```

---

### 2. Página Nosotros

**views/page_nosotros.xml**
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data>
        <!-- Record de página -->
        <record id="page_nosotros" model="website.page">
            <field name="name">Nosotros</field>
            <field name="url">/nosotros</field>
            <field name="website_published" eval="True"/>
            <field name="is_published" eval="True"/>
            <field name="view_id" ref="view_nosotros_template"/>
        </record>

        <!-- Template -->
        <template id="view_nosotros_template" name="Nosotros Page">
            <t t-call="website.layout">
                <div id="wrap" class="oe_structure">
                    
                    <!-- Hero Header -->
                    <section class="s_cover parallax pt96 pb96" 
                             data-scroll-background-ratio="1" 
                             style="background-image: url('/ferreteria_web/static/src/img/nosotros-hero.jpg');">
                        <span class="s_parallax_bg oe_img_bg" 
                              style="background-position: 50% 0;"></span>
                        <div class="container">
                            <div class="row">
                                <div class="col-lg-8 offset-lg-2 text-center text-white">
                                    <h1 class="display-2">Quiénes Somos</h1>
                                    <p class="lead">
                                        Tu ferretería de confianza desde hace más de 20 años
                                    </p>
                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- Nuestra Historia -->
                    <section class="pt64 pb64">
                        <div class="container">
                            <div class="row align-items-center">
                                <div class="col-lg-6 mb-4 mb-lg-0">
                                    <h2>Nuestra Historia</h2>
                                    <p>
                                        Desde 2004, hemos sido la ferretería de referencia en la región,
                                        ofreciendo productos de la más alta calidad y un servicio
                                        personalizado que nos distingue.
                                    </p>
                                    <p>
                                        Comenzamos como un pequeño negocio familiar y hemos crecido
                                        hasta convertirnos en una empresa reconocida, pero manteniendo
                                        siempre nuestros valores de cercanía, confianza y excelencia.
                                    </p>
                                    <p>
                                        Hoy contamos con más de 5,000 productos, atendemos a miles
                                        de clientes satisfechos y seguimos comprometidos con ofrecer
                                        las mejores soluciones para tus proyectos.
                                    </p>
                                </div>
                                <div class="col-lg-6">
                                    <img src="/ferreteria_web/static/src/img/historia.jpg" 
                                         alt="Nuestra historia" 
                                         class="img-fluid rounded shadow"/>
                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- Misión, Visión, Valores -->
                    <section class="pt64 pb64 bg-light">
                        <div class="container">
                            <div class="row mb-4">
                                <div class="col-12 text-center">
                                    <h2>Nuestros Pilares</h2>
                                </div>
                            </div>
                            <div class="row">
                                <!-- Misión -->
                                <div class="col-lg-4 mb-4">
                                    <div class="card h-100 shadow-sm">
                                        <div class="card-body text-center">
                                            <i class="fa fa-bullseye fa-3x text-primary mb-3"></i>
                                            <h4>Misión</h4>
                                            <p>
                                                Proveer productos y servicios de ferretería de calidad,
                                                brindando asesoría experta para que nuestros clientes
                                                completen sus proyectos con éxito.
                                            </p>
                                        </div>
                                    </div>
                                </div>
                                <!-- Visión -->
                                <div class="col-lg-4 mb-4">
                                    <div class="card h-100 shadow-sm">
                                        <div class="card-body text-center">
                                            <i class="fa fa-eye fa-3x text-primary mb-3"></i>
                                            <h4>Visión</h4>
                                            <p>
                                                Ser la ferretería líder en la región, reconocida por
                                                nuestra innovación, calidad de servicio y compromiso
                                                con la satisfacción del cliente.
                                            </p>
                                        </div>
                                    </div>
                                </div>
                                <!-- Valores -->
                                <div class="col-lg-4 mb-4">
                                    <div class="card h-100 shadow-sm">
                                        <div class="card-body text-center">
                                            <i class="fa fa-heart fa-3x text-primary mb-3"></i>
                                            <h4>Valores</h4>
                                            <ul class="list-unstyled">
                                                <li><strong>Calidad:</strong> En productos y servicio</li>
                                                <li><strong>Confianza:</strong> Relaciones duraderas</li>
                                                <li><strong>Innovación:</strong> Mejora continua</li>
                                                <li><strong>Compromiso:</strong> Con nuestros clientes</li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- CTA -->
                    <section class="pt64 pb64">
                        <div class="container text-center">
                            <h3>¿Listo para comenzar tu proyecto?</h3>
                            <p class="lead mb-4">Visita nuestra tienda o explora nuestro catálogo en línea</p>
                            <a href="/shop" class="btn btn-primary btn-lg mr-2">Ver Productos</a>
                            <a href="/contacto" class="btn btn-outline-primary btn-lg">Contáctanos</a>
                        </div>
                    </section>

                </div>
            </t>
        </template>
    </data>
</odoo>
```

---

### 3. Página Contacto

**views/page_contacto.xml**
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data>
        <record id="page_contacto" model="website.page">
            <field name="name">Contacto</field>
            <field name="url">/contacto</field>
            <field name="website_published" eval="True"/>
            <field name="is_published" eval="True"/>
            <field name="view_id" ref="view_contacto_template"/>
        </record>

        <template id="view_contacto_template" name="Contacto Page">
            <t t-call="website.layout">
                <div id="wrap" class="oe_structure">
                    
                    <!-- Header -->
                    <section class="pt64 pb32 bg-light">
                        <div class="container text-center">
                            <h1>Contáctanos</h1>
                            <p class="lead">Estamos aquí para ayudarte</p>
                        </div>
                    </section>

                    <!-- Contenido Principal -->
                    <section class="pt64 pb64">
                        <div class="container">
                            <div class="row">
                                <!-- Formulario -->
                                <div class="col-lg-7 mb-4">
                                    <h3 class="mb-4">Envíanos un mensaje</h3>
                                    <form method="post" 
                                          action="/website_form/crm.lead" 
                                          class="s_website_form" 
                                          data-model_name="crm.lead"
                                          data-success-mode="redirect"
                                          data-success-page="/contacto-gracias">
                                        
                                        <div class="row">
                                            <div class="col-md-6 form-group">
                                                <label for="contact_name">Nombre completo *</label>
                                                <input type="text" 
                                                       class="form-control" 
                                                       id="contact_name"
                                                       name="contact_name" 
                                                       required="required"/>
                                            </div>
                                            <div class="col-md-6 form-group">
                                                <label for="email_from">Email *</label>
                                                <input type="email" 
                                                       class="form-control" 
                                                       id="email_from"
                                                       name="email_from" 
                                                       required="required"/>
                                            </div>
                                        </div>
                                        
                                        <div class="row">
                                            <div class="col-md-6 form-group">
                                                <label for="phone">Teléfono</label>
                                                <input type="tel" 
                                                       class="form-control" 
                                                       id="phone"
                                                       name="phone"/>
                                            </div>
                                            <div class="col-md-6 form-group">
                                                <label for="subject">Asunto *</label>
                                                <select class="form-control" 
                                                        id="subject"
                                                        name="name" 
                                                        required="required">
                                                    <option value="">Selecciona...</option>
                                                    <option value="Consulta general">Consulta general</option>
                                                    <option value="Información de productos">Información de productos</option>
                                                    <option value="Cotización">Cotización</option>
                                                    <option value="Servicio postventa">Servicio postventa</option>
                                                    <option value="Otro">Otro</option>
                                                </select>
                                            </div>
                                        </div>
                                        
                                        <div class="form-group">
                                            <label for="description">Mensaje *</label>
                                            <textarea class="form-control" 
                                                      id="description"
                                                      name="description" 
                                                      rows="5" 
                                                      required="required"></textarea>
                                        </div>
                                        
                                        <div class="form-group form-check">
                                            <input type="checkbox" 
                                                   class="form-check-input" 
                                                   id="privacy"
                                                   required="required"/>
                                            <label class="form-check-label" for="privacy">
                                                Acepto la <a href="/politicas#privacidad" target="_blank">Política de Privacidad</a> *
                                            </label>
                                        </div>
                                        
                                        <input type="hidden" name="type" value="lead"/>
                                        
                                        <button type="submit" class="btn btn-primary btn-lg">
                                            <i class="fa fa-paper-plane mr-2"></i>Enviar mensaje
                                        </button>
                                    </form>
                                </div>

                                <!-- Información de Contacto -->
                                <div class="col-lg-5">
                                    <h3 class="mb-4">Información de Contacto</h3>
                                    
                                    <!-- Dirección -->
                                    <div class="media mb-4">
                                        <i class="fa fa-map-marker-alt fa-2x text-primary mr-3"></i>
                                        <div class="media-body">
                                            <h5>Dirección</h5>
                                            <p class="mb-0">
                                                Calle Principal #123<br/>
                                                Colonia Centro<br/>
                                                Ciudad, Estado, CP 12345
                                            </p>
                                            <p class="text-muted small">
                                                <strong>Horario:</strong><br/>
                                                Lun - Vie: 8:00 AM - 7:00 PM<br/>
                                                Sáb: 9:00 AM - 2:00 PM<br/>
                                                Dom: Cerrado
                                            </p>
                                        </div>
                                    </div>

                                    <!-- Teléfono -->
                                    <div class="media mb-4">
                                        <i class="fa fa-phone fa-2x text-primary mr-3"></i>
                                        <div class="media-body">
                                            <h5>Teléfono</h5>
                                            <p class="mb-0">
                                                <a href="tel:+525512345678">(55) 1234-5678</a><br/>
                                                <a href="tel:+525587654321">(55) 8765-4321</a>
                                            </p>
                                        </div>
                                    </div>

                                    <!-- WhatsApp -->
                                    <div class="media mb-4">
                                        <i class="fab fa-whatsapp fa-2x text-success mr-3"></i>
                                        <div class="media-body">
                                            <h5>WhatsApp</h5>
                                            <p class="mb-0">
                                                <a href="https://wa.me/525512345678" target="_blank">
                                                    +52 55 1234-5678
                                                </a>
                                            </p>
                                        </div>
                                    </div>

                                    <!-- Email -->
                                    <div class="media mb-4">
                                        <i class="fa fa-envelope fa-2x text-primary mr-3"></i>
                                        <div class="media-body">
                                            <h5>Email</h5>
                                            <p class="mb-0">
                                                <a href="mailto:ventas@ferreteria.com">ventas@ferreteria.com</a><br/>
                                                <a href="mailto:soporte@ferreteria.com">soporte@ferreteria.com</a>
                                            </p>
                                        </div>
                                    </div>

                                    <!-- Redes Sociales -->
                                    <div class="mt-4">
                                        <h5>Síguenos</h5>
                                        <a href="#" class="btn btn-outline-primary btn-sm mr-2">
                                            <i class="fab fa-facebook"></i>
                                        </a>
                                        <a href="#" class="btn btn-outline-info btn-sm mr-2">
                                            <i class="fab fa-twitter"></i>
                                        </a>
                                        <a href="#" class="btn btn-outline-danger btn-sm mr-2">
                                            <i class="fab fa-instagram"></i>
                                        </a>
                                        <a href="#" class="btn btn-outline-dark btn-sm">
                                            <i class="fab fa-linkedin"></i>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- Mapa -->
                    <section class="pb64">
                        <div class="container">
                            <div class="row">
                                <div class="col-12">
                                    <h3 class="mb-4 text-center">Nuestra Ubicación</h3>
                                    <div class="embed-responsive embed-responsive-16by9">
                                        <iframe class="embed-responsive-item" 
                                                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3762.123!2d-99.1234!3d19.4321!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMTnCsDI1JzU1LjYiTiA5OcKwMDcnMjQuNCJX!5e0!3m2!1ses!2smx!4v1234567890" 
                                                allowfullscreen="" 
                                                loading="lazy">
                                        </iframe>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>

                </div>
            </t>
        </template>

        <!-- Página de agradecimiento -->
        <record id="page_contacto_gracias" model="website.page">
            <field name="name">Gracias por tu mensaje</field>
            <field name="url">/contacto-gracias</field>
            <field name="website_published" eval="True"/>
            <field name="is_published" eval="True"/>
            <field name="view_id" ref="view_contacto_gracias_template"/>
        </record>

        <template id="view_contacto_gracias_template" name="Contacto Gracias Page">
            <t t-call="website.layout">
                <div id="wrap">
                    <section class="pt128 pb128 text-center">
                        <div class="container">
                            <i class="fa fa-check-circle fa-5x text-success mb-4"></i>
                            <h1>¡Mensaje Enviado!</h1>
                            <p class="lead mb-4">
                                Gracias por contactarnos. Hemos recibido tu mensaje y<br/>
                                te responderemos a la brevedad posible.
                            </p>
                            <a href="/" class="btn btn-primary">Volver al inicio</a>
                        </div>
                    </section>
                </div>
            </t>
        </template>
    </data>
</odoo>
```

---

### 4. Página FAQs

**views/page_faqs.xml**
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data>
        <record id="page_faqs" model="website.page">
            <field name="name">Preguntas Frecuentes</field>
            <field name="url">/faqs</field>
            <field name="website_published" eval="True"/>
            <field name="is_published" eval="True"/>
            <field name="view_id" ref="view_faqs_template"/>
        </record>

        <template id="view_faqs_template" name="FAQs Page">
            <t t-call="website.layout">
                <div id="wrap" class="oe_structure">
                    
                    <!-- Header -->
                    <section class="pt64 pb32 bg-light">
                        <div class="container text-center">
                            <h1>Preguntas Frecuentes</h1>
                            <p class="lead">Encuentra respuestas rápidas a las dudas más comunes</p>
                        </div>
                    </section>

                    <!-- FAQs Content -->
                    <section class="pt64 pb64">
                        <div class="container">
                            <div class="row">
                                <div class="col-lg-10 offset-lg-1">
                                    
                                    <!-- Categoría: Compras y Pedidos -->
                                    <h3 class="mb-4">Compras y Pedidos</h3>
                                    <div class="accordion mb-5" id="faqCompras">
                                        
                                        <div class="card">
                                            <div class="card-header" id="heading1">
                                                <h5 class="mb-0">
                                                    <button class="btn btn-link" type="button" 
                                                            data-toggle="collapse" data-target="#collapse1">
                                                        ¿Cómo puedo realizar un pedido?
                                                    </button>
                                                </h5>
                                            </div>
                                            <div id="collapse1" class="collapse show" data-parent="#faqCompras">
                                                <div class="card-body">
                                                    Puedes realizar tu pedido directamente desde nuestro sitio web.
                                                    Navega por nuestro catálogo, agrega productos al carrito y
                                                    procede al checkout. También puedes contactarnos por teléfono
                                                    o WhatsApp para hacer tu pedido.
                                                </div>
                                            </div>
                                        </div>

                                        <div class="card">
                                            <div class="card-header" id="heading2">
                                                <h5 class="mb-0">
                                                    <button class="btn btn-link collapsed" type="button" 
                                                            data-toggle="collapse" data-target="#collapse2">
                                                        ¿Cuáles son los métodos de pago aceptados?
                                                    </button>
                                                </h5>
                                            </div>
                                            <div id="collapse2" class="collapse" data-parent="#faqCompras">
                                                <div class="card-body">
                                                    Aceptamos tarjetas de crédito y débito (Visa, MasterCard, AMEX),
                                                    transferencias bancarias, PayPal y pago en efectivo en tienda física.
                                                </div>
                                            </div>
                                        </div>

                                        <!-- Más preguntas... -->

                                    </div>

                                    <!-- Categoría: Envíos y Entregas -->
                                    <h3 class="mb-4">Envíos y Entregas</h3>
                                    <div class="accordion mb-5" id="faqEnvios">
                                        
                                        <div class="card">
                                            <div class="card-header">
                                                <h5 class="mb-0">
                                                    <button class="btn btn-link" type="button" 
                                                            data-toggle="collapse" data-target="#collapse5">
                                                        ¿Cuáles son los tiempos de entrega?
                                                    </button>
                                                </h5>
                                            </div>
                                            <div id="collapse5" class="collapse" data-parent="#faqEnvios">
                                                <div class="card-body">
                                                    Los tiempos de entrega varían según tu ubicación:
                                                    <ul>
                                                        <li>Zona metropolitana: 1-3 días hábiles</li>
                                                        <li>Interior del estado: 3-5 días hábiles</li>
                                                        <li>Resto del país: 5-7 días hábiles</li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>

                                        <!-- Más preguntas... -->

                                    </div>

                                    <!-- Más categorías... -->

                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- CTA -->
                    <section class="pt64 pb64 bg-light">
                        <div class="container text-center">
                            <h3>¿No encontraste lo que buscabas?</h3>
                            <p class="mb-4">Contáctanos y con gusto te ayudaremos</p>
                            <a href="/contacto" class="btn btn-primary btn-lg">Contactar</a>
                        </div>
                    </section>

                </div>
            </t>
        </template>
    </data>
</odoo>
```

---

### 5. Página Políticas

**views/page_politicas.xml**
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data>
        <record id="page_politicas" model="website.page">
            <field name="name">Políticas</field>
            <field name="url">/politicas</field>
            <field name="website_published" eval="True"/>
            <field name="is_published" eval="True"/>
            <field name="view_id" ref="view_politicas_template"/>
        </record>

        <template id="view_politicas_template" name="Políticas Page">
            <t t-call="website.layout">
                <div id="wrap">
                    
                    <section class="pt32 pb32 bg-light">
                        <div class="container">
                            <h1>Políticas y Términos</h1>
                        </div>
                    </section>

                    <section class="pt64 pb64">
                        <div class="container">
                            <div class="row">
                                <!-- Sidebar de navegación -->
                                <div class="col-lg-3 mb-4">
                                    <div class="list-group sticky-top" style="top: 80px;">
                                        <a href="#terminos" class="list-group-item list-group-item-action">
                                            Términos y Condiciones
                                        </a>
                                        <a href="#privacidad" class="list-group-item list-group-item-action">
                                            Política de Privacidad
                                        </a>
                                        <a href="#devoluciones" class="list-group-item list-group-item-action">
                                            Política de Devoluciones
                                        </a>
                                        <a href="#envios" class="list-group-item list-group-item-action">
                                            Política de Envíos
                                        </a>
                                    </div>
                                </div>

                                <!-- Contenido principal -->
                                <div class="col-lg-9">
                                    
                                    <!-- Términos y Condiciones -->
                                    <div id="terminos" class="mb-5">
                                        <h2>Términos y Condiciones</h2>
                                        <p class="text-muted"><small>Última actualización: Febrero 2026</small></p>
                                        
                                        <h4>1. Aceptación de términos</h4>
                                        <p>
                                            Al acceder y utilizar este sitio web, aceptas estar sujeto a estos
                                            términos y condiciones de uso, todas las leyes y regulaciones aplicables...
                                        </p>

                                        <h4>2. Uso del sitio</h4>
                                        <p>
                                            Este sitio está destinado únicamente para uso personal y no comercial...
                                        </p>

                                        <!-- Más secciones... -->
                                    </div>

                                    <!-- Política de Privacidad -->
                                    <div id="privacidad" class="mb-5">
                                        <h2>Política de Privacidad</h2>
                                        <p class="text-muted"><small>Última actualización: Febrero 2026</small></p>
                                        
                                        <h4>1. Información que recopilamos</h4>
                                        <p>
                                            Recopilamos información personal como nombre, dirección de correo
                                            electrónico, dirección postal, número de teléfono...
                                        </p>

                                        <!-- Más secciones... -->
                                    </div>

                                    <!-- Más políticas... -->

                                </div>
                            </div>
                        </div>
                    </section>

                </div>
            </t>
        </template>
    </data>
</odoo>
```

---

## Menú Principal

**data/website_menu.xml**
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data>
        <!-- Menú Home -->
        <record id="menu_home" model="website.menu">
            <field name="name">Inicio</field>
            <field name="url">/</field>
            <field name="parent_id" ref="website.main_menu"/>
            <field name="sequence" type="int">10</field>
        </record>

        <!-- Menú Productos -->
        <record id="menu_productos" model="website.menu">
            <field name="name">Productos</field>
            <field name="url">/shop</field>
            <field name="parent_id" ref="website.main_menu"/>
            <field name="sequence" type="int">20</field>
        </record>

        <!-- Menú Nosotros -->
        <record id="menu_nosotros" model="website.menu">
            <field name="name">Nosotros</field>
            <field name="url">/nosotros</field>
            <field name="parent_id" ref="website.main_menu"/>
            <field name="sequence" type="int">40</field>
        </record>

        <!-- Menú Contacto -->
        <record id="menu_contacto" model="website.menu">
            <field name="name">Contacto</field>
            <field name="url">/contacto</field>
            <field name="parent_id" ref="website.main_menu"/>
            <field name="sequence" type="int">50</field>
        </record>

        <!-- Submenú FAQs en footer -->
        <record id="menu_faqs_footer" model="website.menu">
            <field name="name">Preguntas Frecuentes</field>
            <field name="url">/faqs</field>
            <field name="parent_id" ref="website.footer_menu"/>
            <field name="sequence" type="int">10</field>
        </record>

        <!-- Submenú Políticas en footer -->
        <record id="menu_politicas_footer" model="website.menu">
            <field name="name">Políticas</field>
            <field name="url">/politicas</field>
            <field name="parent_id" ref="website.footer_menu"/>
            <field name="sequence" type="int">20</field>
        </record>
    </data>
</odoo>
```

---

## Assets y Estilos

**views/assets.xml**
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <template id="assets_frontend" inherit_id="website.assets_frontend">
        <xpath expr="." position="inside">
            <link rel="stylesheet" href="/ferreteria_web/static/src/css/custom.css"/>
            <script type="text/javascript" src="/ferreteria_web/static/src/js/custom.js"/>
        </xpath>
    </template>
</odoo>
```

**static/src/css/custom.css**
```css
/* Custom Styles - Ferretería Web */

/* Hover effects */
.hover-shadow {
    transition: box-shadow 0.3s ease;
}

.hover-shadow:hover {
    box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15) !important;
}

/* Feature boxes */
.feature-box {
    padding: 20px;
    transition: transform 0.3s ease;
}

.feature-box:hover {
    transform: translateY(-5px);
}

/* Hero section */
.s_banner h1 {
    font-weight: 700;
}

/* Newsletter section */
.s_newsletter {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}

.s_newsletter h3 {
    color: white;
}

/* Category cards */
.card {
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
}

/* Formulario de contacto */
.form-control:focus {
    border-color: #667eea;
    box-shadow: 0 0 0 0.2rem rgba(102, 126, 234, 0.25);
}

/* Accordion para FAQs */
.accordion .btn-link {
    width: 100%;
    text-align: left;
    color: #333;
    text-decoration: none;
    font-weight: 500;
}

.accordion .btn-link:hover {
    color: #667eea;
}

/* Sidebar sticky */
@media (min-width: 992px) {
    .sticky-top {
        position: sticky;
        z-index: 1020;
    }
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .display-3 {
        font-size: 2.5rem;
    }
    
    .display-2 {
        font-size: 2rem;
    }
    
    .pt96 {
        padding-top: 3rem !important;
    }
    
    .pb96 {
        padding-bottom: 3rem !important;
    }
}
```

**static/src/js/custom.js**
```javascript
odoo.define('ferreteria_web.custom', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');

    // Widget para smooth scroll
    publicWidget.registry.SmoothScroll = publicWidget.Widget.extend({
        selector: 'a[href^="#"]',
        events: {
            'click': '_onClickAnchor',
        },

        _onClickAnchor: function (ev) {
            var $target = $($(ev.currentTarget).attr('href'));
            if ($target.length) {
                ev.preventDefault();
                $('html, body').animate({
                    scrollTop: $target.offset().top - 80
                }, 800);
            }
        },
    });

    // Widget para formulario de contacto
    publicWidget.registry.ContactForm = publicWidget.Widget.extend({
        selector: '.s_website_form',
        events: {
            'submit': '_onSubmit',
        },

        _onSubmit: function (ev) {
            // Validaciones adicionales si es necesario
            var $form = $(ev.currentTarget);
            var isValid = true;

            // Validar email
            var email = $form.find('input[type="email"]').val();
            if (email && !this._validateEmail(email)) {
                isValid = false;
                alert('Por favor ingresa un email válido');
            }

            if (!isValid) {
                ev.preventDefault();
            }
        },

        _validateEmail: function (email) {
            var re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return re.test(email);
        },
    });

    return publicWidget.registry;
});
```

---

## Controllers (si se necesitan rutas custom)

**controllers/main.py**
```python
# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class FerreteriaWebController(http.Controller):

    @http.route(['/shop/ofertas'], type='http', auth="public", website=True)
    def shop_ofertas(self, **kwargs):
        """Página de ofertas"""
        products = request.env['product.template'].sudo().search([
            ('website_published', '=', True),
            ('sale_ok', '=', True),
            # Agregar filtro de productos en oferta
        ])
        
        values = {
            'products': products,
            'bins': request.env['product.template']._get_bins(),
        }
        
        return request.render('ferreteria_web.shop_ofertas', values)

    @http.route(['/contacto/submit'], type='http', auth="public", 
                methods=['POST'], website=True, csrf=True)
    def contacto_submit(self, **post):
        """Procesar formulario de contacto"""
        # Crear lead en CRM
        lead_values = {
            'name': post.get('name'),
            'contact_name': post.get('contact_name'),
            'email_from': post.get('email_from'),
            'phone': post.get('phone'),
            'description': post.get('description'),
            'type': 'lead',
        }
        
        lead = request.env['crm.lead'].sudo().create(lead_values)
        
        # Enviar email de confirmación (opcional)
        # template = request.env.ref('ferreteria_web.email_template_contacto')
        # template.send_mail(lead.id, force_send=True)
        
        return request.redirect('/contacto-gracias')
```

---

## Instalación y Actualización

```bash
# Instalar módulo
./odoo-bin -c odoo.conf -d database_name -i ferreteria_web

# Actualizar módulo
./odoo-bin -c odoo.conf -d database_name -u ferreteria_web

# Reiniciar servidor
./odoo-bin -c odoo.conf

# Verificar módulo instalado
# Ir a Apps > Buscar "ferreteria_web" > Debe estar instalado
```

---

## Testing

### Manual Testing Checklist
- [ ] Todas las páginas se cargan correctamente
- [ ] Navegación del menú funciona
- [ ] Formulario de contacto crea leads en CRM
- [ ] Email de confirmación se envía
- [ ] Responsive funciona en mobile/tablet
- [ ] No hay errores en consola del navegador
- [ ] Imágenes se cargan correctamente

### Automated Testing (opcional)
```python
# tests/test_pages.py
from odoo.tests import HttpCase, tagged

@tagged('post_install', '-at_install')
class TestFerreteriaWebPages(HttpCase):

    def test_home_page_loads(self):
        response = self.url_open('/')
        self.assertEqual(response.status_code, 200)

    def test_nosotros_page_loads(self):
        response = self.url_open('/nosotros')
        self.assertEqual(response.status_code, 200)

    def test_contacto_form_creates_lead(self):
        # Test form submission
        pass
```

---

## Troubleshooting

### Problemas Comunes

**1. Página no se muestra**
- Verificar que el módulo esté instalado
- Verificar que `is_published` esté en `True`
- Limpiar caché del navegador
- Actualizar módulo: `./odoo-bin -u ferreteria_web`

**2. Estilos no se aplican**
- Verificar que assets.xml esté correcto
- Modo desarrollador: Regenerar assets
- Limpiar caché de Odoo

**3. Formulario no envía**
- Verificar que website_crm esté instalado
- Verificar CSRF token
- Revisar logs de Odoo para errores

**4. Imágenes no cargan**
- Verificar rutas de archivos
- Subir imágenes a Media Library de Odoo
- Verificar permisos de archivos

---

## Mantenimiento

### Actualizaciones de Contenido
El cliente puede editar contenido desde:
- Website Builder (drag & drop)
- Backend: Website > Pages
- Backend: Website > Menus

### Backup
- Backup regular de base de datos
- Backup de filestore (imágenes)
- Versionado de código en Git

---

## Próximos Pasos (Post-Fase 4)

1. **Fase 5**: Implementar PLP/PDP (listados y fichas de producto)
2. **Fase 6**: Configurar checkout, pagos y envíos
3. **Fase 7**: Optimización SEO
4. **Fase 8**: Integraciones (GA4, CRM externo, etc.)
5. **Fase 9**: QA y Go-live

---

**Fecha de creación**: 2026-02-24  
**Última actualización**: 2026-02-24  
**Versión**: 1.0  
**Autor**: Conceptual Dynamic
