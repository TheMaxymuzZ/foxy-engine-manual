# Ordenar la escena

A la izquierda, debajo del panel «Proyecto», está la lista **En la escena**:
todo lo que hay en el mundo, con su nombre y su tipo (por ejemplo
*Tienda de Tomás · Casa*). Cuando un mundo crece, esa lista se
ordena en **carpetas**, como los archivos de tu ordenador.

![Carpetas en la escena](../imagenes/capturas/editor-proyecto.png)

## Crear carpetas

- <i class="fx fx-carpeta-nueva"></i> (a la derecha de *En la escena*) crea
  una carpeta nueva.
- **Clic derecho** en una carpeta → <i class="fx fx-carpeta"></i>
  **Subcarpeta nueva** crea una dentro.
- En el mismo menú están <i class="fx fx-editar"></i> **Renombrar** y
  <i class="fx fx-borrar"></i> **Borrar carpeta**. Borrar una
  carpeta **no borra sus objetos**: pasan a la carpeta de arriba.

## Meter objetos en carpetas

- **Arrastra** un objeto de la lista hasta una carpeta.
- O haz **clic derecho** en el objeto → <i class="fx fx-carpeta"></i> **Mover a** y elige la carpeta (o
  *En una carpeta nueva*).

Un clic en un objeto de la lista lo elige en el mundo. <i class="fx fx-ver"></i> **Ver** (<kbd>F</kbd>)
lleva la cámara hasta él.

## Meter objetos dentro de otros

Si sueltas un objeto **encima de otro objeto** (y no de una carpeta), va
**dentro** de él y se mueve con él. Ver
[Objetos libres y jerarquía](objetos-libres.md#objetos-dentro-de-otros).

## Cómo se guardan

Las carpetas se guardan dentro del mundo. Las subcarpetas se escriben con `/`:

```ron
carpetas: [
    "Pueblo",
    "Pueblo/Casas",
    "Vecinos",
],
objetos: [
    (tipo: "casa", nombre: "Casa de Plumas", id: 1, pos: (86.0, 16.0, 118.0), carpeta: "Pueblo/Casas"),
],
```

> <i class="fx fx-consejo"></i> **Consejo.** Una carpeta *Juego* para el punto de inicio, las entradas, las
> zonas y las pelotas, y otra por cada barrio o zona del mapa, hacen que un
> mundo grande sea fácil de recorrer.
