# Articulaciones

Une el objeto con otro objeto, o con el mundo, para que se muevan juntos de
una manera concreta: una puerta en su bisagra, un péndulo, un muelle, una
cuerda, un brazo que gira. Necesita las
[físicas precisas](../../guia/fisicas.md) y un
[cuerpo físico](cuerpo-fisico.md) en los dos objetos.

<!-- generado: propiedades -->
<!-- Esta tabla la escribe `foxy-engine --referencia-componentes`. -->

| Propiedad | Campo | De fábrica | Descripción |
|---|---|---|---|
| Uniones | `lista` | `1 bisagra` | Las articulaciones del objeto: cada una tiene su tipo (`Bisagra`, `Rotula`, `Deslizadera`, `Muelle`, `Cuerda` o `Fija`), con qué objeto se une (`con`, vacío = con el mundo), dónde (`ancla`), su eje, sus límites, su motor y la fuerza con la que se rompe. |

<!-- fin -->

## Cada articulación

| Propiedad | Campo | Descripción |
|---|---|---|
| **Tipo** | `tipo` | `Bisagra` (gira alrededor de un eje), `Rotula` (gira hacia todos lados, como un hombro), `Deslizadera` (se desliza a lo largo de un eje), `Muelle` (tira y empuja como un muelle), `Cuerda` (no deja alejarse más de su largo) o `Fija` (como pegados) |
| **Con** | `con` | El nombre del otro objeto. Vacío = con el mundo (un punto que no se mueve) |
| **Ancla** | `ancla` | Dónde está la unión, en metros desde el centro del objeto |
| **Eje** | `eje` | Bisagra y deslizadera: `X`, `Y` o `Z` del objeto |
| **Límites** | `limites`, `minimo`, `maximo` | Hasta dónde gira (en grados) o se desliza (en metros) |
| **Motor** | `motor`, `fuerza` | La hace girar o deslizarse sola a esa velocidad (grados o metros por segundo) |
| **Largo** | `largo` | Muelle y cuerda: lo que miden. 0 = lo que hay entre los dos al empezar |
| **Dureza y amortiguación** | `rigidez`, `amortiguacion` | Muelle: lo fuerte que tira y lo que tarda en dejar de botar |
| **Se rompe con** | `rotura` | Si la fuerza pasa de esto (en newtons) la unión se rompe. 0 = nunca |
| **Chocan entre sí** | `chocan` | Si los dos objetos unidos chocan entre ellos |

La postura que tienen los objetos en el editor es la de reposo: la unión
se crea tal cual están colocados.

```ron
Articulaciones((lista: [
    (tipo: Bisagra, con: "Tabla 3", ancla: (-0.5, 0.0, 0.0), eje: Z),
]))
```

## Véase también

- [Físicas precisas](../../guia/fisicas.md)
- [Laboratorio de físicas](../../tu-primer-juego/laboratorio-fisicas.md)
- [Componentes](index.md)
