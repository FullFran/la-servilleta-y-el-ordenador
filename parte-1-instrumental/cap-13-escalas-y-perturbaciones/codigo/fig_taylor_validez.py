"""Una aproximación no es buena o mala: es buena hasta cierto punto. ¿Cuál?

Desarrollos de Taylor de sin(x) y de 1/(1+x) con su error, y el radio de
validez para una tolerancia dada.

La figura responde: ¿hasta dónde puedo usar «para ángulos pequeños»?

Ejecutar:  python fig_taylor_validez.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import math
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))

x = np.linspace(0, 3.0, 800)
ordenes = [(1, r"$x$"), (3, r"$x-\frac{x^3}{6}$"),
           (5, r"$x-\frac{x^3}{6}+\frac{x^5}{120}$")]
colores = [C.red, C.ochre, C.green]

for (n, etiqueta), color in zip(ordenes, colores):
    aprox = sum((-1)**k * x**(2 * k + 1) / math.factorial(2 * k + 1)
                for k in range((n + 1) // 2))
    err = np.abs(aprox - np.sin(x)) / np.maximum(np.abs(np.sin(x)), 1e-12)
    ax1.semilogy(x, np.maximum(err, 1e-17), color=color, lw=1.8, label=etiqueta)
    for tol in (0.01,):
        idx = np.argmax(err > tol)
        if idx:
            ax1.plot(x[idx], tol, "o", color=color, ms=6)
            print(f"sin(x) con {etiqueta}: error < 1 % hasta x = {x[idx]:.3f} rad "
                  f"= {np.degrees(x[idx]):.0f}°")

ax1.axhline(0.01, color=C.ink, ls="--", lw=1.2)
ax1.text(0.05, 0.013, "tolerancia del 1 %", fontsize=8.4, color=C.ink)
ax1.set_xlabel("$x$ (rad)"), ax1.set_ylabel("error relativo")
ax1.set_title(r"$\sin x$: ¿hasta dónde vale «ángulo pequeño»?")
ax1.legend(fontsize=9, loc="lower right")
ax1.set_ylim(1e-14, 2)

# --- Serie con radio de convergencia finito ------------------------------
x2 = np.linspace(0, 1.6, 800)
for n, color in zip([2, 5, 10, 30], [C.red, C.ochre, C.green, C.blue]):
    aprox = sum((-x2)**k for k in range(n + 1))
    err = np.abs(aprox - 1 / (1 + x2))
    ax2.semilogy(x2, np.maximum(err, 1e-17), color=color, lw=1.5,
                 label=f"{n} términos")
ax2.axvline(1.0, color=C.ink, lw=1.6)
ax2.text(1.03, 1e-10, "radio de\nconvergencia", fontsize=8.4, color=C.ink)
ax2.set_xlabel("$x$"), ax2.set_ylabel("error absoluto")
ax2.set_title(r"$1/(1+x)$: más términos no siempre ayudan")
ax2.legend(fontsize=8, loc="lower right")
ax2.set_ylim(1e-14, 1e6)
ax2.annotate("aquí, añadir términos\nempeora el resultado",
             xy=(1.35, 1e3), xytext=(0.15, 1e3), fontsize=8.4, color=C.red,
             arrowprops=dict(arrowstyle="->", color=C.red, lw=1.0))

save(fig, "fig_taylor_validez")
