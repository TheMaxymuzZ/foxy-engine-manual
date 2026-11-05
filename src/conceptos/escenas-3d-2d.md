# Escenas 3D y 2D

Un proyecto de Foxy Engine puede tener escenas **3D**, hechas de cubitos, y
escenas **2D**, hechas de casillas y sprites. Las dos comparten entidades,
componentes, interfaces, sonidos, nodos y guiones; cambia cómo se construye
y cómo se ve el mundo.

| | Escena 3D | Escena 2D |
|---|---|---|
| **Terreno** | Cubitos de 0,5 m, generados o construidos con pinceles | Capas de casillas pintadas con un juego de casillas |
| **Unidad** | Metros | Casillas (16 píxeles de fábrica) |
| **Cómo se ven las entidades** | Un objeto de cubitos | Un sprite |
| **Cámara** | Con perspectiva, u ortográfica para vistas de lado o desde arriba | *Pixel perfect*: cada píxel del juego ocupa un número entero de píxeles de la pantalla |
| **Espacio de trabajo** | **Construir** | **2D** |
| **Física** | Bloques sólidos, cuerpos que caen y ruedan | Casillas sólidas, plataformas, escaleras, agua y peligro |

## Tres maneras de hacer un juego 2D

| Estilo | Cómo | Plantilla |
|---|---|---|
| **Pixel art de lado** | Escena 2D con el controlador **Plataformas 2D** | Plataformas 2D |
| **Pixel art desde arriba** | Escena 2D con el controlador **Cenital** | Aventura cenital |
| **Cubitos de lado** | Escena 3D con la cámara **Ortográfica** y el controlador **Plataformas 2D** | Plataformas vóxel |

## Unidades

- **Cubito**: el vóxel del terreno, de 0,5 m de lado de fábrica. El tamaño
  se cambia por proyecto en [Ajustes del proyecto](../editor/ajustes-proyecto.md).
- **Bloque**: 2 × 2 × 2 cubitos, es decir, 1 m. Es la medida de las
  texturas y de los pinceles de tamaño 2.
- **Casilla**: la unidad de las escenas 2D. Su tamaño en píxeles se elige en
  el panel [Capas](../interfaz/capas.md).

## Véase también

- [Mundos vóxel](../guia/mundo.md)
- [Juegos 2D](../guia/juegos-2d.md)
- [Escenas](../guia/escenas.md): conectar escenas entre sí.
