# Ajustes del proyecto

La ventana **Ajustes del proyecto** reúne lo que es común a todo el juego.
Se abre con **Proyecto → Ajustes del proyecto…** y tiene cinco páginas:
**General**, **Rejilla y materiales**, **Módulos**, **Acciones de
entrada** y **Gráficos**.

![La ventana Ajustes del proyecto sobre el editor](../imagenes/capturas/ajustes-proyecto.png)

## General

![Ajustes del proyecto](../imagenes/capturas/panel-ajustes-proyecto.png)

| Opción | Descripción |
|---|---|
| **Nombre** | El nombre del proyecto en la pantalla de inicio y en la barra del editor. Cambiarlo no cambia el nombre de la carpeta |
| **Autor** | La persona o el estudio que hace el juego |
| **Versión** | La versión del juego, por ejemplo `0.1.0` |
| **Descripción** | Una frase sobre el juego. Se muestra en la lista de proyectos |
| **Tipo** | El tipo de proyecto elegido al crearlo. No se puede cambiar |
| **Escena inicial** | La escena con la que empieza el juego al pulsar **Desde el inicio** y en el juego publicado |
| **Icono** | Una imagen de la carpeta `imagenes/` del proyecto (preferiblemente cuadrada). **El del motor** usa el icono de Foxy Engine |

Pulsa **Guardar** para aplicar los cambios. Se escriben en el archivo
`proyecto.ron`, en la carpeta del proyecto.

> <i class="fx fx-nota"></i> **Nota.** La escena inicial también se puede
> cambiar desde el panel **Proyecto**, con el botón derecho sobre una escena.

## Rejilla y materiales

| Opción | Descripción |
|---|---|
| **Tamaño del cubito** | La medida de cada cubito del terreno y de los objetos de vóxeles: **1 m**, **50 cm** (el de fábrica) o **25 cm**. Un cubito más pequeño da más detalle y más trabajo al ordenador |

> <i class="fx fx-aviso"></i> **Importante.** Los mundos y los objetos se miden
> en cubitos: al cambiar el tamaño, lo ya construido cambia de tamaño con
> él. Conviene elegirlo al empezar el proyecto. Al guardar, el editor guarda
> las escenas y vuelve a abrir el proyecto.

Los materiales del proyecto se editan en el panel
[Materiales](../guia/materiales.md). Un proyecto creado con la plantilla
**Vacío 3D** no usa los 16 materiales de fábrica del motor (salvo el agua):
empieza con seis propios, *Suelo*, *Tierra*, *Roca*, *Madera*, *Cristal* y
*Luz*. Las plantillas de isla traen los de fábrica.

## Módulos

Activa o desactiva cada [módulo](../referencia/modulos/index.md) del motor
para todo el proyecto: día y noche, clima, estaciones, vecinos, romper
bloques, líquidos y escombros. Cada escena puede cambiarlos en su
inspector.

## Acciones de entrada

Qué tecla, botón del ratón y botón del mando hace cada acción del juego, y
las acciones propias del proyecto. Ver
[Acciones de entrada](../guia/acciones-entrada.md).

## Gráficos

Cómo se ve el juego. Los cambios se ven al momento en la escena.

| Opción | Descripción |
|---|---|
| **Exposición** | Más luz (+) o menos (−), como en una cámara: +1 es el doble |
| **Tono** | Cómo pasa la luz a colores: **Cine (ACES)**, **Como Blender (AgX)**, **Neutro** o **Ninguno** |
| **Calidad del juego** | La calidad con la que empieza el juego. Cada jugador la cambia en **Opciones → Gráficos** |
| **Luz y atmósfera** | Luz que rebota, rincones más oscuros, agua de verdad, cielo físico, destello, desenfoque, suavizado temporal, escala del dibujo y color. **Realista** las enciende todas y **Apagar todo** las quita |
| **Piezas del dibujo** | Apaga sombras, luces, cielo, niebla, agua o transparentes |

**Volver a como venía** deja la página como al principio. Todo se explica en
[Gráficos: luz, sombras y atmósfera](../guia/graficos.md).

## Véase también

- [Archivos del proyecto: proyecto.ron](../referencia/archivos.md#proyecto)
- [Módulos](../referencia/modulos/index.md)
- [Escenas](../guia/escenas.md)
- [Gráficos: luz, sombras y atmósfera](../guia/graficos.md)
- [Pixel art](../guia/pixel-art.md)
