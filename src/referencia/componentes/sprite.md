# Sprite

La imagen con la que se ve una entidad 2D, de la carpeta `imagenes/`. Si la
imagen es una [hoja de sprites](../../guia/sprites.md), puede llevar una
animación.

| Propiedad | Campo | De fábrica | Descripción |
|---|---|---|---|
| Imagen | `imagen` | — | Imagen de `imagenes/`, sin `.png` |
| Animación | `animacion` | (ninguna) | La animación de la hoja con la que empieza |
| Fotograma | `fotograma` | 0 | El fotograma fijo, desde 0, si no hay animación |
| Espejo | `espejo` | No | Dado la vuelta, mirando a la izquierda |
| Orden | `orden` | 0 | Entre entidades, los números altos se dibujan delante |
| Tinte | `color` | (ninguno) | Un color que tiñe la imagen, `"#rrggbb"` |
| Tamaño | `tamano` | 0 | Solo en 3D: alto en metros (0 = el de sus píxeles) |

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
