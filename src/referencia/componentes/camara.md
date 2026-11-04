# Cámara

Cambia cómo se ve el juego.

| Propiedad | Campo | De fábrica | Descripción |
|---|---|---|---|
| Distancia | `distancia` | 4,5 m | Metros por detrás del personaje |
| Altura | `altura` | 1,8 m | Metros por encima de los pies |
| Campo de visión | `campo_de_vision` | 0 | En grados. 0 = el de las opciones del juego |
| Fija | `fija` | No | El juego se ve desde esta entidad, mirando al jugador |
| Ortográfica | `ortografica` | No | Sin perspectiva: lo lejano se ve igual de grande. Para cubitos vistos de lado o desde arriba |
| Alto visible | `alto_visible` | 14 m | Con **Ortográfica**, cuántos metros de alto se ven |
| Suavizado (2D) | `suavizado` | 0,15 | En 2D: 0 = la cámara va pegada al jugador; más, lo sigue con más calma |

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
