# API de Lua

Todo lo que un guion puede usar. Los guiones usan **Lua 5.4**. Mira
[Guiones en Lua](../guia/guiones.md) para empezar.

## Funciones que llama el motor

Escríbelas en `guiones/mundo.lua`; todas son opcionales.

| Función | Cuándo | Argumentos | Devuelve |
|---|---|---|---|
| `al_empezar()` | Al empezar a jugar (partida nueva, cargada o *Jugar aquí*) | — | — |
| `al_hablar(nombre)` | Al hablar con un vecino | `nombre`: el del vecino | Un texto para que lo diga en vez de sus frases, o nada |
| `al_nuevo_dia(dia)` | Al empezar un día | `dia`: número del día, desde 1 | — |
| `al_cambiar_hora(hora)` | Al empezar cada hora | `hora`: entero de 0 a 23 | — |
| `cada_segundo()` | Una vez por segundo de juego | — | — |
| `al_entrar_escena(nombre)` | Al llegar a otra escena | `nombre`: el de la escena | — |
| *tu función*`(quien)` | Un botón o una zona con la acción *Llamar al guion* | `quien`: nombre del botón o la zona | — |

## La tabla `motor`

### Mensajes

| Función | Qué hace |
|---|---|
| `motor.decir(texto)` | Enseña un mensaje abajo de la pantalla |
| `print(...)` | Escribe en la consola del editor (varios valores, separados por tabuladores) |

### Tiempo

| Función | Qué hace |
|---|---|
| `motor.hora()` | La hora, de 0 a 24 con decimales (`13.5` = 13:30) |
| `motor.poner_hora(h)` | Cambia la hora. Se ajusta a 0–24 (`25` → `1`) |
| `motor.dia()` | El día de la partida, desde 1 |
| `motor.clima()` | `"despejado"`, `"nublado"`, `"lluvia"` o `"tormenta"` |
| `motor.poner_clima(nombre)` | Cambia el tiempo (uno de los cuatro de arriba) |
| `motor.estacion()` | `"primavera"`, `"verano"`, `"otono"` o `"invierno"` |
| `motor.poner_estacion(nombre)` | Cambia la estación |

### Jugador y vecinos

| Función | Qué hace |
|---|---|
| `motor.jugador()` | Devuelve `x, y, z` del jugador, en metros |
| `motor.vecinos()` | Una lista con los nombres de los vecinos |
| `motor.vecino(nombre)` | Devuelve `x, y, z` de ese vecino, o `nil` si no existe |
| `motor.llevar(nombre, x, y, z)` | El vecino camina hasta ese punto |

```lua
local x, y, z = motor.jugador()
for _, nombre in ipairs(motor.vecinos()) do
  local vx, vy, vz = motor.vecino(nombre)
  print(nombre, vx, vz)
end
```

### Sonido

| Función | Qué hace |
|---|---|
| `motor.sonar(nombre)` | Toca un efecto |

Sonidos: `paso`, `salto`, `caida`, `patada`, `hablar`, `trueno`, `pajaro`,
`campana`, `clic`.

### Escenas e interfaces

| Función | Qué hace |
|---|---|
| `motor.escena()` | Nombre de la escena actual |
| `motor.cambiar_escena(nombre, entrada)` | Va a otra escena. `entrada` es opcional: el nombre de un punto de entrada; sin él, al punto de inicio |
| `motor.abrir_interfaz(nombre)` | Abre una interfaz de `interfaces/`. Si es un marcador escondido, lo vuelve a enseñar |
| `motor.cerrar_interfaz(nombre)` | Sin nombre, cierra la interfaz de arriba del todo. Con nombre, cierra esa; si es un marcador, lo esconde |

### Valores

Los valores son datos con nombre que **se guardan con la partida** y que las
interfaces enseñan escribiendo `{nombre}`.

| Función | Qué hace |
|---|---|
| `motor.poner_valor(nombre, valor)` | Guarda un número, texto o booleano. `nil` lo borra |
| `motor.valor(nombre)` | Lo devuelve (número si era un número), o `nil` si no existe |

Los booleanos se guardan como `"sí"` y `"no"`.

### Otros

| Función | Qué hace |
|---|---|
| `motor.aleatorio(a, b)` | Un número entero al azar entre `a` y `b`, ambos incluidos |

## Cómo se ejecuta

- Las funciones `motor.poner_*`, `decir`, `llevar`, `sonar`, `cambiar_escena`
  y las de interfaces **piden** cosas: el motor las hace al terminar el
  fotograma.
- Un error sale en pantalla y en la consola del editor; **el juego sigue**.
- Si una llamada tarda demasiado (por ejemplo, un bucle sin fin), el motor la
  corta con el error «el guion tarda demasiado».
- Un nombre que el motor no conoce (un clima, una estación o un sonido) da un
  error que dice cuáles valen.
