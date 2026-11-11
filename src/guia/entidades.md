# Objetos y componentes

Esta guía explica cómo dar comportamiento a los objetos de una escena con
componentes y cómo reutilizarlas. Los conceptos se
describen en [Conceptos básicos](../conceptos/basicos.md).

![Una puerta con el componente Zona en el inspector](../imagenes/capturas/entidades.png)

> <i class="fx fx-consejo"></i> **Consejo.** Los componentes dicen lo que
> un objeto **es** (una luz, un cuerpo que cae, una zona). Para lo que
> **hace** por su cuenta (perseguir, girar, abrirse con un botón), usa
> [comportamientos](comportamientos.md).

## Añadir y quitar componentes

1. Con la herramienta <i class="fx fx-cursor"></i> **Elegir**, haz clic en
   un objeto de la Vista o en el panel **En la escena**.
2. En el [Inspector](../interfaz/inspector.md), pulsa
   <i class="fx fx-mas"></i> **Añadir componente** y elige uno de la lista.
   Las clases que el objeto ya tiene aparecen desactivadas.
3. Ajusta sus valores. Los cambios se ven al momento y se deshacen con
   <kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>Z</kbd>.
4. Para quitarlo, pulsa <i class="fx fx-borrar"></i> **Quitar** al final del
   componente.

Para un objeto que no debe verse al jugar (un punto de luz, un altavoz, el
personaje cuando se juega en primera persona), usa el objeto **Objeto vacío**
de la paleta de **Colocar objetos**.

## Ejemplo: una puerta que se abre al acercarse

Este ejemplo no necesita código ni la plantilla Isla.

1. Crea un proyecto con la plantilla **Vacío 3D**.
2. Añade el objeto de ejemplo **Puerta**: en la paleta de objetos, pulsa
   **Añadir los objetos de ejemplo** y coloca una puerta.
3. Ponle de nombre «Puerta».
4. Añade el componente **Zona**. Deja el tamaño en 4 × 3 × 4 m.
5. En **Al entrar**, elige **Mover un objeto**, deja *Objeto* vacío (la
   propia puerta) y escribe en *Cuánto* `x 1`: la puerta se desplazará un
   metro hacia un lado en 0,4 segundos.
6. En **Al salir**, elige otra vez **Mover un objeto** con `0, 0, 0`: la
   puerta vuelve a su sitio.
7. Pulsa <i class="fx fx-jugar"></i> **Jugar aquí** y acércate.

> <i class="fx fx-consejo"></i> **Consejo.** El desplazamiento siempre se
> cuenta desde la posición que el objeto tiene en el editor. Por eso
> `0, 0, 0` significa «volver a su sitio» y la misma zona sirve para abrir
> y cerrar.

## Ejemplo: un personaje en tercera persona

1. Coloca una **Objeto vacío** (o cualquier objeto que quieras que sea el
   personaje) y llámala «Héroe».
2. Añade el componente **Controlador de jugador** y elige
   **Tipo: Tercera persona**.
3. Si quieres, añade **Cámara** para cambiar la distancia y la altura.
4. Al jugar, la partida empieza en ese objeto y la cámara va detrás del
   personaje.

![Un personaje en tercera persona](../imagenes/capturas/tercera-persona.png)

Si la escena no tiene ningún objeto con controlador, el juego empieza en
el **Punto de inicio** en primera persona, como en versiones anteriores.

## Objetos que se mueven o se esconden

Las acciones **Mover un objeto**, **Ocultar un objeto** y **Mostrar un
objeto** (ver [Acciones](../referencia/acciones.md)) y las funciones
`motor.mover`, `motor.ocultar` y `motor.mostrar` de los
[guiones](../referencia/lua.md) cambian los objetos **solo durante la
partida**. Al volver al editor, todo está como se dejó.

Mientras un objeto se mueve, se dibuja aparte del mundo; al detenerse
vuelve a formar parte de los cubitos, y se puede chocar con ella en su
nueva posición.

## Objetos reutilizables

Un objeto (con lo que lleva dentro) se puede guardar como **objeto
reutilizable** para colocarla muchas veces; sus copias siguen al original.
Se explica en [Objetos reutilizables](reutilizables.md).

## Véase también

- [Comportamientos](comportamientos.md): lo que hace cada objeto, con nodos o con código.
- [Referencia de componentes](../referencia/componentes/index.md)
- [Acciones](../referencia/acciones.md)
- [Objetos reutilizables](reutilizables.md)
