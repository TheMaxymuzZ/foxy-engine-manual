# Sonidos

Un proyecto puede usar sus propios sonidos en formato **WAV** u **OGG**,
además de los sonidos de ejemplo que incluye el motor.

## Añadir sonidos

Arrastra los archivos a la ventana del editor o cópialos en la carpeta
`sonidos/` del proyecto. El nombre del archivo sin la extensión es el
nombre del sonido: `sonidos/campanario.ogg` se llama `campanario`.

## Usar un sonido

- **Desde una entidad**: añade el componente
  [Sonido](../referencia/componentes/sonido.md). El sonido sale de la
  entidad y se oye más fuerte cuanto más cerca está el jugador.
- **Con una acción**: la acción **Tocar un sonido** de una zona, un botón o
  un objeto. Ver [Acciones](../referencia/acciones.md).
- **Desde un guion**: `motor.sonar("campanario")`.

## Sonidos de ejemplo

`paso`, `salto`, `caida`, `patada`, `hablar`, `trueno`, `pajaro`, `campana`
y `clic`. Se generan en el propio motor y siempre están disponibles. Si un
sonido del proyecto se llama igual que uno de ejemplo, se usa el de ejemplo:
conviene darle otro nombre.

## Véase también

- [Componente Sonido](../referencia/componentes/sonido.md)
- [La vida del mundo](vida.md)
