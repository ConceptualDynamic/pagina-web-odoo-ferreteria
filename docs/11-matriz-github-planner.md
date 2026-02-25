# Matriz de vínculo GitHub Project ↔ Planner

## 1) Propósito
Mantener trazabilidad completa entre planificación técnica (GitHub) y ejecución operativa diaria (Planner) para el proyecto de ferretería.

## 2) Regla base de operación
- **GitHub Project:** visión macro, roadmap, dependencias y estado técnico.
- **Planner:** asignación por persona, fechas operativas y seguimiento diario.

## 3) Estructura recomendada en GitHub
### Campos mínimos de Issue
- Título: `[Fase X] Título corto`
- Descripción: contexto, alcance, criterios de aceptación.
- Labels: `proyecto:ferreteria`, `fase:X`, `tipo:(feature/bug/task)`.
- Estado: Backlog / En curso / Bloqueado / Done.
- Responsable técnico.
- Fecha objetivo.
- URL de tarea Planner vinculada.

## 4) Estructura recomendada en Planner
### Campos mínimos de tarea
- Título espejo del issue.
- Asignado.
- Prioridad operativa.
- Fecha de vencimiento.
- Checklist ejecutable.
- URL de Issue/PR en GitHub.
- Etiqueta de proyecto + etiqueta de fase.

## 5) Campos espejo (mapeo)
- Estado:
  - GitHub `Backlog` ↔ Planner `No iniciado`
  - GitHub `En curso` ↔ Planner `En proceso`
  - GitHub `Bloqueado` ↔ Planner `Bloqueado`
  - GitHub `Done` ↔ Planner `Completado`
- Prioridad:
  - GitHub `P1/P2/P3` ↔ Planner `Urgente/Importante/Media`
- Owner:
  - GitHub `assignee` ↔ Planner `assignedTo`
- Fecha objetivo:
  - Sincronización manual diaria (o semiautomática cuando aplique)

## 6) Flujo operativo estándar
1. Crear issue en GitHub (definición técnica).
2. Crear tarea espejo en Planner (ejecución).
3. Vincular URLs cruzadas en ambos lados.
4. Actualizar estado en ambos tableros al menos 1 vez/día.
5. Cerrar issue solo cuando Planner esté completado y validado.

## 7) Reglas de calidad de seguimiento
- No debe existir issue “En curso” sin tarea Planner vinculada.
- Toda tarea Planner debe tener una fase (`fase:X`) y etiqueta de proyecto.
- Bloqueos deben registrar causa, fecha y responsable de desbloqueo.
- Cambios de fecha deben dejar comentario con motivo.

## 8) Cadencia de sincronización recomendada
- Corte AM: revisar prioridades y bloqueos.
- Corte PM: actualizar avances y riesgo de vencimientos.
- Cierre semanal: reporte de hitos, desvíos y acciones correctivas.

## 9) Plantillas sugeridas
### Issue GitHub (resumen)
- Contexto
- Objetivo
- Alcance
- Criterios de aceptación
- Dependencias
- Riesgos
- Link Planner

### Tarea Planner (resumen)
- Entregable concreto
- Checklist operativo
- Fecha compromiso
- Responsable
- Link GitHub

## 10) Indicadores de gobernanza
- % issues con link a Planner.
- % tareas con fase + proyecto.
- Tiempo promedio en estado bloqueado.
- Cumplimiento de fechas por fase.
