"""De la EDO a la EDP: ¿por qué hay un paso de tiempo máximo?

Ecuación del calor resuelta con diferencias finitas explícitas, justo por
debajo y justo por encima del límite CFL.

La figura responde: ¿qué relación hay entre el paso espacial y el temporal, y
qué pasa si la violas?

Ejecutar:  python fig_cfl_calor.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

NX, L, D = 101, 1.0, 1.0
dx = L / (NX - 1)
x = np.linspace(0, L, NX)
u0 = np.where(np.abs(x - 0.5) < 0.12, 1.0, 0.0)


def resuelve(r, t_final):
    """r = D dt / dx^2  es el número adimensional que decide todo."""
    dt = r * dx**2 / D
    n = int(t_final / dt)
    u = u0.copy()
    guardados = []
    for i in range(n):
        u[1:-1] = u[1:-1] + r * (u[2:] - 2 * u[1:-1] + u[:-2])
        if i in {0, n // 8, n // 3, n - 1}:
            guardados.append(u.copy())
    return guardados, dt, n


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.2, 4.1))

for ax, r, titulo in [(ax1, 0.49, "$r = 0{,}49$: estable"),
                      (ax2, 0.51, "$r = 0{,}51$: inestable")]:
    guardados, dt, n = resuelve(r, 0.004)
    for k, u in enumerate(guardados):
        ax.plot(x, u, lw=1.6, alpha=0.85,
                label=f"paso {[0, n//8, n//3, n-1][k]}")
    ax.set_xlabel("$x$"), ax.set_ylabel("$u$")
    ax.set_title(f"{titulo}   ($\\Delta t = {dt:.1e}$)", fontsize=10)
    ax.legend(fontsize=7.6)
    print(f"r={r}: máximo final = {abs(guardados[-1]).max():.3e}")

ax2.set_ylim(-3, 3)
ax2.text(0.02, 2.2, "la solución oscila\ny crece sin control", fontsize=8.6,
         color=C.red)
ax1.text(0.02, 0.85, "difunde, como debe", fontsize=8.6, color=C.green)

save(fig, "fig_cfl_calor")
