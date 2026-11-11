# Luz

Ilumina alrededor de la entidad, de día y de noche.

<!-- generado: propiedades -->
<!-- Esta tabla la escribe `foxy-engine --referencia-componentes`. -->

| Propiedad | Campo | De fábrica | Descripción |
|---|---|---|---|
| Color | `color` | `"#ffd27a"` | Color de la luz, en `#rrggbb`. |
| Intensidad | `intensidad` | 1 | De 0 a 4. |
| Alcance | `alcance` | 8 m | Distancia hasta la que ilumina. En 2D se mide en casillas. |
| Altura | `altura` | 1 m | Altura de la luz sobre la base del objeto. |
| Sombras | `sombras` | — | Hace sombras de verdad (en 3D). Cuántas luces las hacen a la vez depende de la calidad. |

<!-- fin -->

Las luces se ven en el editor y al jugar. En una
[escena 2D](../../guia/juegos-2d.md#partículas-y-luces) se notan cuando la
luz ambiente está por debajo de 1, y el alcance va en casillas. Los materiales con luz propia,
como el farol, siguen iluminando sin necesidad de este componente.

Con **Sombras** marcado, la luz proyecta las sombras de lo que tiene
alrededor, como una antorcha en una cueva. Cuántas luces hacen sombra a la
vez depende de la [calidad](../../guia/graficos.md#calidad).

```ron
Luz((color: "#80c0ff", intensidad: 2.0, alcance: 12.0, altura: 3.0))
Luz((color: "#ff9a3c", intensidad: 3.0, alcance: 12.0, altura: 1.7, sombras: true))
```

## Véase también

- [Componentes](index.md)
- [Gráficos: luz, sombras y calidad](../../guia/graficos.md)
- [Entidades y componentes](../../guia/entidades.md)
