# Editores externos

Los guiones se pueden escribir en **Visual Studio Code**, **Zed** o cualquier
editor con el servidor de lenguaje de Lua (LuaLS). El motor les da la misma
lista de funciones que usa el panel **Código**, así que tienen el mismo
autocompletado y la misma ayuda.

## Abrir el proyecto en VS Code o Zed

1. Abre el panel **Código**.
2. Pulsa **VS Code / Zed** en la barra de herramientas.

El motor prepara la carpeta del proyecto y la abre en el editor que
encuentre (primero VS Code y luego Zed). Si no encuentra ninguno, abre la
carpeta del proyecto para que la abras tú.

> <i class="fx fx-aviso"></i> **Importante.** En VS Code, instala la
> extensión **Lua** (de *sumneko*). Zed trae Lua de serie.

## Qué se prepara

| Archivo | Qué es |
|---|---|
| `.foxy/lua/foxy.lua` | Las definiciones de toda la API: `motor.*`, `yo`, `propiedades` y las funciones que llama el motor, con su ayuda y sus tipos. El motor no lo ejecuta |
| `.luarc.json` | La configuración de LuaLS: Lua 5.4, la carpeta de definiciones y las variables `motor`, `yo` y `propiedades`. Solo se escribe si no existe |

Las definiciones se escriben de nuevo cada vez que se pulsa **VS Code / Zed**,
así que siempre corresponden a la versión del motor instalada. También se
pueden generar a mano:

```sh
foxy-engine --definiciones-lua .foxy/lua/foxy.lua
```

## Cambios hechos fuera del motor

El motor vigila la carpeta `guiones/`:

- **Sin cambios propios**: si un guion abierto en el panel **Código** cambia
  en el disco, se vuelve a leer solo.
- **Con cambios sin guardar** en el motor: sale el aviso «Este archivo ha
  cambiado fuera del motor», con los botones **Leer el de fuera** y
  **Quedarme con el mío**.
- **Jugando**: el guion se recarga en el juego en marcha, como al guardarlo
  en el motor. Ver [Recargar sin reiniciar](lua-depurar.md#recargar-sin-reiniciar).

## Véase también

- [Programar en Lua](programar-lua.md)
- [Línea de comandos](../referencia/linea-de-comandos.md)
- [Referencia de la API de Lua](../referencia/api-lua.md)
