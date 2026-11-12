# Línea de comandos

El programa `foxy-engine` se puede abrir desde la Terminal con opciones. Con
`cargo`, las opciones van después de `--`:

```sh
cargo run --release -- --juego
```

## Abrir

| Opción | Qué hace |
|---|---|
| *(ninguna)* | Abre el editor en la [pantalla de inicio](../empezar/pantalla-de-inicio.md) |
| `--juego` | Abre solo el juego, sin editor |
| `--mundo <archivo.ron>` | Abre ese mundo |
| `--ayuda`, `-h` | Enseña la ayuda |
| `--version`, `-V` | Enseña la versión |

## Publicar

Estas opciones [publican un juego](../publicar/publicar.md) sin abrir el
editor, o abren uno ya publicado.

| Opción | Qué hace |
|---|---|
| `--publicar <carpeta>` | Publica el proyecto de esa carpeta con lo guardado en su `proyecto.ron` |
| `--sistema <nombre>` | `mac`, `windows` o `linux`. Por defecto, el sistema en el que estás |
| `--motor <ejecutable>` | El Foxy Engine del otro sistema, si no es el tuyo |
| `--salida <carpeta>` | Dónde se deja el juego. Por defecto, `Documentos/Foxy Engine/Juegos publicados` |
| `--sin-zip` | Sin el `.zip` para compartir |
| `--paquete <juego.foxy>` | Abre un juego publicado a partir de su paquete |

```sh
foxy-engine --publicar "Documents/Foxy Engine/proyectos/Zorro Saltarín" --sistema linux --motor foxy-engine
```

## Documentación de los nodos y de Lua

Estas opciones escriben un archivo y terminan, sin abrir ninguna ventana.

| Opción | Qué escribe |
|---|---|
| `--referencia-nodos <archivo.md>` | La [referencia de todos los nodos](nodos.md), en Markdown, a partir del catálogo del motor |
| `--referencia-lua <archivo.md>` | La [referencia de la API de Lua](api-lua.md), en Markdown, a partir del catálogo del motor |
| `--referencia-componentes <carpeta>` | Pone al día las tablas de propiedades de las [páginas de componentes](componentes/index.md) a partir del catálogo del motor |
| `--definiciones-lua <archivo.lua>` | Las definiciones de la API (`motor.*`, `yo`, `propiedades` y las funciones que llama el motor) para editores con LuaLS, como Visual Studio Code o Zed. Ver [Editores externos](../guia/lua-editor-externo.md) |

Se pueden usar varias a la vez.

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
| `--pestana <nombre>` | `mundo`, `guion`, `nodos` (el grafo de un enemigo), `nodos-depurar` (el mismo grafo con sus cables encendidos), `objeto`, `pixel`, `imagen`, `texturas`, `interfaz`, `proyecto` (un proyecto con escenas e interfaces), `vacio` (un proyecto vacío recién creado), `materiales`, `archivos`, `importar`, `importado`, `inicio`, `plantillas`, `aprender`, `novedades` (la pantalla de inicio con proyectos de ejemplo), `nuevo` (el asistente de proyecto nuevo), `ajustes` (los ajustes del proyecto), `ajustes-graficos` (en su página Gráficos) o `plataformas-2d`, `aventura-cenital`, `vacio-2d`, `plataformas-voxel`, `tercera-persona` y `puzle` (un proyecto de esa plantilla) o `publicar` (la plantilla Plataformas 2D publicada, con la ventana **Publicar** abierta) o `modelos` (los modelos 3D de ejemplo junto a una farola de cubitos) |
| `--plantilla <nombre>` | Sin `--editor`: dibuja el mundo de una plantilla (`vacio-3d`, `isla-voxel`, `isla-de-ejemplo` o `plataformas-voxel`) |
| `--herramienta <nombre>` | `cursor`, `elegir`, `poner`, `quitar`, `pintar`, `extruir` u `objeto`; en 2D, `choques` o `autocasillas` abren ese modo del panel Casillas |
| `--simetria <ejes>` | Simetría puesta: `x`, `y`, `z` o varios juntos (`xz`) |
| `--modelo <archivo>` | Un `.vox` o `.qb` para `--pestana importar` (la ventana) o `importado` (ya importado) |
| `--raton x,y` | Dónde está el ratón, en píxeles |
| `--elegir <n>` | Elige el objeto número `n` (desde 1) |
| `--jugar` | Como *Jugar aquí* |
| `--romper <x,y,z>` | Jugando, rompe el bloque de ese punto, en metros. Se puede repetir |
| `--esperar <s>` | Jugando, segundos que pasan antes de la captura (de 0 a 60) |
| `--rendimiento` | Con la ventana [Rendimiento](../guia/rendimiento.md) abierta (mide unos fotogramas de verdad) |
| `--memoria` | Con la ventana Rendimiento abierta en su pestaña *Memoria* |
| `--sin-lejos` | Dibuja todo con todo el detalle, sin el [detalle de lejos](../guia/rendimiento.md#detalle-de-lejos) |
| `--espacio <nombre>` | El espacio de trabajo: `construir`, `programar`, `pixel-art` o `2d` |
| `--abrir <panel>` | Abre también ese panel. Se puede repetir |
| `--sencillo` | El editor en el [modo Sencillo](../empezar/modo-sencillo.md), sin los paneles técnicos |
| `--tutorial <n>` | Con el paso `n` del [tutorial guiado](../empezar/modo-sencillo.md#el-tutorial-guiado) a la vista (desde 1) |
| `--flotante <panel>` | Ese panel en una ventana separada. Se puede repetir |
| `--maximizar <panel>` | Ese panel maximizado |
| `--recortar <panel>` | Guarda solo ese panel, con su pestaña |
| `--paleta <texto>` | Con la paleta de comandos abierta y eso escrito |
| `--tema-claro` | Con el tema claro |

### Gráficos de la captura

Valen para cualquier captura, con o sin `--editor`. Ver
[Gráficos](../guia/graficos.md).

| Opción | Qué hace |
|---|---|
| `--calidad <nivel>` | `bajo`, `medio`, `alto`, `ultra` o `cine` |
| `--tono <curva>` | `cine`, `blender`, `neutro` o `ninguno` |
| `--exposicion <n>` | Exposición en pasos, por ejemplo `-1` o `0.5` |
| `--corazon <dibujante>` | `nuevo` o `clasico` |
| `--atmosfera <piezas>` | `realista`, `nada` o una lista separada por comas con `luz`, `oclusion`, `agua`, `cielo`, `destello`, `desenfoque`, `color` y `temporal` |

Los paneles son `vista`, `proyecto`, `escena`, `inspector`, `codigo`,
`nodos`, `archivos`, `materiales`, `pixel` y `registro`. Las capturas
empiezan siempre por los espacios de serie y no cambian los que guardaste.

### Capturas del juego

| Opción | Qué hace |
|---|---|
| `--juego --menu <pantalla>` | `inicio`, `jugando`, `pausa`, `opciones`, `opciones-graficos` (su página Gráficos), `controles` (cambiando una tecla), `guardar`, `cargar`, `menu-propio` o `cartel` |
| `--hablar` | El jugador hablando con el primer vecino |
| `--splash` | La pantalla *Powered by Foxy Engine* |

`--editor`, `--raton`, `--elegir`, `--jugar` y `--menu` solo valen con
`--captura`.

## Medir el motor

Estas órdenes sirven para comprobar que ningún cambio en el motor lo hace más
lento ni cambia la imagen sin querer. Las usa GitHub Actions en cada cambio.

### Escenas de prueba enormes

El motor fabrica solo cinco escenas para medirse al límite. Salen siempre
iguales:

| Nombre | Qué tiene |
|---|---|
| `miles-de-objetos` | 4.096 objetos sobre un llano; uno de cada cuatro gira o flota con un comportamiento |
| `mundo-grande` | Colinas con cuevas de 768 × 768 m |
| `muchas-luces` | 400 farolas encendidas de noche |
| `cueva-con-antorchas` | Una sala de piedra con columnas y seis antorchas que hacen sombra |
| `rayos-de-sol` | Una sala con tres agujeros en el techo, sol de mañana y niebla: salen rayos de luz |

Para verlas: `--captura x.png --enorme <nombre>`. Para verlas en el editor y
jugando, con el perfilador:
`--captura x.png --editor --pestana perfilador --jugar --rendimiento`.

### Pruebas de rendimiento

```sh
cargo run --release -- --medir ver
cargo run --release -- --medir comprobar
cargo run --release -- --medir guardar
```

Mide cada escena enorme sin ventana: lo que cuesta fabricarla, hacer sus
mallas, preparar y dibujar un fotograma, lo que tarda la tarjeta y, jugando,
cada parte del motor. También cuenta trozos, triángulos, llamadas de dibujo,
luces y memoria.

- `ver` enseña las medidas.
- `comprobar` las compara con las guardadas en `pruebas/rendimiento.ron` y
  falla si las cuentas cambian más de un 5 % o si algo tarda más del doble.
  Como cada ordenador va a su ritmo, antes mide una tarea fija (la *vara de
  medir*) y compara en esa medida.
- `guardar` las deja como referencia nueva (cuando un cambio es a propósito).

Con `--escena <nombre>` mide solo esa escena y con `--salida <carpeta>` deja
las medidas en `medidas.ron`.

### Capturas de referencia

```sh
cargo run --release -- --referencias comprobar
cargo run --release -- --referencias guardar
```

Hace unas cuantas capturas (el mundo de día y de noche, las escenas
enormes, el editor, la pantalla de inicio, el 2D y el menú del juego) y las
compara con las guardadas en `pruebas/referencias/`. Si una cambia más del
0,5 % de sus píxeles, falla y deja al lado una imagen
`<nombre>-diferencias.png` con lo que ha cambiado pintado en rojo. Las
diferencias pequeñas de color, que dependen de la tarjeta gráfica, no
cuentan.

Con `--escena <nombre>` hace solo esa captura y con `--salida <carpeta>`
elige dónde dejar las de hoy (por defecto, `capturas/referencias`).

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
