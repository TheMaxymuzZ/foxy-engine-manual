# Escenas

Un proyecto puede tener **varias escenas**. Cada escena es un mundo propio:
la isla, una cueva, el interior de una casa, un barco… El jugador pasa de una
a otra por puertas, botones o desde el guion.

Cada escena se guarda en `mundos/<nombre>.ron`. La que se crea con el
proyecto es `principal`.

## Cambiar de escena en el editor

La pestaña 🌍 dice qué escena estás editando. Su menú **🗺 Escenas ⏷**:

- Lista las escenas del proyecto. Un clic abre otra (el editor guarda antes la
  que tenías abierta).
- **+ Escena nueva…** crea una a partir de una **isla vacía**, de la **plaza
  de prueba** o como **copia de la actual**.
- **🗺 Mapa de escenas…** abre el mapa.

## El mapa de escenas

El mapa enseña de un vistazo cómo se conecta tu juego:

- Cada escena, con sus **entradas**.
- Qué **zonas** salen de ella y a dónde llevan (🚪).
- Qué **botones de interfaz** llevan a ella (⬅).
- La **escena inicial** (⭐), donde empiezan las partidas nuevas.
  *Empezar el juego en esta escena* la cambia.
- **Avisos** (⚠) si una zona o un botón llevan a una escena que no existe.

Desde el mapa también se **cambia el nombre** de una escena (las zonas y
botones que llevan a ella se actualizan solos) y se **quita** una escena: no
se borra, va a la carpeta `papelera` del proyecto. La escena inicial y la
única escena del proyecto no se pueden quitar.

## Conectar escenas sin código

### Puntos de entrada

Un **punto de entrada** es como el punto de inicio, pero **azul y con
nombre** (por ejemplo, *puerta*). Al llegar a una escena, el jugador aparece
en la entrada que se pida. Si no se pide ninguna, aparece en el punto de
inicio de esa escena.

### Zonas de cambio

Una **zona de cambio** es un marco de 2 × 2,5 m que se coloca como cualquier
objeto (*Colocar objetos → Zona de cambio*). Al entrar en ella jugando, pasa
su **acción**:

- **Ir a otra escena**, y por qué entrada.
- **Abrir una interfaz** (una tienda, un cartel…).
- **Llamar al guion**.

Las zonas y las entradas solo se ven en el editor; al jugar son invisibles.

### Un ejemplo: entrar en una cueva

1. Crea la escena *cueva* con **+ Escena nueva…**.
2. En *cueva*, coloca un **punto de entrada** llamado *boca* y una **zona de
   cambio** con la acción *Ir a otra escena → principal, entrada: cueva*.
3. Vuelve a *principal*. Coloca un **punto de entrada** llamado *cueva*
   delante de la cueva, y una **zona** dentro con la acción
   *Ir a otra escena → cueva, entrada: boca*.
4. Pulsa **🎮 Desde el inicio** y entra en la zona.

## Desde una interfaz o el guion

- Un **botón** con la acción *Ir a otra escena*. Mira [Interfaces](interfaces.md).
- En Lua: `motor.cambiar_escena("cueva", "boca")`. Al llegar, el motor llama a
  `al_entrar_escena(nombre)`. Mira [Guiones en Lua](guiones.md).

Las partidas guardadas recuerdan en qué escena estaba el jugador.
