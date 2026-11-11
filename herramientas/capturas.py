#!/usr/bin/env python3
"""Rehace todas las capturas del manual con el propio motor.

Cada captura del manual sale de una orden de `foxy-engine --captura`, con
los mismos proyectos de ejemplo y el mismo tamaño, así que se pueden rehacer
todas en cada versión y ninguna se queda vieja:

    python3 herramientas/capturas.py --motor ../foxy-engine/target/release/foxy-engine

Opciones:
    --solo NOMBRE …     Solo esas capturas (sin «.png»; admite el principio
                        del nombre, como «panel-»)
    --escaparate        Rehace también las animaciones del escaparate (tarda más)
    --sin-capturas      No rehace las capturas (útil con --escaparate)
    --lista             Enseña la lista de capturas y sale

Además de las capturas:

- Pone los **números** de las capturas anotadas (círculos naranjas con un
  número) en el sitio que dice ANOTACIONES. La página del panel explica cada
  número debajo de la imagen.
- Con --escaparate, hace una animación corta de cada plantilla para la
  portada (imagenes/escaparate/<plantilla>.webp) y su primer fotograma
  (<plantilla>.png).
- Escribe la versión del motor en theme/version.js, para que salga en todas
  las páginas.
- Pone al día las tablas de la referencia de componentes
  (`--referencia-componentes`), de nodos y de la API de Lua.

Necesita Pillow (`pip install pillow`). Las capturas se hacen sin ventana: en
Linux sin tarjeta gráfica basta con los controladores de Mesa (lavapipe).
"""

from __future__ import annotations

import argparse
import math
import shlex
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:  # pragma: no cover
    sys.exit("Falta Pillow: pip install pillow")

RAIZ = Path(__file__).resolve().parent.parent
CAPTURAS = RAIZ / "src" / "imagenes" / "capturas"
ESCAPARATE = RAIZ / "src" / "imagenes" / "escaparate"

# Tamaño de todas las capturas de pantalla completa.
ANCHO, ALTO = 1440, 860
ED = f"--ancho {ANCHO} --alto {ALTO} --editor"
JUEGO = f"--ancho {ANCHO} --alto {ALTO}"

# Un modelo de MagicaVoxel para «Importar modelos» (lo hace ejemplos/hacer-seta.py).
SETA = RAIZ / "herramientas" / "ejemplos" / "seta.vox"

# La plaza de prueba del motor (con vecinos, mercado y farolas).
PLAZA = "--mundo " + str(RAIZ.parent / "foxy-engine" / "mundos" / "plaza_de_prueba.ron")

# La isla de prueba vista desde el mismo sitio en todas las capturas de juego.
ISLA = "--camara 150,40,175 --mirar 96,16,120"

# nombre -> argumentos de foxy-engine (además de «--captura <archivo>»).
# Las que empiezan por «panel-» son recortes de un panel con --recortar.
LISTA: dict[str, str] = {
    # Pantalla de inicio y proyecto nuevo
    "inicio": f"{ED} --pestana inicio",
    "inicio-plantillas": f"--ancho {ANCHO} --alto 1100 --editor --pestana plantillas",
    "inicio-aprender": f"{ED} --pestana aprender",
    "inicio-nuevo": f"{ED} --pestana nuevo",
    "proyecto-vacio": f"{ED} --pestana vacio",
    "ajustes-proyecto": f"{ED} --pestana ajustes",
    "panel-ajustes-proyecto": "@recorte ajustes-proyecto 482,241,958,619",
    "panel-asistente": "@recorte inicio-nuevo 280,146,1158,710",
    "panel-inicio-secciones": "@recorte inicio 0,0,236,300",
    "panel-fila-proyecto": "@recorte inicio 276,158,1400,246",
    # Espacio de trabajo
    "panel-barra-superior": "@recorte editor-proyecto 0,0,1440,34 margen=32",
    "editor-proyecto": f"{ED} --pestana proyecto",
    "espacio-construir": f"{ED} --pestana proyecto --espacio construir",
    "espacio-programar": f"{ED} --pestana codigo --espacio programar",
    "espacio-pixel-art": f"{ED} --pestana proyecto --espacio pixel-art",
    "espacio-animar": f"{ED} --pestana personaje-animado --espacio animar --animacion abrir --segundo 0.6",
    "editor-2d": f"{ED} --pestana plataformas-2d --espacio 2d --herramienta pintar",
    "editor-2d-cenital": f"{ED} --pestana aventura-cenital",
    "flotante": f"{ED} --pestana proyecto --flotante inspector",
    # Para principiantes (Fase G)
    "modo-sencillo": f"{ED} --pestana tercera-persona --sencillo",
    "tutorial-guiado": f"{ED} --pestana tercera-persona --sencillo --tutorial 6",
    "plantilla-tercera-persona": f"{ED} --pestana tercera-persona",
    "plantilla-puzle": f"{ED} --pestana puzle",
    "maximizar": f"{ED} --pestana proyecto --maximizar vista",
    "paleta": f"{ED} --pestana proyecto --paleta abri",
    "tema-claro": f"{ED} --pestana proyecto --tema-claro",
    # Paneles (uno por página de «La interfaz»)
    "panel-vista": f"{ED} --pestana proyecto --recortar vista",
    "panel-proyecto": f"{ED} --pestana proyecto --recortar proyecto",
    "panel-escena": f"{ED} --pestana proyecto --recortar escena",
    "panel-inspector": f"{ED} --pestana proyecto --elegir 3 --recortar inspector",
    "panel-terreno": f"{ED} --pestana colinas --herramienta elegir --recortar inspector",
    "escena-vacia": f"{ED} --mundo {RAIZ / 'herramientas' / 'ejemplos' / 'escena-vacia.ron'} --herramienta elegir --camara 48,10,70 --mirar 48,0,48",
    "panel-sol": f"{ED} --mundo {RAIZ / 'herramientas' / 'ejemplos' / 'escena-vacia.ron'} --herramienta elegir --elegir 2 --recortar inspector",
    "modelos-3d": f"{ED} --pestana modelos --herramienta elegir --elegir 4 --camara 50.5,7.6,51.8 --mirar 47.6,5.7,45 --hora 16",
    "modelos-jugando": f"--ancho {ANCHO} --alto {ALTO} --editor --pestana modelos --jugar --hora 10",
    "panel-modelos": f"{ED} --pestana modelos --herramienta objeto --elegir 4 --recortar inspector",
    "panel-componentes": f"{ED} --pestana entidades --elegir 2 --recortar inspector",
    "reutilizables": f"{ED} --pestana reutilizables --herramienta elegir --camara 48,12,62 --mirar 48,5,45",
    "reutilizable-parte": f"{ED} --pestana reutilizables --herramienta elegir --elegir 10 --camara 48,12,62 --mirar 48,5,45",
    "reutilizable-original": f"{ED} --pestana reutilizable-original --herramienta elegir",
    "panel-zona": f"{ED} --pestana entidades --elegir 3 --recortar inspector",
    "panel-codigo": f"{ED} --pestana codigo --espacio programar --recortar codigo",
    "panel-consola": f"{ED} --pestana codigo --espacio programar --recortar consola",
    "panel-depurador": "@recorte depurar 900,160,1440,688",
    "panel-inspector-guion": f"{ED} --pestana codigo --elegir 3 --recortar inspector",
    "panel-nodos": f"--ancho 1600 --alto 900 --editor --pestana nodos --recortar nodos",
    "panel-archivos": f"{ED} --pestana archivos --recortar archivos",
    "panel-materiales": "--ancho 1100 --alto 700 --editor --pestana materiales --maximizar materiales --recortar materiales",
    "panel-pixelart": f"{ED} --pestana pixel --recortar pixel",
    "panel-registro": f"{ED} --pestana proyecto --abrir registro --recortar registro",
    "panel-casillas": f"{ED} --pestana plataformas-2d --espacio 2d --recortar casillas",
    "panel-casillas-choques": f"{ED} --pestana plataformas-2d --espacio 2d --herramienta choques --recortar casillas",
    "panel-casillas-autocasillas": f"{ED} --pestana plataformas-2d --espacio 2d --herramienta autocasillas --recortar casillas",
    "panel-capas": f"{ED} --pestana plataformas-2d --espacio 2d --abrir capas --recortar capas",
    "panel-sprites": "--ancho 1000 --alto 700 --editor --pestana plataformas-2d --espacio 2d --maximizar sprites --recortar sprites",
    "panel-animacion": f"{ED} --pestana personaje-animado --espacio animar --animacion abrir --segundo 0.6 --recortar animacion",
    "panel-animaciones": f"{ED} --pestana personaje-animado --espacio animar --recortar animaciones",
    "panel-estados": "--ancho 1200 --alto 560 --editor --pestana personaje-animado --espacio animar --elegir 3 --maximizar estados --recortar estados",
    "panel-animador": f"{ED} --pestana personaje-animado --espacio animar --elegir 4 --recortar inspector",
    "panel-publicar": "@recorte publicar-ventana 426,76,1008,824",
    # Construir
    "entidades": f"{ED} --pestana entidades --elegir 3",
    "colinas": f"{ED} --pestana colinas",
    "archivos": f"{ED} --pestana archivos",
    "materiales": f"{ED} --pestana materiales --maximizar materiales",
    "creador": f"{ED} --pestana objeto",
    "creador-piezas": f"{ED} --pestana personaje-animado --objeto personaje",
    "extruir-simetria": f"{ED} --pestana proyecto --herramienta extruir --simetria xz",
    "importar-ventana": f"{ED} --pestana importar --modelo {SETA}",
    "importar-objeto": f"{ED} --pestana importado --modelo {SETA}",
    "pixel-biblioteca": f"{ED} --pestana pixel",
    "pixel-boton": f"{ED} --pestana imagen",
    "pixel-texturas": f"{ED} --pestana texturas",
    "interfaces-editor": f"{ED} --pestana interfaz",
    # Lógica
    "nodos": f"--ancho 1600 --alto 900 --editor --pestana nodos",
    "nodos-depurar": f"--ancho 1600 --alto 900 --editor --pestana nodos-depurar",
    "comportamientos": f"{ED} --pestana comportamientos --herramienta elegir",
    "panel-comportamientos": "@recorte comportamientos 1126,70,1440,470",
    "programar": f"{ED} --pestana programar --herramienta elegir",
    "nodos-codigo": f"{ED} --pestana nodos-codigo --maximizar nodos",
    "panel-nodos-codigo": "@recorte nodos-codigo 1160,105,1440,510",
    "guion-mundo": f"{ED} --pestana guion",
    "codigo-autocompletar": f"{ED} --pestana codigo-autocompletar --espacio programar",
    "depurar": f"{ED} --pestana codigo-depurar --jugar --espacio programar",
    "rendimiento": f"--ancho 1600 --alto 900 --editor --pestana proyecto --rendimiento",
    # Animación
    "cinematica-editor": f"{ED} --pestana personaje-animado --espacio animar --animacion cine:presentacion --segundo 2",
    # 2D y publicar
    "juego-plataformas-voxel": f"{ED} --pestana plataformas-voxel --jugar --esperar 0.5",
    "juego-plataformas-2d": f"{ED} --pestana plataformas-2d --jugar --esperar 0.5",
    "publicar-ventana": f"--ancho {ANCHO} --alto 900 --editor --pestana publicar",
    # El juego
    "juego-inicio": f"{JUEGO} --juego --menu inicio",
    "juego-pausa": f"{JUEGO} {PLAZA} --juego --menu pausa",
    "juego-opciones": f"{JUEGO} --juego --menu opciones",
    "juego-controles": f"{JUEGO} --juego --menu controles",
    "juego-jugando": f"{JUEGO} {PLAZA} --juego --menu jugando",
    "juego-hablar": f"{JUEGO} {PLAZA} --juego --menu jugando --hablar",
    "interfaces-menu": f"{JUEGO} --juego --menu menu-propio",
    "interfaces-cartel": f"{JUEGO} --juego --menu cartel",
    "jugar-aqui": f"{ED} --pestana proyecto --jugar",
    "clima-tormenta": f"{JUEGO} {PLAZA} --juego --menu jugando --clima tormenta",
    "estacion-invierno": f"{JUEGO} {PLAZA} --juego --menu jugando --estacion invierno",
    "estacion-otono": f"{JUEGO} {ISLA} --estacion otono",
    "farolas-de-noche": f"{JUEGO} {PLAZA} --camara 118,26,142 --mirar 96,17,118 --hora 21.5",
    "isla": f"{JUEGO} {ISLA}",
    # Gráficos (Fase I)
    "ajustes-graficos": f"{ED} --pestana ajustes-graficos",
    "panel-ajustes-graficos": "@recorte ajustes-graficos 476,236,964,624",
    "juego-opciones-graficos": f"{JUEGO} --juego --menu opciones-graficos",
    "cueva-antorchas": f"{JUEGO} --enorme cueva-con-antorchas",
    "modelos-pbr": f"{ED} --pestana modelos --camara 49.6,6.6,50.6 --mirar 47.8,5.2,46 --hora 21 --recortar vista",
    "tono-cine": f"--ancho 720 --alto 430 {ISLA} --hora 17.2 --tono cine",
    "tono-blender": f"--ancho 720 --alto 430 {ISLA} --hora 17.2 --tono blender",
    "tono-neutro": f"--ancho 720 --alto 430 {ISLA} --hora 17.2 --tono neutro",
    "tono-ninguno": f"--ancho 720 --alto 430 {ISLA} --hora 17.2 --tono ninguno",
    # Marca
    "marca-splash": f"{JUEGO} --splash",
    "marca-carga-editor": f"{JUEGO} --editor --splash",
    "publicado-powered": f"{JUEGO} --juego --splash",
}

# Capturas de pantalla completa que no se pueden rehacer con una sola orden
# (se dejan como están; la razón va al lado).
A_MANO = {
    "dos-ventanas": "dos ventanas del sistema a la vez (Xvfb)",
    "publicado-carga": "el juego publicado, abierto en Xvfb",
    "publicado-titulo": "el juego publicado, abierto en Xvfb",
    "publicado-jugando": "el juego publicado, abierto en Xvfb",
    "publicado-opciones": "el juego publicado, abierto en Xvfb",
    "publicado-controles": "el juego publicado, abierto en Xvfb",
    "cinematica-jugando": "la cinemática a mitad, jugando",
    "personaje-jugando": "el personaje andando, jugando",
    "tercera-persona": "jugando en tercera persona",
    "derrumbe-cae": "una casa cayendo después de romper su base",
    "derrumbe-ruinas": "la casa caída",
    "romper-apuntar": "apuntando a un bloque para romperlo",
    "detalle-de-lejos": "dos capturas comparadas",
    "importar-escena": "un modelo importado y colocado en la escena",
}

# Números sobre las capturas anotadas: nombre -> [(x, y), …] en píxeles de
# la imagen. El número 1 es el primero de la lista.
ANOTACIONES: dict[str, list[tuple[int, int]]] = {}
try:
    from anotaciones import ANOTACIONES  # type: ignore  # noqa: E402,F811
except ImportError:
    pass

# Plantillas del escaparate: slug -> (argumentos, animación).
#   «orbita cx,cy,cz r h»: la cámara da una vuelta alrededor de (cx,cy,cz)
#   a r metros y h metros de altura.
#   «jugar»: el juego de la plantilla, fotograma a fotograma.
ESCAPARATE_LISTA: dict[str, tuple[str, str]] = {
    "isla-voxel": ("--plantilla isla-voxel", "orbita 96,14,96 95 45"),
    "isla-de-ejemplo": ("--plantilla isla-de-ejemplo", "orbita 96,14,118 70 35"),
    "personaje-animado": ("--editor --pestana personaje-animado --jugar", "jugar"),
    "plataformas-voxel": ("--editor --pestana plataformas-voxel --jugar", "jugar"),
    "plataformas-2d": ("--editor --pestana plataformas-2d --jugar", "jugar"),
    "aventura-cenital": ("--editor --pestana aventura-cenital --jugar", "jugar"),
}

NARANJA = (255, 107, 31)


def fuente(tam: int) -> ImageFont.ImageFont:
    for f in (
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
    ):
        try:
            return ImageFont.truetype(f, tam)
        except OSError:
            continue
    return ImageFont.load_default()


def anotar(ruta: Path, puntos: list[tuple[int, int]]) -> None:
    """Pinta un círculo naranja numerado en cada punto."""
    im = Image.open(ruta).convert("RGBA")
    capa = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    r = 11
    f = fuente(13)
    for i, (x, y) in enumerate(puntos, start=1):
        d.ellipse((x - r - 1, y - r + 1, x + r + 1, y + r + 3), fill=(0, 0, 0, 90))
        d.ellipse((x - r - 2, y - r - 2, x + r + 2, y + r + 2), fill=(255, 255, 255, 255))
        d.ellipse((x - r, y - r, x + r, y + r), fill=NARANJA + (255,))
        t = str(i)
        caja = d.textbbox((0, 0), t, font=f)
        w, h = caja[2] - caja[0], caja[3] - caja[1]
        d.text((x - w / 2 - caja[0], y - h / 2 - caja[1]), t, font=f, fill="white")
    Image.alpha_composite(im, capa).convert("RGB").save(ruta, optimize=True)


def correr(motor: Path, args: list[str]) -> None:
    r = subprocess.run([str(motor), *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"foxy-engine {' '.join(args)}\n{r.stdout}\n{r.stderr}")


def capturar(motor: Path, nombre: str, orden: str) -> None:
    destino = CAPTURAS / f"{nombre}.png"
    if orden.startswith("@recorte"):
        _, origen, caja, *resto = orden.split()
        x0, y0, x1, y1 = (int(v) for v in caja.split(","))
        recorte = Image.open(CAPTURAS / f"{origen}.png").convert("RGB").crop((x0, y0, x1, y1))
        # «margen=N»: N píxeles más por debajo, para poner los números.
        margen = next((int(r.split("=")[1]) for r in resto if r.startswith("margen=")), 0)
        if margen:
            fondo = recorte.getpixel((recorte.width // 2, recorte.height - 1))
            con = Image.new("RGB", (recorte.width, recorte.height + margen), fondo)
            con.paste(recorte, (0, 0))
            recorte = con
        recorte.save(destino, optimize=True)
    else:
        correr(motor, ["--captura", str(destino), *shlex.split(orden)])
        Image.open(destino).convert("RGB").save(destino, optimize=True)
    if nombre in ANOTACIONES:
        anotar(destino, ANOTACIONES[nombre])


def escaparate(motor: Path, cuadros: int = 24) -> None:
    ESCAPARATE.mkdir(parents=True, exist_ok=True)
    w, h = 640, 380
    for slug, (args, anim) in ESCAPARATE_LISTA.items():
        fotos = []
        with tempfile.TemporaryDirectory() as tmp:
            for i in range(cuadros):
                p = Path(tmp) / f"{i}.png"
                extra: list[str]
                if anim.startswith("orbita"):
                    _, centro, radio, alto = anim.split()
                    cx, cy, cz = (float(v) for v in centro.split(","))
                    a = 2 * math.pi * i / cuadros + 0.6
                    x = cx + float(radio) * math.cos(a)
                    z = cz + float(radio) * math.sin(a)
                    extra = ["--camara", f"{x:.2f},{cy + float(alto):.2f},{z:.2f}", "--mirar", f"{cx},{cy},{cz}", "--tiempo", f"{i * 0.12:.2f}"]
                else:
                    extra = ["--esperar", f"{0.2 + i * 0.1:.2f}"]
                correr(motor, ["--captura", str(p), "--ancho", str(w), "--alto", str(h), *shlex.split(args), *extra])
                fotos.append(Image.open(p).convert("RGB"))
        fotos[0].save(ESCAPARATE / f"{slug}.png", optimize=True)
        fotos[0].save(
            ESCAPARATE / f"{slug}.webp",
            save_all=True,
            append_images=fotos[1:],
            duration=110,
            loop=0,
            quality=80,
            method=6,
        )
        print(f"  escaparate/{slug}.webp ({len(fotos)} fotogramas)")


def version(motor: Path) -> str:
    r = subprocess.run([str(motor), "--version"], capture_output=True, text=True)
    v = r.stdout.strip().removeprefix("Foxy Engine").strip()
    (RAIZ / "theme" / "version.js").write_text(
        "// Lo escribe herramientas/capturas.py con `foxy-engine --version`.\n"
        f'window.FOXY_VERSION = "{v}";\n',
        encoding="utf-8",
    )
    return v


def referencias(motor: Path) -> None:
    ref = RAIZ / "src" / "referencia"
    correr(motor, ["--referencia-componentes", str(ref / "componentes")])
    correr(motor, ["--referencia-nodos", str(ref / "nodos.md")])
    correr(motor, ["--referencia-lua", str(ref / "api-lua.md")])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--motor", type=Path, default=RAIZ.parent / "foxy-engine" / "target" / "release" / "foxy-engine")
    ap.add_argument("--solo", nargs="*", default=None)
    ap.add_argument("--escaparate", action="store_true")
    ap.add_argument("--sin-capturas", action="store_true")
    ap.add_argument("--lista", action="store_true")
    a = ap.parse_args()
    if a.lista:
        for n, o in LISTA.items():
            print(f"{n:28} {o}")
        for n, r in A_MANO.items():
            print(f"{n:28} (a mano: {r})")
        return
    if not a.motor.exists():
        sys.exit(f"No encuentro el motor en {a.motor}. Compílalo con «cargo build --release» o pasa --motor.")
    print(f"Foxy Engine {version(a.motor)}")
    referencias(a.motor)
    fallos: list[str] = []
    if not a.sin_capturas:
        # Primero las que no son recortes de otras.
        orden = sorted(LISTA.items(), key=lambda kv: kv[1].startswith("@recorte"))
        for nombre, args in orden:
            if a.solo is not None and not any(nombre.startswith(s) for s in a.solo):
                continue
            try:
                capturar(a.motor, nombre, args)
                print(f"  {nombre}.png")
            except Exception as e:  # noqa: BLE001
                fallos.append(nombre)
                print(f"  FALLO {nombre}: {e}", file=sys.stderr)
    if a.escaparate:
        escaparate(a.motor)
    if fallos:
        sys.exit(f"Fallaron {len(fallos)} capturas: {', '.join(fallos)}")


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    main()
