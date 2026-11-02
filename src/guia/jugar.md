# Probar el juego

Hay dos maneras de probar lo que haces, y una tercera para abrir solo el
juego.

| | Qué hace | Para qué |
|---|---|---|
| **▶ Jugar aquí** (<kbd>F5</kbd>) | Te pone de pie donde mira la cámara. <kbd>F5</kbd> vuelve al editor, justo donde estabas | Probar algo al momento |
| **🎮 Desde el inicio** | Abre el juego completo, con su menú principal, en el punto de inicio de la escena inicial | Probar el juego como lo verá quien lo juegue |
| `foxy-engine --juego` | Solo el juego, sin editor | Así será el juego exportado (Fase 6) |

| Menú principal | Jugando | Pausa |
|---|---|---|
| ![Inicio](../imagenes/capturas/fase3-inicio.png) | ![Jugando](../imagenes/capturas/fase3-jugando.png) | ![Pausa](../imagenes/capturas/fase3-pausa.png) |

## Controles

| Acción | Teclado y ratón | Mando (Xbox / PlayStation) |
|---|---|---|
| Andar | <kbd>W</kbd> <kbd>A</kbd> <kbd>S</kbd> <kbd>D</kbd> o flechas | Stick izquierdo |
| Mirar | Ratón | Stick derecho |
| Correr | <kbd>Mayús</kbd> | Stick a fondo, L3 o gatillo izquierdo |
| Saltar (y nadar hacia arriba) | <kbd>Espacio</kbd> | A / ✕ |
| Agacharse | <kbd>C</kbd> o <kbd>Ctrl</kbd> | B / ○ o R3 |
| Patear una pelota, hablar | <kbd>E</kbd> o clic | X / □ o gatillo derecho |
| Menú de pausa | <kbd>Esc</kbd> | Start |
| Moverse por los menús | Flechas, <kbd>Intro</kbd>, <kbd>Esc</kbd> o el ratón | Cruceta o stick, A, B |

## Física

- Los escalones de medio metro se suben solos.
- Agachado no te caes por los bordes.
- Se puede saltar un instante después de salir de un borde.
- Las **pelotas** caen, botan, ruedan, flotan en el agua, chocan entre ellas y
  se empujan al andar contra ellas.

## El punto de inicio

El objeto **Punto de inicio** marca dónde empieza una partida nueva, mirando
hacia donde apunta su flecha. Solo se ve en el editor. Si una escena tiene
[puntos de entrada](escenas.md#puntos-de-entrada), se llega a ellos desde
otras escenas.

## Partidas guardadas

- **Tres ranuras** y una **automática**, que se guarda cada dos minutos y al
  salir.
- **Continuar** carga la partida más reciente.
- Cada partida guarda la escena, la posición del jugador, la hora, el día, el
  clima, la estación, las pelotas y los valores del guion.
- Son archivos de texto en la carpeta `partidas/<escena>/` del proyecto
  (`ranura_1.ron`, `ranura_2.ron`, `ranura_3.ron` y `auto.ron`).

## Opciones

En el menú **Opciones**:

- Sensibilidad del ratón y del mando.
- Invertir arriba/abajo.
- Campo de visión.
- Balanceo al caminar.
- Mostrar los fotogramas por segundo.
- Volumen de la música y de los efectos.

Se guardan para todas las partidas en `Documentos/Foxy Engine/ajustes.ron`.
