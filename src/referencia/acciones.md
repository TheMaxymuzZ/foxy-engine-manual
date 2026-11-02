# Acciones

Una **acción** es lo que pasa al pulsar un botón de una
[interfaz](../guia/interfaces.md) o al entrar en una
[zona de cambio](../guia/escenas.md#zonas-de-cambio). Se eligen de una lista,
sin código.

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

En los archivos, la acción va en el campo `accion` del objeto o del elemento:

```ron
(tipo: "zona", nombre: "Puerta de la cueva", pos: (120.0, 14.0, 90.0), giro: 0,
 accion: IrAEscena(escena: "cueva", entrada: "boca")),
```
