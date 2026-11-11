# Tu primer juego

La forma más rápida de aprender Foxy Engine es **empezar con una plantilla
que ya funciona y cambiarla**. Cada plantilla es un juego pequeño: lo creas,
pulsas **Jugar aquí** y ya se juega. Después eliges sus objetos, miras sus
comportamientos y los cambias para hacer tu propio juego.

Cada página de esta sección sigue los mismos pasos:

1. **Crear el proyecto** con la plantilla.
2. **Jugarlo** para ver qué hace.
3. **Ver cómo está hecho**: qué objetos tiene y qué comportamientos llevan.
4. **Cambiarlo**: unos cambios pequeños, uno detrás de otro.
5. **Seguir**: ideas y páginas para ir más allá.

No hace falta escribir código en ninguna. Todas se pueden seguir en el
[modo Sencillo](../empezar/modo-sencillo.md).

| Quiero hacer… | Plantilla | Página |
|---|---|---|
| Un juego desde una hoja en blanco | Vacío 3D o Vacío 2D | [Desde cero](desde-cero.md) |
| Un juego de correr y saltar, visto de lado | Plataformas 2D o Plataformas vóxel | [Plataformas](plataformas.md) |
| Un juego de explorar, visto desde arriba | Aventura cenital | [Vista desde arriba](vista-desde-arriba.md) |
| Un juego 3D con el personaje visto por detrás | Aventura en tercera persona | [Tercera persona](tercera-persona.md) |
| Un juego de pensar | Puzle de botones | [Puzle](puzle.md) |
| Un mundo para construir y romper | Isla vóxel o Isla de ejemplo | [Mundo de cubitos](mundo-de-cubitos.md) |

> <i class="fx fx-consejo"></i> **Consejo.** Si algo se rompe mientras
> pruebas, <kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>Z</kbd> deshace el último
> cambio, y siempre puedes crear otro proyecto con la misma plantilla.

## Lo que tienen en común

- **Los objetos**: todo lo que hay en la escena es un objeto, y se elige
  con un clic en la Vista o en el panel **En la escena**.
- **Los comportamientos**: lo que hace cada objeto. Salen en el Inspector,
  debajo de su nombre, con sus valores. Ver
  [Comportamientos](../guia/comportamientos.md).
- **Los valores del juego**: las monedas, las gemas o las estrellas que se
  cuentan. Los enseña el **Marcador**, una [interfaz](../guia/interfaces.md)
  que escribe `{monedas}`.
- **El guion del mundo**: unas pocas líneas de Lua que saludan al empezar y
  celebran al ganar. Está en el grupo **Guiones** del panel Proyecto y se
  puede dejar como está.
