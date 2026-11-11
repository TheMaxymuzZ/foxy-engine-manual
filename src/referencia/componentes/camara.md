# Cámara

Cambia cómo se ve el juego.

<!-- generado: propiedades -->
<!-- Esta tabla la escribe `foxy-engine --referencia-componentes`. -->

| Propiedad | Campo | De fábrica | Descripción |
|---|---|---|---|
| Distancia | `distancia` | 4,5 m | Distancia por detrás del personaje. |
| Altura | `altura` | 1,8 m | Altura sobre los pies del personaje. |
| Campo de visión | `campo_de_vision` | 0° | Apertura de la cámara. 0 usa la de las opciones del juego. |
| Fija | `fija` | No | El juego se ve desde este objeto, mirando al jugador. |
| Ortográfica | `ortografica` | No | Sin perspectiva: lo lejano se ve igual de grande. Indicada para cubitos vistos de lado o desde arriba. |
| Alto visible | `alto_visible` | 14 m | Con **Ortográfica**, cuántos metros de alto se ven. |
| Suavizado (2D) | `suavizado` | 0,15 | En 2D: 0 deja la cámara pegada al jugador; valores mayores lo siguen con más calma. |

<!-- fin -->

- En la entidad con [Controlador de jugador](controlador.md), ajusta la
  cámara de ese personaje.
- En otra entidad con **Fija** marcada, el juego se ve desde ella, como una
  cámara de seguridad. *Adelante* se interpreta entonces como «alejarse de
  la cámara».

```ron
Camara((distancia: 6.0, altura: 2.5))
```

## Véase también

- [Componentes](index.md)
- [Entidades y componentes](../../guia/entidades.md)
