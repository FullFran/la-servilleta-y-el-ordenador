"""¿Por qué promediar mil veces no arregla un error sistemático?

Cuatro dianas con las cuatro combinaciones de sesgo y dispersión, y debajo la
evolución del error de la media con el número de medidas.

La figura responde: ¿qué parte de mi error se reduce midiendo más, y cuál no?

Ejecutar:  python fig_sesgo_dispersion.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(5)

CASOS = [
    ("Sin sesgo, poca dispersión", 0.0, 0.15, C.green),
    ("Sin sesgo, mucha dispersión", 0.0, 0.55, C.blue),
    ("Con sesgo, poca dispersión", 0.85, 0.15, C.red),
    ("Con sesgo, mucha dispersión", 0.85, 0.55, C.ochre),
]

fig = plt.figure(figsize=(10.4, 6.4))
gs = fig.add_gridspec(2, 4, height_ratios=[1.25, 1.0], hspace=0.42, wspace=0.3)

for i, (titulo, sesgo, disp, color) in enumerate(CASOS):
    ax = fig.add_subplot(gs[0, i])
    for radio in (0.4, 0.8, 1.2):
        ax.add_patch(plt.Circle((0, 0), radio, fill=False, color=C.grey, lw=0.8))
    x = r.normal(sesgo, disp, 60)
    y = r.normal(0.0, disp, 60)
    ax.plot(x, y, "o", color=color, ms=4, alpha=0.75)
    ax.plot(0, 0, "+", color=C.ink, ms=12, mew=1.8)
    ax.set_xlim(-1.6, 1.9), ax.set_ylim(-1.6, 1.6)
    ax.set_aspect("equal"), ax.axis("off")
    ax.set_title(titulo, fontsize=9)

# --- Error de la media frente al número de medidas ------------------------
ax = fig.add_subplot(gs[1, :])
n = np.arange(1, 5001)
for titulo, sesgo, disp, color in CASOS:
    error = np.sqrt(sesgo**2 + (disp / np.sqrt(n)) ** 2)
    ax.loglog(n, error, color=color, lw=1.9, label=titulo)
ax.set_xlabel("número de medidas promediadas $n$")
ax.set_ylabel("error de la media")
ax.set_title("El sesgo es un suelo: no se cruza midiendo más")
ax.legend(fontsize=8.4, ncol=2)
ax.annotate("aquí deja de servir\nseguir midiendo", xy=(400, 0.86),
            xytext=(30, 0.30), fontsize=8.6, color=C.red,
            arrowprops=dict(arrowstyle="->", color=C.red, lw=1.0))

save(fig, "fig_sesgo_dispersion")
