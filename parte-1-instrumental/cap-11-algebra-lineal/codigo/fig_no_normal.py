"""Todos los autovalores estables y el sistema crece igualmente. ¿Cómo?

Crecimiento transitorio en una matriz no normal: la energía se multiplica por
mil antes de decaer, aunque los dos autovalores sean negativos.

La figura responde: ¿basta con mirar los autovalores para saber si un sistema
es estable en la práctica?

Ejecutar:  python fig_no_normal.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import expm

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

# Matriz no normal: autovalores -1 y -2, pero autovectores casi paralelos
A = np.array([[-1.0, 200.0], [0.0, -2.0]])
lam = np.linalg.eigvals(A)

t = np.linspace(0, 12, 2000)
crecimiento = np.array([np.linalg.norm(expm(A * ti), 2) for ti in t])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))

ax1.semilogy(t, crecimiento, color=C.red, lw=2.0,
             label=r"$\|e^{At}\|$ real")
ax1.semilogy(t, np.exp(np.max(lam.real) * t), "--", color=C.blue, lw=1.8,
             label=r"$e^{\lambda_{\max}t}$ (lo que dicen los autovalores)")
ax1.axhline(1, color=C.grey, lw=1.0)
ax1.set_xlabel("tiempo"), ax1.set_ylabel("amplificación")
ax1.set_title("Autovalores $-1$ y $-2$: ambos estables")
ax1.legend(fontsize=8)
ax1.annotate(f"amplificación máxima: ×{crecimiento.max():.0f}",
             xy=(t[np.argmax(crecimiento)], crecimiento.max()),
             xytext=(3.5, 3), fontsize=8.6, color=C.red,
             arrowprops=dict(arrowstyle="->", color=C.red, lw=1.0))

# --- Trayectorias en el plano --------------------------------------------
for ang in np.linspace(0, np.pi, 9)[:-1]:
    x0 = np.array([np.cos(ang), np.sin(ang)])
    tr = np.array([expm(A * ti) @ x0 for ti in np.linspace(0, 6, 400)])
    ax2.plot(tr[:, 0], tr[:, 1], color=C.blue, lw=1.0, alpha=0.8)
    ax2.plot(*x0, "o", color=C.ink, ms=3)
th = np.linspace(0, 2 * np.pi, 200)
ax2.plot(np.cos(th), np.sin(th), "--", color=C.grey, lw=1.2)
ax2.set_xlabel("$x_1$"), ax2.set_ylabel("$x_2$")
ax2.set_title("Salen del círculo unidad antes de volver")
ax2.set_xlim(-60, 60), ax2.set_ylim(-1.3, 1.3)

print(f"autovalores: {lam}")
print(f"amplificación transitoria máxima: {crecimiento.max():.1f}")
print(f"número de condición de los autovectores: "
      f"{np.linalg.cond(np.linalg.eig(A)[1]):.1f}")
save(fig, "fig_no_normal")
