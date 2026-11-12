# Solución de problemas

## No veo lo nuevo después de actualizar

Seguramente sigue abierta la versión anterior. En Mac:

1. Cierra el motor del todo con <kbd>Cmd</kbd>+<kbd>Q</kbd> (cerrar la
   ventana no basta).
2. Instala otra vez, con el comando completo:

   ```sh
   cd ~/foxy-engine && git checkout main && git pull && scripts/instalar-mac.sh
   ```

3. Abre **Foxy Engine.app** desde `Documentos/Foxy Engine`, no desde una copia
   antigua del Dock o de *Descargas*.

## El mundo va lento o a tirones

1. Abre **Ver → Rendimiento** y mira los fotogramas por segundo y los
   triángulos desde el sitio donde va peor.
2. Comprueba que está activado el **detalle de lejos** y prueba a bajar su
   distancia.
3. Si el «peor» fotograma es mucho más alto que la media, revisa que la
   **sincronía vertical** esté activada en
   [Preferencias](../guia/preferencias.md).

Más en [Rendimiento](../guia/rendimiento.md).

## Windows: el motor no se abre o se cierra solo

Desde la versión 0.0.1-PR15, si el motor se cierra por un error, sale una
ventana **«Foxy Engine se ha cerrado por un error»** con el motivo y la ruta
del registro. Qué hacer:

1. Comprueba que tienes el `foxy-engine.exe` **más reciente** (ver
   [Instalar](../empezar/instalar.md#en-windows)). Las versiones anteriores
   abrían todos los gráficos a la vez y, con algunos controladores, se
   cerraban sin avisar.
2. Actualiza el **controlador de la tarjeta gráfica** desde la web del
   fabricante (Intel, AMD o NVIDIA) o desde *Windows Update*.
3. Prueba a forzar unos gráficos concretos desde *PowerShell*, en la carpeta
   del `.exe`:

   ```powershell
   $env:WGPU_BACKEND = "dx12"; .\foxy-engine.exe
   ```

   Si con `dx12` no va, prueba `vulkan` y después `gl`.
4. Mira el [registro](#el-registro-registrotxt): dice qué gráficos ha probado
   y por qué ha fallado cada uno.

## Windows: «Windows protegió su PC»

Sale la primera vez porque el programa todavía no está firmado. Pulsa
**Más información → Ejecutar de todas formas**. Solo hay que hacerlo una vez
por cada `.exe` nuevo.

## Un juego publicado no se abre

Las soluciones para cada sistema (el aviso del Mac, «Windows protegió su
PC», permisos en Linux) están en [Mac, Windows y
Linux](../publicar/sistemas.md). El registro de un juego publicado está en
[su carpeta de datos](../publicar/publicar.md#dónde-guarda-el-jugador).

## <i class="fx fx-registro"></i> El registro (`registro.txt`)

Cada vez que se abre, el motor apunta lo que hace en
`Documentos/Foxy Engine/registro.txt` (en Windows,
`C:\Users\<tu usuario>\Documents\Foxy Engine\registro.txt`): la versión,
el sistema, los gráficos que prueba y cualquier error. Se sobrescribe cada
vez que abres el motor, así que **cópialo justo después del fallo** si
quieres enseñárselo a alguien.

## `cargo: command not found`

Rust no está instalado, o la Terminal se abrió antes de instalarlo. Instálalo
(ver [Instalar](../empezar/instalar.md)) y abre una Terminal nueva.

## «El motor no conoce estos objetos»

El mundo usa un objeto cuyo archivo no está en `objetos/` (quizá lo borraste
o lo renombraste). Vuelve a ponerlo en la carpeta, o borra esas copias del
mundo.

## Un modelo 3D sale enorme, diminuto, sin textura o no sale

- **Enorme o diminuto**: el programa lo exportó en otra unidad. Cambia su
  **Escala** en el Inspector, o expórtalo en metros. Los que miden más de
  100 m se pasan solos de centímetros a metros.
- **Sin textura** (un `.gltf` o un `.obj`): faltan las imágenes a su lado.
  Importa el modelo arrastrando el `.gltf` o el `.obj` (no la carpeta): el
  motor copia con él lo que nombra. Si las imágenes estaban en otra carpeta
  con una ruta absoluta, mejor expórtalo como `.glb`.
- **No sale, y el Inspector lo dice en rojo**: el archivo se movió, se
  renombró o está roto. Mira el mensaje y el [registro](#el-registro-registrotxt).
- **Sale negro o al revés**: las caras miran hacia dentro. En Blender,
  *Malla → Normales → Recalcular hacia fuera* antes de exportar.

Ver [Modelos 3D (glTF y OBJ)](../guia/modelos-3d.md).

## Un botón o una zona no lleva a ningún sitio

En el panel «Proyecto», abre <i class="fx fx-mapa"></i> **Cómo se
conectan…** (en el grupo *Escenas*): marca con <i class="fx fx-aviso"></i>
las zonas y botones que llevan a una escena que no existe. Revisa también que el **punto de entrada**
tenga exactamente el nombre que pide la acción.

## Mi guion no hace nada

- Si el guion tiene errores, `mundo.lua` lleva un <i class="fx fx-aviso"></i>
  en el panel «Proyecto». Ábrelo y pulsa **Comprobar** para verlos.
- Mira la **consola**: ahí salen los errores al jugar.
- Revisa el nombre de la función: `al_hablar`, no `alHablar` ni `al_Hablar`.
- Añade un `print("aquí llego")` para ver si la función se llama.

## Una escena o una interfaz tiene un <i class="fx fx-aviso"></i>

No es un error: avisa de que **nada lleva todavía** a esa escena, o de que
**nada abre** esa interfaz, así que no se verá al jugar. Para una escena,
crea una salida desde el [mapa de escenas](../guia/escenas.md#el-mapa-de-escenas)
o un objeto con [*Al usarlo*](../guia/mundo.md#al-usarlo-e). Para una
interfaz, mira [Cómo se abre en el juego](../guia/interfaces.md#cómo-se-abre-en-el-juego).

## «El guion tarda demasiado»

Hay un bucle que no termina nunca (un `while true do` sin `break`, por
ejemplo), o una cuenta que tarda más de 0,3 segundos de una vez. El motor
la corta para que el juego no se cuelgue. Si de verdad necesitas una
cuenta tan larga, pártela en trozos con `esperar()` o llévala a una
[extensión en Rust](../guia/extensiones-rust.md).

## Un valor del guion sale vacío en una interfaz

El texto `{monedas}` solo se rellena cuando el guion ha hecho
`motor.poner_valor("monedas", …)`. Comprueba que el nombre sea exactamente el
mismo, con las mismas mayúsculas.

## El mando no responde

Conéctalo antes de abrir el juego. Funcionan los mandos de Xbox y
PlayStation. En Linux hace falta `libudev` (ver [Instalar](../empezar/instalar.md#en-linux)).

## No hay sonido en Linux

Instala `libasound2-dev` y vuelve a compilar.

## He roto un archivo a mano

Si el motor no puede leer un `.ron`, dice en qué línea está el fallo. Los
errores típicos: una coma que falta entre dos elementos, unas comillas sin
cerrar, o un material mal escrito (`Flor_Roja` en vez de `FlorRoja`).

> <i class="fx fx-consejo"></i> **Consejo.** Guarda tus proyectos en Git o en GitHub: como todo es texto,
> verás exactamente qué cambió y podrás volver atrás.
