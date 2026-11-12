# Cuerpo físico

El objeto se mueve con la física: cae, bota, rueda, flota en el agua y se
puede empujar. Con las [físicas precisas](../../guia/fisicas.md)
encendidas en el proyecto tiene además tipo, forma, masa, rozamiento,
capas de choque y se puede romper.

<!-- generado: propiedades -->
<!-- Esta tabla la escribe `foxy-engine --referencia-componentes`. -->

| Propiedad | Campo | De fábrica | Descripción |
|---|---|---|---|
| Rebote | `rebote` | 0,55 | De 0 (no bota) a 1 (bota sin perder fuerza). |
| Empujable | `empujable` | Sí | Se empuja al caminar contra ella y se patea con **Usar**. |
| Tipo | `tipo` | — | Con las físicas precisas: `Dinamico` cae y choca, `Cinematico` lo mueven los guiones y las animaciones, `Fijo` no se mueve nunca. |
| Forma | `forma` | — | La forma con la que choca: `Automatica`, `Caja`, `Esfera`, `Capsula`, `Convexa`, `Malla` o `Cubitos`. |
| Masa | `masa` | — | Cuánto pesa. 0 = según su tamaño. |
| Rozamiento | `friccion` | — | De 0 (resbala como el hielo) a 1 o más (se agarra). |
| Frenado | `frenado` | — | Cuánto le frena el aire al moverse. |
| Frenado al girar | `frenado_giro` | — | Cuánto le frena el aire al girar. |
| Gravedad | `gravedad` | — | Cuánto le afecta la gravedad: 1 = normal, 0 = flota, negativa = sube. |
| Muy rápido | `continua` | — | Detección continua: no atraviesa paredes aunque vaya muy rápido (balas, pelotas lanzadas). |
| Sin girar | `sin_giro` | — | No vuelca ni gira (personajes, cajas que solo se deslizan). |
| Capa | `capa` | — | La capa de choque del objeto (de 0 a 7; sus nombres se ponen en los ajustes «Físicas»). |
| Choca con | `choca_con` | — | Con qué capas choca (una casilla por capa; 255 = con todas). |
| Rompible | `rompible` | — | Se rompe en pedazos con un golpe fuerte. |
| Resistencia | `resistencia` | — | Cuánto golpe aguanta antes de romperse (más alto = más duro). |

<!-- fin -->

Sin las físicas precisas solo cuentan **Rebote** y **Empujable**: el
cuerpo se calcula como una esfera del tamaño del modelo y, al empezar la
partida, el objeto parte del lugar donde se colocó en el editor.

## Las formas

| Forma | Cuándo usarla |
|---|---|
| **Automática** | La elige el motor: esfera para la pelota, envolvente para lo que se mueve y malla para lo fijo |
| **Caja** | Cajas, muros, coches: la más rápida |
| **Esfera** | Pelotas y bolas |
| **Cápsula** | Personajes y barriles |
| **Convexa** | Lo que se mueve con forma irregular: el motor la envuelve como con papel de regalo |
| **Malla** | Lo fijo con huecos (un arco, una cueva): choca con cada cara |
| **Cubitos** | Choca cubito a cubito, exacto y rápido para modelos de vóxeles |

```ron
CuerpoFisico((rebote: 0.1, tipo: Dinamico, forma: Caja, masa: 800.0,
              rompible: true, resistencia: 2.0))
```

## Véase también

- [Físicas precisas](../../guia/fisicas.md)
- [Articulaciones](articulaciones.md)
- [Vehículo](vehiculo.md)
- [Componentes](index.md)
