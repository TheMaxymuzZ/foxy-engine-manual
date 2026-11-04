# Línea de comandos

El programa `foxy-engine` se puede abrir desde la Terminal con opciones. Con
`cargo`, las opciones van después de `--`:

```sh
cargo run --release -- --juego
```

## Abrir

| Opción | Qué hace |
|---|---|
| *(ninguna)* | Abre el editor con el último proyecto |
| `--juego` | Abre solo el juego, sin editor |
| `--mundo <archivo.ron>` | Abre ese mundo |
| `--ayuda`, `-h` | Enseña la ayuda |
| `--version`, `-V` | Enseña la versión |

## Capturas sin ventana

Con `--captura` el motor dibuja una escena y la guarda como imagen PNG, **sin
abrir ninguna ventana**. Sirve para revisar cambios en ordenadores sin pantalla
y en GitHub Actions; así se hacen las capturas de este manual.

```sh
cargo run --release -- --captura isla.png
cargo run --release -- --captura atardecer.png --hora 17.6 --camara 150,16,150 --mirar 100,12,100
cargo run --release -- --captura editor.png --editor --mundo mundos/plaza_de_prueba.ron --elegir 1
cargo run --release -- --captura pausa.png --juego --menu pausa --mundo mundos/plaza_de_prueba.ron
cargo run --release -- --captura hablar.png --juego --hablar --estacion otono --mundo mundos/plaza_de_prueba.ron
```

| Opción | Qué hace | Por defecto |
|---|---|---|
| `--captura <archivo.png>` | Guarda la imagen ahí | — |
| `--ancho <n>`, `--alto <n>` | Tamaño de la imagen, en píxeles | 1280 × 720 |
| `--tiempo <s>` | Segundos que pasan antes de la foto | 1 |
| `--hora <h>` | Hora del día, de 0 a 24 | 16.5 |
| `--camara x,y,z` | Dónde está la cámara, en metros | — |
| `--mirar x,y,z` | Hacia dónde mira, en metros | — |
| `--clima <nombre>` | `despejado`, `nublado`, `lluvia` o `tormenta` | — |
| `--estacion <nombre>` | `primavera`, `verano`, `otono` o `invierno` | — |

### Capturas del editor

| Opción | Qué hace |
|---|---|
| `--editor` | Dibuja también los paneles del editor |
| `--pestana <nombre>` | `mundo`, `guion`, `nodos`, `objeto`, `pixel`, `imagen`, `texturas`, `interfaz`, `proyecto` (un proyecto con escenas e interfaces), `vacio` (un proyecto vacío recién creado), `materiales`, `archivos`, `importar` o `importado` |
| `--herramienta <nombre>` | `cursor`, `elegir`, `poner`, `quitar`, `pintar`, `extruir` u `objeto` |
| `--simetria <ejes>` | Simetría puesta: `x`, `y`, `z` o varios juntos (`xz`) |
| `--modelo <archivo>` | Un `.vox` o `.qb` para `--pestana importar` (la ventana) o `importado` (ya importado) |
| `--raton x,y` | Dónde está el ratón, en píxeles |
| `--elegir <n>` | Elige el objeto número `n` (desde 1) |
| `--jugar` | Como *Jugar aquí* |
| `--romper <x,y,z>` | Jugando, rompe el bloque de ese punto, en metros. Se puede repetir |
| `--esperar <s>` | Jugando, segundos que pasan antes de la captura (de 0 a 60) |

### Capturas del juego

| Opción | Qué hace |
|---|---|
| `--juego --menu <pantalla>` | `inicio`, `jugando`, `pausa`, `opciones`, `guardar`, `cargar`, `menu-propio` o `cartel` |
| `--hablar` | El jugador hablando con el primer vecino |
| `--splash` | La pantalla *Powered by Foxy Engine* |

`--editor`, `--raton`, `--elegir`, `--jugar` y `--menu` solo valen con
`--captura`.

## Gráficos

En Windows el motor prueba **DirectX 12**, luego **Vulkan** y por último
**OpenGL**, y se queda con el primero que funcione. En Mac usa Metal y en
Linux, Vulkan. Para obligarlo a usar uno, pon la variable `WGPU_BACKEND`
antes de abrirlo:

```powershell
$env:WGPU_BACKEND = "dx12"     # dx12, vulkan o gl
.\foxy-engine.exe
```

En Windows, el `.exe` abre sin consola. Si lo lanzas desde *cmd* o
*PowerShell*, los mensajes salen ahí; además, siempre se guardan en
[`registro.txt`](../apendices/problemas.md#el-registro-registrotxt).

## Pruebas

```sh
cargo test                      # todas las pruebas
FOXY_REQUIRE_GPU=1 cargo test   # falla si no hay tarjeta gráfica (así corre en CI)
```
