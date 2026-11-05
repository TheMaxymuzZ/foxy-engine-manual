# Acciones

Una **acción** es lo que pasa:

- al pulsar un <i class="fx fx-boton"></i> **botón** de una
  [interfaz](../guia/interfaces.md),
- al entrar en una <i class="fx fx-zona"></i>
  [**zona de cambio**](../guia/escenas.md#zonas-de-cambio) o al entrar o
  salir de una entidad con el componente [Zona](componentes/zona.md),
- o al **usar un objeto** con <kbd>E</kbd>
  (<i class="fx fx-usar"></i> [*Al usarlo*](../guia/mundo.md#al-usarlo-e)).

Se eligen de una lista, sin código.

| En el editor | En el archivo | Qué hace |
|---|---|---|
| Nada | `Ninguna` | No hace nada |
| Ir a otra escena | `IrAEscena(escena: "cueva", entrada: "boca")` | Cambia de escena. `entrada` es el nombre de un punto de entrada de esa escena; vacía, se llega al punto de inicio |
| Abrir una interfaz | `AbrirInterfaz("tienda")` | Abre una interfaz (una tienda, un cartel…) |
| Cerrar esta interfaz | `CerrarInterfaz` | Cierra la interfaz de arriba del todo |
| Volver al juego | `VolverAlJuego` | Cierra todas las interfaces abiertas y sigue jugando |
| Partida nueva | `PartidaNueva` | Empieza una partida nueva en la escena inicial |
| Continuar partida | `Continuar` | Carga la partida más reciente |
| Cargar partida | `CargarPartida` | Abre el menú de cargar partida del motor |
| Guardar partida | `GuardarPartida` | Abre el menú de guardar partida del motor |
| Opciones | `Opciones` | Abre las opciones del motor |
| Menú principal | `MenuPrincipal` | Vuelve al menú principal |
| Salir del juego | `Salir` | Sale del juego (o vuelve al editor si estabas probando) |
| Llamar al guion | `Guion("abrir_cofre")` | Llama a esa función del guion con el nombre del botón o la zona: `function abrir_cofre(quien) ... end` |
| Mover una entidad | `Mover(entidad: "Puerta", desplazamiento: (1.0, 0.0, 0.0), segundos: 0.5)` | Desplaza la entidad desde su sitio del editor, en metros, durante esos segundos. Con `(0, 0, 0)` vuelve a su sitio. `entidad` vacía = la que tiene la acción |
| Ocultar una entidad | `Ocultar("Cofre")` | La entidad deja de verse y de chocar. Vacío = la que tiene la acción |
| Mostrar una entidad | `Mostrar("Cofre")` | Vuelve a enseñar una entidad oculta |
| Tocar un sonido | `Sonar("campana")` | Toca un sonido del proyecto o de ejemplo. Si es el de una entidad con [Sonido](componentes/sonido.md), suena desde ella |
| Animar una entidad | `Animar(entidad: "Puerta", animacion: "abrir", al_reves: false)` | Pone una [animación](../guia/animacion.md) en la entidad. Con `al_reves: true`, la pone de atrás hacia delante desde donde vaya: así se cierra lo que se abrió. `entidad` vacía = la que tiene la acción |
| Poner una cinemática | `Cinematica("presentacion")` | Pone una [cinemática](../guia/cinematicas.md) de `cinematicas/` |

Las acciones sobre entidades buscan la entidad **por su nombre** en la
escena y solo duran la partida: al volver al editor, todo está como estaba.

En los archivos, la acción va en el campo `accion` del objeto o del elemento:

```ron
(tipo: "zona", nombre: "Puerta de la cueva", pos: (120.0, 14.0, 90.0), giro: 0,
 accion: IrAEscena(escena: "cueva", entrada: "boca")),
(tipo: "casa", nombre: "Casa de Plumas", pos: (86.0, 16.0, 118.0), giro: 0,
 accion: IrAEscena(escena: "interior", entrada: "puerta")),
(tipo: "puesto", nombre: "Puesto", pos: (96.0, 16.0, 112.0), giro: 1,
 accion: AbrirInterfaz("tienda")),
```

Jugando, al mirar de cerca un objeto con acción sale una pista con su nombre
y lo que hace: <kbd>E</kbd> *Casa de Plumas: ir a «interior»*.
