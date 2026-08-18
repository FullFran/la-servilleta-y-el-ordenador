"""¿Cómo se barre un espacio de parámetros sin desperdiciar CPU?

Rejilla, aleatorio e hipercubo latino en 2D, y la cobertura de las
proyecciones unidimensionales.

La figura responde: ¿por qué una rejilla es una idea peor de lo que parece?

Ejecutar:  python fig_muestreo_parametros.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import qmc

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(16)

N = 25
rejilla = np.stack(np.meshgrid(np.linspace(0.1, 0.9, 5),
                               np.linspace(0.1, 0.9, 5)), -1).reshape(-1, 2)
aleatorio = r.random((N, 2))
lhs = qmc.LatinHypercube(d=2, seed=5).random(N)

fig, axes = plt.subplots(2, 3, figsize=(10.6, 5.4),
                         gridspec_kw={"height_ratios": [2.4, 1], "hspace": 0.35})

for col, (puntos, nombre, color) in enumerate([
        (rejilla, "Rejilla $5\\times5$", C.red),
        (aleatorio, "Aleatorio", C.ochre),
        (lhs, "Hipercubo latino", C.green)]):
    ax = axes[0, col]
    ax.plot(puntos[:, 0], puntos[:, 1], "o", color=color, ms=7)
    for k in np.linspace(0, 1, 26):
        ax.axvline(k, color=C.grey, lw=0.3, alpha=0.5)
    ax.set_xlim(0, 1), ax.set_ylim(0, 1), ax.set_aspect("equal")
    ax.set_xlabel("$p_1$"), ax.set_ylabel("$p_2$")
    ax.set_title(nombre, fontsize=10)
    ax.grid(False)

    ax = axes[1, col]
    ax.hist(puntos[:, 0], bins=25, range=(0, 1), color=color, alpha=0.75)
    ax.set_xlabel("proyección sobre $p_1$")
    ax.set_yticks([0, 1, 5])
    valores_distintos = len(np.unique(np.round(puntos[:, 0], 6)))
    ax.set_title(f"{valores_distintos} valores distintos de $p_1$", fontsize=9)
    print(f"{nombre:22s}: {valores_distintos} valores distintos de p1 "
          f"con {len(puntos)} simulaciones")

save(fig, "fig_muestreo_parametros")
