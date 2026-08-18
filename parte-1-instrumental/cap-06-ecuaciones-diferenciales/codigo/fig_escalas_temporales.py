"""Cuando un sistema tiene dos relojes, ¿cuál manda?

Sistema de dos compartimentos con constantes muy distintas. Se muestra la
solución completa y las dos aproximaciones: la rápida y la lenta.

La figura responde: ¿qué significa «separación de escalas» y cuándo se puede
eliminar la variable rápida?

Ejecutar:  python fig_escalas_temporales.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

K_RAPIDA, K_LENTA = 30.0, 0.5      # s^-1


def sistema(_t, y):
    """A -> B (rápida) -> C (lenta)."""
    a, b, _c = y
    return [-K_RAPIDA * a, K_RAPIDA * a - K_LENTA * b, K_LENTA * b]


sol = solve_ivp(sistema, (0, 12), [1.0, 0.0, 0.0], dense_output=True,
                rtol=1e-10, atol=1e-12)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.2, 4.1))

for ax, (t0, t1), titulo in [
        (ax1, (0, 0.35), "Escala rápida: $1/k_1 = 0{,}033$ s"),
        (ax2, (0, 12), "Escala lenta: $1/k_2 = 2$ s")]:
    tt = np.linspace(t0, t1, 600)
    y = sol.sol(tt)
    for i, (nombre, color) in enumerate([("A", C.red), ("B", C.blue),
                                         ("C", C.green)]):
        ax.plot(tt, y[i], color=color, lw=2, label=nombre)
    ax.set_xlabel("tiempo (s)"), ax.set_ylabel("concentración")
    ax.set_title(titulo, fontsize=10)
    ax.legend(fontsize=8.5)

ax1.axvline(1 / K_RAPIDA, color=C.grey, ls=":", lw=1.2)
ax1.text(1 / K_RAPIDA * 1.15, 0.6, r"$t=1/k_1$", fontsize=8.4, color=C.grey)
ax2.plot(np.linspace(0, 12, 300), 1 - np.exp(-K_LENTA * np.linspace(0, 12, 300)),
         "--", color=C.ink, lw=1.4,
         label="aproximación:\nB decae solo")
ax2.legend(fontsize=8)
ax2.annotate("en esta escala, A ya no existe:\nse puede eliminar del modelo",
             xy=(1.0, 0.05), xytext=(3.2, 0.35), fontsize=8.6, color=C.red,
             arrowprops=dict(arrowstyle="->", color=C.red, lw=1.0))

save(fig, "fig_escalas_temporales")
