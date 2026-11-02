# Objetos del motor

Los objetos que trae Foxy Engine, en *Colocar objetos*. El **tipo** es el
nombre que se usa en los archivos de los mundos.

## Para construir

Se funden con los bloques del mundo: puedes cavar, poner o pintar encima de
ellos.

| Objeto | Tipo | Notas |
|---|---|---|
| Casa | `casa` | Con giro 0 la puerta mira al sur |
| Puesto del mercado | `puesto` | |
| Árbol | `arbol` | Sus hojas cambian con la estación |
| Farola | `farola` | |
| Banco | `banco` | |
| Valla | `valla` | |
| Pozo | `pozo` | |
| Roca | `roca` | |

## Especiales

Se dibujan aparte, con su propio modelo.

| Objeto | Tipo | Se ve al jugar | Qué hace |
|---|---|---|---|
| Pelota | `pelota` | Sí | Se mueve con la física: cae, bota, rueda y flota. Se patea con <kbd>E</kbd> |
| Vecino | `vecino` | Sí | Un habitante con nombre y frases. Ver [La vida del mundo](../guia/vida.md#vecinos) |
| Punto de inicio | `inicio` | No | Donde empieza una partida nueva, mirando hacia su flecha |
| Punto de entrada | `entrada` | No | Un punto con nombre por donde se llega desde otra escena |
| Zona de cambio | `zona` | No | Un marco de 2 × 2,5 m que hace una [acción](acciones.md) al entrar |

## Objetos propios

Los que haces con el [creador de objetos](../guia/creador.md) usan como tipo
el nombre de su archivo en `objetos/` (sin `.ron`).

## Posición y giro

En los archivos, `pos` es el **centro de la base** del objeto en metros, y
`giro` va en **cuartos de vuelta** (0, 1, 2 o 3). Con 0 la puerta (o el
frente) mira al **sur**.
