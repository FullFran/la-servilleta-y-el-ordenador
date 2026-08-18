"""¿Por qué dos parámetros bien determinados pueden dar una predicción pésima?

Ajusta una exponencial a datos ruidosos, dibuja la elipse de covarianza de los
parámetros y muestra el efecto de ignorar su correlación al propagar.

La figura responde: ¿qué información pierdo si sólo guardo las barras de error
y no la matriz de covarianza?

Ejecutar:  python fig_covarianza.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(33)


def modelo(t, A, tau):
    return A * np.exp(-t / tau)


A_REAL, TAU_REAL, SIGMA = 100.0, 4.0, 4.0
t = np.linspace(0, 6, 14)
y = modelo(t, A_REAL, TAU_REAL) + r.normal(0, SIGMA, t.size)

popt, pcov = curve_fit(modelo, t, y, p0=[80, 3], sigma=np.full(t.size, SIGMA),
                       absolute_sigma=True)
sA, stau = np.sqrt(np.diag(pcov))
rho = pcov[0, 1] / (sA * stau)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.2, 4.2))

# --- Elipse de covarianza -------------------------------------------------
vals, vecs = np.linalg.eigh(pcov)
ang = np.degrees(np.arctan2(vecs[1, -1], vecs[0, -1]))
from matplotlib.patches import Ellipse  # noqa: E402
for k, alpha in [(1, 0.30), (2, 0.15)]:
    ax1.add_patch(Ellipse(popt, 2 * k * np.sqrt(vals[-1]), 2 * k * np.sqrt(vals[0]),
                          angle=ang, color=C.blue, alpha=alpha, lw=0))
ax1.add_patch(Ellipse(popt, 2 * sA, 2 * stau, angle=0, fill=False,
                      edgecolor=C.red, lw=1.6, ls="--"))
ax1.plot(*popt, "o", color=C.ink, ms=6)
ax1.plot(A_REAL, TAU_REAL, "*", color=C.green, ms=13)
ax1.set_xlabel("amplitud $A$"), ax1.set_ylabel(r"tiempo característico $\tau$")
ax1.set_title(f"Elipse de covarianza,  $\\rho$ = {rho:.2f}")
ax1.text(0.03, 0.05, "azul: la incertidumbre real\nrojo: lo que crees si\n"
         "sólo guardas $\\sigma_A$ y $\\sigma_\\tau$",
         transform=ax1.transAxes, fontsize=8.4, color=C.ink)

# --- Consecuencia al predecir --------------------------------------------
tt = np.linspace(0, 12, 200)
M = 4000
muestras_ok = r.multivariate_normal(popt, pcov, M)
muestras_mal = np.column_stack([r.normal(popt[0], sA, M),
                                r.normal(popt[1], stau, M)])
for muestras, color, etiqueta in [(muestras_ok, C.blue, "con covarianza"),
                                  (muestras_mal, C.red, "ignorando $\\rho$")]:
    curvas = np.array([modelo(tt, a, tau) for a, tau in muestras])
    lo, hi = np.percentile(curvas, [2.5, 97.5], axis=0)
    ax2.fill_between(tt, lo, hi, color=color, alpha=0.22, label=etiqueta)
ax2.errorbar(t, y, yerr=SIGMA, fmt="o", color=C.ink, ms=4, lw=1, capsize=2)
ax2.plot(tt, modelo(tt, A_REAL, TAU_REAL), color=C.green, lw=1.6,
         label="verdad")
ax2.set_xlabel("$t$"), ax2.set_ylabel("$y$")
ax2.set_title("Banda de predicción al 95 %")
ax2.legend(fontsize=8)

print(f"A = {popt[0]:.1f} ± {sA:.1f}   tau = {popt[1]:.2f} ± {stau:.2f}   "
      f"rho = {rho:.3f}")
save(fig, "fig_covarianza")
