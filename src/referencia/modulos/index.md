# Módulos

Los **módulos** son partes del motor que un proyecto puede activar o
desactivar. Un módulo desactivado no se calcula ni aparece en el juego, lo
que simplifica los proyectos que no lo necesitan y ahorra trabajo al
ordenador.

| Módulo | En el archivo | Proyecto vacío | Plantillas de isla |
|---|---|---|---|
| [Día y noche](dia-y-noche.md) | `dia_y_noche` | Activado | Activado |
| [Clima](clima.md) | `clima` | Desactivado | Activado |
| [Estaciones](estaciones.md) | `estaciones` | Desactivado | Activado |
| [Vecinos](vecinos.md) | `vecinos` | Desactivado | Activado |
| [Romper bloques](romper-bloques.md) | `romper_bloques` | Desactivado | Activado |
| [Líquidos](liquidos.md) | `liquidos` | Desactivado | Activado |
| [Escombros](escombros.md) | `escombros` | Desactivado | Activado |

## Módulos del proyecto

Se eligen en **Proyecto → Ajustes del proyecto… → Módulos** y se guardan en
`proyecto.ron`:

```ron
modulos: (dia_y_noche: true, clima: false, estaciones: false, vecinos: false,
          romper_bloques: true, liquidos: true, escombros: false),
```

## Módulos de una escena

Cada escena puede cambiar los módulos del proyecto. Sin nada elegido, el
Inspector muestra **Módulos de la escena**, donde cada módulo puede estar
*Como el proyecto*, *Sí, aquí* o *No, aquí*. Por ejemplo, una cueva puede
desactivar el clima aunque el resto del juego lo tenga.

```ron
modulos: (clima: Some(false)),
```

## Véase también

- [Ajustes del proyecto](../../editor/ajustes-proyecto.md#módulos)
- [La vida del mundo](../../guia/vida.md)
