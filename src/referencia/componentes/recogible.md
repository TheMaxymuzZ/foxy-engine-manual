# Recogible

La entidad desaparece cuando el jugador la toca, suena y suma a un valor
del juego. Sirve para monedas, gemas, llaves o vidas.

| Propiedad | Campo | De fábrica | Descripción |
|---|---|---|---|
| Suma a | `valor` | `monedas` | El valor que sube |
| Cantidad | `cantidad` | 1 | Cuánto suma. Puede ser negativo |
| Sonido | `sonido` | `moneda` | Lo que suena al recogerla (vacío = nada) |
| Chispas | `chispas` | Sí | Suelta unas chispas al recogerla |

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
