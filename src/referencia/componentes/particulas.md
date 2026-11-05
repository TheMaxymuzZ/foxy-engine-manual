# Partículas

Suelta partículas sin parar desde la entidad: polvo, chispas, lluvia,
nieve, humo u hojas. Funciona en 2D y en 3D.

<!-- generado: propiedades -->
<!-- Esta tabla la escribe `foxy-engine --referencia-componentes`. -->

| Propiedad | Campo | De fábrica | Descripción |
|---|---|---|---|
| Tipo | `tipo` | `Polvo` | Qué partículas son. Los tipos se describen más abajo. |
| Por segundo | `cantidad` | 12 | Cuántas salen cada segundo. |
| Color | `color` | — | En `#rrggbb`. Vacío usa el color de su tipo. |
| Zona | `area` | 2 × 1 | Ancho y alto de la zona de donde salen (casillas en 2D, metros en 3D). |
| Tamaño | `tamano` | 2 | Tamaño de cada partícula (píxeles en 2D, centímetros en 3D). |
| Encendidas | `encendidas` | Sí | Salen desde el principio. |

<!-- fin -->

| Tipo | En el archivo | Cómo se mueven |
|---|---|---|
| Polvo | `Polvo` | Motas que flotan despacio |
| Chispas | `Chispas` | Saltan hacia arriba y caen, brillando |
| Lluvia | `Lluvia` | Gotas que caen rectas y rápido desde lo alto de la zona |
| Nieve | `Nieve` | Copos que caen despacio, de lado a lado |
| Humo | `Humo` | Sube y se agranda |
| Hojas | `Hojas` | Caen dando vueltas |

Si **Encendidas** está desmarcado, las enciende el nodo **Encender
partículas** o `motor.particulas(entidad, true)`. Para soltar unas pocas de
golpe (una explosión, un golpe) usa `motor.soltar_particulas`.

```ron
Particulas((tipo: Humo, cantidad: 6.0, area: (0.5, 0.2), tamano: 3.0))
```

## Véase también

- [Juegos 2D](../../guia/juegos-2d.md#partículas-y-luces)
- [Componentes](index.md)
