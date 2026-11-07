# Objetos libres y jerarquía

Cada objeto de la escena es una pieza aparte: se dibuja con su propio modelo
y se puede **mover, girar y escalar como quieras**, en cualquier momento.
También puede ir **dentro de otro objeto**: una espada en la mano, una rueda
en un coche, una lámpara en una casa. Desde entonces se mueve con él.

## Mover, girar y escalar

Elige un objeto (con la herramienta *Elegir y mover*, <kbd>V</kbd>) y mira el
[Inspector](../interfaz/inspector.md). Debajo de sus comportamientos están
sus tres filas de números:

| Fila | Qué es |
|---|---|
| **Posición** | El centro de su base, en metros (`x`, `y` = altura, `z`) |
| **Giro** | En grados alrededor de cada eje. `y` es hacia dónde mira (0 = al sur); `x` y `z` lo inclinan |
| **Escala** | Cuánto más grande o más pequeño es en cada eje. 1 = como su modelo |

Arrastra un número a izquierda o derecha para cambiarlo, o haz doble clic y
escríbelo. Debajo:

- **⟲ ⟳** giran el objeto un paso (como <kbd>R</kbd>).
- **1:1** (encendido de serie) hace la escala **proporcional**: cambiar un
  eje cambia los tres por igual. Apágalo para estirar el objeto solo en un
  eje.
- **⊞ Imán** enciende o apaga el imán a la rejilla (ver abajo).
- **↺** quita el giro y la escala (sale cuando hay alguno).

También puedes **arrastrar** el objeto en la Vista: se apoya donde apuntas.

## El imán a la rejilla

El imán decide si las cosas van **a saltos** o **libres**. Se enciende y se
apaga con <kbd>G</kbd> o con el botón **⊞ Imán**.

| | Con imán (de serie) | Sin imán |
|---|---|---|
| Arrastrar o colocar | De cubito en cubito | Justo donde apuntas |
| <kbd>R</kbd> y ⟲ ⟳ | De 90° en 90° | De 15° en 15° |

Los números del Inspector siempre son libres: con o sin imán puedes escribir
`37.5` grados o una escala de `1.3`.

> <i class="fx fx-consejo"></i> **Consejo.** Construye con el imán encendido
> (todo encaja con el terreno) y apágalo para los detalles: una piedra un
> poco torcida, un cartel inclinado, un árbol un poco más grande que los
> demás.

## Objetos dentro de otros

En el panel [En la escena](../interfaz/escena.md), **arrastra un objeto y
suéltalo encima de otro**. Ahora va **dentro** de él: sale debajo, un poco
hacia la derecha, y su padre tiene una flecha **⏷** para plegar lo que lleva.

Lo que va dentro:

- se **mueve, gira y escala** con su padre, en el editor y jugando (si un
  comportamiento mueve o gira el coche, las ruedas van con él);
- se **esconde** cuando se esconde su padre;
- se **borra** con su padre (y <kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>Z</kbd>
  lo devuelve todo de una vez);
- se puede seguir moviendo por su cuenta: su sitio es suyo.

Para **sacarlo**: clic derecho → **⬆ Sacar de «…»**, el botón **Sacar** del
Inspector, o arrástralo a una carpeta o al hueco de abajo de la lista. Se
queda donde está.

Un objeto puede llevar otros que a su vez llevan otros (un coche → una
rueda → un tapacubos). Lo que no se puede es meter un objeto dentro de sí
mismo ni dentro de lo que lleva dentro: el editor no lo deja.

## Objetos vacíos

El **Objeto vacío** (en *Colocar objetos* → *Entidades del motor*) es solo un
punto: no se ve al jugar. Sirve para:

- **agrupar**: mete varios objetos dentro y mueve el grupo entero de una vez;
- **marcar un sitio**: donde aparece un enemigo, adonde va una plataforma;
- colgarle [componentes](entidades.md) y [comportamientos](comportamientos.md)
  sin modelo: una luz, un sonido, el personaje.

## Con qué se choca

Un objeto sólido choca, de serie, con **sus cubitos**: puedes entrar por la
puerta de una casa aunque esté girada o escalada. En el componente
[Colisión](../referencia/componentes/colision.md) puedes cambiar su
**Forma** por una **caja**, una **esfera** o una **cápsula** que llenan su
caja: más simple y más suave para subirse encima o rodar por ella.

## Cómo se guarda

En el archivo de la escena, cada objeto lleva su número (`id`), y los que
van dentro de otro dicen de cuál (`padre`). La posición, el giro y la escala
son siempre los de la escena, no respecto al padre, para que el archivo se
entienda solo:

```ron
(tipo: "casa", nombre: "Casa de Plumas", id: 1, pos: (86.0, 16.0, 118.0)),
(tipo: "farola", nombre: "Farola de la casa", id: 5, pos: (90.0, 16.0, 122.0),
 giro: (0.0, 0.0, 20.0), escala: (1.2, 1.2, 1.2), padre: 1),
```

Los proyectos de antes (con el giro en cuartos de vuelta, `giro: 1`) se
convierten solos al abrirlos, con una copia de seguridad en
`.foxy/copias/`.

## Véase también

- [Ordenar la escena](carpetas.md)
- [Entidades y componentes](entidades.md)
- [Colisión](../referencia/componentes/colision.md)
