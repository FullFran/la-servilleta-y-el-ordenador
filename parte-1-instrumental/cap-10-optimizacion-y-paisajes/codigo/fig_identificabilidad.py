"""¿Por qué un ajuste puede converger a un número sin significado?

Paisaje de coste de dos ajustes: uno con parámetros identificables y otro donde
sólo una combinación está determinada.

La figura responde: ¿cómo se ve, en el paisaje, que un parámetro no es
identificable?

Ejecutar:  python fig_identificabilidad.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(77)

SIGMA = 0.05

# --- Caso 1: bien determinado -------------------------------------------
t1 = np.linspace(0, 6, 25)
y1 = 2.0 * np.exp(-t1 / 1.5) + r.normal(0, SIGMA, t1.size)

# --- Caso 2: dos exponenciales casi iguales (mal determinado) -----------
t2 = np.linspace(0, 3, 25)
y2 = 1.0 * np.exp(-t2 / 1.0) + 1.0 * np.exp(-t2 / 1.15) + r.normal(0, SIGMA, t2.size)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))

# Paisaje 1: A y tau de una sola exponencial
A = np.linspace(1.2, 3.0, 220)
TAU = np.linspace(0.9, 2.4, 220)
AA, TT = np.meshgrid(A, TAU)
chi1 = np.zeros_like(AA)
for ti, yi in zip(t1, y1):
    chi1 += ((yi - AA * np.exp(-ti / TT)) / SIGMA) ** 2
chi1 -= chi1.min()

cs = ax1.contourf(AA, TT, np.log10(chi1 + 1), levels=25, cmap="Blues_r")
ax1.contour(AA, TT, chi1, levels=[2.30, 6.17, 11.8], colors=[C.red],
            linewidths=[1.8, 1.2, 0.9])
ax1.plot(2.0, 1.5, "*", color=C.ink, ms=14)
ax1.set_xlabel("amplitud $A$"), ax1.set_ylabel(r"tiempo $\tau$")
ax1.set_title("Identificable: el mínimo es un pozo")
ax1.grid(False)
ax1.text(1.3, 2.25, "contornos: 1, 2 y 3$\\sigma$", fontsize=8, color=C.red)

# Paisaje 2: los dos tau de la suma de exponenciales
TAU1 = np.linspace(0.5, 2.2, 220)
TAU2 = np.linspace(0.5, 2.2, 220)
T1, T2 = np.meshgrid(TAU1, TAU2)
chi2 = np.zeros_like(T1)
for ti, yi in zip(t2, y2):
    chi2 += ((yi - np.exp(-ti / T1) - np.exp(-ti / T2)) / SIGMA) ** 2
chi2 -= chi2.min()

ax2.contourf(T1, T2, np.log10(chi2 + 1), levels=25, cmap="Blues_r")
ax2.contour(T1, T2, chi2, levels=[2.30, 6.17, 11.8], colors=[C.red],
            linewidths=[1.8, 1.2, 0.9])
ax2.plot(1.0, 1.15, "*", color=C.ink, ms=14)
ax2.plot(1.15, 1.0, "*", color=C.ink, ms=14, alpha=0.6)
ax2.set_xlabel(r"$\tau_1$"), ax2.set_ylabel(r"$\tau_2$")
ax2.set_title("No identificable: el mínimo es un valle")
ax2.grid(False)
ax2.annotate("todo este valle ajusta\nigual de bien", xy=(1.5, 0.75),
             xytext=(0.6, 1.9), fontsize=8.6, color=C.red,
             arrowprops=dict(arrowstyle="->", color=C.red, lw=1.1))

save(fig, "fig_identificabilidad")
