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
menú con fondo. Cada escena es un archivo de `mundos/` con sus objetos y
los módulos que cambia respecto al proyecto. El suelo de cubitos, si lo
hay, es un objeto más, el [Terreno de cubitos](../guia/generadores.md),
con su generador (vacío, plano, colinas, cuevas, islas o una imagen de
alturas); encima se guardan los cambios hechos con el pincel. Una escena
nueva empieza sin terreno, con una cámara y la luz del sol.

## Objeto

Una **objeto** es cualquier cosa colocada en una escena: una casa, una
puerta, una luz, el personaje del jugador o un punto invisible. Toda objeto
tiene un **nombre**, una **posición** y un **giro**, y puede tener un
**modelo** (un objeto de vóxeles) o ninguno: la *Objeto vacío* no se ve al
jugar y sirve para colgarle componentes.

Las acciones y los guiones se refieren a los objetos **por su nombre**,
por lo que conviene darles nombres claros, como «Puerta del castillo».

## Componente

Un **componente** da a un objeto un comportamiento concreto. Un objeto
sin componentes solo se ve y se choca con ella; con componentes puede
iluminar, sonar, caer con la física, reaccionar cuando el jugador se acerca
o ser el propio jugador.

| Componente | Para qué sirve |
|---|---|
| [Colisión](../referencia/componentes/colision.md) | Decide si el objeto es sólida o se atraviesa |
| [Cuerpo físico](../referencia/componentes/cuerpo-fisico.md) | Cae, bota, rueda y se puede empujar |
| [Controlador de jugador](../referencia/componentes/controlador.md) | El jugador maneja el objeto |
| [Cámara](../referencia/componentes/camara.md) | Cómo se ve el juego |
| [Luz](../referencia/componentes/luz.md) | Ilumina alrededor |
| [Sonido](../referencia/componentes/sonido.md) | Un sonido que sale del objeto |
| [Zona](../referencia/componentes/zona.md) | Hace algo al entrar o salir el jugador |
| [Sprite](../referencia/componentes/sprite.md) | La imagen con la que se ve en 2D |
| [Animador](../referencia/componentes/animador.md) | Sus animaciones y su máquina de estados |
| [Recogible](../referencia/componentes/recogible.md) | Se recoge al tocarlo y suma a un valor |
| [Partículas](../referencia/componentes/particulas.md) | Polvo, chispas, lluvia, humo… |

Cada objeto puede tener **un componente de cada clase**. Se añaden y se
quitan en el [Inspector](../interfaz/inspector.md). Ver
[Objetos y componentes](../guia/entidades.md).

Lo que un objeto **hace** por su cuenta (perseguir, girar, abrirse…) son
sus **comportamientos**: grafos de nodos o guiones Lua, tantos como quieras,
cada uno con sus valores. El motor trae once ya hechos. Ver
[Comportamientos](../guia/comportamientos.md).

## Recurso

Un **recurso** es una pieza reutilizable que se guarda en su propio archivo
y que pueden usar todas las escenas: objetos de vóxeles, materiales,
imágenes, sonidos, interfaces, guiones y objetos reutilizables. Al cambiar un
recurso, cambia en todas partes donde se usa.

## Objeto reutilizable

Un **objeto reutilizable** (antes, *prefabricado*) es un objeto guardado
como recurso, con todo lo que lleva dentro, sus componentes y sus
comportamientos. Se coloca tantas veces como se quiera y **todas las copias
siguen al original**: al cambiar el original, cambian todas. Cada copia puede cambiar por su cuenta algunos
componentes; esos cambios se conservan aunque cambie el original.

Ver [Objetos reutilizables](../guia/reutilizables.md).

## Cómo encaja todo

```text
Proyecto  (proyecto.ron: rejilla, materiales, módulos, acciones de entrada)
├── Recursos  (objetos/, prefabricados/, sonidos/, imagenes/, interfaces/…)
└── Escenas   (mundos/*.ron)
    ├── Cambios del pincel  (cubitos puestos o quitados a mano)
    └── Entidades  (el Terreno de cubitos, la Cámara, el Sol, casas…)
        ├── modelo  (un objeto, o ninguno)
        └── componentes  (Luz, Zona, Controlador…)
```

## Véase también

- [Glosario](../apendices/glosario.md)
- [Referencia de componentes](../referencia/componentes/index.md)
- [Referencia de módulos](../referencia/modulos/index.md)
