"""Dónde van los números de las capturas anotadas.

nombre de la captura -> lista de puntos (x, y) en píxeles de la imagen. El
primer punto es el número 1. Cada página del panel explica los números en
la tabla que hay debajo de la imagen, en el mismo orden.

Para colocarlos, abre la captura en cualquier visor que diga la posición del
ratón, o rehaz la captura con --solo <nombre> y mírala.
"""

ANOTACIONES: dict[str, list[tuple[int, int]]] = {
    "panel-barra-superior": [(300, 50), (712, 50), (800, 50), (1072, 50), (1160, 50), (1262, 50), (1374, 50)],
    "panel-vista": [(100, 14), (240, 43), (75, 95), (472, 50)],
    "panel-proyecto": [(130, 48), (150, 86), (150, 142), (150, 194), (178, 248)],
    "panel-escena": [(175, 42), (120, 67), (195, 93), (175, 254)],
    "panel-inspector": [(200, 45), (100, 215), (130, 414), (170, 636), (175, 666), (140, 740)],
    "panel-codigo": [(360, 43), (615, 71), (45, 320), (15, 420), (400, 779)],
    "panel-consola": [(182, 30), (395, 62), (330, 80), (360, 165), (320, 318)],
    "panel-depurador": [(400, 53), (300, 88), (130, 129), (90, 177), (210, 255), (100, 358), (130, 411)],
    "panel-nodos": [(545, 62), (62, 71), (75, 114), (115, 532), (500, 86), (540, 700), (810, 71)],
    "panel-archivos": [(80, 43), (380, 51), (580, 79), (300, 134), (820, 134)],
    "panel-materiales": [(150, 111), (260, 201), (60, 239), (870, 113), (600, 194), (705, 247), (625, 346), (755, 511), (895, 55)],
    "panel-pixelart": [(735, 127), (630, 215), (135, 321), (155, 446)],
    "panel-casillas": [(245, 43), (282, 71), (290, 150), (110, 314)],
    "panel-capas": [(185, 43), (210, 82), (135, 104), (95, 276)],
    "panel-sprites": [(345, 51), (395, 79), (60, 114), (130, 190), (110, 251), (130, 560), (985, 624)],
    "panel-animacion": [(560, 43), (575, 71), (100, 132), (530, 113), (85, 157), (565, 198)],
    "panel-estados": [(370, 51), (245, 122), (465, 96), (195, 176), (1015, 82), (1025, 192)],
    "panel-animaciones": [(125, 43), (110, 73), (175, 95), (115, 413)],
    "panel-registro": [(95, 42), (800, 42), (240, 78), (400, 103), (355, 128)],
}
