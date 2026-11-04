# Primeros pasos en el editor

Esta página recorre las tareas básicas del editor con un proyecto recién
creado: moverse por el mundo, construir, colocar objetos, probar el juego y
guardar. Se completa en unos diez minutos.

Antes de empezar, crea un proyecto con la plantilla **Vacío 3D** (consulta
[Crear un proyecto](crear-proyecto.md)).

![Un proyecto vacío recién creado](../imagenes/capturas/proyecto-vacio.png)

## 1. Moverse por el mundo

| Acción | Control |
|---|---|
| Desplazarse | <kbd>W</kbd> <kbd>A</kbd> <kbd>S</kbd> <kbd>D</kbd> |
| Subir y bajar | <kbd>Espacio</kbd> y <kbd>Mayús</kbd> |
| Mirar alrededor | Arrastrar con el botón derecho, o mantener <kbd>Cmd</kbd>/<kbd>Ctrl</kbd> y mover el ratón |
| Acercarse y alejarse | Rueda del ratón |

La lista completa está en **Ayuda → <i class="fx fx-teclado"></i> Teclas y
ratón…** y en [Atajos de teclado](../referencia/atajos.md).

## 2. Construir

1. En la tira de herramientas, a la izquierda de la vista, elige
   <i class="fx fx-poner"></i> **Poner bloques** (<kbd>B</kbd>).
2. En el inspector, a la derecha, elige el material **Grava**.
3. Arrastra sobre el suelo para trazar un camino.

Para deshacer, pulsa <kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>Z</kbd>.

## 3. Colocar un objeto

1. Elige <i class="fx fx-colocar"></i> **Colocar objetos** (<kbd>O</kbd>).
2. En el inspector, elige **Farola**.
3. Pulsa <kbd>R</kbd> para girarla y haz clic en el suelo para colocarla.

## 4. Probar el juego

Pulsa <i class="fx fx-jugar"></i> **Jugar aquí** (<kbd>F5</kbd>). El
jugador aparece donde mira la cámara. Se mueve con <kbd>W</kbd>
<kbd>A</kbd> <kbd>S</kbd> <kbd>D</kbd> y salta con <kbd>Espacio</kbd>.
Pulsa <kbd>F5</kbd> de nuevo para volver al editor en el mismo punto.

![Probando el juego con Jugar aquí](../imagenes/capturas/fase2-jugar-aqui.png)

## 5. Guardar

Pulsa <i class="fx fx-guardar"></i> **Guardar**
(<kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>S</kbd>). El botón muestra
**Guardar •** mientras hay cambios pendientes y **Guardado** cuando todo
está a salvo. Al guardar se actualiza también la miniatura del proyecto en la
pantalla de inicio.

> <i class="fx fx-aviso"></i> **Importante.** Al cerrar el proyecto o el
> motor con cambios sin guardar, el editor pregunta qué hacer. Si eliges
> **No guardar**, los cambios se pierden.

> <i class="fx fx-consejo"></i> **Consejo.** Todo se guarda como texto. El
> archivo `mundos/principal.ron` se puede abrir con cualquier editor de
> texto, y en él aparece la farola que acabas de colocar.

## Siguientes pasos

- [La interfaz del editor](editor.md): para qué sirve cada panel.
- [Construir el mundo](../guia/mundo.md): pinceles, simetría y extrusión.
- [Nodos](../guia/nodos.md): dar comportamiento al juego sin escribir código.
