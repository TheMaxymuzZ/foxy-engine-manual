#!/usr/bin/env python3
"""Genera los iconos del manual (src/imagenes/iconos/*.svg) y sus clases CSS
(theme/iconos.css).

Todos siguen la misma regla, la de la marca: trazo de 2 sobre una rejilla de
24 × 24, esquinas en inglete como el zorro y puntas redondeadas. En el manual
se escriben así:

    <i class="fx fx-mundo"></i>

y toman el color del texto que tienen alrededor (naranja en los títulos de las
tarjetas, gris en la barra lateral...).

Uso:  python3 herramientas/generar-iconos.py
"""
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
NARANJA = "#FF6B1F"

# nombre: (descripción, contenido SVG). `F` = relleno (para puntos y formas
# macizas); lo demás es trazo.
F = f'fill="{NARANJA}" stroke="none"'
ICONOS = {
    # Las partes del proyecto
    "proyecto": ("Proyecto", '<path d="M3 7.5V5.5a1.5 1.5 0 0 1 1.5-1.5h4.4l2 2.5h8.6A1.5 1.5 0 0 1 21 8v10.5a1.5 1.5 0 0 1-1.5 1.5h-15A1.5 1.5 0 0 1 3 18.5z"/><path d="M3 9.5h18"/>'),
    "mundo": ("Escena / mundo", '<path d="M12 2.8 20 7.4v9.2L12 21.2 4 16.6V7.4z"/><path d="M4 7.4 12 12l8-4.6M12 12v9.2"/><path d="M8 5.1l8 4.6"/>'),
    "mapa": ("Mapa de escenas", '<path d="M3 6.5 9 4l6 2.5L21 4v13.5L15 20l-6-2.5L3 20z"/><path d="M9 4v13.5M15 6.5V20"/>'),
    "interfaz": ("Interfaz", '<rect x="3" y="4" width="18" height="16" rx="1.5"/><path d="M3 8.5h18"/><path d="M7 12.5h5M7 16h10"/>'),
    "objeto": ("Objeto propio", '<path d="M12 2.8 20.5 7.5v9L12 21.2 3.5 16.5v-9z"/><path d="M3.5 7.5 12 12.2l8.5-4.7M12 12.2v9"/>'),
    "pixel": ("Pixel art", '<rect x="3.5" y="3.5" width="17" height="17" rx="1"/><path d="M3.5 9.17h17M3.5 14.83h17M9.17 3.5v17M14.83 3.5v17"/><rect x="9.17" y="3.5" width="5.66" height="5.67" ' + F + '/><rect x="3.5" y="9.17" width="5.67" height="5.66" ' + F + '/><rect x="14.83" y="14.83" width="5.67" height="5.67" ' + F + '/>'),
    "imagen": ("Imagen", '<rect x="3" y="4" width="18" height="16" rx="1.5"/><circle cx="8.5" cy="9.5" r="1.6"/><path d="m3.5 18 5.5-5.5 4 4 2.5-2.5 5 5"/>'),
    "guion": ("Guion Lua", '<path d="M14 3H6.5A1.5 1.5 0 0 0 5 4.5v15A1.5 1.5 0 0 0 6.5 21h11a1.5 1.5 0 0 0 1.5-1.5V8z"/><path d="M14 3v5h5"/><path d="m10 12.5-2.2 2.2 2.2 2.3M14 12.5l2.2 2.2-2.2 2.3"/>'),
    "vida": ("Día y noche", '<circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/>'),
    "carpeta": ("Carpeta", '<path d="M3 6.5A1.5 1.5 0 0 1 4.5 5h4.4l2 2.5h8.6A1.5 1.5 0 0 1 21 9v9.5a1.5 1.5 0 0 1-1.5 1.5h-15A1.5 1.5 0 0 1 3 18.5z"/>'),
    "carpeta-nueva": ("Carpeta nueva", '<path d="M3 6.5A1.5 1.5 0 0 1 4.5 5h4.4l2 2.5h8.6A1.5 1.5 0 0 1 21 9v9.5a1.5 1.5 0 0 1-1.5 1.5h-15A1.5 1.5 0 0 1 3 18.5z"/><path d="M12 10.5v6M9 13.5h6"/>'),
    "abrir": ("Abrir", '<path d="M3 18.5v-12A1.5 1.5 0 0 1 4.5 5h4.4l2 2.5h6.6A1.5 1.5 0 0 1 19 9v1.5"/><path d="M3 18.5 6 11h16l-3 7.5A1.5 1.5 0 0 1 17.6 20H4.5A1.5 1.5 0 0 1 3 18.5z"/>'),
    # Herramientas del mundo
    "cursor": ("Cursor", '<path d="M5 3.5 19 10l-6.2 1.8L10 18.5z"/><path d="m12.8 11.8 5.2 5.2"/>'),
    "mover": ("Elegir y mover", '<path d="M12 3v18M3 12h18"/><path d="m9 5.5 3-3 3 3M9 18.5l3 3 3-3M5.5 9l-3 3 3 3M18.5 9l3 3-3 3"/>'),
    "poner": ("Poner bloques", '<rect x="4" y="4" width="16" height="16" rx="1"/><path d="M12 8.5v7M8.5 12h7"/>'),
    "quitar": ("Quitar bloques", '<rect x="4" y="4" width="16" height="16" rx="1" stroke-dasharray="3 2.4"/><path d="M8.5 12h7"/>'),
    "pintar": ("Pintar", '<rect x="3.5" y="3" width="14" height="5.5" rx="1"/><path d="M17.5 5.75h3v5.25H11v3"/><rect x="9.5" y="14" width="3" height="7" rx="1"/>'),
    "colocar": ("Colocar objetos", '<path d="M3 11.5 12 4l9 7.5"/><path d="M5.5 9.5V20h13V9.5"/><path d="M10 20v-5.5h4V20"/>'),
    # Objetos del juego
    "vecino": ("Vecino", '<circle cx="12" cy="7.5" r="3.5"/><path d="M5 20.5a7 7 0 0 1 14 0"/>'),
    "zona": ("Zona de cambio", '<path d="M6.5 21V4.5A1.5 1.5 0 0 1 8 3h8a1.5 1.5 0 0 1 1.5 1.5V21"/><path d="M3.5 21h17"/><circle cx="14.2" cy="12.5" r="1.1" ' + F + '/>'),
    "entrada": ("Punto de entrada", '<path d="M12 21s-6.5-5.8-6.5-11a6.5 6.5 0 0 1 13 0c0 5.2-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.4"/>'),
    "inicio": ("Punto de inicio", '<path d="M5.5 21V3.5"/><path d="M5.5 4h12l-2.5 4 2.5 4h-12"/>'),
    "pelota": ("Pelota", '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5l4 3-1.5 4.7h-5L8 10.5z"/><path d="M12 3.5v4M16 10.5l3.9-1.3M14.5 15.2l2.4 3.3M9.5 15.2l-2.4 3.3M8 10.5 4.1 9.2"/>'),
    "usar": ("Al usarlo (E)", '<path d="M9 11.5V5a1.5 1.5 0 0 1 3 0v5.5"/><path d="M12 10V8.5a1.5 1.5 0 0 1 3 0V11"/><path d="M15 10.5a1.5 1.5 0 0 1 3 0V15a6 6 0 0 1-6 6h-.6a6 6 0 0 1-4.7-2.3L4.6 16a1.6 1.6 0 0 1 2.4-2.1L9 15.5"/>'),
    # Acciones del editor
    "jugar": ("Jugar aquí", '<path d="M7 4.5v15l12-7.5z" fill="' + NARANJA + '"/>'),
    "mando": ("Desde el inicio", '<path d="M7 7.5h10a4.5 4.5 0 0 1 4.4 3.6l1 5.2a2.6 2.6 0 0 1-4.6 2.1L15.6 16H8.4l-2.2 2.4a2.6 2.6 0 0 1-4.6-2.1l1-5.2A4.5 4.5 0 0 1 7 7.5z"/><path d="M7.5 10.5v3.5M5.75 12.25h3.5"/><circle cx="15.5" cy="11" r="1" ' + F + '/><circle cx="17.8" cy="13.3" r="1" ' + F + '/>'),
    "guardar": ("Guardar", '<path d="M19 21H5a1.5 1.5 0 0 1-1.5-1.5v-15A1.5 1.5 0 0 1 5 3h11l4.5 4.5v12A1.5 1.5 0 0 1 19 21z"/><path d="M7.5 3v4.5h7V3M7 21v-6.5h10V21"/>'),
    "deshacer": ("Deshacer", '<path d="M9 13.5 4 8.5l5-5"/><path d="M4 8.5h10.5a5.5 5.5 0 0 1 0 11H11"/>'),
    "rehacer": ("Rehacer", '<path d="m15 13.5 5-5-5-5"/><path d="M20 8.5H9.5a5.5 5.5 0 0 0 0 11H13"/>'),
    "editar": ("Editar", '<path d="M4 20h4L19 9a2.83 2.83 0 0 0-4-4L4 16z"/><path d="m13.5 6.5 4 4"/>'),
    "borrar": ("Borrar", '<path d="M4 7h16M9.5 7V4h5v3M6 7l1 13.5h10L18 7"/><path d="M10 11v6M14 11v6"/>'),
    "ver": ("Ver", '<path d="M2.5 12S6 5 12 5s9.5 7 9.5 7-3.5 7-9.5 7-9.5-7-9.5-7z"/><circle cx="12" cy="12" r="3"/>'),
    "buscar": ("Buscar", '<circle cx="10.5" cy="10.5" r="6.5"/><path d="m15.5 15.5 5 5"/>'),
    "girar": ("Girar", '<path d="M20 12a8 8 0 1 1-2.35-5.65"/><path d="M20 4v5h-5"/>'),
    "cerrar": ("Cerrar", '<path d="M6 6l12 12M18 6 6 18"/>'),
    "mas": ("Nuevo", '<path d="M12 5v14M5 12h14"/>'),
    "duplicar": ("Duplicar", '<rect x="8" y="8" width="12.5" height="12.5" rx="1.5"/><path d="M16 8V5A1.5 1.5 0 0 0 14.5 3.5h-9A1.5 1.5 0 0 0 4 5v9.5A1.5 1.5 0 0 0 5.5 16H8"/>'),
    "suelo": ("Al suelo", '<path d="M12 3.5v11M7.5 10l4.5 4.5 4.5-4.5"/><path d="M4 19.5h16"/>'),
    "teclado": ("Teclas", '<rect x="2.5" y="6" width="19" height="12" rx="1.5"/><path d="M6.5 10h.01M10 10h.01M14 10h.01M17.5 10h.01M7.5 14h9"/>'),
    "terminal": ("Línea de comandos", '<rect x="3" y="4" width="18" height="16" rx="1.5"/><path d="m7 9.5 3 2.5-3 2.5M12.5 15H17"/>'),
    "descargar": ("Descargar", '<path d="M12 3.5v11M7.5 10l4.5 4.5 4.5-4.5"/><path d="M4 16.5v2A1.5 1.5 0 0 0 5.5 20h13a1.5 1.5 0 0 0 1.5-1.5v-2"/>'),
    "estrella": ("Escena inicial", '<path d="m12 3 2.8 5.8 6.2.8-4.5 4.4 1.1 6.2L12 17.3l-5.6 2.9 1.1-6.2L3 9.6l6.2-.8z" fill="' + NARANJA + '"/>'),
    "aviso": ("Aviso", '<path d="M12 3.5 2.5 20h19z"/><path d="M12 10v4.5"/><circle cx="12" cy="17.2" r="1.1" ' + F + '/>'),
    "enlace": ("Conectar", '<path d="M10 14a4 4 0 0 0 5.7 0l3.2-3.2a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3.2 3.2a4 4 0 0 0 5.7 5.7l1-1"/>'),
    "flecha": ("Lleva aquí", '<path d="M20 12H4.5M10 6l-6 6 6 6"/>'),
    "registro": ("Registro", '<path d="M14 3H6.5A1.5 1.5 0 0 0 5 4.5v15A1.5 1.5 0 0 0 6.5 21h11a1.5 1.5 0 0 0 1.5-1.5V8z"/><path d="M14 3v5h5M8.5 12.5h7M8.5 16h5"/>'),
    "chip": ("Tarjeta gráfica", '<rect x="6" y="6" width="12" height="12" rx="1.5"/><rect x="9.5" y="9.5" width="5" height="5"/><path d="M9.5 2.5V6M14.5 2.5V6M9.5 18v3.5M14.5 18v3.5M2.5 9.5H6M2.5 14.5H6M18 9.5h3.5M18 14.5h3.5"/>'),
    "escudo": ("Seguridad", '<path d="M12 3 4.5 6v5.5c0 4.6 3.2 8.2 7.5 9.5 4.3-1.3 7.5-4.9 7.5-9.5V6z"/><path d="m9 12 2.2 2.2L15.5 10"/>'),
    "historial": ("Historial", '<path d="M3.5 12a8.5 8.5 0 1 0 2.5-6"/><path d="M3.5 4v5h5"/><path d="M12 7.5V12l3 2"/>'),
    # Avisos del texto
    "consejo": ("Consejo", '<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.6 10.8c.7.5 1.1 1.3 1.1 2.1V16h5v-.1c0-.8.4-1.6 1.1-2.1A6 6 0 0 0 12 3z"/>'),
    "nota": ("Nota", '<circle cx="12" cy="12" r="9"/><path d="M12 11v5.5"/><circle cx="12" cy="7.8" r="1.1" ' + F + '/>'),
    # Elementos de una interfaz
    "panel": ("Panel", '<rect x="3" y="5" width="18" height="14" rx="2"/>'),
    "texto": ("Texto", '<path d="M5 7V4.5h14V7M12 4.5v15M9 19.5h6"/>'),
    "boton": ("Botón", '<rect x="2.5" y="7" width="19" height="10" rx="5"/><path d="M8.5 12h7"/>'),
    # Botones del mando de PlayStation
    "ps-cruz": ("Cruz", '<path d="M6 6l12 12M18 6 6 18"/>'),
    "ps-circulo": ("Círculo", '<circle cx="12" cy="12" r="7.5"/>'),
    "ps-cuadrado": ("Cuadrado", '<rect x="5" y="5" width="14" height="14"/>'),
}

# Páginas de la barra lateral que llevan icono delante.
BARRA = {
    "introduccion.html": "marca",
    "empezar/instalar.html": "descargar",
    "empezar/primer-proyecto.html": "proyecto",
    "empezar/editor.html": "interfaz",
    "guia/mundo.html": "mundo",
    "guia/carpetas.html": "carpeta",
    "guia/creador.html": "objeto",
    "guia/pixel-art.html": "pixel",
    "guia/escenas.html": "mapa",
    "guia/interfaces.html": "boton",
    "guia/vida.html": "vida",
    "guia/guiones.html": "guion",
    "guia/jugar.html": "mando",
    "referencia/atajos.html": "teclado",
    "referencia/lua.html": "guion",
    "referencia/acciones.html": "usar",
    "referencia/objetos.html": "colocar",
    "referencia/materiales.html": "pintar",
    "referencia/archivos.html": "registro",
    "referencia/linea-de-comandos.html": "terminal",
    "apendices/problemas.html": "aviso",
    "apendices/glosario.html": "buscar",
    "apendices/marca.html": "marca",
    "apendices/historial.html": "historial",
}


# Iconos que son archivos de la marca (no se generan).
MARCA = {"marca": ("El zorro", "../imagenes/marca/zorro.svg")}


def svg(cuerpo: str) -> str:
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" '
        f'fill="none" stroke="{NARANJA}" stroke-width="2" stroke-linecap="round" '
        f'stroke-linejoin="round">{cuerpo}</svg>\n'
    )


def main() -> None:
    carpeta = RAIZ / "src" / "imagenes" / "iconos"
    carpeta.mkdir(parents=True, exist_ok=True)
    for nombre, (_, cuerpo) in ICONOS.items():
        (carpeta / f"{nombre}.svg").write_text(svg(cuerpo), encoding="utf-8")

    css = [
        "/* Iconos del manual. Archivo generado por herramientas/generar-iconos.py:",
        "   no lo cambies a mano.",
        '   Uso: <i class="fx fx-mundo"></i>, toma el color del texto. */',
        "",
    ]
    for nombre in ICONOS:
        css.append(f'.fx-{nombre} {{ --fx: url("../imagenes/iconos/{nombre}.svg"); }}')
    for nombre, (_, ruta) in MARCA.items():
        css.append(f'.fx-{nombre} {{ --fx: url("{ruta}"); }}')
    css.append("")
    css.append("/* Barra lateral */")
    for pagina, nombre in BARRA.items():
        ruta = MARCA[nombre][1] if nombre in MARCA else f"../imagenes/iconos/{nombre}.svg"
        css.append(f'.chapter a[href$="{pagina}"]::before {{ --fx: url("{ruta}"); }}')
    (RAIZ / "theme" / "iconos.css").write_text("\n".join(css) + "\n", encoding="utf-8")

    # Tabla para la página de la marca.
    filas = ['<div class="iconos">']
    for nombre, (desc, _) in list(ICONOS.items()) + list(MARCA.items()):
        filas.append(
            f'  <figure><i class="fx fx-{nombre}"></i><figcaption>{desc}<code>{nombre}</code></figcaption></figure>'
        )
    filas.append("</div>")
    (RAIZ / "src" / "apendices" / "iconos.html").write_text("\n".join(filas) + "\n", encoding="utf-8")
    print(f"{len(ICONOS)} iconos")


if __name__ == "__main__":
    main()
