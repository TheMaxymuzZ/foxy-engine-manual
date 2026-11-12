# Vehículo

Convierte el objeto en un coche de cuatro ruedas con motor, freno,
dirección y suspensión. Necesita las
[físicas precisas](../../guia/fisicas.md). Si no tiene
[cuerpo físico](cuerpo-fisico.md), el motor le pone uno de caja de 800 kg.

<!-- generado: propiedades -->
<!-- Esta tabla la escribe `foxy-engine --referencia-componentes`. -->

| Propiedad | Campo | De fábrica | Descripción |
|---|---|---|---|
| Lo conduce | `conductor` | `Jugador` | `Jugador` (se sube con **Usar**) o `Guion` (con `motor.conducir`). |
| Motor | `motor` | 60 | La fuerza del motor. |
| Freno | `freno` | 4 | La fuerza del freno. |
| Giro | `giro` | 30° | Cuánto giran las ruedas de delante. |
| Radio de las ruedas | `radio_ruedas` | 0,4 m | El tamaño de las ruedas. |
| Suspensión | `suspension` | 0,3 m | Cuánto bajan y suben las ruedas. |
| Dureza | `dureza` | 30 | Lo dura que es la suspensión. |
| Agarre | `agarre` | 2 | Cuánto se agarran las ruedas al suelo antes de derrapar. |
| Rueda | `rueda` | — | El objeto que se dibuja en cada rueda (vacío = una rueda sencilla). |

<!-- fin -->

Las ruedas se ponen solas en las cuatro esquinas de abajo del objeto. El
morro es el lado que mira hacia **−Z** (al norte cuando el objeto no está
girado).

## Conducir

- Con **Lo conduce: Jugador**, acércate y pulsa **Usar** (<kbd>E</kbd>)
  para subir. Acelera con <kbd>W</kbd>, frena y da marcha atrás con
  <kbd>S</kbd>, gira con <kbd>A</kbd> y <kbd>D</kbd>, y frena del todo con
  <kbd>Espacio</kbd>. Pulsa **Usar** otra vez para bajar.
- Con **Lo conduce: Guion**, lo mueve el nodo **Conducir un vehículo** o
  `motor.conducir(coche, acelerar, girar, frenar)` en Lua.

```ron
Vehiculo((conductor: Jugador, motor: 90.0, giro: 25.0))
```

## Véase también

- [Físicas precisas](../../guia/fisicas.md)
- [Componentes](index.md)
