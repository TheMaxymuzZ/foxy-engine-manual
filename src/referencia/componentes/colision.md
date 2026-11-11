# Colisión

Decide si se puede chocar con la entidad.

<!-- generado: propiedades -->
<!-- Esta tabla la escribe `foxy-engine --referencia-componentes`. -->

| Propiedad | Campo | De fábrica | Descripción |
|---|---|---|---|
| Sólida | `solida` | Sí | Sin marcar, el objeto se atraviesa. |

<!-- fin -->

Sin este componente, las entidades con modelo son sólidas. Una entidad no
sólida se ve igual, pero se atraviesa.

## Forma

Con qué se choca, en la lista **Forma** (campo `forma`):

| Forma | Campo | Cómo choca |
|---|---|---|
| Sus cubitos | `Cubitos` | Justo sus cubitos, aunque esté girada o escalada: se puede entrar por la puerta de una casa. Es la de serie |
| Caja | `Caja` | Una caja que llena su caja |
| Esfera | `Esfera` | Una bola (un huevo si su caja no es igual de ancha que de alta) |
| Cápsula | `Capsula` | Una cápsula de pie, como un personaje |

```ron
Colision((solida: false))
Colision((solida: true, forma: Esfera))
```

## Véase también

- [Componentes](index.md)
- [Entidades y componentes](../../guia/entidades.md)
