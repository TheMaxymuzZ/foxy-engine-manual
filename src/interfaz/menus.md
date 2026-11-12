# Menús y barra de estado

La barra superior del editor reúne los menús, los espacios de trabajo y los
botones de guardar y probar. La barra de estado, abajo, informa de lo que
acaba de pasar.

![La barra superior del editor](../imagenes/capturas/panel-barra-superior.png)

| Nº | Elemento | Descripción |
|---|---|---|
| 1 | **Menús** | Todas las órdenes del editor, agrupadas (ver abajo) |
| 2 | **Espacios** | El espacio de trabajo activo. En pantallas estrechas sale como lista |
| 3 | **Proyecto** | El nombre del proyecto abierto |
| 4 | **Deshacer** y **Rehacer** | <kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>Z</kbd> y <kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>Mayús</kbd>+<kbd>Z</kbd> |
| 5 | **Guardar** | Muestra **Guardar •** con cambios pendientes y **Guardado** cuando todo está a salvo |
| 6 | **Jugar aquí** | Prueba el juego desde donde mira la cámara (<kbd>F5</kbd>) |
| 7 | **Desde el inicio** | Prueba el juego como lo verá el jugador, con su menú principal |

## Los menús

| Menú | Contiene |
|---|---|
| **Archivo** | Proyecto nuevo, abrir y cerrar proyecto, **Guardar** (<kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>S</kbd>), **Guardar todo** (<kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>S</kbd>), volver a abrir lo guardado, importar archivos y modelos, y salir |
| **Editar** | Deshacer, rehacer, **Duplicar** (<kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>D</kbd>), **Ir a verlo** (<kbd>F</kbd>), **Borrar** (<kbd>Supr</kbd>), **Buscar una acción…** (<kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>K</kbd>) y **Preferencias…** (<kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>,</kbd>) |
| **Crear** | Escena nueva, interfaz nueva, objeto nuevo, imagen de pixel art, material e importar modelo |
| **Ver** | La cámara del editor: hora del día, velocidad y el contador de rendimiento |
| **Ventana** | Abrir cualquier panel, **Maximizar el panel** (<kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>Mayús</kbd>+<kbd>M</kbd>) y gestionar los espacios: guardar uno nuevo, restablecer o borrar |
| **Proyecto** | **Ajustes del proyecto…**, **Mapa de escenas…**, **Publicar…**, los archivos del proyecto y mostrar su carpeta |
| **Herramientas** | Las herramientas de la escena, los paneles Materiales, Pixel art, Nodos, Código y Rendimiento, y **Revisar rendimiento** (el [doctor de rendimiento](../guia/optimizar.md#el-doctor-de-rendimiento)) |
| **Ayuda** | Este manual, **Teclas y ratón…**, **Cambiar las teclas…** y la versión del motor |

> <i class="fx fx-consejo"></i> **Consejo.** Cualquier orden de los menús
> se encuentra también escribiendo en la
> [paleta de comandos](../editor/espacio-de-trabajo.md#paleta-de-comandos)
> (<kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>K</kbd>).

## La barra de estado

La barra de estado ocupa la parte de abajo de la ventana.

| Parte | Qué muestra |
|---|---|
| Izquierda | El último mensaje del editor: lo guardado, lo importado, el último error. Un clic abre el panel [Registro](registro.md) |
| **⛔ n** | Cuántos errores hay en los guiones y en el editor. Un clic los muestra |
| Centro | El progreso de las tareas largas, como preparar el mundo |
| **⚠ 42 fps en un portátil normal** | Sale si lo que se ve pasaría de tu [objetivo de rendimiento](../guia/optimizar.md#el-objetivo-de-rendimiento). Un clic abre el doctor de rendimiento |
| Derecha | Los fotogramas por segundo (se quitan en Preferencias) y la posición de la cámara |

## Véase también

- [La interfaz del editor](../empezar/editor.md)
- [Atajos de teclado](../referencia/atajos.md)
