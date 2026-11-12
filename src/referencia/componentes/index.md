# Componentes

Referencia de los componentes que se pueden añadir a una entidad. Ver
[Entidades y componentes](../../guia/entidades.md) para aprender a usarlos.

![Componentes en el inspector](../../imagenes/capturas/panel-componentes.png)

<!-- generado: propiedades -->
<!-- Esta tabla la escribe `foxy-engine --referencia-componentes`. -->

| Componente | En el archivo | Para qué sirve |
|---|---|---|
| [Colisión](colision.md) | `Colision` | Si se choca con el objeto o se atraviesa. |
| [Cuerpo físico](cuerpo-fisico.md) | `CuerpoFisico` | Cae, bota, rueda y se puede empujar o patear. |
| [Controlador de jugador](controlador.md) | `Controlador` | La maneja el jugador: primera o tercera persona, cenital… |
| [Cámara](camara.md) | `Camara` | Distancia y altura de la cámara, o ver el juego desde aquí. |
| [Luz](luz.md) | `Luz` | Ilumina alrededor, con su color y su alcance. |
| [Sonido](sonido.md) | `Sonido` | Un sonido que sale de aquí y se oye más cerca que lejos. |
| [Zona](zona.md) | `Zona` | Una caja invisible: pasa algo al entrar o al salir. |
| [Sprite](sprite.md) | `Sprite` | Una imagen o un fotograma de una hoja de sprites (en 2D). |
| [Animador](animador.md) | `Animador` | Sus animaciones: un clip o una máquina de estados (quieto, andar, correr…). |
| [Recogible](recogible.md) | `Recogible` | Se recoge al tocarlo: suma monedas (o lo que digas), suena y desaparece. |
| [Partículas](particulas.md) | `Particulas` | Fuego, chispas, ascuas, humo, polvo, lluvia, nieve, hojas o una cascada que salen de aquí. |
| [Terreno de cubitos](terreno.md) | `Terreno` | El suelo de cubitos de la escena: plano, islas, colinas, cuevas o una imagen. |
| [Luz del sol](sol.md) | `Sol` | La luz de la escena: la hora del sol, su fuerza y su color. |
| [Niebla](niebla.md) | `Niebla` | Niebla en toda la escena: donde entra el sol salen rayos de luz, y las luces hacen halo. |
| [En la mano](mano.md) | `Mano` | Se lleva en la mano en primera persona: va delante de la cámara y nunca atraviesa las paredes. |

<!-- fin -->

## En el archivo de la escena

Los componentes van en la lista `componentes` de cada entidad. Solo se
escriben los valores distintos de los de fábrica:

```ron
(tipo: "farola", nombre: "Farola de la plaza", pos: (90.0, 16.0, 118.0),
 componentes: [
     Luz((color: "#ffd27a", intensidad: 1.5, alcance: 10.0)),
     Sonido((sonido: "grillos", volumen: 0.6)),
 ]),
```

En una copia de un [objeto reutilizable](../../guia/reutilizables.md),
`componentes` solo guarda lo que la copia cambia; el resto se toma del
prefabricado.

## Véase también

- [Conceptos básicos](../../conceptos/basicos.md)
- [Entidades y componentes](../../guia/entidades.md)
