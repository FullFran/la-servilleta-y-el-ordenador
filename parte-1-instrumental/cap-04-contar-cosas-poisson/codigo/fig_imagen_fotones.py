"""¿Por qué una foto con poca luz sale con grano?

Simula la misma imagen recogida con números crecientes de fotones. La figura
responde: ¿cómo se ve, literalmente, que el ruido relativo baja como
1/sqrt(N)?

Ejecutar:  python fig_imagen_fotones.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(4)

# Escena sintética: dos discos y un gradiente suave
n_pix = 120
y, x = np.mgrid[0:n_pix, 0:n_pix] / n_pix
escena = 0.25 + 0.35 * x
escena += 0.45 * (((x - 0.32) ** 2 + (y - 0.62) ** 2) < 0.022)
escena += 0.30 * (((x - 0.70) ** 2 + (y - 0.35) ** 2) < 0.010)
escena /= escena.max()

FOTONES = [1, 10, 100, 1000, 10_000, 100_000]

fig, axes = plt.subplots(2, 3, figsize=(10.4, 6.4))
for ax, n_medio in zip(axes.ravel(), FOTONES):
    imagen = r.poisson(escena * n_medio)
    ax.imshow(imagen, cmap="gray", interpolation="nearest")
    ax.set_xticks([]), ax.set_yticks([]), ax.grid(False)
    snr = np.sqrt(n_medio)
    ax.set_title(f"$\\langle N\\rangle$ = {n_medio:,} fotones/píxel\n"
                 f"ruido relativo $\\approx$ {100/snr:.1f} %".replace(",", " "),
                 fontsize=9.5)

fig.suptitle("La misma escena, seis exposiciones: el grano es Poisson, no el "
             "sensor", fontsize=11.5, y=0.99)
save(fig, "fig_imagen_fotones")
