# Luz

Ilumina alrededor de la entidad, de día y de noche.

| Propiedad | Campo | De fábrica | Descripción |
|---|---|---|---|
| Color | `color` | `#ffd27a` | Color de la luz |
| Intensidad | `intensidad` | 1 | De 0 a 4 |
| Alcance | `alcance` | 8 m | Hasta dónde llega |
| Altura | `altura` | 1 m | Altura de la luz sobre la base de la entidad |

Las luces se ven en el editor y al jugar. Los materiales con luz propia,
como el farol, siguen iluminando sin necesidad de este componente.

```ron
Luz((color: "#80c0ff", intensidad: 2.0, alcance: 12.0, altura: 3.0))
```

## Véase también

- [Componentes](index.md)
- [Entidades y componentes](../../guia/entidades.md)
