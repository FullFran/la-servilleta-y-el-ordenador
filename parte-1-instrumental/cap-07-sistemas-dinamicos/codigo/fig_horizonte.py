"""Si mejoro mi medida inicial por un factor 1000, ¿cuánto gano en predicción?

Relación entre precisión inicial y horizonte de predicción en un sistema
caótico, y comparación con un sistema no caótico.

La figura responde: ¿por qué mejorar los datos iniciales da tan poco?

Ejecutar:  python fig_horizonte.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

LAMBDA = 0.906          # exponente de Lyapunov del sistema de Lorenz
TOLERANCIA = 1.0        # error admisible en la predicción

eps = np.logspace(-15, -1, 300)      # error del dato inicial

fig, ax = plt.subplots(figsize=(7.6, 4.2))

t_caotico = np.log(TOLERANCIA / eps) / LAMBDA
t_lineal = TOLERANCIA / eps * 1e-3   # crecimiento lineal del error, escalado

ax.semilogx(eps, t_caotico, color=C.red, lw=2.2,
            label=r"caótico: $t_h \sim \frac{1}{\lambda}\ln(1/\epsilon)$")
ax.semilogx(eps, t_lineal, color=C.blue, lw=2.2,
            label=r"no caótico: $t_h \sim 1/\epsilon$")
ax.set_ylim(0, 45)

for e, txt in [(1e-3, ""), (1e-6, ""), (1e-9, ""), (1e-12, "")]:
    t = np.log(TOLERANCIA / e) / LAMBDA
    ax.plot(e, t, "o", color=C.ink, ms=5)
    ax.annotate(f"$10^{{{int(np.log10(e))}}}$ → {t:.0f}", (e, t),
                textcoords="offset points", xytext=(6, -12), fontsize=8)

ax.annotate("mil veces mejor medida\n= sólo 7,6 unidades más de predicción",
            xy=(1e-9, np.log(1e9) / LAMBDA),
            xytext=(2e-14, 33), fontsize=8.8, color=C.red,
            arrowprops=dict(arrowstyle="->", color=C.red, lw=1.0))

ax.set_xlabel(r"error del dato inicial $\epsilon$")
ax.set_ylabel("horizonte de predicción")
ax.set_title("El precio del caos: el horizonte crece como el logaritmo")
ax.legend(fontsize=9, loc="upper right")

save(fig, "fig_horizonte")
