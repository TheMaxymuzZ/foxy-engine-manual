# Colisión

Decide si se puede chocar con la entidad.

| Propiedad | Campo | De fábrica | Descripción |
|---|---|---|---|
| Sólida | `solida` | Sí | Sin marcar, la entidad se atraviesa |

Sin este componente, las entidades con modelo son sólidas. Una entidad no
sólida se dibuja aparte de los cubitos del mundo: no se puede cavar ni pintar
sobre ella.

```ron
Colision((solida: false))
```

## Véase también

- [Componentes](index.md)
- [Entidades y componentes](../../guia/entidades.md)
