# Eventos y flujo

Toda cadena de nodos empieza en un **evento** y sigue por los cables de
ejecución. Los nodos de **flujo** deciden por dónde sigue: elegir un
camino, repetir, esperar o dejar pasar solo una vez. Esta página explica
los dos grupos con ejemplos. La lista completa, con todos sus pines, está
en la [Referencia de nodos](../referencia/nodos.md).

## Eventos

Un evento se pone en marcha cuando pasa algo en el juego. Puedes poner el
mismo evento varias veces en un grafo: todos se ejecutan, de arriba abajo
según su posición en el lienzo.

| Evento | Cuándo pasa |
|---|---|
| **Al empezar** | Al empezar la partida. En un grafo de escena o de objeto, al llegar a la escena |
| **Cada fotograma** | Unas 60 veces por segundo. Su salida *segundos desde el anterior* sirve para moverse a velocidad constante |
| **Cada segundo** | Una vez por segundo |
| **Cada cierto tiempo** | Cada tantos segundos, los que escribas en el nodo |
| **Al pulsar una acción** | Al pulsar una [acción de entrada](acciones-entrada.md). Vacío: cualquiera |
| **Al chocar con el jugador** | Cuando el jugador toca el objeto. En un grafo de objeto, vacío significa este objeto |
| **Al entrar en una zona** / **Al salir de una zona** | Cuando el jugador entra o sale de un objeto con el componente [Zona](../referencia/componentes/zona.md) |
| **Al recibir daño** | Cuando un nodo *Hacer daño* (o `motor.danar` en Lua) apunta a ese objeto. Da la cantidad y quién lo hace |
| **Al chocar con otro objeto** | Cuando el objeto toca a otro objeto. Con *con etiqueta*, solo si el otro la lleva |
| **Al entrar un objeto en una zona** / **Al salir un objeto de una zona** | Lo mismo que las zonas del jugador, pero con los demás objetos que se mueven |
| **Al hacer clic en el objeto** | Cuando el jugador hace clic mirando al objeto (3D) |
| **Al recibir un mensaje** | Cuando otro grafo, o un guion, envía un mensaje con ese nombre |
| **Al usar un objeto** | Cuando se usa con <kbd>E</kbd> un objeto cuya acción es *Llamar al guion* con ese nombre de función |
| **Al hablar con** | Al hablar con un vecino. Termina con *Responder* para darle su frase |
| **Al entrar en la escena** | Al llegar a esa escena (vacío: a cualquiera) |
| **Cada día nuevo**, **Cada hora**, **Al llegar la hora** | Con el reloj del juego. Ver [La vida del mundo](vida.md) |

Los eventos de objeto (chocar, zonas, daño) llevan un filtro *objeto*.
En el grafo del juego, déjalo vacío para recibir los de todos los objetos
y usa la salida *objeto* para saber de cuál se trata.

### Mensajes

Un mensaje es un aviso con nombre que inventas tú. Sirve para que
grafos distintos se comuniquen sin conocerse:

1. En el grafo que avisa, añade **Enviar mensaje a todos** y escribe su
   nombre, por ejemplo `alarma`. Opcionalmente, conecta un valor.
2. En cualquier otro grafo, añade **Al recibir un mensaje** con el mismo
   nombre. Su salida *valor* trae lo que se envió y *de quién*, el objeto
   que lo envió.

**Enviar mensaje a un objeto** solo llega a ese objeto, y **Enviar mensaje
a los de una etiqueta**, a todas las que la llevan. Desde Lua, usa
`motor.emitir("alarma", valor)`. Ver
[Objetos que se hablan](objetos-que-se-hablan.md).

## Flujo

### Si y Elegir según

**Si** sigue por *sí* o por *no* según una condición de tipo sí/no, como la
salida de *Comparar*, *Ve a* o *Está oculta*.

**Elegir según** compara un valor con varios casos escritos en el nodo y
sigue por el que coincida, o por *otro* si no coincide ninguno. Añade o
quita casos en los ajustes del nodo.

Ejemplo: según el clima, el vecino dice una cosa u otra.

1. **Al hablar con** (vecino *Plumas*) → **Elegir según**.
2. Conecta **Clima** a la entrada *valor* de *Elegir según* y escribe los
   casos `lluvia` y `tormenta`.
3. De *caso 1* y *caso 2* sale un **Responder** con «Mejor quédate en
   casa», y de *otro*, un **Responder** con «¡Qué buen día!».

### Repetir, Para cada elemento y Mientras

Los tres tienen dos salidas de ejecución: lo que se hace **en cada vuelta**
y lo que viene **al terminar**.

- **Repetir** da tantas vueltas como diga *veces*. Su salida *vuelta* cuenta
  desde 1.
- **Para cada elemento** recorre una lista. Por ejemplo, con
  **Objetos que se llaman** («Farola») y **Ocultar**, apaga todas las
  farolas de la escena de una vez.
- **Mientras** repite mientras la condición sea *sí*.

> <i class="fx fx-aviso"></i> **Importante.** Un bucle que no termina nunca
> no cuelga el juego: el motor lo corta y enseña el error «el guion tarda
> demasiado». Para repetir algo a lo largo del tiempo, usa *Cada fotograma*,
> *Cada cierto tiempo* o un *Esperar* dentro del bucle.

### Secuencia

**Secuencia** ejecuta sus salidas una detrás de otra: primero todo lo que
cuelga de *1*, luego lo de *2*, y así. Elige cuántas salidas tiene en sus
ajustes. Sirve para ordenar una cadena larga en ramas que se leen mejor.

### Esperar

**Esperar** detiene **solo esa cadena** durante los segundos indicados y
luego sigue. El resto del juego, y el resto de eventos del mismo grafo,
siguen funcionando mientras tanto.

Ejemplo: una trampa que se activa con retraso.

1. **Al entrar en una zona** → **Decir** («¡Cuidado!») → **Esperar** (2) →
   **Hacer daño** al jugador.

### Solo una vez y Puerta

**Solo una vez** deja pasar la primera ejecución y ninguna más. En un grafo
de objeto, cuenta por separado para cada objeto. Es útil para un mensaje
de bienvenida o un logro.

**Puerta** deja pasar la ejecución mientras está abierta. Tiene dos
entradas de ejecución más, **abrir** y **cerrar**, y en sus ajustes eliges
si empieza abierta.

Ejemplo: como mucho un golpe por segundo. Este patrón aparece en el
[tutorial del enemigo](tutorial-enemigo.md):

1. Lo que da el golpe entra en una **Puerta**.
2. De la puerta sale una **Secuencia** de tres salidas: *1* → **Hacer
   daño**; *2* → la entrada **cerrar** de la misma puerta; *3* →
   **Esperar** (1) → la entrada **abrir** de la puerta.

### Responder y Acabar aquí

**Responder** da la frase de un vecino en *Al hablar con* y termina la
cadena. **Acabar aquí** termina la cadena sin hacer nada más.

## Véase también

- [Nodos](nodos.md)
- [Funciones, bibliotecas y nodos en Lua](nodos-funciones.md)
- [Referencia de nodos](../referencia/nodos.md)
