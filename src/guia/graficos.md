# Gráficos: luz, sombras y calidad

Foxy Engine dibuja con **luz de verdad**: el sol, una antorcha o la lava
pueden dar mucha más luz que el blanco de la pantalla, como en la vida real.
Luego, igual que una cámara, el motor decide cuánta luz deja pasar (la
**exposición**) y cómo la convierte en colores (el **tono**).

Nada viene preparado para un estilo: un proyecto nuevo se ve como siempre, y
tú cambias solo lo que quieras. Pero conseguir algo realista es fácil, porque
los materiales y las luces funcionan como en Blender.

![Una cueva iluminada solo con antorchas que hacen sombra](../imagenes/capturas/cueva-antorchas.png)

## Dónde se cambia cada cosa

| Qué | Dónde | Para quién |
|---|---|---|
| Exposición, tono y piezas del dibujo | **Proyecto → Ajustes del proyecto → Gráficos** | Todo el juego |
| Calidad con la que empieza el juego | **Ajustes del proyecto → Gráficos** | Los jugadores, al abrirlo por primera vez |
| Calidad del juego de cada jugador | **Opciones → Gráficos**, dentro del juego | Ese jugador |
| Calidad en el editor y el dibujante | **Editar → Preferencias** | Tu ordenador |

Los cambios en los ajustes del proyecto se ven **al momento** en la escena,
antes de pulsar **Guardar**.

![La página Gráficos de los ajustes del proyecto](../imagenes/capturas/panel-ajustes-graficos.png)

## Exposición

Más luz (+) o menos (−), en pasos de cámara: **+1** es el doble de luz y
**−1** la mitad. Va de −4 a +4. Úsala cuando la escena entera se vea oscura
(una cueva, una noche) o quemada (un desierto a mediodía).

## Tono

El tono pasa la luz, que puede ser muy fuerte, a los colores que la pantalla
sabe mostrar.

| Tono | Cómo se ve |
|---|---|
| **Cine (ACES)** | El de siempre: contraste y colores vivos, como en el cine. Viene puesto |
| **Como Blender (AgX)** | Igual que el que usa Blender. Elígelo si haces los modelos en Blender y quieres que se vean exactamente igual |
| **Neutro** | Respeta los colores tal cual (bueno para productos o arte con colores exactos) |
| **Ninguno** | Sin curva: lo que pasa de blanco se corta |

| Cine (ACES) | Como Blender (AgX) |
|---|---|
| ![La isla con el tono Cine](../imagenes/capturas/tono-cine.png) | ![La isla con el tono Como Blender](../imagenes/capturas/tono-blender.png) |
| **Neutro** | **Ninguno** |
| ![La isla con el tono Neutro](../imagenes/capturas/tono-neutro.png) | ![La isla con el tono Ninguno](../imagenes/capturas/tono-ninguno.png) |

## Calidad

Cinco niveles. Cuanto más alto, más bonito y más trabajo para el ordenador.

| Calidad | Sombras | Luces a la vez | Luces con sombra |
|---|---|---|---|
| **Bajo** | Sencillas | 64 | Ninguna |
| **Medio** | Normales | 256 | 2 |
| **Alto** | Finas (viene puesta) | 1.024 | 4 |
| **Ultra** | Muy finas | 1.024 | 8 |
| **Cine** | Las mejores, para capturas y vídeos | 1.024 | 16 |

Cuando hay más luces con sombra de las que permite la calidad, hacen sombra
las más cercanas a la cámara; las demás siguen iluminando.

![La calidad en el menú Opciones del juego](../imagenes/capturas/juego-opciones-graficos.png)

## Luces y sombras

Un objeto con el componente [Luz](../referencia/componentes/luz.md) ilumina
alrededor. Marca su casilla **Sombras** en el inspector y además **hace
sombras**: una antorcha en una cueva dibuja la sombra de cada columna y
cada roca. Pueden encenderse **cientos de luces** a la vez sin que el juego
vaya más lento.

> <i class="fx fx-consejo"></i> **Consejo.** Las sombras de las luces cuestan
> más que la luz sola. Ponlas en las luces que importan (la antorcha del
> jugador, la lámpara de una sala) y deja sin sombra las de adorno.

## Materiales de los modelos (PBR)

Los modelos glTF que hagas en Blender se ven con **todo su material**:
color, relieve (mapa de normales), rugosidad, metal, oclusión (los rincones
más oscuros) y brillo. Lo que brilla con fuerza, como la lava, **ilumina lo
que tiene alrededor**. Ver
[Modelos 3D](modelos-3d.md#materiales-y-texturas).

![Una losa de lava con relieve que brilla e ilumina la esfera de al lado](../imagenes/capturas/modelos-pbr.png)

## Piezas del dibujo

Cada parte del dibujo se puede apagar: **Sombras del sol**, **Sombras de las
luces**, **Luces**, **Cielo y nubes**, **Niebla**, **Agua** y
**Transparentes**. Apagar una pieza no rompe nada: solo deja de dibujarse.
Sirve para juegos con un estilo propio (sin niebla, sin agua) o para ver qué
es lo que más cuesta en un ordenador lento.

**Volver a como venía** deja toda la página como al principio.

## El dibujante clásico

En **Editar → Preferencias → Dibujante** puedes elegir el **Clásico**, el
que tenía el motor antes. No tiene exposición, tono, materiales completos ni
luces con sombra. Úsalo solo si el nuevo da problemas en tu ordenador, y
cuéntalo para que se pueda arreglar.

## Véase también

- [Ajustes del proyecto](../editor/ajustes-proyecto.md#gráficos)
- [Preferencias](preferencias.md#gráficos)
- [Rendimiento](rendimiento.md)
- [Luz](../referencia/componentes/luz.md)
