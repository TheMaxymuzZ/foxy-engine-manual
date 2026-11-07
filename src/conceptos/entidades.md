# Entidades, componentes y prefabricados

Todo lo que hay en una escena es una **entidad**, y lo que una entidad hace
lo deciden sus **componentes**. Este modelo es el mismo en 3D y en 2D, y es
la base de todo lo demás: los nodos, los guiones y las animaciones actúan
siempre sobre entidades.

## Entidad

Una entidad es una cosa colocada en una escena: una casa, una moneda, la
cámara, una luz, el jugador o un punto invisible. Toda entidad tiene:

| Dato | Para qué |
|---|---|
| **Nombre** | Identificarla. Las acciones, los nodos y los guiones se refieren a ella por su nombre |
| **Posición** y **giro** | Dónde está. En 3D, en metros; en 2D, en casillas |
| **Modelo** | Cómo se ve: un objeto de cubitos en 3D o un sprite en 2D. La **Objeto vacío** no tiene modelo y no se ve al jugar |
| **Comportamientos** | Lo que hace por su cuenta: grafos de nodos o guiones, tantos como quiera. Ver [Comportamientos](../guia/comportamientos.md) |
| **Componentes** | Qué es: luz, sonido, física, zona… |
| **Al usarlo (E)** | La acción que se ejecuta cuando el jugador la usa |

> <i class="fx fx-consejo"></i> **Consejo.** Da a las entidades nombres
> claros y únicos, como «Puerta del castillo». Un nombre repetido hace que
> una acción o un guion actúe sobre la primera que encuentre.

## Componente

Un componente es una pieza de comportamiento con sus propios valores. Una
entidad puede tener **un componente de cada clase**, y las clases se
combinan libremente:

| Se quiere | Componentes |
|---|---|
| Una farola que alumbra de noche | Luz |
| Una caja que cae y se empuja | Cuerpo físico |
| Una moneda | Sprite (en 2D) y Recogible |
| Una puerta que se abre al acercarse | Zona (con la acción **Mover una entidad**) |
| El jugador en tercera persona | Controlador de jugador y Cámara |
| Un personaje que anda y salta | Controlador de jugador y Animador |

Para que haga algo más (perseguir al jugador, flotar, abrirse con un
botón…), dale un [comportamiento](../guia/comportamientos.md).

La lista completa, con todas sus propiedades y valores de fábrica, está en
la [Referencia de componentes](../referencia/componentes/index.md).

## Prefabricado

Un prefabricado es una entidad guardada como **recurso**, con su modelo, sus
componentes y su acción al usarla. Se coloca tantas veces como haga falta y
**todas las copias siguen al original**:

- Al cambiar el prefabricado, cambian todas las copias.
- Cada copia puede cambiar algunos valores por su cuenta; esos cambios se
  conservan aunque cambie el original. El Inspector los marca como
  *cambiado aquí*.

Los prefabricados se guardan en `prefabricados/`. Se crean con el botón
**Crear prefabricado** del Inspector. Ver
[Prefabricados](../guia/entidades.md#prefabricados).

## Módulos

Algunos comportamientos no son de una entidad sino de toda la escena: el
paso del día y la noche, el clima, los vecinos, romper bloques. Son los
**módulos**. Cada proyecto elige los que usa y cada escena puede activarlos
o desactivarlos para ella. Ver la [referencia de módulos](../referencia/modulos/index.md).

## Véase también

- [Entidades y componentes](../guia/entidades.md): la guía práctica.
- [Inspector](../interfaz/inspector.md): donde se editan.
- [Lógica del juego](logica.md): cómo dar comportamiento a las entidades.
