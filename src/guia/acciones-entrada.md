# Acciones de entrada

El juego no pregunta por teclas concretas sino por **acciones de entrada**:
*Adelante*, *Saltar*, *Usar*. Cada proyecto decide qué tecla, qué botón del
ratón y qué botón del mando activa cada una. Así, el mismo juego se maneja
con teclado o con mando sin cambiar nada más, y los guiones pueden reaccionar
a acciones propias como *Disparar* o *Abrir el mapa*.

## Editar el mapa de acciones

Abre **Proyecto → Ajustes del proyecto… → Acciones de entrada**.

- Para añadir una tecla, pulsa **+ tecla** y luego la tecla.
  <kbd>Esc</kbd> cancela.
- Para quitar una tecla, haz clic sobre ella.
- El botón del ratón abre la lista de botones del ratón, y el del mando la
  de botones del mando.
- **Acción nueva** añade una acción propia; escribe su nombre en la lista.
- **Las de siempre** devuelve a las acciones del motor sus teclas de
  fábrica. Las propias no cambian.

Los cambios se guardan en `acciones.ron` al pulsar **Guardar**.

## Acciones del motor

No se pueden borrar ni renombrar, pero sí cambiar sus teclas.

| Acción | De fábrica |
|---|---|
| Adelante, Atrás, Izquierda, Derecha | <kbd>W</kbd> <kbd>S</kbd> <kbd>A</kbd> <kbd>D</kbd>, flechas y cruceta |
| Saltar | <kbd>Espacio</kbd>, botón sur del mando |
| Correr | <kbd>Mayús</kbd>, clic del stick izquierdo o gatillo izquierdo |
| Agacharse | <kbd>C</kbd> o <kbd>Control</kbd>, botón este del mando |
| Usar | <kbd>E</kbd> o clic izquierdo, botón oeste o gatillo derecho |
| Golpear | Clic izquierdo, gatillo derecho o botón oeste |
| Girar a la izquierda o a la derecha, Mirar arriba o abajo | Las teclas de las preferencias; en el mando, el stick derecho |

## Acciones propias en los guiones

```lua
function al_pulsar(nombre)
  if nombre == "Disparar" then
    motor.sonar("disparo")
  end
end

function cada_segundo()
  if motor.accion("Correr") then
    motor.decir("¡Corriendo!")
  end
end
```

| Función | Descripción |
|---|---|
| `al_pulsar(nombre)` | El motor la llama al pulsar una acción propia |
| `motor.accion(nombre)` | `true` mientras la acción está pulsada |
| `motor.accion_pulsada(nombre)` | `true` solo en el momento de pulsarla |

## En el archivo

```ron
[
    (nombre: "Saltar", teclas: ["Space"], mando: [Sur]),
    (nombre: "Disparar", teclas: ["F"], raton: [Izquierdo], mando: [RT]),
]
```

> <i class="fx fx-nota"></i> **Nota.** Un proyecto sin `acciones.ron` usa las
> teclas de las preferencias del editor. Las acciones del motor que falten
> en el archivo se añaden con sus teclas de fábrica.

## Véase también

- [API de Lua](../referencia/lua.md)
- [Preferencias y teclas](preferencias.md)
