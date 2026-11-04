# Componentes

Referencia de los componentes que se pueden añadir a una entidad. Ver
[Entidades y componentes](../../guia/entidades.md) para aprender a usarlos.

![Componentes en el inspector](../../imagenes/capturas/panel-componentes.png)

| Componente | En el archivo | Estado |
|---|---|---|
| [Colisión](colision.md) | `Colision` | Disponible |
| [Cuerpo físico](cuerpo-fisico.md) | `CuerpoFisico` | Disponible |
| [Controlador de jugador](controlador.md) | `Controlador` | Disponible |
| [Cámara](camara.md) | `Camara` | Disponible |
| [Luz](luz.md) | `Luz` | Disponible |
| [Sonido](sonido.md) | `Sonido` | Disponible |
| [Zona](zona.md) | `Zona` | Disponible |
| [Guion](guion.md) | `Guion` | Disponible |
| [Sprite](sprite.md) | `Sprite` | Disponible |
| [Animador](animador.md) | `Animador` | Llega con la animación |
| [Grafo de nodos](grafo-de-nodos.md) | `GrafoNodos` | Disponible |
| [Recogible](recogible.md) | `Recogible` | Disponible |
| [Partículas](particulas.md) | `Particulas` | Disponible |

## En el archivo de la escena

Los componentes van en la lista `componentes` de cada entidad. Solo se
escriben los valores distintos de los de fábrica:

```ron
(tipo: "farola", nombre: "Farola de la plaza", pos: (90.0, 16.0, 118.0), giro: 0,
 componentes: [
     Luz((color: "#ffd27a", intensidad: 1.5, alcance: 10.0)),
     Sonido((sonido: "grillos", volumen: 0.6)),
 ]),
```

En una copia de un [prefabricado](../../guia/entidades.md#prefabricados),
`componentes` solo guarda lo que la copia cambia; el resto se toma del
prefabricado.

## Véase también

- [Conceptos básicos](../../conceptos/basicos.md)
- [Entidades y componentes](../../guia/entidades.md)
