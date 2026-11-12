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
| Cristal | `Cristal` | <span class="muestra" style="--c:#96c8de"></span>`#96C8DE` | Transparente |
| Yeso | `Yeso` | <span class="muestra" style="--c:#e8e2d2"></span>`#E8E2D2` | |
| Farol | `Farol` | <span class="muestra" style="--c:#ffe28c"></span>`#FFE28C` | Brilla e ilumina alrededor |

`Aire` es la ausencia de material (quitar bloques deja aire, o agua bajo el
nivel del mar).

## Materiales propios

Además, cada proyecto puede tener hasta **240 materiales propios**, que en
los archivos se escriben `Propio(16)`, `Propio(17)`… hasta `Propio(255)`. Se
crean en la [paleta de materiales](../guia/materiales.md).

## `materiales.ron`

Cambia los del motor y define los propios. Solo se escribe lo que cambia, y
cada valor va dentro de `Some(...)`:

```ron
(
    materiales: {
        Hierba: (textura_lado: Some("hierba_lado")),
        Cristal: (transparencia: Some(0.7), pulido: Some(0.95)),
        Propio(16): (nombre: Some("Oro"), color: Some("#e8b43c"), metalico: Some(1.0), pulido: Some(0.8)),
        Propio(17): (nombre: Some("Neón"), color: Some("#50e6ff"), luz: Some(1.0)),
    },
)
```

| Campo | Valores | Qué es |
|---|---|---|
| `nombre` | texto | Nombre (solo los propios) |
| `color`, `lado` | `"#rrggbb"` | Color de arriba y de los lados |
| `textura`, `textura_lado` | imagen de `imagenes/` | Textura de arriba y de los lados |
| `luz` | 0 a 1 | Luz propia: brilla e ilumina alrededor (hasta ~10 m) |
| `metalico` | 0 a 1 | Refleja el cielo y el sol con su color |
| `pulido` | 0 a 1 | De mate a espejo |
| `transparencia` | 0 a 1 | Se ve a través (como mucho 0,92) |
| `atravesable` | `true` / `false` | No choca al caminar |
| `golpes` | número | Golpes que aguanta (0 = no se rompe) |
| `peso` | kg/m³ | Cuánto pesa |
| `detalle` | `Musgo` o `Raices` | Se dibuja con cubitos finos (ver [Cubitos finos](../guia/efectos-de-material.md#cubitos-finos)) |
| `efecto` | nodos o código | Su efecto (ver [Efectos de material](../guia/efectos-de-material.md)) |
