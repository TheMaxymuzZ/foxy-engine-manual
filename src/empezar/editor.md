# Un vistazo al editor

![El editor](../imagenes/capturas/fase4-editor.png)

El editor tiene cuatro zonas:

1. **Barra de arriba**: el menú *Archivo*, las pestañas y los botones de
   *Deshacer*, *Rehacer*, *Guardar*, *▶ Jugar aquí* y *🎮 Desde el inicio*.
2. **Panel de la izquierda**: las herramientas, el pincel, los materiales,
   los objetos que puedes colocar y la **escena** (la lista de todo lo que hay
   en el mundo, ordenada en carpetas).
3. **Vista central**: el mundo, donde trabajas con el ratón.
4. **Panel de la derecha**: las propiedades de lo que tengas elegido o, sin
   nada elegido, las del mundo entero.

## Las pestañas

Arriba hay pestañas, como en un navegador. Cada una es un espacio de trabajo:

| Pestaña | Para qué | Capítulo |
|---|---|---|
| **🌍 Mundo** | La escena que estás editando, con sus paneles. Su menú **🗺 Escenas** cambia de escena | [Construir el mundo](../guia/mundo.md) |
| **📜 Guion** | El guion Lua del mundo, con *Comprobar* y una consola | [Guiones en Lua](../guia/guiones.md) |
| **📦 Objeto** | Un objeto propio abierto en el creador (una pestaña por objeto) | [Crear objetos propios](../guia/creador.md) |
| **🎨 Pixel art** | Imágenes, paletas y materiales del proyecto | [Pixel art](../guia/pixel-art.md) |
| **🖊 Imagen** | Una imagen abierta en el lienzo de pixel art | [Pixel art](../guia/pixel-art.md) |
| **🖼 Interfaces** | Menús, marcadores y carteles (una pestaña por interfaz) | [Interfaces](../guia/interfaces.md) |

Las pestañas con cambios sin guardar llevan un punto (•). La ✖ las cierra.

## Deshacer y guardar

Casi todo se puede deshacer con <kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>Z</kbd> y
rehacer con <kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>Mayús</kbd>+<kbd>Z</kbd>.
Cada pestaña tiene su propio historial: deshacer en un objeto no toca el mundo.

<kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>S</kbd> guarda lo que tengas delante.

## La barra de estado

Abajo, el editor dice qué mundo tienes abierto y avisa si algo no va bien,
por ejemplo si el mundo usa un objeto que el motor no conoce.

## Probar

- **▶ Jugar aquí** (<kbd>F5</kbd>): juegas al momento desde el punto al que
  mira la cámara. <kbd>F5</kbd> vuelve al editor.
- **🎮 Desde el inicio**: abre el juego completo, con su menú principal, y
  empiezas en el punto de inicio de la escena inicial.

Más en [Probar el juego](../guia/jugar.md).
