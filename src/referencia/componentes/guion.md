# Guion

Llama a funciones del guion del mundo (`guiones/mundo.lua`) para esta
entidad. Cada función recibe el nombre de la entidad.

| Propiedad | Campo | Descripción |
|---|---|---|
| Al empezar | `al_empezar` | Función que se llama al empezar la partida |
| Cada segundo | `cada_segundo` | Función que se llama una vez por segundo |

```ron
Guion((al_empezar: "preparar_cofre", cada_segundo: "brillar"))
```

```lua
function brillar(nombre)
  if motor.hora() > 20 then motor.mostrar(nombre) else motor.ocultar(nombre) end
end
```

Ver [API de Lua](../lua.md).

## Véase también

- [Componentes](index.md)
- [Entidades y componentes](../../guia/entidades.md)
