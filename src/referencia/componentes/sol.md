# Luz del sol

La luz de la escena: a qué hora está el sol (y por tanto desde dónde llega
la luz), cuánto ilumina y de qué color. Una escena nueva vacía la trae en el
objeto **Sol**. Si hay varias, manda la primera.

<!-- generado: propiedades -->
<!-- Esta tabla la escribe `foxy-engine --referencia-componentes`. -->

| Propiedad | Campo | De fábrica | Descripción |
|---|---|---|---|
| Hora | `hora` | 11 h | Dónde está el sol: 6 amanece, 12 arriba del todo, 18 se pone. Con **Día y noche**, la partida empieza a esta hora. |
| Intensidad | `intensidad` | 1 | De 0 (apagado) a 2 (el doble de luz). |
| Color | `color` | `"#ffffff"` | Color de la luz, `#rrggbb` (blanco = el de siempre). |

<!-- fin -->

Con una luz del sol, la **hora** del editor y la de la partida salen de
ella (la barra ☀ de la vista la cambia). Con el módulo
[Día y noche](../modulos/dia-y-noche.md), la partida empieza a esa hora y el
sol se mueve; sin él, se queda quieto ahí.

```ron
Sol((hora: 18.5, intensidad: 0.8, color: "#ffd9b0"))
```

## Véase también

- [Componentes](index.md)
- [Empezar una escena desde cero](../../guia/escena-desde-cero.md)
