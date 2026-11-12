# Tabla de rendimiento

Cuántos fotogramas por segundo (fps) dan las demostraciones en tres
ordenadores típicos, a **1920 × 1080** y con sus ajustes de serie. Por
encima de 60 fps se ve fluido; entre 30 y 60, bien; por debajo de 30, a
tirones.

| Demostración | Calidad | Triángulos | PC para juegos | Mac M2 | Portátil normal |
|---|---|---|---|---|---|
| La cueva | Ultra | 1,3 millones | ~200 | ~65 | ~25 |
| Valle enorme con físicas | Alta | 0,5 millones | ~215 | ~130 | ~50 |
| Laboratorio de físicas | Alta | pocos | ~280 | ~170 | ~65 |
| Juego de píxeles | (2D) | pocos | más de 60 | más de 60 | más de 60 |
| Demo técnica | Ultra | 41 millones | ~25 | ~10 | ~5 |

- **PC para juegos**: una gráfica como la GeForce RTX 3060.
- **Mac M2**: un MacBook Air M2.
- **Portátil normal**: gráfica integrada, como una Intel Iris Xe.

> <i class="fx fx-aviso"></i> **Importante.** Son estimaciones, no medidas
> en esos ordenadores. Salen de dos cosas que sí se midieron: lo que dibuja cada
> demostración (triángulos y llamadas de dibujo, con el modelo de la
> pestaña [Otros ordenadores](../guia/rendimiento.md#otros-ordenadores)) y
> lo que tarda cada fotograma, con toda la luz, en un ordenador de pruebas
> sin tarjeta gráfica (abajo), escalado según lo potente que es cada
> tarjeta. Pueden fallar por bastante. Si tienes uno de estos ordenadores,
> mide tú (ver *Medirlo en tu ordenador*) y compara.

## Lo que se midió

En el ordenador donde se hacen las capturas del manual (4 núcleos, sin
tarjeta gráfica: el dibujo lo hace el procesador), a 1920 × 1080:

| Demostración | Llamadas de dibujo | Milisegundos por fotograma |
|---|---|---|
| La cueva | 150 | 736 |
| Valle enorme con físicas | 249 | 381 |
| Laboratorio de físicas | 26 | 67 |
| Demo técnica | 1.236 | 5.518 |

Sirve para comparar unas con otras: la cueva gasta el doble que el valle
aunque es mucho más pequeña, porque casi todo su tiempo se va en la luz
(rayos en la bruma, luz que rebota, sombras de las antorchas, reflejos).

## Si va lenta

- Baja la **Calidad** en **Proyecto → Ajustes del proyecto… → Gráficos**
  (de Ultra a Alta o Media). En la cueva es lo que más se nota.
- En la **Demo técnica**, lo que pesa son los 41 millones de triángulos:
  pasa el [doctor de rendimiento](../guia/optimizar.md), que enciende
  **menos detalle de lejos** y baja mucho los triángulos.
- Mira qué gasta más con la ventana **Rendimiento**
  ([Rendimiento](../guia/rendimiento.md)).

## Medirlo en tu ordenador

1. Abre la demostración y pulsa **Desde el inicio**.
2. Cuando acabe el recorrido (en la cueva), pulsa <kbd>F3</kbd>.
3. Arriba de la ventana **Rendimiento** salen los fps en tu ordenador.
   Espera unos segundos quieto para que la cifra se asiente.

Desde la línea de órdenes, la misma medida sale en la consola (ver
[Línea de comandos](../referencia/linea-de-comandos.md)):

```sh
foxy-engine --captura prueba.png --editor --pestana cueva --jugar --esperar 3 --rendimiento --ancho 1920 --alto 1080
```
