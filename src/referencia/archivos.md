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
    proyecto.ron          nombre del proyecto y escena inicial
    mundos/principal.ron  la escena con la que empieza el juego
    mundos/*.ron          las demás escenas
    interfaces/*.ron      menús, marcadores y carteles
    imagenes/*.png        imágenes de pixel art (y su .ron con datos)
    paletas/*.ron         paletas de colores
    materiales.ron        color y textura de los materiales
    objetos/*.ron         objetos propios
    guiones/mundo.lua     el guion del mundo
    partidas/             partidas guardadas al jugar
    papelera/             escenas quitadas desde el mapa de escenas
```

Los nombres de archivo (los *id*) van en minúsculas y sin tildes:
«Botón verde» se guarda como `boton_verde`.

## Proyecto

Archivo: `proyecto.ron`

```ron
(
    nombre: "Mi isla",
    mundo: "mundos/principal.ron",   // escena inicial
)
```

## Mundos

Archivo: `mundos/<escena>.ron`

```ron
(
    isla: (
        semilla: 7,           // otra semilla, otra isla
        lado: 192.0,          // tamaño del mundo (la isla está en el centro)
        radio: 66.0,          // tamaño de la isla
        altura: 16.0,         // altura de las colinas sobre el mar
        nivel_del_mar: 10.0,  // profundidad del mar en los bordes
        arboles: 0.2,         // de 0 (ninguno) a 1 (bosque)
        muelle: true,         // muelle de madera en la playa del sur
    ),
    vida: (
        minutos_por_dia: 24.0,   // 0 = la hora no avanza
        dias_por_estacion: 7,
        estacion: Primavera,     // Primavera, Verano, Otono o Invierno
        clima: Despejado,        // Despejado, Nublado, Lluvia o Tormenta
        clima_cambia: true,
    ),
    carpetas: ["Pueblo", "Pueblo/Casas", "Vecinos"],
    objetos: [
        (tipo: "casa", nombre: "Casa de Plumas", pos: (86.0, 16.0, 118.0), giro: 0, carpeta: "Pueblo/Casas"),
        (tipo: "vecino", nombre: "Plumas", pos: (88.0, 20.0, 123.0), giro: 0, carpeta: "Vecinos",
         frases: ["¡Hola! Vivo en la casa del tejado rojo.", "¿Has visto el pozo?"]),
        (tipo: "zona", nombre: "Cueva", pos: (120.0, 14.0, 90.0), giro: 0,
         accion: IrAEscena(escena: "cueva", entrada: "boca")),
    ],
    cambios: [
        (196, 29, 254, 4, Grava),
    ],
)
```

| Campo | Qué es |
|---|---|
| `isla` | Cómo se genera el terreno. Ver [Construir el mundo](../guia/mundo.md#la-isla) |
| `vida` | Cómo pasa el tiempo. Ver [La vida del mundo](../guia/vida.md#ajustes-de-la-vida) |
| `carpetas` | Carpetas de la escena; las subcarpetas con `/` |
| `objetos` | Objetos colocados: `tipo`, `nombre`, `pos` (centro de la base, en metros) y `giro` (cuartos de vuelta, 0 = mira al sur). Opcionales: `carpeta`, `frases` (vecinos) y `accion` (zonas) |
| `cambios` | Lo que has cambiado con el pincel: `(x, y, z, cuántos seguidos hacia +x, material)`, en **cubitos de medio metro** |

El motor construye el mundo en tres pasos: genera la isla a partir de `isla`,
aplica encima los `cambios` y coloca los `objetos`.

> **Compatibilidad.** Los archivos de la Fase 1, que solo describían la isla
> (sin `isla:` alrededor), se siguen abriendo.

## Objetos propios

Archivo: `objetos/<id>.ron`

```ron
(
    nombre: "Farolillo",
    tamano: (4, 8, 4),          // ancho, alto y fondo, en cubitos (máx. 32 = 16 m)
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
| `tipo` | `Panel`, `Texto`, `Boton` o `Imagen` |
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
    uso: Interfaz,          // Interfaz, Textura u Otro
    bordes: (4, 4, 4, 4),   // izquierda, arriba, derecha, abajo (en píxeles)
)
```

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
motor.

```ron
(
    materiales: {
        Hierba: (textura_lado: Some("hierba_lado")),
        Yeso: (textura: Some("ladrillos")),
        Teja: (color: Some("#3f8ad6")),
    },
)
```

| Campo | Qué es |
|---|---|
| `color` | Color de arriba (y de los lados, si no se pone `lado`) |
| `lado` | Color de los lados |
| `textura` | Imagen de `imagenes/` (por su id) para las caras de arriba, y las de los lados si no hay `textura_lado` |
| `textura_lado` | Imagen para los lados |

Los nombres de los materiales están en [Materiales](materiales.md).

## Guion

Archivo: `guiones/mundo.lua`

Código Lua. Ver [Guiones en Lua](../guia/guiones.md) y [API de Lua](lua.md).

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
