# Funciones, bibliotecas y nodos en Lua

Cuando un grupo de nodos se repite, conviértelo en una **función**: un
nodo nuevo que aparece en la paleta y se usa como cualquier otro. Las
funciones se pueden llevar de un proyecto a otro como **bibliotecas**. Y si
programas en Lua, puedes escribir **nodos en Lua** para que otras personas
del equipo los usen sin ver el código.

## Funciones hechas con nodos

Una función es un grafo guardado en `funciones/<nombre>.nodos.ron`. Empieza
en el nodo **Entrada**, que trae lo que recibe, y acaba en **Devolver**,
que entrega lo que devuelve.

### Crear una función desde una selección

La forma más rápida es partir de nodos que ya funcionan:

1. Elige los nodos que quieres convertir (sin eventos), con un recuadro o
   con <kbd>Mayús</kbd>+clic.
2. Pulsa **Pasar a función** en la barra del panel.
3. Los nodos pasan a una función nueva de `funciones/` y en su lugar queda
   un nodo que la llama, con los mismos cables. Cada dato que entraba desde
   fuera se convierte en una entrada de la función, y cada dato que salía,
   en una salida.

La selección debe tener una sola entrada y una sola salida de ejecución.
Las variables **del grafo** no existen dentro de una función: pásalas como
entrada, o cámbialas a variables de la entidad.

### Crear una función vacía

Pulsa <i class="fx fx-mas"></i> **Función** en la lista de grafos. La
función nueva ya trae *Entrada* unida a *Devolver*. En el grupo
**La función** de la izquierda:

- **Nombre** es el título del nodo en la paleta, y la descripción, su ayuda.
- **Recibe** y **Devuelve** son sus parámetros: añade cada uno con su
  nombre y su tipo. Aparecen como pines en *Entrada* y *Devolver*, y en el
  nodo que la llama.

Guarda la función y estará en la categoría **Funciones** de la paleta de
todos los grafos del proyecto.

> <i class="fx fx-nota"></i> **Nota.** Una función se ejecuta dentro de la
> cadena que la llama. Por eso puede usar **Esperar**, y **Esta entidad**
> es la entidad del grafo que la llama.

## Bibliotecas

Una biblioteca es simplemente una carpeta con funciones y nodos en Lua.
Para usar las de otro proyecto:

1. Pulsa **Importar** en la lista de grafos.
2. Elige la carpeta de otro proyecto, o una carpeta suelta con archivos
   `.nodos.ron` y `.lua`.
3. Se copian las funciones a `funciones/` y los nodos en Lua a `nodos/`.
   Lo que ya existe con el mismo nombre no se sobrescribe.

Para compartir tus funciones, comparte la carpeta `funciones/` (y `nodos/`
si las funciones usan nodos en Lua).

## Nodos en Lua

Un nodo en Lua es un archivo `nodos/<nombre>.lua` con una cabecera de
comentarios que lo describe. Pulsa <i class="fx fx-mas"></i> **Nodo en Lua**
en la lista para crear uno de ejemplo:

```lua
-- @nodo Tirar un dado
-- @categoria Matemáticas
-- @ayuda Un número al azar entre 1 y las caras del dado.
-- @entrada caras numero 6
-- @salida resultado numero
-- @puro
return function(caras)
  return motor.aleatorio(1, caras)
end
```

| Línea | Qué indica |
|---|---|
| `@nodo <título>` | El nombre del nodo en la paleta |
| `@categoria <nombre>` | La categoría de la paleta. Sin ella, *Nodos en Lua* |
| `@ayuda <texto>` | La ayuda del nodo. Puede ocupar varias líneas `@ayuda` |
| `@entrada <nombre> <tipo> [valor]` | Una entrada, con su valor de partida opcional |
| `@salida <nombre> <tipo>` | Una salida |
| `@puro` | El nodo solo calcula: no tiene pines de ejecución |

Los tipos son `numero`, `texto`, `sino`, `vector`, `color`, `entidad`,
`recurso`, `lista` y `cualquiera`. Los nombres de los pines y del archivo
solo pueden tener letras sin acentos, números y `_`.

El archivo **devuelve la función** que hace el nodo. Recibe las entradas en
el mismo orden de la cabecera y devuelve las salidas también en orden. En
un nodo sin `@puro`, la función puede usar `motor.esperar`.

Haz clic en un nodo en Lua de la lista para abrir el archivo con tu editor.
Los cambios se leen al volver a abrir el grafo y siempre al jugar. Si la
cabecera tiene un error, aparece en rojo debajo de la lista, con el archivo
y la línea.

## Véase también

- [Nodos](nodos.md)
- [Guiones en Lua](guiones.md)
- [API de Lua](../referencia/lua.md)
