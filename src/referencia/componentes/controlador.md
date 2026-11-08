# Controlador de jugador

El jugador maneja esta entidad. La partida empieza en ella, en lugar de en
el *Punto de inicio*.

<!-- generado: propiedades -->
<!-- Esta tabla la escribe `foxy-engine --referencia-componentes`. -->

| Propiedad | Campo | De fábrica | Descripción |
|---|---|---|---|
| Tipo | `tipo` | `PrimeraPersona` | Cómo se maneja y desde dónde se ve. Los tipos se describen más abajo. |
| Andando | `velocidad` | 4,5 m/s | Velocidad al caminar. |
| Corriendo | `carrera` | 8 m/s | Velocidad con **Correr**. |
| Salto | `salto` | 1,33 m | Altura del salto. 0 desactiva el salto. |
| Gravedad | `gravedad` | 24 m/s² | Aceleración de caída. La de la Tierra es 9,8. |
| Coyote time | `coyote` | 0,1 s | En 2D: tiempo para saltar después de salir de un borde. |
| Salto variable | `salto_variable` | Sí | En 2D: soltar **Saltar** pronto hace el salto más bajo. |

<!-- fin -->

En una [escena 2D](../../guia/juegos-2d.md) las medidas van en casillas
(casillas por segundo, casillas de salto).

## Tipos

| Tipo | En el archivo | Descripción |
|---|---|---|
| Primera persona | `PrimeraPersona` | Se ve con los ojos del personaje. El ratón mueve la mirada |
| Tercera persona | `TerceraPersona` | La cámara va detrás del personaje, que se ve entero. Si una pared se interpone, la cámara se acerca |
| Cenital | `Cenital` | Desde arriba. La cámara no gira; *Adelante* es hacia el norte. En 2D, anda en las cuatro direcciones sin gravedad |
| Isométrico | `Isometrico` | En diagonal desde arriba, como un diorama |
| Plataformas 2D | `Plataformas2D` | De lado. El personaje solo se mueve a izquierda y derecha, salta, trepa y nada |
| Cámara libre | `CamaraLibre` | Vuela y atraviesa todo. Útil para recorrer la escena |

En los tipos en los que se ve el personaje, se usa el modelo de la entidad;
una *Objeto vacío* se muestra con la figura de un vecino.

Si hay varias entidades con controlador, se usa la primera de la lista
**En la escena**. La distancia y la altura de la cámara se ajustan con el
componente [Cámara](camara.md).

```ron
Controlador((tipo: TerceraPersona, velocidad: 5.0, salto: 1.5))
```

## Véase también

- [Componentes](index.md)
- [Entidades y componentes](../../guia/entidades.md)
