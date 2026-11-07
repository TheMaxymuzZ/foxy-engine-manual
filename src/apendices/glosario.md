# Glosario

| Término | Qué significa |
|---|---|
| **Acción** | Lo que pasa al pulsar un botón, entrar en una zona o usar un objeto con <kbd>E</kbd>. Ver [Acciones](../referencia/acciones.md). |
| **Al usarlo (E)** | La acción de un objeto que el jugador usa mirándolo de cerca y pulsando <kbd>E</kbd>. |
| **Ancla** | El punto de la pantalla al que está pegado un elemento de una interfaz. |
| **Animación** | Lo que cambia con el tiempo en una entidad: posición, giro, escala, color, luz o fotograma. Se guarda en `animaciones/`. Ver [Animación](../guia/animacion.md). |
| **Animador** | El componente que dice qué animaciones usa una entidad, con su máquina de estados. Ver [Animador](../referencia/componentes/animador.md). |
| **Autocasilla** | Un terreno de casillas que pone solo sus bordes y esquinas al pintar. Ver [Mapas de casillas](../guia/casillas.md#autocasillas). |
| **Bloque** | Un cubo de 1 m, hecho de 2 × 2 × 2 cubitos. |
| **Cable** | La unión entre dos nodos. Los de ejecución marcan el orden y los de datos llevan un valor. Ver [Nodos](../guia/nodos.md#cables-y-tipos). |
| **Capa** | En una escena 2D, cada plano de casillas o de imagen que se dibuja uno encima de otro. Ver [Capas](../guia/casillas.md#capas). |
| **Casilla** | En 2D, cada cuadrito de un mapa de casillas, y la medida de las escenas 2D. Ver [Mapas de casillas](../guia/casillas.md). |
| **Cinemática** | Una escena corta que el jugador mira sin manejar, con la cámara y frases. Ver [Cinemáticas](../guia/cinematicas.md). |
| **Clave** | El valor de una propiedad en un segundo concreto de una animación. Entre dos claves, el motor rellena el camino. |
| **Componente** | Una pieza que dice lo que una entidad es: Luz, Zona, Controlador… Ver [Componentes](../referencia/componentes/index.md). |
| **Comportamiento** | Algo que hace un objeto por su cuenta, con un grafo de nodos o un guion Lua. Un objeto puede llevar varios, cada uno con sus valores; el motor trae diez ya hechos. Ver [Comportamientos](../guia/comportamientos.md). |
| **Coyote time** | Un momento después de salir de un borde en el que todavía se puede saltar. |
| **Cubito** | La pieza más pequeña del mundo. Mide 50 cm salvo que el proyecto elija otra [rejilla](../editor/ajustes-proyecto.md#rejilla-y-materiales). |
| **Curva** | Cómo se va de una clave a la siguiente: suave, lineal, rebotando, de golpe… Ver [Las curvas](../guia/animacion.md#las-curvas). |
| **Detalle de lejos** | Los trozos lejanos se dibujan con una forma más sencilla (cada casilla junta 2 × 2 × 2 cubitos) para que todo vaya más rápido. Ver [Rendimiento](../guia/rendimiento.md). |
| **Entidad** | Cualquier cosa colocada en una escena, con nombre, posición, giro, un modelo opcional y componentes. Ver [Conceptos básicos](../conceptos/basicos.md). |
| **Entrada (punto de)** | Un punto con nombre por donde se llega a una escena desde otra. |
| **Escena** | Un mundo dentro de un proyecto (la isla, una cueva…). Se guarda en `mundos/`. |
| **Escena inicial** | La escena donde empiezan las partidas nuevas (<i class="fx fx-estrella"></i>). |
| **Espacio (de trabajo)** | Un reparto de paneles para un trabajo: Construir, 2D, Programar, Pixel art, Animar o uno propio. Ver [Personalizar el espacio de trabajo](../editor/espacio-de-trabajo.md). |
| **Evento** | El nodo con el que empieza una cadena: al empezar, cada fotograma, al chocar… Ver [Eventos y flujo](../guia/nodos-flujo.md). |
| **Fotogramas por segundo (fps)** | Cuántas imágenes dibuja el motor cada segundo. Con 60 o más va suave; por debajo de 30 se notan tirones. |
| **Función (de nodos)** | Un grupo de nodos guardado en `funciones/` que se usa como un nodo más. Ver [Funciones](../guia/nodos-funciones.md). |
| **Generador** | Lo que crea el terreno de una escena: vacío, plano, isla, colinas o cuevas. Ver [Generadores de terreno](../guia/generadores.md). |
| **Grafo** | Un conjunto de nodos unidos con cables: del juego, de una escena o de una entidad. Ver [Nodos](../guia/nodos.md). |
| **Guion** | Un archivo de código Lua en `guiones/`. El guion del mundo es `mundo.lua`; los guiones de entidad son comportamientos de una entidad. Ver [Programar en Lua](../guia/programar-lua.md). |
| **Guion de entidad** | Un guion que lleva una entidad como comportamiento. Cada entidad tiene su propia copia. Ver [Guiones de entidad](../guia/guiones-entidad.md). |
| **Hoja de sprites** | Una imagen con varios fotogramas que se cortan para hacer animaciones. Ver [Sprites](../guia/sprites.md). |
| **Inspector** | El [panel](../interfaz/inspector.md) del editor con las opciones de la herramienta y de lo que tengas elegido. |
| **Interfaz** | Algo que se dibuja encima del juego: un menú, un marcador, un cartel. |
| **Juego de casillas** | Una imagen con todas las casillas con las que se pinta un mapa 2D. |
| **Juego publicado** | Una aplicación hecha con **Proyecto › Publicar…** que se abre con doble clic, sin el motor instalado. Ver [Publicar tu juego](../publicar/publicar.md). |
| **Llano** | Un terreno de hierba completamente plano, sin isla ni mar a la vista. Es el de un proyecto vacío. |
| **Máquina de estados** | Estados con su animación y flechas con condiciones que eligen la animación sola. Ver [Máquina de estados](../guia/animacion.md#máquina-de-estados). |
| **Marcador** | Una interfaz que está siempre a la vista mientras se juega. |
| **Material** | De qué está hecho un cubito: hierba, piedra, madera… |
| **Mipmaps** | Copias cada vez más pequeñas de una textura, que se usan de lejos para que no parpadee. |
| **Módulo** | Una parte del motor que el proyecto activa o desactiva. Ver [Módulos](../referencia/modulos/index.md). |
| **Módulo (de Lua)** | Un guion que devuelve funciones para otros guiones, que lo cargan con `require`. |
| **Nine-slice (estirar en nueve partes)** | Forma de estirar una imagen sin deformar sus esquinas. |
| **Nodo** | Una caja de un grafo que hace una sola cosa. Ver la [Referencia de nodos](../referencia/nodos.md). |
| **Objeto propio** | Un objeto hecho con el creador de objetos, guardado en `objetos/`. |
| **Ortográfica (cámara)** | Una cámara sin perspectiva: lo lejano se ve igual de grande que lo cercano. |
| **Paleta** | Una lista de colores para dibujar en pixel art. |
| **Paleta de comandos** | La búsqueda de <kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>K</kbd>: escribe lo que quieres hacer o abrir. |
| **Panel** | Cada parte del editor (Vista, Proyecto, Inspector, Código…). Se mueve, se junta en pestañas, se maximiza o se separa en otra ventana. Ver [La interfaz del editor](../empezar/editor.md#los-paneles). |
| **Panel «Proyecto»** | El [panel](../interfaz/proyecto.md) del editor con las escenas, interfaces, objetos, imágenes y el guion del proyecto. |
| **Pantalla de carga** | La imagen que sale al abrir un juego publicado, antes de «Powered by Foxy Engine». |
| **Pantalla de inicio** | Lo primero que muestra el motor al abrirse: la lista de proyectos, las plantillas, los accesos al manual y las novedades. Ver [La pantalla de inicio](../empezar/pantalla-de-inicio.md). |
| **Paquete (del juego)** | El archivo `juego.foxy` que va con un juego publicado: los archivos del proyecto que el juego usa, comprimidos. |
| **Paralaje** | Cuánto se mueve una capa con la cámara. Las capas lejanas se mueven menos y dan sensación de profundidad. |
| **Partículas** | Puntos pequeños que salen de una entidad: polvo, chispas, lluvia, nieve, humo u hojas. |
| **Pieza** | Una caja de cubitos de un objeto que se anima por separado, con su punto de giro. Ver [Personajes por piezas](../guia/personajes-piezas.md). |
| **Pincel** | La forma (cubo o esfera) y el tamaño con los que se ponen, quitan o pintan bloques. |
| **Pista** | En una animación, la fila que cambia una propiedad de una cosa (el giro de la hoja, la posición de la cámara…). |
| **Pixel perfect** | Cada píxel del juego ocupa un número entero de píxeles de la pantalla, para que el pixel art se vea nítido. |
| **Plantilla** | El punto de partida de un proyecto nuevo: Vacío 3D, Isla vóxel, Isla de ejemplo, Personaje animado, Vacío 2D, Plataformas 2D, Aventura cenital o Plataformas vóxel. Ver [Crear un proyecto](../empezar/crear-proyecto.md). |
| **Prefabricado** | Una entidad guardada como recurso; sus copias siguen al original. Ver [Prefabricados](../guia/entidades.md#prefabricados). |
| **Propiedad (de un guion)** | Un valor de la tabla `propiedades` de un guion de entidad, que se ajusta en el inspector de cada entidad. |
| **Proyecto** | La carpeta de un juego, con todas sus escenas, objetos, imágenes e interfaces. |
| **Punto de parada** | Un nodo o una línea de un guion marcados para que el juego se detenga justo antes de ejecutarlos. Ver [Depurar los nodos](../guia/nodos-depurar.md#puntos-de-parada) y [el depurador de Lua](../guia/lua-depurar.md#el-depurador). |
| **Recarga en caliente** | Volver a cargar un guion al guardarlo, con el juego en marcha y sin reiniciar. |
| **Registro** | El [panel](../interfaz/registro.md) con todos los avisos del editor; y el archivo `registro.txt`, donde el motor apunta lo que hace al abrirse y los errores. |
| **RON** | El formato de texto de los archivos `.ron` de Foxy Engine. |
| **Sprite** | La imagen con la que se ve una entidad 2D. Ver [Sprites](../guia/sprites.md). |
| **Suceso** | Algo que pasa en un segundo de una animación: un sonido, partículas, un aviso a los nodos o una frase. |
| **Trozo** | Un pedazo del mundo de 32 × 32 × 32 cubitos. El motor dibuja y actualiza el mundo por trozos. |
| **Valor** | Un dato con nombre que pone el guion (`motor.poner_valor`) y que se guarda con la partida. |
| **Variable** | Un valor con nombre de un grafo, de una entidad o del juego. Ver [Nodos](../guia/nodos.md#variables). |
| **Vecino** | Un habitante del mundo que pasea y habla. |
| **Vista** | El [panel](../interfaz/vista.md) con la escena en 3D. Se puede separar en otra ventana, por ejemplo en otro monitor. |
| **Zona de cambio** | Un marco invisible al jugar que hace una acción al entrar en él. |
