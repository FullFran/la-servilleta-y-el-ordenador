"""¿Qué significa que un sistema esté mal condicionado?

Dos sistemas 2x2 con soluciones idénticas: uno bien condicionado y otro casi
singular. Se perturba el término independiente un 1 % y se mira qué pasa.

La figura responde: ¿por qué una matriz puede amplificar tus errores, y cuánto?

Ejecutar:  python fig_condicionamiento.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(31)

CASOS = [
    ("Bien condicionado", np.array([[1.0, 0.2], [0.2, 1.0]])),
    ("Casi singular", np.array([[1.0, 0.999], [0.999, 1.0]])),
]
x_real = np.array([1.0, 1.0])

fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.4))

for ax, (titulo, A) in zip(axes, CASOS):
    b = A @ x_real
    kappa = np.linalg.cond(A)

    # Las dos rectas del sistema
    xx = np.linspace(-3, 5, 200)
    for i, color in zip(range(2), [C.blue, C.red]):
        ax.plot(xx, (b[i] - A[i, 0] * xx) / A[i, 1], color=color, lw=1.8,
                alpha=0.9)

    # 300 perturbaciones del 1 % en b
    soluciones = []
    for _ in range(300):
        bp = b * (1 + 0.01 * r.standard_normal(2))
        soluciones.append(np.linalg.solve(A, bp))
    soluciones = np.array(soluciones)
    ax.plot(soluciones[:, 0], soluciones[:, 1], ".", color=C.ochre, ms=3,
            alpha=0.6)
    ax.plot(*x_real, "*", color=C.ink, ms=15, zorder=6)

    dispersión = np.linalg.norm(soluciones - x_real, axis=1).std()
    ax.set_title(f"{titulo}\n$\\kappa$ = {kappa:.1f},  dispersión = "
                 f"{dispersión:.2f}", fontsize=10)
    ax.set_xlabel("$x_1$"), ax.set_ylabel("$x_2$")
    ax.set_xlim(-2, 4), ax.set_ylim(-2, 4)
    ax.set_aspect("equal")
    print(f"{titulo:22s} kappa = {kappa:8.1f}   dispersión = {dispersión:.3f}")

axes[1].annotate("las dos rectas son\ncasi paralelas",
                 xy=(0.5, 1.5), xytext=(-1.7, 3.2), fontsize=8.6, color=C.red,
                 arrowprops=dict(arrowstyle="->", color=C.red, lw=1.0))
save(fig, "fig_condicionamiento")
