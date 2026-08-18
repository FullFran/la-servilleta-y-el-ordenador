"""¿De verdad se puede hacer una esquina sumando ondas suaves?

Construcción de una onda cuadrada y de un diente de sierra sumando armónicos,
con el fenómeno de Gibbs medido.

La figura responde: ¿converge la serie de Fourier en las discontinuidades?

Ejecutar:  python fig_series_fourier.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

x = np.linspace(-np.pi, np.pi, 4000)


def cuadrada_parcial(x, n_arm):
    s = np.zeros_like(x)
    for k in range(1, n_arm + 1, 2):
        s += (4 / (np.pi * k)) * np.sin(k * x)
    return s


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))

ax1.plot(x, np.sign(np.sin(x)), color=C.ink, lw=2.0, label="onda cuadrada")
for n, color in zip([1, 3, 9, 51], [C.grey, C.ochre, C.green, C.blue]):
    ax1.plot(x, cuadrada_parcial(x, n), color=color, lw=1.3,
             label=f"{(n+1)//2} armónicos")
ax1.set_xlabel("$x$"), ax1.set_ylabel("$f(x)$")
ax1.set_title("Sumando senos impares")
ax1.legend(fontsize=7.6, loc="lower right")
ax1.set_ylim(-1.5, 1.5)

# --- Gibbs -----------------------------------------------------------------
for n, color in zip([11, 51, 201, 1001], [C.ochre, C.green, C.blue, C.red]):
    y = cuadrada_parcial(x, n)
    sobrepaso = y.max()
    ax2.plot(x, y, color=color, lw=1.2,
             label=f"{(n+1)//2} arm.: máx = {sobrepaso:.4f}")
ax2.axhline(1, color=C.ink, lw=1.2)
ax2.axhline(1.17898, color=C.grey, ls="--", lw=1.2)
ax2.text(0.35, 1.19, "límite de Gibbs: 1,17898…", fontsize=8.2, color=C.grey)
ax2.set_xlim(-0.05, 0.6), ax2.set_ylim(0.8, 1.28)
ax2.set_xlabel("$x$ (zoom en la discontinuidad)")
ax2.set_title("El sobrepaso no desaparece: se estrecha")
ax2.legend(fontsize=7.6, loc="lower right")

for n in [11, 51, 201, 1001, 5001]:
    print(f"{(n+1)//2:5d} armónicos -> sobrepaso máximo = "
          f"{cuadrada_parcial(np.linspace(0, 0.5, 20000), n).max():.6f}")
save(fig, "fig_series_fourier")
