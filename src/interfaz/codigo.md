# Código

El panel **Código** es el editor de guiones de Lua del motor: el guion del
mundo, los guiones de entidad y los módulos.

![El panel Código con un guion de enemigo](../imagenes/capturas/panel-codigo.png)

| Nº | Elemento | Descripción |
|---|---|---|
| 1 | **Pestañas** | Los guiones abiertos. **+** abre otro |
| 2 | **Barra** | Guardar, Comprobar, Buscar, Dividir, la lista de funciones y abrir en un editor externo |
| 3 | **Margen** | Los números de línea y las flechas para plegar funciones |
| 4 | **Punto de parada** | Un clic en el margen pone o quita un punto rojo; jugando, el juego se para ahí |
| 5 | **Estado** | Los errores del guion o la ayuda del autocompletado |

Se abre con un clic en un guion del grupo **Guiones** del panel
[Proyecto](proyecto.md), con **Abrir en Código** en el componente Guion del
inspector, desde *Herramientas → Código* o en el espacio **Programar**.
Jugando, se abre encima del juego con <kbd>F7</kbd>.

## Partes del panel

| Parte | Qué hace |
|---|---|
| **Pestañas** | Un guion en cada una. El punto `•` indica cambios sin guardar. **+** crea un guion a partir de una plantilla o abre otro |
| **Guardar** | Guarda el guion (<kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>S</kbd>). Jugando, se recarga en el juego |
| **Comprobar** | Busca errores en todo el guion |
| **Buscar** | Buscar y reemplazar, con o sin distinguir mayúsculas (<kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>F</kbd>) |
| **Dividir** | Enseña dos guiones, o dos partes del mismo, uno al lado del otro |
| **Funciones** | Lista las funciones del guion. Al elegir una, salta a ella |
| **VS Code / Zed** | Abre el proyecto en un [editor externo](../guia/lua-editor-externo.md) con el mismo autocompletado |
| **Margen** | Números de línea, puntos de parada (clic), marcas de error y triángulos para plegar funciones y bloques |
| **Barra de abajo** | Los errores y avisos del guion, o la ayuda de lo que hay bajo el ratón |

## Escribir

- **Autocompletado**: al escribir sale la lista de lo que encaja (`motor.`,
  las propiedades, tus funciones y variables y las palabras de Lua), con la
  ayuda de cada una. Se elige con las flechas e <kbd>Intro</kbd> o
  <kbd>Tab</kbd>.
- **Ayuda de la función**: dentro de los paréntesis de una función de
  `motor`, encima sale su firma con el parámetro actual resaltado.
- **Ir a la definición**: <kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+clic o
  <kbd>F12</kbd> sobre un nombre. Funciona también con las funciones de los
  módulos.
- **Errores**: los de sintaxis se subrayan en rojo al momento; los nombres
  de `motor` que no existen, en amarillo.
- **Sangría y comentarios**: <kbd>Intro</kbd> mantiene la sangría,
  <kbd>Tab</kbd> y <kbd>Mayús</kbd>+<kbd>Tab</kbd> la cambian y
  <kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>/</kbd> comenta las líneas.

![El autocompletado de la API](../imagenes/capturas/codigo-autocompletar.png)

> <i class="fx fx-consejo"></i> **Consejo.** Si cambias un guion en otro
> editor, el panel lo vuelve a leer solo. Si además tenías cambios sin
> guardar, te pregunta cuál quieres conservar.

## Véase también

- [Programar en Lua](../guia/programar-lua.md)
- [Consola](consola.md) y [Depurador](depurador.md)
- [Atajos de teclado](../referencia/atajos.md#panel-código)
- [Referencia de la API de Lua](../referencia/api-lua.md)
