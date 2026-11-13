# Personajes que andan

Un enemigo que persigue, un animal que patrulla o un vecino que pasea
tienen que **pisar el suelo y esquivar lo que hay en medio**. Para eso
está **Andar hacia**: el objeto anda hasta un destino como lo haría un
personaje de verdad.

| Qué hace | Cómo |
|---|---|
| Pisa el suelo | Cae si no hay suelo debajo y sigue el terreno al subir y bajar |
| Sube escalones | Los de medio metro los sube andando |
| Salta bordillos | Salta lo que mide hasta un metro de alto |
| Se deja caer | Baja de un salto alturas de hasta tres metros |
| Rodea las paredes | Busca un camino por donde cabe su cuerpo: puertas, pasillos y rampas |
| No se moja | No entra en el agua |
| No se amontona | Dos personajes que andan no se pisan: se apartan |

## Sin programar: los comportamientos ya hechos

**Seguir al jugador** y **Patrullar** ya andan así.

1. Elige el objeto que hará de personaje.
2. En el [Inspector](../interfaz/inspector.md), pulsa **➕ Comportamiento →
   Ya hechos → Seguir al jugador** (o **Patrullar**).
3. Pulsa **Jugar aquí**. El objeto anda por el suelo y rodea las paredes
   para llegar.

Para un fantasma, un pájaro o un dron, marca su valor **volando**: va en
línea recta por el aire y lo atraviesa todo.

> **Nota.** Los comportamientos se copian al proyecto al ponerlos. Un
> proyecto que ya tenía **Seguir al jugador** o **Patrullar** conserva los
> suyos, que van en línea recta. Para que anden, abre el grafo en el panel
> **Nodos** y cambia el nodo **Ir hacia** por **Andar hacia**, o borra el
> archivo de `grafos/` y vuelve a poner el comportamiento.

## Con nodos: Andar hacia

El nodo **Andar hacia** (categoría *Objetos*) se usa después de **Cada
fotograma**, igual que **Ir hacia**.

| Pin | Qué es |
|---|---|
| *objeto* | Quién anda. Vacío es *este objeto* |
| *destino* | A dónde va: un punto, o **Posición del jugador** para perseguirlo |
| *metros por segundo* | La velocidad. Una persona anda a 1,5 y corre a 4 |
| *ha llegado* | Sí cuando está en el destino o cuando no puede acercarse más |

Mientras el nodo se ejecuta, el objeto anda y mira hacia donde va. Cuando
deja de ejecutarse, se para. Si el suelo desaparece bajo sus pies, cae.

El [tutorial del enemigo que persigue](tutorial-enemigo.md) lo usa de
principio a fin.

## Con Lua: motor.andar_hacia

```lua
propiedades = {
  velocidad = 3,   -- metros por segundo
}

function cada_fotograma(segundos)
  if motor.andar_hacia(yo, "jugador", propiedades.velocidad) then
    motor.decir("Te tengo")
  end
end
```

`motor.andar_hacia(objeto, destino, velocidad)` devuelve `true` al llegar
o cuando no hay forma de acercarse más. El destino puede ser un vector, un
objeto o `"jugador"`.

## Andar hacia o Ir hacia

| | Andar hacia | Ir hacia |
|---|---|---|
| Camino | Por el suelo, rodeando lo que estorba | En línea recta |
| Paredes y suelo | Choca con ellos | Los atraviesa |
| Caer | Sí | No |
| Para | Personas, animales, enemigos, robots con patas | Fantasmas, pájaros, drones, balas, plataformas |

## Lo que conviene saber

- **El tamaño cuenta.** El cuerpo mide lo que el objeto. Uno ancho no
  pasa por una puerta estrecha, y uno alto no pasa bajo un techo bajo.
- **Con qué choca.** Con el terreno y con los objetos quietos de la
  escena. No choca con el jugador: para que se pare a su lado, usa el valor
  `distancia` de **Seguir al jugador**.
- **Si no puede llegar**, se acerca todo lo que puede y espera. Vuelve a
  buscar camino cuando el destino se mueve.
- **Lejos, busca menos.** El camino se busca en los alrededores del
  personaje. Si el destino queda detrás de un laberinto largo, va hasta el
  sitio más cercano que encuentra y sigue buscando desde allí.
- **Muchos a la vez.** Los caminos largos se reparten entre fotogramas,
  así que una manada no frena el juego.
- **En escenas 2D**, **Andar hacia** hace lo mismo que **Ir hacia**. En 2D,
  el suelo y la gravedad son cosa del
  [cuerpo de cada sprite](juegos-2d.md).
- **Con [físicas precisas](fisicas.md)**, da al personaje un cuerpo
  **Cinemático** para que empuje cajas al andar. Un cuerpo **Dinámico** lo
  mueve la física, no **Andar hacia**.

## Véase también

- [Comportamientos](comportamientos.md)
- [Tutorial: un enemigo que persigue](tutorial-enemigo.md)
- [Referencia de nodos](../referencia/nodos.md)
- [Referencia de Lua](../referencia/lua.md)
