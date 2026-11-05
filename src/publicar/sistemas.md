# Mac, Windows y Linux

Cada sistema tiene su forma de aplicación. Esta página explica qué sale para
cada uno, cómo publicar para un sistema que no es el tuyo y qué hacer si el
juego no se abre.

| Sistema | Qué sale | Cómo se abre |
|---|---|---|
| Mac | `Nombre.app` (y `Nombre-mac.zip`) | Doble clic en la `.app` |
| Windows | La carpeta `Nombre` con `Nombre.exe` y `juego.foxy` (y `Nombre-windows.zip`) | Doble clic en `Nombre.exe` |
| Linux | La carpeta `Nombre` con el ejecutable, `juego.foxy`, el icono y un lanzador `.desktop` (y `Nombre-linux.zip`) | Doble clic en el ejecutable o en el lanzador |

> <i class="fx fx-aviso"></i> **Importante.** En Windows y Linux,
> `juego.foxy` tiene que estar **en la misma carpeta** que el ejecutable.
> Comparte la carpeta entera o el `.zip`, nunca el ejecutable solo.

## Publicar para otro sistema

Un juego publicado lleva dentro el Foxy Engine de su sistema. Para tu
sistema se usa el motor que tienes abierto. Para otro, la ventana pide su
ejecutable:

1. En **Sistema**, elige el otro sistema.
2. Pulsa **Elegir…** junto a **Foxy Engine de …** y busca su ejecutable:
   - **Windows**: `foxy-engine.exe`, del archivo *FoxyEngine-Windows* de
     GitHub Actions o de un PC con Windows.
   - **Linux**: `foxy-engine`, del archivo *FoxyEngine-Linux* de GitHub
     Actions o de un PC con Linux.
3. Pulsa **Publicar para …**.

El editor comprueba que el ejecutable es de ese sistema. La ruta se
recuerda para la próxima vez.

> <i class="fx fx-consejo"></i> **Consejo.** Usa un Foxy Engine de la
> **misma versión** (o más nueva) que el editor con el que publicas. Un motor
> más viejo no abre el paquete y avisa al arrancar.

Para el **Mac**, lo mejor es publicar desde un Mac: así la `.app` sale
firmada y se abre con doble clic. Una `.app` publicada desde otro sistema
sale sin firmar.

## Mac

### «No se puede abrir porque procede de un desarrollador no identificado»

El motor firma la `.app` en tu Mac, pero sin una cuenta de desarrollador de
Apple. En **tu** Mac se abre con doble clic. En **otro** Mac, si la `.app`
llegó por internet, AirDrop o un mensaje, el Mac la marca como descargada y
pide confirmación la primera vez:

1. Haz clic derecho (o <kbd>Control</kbd> + clic) en la `.app` y elige
   **Abrir**.
2. En el aviso, pulsa **Abrir**.

Solo hay que hacerlo una vez. En macOS 15 o más nuevo, si no sale el botón,
ve a **Ajustes del Sistema › Privacidad y seguridad** y pulsa **Abrir
igualmente** junto al nombre del juego.

> <i class="fx fx-nota"></i> **Nota.** Copiada con un disco USB, la `.app`
> no lleva esa marca y se abre con doble clic directamente.

### «La aplicación está dañada y no se puede abrir»

Pasa si la `.app` se publicó desde Windows o Linux (sin firmar) o si se
descomprimió con un programa que pierde los permisos. Publícala otra vez
desde un Mac, o fírmala en el Mac con la Terminal:

```sh
codesign --force --deep --sign - "Nombre.app"
```

### La `.app` no se abre en un Mac con procesador Intel

El juego lleva el motor del Mac en el que se publicó. Un motor compilado en
un Mac con Apple Silicon (M1, M2…) solo funciona en Macs con Apple Silicon.

## Windows

### «Windows protegió su PC»

El `.exe` no lleva firma de Microsoft. La primera vez, pulsa **Más
información › Ejecutar de todas formas**.

### El juego no se abre o se cierra solo

Sale una ventana con el error y la ruta del registro
(`%APPDATA%\<Nombre>\registro.txt`). Las causas y soluciones son las mismas
que las del motor: ver [Windows: el motor no se abre o se cierra
solo](../apendices/problemas.md#windows-el-motor-no-se-abre-o-se-cierra-solo).

### El icono del `.exe` es el zorro

El archivo `.exe` lleva el icono del motor. La ventana del juego y la barra
de tareas usan el icono del juego.

## Linux

### El ejecutable no se abre con doble clic

Algunos gestores de archivos no abren programas con doble clic. Ábrelo
desde la Terminal, en la carpeta del juego:

```sh
./nombre-del-juego
```

Si dice *Permiso denegado*, el `.zip` se descomprimió sin permisos. Dáselos
con `chmod +x nombre-del-juego`.

### Sin sonido

Instala los paquetes de sonido de ALSA (`libasound2` en Debian y Ubuntu).

## Véase también

- [Publicar tu juego](publicar.md)
- [Solución de problemas](../apendices/problemas.md)
- [Instalar Foxy Engine](../empezar/instalar.md)
