#!/usr/bin/env python3
"""Escribe seta.vox (formato de MagicaVoxel) para las capturas de «Importar modelos»."""
import struct
from pathlib import Path

N = 16
vox = []
c = (N - 1) / 2
for z in range(N):            # en MagicaVoxel, Z es la altura
    for y in range(N):
        for x in range(N):
            dx, dy = x - c, y - c
            r2 = dx * dx + dy * dy
            if z < 7 and r2 <= 6:                       # pie
                vox.append((x, y, z, 2))
            elif 7 <= z < 12:                           # sombrero
                rr = 7.5 - (z - 7) * 1.2
                if r2 <= rr * rr:
                    borde = r2 > (rr - 1.4) ** 2 or z == 11
                    mancha = borde and ((x * 3 + y * 5 + z * 7) % 9 == 0)
                    vox.append((x, y, z, 3 if mancha else 1))
paleta = [(0, 0, 0, 0)] * 256
paleta[0] = (214, 58, 46, 255)    # índice 1: rojo
paleta[1] = (236, 226, 204, 255)  # índice 2: pie
paleta[2] = (255, 255, 255, 255)  # índice 3: manchas


def chunk(nombre, datos, hijos=b""):
    return nombre + struct.pack("<ii", len(datos), len(hijos)) + datos + hijos


size = chunk(b"SIZE", struct.pack("<iii", N, N, N))
xyzi = chunk(b"XYZI", struct.pack("<i", len(vox)) + b"".join(struct.pack("<BBBB", *v) for v in vox))
rgba = chunk(b"RGBA", b"".join(struct.pack("<BBBB", *p) for p in paleta))
main = chunk(b"MAIN", b"", size + xyzi + rgba)
Path(__file__).with_name("seta.vox").write_bytes(b"VOX " + struct.pack("<i", 150) + main)
print(len(vox), "cubitos")
