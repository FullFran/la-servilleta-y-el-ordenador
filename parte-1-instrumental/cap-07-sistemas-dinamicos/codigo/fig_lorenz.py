"""El sistema de Lorenz: tres ecuaciones, ninguna predicción a largo plazo.

Atractor de Lorenz proyectado, dos trayectorias que empiezan a 1e-9 de
distancia, y el crecimiento exponencial de su separación.

La figura responde: ¿qué significa exactamente «sensibilidad a las condiciones
iniciales», medido en números?

Ejecutar:  python fig_lorenz.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

SIGMA, RHO, BETA = 10.0, 28.0, 8.0 / 3.0


def lorenz(_t, y):
    x, yy, z = y
    return [SIGMA * (yy - x), x * (RHO - z) - yy, x * yy - BETA * z]


# Transitorio de entrada al atractor: si empezamos fuera de él, la separación
# se contrae durante el transitorio y el exponente medido sale falseado.
quema = solve_ivp(lorenz, (0, 30), [1.0, 1.0, 1.0], rtol=1e-12, atol=1e-14)
y0 = quema.y[:, -1]

T_MAX = 30.0
tt = np.linspace(0, T_MAX, 40_000)
sol1 = solve_ivp(lorenz, (0, T_MAX), y0, t_eval=tt, rtol=1e-12, atol=1e-14)
sol2 = solve_ivp(lorenz, (0, T_MAX), y0 + np.array([1e-9, 0, 0]), t_eval=tt,
                 rtol=1e-12, atol=1e-14)

fig = plt.figure(figsize=(11.0, 4.6))
gs = fig.add_gridspec(2, 2, width_ratios=[1, 1.25], hspace=0.45)

# --- Atractor -------------------------------------------------------------
ax = fig.add_subplot(gs[:, 0])
ax.plot(sol1.y[0], sol1.y[2], color=C.blue, lw=0.35, alpha=0.85)
ax.set_xlabel("$x$"), ax.set_ylabel("$z$")
ax.set_title("Atractor de Lorenz (proyección $x$–$z$)")

# --- Dos trayectorias -----------------------------------------------------
ax = fig.add_subplot(gs[0, 1])
ax.plot(tt, sol1.y[0], color=C.blue, lw=0.9, label="$x_0 = 1$")
ax.plot(tt, sol2.y[0], color=C.red, lw=0.9, alpha=0.85,
        label="$x_0 = 1 + 10^{-9}$")
ax.set_ylabel("$x(t)$")
ax.set_title("Una diferencia de $10^{-9}$ en el dato inicial", fontsize=10)
ax.legend(fontsize=8, loc="lower left")
ax.set_xlim(0, T_MAX)

# --- Separación -----------------------------------------------------------
ax = fig.add_subplot(gs[1, 1])
d = np.linalg.norm(sol1.y - sol2.y, axis=0)
ax.semilogy(tt, np.maximum(d, 1e-16), color=C.ink, lw=1.2)
ventana = (tt > 1) & (tt < 20)          # antes de saturar en el atractor
ajuste = np.polyfit(tt[ventana], np.log(d[ventana]), 1)
ax.semilogy(tt, np.exp(np.polyval(ajuste, tt)), "--", color=C.red, lw=1.5,
            label=f"$e^{{\\lambda t}}$, $\\lambda$ = {ajuste[0]:.2f}")
ax.axhline(30, color=C.grey, ls=":", lw=1.2)
ax.text(1, 40, "tamaño del atractor: predicción perdida", fontsize=8,
        color=C.grey)
ax.set_ylim(1e-10, 1e3), ax.set_xlim(0, T_MAX)
ax.set_xlabel("tiempo"), ax.set_ylabel("separación")
ax.legend(fontsize=8, loc="lower right")

print(f"exponente de Lyapunov medido: {ajuste[0]:.3f}  (valor aceptado ~0,906)")
t_horizonte = (np.log(30) - np.log(1e-9)) / ajuste[0]
print(f"horizonte de predicción con error inicial 1e-9: {t_horizonte:.1f}")
save(fig, "fig_lorenz")
