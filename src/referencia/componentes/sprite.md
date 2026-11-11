# Sprite

La imagen con la que se ve una entidad 2D, de la carpeta `imagenes/`. Si la
imagen es una [hoja de sprites](../../guia/sprites.md), puede llevar una
animación.

<!-- generado: propiedades -->
<!-- Esta tabla la escribe `foxy-engine --referencia-componentes`. -->

| Propiedad | Campo | De fábrica | Descripción |
|---|---|---|---|
| Imagen | `imagen` | — | Imagen de `imagenes/`, sin `.png`. |
| Tamaño | `tamano` | 0 m | Solo en 3D: alto en metros. 0 usa el tamaño de sus píxeles. |
| Fotograma | `fotograma` | 0 | El fotograma fijo, contando desde 0, si no hay animación. |
| Animación | `animacion` | — | La animación de la hoja con la que empieza. |
| Espejo | `espejo` | No | Dibuja la imagen volteada, mirando a la izquierda. |
| Orden | `orden` | 0 | Entre objetos, los números altos se dibujan delante. |
| Tinte | `color` | — | Color que tiñe la imagen, en `#rrggbb`. Vacío no tiñe. |

<!-- fin -->

En una escena 2D, cada píxel del sprite mide lo mismo que un píxel de las
casillas. El sprite del jugador cambia de animación solo (ver
[Juegos 2D](../../guia/juegos-2d.md#animaciones-del-jugador)).

```ron
Sprite((imagen: "zorro", animacion: "quieto"))
```

## Véase también

- [Sprites](../../guia/sprites.md)
- [Juegos 2D](../../guia/juegos-2d.md)
- [Componentes](index.md)
