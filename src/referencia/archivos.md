# Archivos del proyecto

Todo lo que haces en Foxy Engine se guarda en **archivos de texto** (salvo las
imágenes, que son PNG). Se pueden leer, editar a mano, copiar, mandar por
correo o subir a GitHub tal cual.

Los archivos `.ron` usan [RON](https://github.com/ron-rs/ron), un formato
parecido a JSON pero más cómodo de leer: admite comentarios con `//`, comas al
final y nombres sin comillas.

## La carpeta de un proyecto

```text
Documentos/Foxy Engine/proyectos/Mi isla/
    proyecto.ron          nombre, tipo, autor, versión, icono y escena inicial
    .foxy/miniatura.png   miniatura para la pantalla de inicio (la hace el editor)
    .foxy/espacio.ron     cómo quedaron los paneles de cada espacio
    mundos/principal.ron  la escena con la que empieza el juego
    mundos/*.ron          las demás escenas
    interfaces/*.ron      menús, marcadores y carteles
    imagenes/*.png        imágenes de pixel art (y su .ron con datos)
    paletas/*.ron         paletas de colores
    materiales.ron        materiales propios y cómo es cada material
    acciones.ron          el mapa de acciones de entrada
    objetos/*.ron         objetos propios y objetos de ejemplo
    prefabricados/*.ron   prefabricados
    sonidos/*.wav, *.ogg  sonidos propios
    .foxy/copias/         copias de seguridad hechas al actualizar el formato
    guiones/mundo.lua     el guion del mundo
    guiones/mundo.nodos.ron  el grafo de nodos del juego
    mundos/*.nodos.ron    el grafo de cada escena (junto a su escena)
    grafos/*.nodos.ron    grafos de entidad
    funciones/*.nodos.ron funciones hechas con nodos
    nodos/*.lua           nodos escritos en Lua
    partidas/             partidas guardadas al jugar
    papelera/             escenas quitadas desde el mapa de escenas
    .papelera/            archivos quitados desde Archivos del proyecto
```

Los nombres de archivo (los *id*) van en minúsculas y sin tildes:
«Botón verde» se guarda como `boton_verde`.

## Proyecto

Archivo: `proyecto.ron`

```ron
(
    nombre: "Mi isla",
    mundo: "mundos/principal.ron",   // escena inicial
    tipo: Voxel3D,                   // Voxel3D, Pixel2D o Voxel2D
    autor: "Andrés",
    version: "0.1.0",
    descripcion: "Un pueblo con mercado y vecinos.",
    icono: "",                       // imagen de imagenes/ sin .png; vacío = el del motor
    cubito: 0.5,                     // tamaño del cubito: 1.0, 0.5 o 0.25 m
    modulos: (clima: true, vecinos: false, ...),   // ver Módulos
    formato: 3,                      // versión del formato del proyecto
)
```

### Actualizar el formato

Cuando una versión nueva del motor cambia el formato de los archivos, al
abrir un proyecto antiguo el editor:

1. Hace una **copia de seguridad** de todo el proyecto en
   `.foxy/copias/formato-<anterior>-<fecha>/`.
2. Copia en `objetos/` los objetos de ejemplo que usan sus escenas.
3. Vuelve a escribir las escenas con el formato nuevo.
4. Lo indica en la barra de estado.

El juego se ve y se juega igual que antes. Para volver atrás, basta con
copiar el contenido de la copia de seguridad sobre la carpeta del
proyecto.

Todos los campos menos `nombre` son opcionales: un proyecto creado con una
versión anterior del motor se abre igual. Se editan desde
[Ajustes del proyecto](../editor/ajustes-proyecto.md).

### Lista de proyectos

`Documentos/Foxy Engine/editor.ron` guarda los proyectos recientes de la
pantalla de inicio (`recientes`, con su carpeta, si está fijado y cuándo se
abrió) y los que se quitaron de la lista (`ocultos`).

### Espacios de trabajo

`.foxy/espacio.ron` guarda el espacio que se estaba usando (`actual`) y, en
`espacios`, cómo quedó cada uno: el árbol de paneles (`arbol`) y las
ventanas separadas (`flotantes`, con su panel, posición y tamaño). Si se
borra, el proyecto se abre con los espacios de serie. Los espacios propios
están en `Documentos/Foxy Engine/espacios/<nombre>.ron`, con un árbol y sus
ventanas. Ver [Personalizar el espacio de trabajo](../editor/espacio-de-trabajo.md).

## Mundos

Archivo: `mundos/<escena>.ron`

```ron
(
    generador: (
        tipo: Isla,           // Isla, Llano, Vacio, Colinas o Cuevas
        semilla: 7,           // otra semilla, otra isla
        lado: 192.0,          // tamaño del mundo (la isla está en el centro)
        radio: 66.0,          // tamaño de la isla
        altura: 16.0,         // altura de las colinas sobre el mar
        nivel_del_mar: 10.0,  // profundidad del mar en los bordes
        arboles: 0.2,         // de 0 (ninguno) a 1 (bosque)
        muelle: true,         // muelle de madera en la playa del sur
    ),
    // Cada generador usa sus campos; ver Generadores de terreno.
    vida: (
        minutos_por_dia: 24.0,   // 0 = la hora no avanza
        dias_por_estacion: 7,
        estacion: Primavera,     // Primavera, Verano, Otono o Invierno
        clima: Despejado,        // Despejado, Nublado, Lluvia o Tormenta
        clima_cambia: true,
    ),
    modulos: (clima: Some(false)),   // lo que la escena cambia de los módulos del proyecto
    carpetas: ["Pueblo", "Pueblo/Casas", "Vecinos"],
    objetos: [
        (tipo: "casa", nombre: "Casa de Plumas", pos: (86.0, 16.0, 118.0), giro: 0, carpeta: "Pueblo/Casas"),
        (tipo: "vecino", nombre: "Plumas", pos: (88.0, 20.0, 123.0), giro: 0, carpeta: "Vecinos",
         frases: ["¡Hola! Vivo en la casa del tejado rojo.", "¿Has visto el pozo?"]),
        (tipo: "zona", nombre: "Cueva", pos: (120.0, 14.0, 90.0), giro: 0,
         accion: IrAEscena(escena: "cueva", entrada: "boca")),
        (tipo: "casa", nombre: "Tienda de Tomás", pos: (108.0, 18.0, 121.0), giro: 3,
         accion: AbrirInterfaz("tienda")),
        (tipo: "puerta", nombre: "Puerta", pos: (92.0, 16.0, 118.0), giro: 0,
         componentes: [Zona((tamano: (4.0, 3.0, 4.0),
             al_entrar: Mover(desplazamiento: (1.0, 0.0, 0.0)),
             al_salir: Mover(desplazamiento: (0.0, 0.0, 0.0))))]),
        (tipo: "farola", nombre: "Farola", pos: (94.0, 16.0, 116.0), giro: 0,
         prefabricado: "farola_de_la_plaza"),
    ],
    cambios: [
        (196, 29, 254, 4, Grava),
    ],
)
```

| Campo | Qué es |
|---|---|
| `generador` | Cómo se genera el terreno: `tipo` y sus parámetros. Ver [Generadores de terreno](../guia/generadores.md). Antes se llamaba `isla` |
| `vida` | Cómo pasa el tiempo. Ver [La vida del mundo](../guia/vida.md#ajustes-de-la-vida) |
| `modulos` | Los [módulos](modulos/index.md) que la escena cambia respecto al proyecto |
| `carpetas` | Carpetas de la escena; las subcarpetas con `/` |
| `objetos` | Objetos colocados: `tipo`, `nombre`, `pos` (centro de la base, en metros) y `giro` (cuartos de vuelta, 0 = mira al sur). Opcionales: `carpeta`, `frases` (vecinos), `accion` (zonas, y objetos que hacen algo al usarlos con <kbd>E</kbd>), `componentes` (ver [Componentes](componentes/index.md)) y `prefabricado` (el id del prefabricado del que es copia) |
| `cambios` | Lo que has cambiado con el pincel: `(x, y, z, cuántos seguidos hacia +x, material)`, en **cubitos** de la rejilla del proyecto |
| `plano` | Solo en las escenas 2D: casilla, resolución, fondo, luz ambiente y las capas con sus mapas. Las posiciones de los `objetos` van entonces en casillas. Ver [Mapas de casillas](../guia/casillas.md#en-el-archivo-de-la-escena) |

El motor construye el mundo en tres pasos: genera el terreno a partir de `generador`,
aplica encima los `cambios` y coloca los `objetos`.

> <i class="fx fx-nota"></i> **Compatibilidad.** Los archivos con `isla:` y
> `terreno:` de versiones anteriores, y los de la Fase 1, que solo
> describían la isla, se siguen abriendo.

## Prefabricados

Archivo: `prefabricados/<id>.ron`

```ron
(
    nombre: "Farola de la plaza",
    tipo: "farola",                  // su modelo; "entidad" si no se ve
    componentes: [
        Luz((intensidad: 1.5, alcance: 10.0)),
    ],
    accion: Ninguna,                 // lo que pasa al usarlo (E)
)
```

Ver [Prefabricados](../guia/entidades.md#prefabricados).

## Acciones de entrada

Archivo: `acciones.ron`. Ver [Acciones de entrada](../guia/acciones-entrada.md#en-el-archivo).

## Sonidos

Carpeta: `sonidos/`, con archivos WAV u OGG. Ver [Sonidos](../guia/sonidos.md).

## Objetos propios

Archivo: `objetos/<id>.ron`

```ron
(
    nombre: "Farolillo",
    tamano: (4, 8, 4),          // ancho, alto y fondo, en cubitos (máx. 64 = 32 m)
    cubitos: [
        (1, 0, 1, 2, Madera),   // (x, y, z, cuántos seguidos hacia +x, material)
        (1, 1, 1, 2, Madera),
        (1, 6, 1, 2, Farol),
    ],
)
```

## Interfaces

Archivo: `interfaces/<nombre>.ron`

Las medidas van en puntos de una pantalla de diseño de **1280 × 720**.

```ron
(
    uso: Pantalla,          // Pantalla, Marcador, MenuPrincipal o MenuPausa
    pausa: true,            // pausa el juego mientras está abierta
    oscurecer: 140,         // 0 = nada, 255 = negro
    ocultar_reloj: false,   // (marcadores) esconde el reloj del motor
    tecla: "I",             // (pantallas) la abre y la cierra al jugar; "" = ninguna
    elementos: [            // de atrás hacia delante
        (
            tipo: Panel,
            nombre: "fondo",
            ancla: Centro,
            pos: (0.0, 0.0),
            tamano: (520.0, 280.0),
            imagen: "imagenes/panel.png",
            pixel: 4.0,
        ),
        (
            tipo: Boton,
            nombre: "cerrar",
            ancla: Centro,
            pos: (0.0, 90.0),
            tamano: (200.0, 56.0),
            texto: "Cerrar",
            accion: CerrarInterfaz,
        ),
    ],
)
```

| Campo del elemento | Qué es |
|---|---|
| `tipo` | `Panel`, `Texto`, `Boton`, `Imagen` o `Barra` |
| `nombre` | Para reconocerlo en la lista y en el guion |
| `ancla` | A qué está pegado: `ArribaIzquierda`, `Arriba`, `ArribaDerecha`, `Izquierda`, `Centro`, `Derecha`, `AbajoIzquierda`, `Abajo` o `AbajoDerecha` |
| `pos` | Distancia al punto del ancla, en puntos |
| `tamano` | Ancho y alto, en puntos |
| `texto` | Puede llevar `{hora}`, `{dia}`, `{estacion}`, `{clima}`, `{escena}`, `{proyecto}` o un valor del guion |
| `letra` | Tamaño de la letra |
| `alinear` | `Izquierda`, `Centro` o `Derecha` |
| `color_texto`, `color`, `color_encima`, `color_borde` | Colores `[r, g, b, a]` de 0 a 255. `color_encima` es el relleno de un botón con el ratón encima |
| `redondeo`, `borde` | Radio de las esquinas y grosor del borde |
| `imagen` | Ruta de una imagen del proyecto (`imagenes/boton.png`), o vacío |
| `pixel` | Puntos de pantalla por píxel de la imagen (para las esquinas de las que se estiran) |
| `proporcion` | `true`: la imagen no se deforma y cabe entera |
| `accion` | Lo que hace un botón. Ver [Acciones](acciones.md) |
| `visible` | `false` lo esconde |
| `valor`, `maximo` | En una barra: lo que la llena (`{vida}` o un número) y el valor con el que está llena |

Todos los campos son opcionales: lo que no se escribe toma su valor por defecto.

## Imágenes

Archivo: `imagenes/<id>.png` y `imagenes/<id>.ron`

La imagen es un **PNG RGBA** normal, de hasta 256 × 256 píxeles. Se dibuja sin
suavizar. Desde las interfaces se nombra por su ruta: `imagenes/boton_verde.png`.

El `.ron` de al lado es opcional (sin él: el nombre del archivo, uso
`Interfaz` y bordes 0):

```ron
(
    nombre: "Botón verde",
    uso: Interfaz,          // Interfaz, Textura, Sprite, Casillas u Otro
    bordes: (4, 4, 4, 4),   // izquierda, arriba, derecha, abajo (en píxeles)
)
```

Las hojas de sprites (`uso: Sprite`) añaden `hoja` y los juegos de casillas
(`uso: Casillas`) añaden `casillas`:

```ron
hoja: Some((
    corte: Rejilla(ancho: 16, alto: 16, margen: 0, separacion: 0),
    ancla: (0.5, 1.0),
    animaciones: {
        "correr": (fotogramas: [2, 3, 4, 5], fps: 15.0, bucle: true, ida_y_vuelta: false),
    },
)),
casillas: Some((
    lado: 16, margen: 0, separacion: 0,
    choques: { 32: Plataforma, 33: Escalera, 34: Peligro, 35: Agua },
    autocasillas: [(nombre: "Hierba", casillas: [ /* 16 casillas */ ])],
)),
```

`corte` puede ser `Entera`, `Rejilla(...)` o `AMano([(x, y, ancho, alto), ...])`.
Ver [Sprites](../guia/sprites.md) y [Mapas de casillas](../guia/casillas.md).

`bordes` sirve para estirar en nueve partes. Ver
[Pixel art](../guia/pixel-art.md#imágenes-que-se-estiran-bordes).

## Paletas

Archivo: `paletas/<id>.ron`

```ron
(
    nombre: "Atardecer",
    colores: ["#2b1d3a", "#5a2d5c", "#a63c5c", "#e2584a", "#f29072", "#ffd75e"],
)
```

Cada color es `"#rrggbb"` o, si es semitransparente, `"#rrggbbaa"`.

## Materiales

Archivo: `materiales.ron`

Solo hace falta escribir lo que cambia; el resto se queda como viene en el
motor. Aquí viven también los materiales propios (`Propio(16)` en adelante).

```ron
(
    materiales: {
        Hierba: (textura_lado: Some("hierba_lado")),
        Teja: (color: Some("#3f8ad6")),
        Propio(16): (nombre: Some("Oro"), color: Some("#e8b43c"), metalico: Some(1.0), pulido: Some(0.8)),
    },
)
```

Todos los campos (color, texturas, luz, metálico, pulido, transparencia,
atravesable, golpes y peso) están en
[Materiales › `materiales.ron`](materiales.md#materialesron).

## Guiones

Archivos: `guiones/mundo.lua` (el guion del mundo) y `guiones/<nombre>.lua`
(guiones de entidad y módulos; pueden ir en subcarpetas).

Código Lua. Ver [Programar en Lua](../guia/programar-lua.md) y [API de Lua](lua.md).

Para los editores externos, el motor escribe además `.foxy/lua/foxy.lua`
(definiciones de la API) y `.luarc.json` (configuración de LuaLS). Ver
[Editores externos](../guia/lua-editor-externo.md).

## Partidas

Archivo: `partidas/<escena>/*.ron`

Las guarda el juego: `ranura_1.ron`, `ranura_2.ron`, `ranura_3.ron` y
`auto.ron`. Guardan la escena, la hora, el día, el clima, la estación, el
jugador (posición, hacia dónde mira y si está agachado), las pelotas y los
valores del guion. Se pueden leer, pero es mejor no cambiarlas a mano.

## Ajustes del jugador

Archivo: `Documentos/Foxy Engine/ajustes.ron`

Comunes a todos los proyectos. Se cambian en el menú *Opciones*:

```ron
(
    sensibilidad_raton: 1.0,   // 0.1 a 4
    sensibilidad_mando: 1.0,   // 0.1 a 4
    invertir_y: false,
    campo_de_vision: 70.0,     // grados, 50 a 110
    balanceo: true,
    mostrar_fps: false,
    volumen_musica: 0.7,       // 0 a 1
    volumen_efectos: 0.9,      // 0 a 1
)
```
