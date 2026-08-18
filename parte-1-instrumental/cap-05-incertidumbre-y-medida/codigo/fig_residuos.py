"""Un ajuste con R^2 = 0,998 puede estar completamente mal. ¿Cómo se ve?

Ajusta una recta a datos que en realidad siguen una ley cuadrática suave y
compara con el ajuste correcto. La clave está abajo: los residuos.

La figura responde: ¿qué gráfica detecta un modelo mal especificado, si el
coeficiente de determinación no lo detecta?

Ejecutar:  python fig_residuos.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(21)

# Datos "experimentales": una curvatura suave más ruido
x = np.linspace(0, 10, 40)
sigma = 0.6
y_real = 2.0 + 1.2 * x + 0.09 * x**2
y = y_real + r.normal(0, sigma, x.size)

ajuste_lineal = np.polyfit(x, y, 1)
ajuste_cuad = np.polyfit(x, y, 2)
res_lin = y - np.polyval(ajuste_lineal, x)
res_cua = y - np.polyval(ajuste_cuad, x)


def r2(res):
    return 1 - np.sum(res**2) / np.sum((y - y.mean()) ** 2)


def chi2_red(res, k):
    return np.sum((res / sigma) ** 2) / (x.size - k)


fig, axes = plt.subplots(2, 2, figsize=(10.2, 6.0), sharex=True,
                         gridspec_kw={"height_ratios": [1.6, 1]})

for col, (nombre, ajuste, res, k) in enumerate([
        ("Modelo lineal", ajuste_lineal, res_lin, 2),
        ("Modelo cuadrático", ajuste_cuad, res_cua, 3)]):
    ax = axes[0, col]
    ax.errorbar(x, y, yerr=sigma, fmt="o", color=C.red, ms=4, lw=1,
                capsize=2, label="datos")
    xx = np.linspace(0, 10, 200)
    ax.plot(xx, np.polyval(ajuste, xx), color=C.blue, lw=2, label="ajuste")
    ax.set_ylabel("$y$")
    ax.set_title(f"{nombre}:  $R^2$ = {r2(res):.4f},  "
                 f"$\\chi^2_\\nu$ = {chi2_red(res, k):.2f}", fontsize=10)
    ax.legend(fontsize=8)

    ax = axes[1, col]
    ax.axhline(0, color=C.ink, lw=1.2)
    ax.axhspan(-sigma, sigma, color=C.grey, alpha=0.18)
    ax.plot(x, res, "o-", color=C.ochre if col == 0 else C.green, ms=4, lw=1)
    ax.set_xlabel("$x$"), ax.set_ylabel("residuo")
    if col == 0:
        ax.annotate("estructura:\nel modelo está mal", xy=(5, res_lin[20]),
                    xytext=(2.2, 1.35), fontsize=8.8, color=C.red,
                    arrowprops=dict(arrowstyle="->", color=C.red, lw=1.0))
    else:
        ax.text(0.4, 1.35, "sin estructura: sólo ruido", fontsize=8.8,
                color=C.green)
    ax.set_ylim(-1.9, 1.9)

print(f"lineal:     R2={r2(res_lin):.4f}  chi2red={chi2_red(res_lin,2):.2f}")
print(f"cuadrático: R2={r2(res_cua):.4f}  chi2red={chi2_red(res_cua,3):.2f}")
save(fig, "fig_residuos")
