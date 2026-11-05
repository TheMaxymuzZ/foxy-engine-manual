# Colisión

Decide si se puede chocar con la entidad.

<!-- generado: propiedades -->
<!-- Esta tabla la escribe `foxy-engine --referencia-componentes`. -->

| Propiedad | Campo | De fábrica | Descripción |
|---|---|---|---|
| Sólida | `solida` | Sí | Sin marcar, la entidad se atraviesa. |

<!-- fin -->

Sin este componente, las entidades con modelo son sólidas. Una entidad no
sólida se dibuja aparte de los cubitos del mundo: no se puede cavar ni pintar
sobre ella.

```ron
Colision((solida: false))
```

## Véase también

- [Componentes](index.md)
- [Entidades y componentes](../../guia/entidades.md)
