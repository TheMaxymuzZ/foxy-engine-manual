# Cuerpo físico

La entidad se mueve con la física: cae, bota, rueda, flota en el agua y se
puede empujar.

| Propiedad | Campo | De fábrica | Descripción |
|---|---|---|---|
| Rebote | `rebote` | 0,55 | De 0 (no bota) a 1 (bota sin perder fuerza) |
| Empujable | `empujable` | Sí | Se empuja al caminar contra ella y se patea con *Usar* |

El cuerpo se calcula como una esfera del tamaño del modelo. Al empezar la
partida, la entidad parte del lugar donde se colocó en el editor.

```ron
CuerpoFisico((rebote: 0.8))
```

## Véase también

- [Componentes](index.md)
- [Entidades y componentes](../../guia/entidades.md)
