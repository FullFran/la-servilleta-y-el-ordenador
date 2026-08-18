"""¿Por qué una bacteria no puede nadar como un pez?

Mapa del número de Reynolds de nadadores y voladores, de la bacteria al
avión. La figura responde: ¿cuántas décadas de Re separan a los seres vivos, y
dónde está la frontera entre «manda la viscosidad» y «manda la inercia»?

Ejecutar:  python fig_mapa_reynolds.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

# (nombre, longitud L en m, velocidad U en m/s, fluido)
CASOS = [
    ("Bacteria (E. coli)", 2e-6, 3e-5, "agua"),
    ("Espermatozoide", 5e-5, 2e-4, "agua"),
    ("Paramecio", 2e-4, 1e-3, "agua"),
    ("Larva de mosquito", 5e-3, 2e-2, "agua"),
    ("Renacuajo", 2e-2, 5e-2, "agua"),
    ("Sardina", 0.15, 1.0, "agua"),
    ("Persona nadando", 1.8, 1.5, "agua"),
    ("Atún", 2.0, 10.0, "agua"),
    ("Ballena azul", 25.0, 5.0, "agua"),
    ("Mosca de la fruta", 3e-3, 1.0, "aire"),
    ("Abeja", 1.3e-2, 5.0, "aire"),
    ("Gorrión", 0.15, 10.0, "aire"),
    ("Águila", 0.9, 20.0, "aire"),
    ("Airbus A320", 37.0, 250.0, "aire"),
]
NU = {"agua": 1.0e-6, "aire": 1.5e-5}      # viscosidad cinemática, m^2/s

fig, ax = plt.subplots(figsize=(8.6, 5.0))

for nombre, L, U, fluido in CASOS:
    Re = L * U / NU[fluido]
    color = C.blue if fluido == "agua" else C.ochre
    ax.plot(Re, L, "o", color=color, ms=7, zorder=4)
    ax.annotate(nombre, (Re, L), textcoords="offset points",
                xytext=(8, 4), fontsize=7.8, color=color)

# Fronteras de régimen
ax.axvspan(1e-8, 1, color=C.green, alpha=0.10)
ax.axvspan(1, 1e3, color=C.grey, alpha=0.10)
ax.axvspan(1e3, 1e10, color=C.red, alpha=0.07)
for x, txt, col in [(1e-4, "manda la viscosidad\n$Re \\ll 1$", C.green),
                    (30, "zona de nadie", C.grey),
                    (1e6, "manda la inercia\n$Re \\gg 1$", C.red)]:
    ax.text(x, 3e-6, txt, fontsize=8.6, color=col, ha="center", va="bottom")

ax.set_xscale("log"), ax.set_yscale("log")
ax.set_xlim(1e-6, 1e9), ax.set_ylim(1e-6, 2e2)
ax.set_xlabel("número de Reynolds  $Re = UL/\\nu$")
ax.set_ylabel("tamaño característico $L$ (m)")
ax.set_title("Quince décadas de Reynolds, dos mundos físicos distintos")

save(fig, "fig_mapa_reynolds")
