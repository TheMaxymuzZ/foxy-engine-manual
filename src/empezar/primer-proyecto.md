# Tu primer proyecto

Cada juego que haces con Foxy Engine es un **proyecto**: una carpeta con tus
mundos, objetos, imágenes, interfaces y guiones. En este capítulo vas a crear
uno, cambiar algo y jugarlo, en unos diez minutos.

## Dónde viven los proyectos

```text
Documentos/
  Foxy Engine/
    Foxy Engine.app        el motor (en Mac)
    proyectos/
      Mi isla/             un proyecto
      La cueva/            otro
    ajustes.ron            tus opciones de juego
```

Instalar una versión nueva del motor solo cambia la app; los proyectos se
quedan como estaban.

## 1. Crea el proyecto

En el menú **Archivo → 📁 Proyecto nuevo…**:

1. Escribe un nombre, por ejemplo *Isla del faro*.
2. Elige con qué empieza:
   - **Plaza de prueba**: una isla con casas, un mercado, vecinos y pelotas.
     Ideal para aprender.
   - **Isla vacía**: solo el terreno y el punto de inicio.
3. Pulsa **Crear**.

El editor abre el proyecto. A partir de ahora, cada vez que abras Foxy Engine
volverá a este proyecto. Para cambiar de proyecto usa **Archivo → 📂 Abrir
proyecto…**, y para ver sus archivos, **Archivo → 🔍 Ver la carpeta del
proyecto**.

## 2. Muévete por el mundo

| Para | Haz |
|---|---|
| Volar | <kbd>W</kbd> <kbd>A</kbd> <kbd>S</kbd> <kbd>D</kbd> |
| Subir y bajar | <kbd>Espacio</kbd> y <kbd>Mayús</kbd> |
| Mirar alrededor | Arrastra con el botón derecho (o mantén <kbd>Cmd</kbd>/<kbd>Ctrl</kbd> y mueve el ratón) |
| Acercarte | La rueda del ratón |

## 3. Pon algo

1. Elige **Colocar objetos** en el panel de la izquierda (o pulsa <kbd>O</kbd>).
2. Elige **Farola** en la lista.
3. Haz clic en el suelo. Con <kbd>R</kbd> la giras antes de ponerla.

Ahora elige **Poner bloques** (<kbd>B</kbd>), escoge el material *Grava* y
arrastra por el suelo para hacer un camino.

## 4. Pruébalo

Pulsa **▶ Jugar aquí** (<kbd>F5</kbd>). Apareces de pie justo donde miraba
la cámara. Anda con <kbd>W</kbd> <kbd>A</kbd> <kbd>S</kbd> <kbd>D</kbd>,
salta con <kbd>Espacio</kbd> y dale una patada a una pelota con
<kbd>E</kbd>. Pulsa <kbd>F5</kbd> otra vez para volver al editor, justo
donde estabas.

![Jugar aquí](../imagenes/capturas/fase2-jugar-aqui.png)

## 5. Guarda

**💾 Guardar** (<kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>S</kbd>). El botón muestra
un punto (`Guardar •`) cuando hay cambios sin guardar. Si cierras el editor con
cambios pendientes, te pregunta antes.

> **Consejo.** Todo se guarda como texto. Puedes abrir
> `mundos/principal.ron` con cualquier editor y ver tu farola ahí escrita.
> Más en [Archivos del proyecto](../referencia/archivos.md).

## Siguiente paso

Lee [Un vistazo al editor](editor.md) para conocer cada panel, o salta
directamente a [Construir el mundo](../guia/mundo.md).
