<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="src/imagenes/marca/logo-horizontal-oscuro.png">
    <img alt="Foxy Engine" src="src/imagenes/marca/logo-horizontal-claro.png" width="420">
  </picture>
</p>

# Manual de Foxy Engine

Guía de usuario y referencia de **Foxy Engine**, el motor de juegos de bloques
para Mac, Windows y Linux.

**Léelo en línea: <https://themaxymuzz.github.io/foxy-engine-manual/>**

## Contenido

- **Primeros pasos**: instalar, primer proyecto y un vistazo al editor.
- **Guía del editor**: mundo, carpetas, creador de objetos, pixel art,
  escenas, interfaces, vida del mundo, guiones en Lua y probar el juego.
- **Referencia**: atajos, API de Lua, acciones, objetos, materiales, formato
  de los archivos y línea de comandos.
- **Apéndices**: solución de problemas, glosario, marca e historial.

## Cómo está hecho

El manual es un libro de [mdBook](https://rust-lang.github.io/mdBook/). Cada
página es un archivo Markdown en `src/`, y el índice está en
[`src/SUMMARY.md`](src/SUMMARY.md). Los colores de la marca están en
[`theme/foxy.css`](theme/foxy.css).

Para verlo en tu ordenador:

```sh
cargo install mdbook
mdbook serve --open
```

Cada cambio en `main` se publica solo en GitHub Pages
([`.github/workflows/pages.yml`](.github/workflows/pages.yml)). Los pull
requests solo comprueban que el libro se compila.

## Escribir en el manual

- En español, de tú, con frases cortas y nombres de botones tal como salen en
  el editor (**Guardar**, *Colocar objetos → Mis objetos*).
- Teclas con `<kbd>`: `<kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>S</kbd>`.
- Las capturas van en `src/imagenes/capturas/` y salen del modo sin ventana
  del motor (`foxy-engine --captura …`, ver *Línea de comandos*).
- Si cambia algo en el motor, se cambia aquí en el mismo momento.
