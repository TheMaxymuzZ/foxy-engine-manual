# Escenas

Un proyecto puede tener **varias escenas**. Cada escena es un mundo propio:
la isla, una cueva, el interior de una casa, un barco… El jugador pasa de una
a otra por zonas, objetos, botones o desde el guion.

Cada escena se guarda en `mundos/<nombre>.ron`. La que se crea con el
proyecto es `principal`.

## Las escenas en el panel «Proyecto»

El grupo <i class="fx fx-mundo"></i> **Escenas** del panel «Proyecto» lista
todas las escenas:

- Un **clic** abre otra. Si la que tenías abierta tiene cambios, el editor
  pregunta si guardarlos.
- La <i class="fx fx-estrella"></i> marca la **escena inicial**, donde
  empiezan las partidas nuevas.
- Un <i class="fx fx-aviso"></i> avisa de que **nada lleva todavía** a esa
  escena: así no se podrá ver al jugar.
- <i class="fx fx-mapa"></i> **Cómo se conectan…** abre el
  [mapa de escenas](#el-mapa-de-escenas).

## Crear una escena

El <i class="fx fx-mas"></i> del grupo *Escenas* (o **Crear → Escena
nueva…**) abre una ventana:

1. Escribe su **nombre**, por ejemplo *cueva*.
2. Elige con qué empieza:

   | Empezar con | Qué trae |
   |---|---|
   | **Vacía** | Una cámara y la luz del sol, sin terreno (ver [Empezar una escena desde cero](escena-desde-cero.md)) |
   | **Con un terreno de cubitos llano** | Un suelo plano y el punto de inicio |
   | **Isla sin objetos** | Una isla con colinas, playa y árboles |
   | **Plaza de prueba** | La isla de ejemplo, con casas y vecinos |
   | **Una copia de esta escena** | Todo lo que tiene la escena abierta |

3. Deja marcado <i class="fx fx-enlace"></i> **Conectarla con «principal»**
   (o con la escena que tengas abierta) y pulsa **Crear**.

Con *Conectarla*, la escena nueva **ya está conectada** de ida y vuelta: el
editor pone una <i class="fx fx-zona"></i> zona de cambio delante de la
cámara que lleva a la escena nueva, una <i class="fx fx-entrada"></i> entrada
al lado para volver, y en la escena nueva otra zona de vuelta. Solo queda
**moverlas** a su sitio, por ejemplo a la boca de la cueva.

## El mapa de escenas

<i class="fx fx-mapa"></i> **Cómo se conectan…** enseña de un vistazo cómo
se une tu juego:

- Cada escena, con sus **entradas**.
- Qué **zonas** y **objetos** salen de ella y a dónde llevan.
- Por dónde **se llega** a ella: zonas, objetos, botones de interfaz o el
  guion (`motor.cambiar_escena`).
- La **escena inicial** (<i class="fx fx-estrella"></i>).
  *Empezar el juego en esta escena* la cambia.
- **Avisos** (<i class="fx fx-aviso"></i>) de escenas a las que no lleva nada
  y de zonas o botones que llevan a una escena que no existe.
- Un botón para poner en la escena abierta una **salida hacia cualquier
  otra**.

Desde el mapa también se **renombra** una escena (las zonas y botones que
llevan a ella se cambian solos) y se **quita**: no se borra, va a la carpeta
`papelera` del proyecto. La escena inicial y la única escena del proyecto no
se pueden quitar.

## Conectar escenas sin código

### Puntos de entrada

Un <i class="fx fx-entrada"></i> **punto de entrada** es como el punto de
inicio, pero **azul y con nombre** (por ejemplo, *puerta*). Al llegar a una
escena, el jugador aparece en la entrada que se pida. Si no se pide ninguna,
aparece en el punto de inicio de esa escena.

### Zonas de cambio

Una <i class="fx fx-zona"></i> **zona de cambio** es un marco de 2 × 2,5 m
(**Crear → Zona de cambio**, o en *Colocar objetos*). Al entrar en ella
jugando, pasa su **acción**:

- **Ir a otra escena**, y por qué entrada.
- **Abrir una interfaz** (una tienda, un cartel…).
- **Llamar al guion**.

Las zonas y las entradas solo se ven en el editor; al jugar son invisibles.

### Objetos que se usan

Cualquier casa, puerta u objeto propio puede llevar a otra escena con
<i class="fx fx-usar"></i> [**Al usarlo (E)**](mundo.md#al-usarlo-e).
Jugando, al mirarlo de cerca sale <kbd>E</kbd> *Casa: ir a «interior»*.
Es la forma más natural de entrar en un edificio.

### Un ejemplo: entrar en una cueva

1. Pulsa el <i class="fx fx-mas"></i> de *Escenas*, llámala *cueva*, elige
   **Con un terreno de cubitos llano** y deja marcado **Conectarla con
   «principal»**.
2. En *principal*, mueve la zona que ha puesto el editor hasta la boca de la
   cueva, y la entrada justo delante.
3. En *cueva*, mueve la zona de vuelta a donde quieras salir.
4. Pulsa <i class="fx fx-mando"></i> **Desde el inicio** y entra en la zona.

## Desde una interfaz o el guion

- Un **botón** con la acción *Ir a otra escena*. Mira [Interfaces](interfaces.md).
- En Lua: `motor.cambiar_escena("cueva", "boca")`. Al llegar, el motor llama a
  `al_entrar_escena(nombre)`. Mira [Guion del mundo](guiones.md).

Las partidas guardadas recuerdan en qué escena estaba el jugador.
