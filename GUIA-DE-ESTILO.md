# Guía de estilo del manual

El manual es la **documentación oficial** de Foxy Engine. Tiene tres usos:
aprender a usar el motor, consultar cómo se hace algo concreto y enseñar lo
que se puede hacer con él. Todo lo que se escriba aquí sigue estas reglas.

## Tono

- **Claro, preciso y profesional.** Frases cortas (menos de 25 palabras) y
  párrafos de tres frases como mucho.
- **Tú en las instrucciones, impersonal en las descripciones.** Los pasos
  van en imperativo («Pulsa **Crear proyecto**»); lo que explica cómo es
  algo, en tercera persona («La pantalla de inicio muestra…»).
- **Sin coloquialismos ni exclamaciones**, sin emojis y sin bromas.
- **Primero la respuesta.** La primera frase de cada página y de cada
  sección dice qué es o para qué sirve; los detalles van después.
- **Lo que el lector ve, no cómo está hecho por dentro.** El código del
  motor, los nombres de fases o de *pull requests* solo aparecen en el
  historial de versiones.

## Términos fijos

Se usan siempre las mismas palabras (las del editor) y se definen en el
[glosario](src/apendices/glosario.md): *proyecto*, *escena*, *objeto*,
*objeto propio*, *interfaz*, *material*, *cubito* (vóxel de 0,5 m),
*bloque* (1 m), *plantilla*, *pantalla de inicio*, *inspector*, *panel*,
*pestaña*, *guion*, *nodo*. Los nombres de botones, menús y pestañas se
escriben **en negrita** y exactamente como en el editor.

## Estructura de cada página

1. Título y una frase de qué es.
2. Una **captura de pantalla completa** para situar al lector y, por cada
   panel que se explique, una **captura del panel** recortada.
3. Secciones cortas: qué hay en el panel (tabla) y cómo se hace cada tarea
   (pasos numerados).
4. Avisos con su formato: **Nota** (información extra), **Consejo** (un
   atajo o una buena práctica) e **Importante** (algo que puede hacer
   perder trabajo).
5. Al final, «Véase también» con los enlaces relacionados.

## Partes del manual

| Parte | Para qué |
|---|---|
| **Empezar** | Instalar, la pantalla de inicio y los primeros pasos |
| **Manual del editor** | Una página por panel o herramienta |
| **Conceptos** | Las ideas del motor: proyectos, escenas, objetos, recursos |
| **Guías prácticas** | Tutoriales de principio a fin (llegarán con las plantillas) |
| **Referencia** | Teclas, Lua, nodos, acciones, formatos de archivo, línea de comandos |
| **Apéndices** | Problemas comunes, glosario, marca e historial |

## Capturas

- Se hacen con el propio motor (`foxy-engine --captura … --editor
  --pestana …`), a 1440 × 860, con los proyectos de ejemplo, para que todas
  tengan el mismo aspecto y se puedan rehacer en cada versión.
- Las capturas de panel se recortan de esas mismas imágenes y se llaman
  `panel-<nombre>.png`.
- Toda imagen lleva un texto alternativo que dice qué muestra.
