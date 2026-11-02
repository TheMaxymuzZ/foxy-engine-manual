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

## `cargo: command not found`

Rust no está instalado, o la Terminal se abrió antes de instalarlo. Instálalo
(ver [Instalar](../empezar/instalar.md)) y abre una Terminal nueva.

## «El motor no conoce estos objetos»

El mundo usa un objeto cuyo archivo no está en `objetos/` (quizá lo borraste
o lo renombraste). Vuelve a ponerlo en la carpeta, o borra esas copias del
mundo.

## Un botón o una zona no lleva a ningún sitio

Abre **🗺 Escenas → Mapa de escenas**: marca con ⚠ las zonas y botones que
llevan a una escena que no existe. Revisa también que el **punto de entrada**
tenga exactamente el nombre que pide la acción.

## Mi guion no hace nada

- Pulsa **Comprobar** en la pestaña 📜 Guion para ver si hay errores.
- Mira la **consola**: ahí salen los errores al jugar.
- Revisa el nombre de la función: `al_hablar`, no `alHablar` ni `al_Hablar`.
- Añade un `print("aquí llego")` para ver si la función se llama.

## «El guion tarda demasiado»

Hay un bucle que no termina nunca (un `while true do` sin `break`, por
ejemplo). El motor lo corta para que el juego no se cuelgue.

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

> **Consejo.** Guarda tus proyectos en Git o en GitHub: como todo es texto,
> verás exactamente qué cambió y podrás volver atrás.
