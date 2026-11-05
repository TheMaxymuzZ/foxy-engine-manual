# Grafo de nodos

Le da a la entidad el comportamiento de un grafo de [nodos](../../guia/nodos.md)
de la carpeta `grafos/`. Cada entidad con este componente tiene su propia
copia del grafo, con sus propias variables, que empieza a funcionar al
llegar a la escena.

<!-- generado: propiedades -->
<!-- Esta tabla la escribe `foxy-engine --referencia-componentes`. -->

| Propiedad | Campo | De fábrica | Descripción |
|---|---|---|---|
| Grafo | `archivo` | — | Archivo del grafo, relativo al proyecto (`grafos/enemigo.nodos.ron`). |
| Variables de la entidad | `variables` | — | El valor de cada variable *de la entidad* del grafo para esta entidad. Las que no se cambian usan su valor inicial. |

<!-- fin -->

En el [Inspector](../../interfaz/inspector.md):

- **Grafo** elige uno de los grafos de entidad del proyecto.
- **Abrir en Nodos** lo abre en el panel [Nodos](../../interfaz/nodos.md).
- **Grafo nuevo** crea un grafo con el nombre de la entidad y lo abre.
- **Variables de la entidad** enseña cada variable de ese ámbito con su
  tipo, para darle un valor propio.

Dentro del grafo, **Esta entidad** es la entidad que lleva el componente.
Una entidad que el grafo mueve con *Ir hacia* o *Poner en un sitio* deja de
estar fija en la rejilla y se dibuja como un objeto suelto.

```ron
GrafoNodos((
    archivo: "grafos/enemigo.nodos.ron",
    variables: {"vision": "12", "patrulla": "(6, 0, 0)"},
))
```

## Véase también

- [Componentes](index.md)
- [Nodos](../../guia/nodos.md)
- [Tutorial: un enemigo que persigue](../../guia/tutorial-enemigo.md)
