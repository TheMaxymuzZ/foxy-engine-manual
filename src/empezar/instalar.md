# Instalar Foxy Engine

Foxy Engine funciona en **macOS**, **Windows** y **Linux**. Por ahora se
instala compilándolo desde su código, lo que solo lleva unos minutos la
primera vez. Cuando llegue la Fase 6 habrá instaladores listos para descargar.

## Lo que necesitas

| | Qué hace falta |
|---|---|
| Sistema | macOS (probado en macOS 14 con Apple M2), Windows 10/11, o Linux con Vulkan |
| Tarjeta gráfica | Compatible con Metal (Mac), DirectX 12 o Vulkan |
| Espacio | Unos gigas libres para la compilación; la app ocupa mucho menos |
| Herramientas | [Rust](https://rustup.rs) y Git |

## En Mac

### 1. Instala las herramientas (solo una vez)

Abre la app **Terminal** y pega estas dos líneas, una cada vez:

```sh
xcode-select --install
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

La primera instala las herramientas de Apple; la segunda, Rust. Cuando
terminen, cierra la Terminal y ábrela de nuevo.

### 2. Descarga el motor

```sh
git clone https://github.com/TheMaxymuzZ/foxy-engine.git ~/foxy-engine
```

### 3. Instala la app

```sh
cd ~/foxy-engine && scripts/instalar-mac.sh
```

El script compila el motor y deja **Foxy Engine.app**, con su icono, en
`Documentos/Foxy Engine`. Ábrela con doble clic; puedes arrastrarla al Dock.

> **Consejo.** Si prefieres probarlo sin instalar nada, dentro de la carpeta
> del motor basta con `cargo run --release`.

## En Windows

1. Instala [Rust](https://rustup.rs) (el instalador te pedirá las
   *Build Tools* de Visual Studio; acepta) y [Git](https://git-scm.com).
2. En *PowerShell*:

   ```powershell
   git clone https://github.com/TheMaxymuzZ/foxy-engine.git
   cd foxy-engine
   cargo run --release
   ```

## En Linux

Instala Rust y las librerías del mando y del sonido. En Debian o Ubuntu:

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
sudo apt install git libudev-dev libasound2-dev
git clone https://github.com/TheMaxymuzZ/foxy-engine.git
cd foxy-engine
cargo run --release
```

## Actualizar a una versión nueva

Cada vez que salga una versión nueva, en Mac:

```sh
cd ~/foxy-engine && git checkout main && git pull && scripts/instalar-mac.sh
```

Luego **cierra el motor del todo** con <kbd>Cmd</kbd>+<kbd>Q</kbd> y vuelve a
abrirlo desde `Documentos/Foxy Engine`. La versión nueva sustituye a la
anterior; **tus proyectos no se tocan**, porque viven en su propia carpeta.

En Windows y Linux: `git pull` y otra vez `cargo run --release`.

## Al abrirlo

Durante unos segundos sale la pantalla **Powered by Foxy Engine**. Un clic o
cualquier tecla la salta.

![Powered by Foxy Engine](../imagenes/capturas/marca-splash.png)

Después se abre el editor con tu último proyecto. La primera vez crea uno
llamado **Mi isla**. Sigue en [Tu primer proyecto](primer-proyecto.md).
