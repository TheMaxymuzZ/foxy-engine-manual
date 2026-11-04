# Nodos (guiones sin código)

Los **nodos** hacen lo mismo que un [guion en Lua](guiones.md), pero sin
escribir: se ponen cajas y se unen con cables. Sirven para lo de cada día,
como que un vecino conteste según el tiempo, que suene una campana por la
mañana o que un cofre dé monedas.

![La pestaña Nodos](../imagenes/capturas/nodos.png)

## Abrir los nodos

En el panel «Proyecto», grupo *Guion*, haz clic en **Nodos (sin código)**.
Se abre la pestaña 🔌 **Nodos**:

- A la **izquierda**, todos los nodos que se pueden añadir, por colores.
- En el **centro**, el lienzo donde se colocan y se unen.
- A la **derecha**, el Lua que sale de tus nodos. No hace falta mirarlo,
  pero enseña cómo se escribiría a mano.

## Cómo se leen

Cada cadena va de izquierda a derecha y tiene tres tipos de nodos:

| Color | Tipo | Qué hace |
|---|---|---|
| Naranja | **Cuándo** | Empieza la cadena: dice cuándo pasa |
| Azul | **Si** | Pregunta algo. Tiene dos salidas: **sí** y **no** |
| Verde | **Hacer** | Hace algo y sigue con el siguiente |

Por ejemplo: *Al hablar con Plumas* → *Sumar a un valor (monedas, +1)* →
*Si el clima es Lluvia* → **sí**: *Responder «¡Qué día más feo!»*, **no**:
*Responder «¡Toma una moneda!»*.

## Trabajar con nodos

| Para | Haz |
|---|---|
| Añadir un nodo | Un botón de la izquierda, o clic derecho en el lienzo |
| Moverlo | Arrastra su cabecera (el título) |
| Unir dos nodos | Arrastra desde la bolita de la **derecha** de uno hasta la bolita de la **izquierda** del otro |
| Quitar un cable | Arrastra desde su bolita de salida y suéltalo en el vacío |
| Borrar un nodo | Clic derecho en su cabecera → *Borrar el nodo*, o elígelo y pulsa <kbd>Supr</kbd> |
| Mover el lienzo | Arrastra el fondo |
| Guardar | **Guardar** o <kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>S</kbd> |

Cada salida va a un solo sitio. Si unes una salida que ya tenía cable, el
cable viejo se cambia por el nuevo.

## Los nodos

### Cuándo

| Nodo | Cuándo pasa |
|---|---|
| **Al empezar** | Al empezar la partida |
| **Al hablar con** | Al hablar con ese vecino (vacío: con cualquiera) |
| **Cada día nuevo** | Cada vez que empieza un día |
| **Al llegar la hora** | Cuando el reloj llega a esa hora en punto |
| **Cada segundo** | Una vez por segundo mientras se juega |
| **Al entrar en la escena** | Al llegar a esa escena (vacío: a cualquiera) |
| **Al usar un objeto** | Cuando se usa un objeto cuya acción es [llamar a esa función del guion](mundo.md#al-usarlo-e). Escribe el mismo nombre en los dos sitios, como `al_abrir_cofre` |

### Si

| Nodo | Pregunta |
|---|---|
| **Si el clima es** | Despejado, nublado, lluvia o tormenta |
| **Si la estación es** | Primavera, verano, otoño o invierno |
| **Si la hora está entre** | Entre dos horas. Si la primera es mayor (de 20 a 6), pasa por la medianoche |
| **Si un valor** | Compara un valor del guion (como `monedas`) con un número: *es*, *no es*, *es más de*, *es menos de* o *es al menos* |
| **Si sale al azar** | Sale «sí» ese tanto por ciento de las veces |

### Hacer

| Nodo | Qué hace |
|---|---|
| **Decir** | Enseña un mensaje abajo |
| **Responder** | Lo que contesta el vecino. Solo vale después de *Al hablar con* y acaba la cadena |
| **Poner el clima** / **la estación** / **la hora** | Los cambia al momento |
| **Sonar** | Un sonido del motor (campana, pájaro, trueno…) |
| **Llevar a un vecino** | El vecino camina hasta ese punto (en metros) |
| **Ir a la escena** | Cambia de escena, entrando por la entrada que digas |
| **Abrir la interfaz** / **Cerrar la interfaz** | Abre una [interfaz](interfaces.md) o cierra la de arriba |
| **Poner un valor** | Guarda un número o un texto con nombre. Las interfaces lo enseñan con `{nombre}` y se guarda con la partida |
| **Sumar a un valor** | Le suma (o resta, con un número negativo) |

## Nodos y Lua juntos

Los nodos se guardan en `guiones/mundo.nodos.ron`, al lado de `mundo.lua`.
Al jugar, el motor los convierte en Lua y los carga **con** tu guion: si los
dos tienen, por ejemplo, *Al empezar*, se hacen los dos (primero el del
guion escrito). Si los dos responden a un vecino, vale la respuesta del
guion escrito.

> **Consejo:** si un día una cadena se te queda corta, copia el Lua de la
> derecha a `mundo.lua` y sigue desde ahí.

Los nodos se usan al jugar cuando están **guardados**. Una pestaña con
cambios sin guardar lleva un punto en su nombre (🔌 Nodos •).
