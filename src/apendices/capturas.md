# Capturas del manual

Todas las capturas de este manual las hace el propio motor, sin ventana, con
los mismos proyectos de ejemplo y el mismo tamaño (1440 × 860). Así se
pueden rehacer todas en cada versión y ninguna se queda vieja.

## Rehacer las capturas

Hace falta una copia del motor compilada y Python 3 con Pillow.

1. Compila el motor: en la carpeta de `foxy-engine`, ejecuta
   `cargo build --release`.
2. En la carpeta del manual, ejecuta:

   ```sh
   python3 herramientas/capturas.py --motor ../foxy-engine/target/release/foxy-engine
   ```

El guion hace, en este orden:

1. Escribe la versión del motor en `theme/version.js`, que la muestra en
   todas las páginas.
2. Pone al día las referencias generadas: componentes, nodos y API de Lua.
3. Rehace cada captura de la lista y le pone sus números, si es una captura
   anotada.

| Opción | Para qué |
|---|---|
| `--solo panel- inicio` | Solo las capturas cuyo nombre empieza así |
| `--escaparate` | Rehace también las animaciones de la portada (tarda unos minutos) |
| `--sin-capturas` | Solo la versión y las referencias (con `--escaparate`, solo las animaciones) |
| `--lista` | Muestra todas las capturas y la orden de cada una |

## Cómo se hace una captura

Cada captura es una orden de `foxy-engine --captura` (ver
[Línea de comandos](../referencia/linea-de-comandos.md)). Por ejemplo, la
del Inspector es:

```sh
foxy-engine --captura panel-inspector.png --ancho 1440 --alto 860 \
  --editor --pestana proyecto --elegir 2 --recortar inspector
```

`--recortar` guarda solo ese panel, con su pestaña. Las capturas de diálogos
se recortan de la captura de pantalla completa.

## Capturas anotadas

Las capturas de los paneles llevan **números** naranjas que se explican en
la tabla de debajo. La posición de cada número está en
`herramientas/anotaciones.py`, en píxeles de la imagen. Si un panel cambia
de forma, basta con mover sus números ahí y volver a ejecutar el guion.

## Capturas hechas a mano

Unas pocas capturas necesitan algo que una sola orden no puede hacer: dos
ventanas a la vez, el juego publicado abierto o una casa cayendo. Están en la
lista `A_MANO` del guion, con la razón, y se rehacen a mano cuando cambia lo
que muestran.

## Véase también

- [Guía de estilo](https://github.com/TheMaxymuzZ/foxy-engine-manual/blob/main/GUIA-DE-ESTILO.md)
- [Línea de comandos](../referencia/linea-de-comandos.md)
