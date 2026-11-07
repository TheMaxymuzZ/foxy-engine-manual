# Inspector

El inspector **cambia según lo que estés haciendo**.

![El Inspector](../imagenes/capturas/panel-inspector.png)

| Nº | Elemento | Descripción |
|---|---|---|
| 1 | **Herramienta activa** | Las opciones de la herramienta: forma y tamaño del pincel, simetría |
| 2 | **Material** | El material con el que se construye o se pinta |
| 3 | **Objeto elegido** | El nombre, los comportamientos, el tipo y la posición de la entidad elegida |
| 4 | **Crear prefabricado** | Guarda la entidad como recurso reutilizable |
| 5 | **Componentes** | Los componentes de la entidad y **Añadir componente** |
| 6 | **Al usarlo (E)** | La acción que se ejecuta cuando el jugador usa la entidad |

Lo que muestra depende de la situación:

- Con una herramienta de bloques: el **pincel** (forma, tamaño, simetría) y
  los **materiales**.
- Con *Colocar objetos*: la **lista de objetos** para colocar.
- Con una entidad elegida: su **nombre**, sus
  [**comportamientos**](../guia/comportamientos.md) con **➕ Comportamiento**,
  su posición, **Crear
  prefabricado** (o, en una copia, los botones de su prefabricado), sus
  **componentes** con <i class="fx fx-mas"></i> **Añadir componente**, y
  <i class="fx fx-usar"></i> **Al usarlo (E)**, lo que pasa cuando el
  jugador la usa. Abajo, el giro, *Al suelo*, *Ver*, *Duplicar* y *Borrar*.
- Sin nada elegido: el **terreno** de la escena (su
  [generador](../guia/generadores.md)), cómo pasa el **tiempo** y los
  **módulos de la escena**.

![Componentes de una entidad en el inspector](../imagenes/capturas/panel-componentes.png)

## Componentes

Cada componente se muestra en un apartado plegable con su descripción y sus
valores. En una copia de un prefabricado, los componentes heredados indican
*del prefabricado* y los cambiados *cambiado aquí*. Ver
[Entidades y componentes](../guia/entidades.md).

## Comportamientos

Justo debajo del nombre, la sección **Comportamientos** enseña los grafos y
guiones que lleva la entidad, cada uno en un recuadro con su casilla para
encenderlo o apagarlo, su menú **☰** y sus valores. **Doble clic** en el
nombre lo abre en Nodos o en Código. Ver
[Comportamientos](../guia/comportamientos.md).

![Las propiedades de un guion de enemigo en el inspector](../imagenes/capturas/panel-inspector-guion.png)

## Módulos de la escena

Cada [módulo](../referencia/modulos/index.md) puede estar *Como el
proyecto*, *Sí, aquí* o *No, aquí*.

Ver [Construir el mundo](../guia/mundo.md), [Generadores de terreno](../guia/generadores.md)
y [La vida del mundo](../guia/vida.md).
