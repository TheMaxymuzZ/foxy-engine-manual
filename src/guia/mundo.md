# Construir el mundo

La pestaña **🌍 Mundo** es donde das forma a la isla: añades y quitas
terreno, lo pintas y colocas objetos.

## Las herramientas

Están arriba del panel de la izquierda. Cada una tiene su tecla:

| Herramienta | Tecla | Qué hace |
|---|---|---|
| 👆 **Cursor** | <kbd>C</kbd> | Solo elegir. Un clic elige un objeto y nada se mueve ni cambia. La más segura para mirar |
| 🖱 **Elegir y mover** | <kbd>V</kbd> | Clic para elegir un objeto; arrástralo para moverlo |
| ⬛ **Poner bloques** | <kbd>B</kbd> | Clic o arrastra para poner bloques encima de lo que tocas |
| **Quitar bloques** | <kbd>E</kbd> | Clic o arrastra para cavar. Bajo el nivel del mar el hueco se llena de agua |
| **Pintar** | <kbd>P</kbd> | Cambia el material de lo que ya hay, sin añadir ni quitar |
| **Colocar objetos** | <kbd>O</kbd> | Pone casas, árboles, vecinos, pelotas… |

## El pincel

Poner, quitar y pintar usan el **pincel**:

- **Forma**: cubo o esfera.
- **Tamaño**: de 1 a 24 cubitos. <kbd>[</kbd> lo hace más pequeño y
  <kbd>]</kbd> más grande.
- **Material**: hierba, piedra, madera, teja… (todos están en
  [Materiales](../referencia/materiales.md)).

Con un tamaño **par**, el pincel se ajusta a la rejilla de bloques de 1 m:
así es fácil construir paredes y suelos rectos. Con un tamaño impar puedes
trabajar al detalle, cubito a cubito.

> **Consejo.** Al arrastrar poniendo bloques, el pincel se queda en la capa
> donde empezó la pincelada. Así puedes pintar un suelo plano entero sin que
> vaya subiendo encima de lo que acabas de poner.

## Colocar objetos

Con **Colocar objetos** (<kbd>O</kbd>) eliges un objeto de la lista y haces
clic donde lo quieras. Antes de soltarlo, <kbd>R</kbd> lo gira un cuarto de
vuelta. La lista tiene dos partes:

- **Del motor**: casa, puesto del mercado, árbol, farola, banco, valla, pozo,
  roca, pelota, vecino, punto de inicio, punto de entrada y zona de cambio.
  Los describe [Objetos del motor](../referencia/objetos.md).
- **Mis objetos**: los que has hecho con el
  [creador de objetos](creador.md). El ✏ de al lado los abre para editarlos.

## Editar un objeto colocado

Elige un objeto (con el cursor, con *Elegir y mover*, o en la lista de la
escena) y el panel de la derecha muestra:

- **Nombre**: por ejemplo «Casa de Plumas». Los vecinos usan su nombre al
  hablar y en los guiones.
- **Posición** en metros y **giro**.
- **Al suelo**: lo baja hasta que toca el terreno.
- **Ver** (<kbd>F</kbd>): lleva la cámara hasta él.
- **Duplicar** (<kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>D</kbd>) y **Borrar**
  (<kbd>Supr</kbd>).

Algunos objetos tienen más opciones:

- **Vecino**: *Lo que dice*, una frase por línea. <kbd>Intro</kbd> empieza
  una línea nueva.
- **Zona de cambio**: la [acción](../referencia/acciones.md) que pasa al
  entrar en ella.
- **Punto de entrada**: su nombre, que es el que usan las zonas y los botones
  para llegar a él.

Con un objeto del motor elegido, **Hacer una versión propia** lo copia al
creador de objetos para que lo cambies a tu gusto.

## Las opciones del mundo

Sin nada elegido, el panel de la derecha muestra el mundo entero.

### La vida

Cuánto dura un día, con qué estación y clima empieza, cuántos días dura cada
estación y si el tiempo cambia solo. Lo explica [La vida del mundo](vida.md).

### La isla

La isla se genera a partir de unos pocos números:

| Opción | Qué cambia |
|---|---|
| **Semilla** | Otra semilla, otra isla con otra forma |
| **Tamaño del mundo** | El lado del mundo en metros; la isla queda en el centro |
| **Radio** | Lo grande que es la isla |
| **Altura** | Lo altas que son las colinas sobre el mar |
| **Nivel del mar** | La profundidad del mar en los bordes |
| **Árboles** | De 0 (ninguno) a 1 (un bosque) |
| **Muelle** | Un muelle de madera en la playa del sur |

**Regenerar la isla** vuelve a crear el terreno con los números nuevos y
**conserva** los objetos y los bloques que pusiste a mano.

## La cámara

| Para | Haz |
|---|---|
| Volar | <kbd>W</kbd> <kbd>A</kbd> <kbd>S</kbd> <kbd>D</kbd> |
| Subir / bajar | <kbd>Espacio</kbd> / <kbd>Mayús</kbd> |
| Mirar | Botón derecho y arrastrar, <kbd>Alt</kbd> + clic y arrastrar, o mantener <kbd>Cmd</kbd>/<kbd>Ctrl</kbd> y mover el ratón |
| Girar sin ratón | Flechas |
| Acercarse o alejarse | Rueda |
| Ir al objeto elegido | <kbd>F</kbd> |
