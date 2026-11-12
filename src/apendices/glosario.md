# Glosario

| Término | Qué significa |
|---|---|
| **Acción** | Lo que pasa al pulsar un botón, entrar en una zona o usar un objeto con <kbd>E</kbd>. Ver [Acciones](../referencia/acciones.md). |
| **Al usarlo (E)** | La acción de un objeto que el jugador usa mirándolo de cerca y pulsando <kbd>E</kbd>. |
| **Ancla** | El punto de la pantalla al que está pegado un elemento de una interfaz. |
| **Animación** | Lo que cambia con el tiempo en un objeto: posición, giro, escala, color, luz o fotograma. Se guarda en `animaciones/`. Ver [Animación](../guia/animacion.md). |
| **Animador** | El componente que dice qué animaciones usa un objeto, con su máquina de estados. Ver [Animador](../referencia/componentes/animador.md). |
| **Autocasilla** | Un terreno de casillas que pone solo sus bordes y esquinas al pintar. Ver [Mapas de casillas](../guia/casillas.md#autocasillas). |
| **Bloque** | Un cubo de 1 m, hecho de 2 × 2 × 2 cubitos. |
| **Cable** | La unión entre dos nodos. Los de ejecución marcan el orden y los de datos llevan un valor. Ver [Nodos](../guia/nodos.md#cables-y-tipos). |
| **Calidad (de los gráficos)** | Bajo, Medio, Alto, Ultra o Cine: lo finas que son las sombras y cuántas luces hay a la vez. Ver [Gráficos](../guia/graficos.md#calidad). |
| **Capa** | En una escena 2D, cada plano de casillas o de imagen que se dibuja uno encima de otro. Ver [Capas](../guia/casillas.md#capas). |
| **Casilla** | En 2D, cada cuadrito de un mapa de casillas, y la medida de las escenas 2D. Ver [Mapas de casillas](../guia/casillas.md). |
| **Cinemática** | Una escena corta que el jugador mira sin manejar, con la cámara y frases. Ver [Cinemáticas](../guia/cinematicas.md). |
| **Clave** | El valor de una propiedad en un segundo concreto de una animación. Entre dos claves, el motor rellena el camino. |
| **Componente** | Una pieza que dice lo que un objeto es: Luz, Zona, Controlador… Ver [Componentes](../referencia/componentes/index.md). |
| **Comportamiento** | Algo que hace un objeto por su cuenta, con un grafo de nodos o un guion Lua. Un objeto puede llevar varios, cada uno con sus valores; el motor trae once ya hechos. Ver [Comportamientos](../guia/comportamientos.md). |
| **Coyote time** | Un momento después de salir de un borde en el que todavía se puede saltar. |
| **Cubito** | La pieza más pequeña del mundo. Mide 50 cm salvo que el proyecto elija otra [rejilla](../editor/ajustes-proyecto.md#rejilla-y-materiales). |
| **Curva** | Cómo se va de una clave a la siguiente: suave, lineal, rebotando, de golpe… Ver [Las curvas](../guia/animacion.md#las-curvas). |
| **Detalle de lejos** | Los trozos lejanos se dibujan con una forma más sencilla (cada casilla junta 2 × 2 × 2 cubitos) para que todo vaya más rápido. Ver [Rendimiento](../guia/rendimiento.md). |
| **Entrada (punto de)** | Un punto con nombre por donde se llega a una escena desde otra. |
| **Escena** | Un mundo dentro de un proyecto (la isla, una cueva…). Se guarda en `mundos/`. |
| **Escena inicial** | La escena donde empiezan las partidas nuevas (<i class="fx fx-estrella"></i>). |
| **Espacio (de trabajo)** | Un reparto de paneles para un trabajo: Construir, 2D, Programar, Pixel art, Animar o uno propio. Ver [Personalizar el espacio de trabajo](../editor/espacio-de-trabajo.md). |
| **Evento** | El nodo con el que empieza una cadena: al empezar, cada fotograma, al chocar… Ver [Eventos y flujo](../guia/nodos-flujo.md). |
| **Exposición** | Cuánta luz deja pasar el motor a la imagen, como en una cámara: +1 es el doble. Ver [Gráficos](../guia/graficos.md#exposición). |
| **Fotogramas por segundo (fps)** | Cuántas imágenes dibuja el motor cada segundo. Con 60 o más va suave; por debajo de 30 se notan tirones. |
| **Función (de nodos)** | Un grupo de nodos guardado en `funciones/` que se usa como un nodo más. Ver [Funciones](../guia/nodos-funciones.md). |
| **Generador** | Lo que crea el terreno de cubitos de una escena: vacío, plano, colinas, cuevas, islas o una imagen de alturas. Ver [El terreno de cubitos](../guia/generadores.md). |
| **glTF** | El formato más común para modelos 3D: `.glb` (todo en un archivo) o `.gltf` (con su `.bin` y sus imágenes). Ver [Modelos 3D](../guia/modelos-3d.md). |
| **Grafo** | Un conjunto de nodos unidos con cables: del juego, de una escena o de un objeto. Ver [Nodos](../guia/nodos.md). |
| **Guion** | Un archivo de código Lua en `guiones/`. El guion del mundo es `mundo.lua`; los guiones de objeto son comportamientos de un objeto. Ver [Programar en Lua](../guia/programar-lua.md). |
| **Guion de objeto** | Un guion que lleva un objeto como comportamiento. Cada objeto tiene su propia copia. Ver [Guiones de objeto](../guia/guiones-entidad.md). |
| **HDR (luz de verdad)** | El motor calcula la luz sin límite (el sol puede ser mil veces más fuerte que una vela) y al final la pasa a colores de pantalla con el tono. |
| **Hoja de sprites** | Una imagen con varios fotogramas que se cortan para hacer animaciones. Ver [Sprites](../guia/sprites.md). |
| **Inspector** | El [panel](../interfaz/inspector.md) del editor con las opciones de la herramienta y de lo que tengas elegido. |
| **Interfaz** | Algo que se dibuja encima del juego: un menú, un marcador, un cartel. |
| **Juego de casillas** | Una imagen con todas las casillas con las que se pinta un mapa 2D. |
| **Juego publicado** | Una aplicación hecha con **Proyecto › Publicar…** que se abre con doble clic, sin el motor instalado. Ver [Publicar tu juego](../publicar/publicar.md). |
| **Llano** | Un terreno de hierba completamente plano, sin isla ni mar a la vista. Es el de un proyecto vacío. |
| **Luz del sol** | El componente que pone la hora del sol, su fuerza y su color. Ver [Luz del sol](../referencia/componentes/sol.md). |
| **Luz que rebota** | La luz del sol que rebota en el terreno y aclara lo que está a la sombra; también deja a oscuras las cuevas cerradas. Ver [Gráficos](../guia/graficos.md#luz-y-atmósfera). |
| **Máquina de estados** | Estados con su animación y flechas con condiciones que eligen la animación sola. Ver [Máquina de estados](../guia/animacion.md#máquina-de-estados). |
| **Marcador** | Una interfaz que está siempre a la vista mientras se juega. |
| **Material** | De qué está hecho un cubito: hierba, piedra, madera… |
| **Mipmaps** | Copias cada vez más pequeñas de una textura, que se usan de lejos para que no parpadee. |
| **Modelo 3D** | Un modelo de triángulos hecho en otro programa (Blender, Blockbench…), en glTF u OBJ, que se coloca como cualquier objeto. Ver [Modelos 3D](../guia/modelos-3d.md). |
| **Modo Avanzado** | El modo del editor con todos los paneles: código, consola, depurador, espacios de trabajo… Ver [Modo Sencillo y Avanzado](../empezar/modo-sencillo.md). |
| **Modo Sencillo** | El modo del editor para empezar: solo la escena, el panel Proyecto, la lista de la escena y el inspector. Ver [Modo Sencillo y Avanzado](../empezar/modo-sencillo.md). |
| **Módulo** | Una parte del motor que el proyecto activa o desactiva. Ver [Módulos](../referencia/modulos/index.md). |
| **Módulo (de Lua)** | Un guion que devuelve funciones para otros guiones, que lo cargan con `require`. |
| **Niebla** | El componente que llena la escena de niebla. Donde le da el sol salen rayos de luz. Ver [Niebla](../referencia/componentes/niebla.md). |
| **Nine-slice (estirar en nueve partes)** | Forma de estirar una imagen sin deformar sus esquinas. |
| **Nodo** | Una caja de un grafo que hace una sola cosa. Ver la [Referencia de nodos](../referencia/nodos.md). |
| **OBJ** | Un formato sencillo de modelos 3D: el `.obj` con la forma y el `.mtl` con los materiales. Ver [Modelos 3D](../guia/modelos-3d.md). |
| **Objeto** | Cualquier cosa colocada en una escena, con nombre, posición, giro, un modelo opcional, componentes y comportamientos. En versiones antiguas del manual se llamaba *entidad*. Ver [Conceptos básicos](../conceptos/basicos.md). |
| **Objeto propio** | Un objeto hecho con el creador de objetos, guardado en `objetos/`. |
| **Oclusión ambiental** | Que los rincones y las juntas reciban menos luz. En los ajustes se llama «Rincones más oscuros». |
| **Ortográfica (cámara)** | Una cámara sin perspectiva: lo lejano se ve igual de grande que lo cercano. |
| **Paleta** | Una lista de colores para dibujar en pixel art. |
| **Paleta de comandos** | La búsqueda de <kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>K</kbd>: escribe lo que quieres hacer o abrir. |
| **Panel** | Cada parte del editor (Vista, Proyecto, Inspector, Código…). Se mueve, se junta en pestañas, se maximiza o se separa en otra ventana. Ver [La interfaz del editor](../empezar/editor.md#los-paneles). |
| **Panel «Proyecto»** | El [panel](../interfaz/proyecto.md) del editor con las escenas, interfaces, objetos, imágenes y el guion del proyecto. |
| **Pantalla de carga** | La imagen que sale al abrir un juego publicado, antes de «Powered by Foxy Engine». |
| **Pantalla de inicio** | Lo primero que muestra el motor al abrirse: la lista de proyectos, las plantillas, los accesos al manual y las novedades. Ver [La pantalla de inicio](../empezar/pantalla-de-inicio.md). |
| **Paquete (del juego)** | El archivo `juego.foxy` que va con un juego publicado: los archivos del proyecto que el juego usa, comprimidos. |
| **Paralaje** | Cuánto se mueve una capa con la cámara. Las capas lejanas se mueven menos y dan sensación de profundidad. |
| **Partículas** | Puntos pequeños que salen de un objeto: polvo, chispas, lluvia, nieve, humo u hojas. |
| **PBR (materiales)** | Materiales que imitan los de verdad: color, relieve, rugosidad, metal, oclusión y brillo. Los mismos que Blender. Ver [Gráficos](../guia/graficos.md#materiales-de-los-modelos-pbr). |
| **Perfilador** | La pestaña *Qué gasta más* de la ventana Rendimiento: cuánto tiempo de cada fotograma se va en cada parte del motor y en cada objeto. Ver [Rendimiento](../guia/rendimiento.md#qué-gasta-más-el-perfilador). |
| **Pieza** | Una caja de cubitos de un objeto que se anima por separado, con su punto de giro. Ver [Personajes por piezas](../guia/personajes-piezas.md). |
| **Pincel** | La forma (cubo o esfera) y el tamaño con los que se ponen, quitan o pintan bloques. |
| **Pista** | En una animación, la fila que cambia una propiedad de una cosa (el giro de la hoja, la posición de la cámara…). |
| **Pixel perfect** | Cada píxel del juego ocupa un número entero de píxeles de la pantalla, para que el pixel art se vea nítido. |
| **Plantilla** | Con qué empieza un proyecto nuevo: un folio en blanco o un ejemplo de un tipo de juego (plataformas, vista desde arriba, tercera persona, puzle, mundo de cubitos). Ver [Crear un proyecto](../empezar/crear-proyecto.md) y [Tu primer juego](../tu-primer-juego/index.md). |
| **Prefabricado** | El nombre de antes de los [objetos reutilizables](../guia/reutilizables.md). |
| **Propiedad (de un guion)** | Un valor de la tabla `propiedades` de un guion de objeto, que se ajusta en el inspector de cada objeto. |
| **Proyecto** | La carpeta de un juego, con todas sus escenas, objetos, imágenes e interfaces. |
| **Punto de parada** | Un nodo o una línea de un guion marcados para que el juego se detenga justo antes de ejecutarlos. Ver [Depurar los nodos](../guia/nodos-depurar.md#puntos-de-parada) y [el depurador de Lua](../guia/lua-depurar.md#el-depurador). |
| **Recarga en caliente** | Volver a cargar un guion al guardarlo, con el juego en marcha y sin reiniciar. |
| **Registro** | El [panel](../interfaz/registro.md) con todos los avisos del editor; y el archivo `registro.txt`, donde el motor apunta lo que hace al abrirse y los errores. |
| **Reutilizable (objeto)** | Un objeto guardado, con lo que lleva dentro, para colocarlo muchas veces. Sus copias siguen al original salvo lo cambiado a mano en cada una; sus **partes** son lo que lleva dentro. Ver [Objetos reutilizables](../guia/reutilizables.md). |
| **RON** | El formato de texto de los archivos `.ron` de Foxy Engine. |
| **Sprite** | La imagen con la que se ve un objeto 2D. Ver [Sprites](../guia/sprites.md). |
| **Suavizado temporal** | Quitar los dientes de sierra de los bordes mezclando cada fotograma con el anterior. |
| **Suceso** | Algo que pasa en un segundo de una animación: un sonido, partículas, un aviso a los nodos o una frase. |
| **Terreno de cubitos** | El objeto que lleva el suelo de cubitos de una escena y su generador. Una escena lleva uno o ninguno. Ver [El terreno de cubitos](../guia/generadores.md). |
| **Tono** | La curva que pasa la luz a los colores de la pantalla: Cine, Como Blender, Neutro o Ninguno. Ver [Gráficos](../guia/graficos.md#tono). |
| **Trozo** | Un pedazo del mundo de 32 × 32 × 32 cubitos. El motor dibuja y actualiza el mundo por trozos. |
| **Tutorial guiado** | Los pasos que enseñan el editor la primera vez que se abre un proyecto. Se repite en **Ayuda › Tutorial guiado**. |
| **Valor** | Un dato con nombre que pone el guion (`motor.poner_valor`) y que se guarda con la partida. |
| **Variable** | Un valor con nombre de un grafo, de un objeto o del juego. Ver [Nodos](../guia/nodos.md#variables). |
| **Vecino** | Un habitante del mundo que pasea y habla. |
| **Vista** | El [panel](../interfaz/vista.md) con la escena en 3D. Se puede separar en otra ventana, por ejemplo en otro monitor. |
| **Zona de cambio** | Un marco invisible al jugar que hace una acción al entrar en él. |
