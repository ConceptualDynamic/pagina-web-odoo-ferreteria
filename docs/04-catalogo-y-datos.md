# Catálogo y datos

## 1) Objetivo
Garantizar que cada SKU tenga información suficiente para vender, comparar y evitar errores de compra.

## 2) Plantilla maestra de productos (campos mínimos)
- SKU (único)
- Nombre comercial
- Categoría / subcategoría
- Marca
- Descripción corta (beneficio)
- Descripción técnica (especificaciones)
- Unidad de medida
- Precio
- Impuesto aplicable
- Stock disponible
- Estado (activo/inactivo)
- Peso/dimensiones (si aplica)
- Imágenes (mínimo 2)
- Palabras clave SEO

## 3) Reglas de calidad de datos
- SKU único obligatorio.
- Nombre sin ambigüedad (marca + tipo + medida clave).
- Descripción técnica verificable.
- Precio y stock sin valores nulos al publicar.
- Imágenes nítidas y consistentes en formato.

## 4) Modelo de naming recomendado
`[TipoProducto] [Marca] [Modelo/Medida] [Uso]`
Ejemplo: `Taladro Percutor Bosch GSB13RE 650W`

## 5) Atributos por familia (ejemplos)
- Taladros: potencia, mandril, velocidad, tipo de uso.
- Tornillería: diámetro, largo, material, cabeza, rosca.
- Pintura: tipo, rendimiento, acabado, color.

## 6) Proceso de carga
1. Preparación en plantilla maestra.
2. Validación automática (duplicados/campos obligatorios).
3. Carga en entorno staging.
4. Revisión visual y funcional.
5. Publicación controlada en producción.

## 7) Control de duplicados
- Regla por SKU.
- Regla secundaria por nombre + marca + medida.
- Revisión manual de excepciones.

## 8) Gobernanza y roles
- Data owner catálogo: aprueba estructura y calidad.
- Cargador operativo: ejecuta importaciones.
- QA catálogo: valida fichas y consistencia.

## 9) KPI de calidad de catálogo
- % SKUs completos (objetivo >95%).
- % SKUs con imagen principal + secundaria (objetivo >90%).
- Tasa de errores de carga por lote (objetivo <2%).

## 10) Checklist pre-publicación de lote
- Campos obligatorios completos.
- Precios e impuestos correctos.
- Stock > 0 para productos visibles.
- URLs y slugs correctos.
- Muestra de productos validada manualmente.
