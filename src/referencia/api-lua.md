# Referencia de la API de Lua

<!-- Generado con `foxy-engine --referencia-lua`. No lo cambies a mano: sale del catálogo del motor. -->

Esta página recoge todo lo que un guion puede usar: las funciones que llama el motor y todas las de la tabla `motor`, agrupadas como en la paleta de nodos. Es la misma lista que usa el autocompletado del panel **Código** y la que reciben VS Code y Zed. Para aprender a usarlas, consulta [Programar en Lua](../guia/programar-lua.md) y la [API de Lua explicada](lua.md).

Tipos: **número**, **texto**, **sí/no**, **vector** (tabla con `x`, `y` y `z`), **entidad** (nombre, número o `"jugador"`), **lista** y **cualquiera**.

## Funciones que llama el motor

Se escriben en el guion; todas son opcionales. En un guion de entidad, las de choque, zona y daño solo llegan cuando afectan a esa entidad, y no reciben la entidad como primer argumento.

| Función | Cuándo |
|---|---|
| `al_empezar()` | Al empezar la partida (guion del mundo) o al llegar a la escena (guion de entidad). |
| `cada_fotograma(segundos)` | Unas 60 veces por segundo, con los segundos desde la anterior. |
| `cada_segundo()` | Una vez por segundo. |
| `al_chocar(otro)` | Cuando el jugador toca la entidad (en el guion del mundo: entidad, otro). |
| `al_chocar_objeto(otro)` | Cuando la entidad choca con otro objeto (en el guion del mundo: entidad, otro). |
| `al_hacer_clic()` | Cuando el jugador hace clic en la entidad, mirándola (en el guion del mundo: entidad). |
| `al_recoger(entidad, valor)` | Cuando el jugador recoge una entidad con el componente Recogible (con el valor que sube). |
| `al_entrar_zona(quien)` | Cuando el jugador entra en la zona de la entidad (en el guion del mundo: entidad, quien). |
| `al_salir_zona(quien)` | Cuando el jugador sale de la zona de la entidad (en el guion del mundo: entidad, quien). |
| `al_entrar_objeto_zona(quien)` | Cuando otro objeto (no el jugador) entra en la zona de la entidad (en el guion del mundo: entidad, quien). |
| `al_salir_objeto_zona(quien)` | Cuando otro objeto (no el jugador) sale de la zona de la entidad (en el guion del mundo: entidad, quien). |
| `al_recibir_dano(cantidad, de)` | Cuando algo le hace daño con motor.danar (en el guion del mundo: entidad, cantidad, de). |
| `al_recibir(evento, valor, de)` | Un mensaje enviado con motor.emitir, motor.emitir_a o motor.emitir_etiqueta (solo en guiones de entidad). |
| `al_pulsar(accion)` | Al pulsar una acción del mapa de acciones del proyecto. |
| `al_terminar_animacion(animacion)` | Cuando termina un clip que no va en bucle (en el guion del mundo: entidad, animacion). |
| `al_evento_animacion(evento)` | Un suceso «Avisar a los nodos» de la línea de tiempo (en el guion del mundo: entidad, evento). |
| `al_terminar_cinematica(cinematica)` | Cuando una cinemática acaba o el jugador la salta. |
| `al_hablar(vecino)` | Al hablar con un vecino. Lo que devuelva es lo que dice. |
| `al_entrar_escena(escena)` | Al llegar a una escena. |
| `al_nuevo_dia(dia)` | Cada vez que empieza un día. |
| `al_cambiar_hora(hora)` | Cada vez que el reloj llega a una hora en punto. |
| `al_recargar()` | Después de recargar el guion con el juego en marcha (al guardarlo). |

## Variables de los guiones de entidad

| Nombre | Qué es |
|---|---|
| `yo` | La entidad que lleva el guion |
| `propiedades` | Los valores de la entidad: los de la tabla `propiedades` del guion, cambiados en el inspector |

## Flujo

| Función | Devuelve | Qué hace |
|---|---|---|
| `motor.esperar(segundos: número)` | — | En Lua: espera sin parar el juego. En los nodos se usa «Esperar». |

## Variables

| Función | Devuelve | Qué hace |
|---|---|---|
| `motor.variable(entidad: entidad, nombre: texto)` | valor (cualquiera) | Lee una variable «de la entidad» de otro objeto (de sus grafos, o una propiedad de sus guiones): la vida del jugador, las monedas… |
| `motor.poner_variable(entidad: entidad, nombre: texto, valor)` | — | Cambia una variable «de la entidad» de otro objeto. Sus grafos y guiones ven el valor nuevo. |

## Matemáticas

| Función | Devuelve | Qué hace |
|---|---|---|
| `motor.aleatorio(desde: número, hasta: número)` | numero (número) | Un número entero al azar entre los dos (los dos incluidos). |

## Vectores y colores

| Función | Devuelve | Qué hace |
|---|---|---|
| `motor.vector(x: número, y: número, z: número)` | v (vector) | Un punto o una dirección en metros (x a la derecha, y arriba, z hacia atrás). |
| `motor.distancia(a: vector, b: vector)` | metros (número) | Los metros que hay entre dos puntos. Vale también con entidades. |
| `motor.longitud(v: vector)` | metros (número) | Lo largo que es (en metros). |
| `motor.normalizar(v: vector)` | v (vector) | La misma dirección, con largo 1. |
| `motor.color(r: número, g: número, b: número)` | color (texto) | Un color, como "#rrggbb". |

## Entidades

| Función | Devuelve | Qué hace |
|---|---|---|
| `motor.entidad(nombre: texto)` | entidad (entidad) | La primera entidad de la escena con ese nombre. |
| `motor.entidades(nombre: texto)` | lista (lista) | Todas las entidades con ese nombre (las copias de un prefabricado, por ejemplo). |
| `motor.nombre(entidad: entidad)` | nombre (texto) | Su nombre en la escena. |
| `motor.posicion(entidad: entidad)` | posicion (vector) | Dónde está ahora la entidad (sus pies), en metros. |
| `motor.poner_posicion(entidad: entidad, posicion: vector)` | — | Lleva la entidad a ese sitio de golpe. Con el jugador, lo teletransporta. |
| `motor.mover_hacia(entidad: entidad, destino: vector, velocidad: número)` | llegado (sí/no) | Da un paso hacia el destino, a esa velocidad. Úsalo en «Cada fotograma» para que vaya andando. |
| `motor.mirar_hacia(entidad: entidad, punto: vector)` | — | Gira la entidad para que mire a ese punto. |
| `motor.mover(entidad: entidad, x: número, y: número, z: número, segundos: número)` | — | La lleva poco a poco a su sitio del editor más esos metros (puertas, plataformas...). |
| `motor.ocultar(entidad: entidad)` | — | La entidad deja de verse y de chocar. |
| `motor.mostrar(entidad: entidad)` | — | Vuelve a verse una entidad oculta. |
| `motor.oculta(entidad: entidad)` | si (sí/no) | Sí si está oculta. |
| `motor.ve(entidad: entidad, objetivo: entidad, alcance: número)` | si (sí/no) | Sí si el objetivo está a la vista: a menos de esa distancia y sin ocultar. |

## Etiquetas y mensajes

| Función | Devuelve | Qué hace |
|---|---|---|
| `motor.tiene_etiqueta(entidad: entidad, etiqueta: texto)` | si (sí/no) | Sí si el objeto lleva esa etiqueta. Para saber con qué se ha chocado. El jugador lleva siempre «jugador». |
| `motor.con_etiqueta(etiqueta: texto)` | lista (lista) | Todos los objetos que llevan esa etiqueta y no están ocultos (para «Para cada elemento»). |
| `motor.mas_cercano(etiqueta: texto, desde: entidad)` | entidad (entidad) | El objeto con esa etiqueta que está más cerca (sin contar el de «cerca de»). Nada si no hay ninguno. |
| `motor.etiquetas(entidad: entidad)` | lista (lista) | Las etiquetas que lleva ahora el objeto. |
| `motor.poner_etiqueta(entidad: entidad, etiqueta: texto)` | — | Le pone una etiqueta mientras dure la partida (en el editor no cambia). |
| `motor.quitar_etiqueta(entidad: entidad, etiqueta: texto)` | — | Le quita una etiqueta mientras dure la partida. |

## Jugador

| Función | Devuelve | Qué hace |
|---|---|---|
| `motor.posicion_jugador()` | posicion (vector) | Dónde están los pies del jugador, en metros. |
| `motor.jugador()` | x (número), y (número), z (número) | Lo mismo, en tres números. |
| `motor.accion(nombre: texto)` | si (sí/no) | Sí mientras se aprieta esa acción del mapa de acciones. |
| `motor.accion_pulsada(nombre: texto)` | si (sí/no) | Sí solo en el fotograma en que se pulsa. |

## Mensajes y consola

| Función | Devuelve | Qué hace |
|---|---|---|
| `motor.decir(texto: texto)` | — | Enseña un mensaje abajo en la pantalla. |
| `motor.imprimir(texto: texto)` | — | Escribe en la consola del editor (para comprobar cosas). |

## Tiempo y clima

| Función | Devuelve | Qué hace |
|---|---|---|
| `motor.hora()` | hora (número) | La hora del reloj del juego, con decimales. |
| `motor.poner_hora(hora: número)` | — | Cambia la hora del reloj. |
| `motor.dia()` | dia (número) | El día de la partida (empieza en 1). |
| `motor.tiempo()` | segundos (número) | Segundos desde que empezó la partida. |
| `motor.clima()` | clima (texto) | despejado, nublado, lluvia o tormenta. |
| `motor.poner_clima(clima: texto)` | — | Cambia el clima poco a poco. |
| `motor.estacion()` | estacion (texto) | primavera, verano, otono o invierno. |
| `motor.poner_estacion(estacion: texto)` | — | Cambia la estación. |

## Escenas e interfaces

| Función | Devuelve | Qué hace |
|---|---|---|
| `motor.escena()` | escena (texto) | El nombre de la escena en la que se está. |
| `motor.cambiar_escena(escena: texto, entrada: texto)` | — | Va a otra escena (y entra por esa entrada, si se dice). |
| `motor.abrir_interfaz(nombre: texto)` | — | Abre una interfaz del proyecto encima del juego. |
| `motor.cerrar_interfaz(nombre: texto)` | — | Cierra esa interfaz (vacío = la de más arriba). |
| `motor.partida_nueva()` | — | Empieza una partida nueva desde el principio. |

## Sonido

| Función | Devuelve | Qué hace |
|---|---|---|
| `motor.sonar(sonido: texto)` | — | Toca un sonido del proyecto (de sonidos/) o uno de ejemplo: paso, salto, campana... |

## Valores del juego

| Función | Devuelve | Qué hace |
|---|---|---|
| `motor.valor(nombre: texto)` | valor (cualquiera) | Un valor guardado con la partida (las interfaces lo enseñan con {nombre}). |
| `motor.poner_valor(nombre: texto, valor)` | — | Guarda un valor del juego. |
| `motor.sumar_valor(nombre: texto, cantidad: número)` | — | Suma (o resta, con un número negativo) a un valor del juego. |

## Vecinos

| Función | Devuelve | Qué hace |
|---|---|---|
| `motor.vecinos()` | lista (lista) | Los nombres de los vecinos de la escena. |
| `motor.vecino(nombre: texto)` | x (número), y (número), z (número) | La posición de un vecino. |
| `motor.llevar(nombre: texto, x: número, y: número, z: número)` | — | El vecino camina hasta allí. |

## Animación

| Función | Devuelve | Qué hace |
|---|---|---|
| `motor.animar(entidad: entidad, animacion: texto)` | — | Pone un clip de animaciones/ (o, en 2D, una animación de su hoja de sprites). Manda sobre su máquina de estados hasta que acaba. Vacío = vuelve la de siempre. |
| `motor.animar_al_reves(entidad: entidad, animacion: texto)` | — | Pone el clip hacia atrás desde donde vaya: una puerta abierta con «abrir» se cierra así. Al volver al principio, queda en reposo. |
| `motor.parar_animacion(entidad: entidad)` | — | Quita el clip puesto a mano: vuelve el de su máquina de estados (o se queda quieta). |
| `motor.parametro_animacion(entidad: entidad, nombre: texto, valor: número)` | — | Cambia un parámetro de su máquina de estados (sí = 1, no = 0). Los de velocidad, en el suelo y en el agua los pone el motor. |
| `motor.cinematica(nombre: texto)` | — | Pone una cinemática de cinematicas/: mueve la cámara y las entidades y enseña sus frases. El jugador la salta con Espacio. |
| `motor.terminar_cinematica()` | — | Termina la cinemática que se esté viendo y devuelve la cámara al jugador. |

## 2D

| Función | Devuelve | Qué hace |
|---|---|---|
| `motor.voltear(entidad: entidad, espejo: sí/no)` | — | Da la vuelta al sprite de la entidad (como en un espejo). |
| `motor.impulsar(entidad: entidad, x: número, y: número)` | — | Empuja un cuerpo físico (o al jugador) con esa velocidad, en casillas por segundo. |
| `motor.casilla(x: número, y: número, capa: texto)` | casilla (número) | El número de la casilla que hay en ese sitio de la capa (nada si está vacía). Capa vacía = la primera que choca. |
| `motor.poner_casilla(x: número, y: número, casilla: número, capa: texto)` | — | Cambia una casilla del mapa mientras se juega (para romper bloques, abrir pasos...). |
| `motor.particulas(entidad: entidad, encendidas: sí/no)` | — | Enciende o apaga el componente Partículas de la entidad (también en 3D). |

## Otros

| Función | Devuelve | Qué hace |
|---|---|---|
| `motor.soltar_particulas(tipo, x, y, z, cantidad)` | — | Suelta de golpe partículas de un tipo (polvo, chispas, lluvia, nieve, humo u hojas) en ese sitio. |
| `motor.danar(entidad, cantidad, de)` | — | Pone en marcha «Al recibir daño» de esa entidad. |
| `motor.emitir(evento, valor, de)` | — | Envía un mensaje a todos: lo reciben los nodos «Al recibir un mensaje» y la función al_recibir de los guiones de entidad. |
| `motor.emitir_a(entidad, evento, valor, de)` | — | Como motor.emitir, pero solo para los comportamientos de esa entidad. |
| `motor.emitir_etiqueta(etiqueta, evento, valor, de)` | — | Como motor.emitir, pero solo para las entidades que llevan esa etiqueta. |
