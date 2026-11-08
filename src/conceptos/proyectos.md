# Proyectos, escenas y recursos

Todo lo que se hace en Foxy Engine pertenece a un **proyecto**. Un proyecto
es una carpeta que contiene las **escenas** del juego y los **recursos** que
usan: objetos, materiales, imágenes, interfaces y guiones.

## Proyecto

Un proyecto es un juego. Su carpeta puede estar en cualquier lugar del
ordenador y se identifica por el archivo `proyecto.ron`, que guarda su
nombre, su tipo, su autor, su versión, su icono y la escena inicial.

Al estar formado solo por archivos de texto e imágenes, un proyecto se puede
copiar a otro ordenador, enviar comprimido o guardar en un repositorio de
Git sin ninguna conversión.

## Escena

Una escena es un lugar del juego: una isla, una cueva, el interior de una
casa. Cada escena es un archivo de `mundos/` con su terreno, los objetos
colocados y cómo pasa el tiempo en ella. Las escenas se conectan entre sí con
zonas y puntos de entrada. Más información en [Escenas](../guia/escenas.md).

## Recursos

Los recursos son las piezas que usan las escenas. Se crean en el editor y
se guardan en su propia carpeta:

| Recurso | Carpeta | Se crea en |
|---|---|---|
| Objetos propios | `objetos/` | [Creador de objetos](../guia/creador.md) |
| Materiales | `materiales.ron` | [Materiales](../guia/materiales.md) |
| Imágenes y paletas | `imagenes/`, `paletas/` | [Pixel art](../guia/pixel-art.md) |
| Interfaces | `interfaces/` | [Interfaces](../guia/interfaces.md) |
| Guiones y nodos | `guiones/`, `grafos/`, `funciones/`, `nodos/` | [Nodos](../guia/nodos.md) y [Programar en Lua](../guia/programar-lua.md) |
| Objetos reutilizables | `prefabricados/` | [Objetos reutilizables](../guia/reutilizables.md) |
| Sonidos | `sonidos/` | Arrastrando archivos WAV u OGG ([Sonidos](../guia/sonidos.md)) |

Un mismo recurso se puede usar en todas las escenas del proyecto: al
cambiarlo, cambia en todas.

## Datos del editor

La carpeta `.foxy/` del proyecto guarda datos que genera el editor, como la
miniatura de la pantalla de inicio. Se puede borrar sin perder nada del
juego: el editor la vuelve a crear.

## Véase también

- [Conceptos básicos](basicos.md)

- [Archivos del proyecto](../referencia/archivos.md)
- [Glosario](../apendices/glosario.md)
