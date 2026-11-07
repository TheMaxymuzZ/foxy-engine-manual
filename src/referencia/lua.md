# API de Lua

Todo lo que un guion puede usar, con ejemplos. Los guiones usan **Lua 5.4**.
Mira [Programar en Lua](../guia/programar-lua.md) para empezar. La lista
completa, generada a partir del motor, está en la
[referencia de la API de Lua](api-lua.md).

## Funciones que llama el motor

Escríbelas en `guiones/mundo.lua`; todas son opcionales.

| Función | Cuándo | Argumentos | Devuelve |
|---|---|---|---|
| `al_empezar()` | Al empezar a jugar (partida nueva, cargada o *Jugar aquí*) | — | — |
| `al_hablar(nombre)` | Al hablar con un vecino | `nombre`: el del vecino | Un texto para que lo diga en vez de sus frases, o nada |
| `al_nuevo_dia(dia)` | Al empezar un día | `dia`: número del día, desde 1 | — |
| `al_cambiar_hora(hora)` | Al empezar cada hora | `hora`: entero de 0 a 23 | — |
| `cada_segundo()` | Una vez por segundo de juego | — | — |
| `cada_fotograma(segundos)` | Cada fotograma | `segundos`: los que han pasado desde el anterior | — |
| `al_chocar(entidad, otro)` | Cuando el jugador toca una entidad | `entidad`: la que se toca; `otro`: `0`, el jugador | — |
| `al_entrar_zona(entidad, quien)`, `al_salir_zona(entidad, quien)` | Cuando el jugador entra o sale de una entidad con [Zona](componentes/zona.md) | `entidad`: la zona; `quien`: `0`, el jugador | — |
| `al_recibir_dano(entidad, cantidad, de)` | Cuando `motor.danar` (o el nodo *Hacer daño*) apunta a una entidad | `entidad`, `cantidad` y quién lo hace | — |
| `al_pulsar(nombre)` | Al pulsar una [acción de entrada](../guia/acciones-entrada.md) propia | `nombre`: el de la acción | — |
| *tu función*`(nombre)` | Las que elige el comportamiento *Llamar al mundo* (`guiones/llamar_al_mundo.lua`) de una entidad, al empezar o cada segundo. Lo crean solos los proyectos antiguos; ver [Comportamientos](../guia/comportamientos.md#proyectos-de-versiones-anteriores) | `nombre`: el de la entidad | — |
| `al_entrar_escena(nombre)` | Al llegar a otra escena | `nombre`: el de la escena | — |
| *tu función*`(quien)` | Un botón o una zona con la acción *Llamar al guion* | `quien`: nombre del botón o la zona | — |

## Entidades en Lua

Las funciones que reciben una **entidad** aceptan su nombre (`"Lobo"`), su
número (el que dan `motor.entidad` y los eventos) o `"jugador"`. El número
`0` es siempre el jugador. Las posiciones son **vectores**: tablas con `x`,
`y` y `z`, en metros, que se suman, se restan y se multiplican por un
número con `+`, `-` y `*`.

```lua
local lobo = motor.entidad("Lobo")
local hacia = motor.posicion_jugador() - motor.posicion(lobo)
if motor.longitud(hacia) < 5 then
  motor.decir("¡El lobo está cerca!")
end
```

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
| `motor.posicion_jugador()` | Dónde está el jugador, como vector |
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
| `motor.sonar(nombre)` | Toca un sonido: uno de ejemplo o uno de `sonidos/` |

Sonidos de ejemplo: `paso`, `salto`, `caida`, `patada`, `hablar`, `trueno`,
`pajaro`, `campana`, `clic`. Ver [Sonidos](../guia/sonidos.md).

### Entidades

| Función | Qué hace |
|---|---|
| `motor.entidad(nombre)` | El número de la entidad que se llama así, o `nil` |
| `motor.entidades(nombre)` | Una lista con todas las que se llaman así |
| `motor.nombre(e)` | El nombre de una entidad |
| `motor.posicion(e)` | Dónde está, como vector |
| `motor.poner_posicion(e, v)` | La pone en ese sitio al momento |
| `motor.mover_hacia(e, destino, velocidad)` | La acerca al destino a esa velocidad (metros por segundo; por defecto 3). Úsala en `cada_fotograma`. Devuelve `true` al llegar |
| `motor.mirar_hacia(e, punto)` | La gira para que mire hacia ese punto |
| `motor.ve(e, objetivo, alcance)` | `true` si el objetivo (por defecto, el jugador) está a menos de `alcance` metros (por defecto 8) y no está oculto |
| `motor.mover(nombre, x, y, z, segundos)` | Desplaza la entidad desde su sitio del editor. Con `0, 0, 0` vuelve a su sitio |
| `motor.ocultar(nombre)` | La entidad deja de verse y de chocar |
| `motor.mostrar(nombre)` | Vuelve a enseñarla |
| `motor.oculta(e)` | `true` si está oculta |
| `motor.danar(e, cantidad, de)` | Pone en marcha `al_recibir_dano` y los nodos *Al recibir daño* |
| `motor.variable(e, nombre)` | Una variable *de la entidad* de sus nodos |
| `motor.poner_variable(e, nombre, valor)` | La cambia |

```lua
function abrir_cofre(quien)
  motor.mover("Tapa del cofre", 0, 0.5, 0, 0.6)
  motor.sonar("campana")
end
```

### Acciones de entrada

| Función | Qué hace |
|---|---|
| `motor.accion(nombre)` | `true` mientras la acción está pulsada |
| `motor.accion_pulsada(nombre)` | `true` solo en el momento de pulsarla |

### Escenas e interfaces

| Función | Qué hace |
|---|---|
| `motor.escena()` | Nombre de la escena actual |
| `motor.cambiar_escena(nombre, entrada)` | Va a otra escena. `entrada` es opcional: el nombre de un punto de entrada; sin él, al punto de inicio |
| `motor.abrir_interfaz(nombre)` | Abre una interfaz de `interfaces/`. Si es un marcador escondido, lo vuelve a enseñar |
| `motor.cerrar_interfaz(nombre)` | Sin nombre, cierra la interfaz de arriba del todo. Con nombre, cierra esa; si es un marcador, lo esconde |
| `motor.partida_nueva()` | Empieza una partida nueva |

### Valores

Los valores son datos con nombre que **se guardan con la partida** y que las
interfaces enseñan escribiendo `{nombre}`.

| Función | Qué hace |
|---|---|
| `motor.poner_valor(nombre, valor)` | Guarda un número, texto o booleano. `nil` lo borra |
| `motor.valor(nombre)` | Lo devuelve (número si era un número), o `nil` si no existe |
| `motor.sumar_valor(nombre, n)` | Le suma `n` (por defecto 1). Si no existía, empieza en 0 |

Los booleanos se guardan como `"sí"` y `"no"`.

Las variables **del juego** de los [nodos](../guia/nodos.md#variables)
también son valores.

### Tiempo, eventos y vectores

| Función | Qué hace |
|---|---|
| `motor.esperar(segundos)` | Detiene la función que la llama durante esos segundos, sin parar el juego. Solo dentro de las funciones que llama el motor |
| `motor.tiempo()` | Segundos de juego desde que empezó la partida |
| `motor.emitir(evento, valor)` | Pone en marcha los nodos *Al recibir un mensaje* con ese nombre |
| `motor.emitir_etiqueta(etiqueta, evento, valor)` | Lo mismo, solo para las entidades con esa etiqueta |
| `motor.emitir_a(e, evento, valor)` | Lo mismo, solo para el grafo de esa entidad |
| `motor.vector(x, y, z)` | Un vector nuevo |
| `motor.longitud(v)`, `motor.normalizar(v)` | El largo de un vector y el mismo vector con largo 1 |
| `motor.distancia(a, b)` | Metros entre dos puntos o dos entidades |
| `motor.color(r, g, b)` | Un color como `"#ff8000"`, con componentes de 0 a 255 |

### Otros

| Función | Qué hace |
|---|---|
| `motor.aleatorio(a, b)` | Un número entero al azar entre `a` y `b`, ambos incluidos |
| `motor.imprimir(...)` | Como `print` |

Para el autocompletado en un editor externo, genera las definiciones con
`foxy-engine --definiciones-lua`. Ver
[Editores externos](../guia/lua-editor-externo.md).

## Cómo se ejecuta

- Las funciones `motor.poner_*`, `decir`, `llevar`, `sonar`, `cambiar_escena`
  y las de interfaces **piden** cosas: el motor las hace al terminar el
  fotograma.
- Un error sale en pantalla y en la consola del editor; **el juego sigue**.
- Si una llamada tarda demasiado (por ejemplo, un bucle sin fin), el motor la
  corta con el error «el guion tarda demasiado».
- Un nombre que el motor no conoce (un clima, una estación o un sonido) da un
  error que dice cuáles valen.
