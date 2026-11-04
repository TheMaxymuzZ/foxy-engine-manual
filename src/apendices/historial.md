# Historial de versiones

Foxy Engine se construye por fases. Cada fase deja el motor funcionando.

La versión que sale al abrir el editor, como `0.0.1-PR15`, junta la versión
del motor con el número del último cambio (*pull request*) incorporado.

## 0.0.1-PR20: nodos

- **[Nodos](../guia/nodos.md)**: guiones sin código, con cajas *Cuándo*,
  *Si* y *Hacer* unidas por cables. Se convierten en Lua y se cargan junto
  a `mundo.lua`.

## 0.0.1-PR19: romper bloques, derrumbes y agua

- **[Romper bloques](../guia/jugar.md#romper-bloques)** jugando, según los
  golpes de cada material.
- Lo que se queda sin apoyo **se derrumba** y cae con física (Rapier); al
  pararse, deja ruinas.
- El **agua corre** por los huecos que se abren y se retira si se tapan.
- Ajuste **Romper bloques** en la vida de la escena.

## 0.0.1-PR18: mundos más ligeros

- Las caras iguales que están juntas se dibujan como un solo rectángulo: la
  isla de prueba pasa de 746 000 a 304 000 triángulos y se ve igual.
- Al abrir otra escena, regenerar el terreno o cambiar los materiales, el
  mundo nuevo se prepara en segundo plano (los trozos más cercanos primero)
  mientras se sigue viendo el de antes. Abajo a la derecha sale
  **Preparando el mundo…** con su barra.

## 0.0.1-PR17: importar modelos, extruir y simetría

- **[Importar modelos](../guia/importar.md)** de MagicaVoxel (`.vox`) y
  Qubicle (`.qb`), como objeto propio o directamente en la escena, con un
  material propio para cada color.
- Herramienta **[Extruir](../guia/mundo.md#extruir)** (<kbd>X</kbd>): saca o
  mete una capa de toda una cara.
- **[Simetría](../guia/mundo.md#simetría)** en X, Y y Z al poner, quitar,
  pintar y extruir, en el mundo y en el creador de objetos.
- Los objetos propios pueden medir hasta 64 cubitos (32 m) de lado.

## 0.0.1-PR16: materiales, luces y archivos

- **[Paleta de materiales](../guia/materiales.md)**: materiales propios con
  color, textura y atributos (luz propia, metálico, pulido, transparencia,
  atravesable, golpes y peso). Plantillas de oro, hierro, lava, neón, hielo y
  mármol.
- **Usar como textura** desde cualquier imagen de pixel art, y **Dibujar…**
  desde un material.
- Los materiales que brillan **iluminan alrededor**; sombras más finas cerca
  de la cámara; el cristal es transparente.
- **[Gestor de archivos](../guia/archivos.md)**: carpetas, mover, renombrar,
  papelera e importar (también arrastrando archivos sobre la ventana).
- **[Preferencias](../guia/preferencias.md)** con sincronía vertical (adiós a
  los tirones de la cámara) y asignación de teclas.
- **Ayuda → Manual de Foxy Engine** abre este manual.

![Farolas de noche](../imagenes/capturas/farolas-de-noche.png)

## 0.0.1-PR15: Windows

- En Windows, los gráficos se prueban uno a uno: primero **DirectX 12**,
  después Vulkan y por último OpenGL. Arregla el motor que se cerraba sin
  avisar al abrirse en algunos ordenadores.
- [Registro](problemas.md#el-registro-registrotxt) en
  `Documentos/Foxy Engine/registro.txt` y una ventana de aviso si el motor
  se cierra por un error.
- El `.exe` de Windows ya no abre la ventana negra de consola.

## 0.0.1-PR14: el editor, ordenado

- **Barra de menús** (*Archivo*, *Editar*, *Crear*, *Ver* y *Ayuda*), panel
  **«Proyecto»** a la izquierda con todo el proyecto, **tira de
  herramientas** dentro de la vista e **inspector** a la derecha. Las
  pestañas son solo de lo que está abierto.
- **Ayuda → Teclas y ratón…**, con todas las teclas.
- **Proyecto vacío**: un llano de hierba, el punto de inicio y un guion con
  las funciones vacías. Nuevo terreno **Llano vacío**, también para escenas.
- **Al usarlo (E)**: cualquier casa u objeto propio puede llevar a otra
  escena, abrir una interfaz o llamar al guion.
- Las escenas nuevas pueden quedar **ya conectadas**, con zonas de ida y
  vuelta.
- Las pantallas pueden abrirse con **su propia tecla**, y cada interfaz dice
  **cómo se abre en el juego**.
- Avisos <i class="fx fx-aviso"></i> de escenas a las que no se llega y de
  interfaces que nada abre.
- El editor gasta menos: las sombras solo se redibujan si cambia algo, y
  dibuja más despacio cuando nadie lo toca.

## 0.0.1-PR13: la marca

- El editor se abre con el logo horizontal y la versión; los juegos enseñan
  *Powered by Foxy Engine*.
- Identidad visual: el zorro, los iconos de la app y la pantalla *Powered by
  Foxy Engine*.

## Escenas e interfaces

- Varias escenas por proyecto, mapa de escenas, puntos de entrada y zonas de
  cambio.
- Editor de interfaces: menús, marcadores y carteles, con acciones sin código.
- Valores del guion que se enseñan en las interfaces y se guardan con la
  partida.
- Editor de pixel art: imágenes, paletas, texturas para los materiales e
  imágenes que se estiran en nueve partes.

## Extras del editor

- Proyectos, cada uno en su carpeta.
- Creador de objetos en su propia pestaña.
- Carpetas en la escena y modo cursor.

## Fase 4: vida

- Guiones en Lua, con consola y *Comprobar*.
- Vecinos que pasean, miran y hablan.
- Día y noche, estaciones y clima con lluvia, nieve y tormentas.
- Música y efectos de sonido.

## Fase 3: se puede jugar

- Primera persona con física: escalones, agacharse, saltar.
- Teclado, ratón y mando.
- Menú principal, pausa, opciones y partidas guardadas.
- Pelotas con física.

## Fase 2: editor

- Paneles, pincel de bloques, objetos, deshacer y guardar.
- *Jugar aquí*.

## Fase 1: mundo de bloques

- Rejilla fina de cubitos, trozos, luz, sombras, agua y niebla.
- Isla de prueba generada y cámara libre.

## Fase 0: cimientos

- Ventana, modo sin ventana para capturas e integración continua para Mac,
  Windows y Linux.

## Lo que viene

- **Fase 5**: la mudanza de Maxycraft al motor, y sonidos grabados.
- **Fase 6**: exportar y publicar juegos para Mac, Windows y Linux.
