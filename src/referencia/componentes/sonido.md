# Sonido

Un sonido que sale de la entidad. Se oye más fuerte cuanto más cerca está el
jugador.

<!-- generado: propiedades -->
<!-- Esta tabla la escribe `foxy-engine --referencia-componentes`. -->

| Propiedad | Campo | De fábrica | Descripción |
|---|---|---|---|
| Sonido | `sonido` | — | Un sonido de `sonidos/` (sin extensión) o uno de ejemplo. |
| Volumen | `volumen` | 1 | De 0 a 2. |
| Se oye hasta | `distancia` | 15 m | Más allá no se oye. 0 hace que se oiga igual en todas partes. |
| En bucle | `bucle` | Sí | Vuelve a empezar al terminar. |
| Al empezar | `al_empezar` | Sí | Empieza a sonar con la partida. Si no, lo hace sonar la acción **Tocar un sonido** o un guion. |

<!-- fin -->

Ver [Sonidos](../../guia/sonidos.md) para añadir archivos WAV u OGG.

```ron
Sonido((sonido: "rio", volumen: 0.8, distancia: 20.0))
```

## Véase también

- [Componentes](index.md)
- [Entidades y componentes](../../guia/entidades.md)
