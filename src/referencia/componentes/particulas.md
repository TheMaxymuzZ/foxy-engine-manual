# Partículas

Suelta partículas sin parar desde el objeto: polvo, chispas, lluvia,
nieve, humo, hojas, fuego, ascuas, una cascada o destellos. Funciona en 2D
y en 3D. Se edita con botones y una vista previa; ver
[Efectos y estilos](../../guia/efectos.md#partículas).

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
| Color al acabar | `color_final` | — | En `#rrggbb`: se van pasando del color al de acabar (el fuego, de amarillo a rojo). Vacío = el de su tipo. |
| Brillo | `brillo` | — | Cuánto brillan (vacío = lo de su tipo; 0 = nada). Las que brillan suman luz y, con **Destello**, dejan halo. |
| Velocidad | `velocidad` | — | Lo rápido que salen (1 = como su tipo). |
| Vida | `vida` | — | Lo que dura cada una (1 = como su tipo). |
| Gravedad | `gravedad` | — | Cuánto tira de ellas hacia abajo (vacío = como su tipo; 0 = flotan; negativo = suben). |
| Crecen | `crece` | — | Cuánto cambian de tamaño hasta que se van (1 = como su tipo). |
| Viento | `viento` | — | Las empuja hacia los lados (x, z). |

<!-- fin -->

| Tipo | En el archivo | Cómo se mueven |
|---|---|---|
| Polvo | `Polvo` | Motas que flotan despacio |
| Chispas | `Chispas` | Saltan hacia arriba y caen, brillando |
| Lluvia | `Lluvia` | Gotas que caen rectas y rápido desde lo alto de la zona |
| Nieve | `Nieve` | Copos que caen despacio, de lado a lado |
| Humo | `Humo` | Sube y se agranda |
| Hojas | `Hojas` | Caen dando vueltas |
| Fuego | `Fuego` | Llamas que suben, tiemblan y pasan de amarillo a rojo |
| Ascuas | `Ascuas` | Puntos encendidos que suben despacio y se apagan |
| Cascada | `Cascada` | Agua que cae desde lo alto de la zona |
| Destellos | `Destellos` | Brillitos que se encienden y se apagan en el sitio |

Si **Encendidas** está desmarcado, las enciende el nodo **Encender
partículas** o `motor.particulas(entidad, true)`. Para soltar unas pocas de
golpe (una explosión, un golpe) usa `motor.soltar_particulas`.

```ron
Particulas((tipo: Humo, cantidad: 6.0, area: (0.5, 0.2), tamano: 3.0))
```

## Véase también

- [Juegos 2D](../../guia/juegos-2d.md#partículas-y-luces)
- [Efectos y estilos](../../guia/efectos.md#partículas)
- [Componentes](index.md)
