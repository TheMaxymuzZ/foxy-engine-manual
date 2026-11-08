# Terreno de cubitos

El suelo de cubitos de la escena y cómo se genera. Solo lo lleva el objeto
**Terreno de cubitos** (no está en *Añadir componente*): se pone con
**Crear → Terreno de cubitos**. Una escena lleva uno o ninguno.

<!-- generado: propiedades -->
<!-- Esta tabla la escribe `foxy-engine --referencia-componentes`. -->

| Propiedad | Campo | De fábrica | Descripción |
|---|---|---|---|
| Generador | `tipo` | `Llano` | Vacio (solo aire), Llano, Colinas, Cuevas, Isla o Alturas (una imagen en grises). |
| Semilla | `semilla` | 7 | Cambia la forma del relieve: el mismo número da siempre el mismo terreno. |
| Lado | `lado` | 96 m | Tamaño del mundo de cubitos (se redondea a trozos enteros). |
| Tamaño de la isla | `radio` | 66 m | Solo en **Isla**: radio de la isla. |
| Colinas / Del negro al blanco | `altura` | 16 m | Altura de las colinas; en **Alturas**, lo que sube el blanco sobre el negro. |
| Nivel del agua | `nivel_del_mar` | 4 m | Altura del agua sobre el fondo del mundo (en el llano, el suelo queda un metro por encima). |
| Árboles | `arboles` | 0 | De 0 (ninguno) a 1 (bosque). |
| Muelle | `muelle` | No | Solo en **Isla**: un muelle de madera en la playa del sur. |
| Superficie | `suelo` | `Hierba` | Material de arriba (menos en **Isla**, que pone hierba, arena y piedra según el sitio). |
| Debajo | `relleno` | `Tierra` | Material de los tres cubitos de debajo de la superficie. |
| Fondo | `roca` | `Piedra` | Material de todo lo de más abajo. |
| Ancho de las colinas | `escala` | 40 m | Solo en **Colinas** y **Cuevas**: más, más suaves. |
| Cuevas | `cuevas` | 0,5 | Solo en **Cuevas**: de 0 (ninguna) a 1 (muchas). |
| Plataforma | `plataforma` | Sí | Solo en **Vacio**: una plataforma de 6 × 6 m en el centro, para no caerse. |
| Imagen | `imagen` | — | Solo en **Alturas**: la imagen del proyecto (`imagenes/relieve.png`); blanco alto, negro bajo. |

<!-- fin -->

Cada generador usa solo algunos campos: en el Inspector y en el archivo
salen solo esos. Los cambios se aplican al pulsar **Regenerar el terreno**,
que se deshace con <kbd>Cmd/Ctrl</kbd>+<kbd>Z</kbd>. Los generadores y sus
campos se explican en [El terreno de cubitos](../../guia/generadores.md).

```ron
(tipo: "terreno", nombre: "Terreno", id: 1, pos: (0.0, 0.0, 0.0),
 componentes: [Terreno((tipo: Alturas, semilla: 7, lado: 128.0, altura: 16.0,
     nivel_del_mar: 3.0, arboles: 0.0, imagen: "imagenes/relieve.png"))]),
```

## Véase también

- [Componentes](index.md)
- [El terreno de cubitos](../../guia/generadores.md)
