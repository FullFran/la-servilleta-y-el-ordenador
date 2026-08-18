"""¿Cómo se pasa del orden al caos? Una ecuación de una línea lo enseña.

Diagrama de bifurcación del mapa logístico x -> r x (1-x), con los cuatro
regímenes marcados, y una telaraña que muestra el mecanismo.

La figura responde: ¿el caos es ruido, o es determinismo?

Ejecutar:  python fig_mapa_logistico.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

fig = plt.figure(figsize=(11.0, 5.2))
gs = fig.add_gridspec(2, 2, width_ratios=[2.1, 1], hspace=0.42, wspace=0.24)

# --- Diagrama de bifurcación ---------------------------------------------
ax = fig.add_subplot(gs[:, 0])
n_r, n_iter, n_guarda = 2400, 900, 250
rs = np.linspace(2.5, 4.0, n_r)
x = np.full(n_r, 0.4)
for i in range(n_iter):
    x = rs * x * (1 - x)
    if i >= n_iter - n_guarda:
        ax.plot(rs, x, ",", color=C.ink, alpha=0.28, markersize=0.4)
for r_c, etiqueta in [(3.0, "1 → 2"), (3.449, "2 → 4"), (3.544, "4 → 8"),
                      (3.5699, "caos")]:
    ax.axvline(r_c, color=C.red, lw=0.9, alpha=0.6)
    ax.text(r_c - 0.012, 0.03, etiqueta, rotation=90, fontsize=7.4,
            color=C.red, ha="right", va="bottom")
ax.axvspan(3.8280, 3.8415, color=C.green, alpha=0.25)
ax.annotate("ventana de periodo 3", xy=(3.835, 0.62), xytext=(3.30, 0.13),
            fontsize=8.4, color=C.green,
            arrowprops=dict(arrowstyle="->", color=C.green, lw=1.1))
ax.set_xlabel("parámetro $r$"), ax.set_ylabel("valores visitados $x$")
ax.set_title("Cascada de duplicación de periodo: el camino al caos")
ax.set_ylim(0, 1)

# --- Telarañas -----------------------------------------------------------
def telarana(ax, r, x0=0.2, n=60):
    x = np.linspace(0, 1, 300)
    ax.plot(x, r * x * (1 - x), color=C.blue, lw=1.8)
    ax.plot(x, x, color=C.grey, lw=1.0)
    px, py = x0, 0.0
    for _ in range(n):
        ny = r * px * (1 - px)
        ax.plot([px, px], [py, ny], color=C.red, lw=0.7, alpha=0.75)
        ax.plot([px, ny], [ny, ny], color=C.red, lw=0.7, alpha=0.75)
        px, py = ny, ny
    ax.set_xlim(0, 1), ax.set_ylim(0, 1)
    ax.set_xlabel("$x_n$"), ax.set_ylabel("$x_{n+1}$")

ax1 = fig.add_subplot(gs[0, 1]); telarana(ax1, 2.8)
ax1.set_title("$r=2{,}8$: un punto fijo", fontsize=9.5)
ax2 = fig.add_subplot(gs[1, 1]); telarana(ax2, 3.9)
ax2.set_title("$r=3{,}9$: caos determinista", fontsize=9.5)

save(fig, "fig_mapa_logistico")
