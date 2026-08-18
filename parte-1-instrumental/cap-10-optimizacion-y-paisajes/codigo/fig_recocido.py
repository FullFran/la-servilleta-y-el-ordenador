"""Recocido simulado: ¿por qué aceptar empeorar ayuda a mejorar?

Optimización de una función rugosa en 1D con tres temperaturas fijas y con un
enfriamiento programado, mostrando la mejor solución encontrada.

La figura responde: ¿qué papel juega exactamente la temperatura?

Ejecutar:  python fig_recocido.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(1983)


def energia(x):
    """Pozo suave con mínimos locales profundos: hay barreras reales."""
    return 0.05 * x**2 + 3.0 * np.sin(2.0 * x)


def recocido(T_prog, n=40_000, x0=8.0, paso=0.35):
    x, E = x0, energia(x0)
    mejor_x, mejor_E = x, E
    camino = np.empty(n)
    for i in range(n):
        T = T_prog(i / n)
        y = x + r.normal(0, paso)
        Ey = energia(y)
        if Ey < E or (T > 0 and r.random() < np.exp(-(Ey - E) / T)):
            x, E = y, Ey
            if E < mejor_E:
                mejor_x, mejor_E = x, E
        camino[i] = x
    return camino, mejor_x, mejor_E


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2),
                               gridspec_kw={"width_ratios": [1, 1.2]})

xx = np.linspace(-10, 10, 2000)
ax1.plot(xx, energia(xx), color=C.ink, lw=1.6)
ax1.set_xlabel("$x$"), ax1.set_ylabel("energía $E(x)$")
ax1.set_title("Un paisaje con muchos mínimos locales")
x_opt = xx[np.argmin(energia(xx))]
ax1.plot(x_opt, energia(x_opt), "*", color=C.green, ms=15, zorder=5)
ax1.annotate("mínimo global", (x_opt, energia(x_opt)),
             textcoords="offset points", xytext=(10, -18), fontsize=8.4,
             color=C.green)

PROGRAMAS = [
    (lambda u: 1e-4, "$T$ = $10^{-4}$ (casi cero)", C.red),
    (lambda u: 6.0, "$T$ = 6 (muy caliente)", C.ochre),
    (lambda u: 6.0 * (1e-4 / 6.0) ** u, "enfriamiento exponencial", C.green),
]
for prog, nombre, color in PROGRAMAS:
    camino, mejor_x, mejor_E = recocido(prog)
    ax2.plot(camino, color=color, lw=0.4, alpha=0.75)
    ax1.plot(mejor_x, energia(mejor_x), "o", color=color, ms=7, zorder=6)
    print(f"{nombre:32s} mejor E = {mejor_E:+.4f}  en x = {mejor_x:+.3f}")
    ax2.plot([], [], color=color, lw=2, label=f"{nombre}: $E$ = {mejor_E:.3f}")

ax2.axhline(x_opt, color=C.ink, ls="--", lw=1.2)
ax2.text(500, x_opt + 0.35, "posición del mínimo global", fontsize=8,
         color=C.ink)
ax2.set_xlabel("iteración"), ax2.set_ylabel("$x$ visitada")
ax2.set_title("Demasiado frío se atasca; demasiado caliente no se posa")
ax2.legend(fontsize=8, loc="upper right")
ax2.set_ylim(-10, 10)

save(fig, "fig_recocido")
