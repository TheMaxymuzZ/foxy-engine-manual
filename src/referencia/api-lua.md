# Referencia de la API de Lua

<!-- Generado con `foxy-engine --referencia-lua`. No lo cambies a mano: sale del catálogo del motor. -->

Esta página recoge todo lo que un guion puede usar: las funciones que llama el motor y todas las de la tabla `motor`, agrupadas como en la paleta de nodos. Es la misma lista que usa el autocompletado del panel **Código** y la que reciben VS Code y Zed. Para aprender a usarlas, consulta [Programar en Lua](../guia/programar-lua.md) y la [API de Lua explicada](lua.md).

Tipos: **número**, **texto**, **sí/no**, **vector** (tabla con `x`, `y` y `z`), **entidad** (nombre, número o `"jugador"`), **lista** y **cualquiera**.

## Funciones que llama el motor

Se escriben en el guion; todas son opcionales. En un guion de entidad, las de choque, zona y daño solo llegan cuando afectan a esa entidad, y no reciben la entidad como primer argumento.

| Función | Cuándo |
|---|---|
| `al_empezar()` | Al empezar la partida (guion del mundo) o al llegar a la escena (guion de objeto). |
| `cada_fotograma(segundos)` | Unas 60 veces por segundo, con los segundos desde la anterior. |
| `cada_segundo()` | Una vez por segundo. |
| `al_chocar(otro)` | Cuando el jugador toca el objeto (en el guion del mundo: objeto, otro). |
| `al_chocar_objeto(otro)` | Cuando el objeto choca con otro objeto (en el guion del mundo: objeto, otro). |
| `al_hacer_clic()` | Cuando el jugador hace clic en el objeto, mirándolo (en el guion del mundo: objeto). |
| `al_recoger(objeto, valor)` | Cuando el jugador recoge un objeto con el componente Recogible (con el valor que sube). |
| `al_entrar_zona(quien)` | Cuando el jugador entra en la zona del objeto (en el guion del mundo: objeto, quien). |
| `al_salir_zona(quien)` | Cuando el jugador sale de la zona del objeto (en el guion del mundo: objeto, quien). |
| `al_entrar_objeto_zona(quien)` | Cuando otro objeto (no el jugador) entra en la zona del objeto (en el guion del mundo: objeto, quien). |
| `al_salir_objeto_zona(quien)` | Cuando otro objeto (no el jugador) sale de la zona del objeto (en el guion del mundo: objeto, quien). |
| `al_romperse()` | Cuando el objeto se rompe en pedazos, con las físicas precisas (en el guion del mundo: objeto). |
| `al_soltarse()` | Cuando se rompe o se suelta una articulación del objeto (en el guion del mundo: objeto). |
| `al_recibir_dano(cantidad, de)` | Cuando algo le hace daño con motor.danar (en el guion del mundo: objeto, cantidad, de). |
| `al_recibir(evento, valor, de)` | Un mensaje enviado con motor.emitir, motor.emitir_a o motor.emitir_etiqueta (solo en guiones de objeto). |
| `al_pulsar(accion)` | Al pulsar una acción del mapa de acciones del proyecto. |
| `al_terminar_animacion(animacion)` | Cuando termina un clip que no va en bucle (en el guion del mundo: objeto, animacion). |
| `al_evento_animacion(evento)` | Un suceso «Avisar a los nodos» de la línea de tiempo (en el guion del mundo: objeto, evento). |
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
| `motor.variable(entidad: objeto, nombre: texto)` | valor (cualquiera) | Lee una variable «del objeto» de otro objeto (de sus grafos, o una propiedad de sus guiones): la vida del jugador, las monedas… |
| `motor.poner_variable(entidad: objeto, nombre: texto, valor)` | — | Cambia una variable «del objeto» de otro objeto. Sus grafos y guiones ven el valor nuevo. |

## Matemáticas

| Función | Devuelve | Qué hace |
|---|---|---|
| `motor.aleatorio(desde: número, hasta: número)` | numero (número) | Un número entero al azar entre los dos (los dos incluidos). |

## Vectores y colores

| Función | Devuelve | Qué hace |
|---|---|---|
| `motor.vector(x: número, y: número, z: número)` | v (vector) | Un punto o una dirección en metros (x a la derecha, y arriba, z hacia atrás). |
| `motor.distancia(a: vector, b: vector)` | metros (número) | Los metros que hay entre dos puntos. Vale también con objetos. |
| `motor.longitud(v: vector)` | metros (número) | Lo largo que es (en metros). |
| `motor.normalizar(v: vector)` | v (vector) | La misma dirección, con largo 1. |
| `motor.color(r: número, g: número, b: número)` | color (texto) | Un color, como "#rrggbb". |

## Objetos

| Función | Devuelve | Qué hace |
|---|---|---|
| `motor.entidad(nombre: texto)` | entidad (objeto) | El primer objeto de la escena con ese nombre. |
| `motor.entidades(nombre: texto)` | lista (lista) | Todos los objetos con ese nombre (las copias de un objeto reutilizable, por ejemplo). |
| `motor.nombre(entidad: objeto)` | nombre (texto) | Su nombre en la escena. |
| `motor.posicion(entidad: objeto)` | posicion (vector) | Dónde está ahora el objeto (sus pies), en metros. |
| `motor.poner_posicion(entidad: objeto, posicion: vector)` | — | Lleva el objeto a ese sitio de golpe. Con el jugador, lo teletransporta. |
| `motor.mover_hacia(entidad: objeto, destino: vector, velocidad: número)` | llegado (sí/no) | Da un paso hacia el destino, a esa velocidad. Úsalo en «Cada fotograma» para que vaya andando. |
| `motor.mirar_hacia(entidad: objeto, punto: vector)` | — | Gira el objeto para que mire a ese punto. |
| `motor.mover(entidad: objeto, x: número, y: número, z: número, segundos: número)` | — | La lleva poco a poco a su sitio del editor más esos metros (puertas, plataformas...). |
| `motor.ocultar(entidad: objeto)` | — | El objeto deja de verse y de chocar. |
| `motor.mostrar(entidad: objeto)` | — | Vuelve a verse un objeto oculto. |
| `motor.oculta(entidad: objeto)` | si (sí/no) | Sí si está oculta. |
| `motor.ve(entidad: objeto, objetivo: objeto, alcance: número)` | si (sí/no) | Sí si el objetivo está a la vista: a menos de esa distancia y sin ocultar. |

## Etiquetas y mensajes

| Función | Devuelve | Qué hace |
|---|---|---|
| `motor.tiene_etiqueta(entidad: objeto, etiqueta: texto)` | si (sí/no) | Sí si el objeto lleva esa etiqueta. Para saber con qué se ha chocado. El jugador lleva siempre «jugador». |
| `motor.con_etiqueta(etiqueta: texto)` | lista (lista) | Todos los objetos que llevan esa etiqueta y no están ocultos (para «Para cada elemento»). |
| `motor.mas_cercano(etiqueta: texto, desde: objeto)` | entidad (objeto) | El objeto con esa etiqueta que está más cerca (sin contar el de «cerca de»). Nada si no hay ninguno. |
| `motor.etiquetas(entidad: objeto)` | lista (lista) | Las etiquetas que lleva ahora el objeto. |
| `motor.poner_etiqueta(entidad: objeto, etiqueta: texto)` | — | Le pone una etiqueta mientras dure la partida (en el editor no cambia). |
| `motor.quitar_etiqueta(entidad: objeto, etiqueta: texto)` | — | Le quita una etiqueta mientras dure la partida. |

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
| `motor.animar(entidad: objeto, animacion: texto)` | — | Pone un clip de animaciones/ (o, en 2D, una animación de su hoja de sprites). Manda sobre su máquina de estados hasta que acaba. Vacío = vuelve la de siempre. |
| `motor.animar_al_reves(entidad: objeto, animacion: texto)` | — | Pone el clip hacia atrás desde donde vaya: una puerta abierta con «abrir» se cierra así. Al volver al principio, queda en reposo. |
| `motor.parar_animacion(entidad: objeto)` | — | Quita el clip puesto a mano: vuelve el de su máquina de estados (o se queda quieta). |
| `motor.parametro_animacion(entidad: objeto, nombre: texto, valor: número)` | — | Cambia un parámetro de su máquina de estados (sí = 1, no = 0). Los de velocidad, en el suelo y en el agua los pone el motor. |
| `motor.cinematica(nombre: texto)` | — | Pone una cinemática de cinematicas/: mueve la cámara y los objetos y enseña sus frases. El jugador la salta con Espacio. |
| `motor.terminar_cinematica()` | — | Termina la cinemática que se esté viendo y devuelve la cámara al jugador. |

## Física

| Función | Devuelve | Qué hace |
|---|---|---|
| `motor.empujar(entidad: objeto, fuerza: vector)` | — | Da un empujón a un cuerpo físico: le suma esa velocidad (metros por segundo) de golpe. Pesado o ligero, sale igual de rápido. |
| `motor.velocidad(entidad: objeto)` | v (vector) | Hacia dónde y cuánto se mueve un cuerpo físico, en metros por segundo. |
| `motor.poner_velocidad(entidad: objeto, v: vector)` | — | Cambia de golpe la velocidad de un cuerpo físico (en metros por segundo). |
| `motor.girar_cuerpo(entidad: objeto, giro: vector)` | — | Pone a girar un cuerpo físico alrededor de cada eje (en vueltas por segundo). |
| `motor.tipo_cuerpo(entidad: objeto, tipo: texto)` | — | Dinámico: cae y choca. Cinemático: lo mueven los guiones y las animaciones y empuja a los demás. Fijo: no se mueve nunca. |
| `motor.masa(entidad: objeto)` | masa (número) | Cuánto pesa un cuerpo físico, en kilos. |
| `motor.dormido(entidad: objeto)` | quieto (sí/no) | Sí cuando el cuerpo lleva un rato sin moverse y la física lo ha dejado dormir. |
| `motor.rayo(desde: vector, hacia: vector, alcance: número)` | entidad (objeto), distancia (número), punto (vector) | Una línea invisible desde un punto hacia una dirección: el primer cuerpo físico que toca, a qué distancia y en qué punto (nada si no toca ninguno). |
| `motor.motor_union(entidad: objeto, velocidad: número, fuerza: número)` | — | Enciende el motor de las articulaciones del objeto: en las bisagras, grados por segundo; en las deslizaderas, metros por segundo. Velocidad 0 = frena. |
| `motor.soltar_union(entidad: objeto)` | — | Rompe todas las articulaciones del objeto: se suelta y cae. |
| `motor.romper(entidad: objeto)` | — | Rompe en pedazos un objeto con cuerpo físico, como si le hubieran dado un golpe enorme. |
| `motor.conducir(entidad: objeto, acelerar: número, girar: número, frenar: sí/no)` | — | Mueve un vehículo que conduce un guion: acelerar 1 = adelante, -1 = atrás; girar 1 = a la derecha. Se queda así hasta que se cambie. |
| `motor.velocidad_vehiculo(entidad: objeto)` | v (número) | Lo rápido que va un vehículo, en kilómetros por hora. |

## 2D

| Función | Devuelve | Qué hace |
|---|---|---|
| `motor.voltear(entidad: objeto, espejo: sí/no)` | — | Da la vuelta al sprite del objeto (como en un espejo). |
| `motor.impulsar(entidad: objeto, x: número, y: número)` | — | Empuja un cuerpo físico (o al jugador) con esa velocidad, en casillas por segundo. |
| `motor.casilla(x: número, y: número, capa: texto)` | casilla (número) | El número de la casilla que hay en ese sitio de la capa (nada si está vacía). Capa vacía = la primera que choca. |
| `motor.poner_casilla(x: número, y: número, casilla: número, capa: texto)` | — | Cambia una casilla del mapa mientras se juega (para romper bloques, abrir pasos...). |
| `motor.particulas(entidad: objeto, encendidas: sí/no)` | — | Enciende o apaga el componente Partículas del objeto (también en 3D). |
| `motor.luz_color(entidad: objeto, color: texto)` | — | Cambia el color de la luz del objeto mientras se juega ("#rrggbb"). |
| `motor.luz_fuerza(entidad: objeto, fuerza: número)` | — | Cambia cuánto alumbra la luz del objeto: 0 la apaga, 4 es lo máximo. |
| `motor.luz_alcance(entidad: objeto, alcance: número)` | — | Cambia hasta dónde llega la luz del objeto, en metros. |
| `motor.ambiente(nombre: texto)` | — | Cambia el aspecto del juego mientras se juega: realista, dibujo, neon, acuarela, pixel o ninguno. «proyecto» vuelve al de los ajustes del proyecto. |

## Otros

| Función | Devuelve | Qué hace |
|---|---|---|
| `motor.soltar_particulas(tipo, x, y, z, cantidad)` | — | Suelta de golpe partículas de un tipo (polvo, chispas, lluvia, nieve, humo u hojas) en ese sitio. |
| `motor.danar(entidad, cantidad, de)` | — | Pone en marcha «Al recibir daño» de esa entidad. |
| `motor.emitir(evento, valor, de)` | — | Envía un mensaje a todos: lo reciben los nodos «Al recibir un mensaje» y la función al_recibir de los guiones de entidad. |
| `motor.emitir_a(entidad, evento, valor, de)` | — | Como motor.emitir, pero solo para los comportamientos de esa entidad. |
| `motor.emitir_etiqueta(etiqueta, evento, valor, de)` | — | Como motor.emitir, pero solo para las entidades que llevan esa etiqueta. |

## Extensiones en Rust

Si el proyecto las permite (Ajustes del proyecto › Extensiones), cada extensión compilada de `extensiones/` sale en la tabla `extensiones`: `extensiones.<nombre>.<función>(…)`. Reciben y devuelven números, textos, sí/no, vectores y nil. Ver [Extensiones en Rust](../guia/extensiones-rust.md).

## Herramientas del editor

Los guiones de la carpeta `herramientas/` no son del juego: corren en el editor y tienen su propia API. Ver [Paneles y herramientas propias](../guia/herramientas-propias.md).

| Función | Qué hace |
|---|---|
| `panel(nombre, function(ui) … end)` | Añade un panel a «Paneles propios». La función dibuja el panel en cada fotograma. |
| `herramienta(nombre, function() … end, ayuda)` | Añade una orden al menú Herramientas (la ayuda sale al pasar el ratón). |
| `editor.objetos()` | La lista de objetos de la escena: cada uno con id, nombre, tipo, posicion, giro, escala y etiquetas. |
| `editor.elegido()` | El objeto elegido, o nil. |
| `editor.tipos()` | Los tipos de objeto que se pueden crear. |
| `editor.crear(tipo, x, y, z, nombre)` | Crea un objeto (el nombre es opcional). |
| `editor.mover(objeto, x, y, z)` | Lleva un objeto a esa posición (también con un vector). |
| `editor.girar(objeto, x, y, z)` | Cambia el giro, en grados. |
| `editor.escalar(objeto, cuanto)` | Cambia el tamaño: un número para todo, o x, y, z. |
| `editor.borrar(objeto)` | Borra un objeto. |
| `editor.nombrar(objeto, nombre)` | Le cambia el nombre. |
| `editor.etiquetar(objeto, etiqueta)` | Le pone una etiqueta. |
| `editor.elegir(objeto)` | Lo elige en el editor (nil para no elegir nada). |
| `editor.aviso(texto)` | Escribe en la barra de abajo. |
| `ui.titulo(texto) · ui.texto(texto) · ui.nota(texto) · ui.separador()` | Textos y separadores. |
| `ui.boton(texto)` | Un botón: devuelve true el fotograma en que se pulsa. |
| `ui.casilla(texto, valor)` | Una casilla: devuelve el valor nuevo. |
| `ui.deslizador(texto, valor, min, max)` | Un deslizador: devuelve el valor nuevo. |
| `ui.numero(texto, valor) · ui.campo(texto, valor)` | Un número o un texto que se escribe: devuelven el valor nuevo. |
| `ui.lista(texto, opciones, valor)` | Una lista desplegable: devuelve la opción elegida. |
| `ui.fila(function() … end)` | Pone lo de dentro en una fila. |
