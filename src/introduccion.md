<div class="portada">
  <img class="logo-claro" src="imagenes/marca/logo-horizontal-claro.svg" alt="Foxy Engine">
  <img class="logo-oscuro" src="imagenes/marca/logo-horizontal-oscuro.svg" alt="Foxy Engine">
  <p class="lema">Motor de juegos vóxel y pixel art para Mac, Windows y Linux.</p>
</div>

# Introducción

**Foxy Engine** es un motor de juegos de escritorio para crear mundos de
cubitos (vóxeles) y juegos de pixel art. Reúne en un solo editor todo lo
necesario para hacer un juego: construir escenas, modelar objetos, dibujar
texturas, diseñar menús y dar comportamiento con nodos sin código o con
guiones en Lua. Cada proyecto se guarda como archivos de texto legibles que
se pueden copiar, comparar y versionar con Git.

![La pantalla de inicio de Foxy Engine](imagenes/capturas/inicio.png)

## Qué se puede hacer

<div class="tarjetas">
  <a href="guia/mundo.html"><strong><i class="fx fx-mundo"></i>Construir</strong><span>Esculpir el terreno con pinceles de bloques y colocar objetos en la escena.</span></a>
  <a href="guia/creador.html"><strong><i class="fx fx-objeto"></i>Modelar</strong><span>Crear objetos de cubitos propios o importarlos de MagicaVoxel y Qubicle.</span></a>
  <a href="guia/pixel-art.html"><strong><i class="fx fx-pixel"></i>Dibujar</strong><span>Pixel art para botones, iconos y texturas de los materiales.</span></a>
  <a href="guia/interfaces.html"><strong><i class="fx fx-interfaz"></i>Diseñar interfaces</strong><span>Menús, marcadores y carteles que funcionan con ratón, teclado y mando.</span></a>
  <a href="guia/nodos.html"><strong><i class="fx fx-mapa"></i>Programar sin código</strong><span>Comportamientos con nodos unidos por cables.</span></a>
  <a href="guia/guiones.html"><strong><i class="fx fx-guion"></i>Programar en Lua</strong><span>Guiones para quien prefiere escribir código.</span></a>
</div>

## Organización del manual

| Parte | Contenido |
|---|---|
| **Empezar** | Instalación, la pantalla de inicio, la creación de un proyecto y los primeros pasos en el editor. Se recomienda leerla en orden. |
| **Manual del editor** | Una página por cada panel y herramienta, con capturas. Se puede consultar en cualquier orden. |
| **Conceptos** | Las ideas en las que se basa el motor: proyectos, escenas y recursos. |
| **Referencia** | Teclas, funciones de Lua, acciones, objetos, materiales, formatos de archivo y línea de comandos. |
| **Apéndices** | Solución de problemas, glosario, marca e historial de versiones. |

El buscador (la lupa de la parte superior o la tecla <kbd>S</kbd>) encuentra
cualquier término en todo el manual.

## Convenciones

| Formato | Significado |
|---|---|
| <kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>S</kbd> | <kbd>Cmd</kbd> en Mac; <kbd>Ctrl</kbd> en Windows y Linux |
| **Guardar** | Un botón, una pestaña, un menú o una opción del editor, con su nombre exacto |
| **Proyecto → Ajustes del proyecto** | Una opción dentro de un menú |
| `mundos/principal.ron` | Un archivo o una carpeta, relativos a la carpeta del proyecto |
| `motor.decir(texto)` | Código que se escribe tal cual |

> <i class="fx fx-nota"></i> **Nota.** Información adicional sobre lo que se
> está explicando.

> <i class="fx fx-consejo"></i> **Consejo.** Un atajo o una práctica
> recomendada.

> <i class="fx fx-aviso"></i> **Importante.** Algo que puede hacer perder
> trabajo si no se tiene en cuenta.

## Unidades

Foxy Engine mide en **metros**. El terreno está formado por **cubitos** de
0,5 m; dos por dos por dos cubitos forman un **bloque** de 1 m. Los archivos
indican en cada caso si un valor está en metros o en cubitos.

## Versión

Este manual corresponde a Foxy Engine **0.0.1-PR22**. Los cambios de cada
versión están en el [historial de versiones](apendices/historial.md).
