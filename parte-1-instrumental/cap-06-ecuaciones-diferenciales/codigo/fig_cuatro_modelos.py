"""Cuatro ecuaciones explican medio mundo. ¿Cuáles y por qué?

Relajación, crecimiento, saturación y oscilación: para cada una, la línea de
fases (dx/dt frente a x) y la solución temporal.

La figura responde: ¿qué te dice la línea de fases que no te dice la solución?

Ejecutar:  python fig_cuatro_modelos.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

MODELOS = [
    ("Relajación\n$\\dot x = -x/\\tau$",
     lambda x: -x / 2.0, np.linspace(-2, 2, 200), [2.0, 1.0, -1.5], (0, 10)),
    ("Crecimiento\n$\\dot x = rx$",
     lambda x: 0.4 * x, np.linspace(-0.5, 3, 200), [0.2, 0.5, 1.0], (0, 6)),
    ("Saturación (logística)\n$\\dot x = rx(1-x/K)$",
     lambda x: 0.8 * x * (1 - x / 1.0), np.linspace(-0.15, 1.4, 200),
     [0.02, 0.4, 1.3], (0, 14)),
    ("Oscilación\n$\\ddot x = -\\omega^2 x$", None, None, None, (0, 14)),
]

fig, axes = plt.subplots(2, 4, figsize=(12.0, 6.0),
                         gridspec_kw={"height_ratios": [1, 1.15],
                                      "wspace": 0.42, "hspace": 0.45})

for col, (titulo, f, malla, inicios, trango) in enumerate(MODELOS):
    ax_f, ax_t = axes[0, col], axes[1, col]

    if f is not None:
        # --- línea de fases -----------------------------------------------
        ax_f.plot(malla, f(malla), color=C.blue, lw=2)
        ax_f.axhline(0, color=C.ink, lw=1.0)
        # puntos fijos y flechas de flujo
        v = f(malla)
        h = 3 * (malla[1] - malla[0])          # margen mayor que el paso de malla
        cruces = malla[:-1][np.sign(v[:-1]) != np.sign(v[1:])]
        for xc in cruces:
            # estable si el flujo apunta hacia el punto fijo por ambos lados
            estable = f(xc + h) < 0 < f(xc - h)
            ax_f.plot(xc, 0, "o", ms=8, color=C.ink if estable else "white",
                      mec=C.ink, mew=1.6, zorder=5)
        for xm in malla[::28]:
            if abs(f(xm)) > 1e-3:
                ax_f.annotate("", xy=(xm + 0.16 * np.sign(f(xm)), 0),
                              xytext=(xm, 0),
                              arrowprops=dict(arrowstyle="->", color=C.red, lw=1.2))
        ax_f.set_xlabel("$x$"), ax_f.set_ylabel(r"$\dot x$")
        ax_f.set_title(titulo, fontsize=9.5)

        # --- soluciones ---------------------------------------------------
        for x0 in inicios:
            sol = solve_ivp(lambda t, y: [f(y[0])], trango, [x0],
                            dense_output=True, rtol=1e-8)
            tt = np.linspace(*trango, 300)
            ax_t.plot(tt, sol.sol(tt)[0], lw=1.8)
        ax_t.set_xlabel("$t$"), ax_t.set_ylabel("$x$")
    else:
        # --- el oscilador necesita dos dimensiones -------------------------
        w = 1.2
        for x0 in (0.4, 0.8, 1.2):
            th = np.linspace(0, 2 * np.pi, 200)
            ax_f.plot(x0 * np.cos(th), -x0 * w * np.sin(th), lw=1.6)
        ax_f.plot(0, 0, "o", ms=7, color="white", mec=C.ink, mew=1.6)
        ax_f.set_xlabel("$x$"), ax_f.set_ylabel(r"$\dot x$")
        ax_f.set_title(titulo, fontsize=9.5)
        ax_f.set_aspect("equal")
        tt = np.linspace(*trango, 400)
        for x0 in (0.4, 0.8, 1.2):
            ax_t.plot(tt, x0 * np.cos(w * tt), lw=1.6)
        ax_t.set_xlabel("$t$"), ax_t.set_ylabel("$x$")

fig.suptitle("Arriba: línea de fases (círculo lleno = estable, hueco = "
             "inestable).  Abajo: solución temporal.",
             fontsize=9.5, color=C.grey, y=1.0)
save(fig, "fig_cuatro_modelos")
