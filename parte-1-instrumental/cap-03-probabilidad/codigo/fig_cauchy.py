"""¿Y si la ley de los grandes números no se cumple?

Compara la media acumulada de muestras normales con la de muestras de Cauchy,
que no tiene media. La figura responde: ¿cómo se ve, en la práctica, que una
distribución no tiene los momentos que damos por supuestos?

Ejecutar:  python fig_cauchy.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(1729)

N = 100_000
n = np.arange(1, N + 1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.2, 4.0), sharey=False)

for _ in range(6):
    x = r.normal(0, 1, N)
    ax1.plot(n, np.cumsum(x) / n, lw=0.8, color=C.blue, alpha=0.7)
ax1.axhline(0, color=C.ink, lw=1.2)
ax1.set_xscale("log"), ax1.set_ylim(-1.2, 1.2)
ax1.set_xlabel("número de muestras")
ax1.set_ylabel("media acumulada")
ax1.set_title("Normal: la media se asienta")

for _ in range(6):
    x = r.standard_cauchy(N)
    ax2.plot(n, np.cumsum(x) / n, lw=0.8, color=C.red, alpha=0.75)
ax2.axhline(0, color=C.ink, lw=1.2)
ax2.set_xscale("log")
ax2.set_xlabel("número de muestras")
ax2.set_title("Cauchy: la media nunca se asienta")
ax2.annotate("un solo dato puede\nmover la media entera",
             xy=(3e3, ax2.get_ylim()[1] * 0.55),
             xytext=(20, ax2.get_ylim()[1] * 0.8), fontsize=8.6, color=C.red,
             arrowprops=dict(arrowstyle="->", color=C.red, lw=1.0))

save(fig, "fig_cauchy")
