# Construir el mundo

La pestaña de la **escena** es donde das forma al mundo: añades y quitas
terreno, lo pintas y colocas objetos.

## Las herramientas

Están en la **tira** del borde izquierdo de la vista. Cada una tiene su
tecla:

| | Herramienta | Tecla | Qué hace |
|---|---|---|---|
| <i class="fx fx-cursor"></i> | **Cursor** | <kbd>C</kbd> | Solo elegir. Un clic elige un objeto y nada se mueve ni cambia. La más segura para mirar |
| <i class="fx fx-mover"></i> | **Elegir y mover** | <kbd>V</kbd> | Clic para elegir un objeto; arrástralo para moverlo |
| <i class="fx fx-poner"></i> | **Poner bloques** | <kbd>B</kbd> | Clic o arrastra para poner bloques encima de lo que tocas |
| <i class="fx fx-quitar"></i> | **Quitar bloques** | <kbd>E</kbd> | Clic o arrastra para cavar. Bajo el nivel del mar el hueco se llena de agua |
| <i class="fx fx-pintar"></i> | **Pintar** | <kbd>P</kbd> | Cambia el material de lo que ya hay, sin añadir ni quitar |
| <i class="fx fx-colocar"></i> | **Colocar objetos** | <kbd>O</kbd> | Pone casas, árboles, vecinos, pelotas… |

Las opciones de cada herramienta salen en el **inspector**, a la derecha.

## El pincel

Poner, quitar y pintar usan el **pincel**, que se ajusta arriba del
inspector:

- **Forma**: cubo o esfera.
- **Tamaño**: de 1 a 24 cubitos. <kbd>[</kbd> lo hace más pequeño y
  <kbd>]</kbd> más grande.
- **Material**: hierba, piedra, madera, teja… Un clic en su color. Todos
  están en [Materiales](../referencia/materiales.md).

Con un tamaño **par**, el pincel se ajusta a la rejilla de bloques de 1 m:
así es fácil construir paredes y suelos rectos. Con un tamaño impar puedes
trabajar al detalle, cubito a cubito.

> <i class="fx fx-consejo"></i> **Consejo.** Al arrastrar poniendo bloques,
> el pincel se queda en la capa donde empezó la pincelada. Así puedes pintar
> un suelo plano entero sin que vaya subiendo encima de lo que acabas de
> poner.

## Colocar objetos

Con <i class="fx fx-colocar"></i> **Colocar objetos** (<kbd>O</kbd>) eliges
un objeto en el inspector y haces clic donde lo quieras. Antes de soltarlo,
<kbd>R</kbd> (o los botones de giro) lo gira un cuarto de vuelta. La lista
tiene tres partes:

- **Construcción y naturaleza**: casa, puesto del mercado, árbol, farola,
  banco, valla, pozo y roca.
- **Juego**: pelota, vecino, punto de inicio, punto de entrada y zona de
  cambio. Todos están en [Objetos del motor](../referencia/objetos.md).
- **Mis objetos**: los que has hecho con el
  [creador de objetos](creador.md).

El menú **Crear** también pone al momento una
<i class="fx fx-zona"></i> *Zona de cambio*, un
<i class="fx fx-entrada"></i> *Punto de entrada* o un
<i class="fx fx-vecino"></i> *Vecino* en la escena abierta.

## Editar un objeto colocado

Elige un objeto (con el cursor, con *Elegir y mover*, o en la lista
[En la escena](carpetas.md)) y el inspector muestra:

- **Nombre**: por ejemplo «Casa de Plumas». Los vecinos usan su nombre al
  hablar y en los guiones, y sale en el juego al usar el objeto.
- **Posición** (X, altura y Z, en metros) y **giro**.
- <i class="fx fx-suelo"></i> **Al suelo**: lo baja hasta que toca el terreno.
- <i class="fx fx-ver"></i> **Ver** (<kbd>F</kbd>): lleva la cámara hasta él.
- <i class="fx fx-duplicar"></i> **Duplicar**
  (<kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>D</kbd>) y
  <i class="fx fx-borrar"></i> **Borrar** (<kbd>Supr</kbd>).

<kbd>Esc</kbd> deja de elegirlo.

### <i class="fx fx-usar"></i> Al usarlo (E)

Las casas, los puestos, los árboles, las farolas y demás objetos de
construcción, y también **tus objetos propios**, pueden hacer una
[acción](../referencia/acciones.md) cuando el jugador los **mira de cerca y
pulsa <kbd>E</kbd>** (o hace clic). Por ejemplo:

- Una **casa** que lleva a la escena de su interior.
- Un **cartel** o un **puesto** que abre una interfaz (una tienda, un mapa).
- Un **pozo** que llama a una función del guion.

Jugando, al acercarse aparece una pista como
<kbd>E</kbd> *Casa: ir a «interior»*. Si eliges una escena, puedes elegir
también por qué **entrada** se llega.

### Opciones de algunos objetos

- <i class="fx fx-vecino"></i> **Vecino**: *Lo que dice*, una frase por
  línea. <kbd>Intro</kbd> empieza una línea nueva.
- <i class="fx fx-zona"></i> **Zona de cambio**: *Al entrar en la zona*, la
  acción que pasa al entrar en ella jugando.
- <i class="fx fx-entrada"></i> **Punto de entrada** y
  <i class="fx fx-inicio"></i> **punto de inicio**: su nombre, que es el que
  eligen las zonas, los objetos y los botones de otras escenas para llegar a
  él.

Con un objeto del motor elegido, <i class="fx fx-editar"></i> **Hacer una
versión propia** lo copia al creador de objetos para que lo cambies a tu
gusto. Con uno de los tuyos, **Editar este objeto** lo abre en el creador.

## Las opciones de la escena

Sin nada elegido, el inspector muestra la **escena** entera.

### El terreno

**Tipo** elige cómo se genera el suelo:

| Tipo | Opciones |
|---|---|
| **Isla** | **Semilla** (otra semilla, otra isla), **Tamaño** de la isla (de 20 a 90 m de radio), **Colinas** (lo altas que son, de 2 a 30 m), **Árboles** (de 0, ninguno, a 1, un bosque) y **Muelle** (de madera, en la playa del sur) |
| **Llano vacío** | **Lado**: un suelo de hierba cuadrado y completamente llano, de 32 a 256 m. Es el terreno de un proyecto vacío |

<i class="fx fx-girar"></i> **Regenerar el terreno** vuelve a crear el suelo
con las opciones nuevas y **conserva** los objetos y los bloques que pusiste
a mano.

> <i class="fx fx-aviso"></i> **Atención.** Regenerar el terreno no se puede
> deshacer. Si dudas, guarda antes.

### La vida

Cuánto dura un día, con qué estación y clima empieza, cuántos días dura cada
estación y si el tiempo cambia solo. Lo explica [La vida del mundo](vida.md).

## La cámara

| Para | Haz |
|---|---|
| Volar | <kbd>W</kbd> <kbd>A</kbd> <kbd>S</kbd> <kbd>D</kbd> |
| Subir / bajar | <kbd>Espacio</kbd> / <kbd>Mayús</kbd> |
| Mirar | Botón derecho y arrastrar, <kbd>Alt</kbd> + clic y arrastrar, o mantener <kbd>Cmd</kbd>/<kbd>Ctrl</kbd> y mover el ratón |
| Girar sin ratón | Flechas |
| Acercarse o alejarse | Rueda |
| Ir al objeto elegido | <kbd>F</kbd> |

La **velocidad** de la cámara (de 2 a 80 m/s) y la **hora** a la que ves el
mundo se cambian arriba a la derecha de la vista, o en el menú **Ver**.
