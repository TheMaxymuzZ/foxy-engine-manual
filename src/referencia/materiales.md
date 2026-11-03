# Materiales

Los materiales con los que se construye el mundo. El **nombre en el archivo**
es el que se usa en los `.ron` (en `cambios`, `cubitos` y `materiales.ron`).

| Material | En el archivo | Color | Notas |
|---|---|---|---|
| Hierba | `Hierba` | <span class="muestra" style="--c:#68a83e"></span>`#68A83E` | Los lados enseñan algo más oscuro (`#5C8C3A`). Cambia con las estaciones |
| Tierra | `Tierra` | <span class="muestra" style="--c:#7e5838"></span>`#7E5838` | |
| Piedra | `Piedra` | <span class="muestra" style="--c:#808084"></span>`#808084` | |
| Arena | `Arena` | <span class="muestra" style="--c:#e2cc92"></span>`#E2CC92` | |
| Agua | `Agua` | <span class="muestra" style="--c:#2670a0"></span>`#2670A0` | No es sólida: se nada en ella |
| Tronco | `Tronco` | <span class="muestra" style="--c:#68482c"></span>`#68482C` | |
| Hojas | `Hojas` | <span class="muestra" style="--c:#408434"></span>`#408434` | Cambian con las estaciones |
| Madera | `Madera` | <span class="muestra" style="--c:#b0804e"></span>`#B0804E` | |
| Flor roja | `FlorRoja` | <span class="muestra" style="--c:#d63a3a"></span>`#D63A3A` | Se atraviesa al andar |
| Flor amarilla | `FlorAmarilla` | <span class="muestra" style="--c:#f0cc3c"></span>`#F0CC3C` | Se atraviesa al andar |
| Grava | `Grava` | <span class="muestra" style="--c:#706a64"></span>`#706A64` | |
| Teja | `Teja` | <span class="muestra" style="--c:#b24a34"></span>`#B24A34` | |
| Cristal | `Cristal` | <span class="muestra" style="--c:#96c8de"></span>`#96C8DE` | |
| Yeso | `Yeso` | <span class="muestra" style="--c:#e8e2d2"></span>`#E8E2D2` | |
| Farol | `Farol` | <span class="muestra" style="--c:#ffe28c"></span>`#FFE28C` | |

`Aire` es la ausencia de material (quitar bloques deja aire, o agua bajo el
nivel del mar).

Cada proyecto puede cambiar el color de cualquier material y ponerle una
textura en [Pixel art](../guia/pixel-art.md#texturas-para-los-materiales);
se guarda en [`materiales.ron`](archivos.md#materiales).
