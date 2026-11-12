# Crear un proyecto

Un proyecto nuevo se crea con el asistente de la pantalla de inicio: se
elige qué juego vas a hacer, el nombre y la carpeta donde se guarda.

![El asistente de proyecto nuevo](../imagenes/capturas/inicio-nuevo.png)

## Pasos

1. En la pantalla de inicio, pulsa **Nuevo proyecto**
   (<kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>N</kbd>). También puedes elegir una
   tarjeta en la sección **Plantillas**.
2. En **¿Qué juego quieres hacer?**, elige una plantilla. Están agrupadas
   por tipo de juego y la imagen de la derecha muestra cómo es. Si no sabes
   cuál, empieza por **Vacío 3D** o **Vacío 2D**.
3. Escribe el **Nombre** del proyecto.
4. Si quieres guardarlo en otro sitio, pulsa **Cambiar…** en **Ubicación**.
   Debajo se indica la carpeta exacta que se va a crear.
5. Pulsa **Crear proyecto** o <kbd>Intro</kbd>.

El editor abre el proyecto nuevo y lo añade a la lista de proyectos. La
primera vez, el [tutorial guiado](modo-sencillo.md#el-tutorial-guiado)
enseña las partes del editor en ocho pasos cortos.

![El asistente, en detalle](../imagenes/capturas/panel-asistente.png)

## Las plantillas

![Las plantillas disponibles](../imagenes/capturas/inicio-plantillas.png)

Cada plantilla es un juego pequeño que ya funciona: se pulsa **Jugar aquí**
y se juega. Sus objetos traen [comportamientos](../guia/comportamientos.md)
ya puestos, así que basta elegir uno para ver cómo está hecho y cambiarlo.
La sección [Tu primer juego](../tu-primer-juego/index.md) tiene un tutorial
para cada una.

| Tipo de juego | Plantilla | Qué incluye | Tutorial |
|---|---|---|---|
| **Empezar de cero** | **Vacío 3D** | Un llano de 96 × 96 m y el punto de inicio. Nada más | [Desde cero](../tu-primer-juego/desde-cero.md) |
| | **Vacío 2D** | Un suelo de casillas, el cielo y un zorro que salta | [Tu primer juego 2D](primer-juego-2d.md) |
| **Plataformas** | **Plataformas 2D** | Un nivel de pixel art con monedas que flotan, escaleras, pinchos, agua y una bandera de meta | [Plataformas](../tu-primer-juego/plataformas.md) |
| | **Plataformas vóxel** | Un nivel de cubitos visto de lado, con cámara fija y monedas que giran | [Plataformas](../tu-primer-juego/plataformas.md) |
| **Vista desde arriba** | **Aventura cenital** | Un prado visto desde arriba con camino, lago, una vecina y gemas que buscar | [Vista desde arriba](../tu-primer-juego/vista-desde-arriba.md) |
| **3D en tercera persona** | **Aventura en tercera persona** | Monedas que giran, una babosa que patrulla, una plataforma que sube y un botón que abre la puerta de la estrella | [Tercera persona](../tu-primer-juego/tercera-persona.md) |
| **Puzle** | **Puzle de botones** | Tres botones de colores y tres puertas que hay que abrir a la vez | [Puzle](../tu-primer-juego/puzle.md) |
| **Mundo de cubitos** | **Isla vóxel** | Una isla generada con colinas, playa, árboles y muelle, sin construcciones | [Mundo de cubitos](../tu-primer-juego/mundo-de-cubitos.md) |
| | **Isla de ejemplo** | Una isla con pueblo, mercado, vecinos, pelotas y un guion de ejemplo | [Mundo de cubitos](../tu-primer-juego/mundo-de-cubitos.md) |
| **Más ejemplos** | **Personaje animado** | Un personaje que anda, corre y salta, una puerta que se abre sola y una cinemática | [Animación](../guia/animacion.md) |
| | **Demo técnica** | El templo del zorro en la cumbre de un monte junto al mar, con una ciudad griega, un puerto y una cinemática | [Demo técnica](../tu-primer-juego/demo-tecnica.md) |

Cada plantilla trae **solo lo que usa**: los objetos, los comportamientos y
los módulos de su juego. El motor no añade nada más, así que un proyecto
vacío está vacío de verdad. Todo lo que trae una plantilla forma parte del
proyecto y se puede cambiar o borrar.

### Qué clase de proyecto crea cada una

Las plantillas 3D crean un proyecto **3D vóxel**; Vacío 2D, Plataformas 2D
y Aventura cenital, uno **2D pixel art**, y Plataformas vóxel, uno **2D con
vóxeles** (cubitos vistos de lado). La clase sale en la esquina de cada
fila del asistente. Los juegos 2D se explican en
[Juegos 2D](../guia/juegos-2d.md).

## Dónde se guardan los proyectos

Por defecto, los proyectos se crean en `Documentos/Foxy Engine/proyectos/`,
cada uno en su propia carpeta con el nombre del proyecto. Si ya existe una
carpeta con ese nombre, se añade un número (`Mi juego 2`).

```text
Documentos/
  Foxy Engine/
    Foxy Engine.app        el motor (en Mac)
    proyectos/
      Mi juego/            un proyecto
    editor.ron             proyectos recientes y fijados
    preferencias.ron       preferencias del motor
    registro.txt           registro de la última sesión
```

> <i class="fx fx-consejo"></i> **Consejo.** Instalar una versión nueva del
> motor solo sustituye la aplicación. Los proyectos y las preferencias se
> conservan.

## Véase también

- [La pantalla de inicio](pantalla-de-inicio.md)
- [Tu primer juego](../tu-primer-juego/index.md)
- [Modo Sencillo y tutorial guiado](modo-sencillo.md)
- [Archivos del proyecto](../referencia/archivos.md)
