# Generadores de terreno

El terreno de cada escena lo crea un **generador** a partir de unos pocos
parámetros. Encima se guardan los cambios hechos con el pincel, de modo que
el archivo de la escena sigue siendo pequeño.

![Un terreno de colinas con los materiales de un proyecto vacío](../imagenes/capturas/colinas.png)

## Elegir el generador

Sin nada elegido, el [Inspector](../interfaz/inspector.md) muestra la
sección **Terreno** de la escena:

![La sección Terreno del inspector](../imagenes/capturas/panel-terreno.png)

1. Elige un **Generador**.
2. Ajusta sus parámetros. Solo aparecen los que usa ese generador.
3. Pulsa **Regenerar el terreno**. Las entidades y los bloques puestos a
   mano se conservan.

> <i class="fx fx-aviso"></i> **Importante.** Regenerar el terreno no se puede
> deshacer.

## Generadores

| Generador | En el archivo | Descripción |
|---|---|---|
| **Vacío** | `Vacio` | Ningún terreno. Con *Plataforma*, una plataforma de 6 × 6 m en el centro para no caer |
| **Plano** | `Llano` | Un suelo llano con agua opcional |
| **Isla** | `Isla` | Una isla rodeada de mar, con colinas, árboles y un muelle |
| **Colinas** | `Colinas` | Colinas suaves por todo el mundo, con agua en los valles |
| **Cuevas** | `Cuevas` | Colinas con cuevas por dentro |

## Parámetros

| Parámetro | Campo | Generadores | Descripción |
|---|---|---|---|
| Semilla | `semilla` | Isla, Colinas, Cuevas | Con la misma semilla sale el mismo terreno |
| Lado | `lado` | Todos | Tamaño del mundo, en metros |
| Tamaño de la isla | `radio` | Isla | Radio de la isla |
| Colinas | `altura` | Isla, Colinas, Cuevas | Altura de las colinas |
| Ancho de las colinas | `escala` | Colinas, Cuevas | Distancia entre una colina y la siguiente |
| Cuevas | `cuevas` | Cuevas | De 0 (pocas) a 1 (muchas) |
| Nivel del agua | `nivel_del_mar` | Plano, Isla, Colinas, Cuevas | Altura del agua |
| Árboles | `arboles` | Isla, Colinas | De 0 (ninguno) a 1 (bosque) |
| Muelle | `muelle` | Isla | Un muelle de madera en la playa del sur |
| Plataforma | `plataforma` | Vacío | La plataforma del centro |
| Superficie, Debajo, Fondo | `suelo`, `relleno`, `roca` | Todos menos Vacío | Los materiales de cada capa |

Los materiales de cada capa se eligen entre los del proyecto. Un proyecto
vacío usa sus propios materiales (*Suelo*, *Tierra* y *Roca*).

## En el archivo

```ron
generador: (
    tipo: Colinas,
    semilla: 7,
    lado: 128.0,
    altura: 14.0,
    escala: 40.0,
    nivel_del_mar: 6.0,
    suelo: Propio(16),
    relleno: Propio(17),
    roca: Propio(18),
),
```

> <i class="fx fx-nota"></i> **Nota.** Las escenas de versiones
> anteriores, con `isla:` y `terreno:`, se siguen abriendo y se guardan con
> los nombres nuevos.

## Véase también

- [Construir el mundo](mundo.md)
- [Rejilla y materiales](../editor/ajustes-proyecto.md#rejilla-y-materiales)
