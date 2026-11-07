# Referencia de nodos

<!-- Generado con `foxy-engine --referencia-nodos`. No lo cambies a mano: sale del catálogo del motor. -->

Esta página recoge todos los nodos que trae el motor, agrupados como en la paleta. Cada uno indica su tipo, sus entradas y salidas y su equivalente en Lua. Las funciones hechas con nodos y los nodos escritos en Lua de cada proyecto aparecen además en la paleta de ese proyecto.

| Tipo | Qué es |
|---|---|
| Evento | Empieza una cadena cuando pasa algo. |
| Acción | Hace algo. Tiene cable de ejecución de entrada y de salida. |
| Valor | Calcula algo. No tiene ejecución: se calcula cuando se usa. |
| Flujo | Decide por dónde sigue la ejecución. |

Tipos de dato: **número**, **texto**, **sí/no**, **vector**, **color**, **entidad**, **recurso**, **lista**, **cualquiera**.

## Eventos

### Al empezar {#evento-al_empezar}

*Evento* · `evento.al_empezar`

Al empezar la partida, o al llegar a la escena si es el grafo de una entidad.

En Lua: `function al_empezar() ... end`

### Cada fotograma {#evento-cada_fotograma}

*Evento* · `evento.cada_fotograma`

Unas 60 veces por segundo, mientras se juega. Para lo que se mueve o se comprueba sin parar.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Salida | segundos desde el anterior | número | — |

En Lua: `function cada_fotograma(segundos) ... end`

### Cada segundo {#evento-cada_segundo}

*Evento* · `evento.cada_segundo`

Una vez por segundo, mientras se juega.

En Lua: `function cada_segundo() ... end`

### Cada cierto tiempo {#evento-temporizador}

*Evento* · `evento.temporizador`

Un temporizador: se repite cada tantos segundos.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | cada (segundos) | número | 2 (se escribe en el nodo) |

En Lua: `while true do motor.esperar(cada) ... end`

### Al pulsar una acción {#evento-al_pulsar}

*Evento* · `evento.al_pulsar`

Al pulsar una acción del mapa de acciones del proyecto (vacío = cualquiera).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | acción | recurso | — (se escribe en el nodo) |
| Salida | acción | texto | — |

En Lua: `function al_pulsar(accion) ... end`

### Al chocar con el jugador {#evento-al_chocar}

*Evento* · `evento.al_chocar`

Cuando el jugador toca la entidad. Vacío = esta entidad (o cualquiera en el grafo del juego).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | entidad | entidad | esta entidad (se escribe en el nodo) |
| Salida | entidad | entidad | — |
| Salida | quién choca | entidad | — |

En Lua: `function al_chocar(entidad, otro) ... end`

### Al recoger algo {#evento-al_recoger}

*Evento* · `evento.al_recoger`

Cuando el jugador recoge una entidad con el componente Recogible (vacío = cualquiera).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | entidad | entidad | esta entidad (se escribe en el nodo) |
| Salida | lo recogido | entidad | — |
| Salida | valor que sube | texto | — |

En Lua: `function al_recoger(entidad, valor) ... end`

### Al entrar en una zona {#evento-al_entrar_zona}

*Evento* · `evento.al_entrar_zona`

Cuando el jugador entra en la zona (componente Zona) de una entidad.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | zona de | entidad | esta entidad (se escribe en el nodo) |
| Salida | entidad de la zona | entidad | — |
| Salida | quién entra | entidad | — |

En Lua: `function al_entrar_zona(entidad, quien) ... end`

### Al salir de una zona {#evento-al_salir_zona}

*Evento* · `evento.al_salir_zona`

Cuando el jugador sale de la zona (componente Zona) de una entidad.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | zona de | entidad | esta entidad (se escribe en el nodo) |
| Salida | entidad de la zona | entidad | — |
| Salida | quién sale | entidad | — |

En Lua: `function al_salir_zona(entidad, quien) ... end`

### Al recibir daño {#evento-al_recibir_dano}

*Evento* · `evento.al_recibir_dano`

Cuando algo hace daño a la entidad con «Hacer daño». Pon «jugador» para el jugador.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | quién | entidad | esta entidad (se escribe en el nodo) |
| Salida | quién lo recibe | entidad | — |
| Salida | cantidad | número | — |
| Salida | de quién | entidad | — |

En Lua: `function al_recibir_dano(entidad, cantidad, de) ... end`

### Al recibir un evento {#evento-al_recibir}

*Evento* · `evento.al_recibir`

Un evento propio: otro grafo (o este) lo emite con «Emitir un evento».

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | evento | texto | «mi_evento» (se escribe en el nodo) |
| Salida | valor | cualquiera | — |
| Salida | de quién | entidad | — |

En Lua: `motor.emitir("mi_evento", valor)`

### Al usar un objeto {#evento-al_usar}

*Evento* · `evento.al_usar`

Un objeto con «Al usarlo → llama a…» del guion se usa con E.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | función | texto | «al_usar» (se escribe en el nodo) |
| Salida | qué objeto | texto | — |

En Lua: `function al_abrir_cofre() ... end`

### Al hablar con {#evento-al_hablar}

*Evento* · `evento.al_hablar`

Al hablar con un vecino (vacío = con cualquiera). Responde con «Responder».

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | vecino | texto | — (se escribe en el nodo) |
| Salida | vecino | texto | — |

En Lua: `function al_hablar(vecino) ... end`

### Al entrar en la escena {#evento-al_entrar_escena}

*Evento* · `evento.al_entrar_escena`

Al llegar a una escena (vacío = a cualquiera).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | escena | recurso | — (se escribe en el nodo) |
| Salida | escena | texto | — |

En Lua: `function al_entrar_escena(escena) ... end`

### Al terminar una animación {#evento-al_terminar_animacion}

*Evento* · `evento.al_terminar_animacion`

Cuando un clip que no va en bucle llega al final (o al principio, hacia atrás). Vacío = esta entidad (o cualquiera en el grafo del juego).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | entidad | entidad | esta entidad (se escribe en el nodo) |
| Salida | entidad | entidad | — |
| Salida | animación | texto | — |

En Lua: `function al_terminar_animacion(entidad, animacion) ... end`

### Aviso de una animación {#evento-al_evento_animacion}

*Evento* · `evento.al_evento_animacion`

Un suceso «Avisar a los nodos» de la línea de tiempo (vacío = cualquier aviso).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | entidad | entidad | esta entidad (se escribe en el nodo) |
| Entrada | aviso | texto | — (se escribe en el nodo) |
| Salida | entidad | entidad | — |
| Salida | aviso | texto | — |

En Lua: `function al_evento_animacion(entidad, evento) ... end`

### Al terminar una cinemática {#evento-al_terminar_cinematica}

*Evento* · `evento.al_terminar_cinematica`

Cuando una cinemática acaba o el jugador la salta (vacío = cualquiera).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | cinemática | recurso | — (se escribe en el nodo) |
| Salida | cinemática | texto | — |

En Lua: `function al_terminar_cinematica(cinematica) ... end`

### Cada día nuevo {#evento-al_nuevo_dia}

*Evento* · `evento.al_nuevo_dia`

Cada vez que empieza un día (con el módulo de día y noche).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Salida | día | número | — |

En Lua: `function al_nuevo_dia(dia) ... end`

### Cada hora {#evento-al_cambiar_hora}

*Evento* · `evento.al_cambiar_hora`

Cada vez que el reloj llega a una hora en punto.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Salida | hora | número | — |

En Lua: `function al_cambiar_hora(hora) ... end`

### Al llegar la hora {#evento-al_llegar_hora}

*Evento* · `evento.al_llegar_hora`

Cuando el reloj llega a esa hora en punto.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | hora | número | 8 (se escribe en el nodo) |

En Lua: `function al_cambiar_hora() ... end`

## Flujo

### Si {#control-si}

*Flujo* · `control.si`

Sigue por «sí» o por «no» según la condición.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | condición | sí/no | sí |
| Salida de ejecución | sí | — | — |
| Salida de ejecución | no | — | — |

### Elegir según {#control-elegir}

*Flujo* · `control.elegir`

Sigue por el caso que tenga el mismo valor, o por «otro». Los casos se escriben en el nodo.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | valor | cualquiera | — |
| Salida de ejecución | caso 1 | — | — |
| Salida de ejecución | caso 2 | — | — |
| Salida de ejecución | otro | — | — |

### Repetir {#control-repetir}

*Flujo* · `control.repetir`

Hace lo de «cada vez» tantas veces y luego sigue.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | veces | número | 3 |
| Salida de ejecución | cada vez | — | — |
| Salida de ejecución | al terminar | — | — |
| Salida | vuelta (1, 2...) | número | — |

### Para cada elemento {#control-para_cada}

*Flujo* · `control.para_cada`

Recorre una lista: hace lo de «con cada uno» con cada elemento.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | lista | lista | lista vacía |
| Salida de ejecución | con cada uno | — | — |
| Salida de ejecución | al terminar | — | — |
| Salida | elemento | cualquiera | — |
| Salida | posición | número | — |

### Mientras {#control-mientras}

*Flujo* · `control.mientras`

Repite mientras se cumpla la condición. Si nunca deja de cumplirse, el motor lo para.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | condición | sí/no | no |
| Salida de ejecución | mientras se cumpla | — | — |
| Salida de ejecución | al terminar | — | — |

### Secuencia {#control-secuencia}

*Flujo* · `control.secuencia`

Hace una salida detrás de otra: 1, 2, 3...

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Salida de ejecución | 1 | — | — |
| Salida de ejecución | 2 | — | — |

### Esperar {#control-esperar}

*Flujo* · `control.esperar`

Espera y sigue después, sin parar el juego.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | segundos | número | 1 |

### Solo una vez {#control-una_vez}

*Flujo* · `control.una_vez`

Deja pasar la primera vez y ninguna más (por cada entidad).

### Puerta {#control-puerta}

*Flujo* · `control.puerta`

Deja pasar mientras está abierta. Ábrela o ciérrala con sus otras entradas.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada de ejecución | abrir | — | — |
| Entrada de ejecución | cerrar | — | — |
| Entrada | empieza abierta | sí/no | sí (se escribe en el nodo) |

### Emitir un evento {#control-emitir}

*Flujo* · `control.emitir`

Avisa a todos los grafos: los nodos «Al recibir un evento» con ese nombre se ponen en marcha.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | evento | texto | «mi_evento» (se escribe en el nodo) |
| Entrada | valor | cualquiera | — |

### Emitir un evento a {#control-emitir_a}

*Flujo* · `control.emitir_a`

Como «Emitir un evento», pero solo lo recibe el grafo de esa entidad.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | entidad | entidad | jugador |
| Entrada | evento | texto | «mi_evento» (se escribe en el nodo) |
| Entrada | valor | cualquiera | — |

### Responder {#control-responder}

*Flujo* · `control.responder`

Lo que contesta el vecino (en «Al hablar con»). Acaba la cadena.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | texto | texto | «¡Hola!» |

### Acabar aquí {#control-parar}

*Flujo* · `control.parar`

Termina la cadena: no hace nada más.

### Punto de paso {#redireccion-flujo}

*Flujo* · `redireccion.flujo`

Solo sirve para llevar el cable por otro sitio.

## Variables

Las variables del grafo, de la entidad y del juego se leen y se cambian con los nodos **Leer** y **Poner** que añaden sus botones en el grupo *Variables* del panel; su tipo es el de la variable. Los nodos de esta categoría leen y cambian las variables de la entidad de **otra** entidad.

### Variable de una entidad {#motor-variable}

*Valor* · `motor.variable`

Lee una variable «de la entidad» de otra entidad.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | entidad | entidad | esta entidad |
| Entrada | variable | texto | «vida» |
| Salida | valor | cualquiera | — |

En Lua: `local valor = motor.variable(entidad, nombre)`

### Poner variable de una entidad {#motor-poner_variable}

*Acción* · `motor.poner_variable`

Cambia una variable «de la entidad» de otra entidad.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | entidad | entidad | esta entidad |
| Entrada | variable | texto | «vida» |
| Entrada | valor | cualquiera | — |

En Lua: `motor.poner_variable(entidad, nombre, valor)`

## Matemáticas

### Sumar {#mat-sumar}

*Valor* · `mat.sumar`

a + b

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | a | número | 0 |
| Entrada | b | número | 1 |
| Salida | resultado | número | — |

En Lua: `(a + b)`

### Restar {#mat-restar}

*Valor* · `mat.restar`

a − b

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | a | número | 0 |
| Entrada | b | número | 1 |
| Salida | resultado | número | — |

En Lua: `(a - b)`

### Multiplicar {#mat-multiplicar}

*Valor* · `mat.multiplicar`

a × b

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | a | número | 0 |
| Entrada | b | número | 1 |
| Salida | resultado | número | — |

En Lua: `(a * b)`

### Dividir {#mat-dividir}

*Valor* · `mat.dividir`

a ÷ b (si b es 0, da 0).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | a | número | 0 |
| Entrada | b | número | 1 |
| Salida | resultado | número | — |

En Lua: `__foxy.dividir(a, b)`

### Resto {#mat-resto}

*Valor* · `mat.resto`

Lo que sobra al dividir a entre b.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | a | número | 0 |
| Entrada | b | número | 1 |
| Salida | resultado | número | — |

En Lua: `__foxy.resto(a, b)`

### Potencia {#mat-potencia}

*Valor* · `mat.potencia`

a elevado a b.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | a | número | 0 |
| Entrada | b | número | 1 |
| Salida | resultado | número | — |

En Lua: `(a ^ b)`

### Mínimo {#mat-minimo}

*Valor* · `mat.minimo`

El más pequeño de los dos.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | a | número | 0 |
| Entrada | b | número | 1 |
| Salida | resultado | número | — |

En Lua: `math.min(a, b)`

### Máximo {#mat-maximo}

*Valor* · `mat.maximo`

El más grande de los dos.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | a | número | 0 |
| Entrada | b | número | 1 |
| Salida | resultado | número | — |

En Lua: `math.max(a, b)`

### Valor absoluto {#mat-absoluto}

*Valor* · `mat.absoluto`

El número sin signo.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | número | número | 0 |
| Salida | resultado | número | — |

En Lua: `math.abs(n)`

### Redondear {#mat-redondear}

*Valor* · `mat.redondear`

Al entero más cercano.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | número | número | 0 |
| Salida | resultado | número | — |

En Lua: `__foxy.redondear(n)`

### Raíz cuadrada {#mat-raiz}

*Valor* · `mat.raiz`

La raíz cuadrada.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | número | número | 0 |
| Salida | resultado | número | — |

En Lua: `math.sqrt(math.max(0, n))`

### Seno {#mat-seno}

*Valor* · `mat.seno`

El seno de un ángulo en grados: va de −1 a 1 y vuelve. Para lo que sube y baja o va y viene.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | número | número | 0 |
| Salida | resultado | número | — |

En Lua: `math.sin(math.rad(n))`

### Coseno {#mat-coseno}

*Valor* · `mat.coseno`

El coseno de un ángulo en grados (como el seno, un cuarto de vuelta antes).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | número | número | 0 |
| Salida | resultado | número | — |

En Lua: `math.cos(math.rad(n))`

### Limitar {#mat-limitar}

*Valor* · `mat.limitar`

El número, sin bajar del mínimo ni pasar del máximo.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | número | número | 0 |
| Entrada | mínimo | número | 0 |
| Entrada | máximo | número | 100 |
| Salida | resultado | número | — |

En Lua: `math.max(min, math.min(max, n))`

### Mezclar números {#mat-interpolar}

*Valor* · `mat.interpolar`

Un número entre a y b: con 0 da a, con 1 da b.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | de | número | 0 |
| Entrada | a | número | 1 |
| Entrada | cuánto (0 a 1) | número | 0.5 |
| Salida | resultado | número | — |

En Lua: `(a + (b - a) * t)`

### Número al azar {#motor-aleatorio}

*Valor* · `motor.aleatorio`

Un número entero al azar entre los dos (los dos incluidos).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | desde | número | 1 |
| Entrada | hasta | número | 6 |
| Salida | número | número | — |

En Lua: `local numero = motor.aleatorio(desde, hasta)`

## Lógica

### Sale al azar {#mat-azar_si}

*Valor* · `mat.azar_si`

Sí esa proporción de las veces.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | % de las veces | número | 50 |
| Salida | sale | sí/no | — |

En Lua: `(motor.aleatorio(1, 100) <= por_ciento)`

### Comparar {#logica-comparar}

*Valor* · `logica.comparar`

Compara dos valores: igual, distinto, mayor, menor... Los números escritos como texto cuentan como números.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | a | cualquiera | 0 |
| Entrada | op | texto | «==» (se escribe en el nodo) |
| Entrada | b | cualquiera | 0 |
| Salida | resultado | sí/no | — |

En Lua: `__foxy.comparar(a, op, b)`

### Y {#logica-y}

*Valor* · `logica.y`

Sí cuando se cumplen las dos.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | a | sí/no | sí |
| Entrada | b | sí/no | sí |
| Salida | las dos | sí/no | — |

En Lua: `(a and b)`

### O {#logica-o}

*Valor* · `logica.o`

Sí cuando se cumple alguna de las dos.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | a | sí/no | no |
| Entrada | b | sí/no | no |
| Salida | alguna | sí/no | — |

En Lua: `(a or b)`

### No {#logica-no}

*Valor* · `logica.no`

Lo contrario: sí si es no, y no si es sí.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | a | sí/no | no |
| Salida | al revés | sí/no | — |

En Lua: `(not a)`

### Uno u otro {#logica-elegir}

*Valor* · `logica.elegir`

Da un valor u otro según la condición.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | si | sí/no | sí |
| Entrada | entonces | cualquiera | — |
| Entrada | si no | cualquiera | — |
| Salida | valor | cualquiera | — |

En Lua: `__foxy.si(condicion, si, no)`

### Tiene valor {#logica-existe}

*Valor* · `logica.existe`

Sí si el valor existe (una variable sin poner, una entidad que no está... no tienen).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | valor | cualquiera | — |
| Salida | tiene valor | sí/no | — |

En Lua: `(valor ~= nil)`

## Texto

### Unir textos {#texto-unir}

*Valor* · `texto.unir`

Pone un texto detrás de otro. Los números se escriben solos.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | a | texto | «Vida: » |
| Entrada | b | texto | — |
| Salida | texto | texto | — |

En Lua: `(a .. b)`

### Largo del texto {#texto-longitud}

*Valor* · `texto.longitud`

Cuántas letras tiene.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | texto | texto | — |
| Salida | letras | número | — |

En Lua: `(utf8.len(texto) or 0)`

### El texto contiene {#texto-contiene}

*Valor* · `texto.contiene`

Sí si el texto tiene dentro lo que se busca.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | texto | texto | — |
| Entrada | buscar | texto | — |
| Salida | lo contiene | sí/no | — |

En Lua: `(string.find(texto, buscar, 1, true) ~= nil)`

### Texto a número {#texto-numero}

*Valor* · `texto.numero`

El número que hay escrito (0 si no es un número).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | texto | texto | «0» |
| Salida | número | número | — |

En Lua: `(tonumber(texto) or 0)`

## Vectores y colores

### Hacer un vector {#motor-vector}

*Valor* · `motor.vector`

Un punto o una dirección en metros (x a la derecha, y arriba, z hacia atrás).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | x | número | 0 |
| Entrada | y | número | 0 |
| Entrada | z | número | 0 |
| Salida | vector | vector | — |

En Lua: `local v = motor.vector(x, y, z)`

### Separar un vector {#vec-separar}

*Valor* · `vec.separar`

Las tres partes de un vector.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | vector | vector | (0, 0, 0) |
| Salida | x | número | — |
| Salida | y | número | — |
| Salida | z | número | — |

En Lua: `(v).x  ·  (v).y  ·  (v).z`

### Sumar vectores {#vec-sumar}

*Valor* · `vec.sumar`

a + b

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | a | vector | (0, 0, 0) |
| Entrada | b | vector | (0, 0, 0) |
| Salida | vector | vector | — |

En Lua: `(a + b)`

### Restar vectores {#vec-restar}

*Valor* · `vec.restar`

a − b (la flecha que va de b a a).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | a | vector | (0, 0, 0) |
| Entrada | b | vector | (0, 0, 0) |
| Salida | vector | vector | — |

En Lua: `(a - b)`

### Dirección hacia {#vec-direccion}

*Valor* · `vec.direccion`

La dirección (de largo 1) que va de a hacia b.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | a | vector | (0, 0, 0) |
| Entrada | b | vector | (0, 0, 0) |
| Salida | vector | vector | — |

En Lua: `motor.normalizar(b - a)`

### Multiplicar vector {#vec-escalar}

*Valor* · `vec.escalar`

El vector, más largo o más corto.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | vector | vector | (0, 0, 0) |
| Entrada | por | número | 2 |
| Salida | vector | vector | — |

En Lua: `(v * k)`

### Distancia {#motor-distancia}

*Valor* · `motor.distancia`

Los metros que hay entre dos puntos. Vale también con entidades.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | a | vector | (0, 0, 0) |
| Entrada | b | vector | (0, 0, 0) |
| Salida | metros | número | — |

En Lua: `local metros = motor.distancia(a, b)`

### Largo del vector {#motor-longitud}

*Valor* · `motor.longitud`

Lo largo que es (en metros).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | vector | vector | (0, 0, 0) |
| Salida | metros | número | — |

En Lua: `local metros = motor.longitud(v)`

### Vector de largo 1 {#motor-normalizar}

*Valor* · `motor.normalizar`

La misma dirección, con largo 1.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | vector | vector | (0, 0, 0) |
| Salida | dirección | vector | — |

En Lua: `local v = motor.normalizar(v)`

### Hacer un color {#motor-color}

*Valor* · `motor.color`

Un color, como "#rrggbb".

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | rojo (0-255) | número | 255 |
| Entrada | verde (0-255) | número | 255 |
| Entrada | azul (0-255) | número | 255 |
| Salida | color | color | — |

En Lua: `local color = motor.color(r, g, b)`

## Listas

### Lista {#lista-nueva}

*Valor* · `lista.nueva`

Una lista con esos valores (los vacíos no cuentan).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | 1 | cualquiera | — |
| Entrada | 2 | cualquiera | — |
| Entrada | 3 | cualquiera | — |
| Salida | lista | lista | — |

En Lua: `__foxy.lista(a, b, c)`

### Lista vacía {#lista-vacia}

*Valor* · `lista.vacia`

Una lista sin nada (guárdala en una variable para ir llenándola).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Salida | lista | lista | — |

En Lua: `{}`

### Elemento de la lista {#lista-elemento}

*Valor* · `lista.elemento`

El elemento de esa posición (la primera es la 1).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | lista | lista | lista vacía |
| Entrada | posición | número | 1 |
| Salida | valor | cualquiera | — |

En Lua: `((lista) or {})[i]`

### Cuántos hay {#lista-tamano}

*Valor* · `lista.tamano`

Cuántos elementos tiene la lista.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | lista | lista | lista vacía |
| Salida | cuántos | número | — |

En Lua: `#((lista) or {})`

### La lista contiene {#lista-contiene}

*Valor* · `lista.contiene`

Sí si el valor está en la lista.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | lista | lista | lista vacía |
| Entrada | valor | cualquiera | — |
| Salida | lo contiene | sí/no | — |

En Lua: `__foxy.contiene(lista, valor)`

### Elemento al azar {#lista-azar}

*Valor* · `lista.azar`

Uno cualquiera de la lista.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | lista | lista | lista vacía |
| Salida | valor | cualquiera | — |

En Lua: `__foxy.azar(lista)`

### Añadir a la lista {#lista-anadir}

*Acción* · `lista.anadir`

Pone el valor al final de la lista.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | lista | lista | lista vacía |
| Entrada | valor | cualquiera | — |

En Lua: `__foxy.anadir(lista, valor)`

### Quitar de la lista {#lista-quitar}

*Acción* · `lista.quitar`

Quita el elemento de esa posición.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | lista | lista | lista vacía |
| Entrada | posición | número | 1 |

En Lua: `__foxy.quitar(lista, i)`

## Entidades

### Esta entidad {#ent-yo}

*Valor* · `ent.yo`

La entidad que tiene este grafo (nada en el grafo del juego).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Salida | entidad | entidad | — |

En Lua: `yo`

### Entidad que se llama {#motor-entidad}

*Valor* · `motor.entidad`

La primera entidad de la escena con ese nombre.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | nombre | texto | — |
| Salida | entidad | entidad | — |

En Lua: `local entidad = motor.entidad(nombre)`

### Entidades que se llaman {#motor-entidades}

*Valor* · `motor.entidades`

Todas las entidades con ese nombre (las copias de un prefabricado, por ejemplo).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | nombre | texto | — |
| Salida | lista | lista | — |

En Lua: `local lista = motor.entidades(nombre)`

### Nombre de la entidad {#motor-nombre}

*Valor* · `motor.nombre`

Su nombre en la escena.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | entidad | entidad | esta entidad |
| Salida | nombre | texto | — |

En Lua: `local nombre = motor.nombre(entidad)`

### Posición {#motor-posicion}

*Valor* · `motor.posicion`

Dónde está ahora la entidad (sus pies), en metros.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | entidad | entidad | esta entidad |
| Salida | posición | vector | — |

En Lua: `local posicion = motor.posicion(entidad)`

### Poner en un sitio {#motor-poner_posicion}

*Acción* · `motor.poner_posicion`

Lleva la entidad a ese sitio de golpe. Con el jugador, lo teletransporta.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | entidad | entidad | esta entidad |
| Entrada | posición | vector | (0, 0, 0) |

En Lua: `motor.poner_posicion(entidad, posicion)`

### Ir hacia {#motor-mover_hacia}

*Acción* · `motor.mover_hacia`

Da un paso hacia el destino, a esa velocidad. Úsalo en «Cada fotograma» para que vaya andando.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | entidad | entidad | esta entidad |
| Entrada | destino | vector | (0, 0, 0) |
| Entrada | metros por segundo | número | 3 |
| Salida | ha llegado | sí/no | — |

En Lua: `local llegado = motor.mover_hacia(entidad, destino, velocidad)`

### Mirar hacia {#motor-mirar_hacia}

*Acción* · `motor.mirar_hacia`

Gira la entidad para que mire a ese punto.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | entidad | entidad | esta entidad |
| Entrada | punto | vector | (0, 0, 0) |

En Lua: `motor.mirar_hacia(entidad, punto)`

### Mover desde su sitio {#motor-mover}

*Acción* · `motor.mover`

La lleva poco a poco a su sitio del editor más esos metros (puertas, plataformas...).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | entidad | entidad | esta entidad |
| Entrada | x | número | 0 |
| Entrada | y | número | 2.5 |
| Entrada | z | número | 0 |
| Entrada | en segundos | número | 0.6 |

En Lua: `motor.mover(entidad, x, y, z, segundos)`

### Ocultar {#motor-ocultar}

*Acción* · `motor.ocultar`

La entidad deja de verse y de chocar.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | entidad | entidad | esta entidad |

En Lua: `motor.ocultar(entidad)`

### Mostrar {#motor-mostrar}

*Acción* · `motor.mostrar`

Vuelve a verse una entidad oculta.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | entidad | entidad | esta entidad |

En Lua: `motor.mostrar(entidad)`

### Está oculta {#motor-oculta}

*Valor* · `motor.oculta`

Sí si está oculta.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | entidad | entidad | esta entidad |
| Salida | oculta | sí/no | — |

En Lua: `local si = motor.oculta(entidad)`

### Ve a {#motor-ve}

*Valor* · `motor.ve`

Sí si el objetivo está a la vista: a menos de esa distancia y sin ocultar.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | quién mira | entidad | esta entidad |
| Entrada | a quién | entidad | jugador |
| Entrada | hasta (metros) | número | 8 |
| Salida | lo ve | sí/no | — |

En Lua: `local si = motor.ve(entidad, objetivo, alcance)`

### Hacer daño {#motor-danar}

*Acción* · `motor.danar`

Pone en marcha «Al recibir daño» de esa entidad (y los del juego). Qué pasa con la vida lo decides tú.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | a quién | entidad | jugador |
| Entrada | cantidad | número | 10 |

En Lua: `motor.danar(entidad, cantidad, yo)`

## Jugador

### El jugador {#ent-jugador}

*Valor* · `ent.jugador`

El jugador, como entidad (para «Hacer daño», «Distancia»...).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Salida | jugador | entidad | — |

En Lua: `0`

### Posición del jugador {#motor-posicion_jugador}

*Valor* · `motor.posicion_jugador`

Dónde están los pies del jugador, en metros.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Salida | posición | vector | — |

En Lua: `local posicion = motor.posicion_jugador()`

### Acción apretada {#motor-accion}

*Valor* · `motor.accion`

Sí mientras se aprieta esa acción del mapa de acciones.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | acción | recurso | «Saltar» |
| Salida | apretada | sí/no | — |

En Lua: `local si = motor.accion(nombre)`

### Acción recién pulsada {#motor-accion_pulsada}

*Valor* · `motor.accion_pulsada`

Sí solo en el fotograma en que se pulsa.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | acción | recurso | «Saltar» |
| Salida | pulsada | sí/no | — |

En Lua: `local si = motor.accion_pulsada(nombre)`

## Mensajes y consola

### Decir {#motor-decir}

*Acción* · `motor.decir`

Enseña un mensaje abajo en la pantalla.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | texto | texto | «¡Hola!» |

En Lua: `motor.decir(texto)`

### Escribir en la consola {#motor-imprimir}

*Acción* · `motor.imprimir`

Escribe en la consola del editor (para comprobar cosas).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | texto | texto | — |

En Lua: `motor.imprimir(texto)`

## Tiempo y clima

### Hora {#motor-hora}

*Valor* · `motor.hora`

La hora del reloj del juego, con decimales.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Salida | hora (0-24) | número | — |

En Lua: `local hora = motor.hora()`

### Poner la hora {#motor-poner_hora}

*Acción* · `motor.poner_hora`

Cambia la hora del reloj.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | hora | número | 8 |

En Lua: `motor.poner_hora(hora)`

### Día {#motor-dia}

*Valor* · `motor.dia`

El día de la partida (empieza en 1).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Salida | día | número | — |

En Lua: `local dia = motor.dia()`

### Tiempo jugando {#motor-tiempo}

*Valor* · `motor.tiempo`

Segundos desde que empezó la partida.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Salida | segundos | número | — |

En Lua: `local segundos = motor.tiempo()`

### Clima {#motor-clima}

*Valor* · `motor.clima`

despejado, nublado, lluvia o tormenta.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Salida | clima | texto | — |

En Lua: `local clima = motor.clima()`

### Poner el clima {#motor-poner_clima}

*Acción* · `motor.poner_clima`

Cambia el clima poco a poco.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | clima | texto | «lluvia» |

En Lua: `motor.poner_clima(clima)`

### Hace este clima {#clima-es}

*Valor* · `clima.es`

Sí si el clima es ese.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | clima | texto | «lluvia» |
| Salida | sí | sí/no | — |

En Lua: `(motor.clima() == clima)`

### Estación {#motor-estacion}

*Valor* · `motor.estacion`

primavera, verano, otono o invierno.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Salida | estación | texto | — |

En Lua: `local estacion = motor.estacion()`

### Poner la estación {#motor-poner_estacion}

*Acción* · `motor.poner_estacion`

Cambia la estación.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | estación | texto | «invierno» |

En Lua: `motor.poner_estacion(estacion)`

### Es esta estación {#estacion-es}

*Valor* · `estacion.es`

Sí si la estación es esa.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | estación | texto | «invierno» |
| Salida | sí | sí/no | — |

En Lua: `(motor.estacion() == estacion)`

### La hora está entre {#hora-entre}

*Valor* · `hora.entre`

Sí entre esas dos horas (si «desde» es mayor, pasa por la medianoche).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | desde | número | 20 |
| Entrada | hasta | número | 6 |
| Salida | sí | sí/no | — |

En Lua: `__foxy.hora_entre(desde, hasta)`

## Escenas e interfaces

### Escena {#motor-escena}

*Valor* · `motor.escena`

El nombre de la escena en la que se está.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Salida | escena | texto | — |

En Lua: `local escena = motor.escena()`

### Ir a la escena {#motor-cambiar_escena}

*Acción* · `motor.cambiar_escena`

Va a otra escena (y entra por esa entrada, si se dice).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | escena | recurso | — |
| Entrada | entrada | texto | — |

En Lua: `motor.cambiar_escena(escena, entrada)`

### Abrir la interfaz {#motor-abrir_interfaz}

*Acción* · `motor.abrir_interfaz`

Abre una interfaz del proyecto encima del juego.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | interfaz | recurso | — |

En Lua: `motor.abrir_interfaz(nombre)`

### Cerrar la interfaz {#motor-cerrar_interfaz}

*Acción* · `motor.cerrar_interfaz`

Cierra esa interfaz (vacío = la de más arriba).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | interfaz | recurso | — |

En Lua: `motor.cerrar_interfaz(nombre)`

### Volver a empezar {#motor-partida_nueva}

*Acción* · `motor.partida_nueva`

Empieza una partida nueva desde el principio.

En Lua: `motor.partida_nueva()`

## Sonido

### Sonar {#motor-sonar}

*Acción* · `motor.sonar`

Toca un sonido del proyecto (de sonidos/) o uno de ejemplo: paso, salto, campana...

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | sonido | recurso | «campana» |

En Lua: `motor.sonar(sonido)`

## Valores del juego

### Valor del juego {#motor-valor}

*Valor* · `motor.valor`

Un valor guardado con la partida (las interfaces lo enseñan con {nombre}).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | nombre | texto | «monedas» |
| Salida | valor | cualquiera | — |

En Lua: `local valor = motor.valor(nombre)`

### Poner un valor {#motor-poner_valor}

*Acción* · `motor.poner_valor`

Guarda un valor del juego.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | nombre | texto | «monedas» |
| Entrada | valor | cualquiera | «0» |

En Lua: `motor.poner_valor(nombre, valor)`

### Sumar a un valor {#motor-sumar_valor}

*Acción* · `motor.sumar_valor`

Suma (o resta, con un número negativo) a un valor del juego.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | nombre | texto | «monedas» |
| Entrada | cantidad | número | 1 |

En Lua: `motor.sumar_valor(nombre, cantidad)`

## Vecinos

### Vecinos {#motor-vecinos}

*Valor* · `motor.vecinos`

Los nombres de los vecinos de la escena.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Salida | nombres | lista | — |

En Lua: `local lista = motor.vecinos()`

### Dónde está el vecino {#motor-vecino}

*Valor* · `motor.vecino`

La posición de un vecino.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | vecino | texto | — |
| Salida | x | número | — |
| Salida | y | número | — |
| Salida | z | número | — |

En Lua: `local x, y, z = motor.vecino(nombre)`

### Llevar a un vecino {#motor-llevar}

*Acción* · `motor.llevar`

El vecino camina hasta allí.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | vecino | texto | — |
| Entrada | x | número | 0 |
| Entrada | y | número | 0 |
| Entrada | z | número | 0 |

En Lua: `motor.llevar(nombre, x, y, z)`

## Animación

### Animar {#motor-animar}

*Acción* · `motor.animar`

Pone un clip de animaciones/ (o, en 2D, una animación de su hoja de sprites). Manda sobre su máquina de estados hasta que acaba. Vacío = vuelve la de siempre.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | entidad | entidad | esta entidad |
| Entrada | animación | recurso | «abrir» |

En Lua: `motor.animar(entidad, animacion)`

### Animar hacia atrás {#motor-animar_al_reves}

*Acción* · `motor.animar_al_reves`

Pone el clip hacia atrás desde donde vaya: una puerta abierta con «abrir» se cierra así. Al volver al principio, queda en reposo.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | entidad | entidad | esta entidad |
| Entrada | animación | recurso | «abrir» |

En Lua: `motor.animar_al_reves(entidad, animacion)`

### Parar la animación {#motor-parar_animacion}

*Acción* · `motor.parar_animacion`

Quita el clip puesto a mano: vuelve el de su máquina de estados (o se queda quieta).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | entidad | entidad | esta entidad |

En Lua: `motor.parar_animacion(entidad)`

### Poner un parámetro de animación {#motor-parametro_animacion}

*Acción* · `motor.parametro_animacion`

Cambia un parámetro de su máquina de estados (sí = 1, no = 0). Los de velocidad, en el suelo y en el agua los pone el motor.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | entidad | entidad | esta entidad |
| Entrada | parámetro | texto | «enfadado» |
| Entrada | valor | número | 1 |

En Lua: `motor.parametro_animacion(entidad, nombre, valor)`

### Poner una cinemática {#motor-cinematica}

*Acción* · `motor.cinematica`

Pone una cinemática de cinematicas/: mueve la cámara y las entidades y enseña sus frases. El jugador la salta con Espacio.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | cinemática | recurso | — |

En Lua: `motor.cinematica(nombre)`

### Terminar la cinemática {#motor-terminar_cinematica}

*Acción* · `motor.terminar_cinematica`

Termina la cinemática que se esté viendo y devuelve la cámara al jugador.

En Lua: `motor.terminar_cinematica()`

## 2D

### Dar la vuelta al sprite {#motor-voltear}

*Acción* · `motor.voltear`

Da la vuelta al sprite de la entidad (como en un espejo).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | entidad | entidad | esta entidad |
| Entrada | mirando a la izquierda | sí/no | sí |

En Lua: `motor.voltear(entidad, espejo)`

### Impulsar {#motor-impulsar}

*Acción* · `motor.impulsar`

Empuja un cuerpo físico (o al jugador) con esa velocidad, en casillas por segundo.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | entidad | entidad | esta entidad |
| Entrada | x | número | 0 |
| Entrada | y | número | 8 |

En Lua: `motor.impulsar(entidad, x, y)`

### Casilla en {#motor-casilla}

*Valor* · `motor.casilla`

El número de la casilla que hay en ese sitio de la capa (nada si está vacía). Capa vacía = la primera que choca.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | x | número | 0 |
| Entrada | y | número | 0 |
| Entrada | capa | texto | — |
| Salida | casilla | número | — |

En Lua: `local casilla = motor.casilla(x, y, capa)`

### Poner una casilla {#motor-poner_casilla}

*Acción* · `motor.poner_casilla`

Cambia una casilla del mapa mientras se juega (para romper bloques, abrir pasos...).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | x | número | 0 |
| Entrada | y | número | 0 |
| Entrada | casilla | número | 0 |
| Entrada | capa | texto | — |

En Lua: `motor.poner_casilla(x, y, casilla, capa)`

### Encender partículas {#motor-particulas}

*Acción* · `motor.particulas`

Enciende o apaga el componente Partículas de la entidad (también en 3D).

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | entidad | entidad | esta entidad |
| Entrada | encendidas | sí/no | sí |

En Lua: `motor.particulas(entidad, encendidas)`

### Soltar partículas {#motor-soltar_particulas}

*Acción* · `motor.soltar_particulas`

Suelta de golpe partículas de un tipo: polvo, chispas, lluvia, nieve, humo u hojas.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | tipo | texto | «chispas» |
| Entrada | dónde | vector | (0, 0, 0) |
| Entrada | cuántas | número | 12 |

En Lua: `motor.soltar_particulas(tipo, punto.x, punto.y, punto.z, cantidad)`

## Otros

### Comentario {#comentario}

*Nota* · `comentario`

Un marco con un título para agrupar nodos. Al moverlo se mueve lo que tiene dentro.

### Punto de paso (datos) {#redireccion-dato}

*Valor* · `redireccion.dato`

Solo sirve para llevar un cable de datos por otro sitio.

| Pin | Nombre | Tipo | Valor de partida |
|---|---|---|---|
| Entrada | valor | cualquiera | — |
| Salida | valor | cualquiera | — |

En Lua: `valor`

## Funciones

Las funciones hechas con nodos del proyecto aparecen en esta categoría de la paleta, con el nombre, las entradas y las salidas que les hayas dado. Dentro de una función hay además dos nodos propios:

| Nodo | Qué hace |
|---|---|
| **Entrada** | Donde empieza la función. Sus salidas son lo que recibe |
| **Devolver** | Donde acaba. Sus entradas son lo que devuelve |

Los nodos escritos en Lua (`nodos/*.lua`) salen en la categoría que diga su cabecera.
