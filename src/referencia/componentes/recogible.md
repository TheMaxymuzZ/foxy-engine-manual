# Recogible

La entidad desaparece cuando el jugador la toca, suena y suma a un valor
del juego. Sirve para monedas, gemas, llaves o vidas.

<!-- generado: propiedades -->
<!-- Esta tabla la escribe `foxy-engine --referencia-componentes`. -->

| Propiedad | Campo | De fábrica | Descripción |
|---|---|---|---|
| Suma a | `valor` | `"monedas"` | El valor del juego que aumenta. |
| Cantidad | `cantidad` | 1 | Cuánto suma. Puede ser negativo. |
| Sonido | `sonido` | `"moneda"` | Lo que suena al recogerlo. Vacío no suena. |
| Chispas | `chispas` | Sí | Suelta unas chispas al recogerlo. |

<!-- fin -->

Una [interfaz](../../guia/interfaces.md) enseña el valor escribiendo su
nombre entre llaves en un texto, como `Monedas: {monedas}`. Al recogerla se
llama al evento **Al recoger** de los nodos y a `al_recoger(entidad, valor)`
de los guiones.

Funciona en 2D y en 3D. En 3D se recoge al pasar a menos de 1 m.

```ron
Recogible((valor: "gemas", cantidad: 1.0, sonido: "moneda"))
```

## Véase también

- [Juegos 2D](../../guia/juegos-2d.md#recoger-cosas)
- [Componentes](index.md)
