"""Cuando el término pequeño manda: capas límite.

Problema eps y'' + y' + y = 0 con y(0)=0, y(1)=1: solución exacta, solución
exterior, solución interior y su empalme.

La figura responde: ¿por qué despreciar el término con el parámetro pequeño
puede ser catastrófico?

Ejecutar:  python fig_capa_limite.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

x = np.linspace(0, 1, 3000)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))

for eps, color in zip([0.2, 0.05, 0.01], [C.ochre, C.green, C.blue]):
    # raíces de eps m^2 + m + 1 = 0
    disc = np.sqrt(1 - 4 * eps)
    m1 = (-1 + disc) / (2 * eps)          # lenta, ~ -1
    m2 = (-1 - disc) / (2 * eps)          # rápida, ~ -1/eps
    A = 1 / (np.exp(m1) - np.exp(m2))
    y = A * (np.exp(m1 * x) - np.exp(m2 * x))
    ax1.plot(x, y, color=color, lw=1.8, label=f"$\\epsilon$ = {eps}")
    print(f"eps={eps}: m1={m1:.3f}, m2={m2:.1f}, anchura de capa ~ {eps:.3f}")

# Solución exterior (ignorando el término eps y''): y' + y = 0 con y(1)=1
ax1.plot(x, np.exp(1 - x), "--", color=C.red, lw=2.0,
         label=r"exterior: $e^{1-x}$")
ax1.plot(0, np.e, "o", color=C.red, ms=7)
ax1.annotate("la exterior no cumple\n$y(0)=0$", xy=(0, np.e),
             xytext=(0.25, 2.3), fontsize=8.6, color=C.red,
             arrowprops=dict(arrowstyle="->", color=C.red, lw=1.0))
ax1.set_xlabel("$x$"), ax1.set_ylabel("$y$")
ax1.set_title("Despreciar el término pequeño rompe la condición de contorno")
ax1.legend(fontsize=8, loc="upper right")

# --- Empalme --------------------------------------------------------------
eps = 0.02
disc = np.sqrt(1 - 4 * eps)
m1, m2 = (-1 + disc) / (2 * eps), (-1 - disc) / (2 * eps)
A = 1 / (np.exp(m1) - np.exp(m2))
exacta = A * (np.exp(m1 * x) - np.exp(m2 * x))
exterior = np.exp(1 - x)
interior = np.e * (1 - np.exp(-x / eps))
compuesta = exterior + np.e * (-np.exp(-x / eps))

ax2.plot(x, exacta, color=C.ink, lw=2.6, label="exacta", alpha=0.9)
ax2.plot(x, exterior, "--", color=C.red, lw=1.5, label="exterior")
ax2.plot(x, interior, ":", color=C.blue, lw=2.0, label="interior")
ax2.plot(x, compuesta, "-", color=C.green, lw=1.5, label="compuesta")
ax2.axvspan(0, 5 * eps, color=C.grey, alpha=0.18)
ax2.text(5 * eps + 0.02, 0.5, f"capa límite\nde anchura $\\epsilon$ = {eps}",
         fontsize=8.4, color=C.ink)
ax2.set_xlabel("$x$"), ax2.set_ylabel("$y$")
ax2.set_title(r"Empalme asintótico ($\epsilon = 0{,}02$)")
ax2.legend(fontsize=8, loc="lower right")
print(f"error máximo de la compuesta: {np.abs(compuesta-exacta).max():.4f}")

save(fig, "fig_capa_limite")
