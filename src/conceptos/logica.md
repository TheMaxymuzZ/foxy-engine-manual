# Lógica del juego: acciones, nodos y Lua

Foxy Engine ofrece tres maneras de decir qué pasa en el juego, de la más
sencilla a la más potente. Se pueden mezclar en un mismo proyecto e incluso
en una misma entidad.

| | Acciones | Nodos | Lua |
|---|---|---|---|
| **Qué es** | Una respuesta elegida de una lista | Un grafo de cajas unidas por cables | Código en el lenguaje Lua |
| **Dónde** | En componentes (Zona), botones de interfaces y **Al usarlo (E)** | Panel [Nodos](../interfaz/nodos.md) | Panel [Código](../interfaz/codigo.md) o un editor externo |
| **Para** | Abrir una puerta, ir a otra escena, abrir un menú | Comportamientos completos sin escribir código | Sistemas complejos y control total |
| **Hace falta saber programar** | No | No | Sí |

## Acciones

Una acción es algo que pasa en respuesta a un suceso: el jugador entra en
una zona, pulsa un botón o usa un objeto. Se elige de una lista, como **Ir a
otra escena**, **Abrir una interfaz**, **Mover una entidad** o **Tocar un
sonido**. La lista completa está en [Acciones](../referencia/acciones.md).

## Nodos

Un grafo de nodos describe un comportamiento con cajas: los **eventos**
(*Al empezar*, *Cada fotograma*, *Al entrar en una zona*) dan la salida, y
los cables llevan el flujo por **condiciones**, **bucles** y **acciones**.
Los datos tienen tipo (número, texto, vector, entidad) y se ven en el color
de cada cable. Un grafo puede ser del juego, de una escena o de una entidad,
y se puede **depurar en vivo** viendo qué cables se encienden.

Todo nodo es una función de la API de Lua, así que un grafo se puede pasar a
código en cualquier momento. Ver [Nodos](../guia/nodos.md).

## Lua

Lua es un lenguaje de programación sencillo y muy usado en videojuegos. Los
guiones Lua tienen acceso a la misma API que los nodos (`motor.*`), con
autocompletado, recarga en caliente, consola y depurador con puntos de
parada. Hay dos clases de guion:

- El **guion del mundo** (`guiones/mundo.lua`): las reglas generales del
  juego.
- Los **guiones de entidad**: el comportamiento de una entidad, con
  propiedades que se ajustan en el Inspector para cada copia.

Ver [Programar en Lua](../guia/programar-lua.md).

## Qué elegir

- Empieza con **acciones**: resuelven la mayoría de las interacciones de un
  nivel.
- Pasa a **nodos** cuando una entidad tenga que decidir algo (perseguir al
  jugador, contar, esperar).
- Usa **Lua** para sistemas grandes (inventarios, diálogos, inteligencia
  artificial) o si ya sabes programar.

## Véase también

- [Tutorial: un enemigo que persigue](../guia/tutorial-enemigo.md), con
  nodos, y [el mismo enemigo en Lua](../guia/tutorial-enemigo-lua.md).
- [Referencia de nodos](../referencia/nodos.md) y
  [Referencia de la API de Lua](../referencia/api-lua.md).
