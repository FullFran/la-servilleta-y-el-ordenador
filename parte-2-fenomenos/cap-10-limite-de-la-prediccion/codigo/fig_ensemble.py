"""¿Cuándo deja de ser posible predecir?

Predicción por conjuntos en el sistema de Lorenz: 200 trayectorias con
condiciones iniciales ligeramente distintas, y la evolución de la dispersión.

La figura responde: ¿qué se puede afirmar cuando la trayectoria individual ya
no significa nada?

Ejecutar:  python fig_ensemble.py
"""
import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(63)
S, RHO, B = 10.0, 28.0, 8 / 3


def lorenz(_t, y):
    y = y.reshape(3, -1)
    x, yy, z = y
    return np.vstack([S * (yy - x), x * (RHO - z) - yy, x * yy - B * z]).ravel()


quema = solve_ivp(lambda t, y: lorenz(t, y), (0, 40), [1, 1, 1], rtol=1e-12)
y0 = quema.y[:, -1]

M = 200
inicio = (y0[:, None] + r.normal(0, 0.05, (3, M))).ravel()
T = 12.0
tt = np.linspace(0, T, 1200)
sol = solve_ivp(lorenz, (0, T), inicio, t_eval=tt, rtol=1e-10, atol=1e-12)
Y = sol.y.reshape(3, M, -1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))

for k in range(0, M, 2):
    ax1.plot(tt, Y[0, k], color=C.blue, lw=0.35, alpha=0.35)
ax1.plot(tt, Y[0].mean(axis=0), color=C.red, lw=2.0, label="media del conjunto")
ax1.fill_between(tt, np.percentile(Y[0], 5, axis=0),
                 np.percentile(Y[0], 95, axis=0), color=C.red, alpha=0.15,
                 label="banda 5–95 %")
ax1.set_xlabel("tiempo"), ax1.set_ylabel("$x$")
ax1.set_title("200 predicciones con datos iniciales casi iguales")
ax1.legend(fontsize=8.5, loc="lower left")

disp = Y[0].std(axis=0)
ax2.semilogy(tt, disp, color=C.ink, lw=2.0, label="dispersión del conjunto")
m = (tt > 1) & (tt < 6)
p = np.polyfit(tt[m], np.log(disp[m]), 1)
ax2.semilogy(tt, np.exp(np.polyval(p, tt)), "--", color=C.red, lw=1.5,
             label=f"$e^{{\\lambda t}}$, $\\lambda$={p[0]:.2f}")
ax2.axhline(Y[0].std(), color=C.grey, ls=":", lw=1.4)
ax2.text(0.3, Y[0].std() * 1.15, "dispersión climatológica: predicción perdida",
         fontsize=8, color=C.grey)
ax2.set_xlabel("tiempo"), ax2.set_ylabel("desviación típica de $x$")
ax2.set_title("La dispersión crece y satura")
ax2.legend(fontsize=8.5, loc="lower right")

i_sat = int(np.argmax(disp > 0.9 * Y[0].std()))
print(f"lambda medido = {p[0]:.3f}")
print(f"horizonte útil (dispersión = 90 % de la climatológica): "
      f"t = {tt[i_sat]:.1f}")
save(fig, "fig_ensemble")
