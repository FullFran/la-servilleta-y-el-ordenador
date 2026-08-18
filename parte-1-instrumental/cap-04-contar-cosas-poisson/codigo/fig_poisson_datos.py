"""¿Se cumple Poisson con datos reales de hace un siglo?

Compara dos conjuntos de datos históricos con la ley de Poisson: los conteos
de partículas alfa de Rutherford, Geiger y Bateman (1910) y las muertes por
coz de caballo en el ejército prusiano de Bortkiewicz (1898).

La figura responde: ¿es Poisson una idealización o describe datos reales?

Ejecutar:  python fig_poisson_datos.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

# --- Rutherford, Geiger y Bateman (1910): 2608 intervalos de 7,5 s --------
alfa_k = np.arange(0, 15)
alfa_n = np.array([57, 203, 383, 525, 532, 408, 273, 139, 45, 27, 10, 4, 0, 1, 1])

# --- Bortkiewicz (1898): 200 cuerpo-años del ejército prusiano ------------
coz_k = np.arange(0, 5)
coz_n = np.array([109, 65, 22, 3, 1])

fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.2))

for ax, k, n, titulo, unidad in [
    (axes[0], alfa_k, alfa_n, "Partículas $\\alpha$ en 7,5 s\nRutherford, Geiger y "
     "Bateman (1910)", "intervalos"),
    (axes[1], coz_k, coz_n, "Muertes por coz de caballo\nBortkiewicz (1898)",
     "cuerpo-años"),
]:
    total = n.sum()
    media = (k * n).sum() / total
    varianza = ((k - media) ** 2 * n).sum() / total
    esperado = total * stats.poisson.pmf(k, media)

    ax.bar(k, n, color=C.blue, alpha=0.55, width=0.75, label="observado")
    ax.plot(k, esperado, "o-", color=C.red, ms=5, lw=1.4,
            label=f"Poisson($\\lambda$={media:.2f})")
    ax.set_xlabel("número de sucesos en el intervalo")
    ax.set_ylabel(f"número de {unidad}")
    ax.set_title(titulo, fontsize=10)
    ax.legend()
    ax.text(0.97, 0.62,
            f"media = {media:.3f}\nvarianza = {varianza:.3f}\n"
            f"cociente = {varianza/media:.3f}",
            transform=ax.transAxes, ha="right", va="top", fontsize=8.8,
            color=C.ink,
            bbox=dict(boxstyle="round,pad=0.4", fc=C.light, ec=C.grey, lw=0.6))
    print(f"{titulo.splitlines()[0]}: media={media:.3f} var={varianza:.3f} "
          f"var/media={varianza/media:.3f}")

save(fig, "fig_poisson_datos")
