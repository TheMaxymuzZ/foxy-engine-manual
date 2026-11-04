# Depurar y pasar a código

Cuando un grafo no hace lo que esperas, el editor te deja verlo funcionar
por dentro mientras juegas: qué cables se encienden, qué valor lleva cada
uno y dónde se detiene la ejecución. Esta página explica esas herramientas
y cómo leer o conservar el Lua que sale de los nodos.

![Un grafo depurándose: los nodos por los que pasa la ejecución se encienden y cada salida enseña su último valor](../imagenes/capturas/nodos-depurar.png)

## Ver el grafo mientras juegas

1. Abre en el panel Nodos el grafo que quieres observar.
2. Pulsa <i class="fx fx-jugar"></i> **Jugar aquí** o **Desde el inicio**.
3. Pulsa <kbd>F8</kbd>. Aparece una ventana con el grafo encima del juego.
   Pulsa <kbd>F8</kbd> otra vez para ocultarla.

En esa ventana:

- Los **cables de ejecución** y los **nodos** por los que acaba de pasar la
  ejecución se iluminan en naranja y se apagan poco a poco. En un evento
  como *Cada fotograma*, el camino que se toma en cada momento queda siempre
  encendido.
- Cada **salida de datos** enseña, en una etiqueta de su color, el último
  valor que ha salido por ella.

Si un grafo de entidad lo llevan varias entidades, la ventana junta lo que
hacen todas.

## Puntos de parada

Un **punto de parada** detiene el juego justo antes de ejecutar un nodo,
para que puedas mirar los valores con calma.

1. Elige el nodo y pulsa <kbd>F9</kbd>. También puedes marcar
   **Punto de parada** en sus ajustes o en su menú de clic derecho. El nodo
   queda marcado con un punto rojo.
2. Juega. Cuando la ejecución llega a ese nodo, el juego se congela, el
   ratón queda libre y la ventana del grafo se abre sola con el nodo
   resaltado.
3. Pulsa <kbd>F6</kbd> para seguir.

Los puntos de parada solo funcionan en el grafo abierto en el panel y solo
al jugar desde el editor. No se guardan con el proyecto.

> <i class="fx fx-consejo"></i> **Consejo.** Para saber si una rama se
> ejecuta, pon un *Escribir en la consola* con un texto en ella: lo verás en
> el [Registro](../interfaz/registro.md) cada vez que pase.

## Errores

Un error en un grafo no cierra el juego. Aparece abajo en la pantalla y en
el [Registro](../interfaz/registro.md), con el nombre del grafo. Los más
habituales:

| Mensaje | Qué significa |
|---|---|
| «el guion tarda demasiado» | Un *Mientras* o un *Repetir* que nunca termina. Revisa su condición |
| «grafos/….nodos.ron: no se pudo leer» | El componente *Grafo de nodos* apunta a un archivo que ya no existe |

En el lienzo, un nodo que llama a una función borrada o renombrada se
titula *Función «…» (no existe)* y aparece apagado. Vuelve a elegir la
función o borra el nodo.

## Ver el Lua

Activa **Ver el Lua** en la barra del panel. A la derecha aparece el código
que el motor genera a partir del grafo, y se actualiza al momento con cada
cambio. Es una buena forma de aprender Lua: cada nodo se convierte en una
o dos líneas reconocibles, como `motor.decir("Hola")`.

## Pasar a código

Si un grafo del juego ha crecido tanto que prefieres seguir escribiéndolo a
mano, pulsa **Pasar a código**:

1. El código del grafo se añade al final de `guiones/mundo.lua`, con un
   comentario que indica de dónde viene.
2. El grafo se vacía (las variables se conservan) y se abre el panel
   [Código](../interfaz/codigo.md).

El resultado funciona igual que antes. **Pasar a código** solo está en el
grafo del juego; para los demás grafos, usa **Ver el Lua** y copia lo que
necesites.

## Véase también

- [Nodos](nodos.md)
- [Guiones en Lua](guiones.md)
- [Probar el juego](jugar.md)
