# Conceptos básicos

Foxy Engine organiza un juego con seis ideas. Conocerlas permite entender
cualquier parte del editor y de los archivos del proyecto.

## Proyecto

Un **proyecto** es un juego: una carpeta con un archivo `proyecto.ron` y
todo lo que el juego necesita. Define los ajustes comunes a todas las
escenas: la escena inicial, el tamaño del cubito de la rejilla, los
materiales, los [módulos](../referencia/modulos/index.md) que usa y el
[mapa de acciones de entrada](../guia/acciones-entrada.md).

Ver [Proyectos, escenas y recursos](proyectos.md).

## Escena

Una **escena** es un lugar del juego: un nivel, una casa por dentro, un
menú con fondo. Cada escena es un archivo de `mundos/` con su terreno, sus
entidades y los módulos que cambia respecto al proyecto. El terreno lo
crea un [generador](../guia/generadores.md) (vacío, plano, isla, colinas o
cuevas) y encima se guardan los cambios hechos con el pincel.

## Entidad

Una **entidad** es cualquier cosa colocada en una escena: una casa, una
puerta, una luz, el personaje del jugador o un punto invisible. Toda entidad
tiene un **nombre**, una **posición** y un **giro**, y puede tener un
**modelo** (un objeto de vóxeles) o ninguno: la *Entidad vacía* no se ve al
jugar y sirve para colgarle componentes.

Las acciones y los guiones se refieren a las entidades **por su nombre**,
por lo que conviene darles nombres claros, como «Puerta del castillo».

## Componente

Un **componente** da a una entidad un comportamiento concreto. Una entidad
sin componentes solo se ve y se choca con ella; con componentes puede
iluminar, sonar, caer con la física, reaccionar cuando el jugador se acerca
o ser el propio jugador.

| Componente | Para qué sirve |
|---|---|
| [Colisión](../referencia/componentes/colision.md) | Decide si la entidad es sólida o se atraviesa |
| [Cuerpo físico](../referencia/componentes/cuerpo-fisico.md) | Cae, bota, rueda y se puede empujar |
| [Controlador de jugador](../referencia/componentes/controlador.md) | El jugador maneja la entidad |
| [Cámara](../referencia/componentes/camara.md) | Cómo se ve el juego |
| [Luz](../referencia/componentes/luz.md) | Ilumina alrededor |
| [Sonido](../referencia/componentes/sonido.md) | Un sonido que sale de la entidad |
| [Zona](../referencia/componentes/zona.md) | Hace algo al entrar o salir el jugador |
| [Guion](../referencia/componentes/guion.md) | Llama a funciones del guion |
| [Sprite](../referencia/componentes/sprite.md), [Animador](../referencia/componentes/animador.md), [Grafo de nodos](../referencia/componentes/grafo-de-nodos.md) | Preparados para próximas versiones |

Cada entidad puede tener **un componente de cada clase**. Se añaden y se
quitan en el [Inspector](../interfaz/inspector.md). Ver
[Entidades y componentes](../guia/entidades.md).

## Recurso

Un **recurso** es una pieza reutilizable que se guarda en su propio archivo
y que pueden usar todas las escenas: objetos de vóxeles, materiales,
imágenes, sonidos, interfaces, guiones y prefabricados. Al cambiar un
recurso, cambia en todas partes donde se usa.

## Prefabricado

Un **prefabricado** es una entidad guardada como recurso, con su modelo,
sus componentes y su acción al usarla. Se coloca tantas veces como se
quiera y **todas las copias siguen al original**: al cambiar el
prefabricado, cambian todas. Cada copia puede cambiar por su cuenta algunos
componentes; esos cambios se conservan aunque cambie el original.

Ver [Prefabricados](../guia/entidades.md#prefabricados).

## Cómo encaja todo

```text
Proyecto  (proyecto.ron: rejilla, materiales, módulos, acciones de entrada)
├── Recursos  (objetos/, prefabricados/, sonidos/, imagenes/, interfaces/…)
└── Escenas   (mundos/*.ron)
    ├── Terreno  (generador + cambios del pincel)
    └── Entidades
        ├── modelo  (un objeto, o ninguno)
        └── componentes  (Luz, Zona, Controlador…)
```

## Véase también

- [Glosario](../apendices/glosario.md)
- [Referencia de componentes](../referencia/componentes/index.md)
- [Referencia de módulos](../referencia/modulos/index.md)
