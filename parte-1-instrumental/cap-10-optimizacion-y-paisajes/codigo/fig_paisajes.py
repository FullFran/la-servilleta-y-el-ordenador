"""¿Por qué el descenso por gradiente funciona a veces y a veces no?

Tres paisajes: convexo, mal condicionado y rugoso. Sobre cada uno, la
trayectoria del descenso por gradiente desde varios puntos de partida.

La figura responde: ¿qué propiedad del paisaje decide si el problema es fácil?

Ejecutar:  python fig_paisajes.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()


def descenso(grad, x0, paso, n=300):
    x = np.array(x0, dtype=float)
    camino = [x.copy()]
    for _ in range(n):
        g = grad(x)
        x = x - paso * g
        camino.append(x.copy())
        if np.linalg.norm(g) < 1e-8:
            break
    return np.array(camino)


PAISAJES = [
    ("Convexo y bien condicionado\n$f=x^2+y^2$",
     lambda x, y: x**2 + y**2,
     lambda v: np.array([2 * v[0], 2 * v[1]]), 0.15, C.green),
    ("Convexo, mal condicionado\n$f=x^2+50y^2$",
     lambda x, y: x**2 + 50 * y**2,
     lambda v: np.array([2 * v[0], 100 * v[1]]), 0.018, C.ochre),
    ("Rugoso\n$f=x^2+y^2+3\\sin^2(3x)\\sin^2(3y)$",
     lambda x, y: x**2 + y**2 + 3 * np.sin(3 * x)**2 * np.sin(3 * y)**2,
     lambda v: np.array([
         2 * v[0] + 18 * np.sin(3 * v[0]) * np.cos(3 * v[0]) * np.sin(3 * v[1])**2,
         2 * v[1] + 18 * np.sin(3 * v[1]) * np.cos(3 * v[1]) * np.sin(3 * v[0])**2]),
     0.03, C.red),
]

fig, axes = plt.subplots(1, 3, figsize=(11.6, 4.0))
X, Y = np.meshgrid(np.linspace(-2.2, 2.2, 300), np.linspace(-2.2, 2.2, 300))

for ax, (titulo, f, grad, paso, color) in zip(axes, PAISAJES):
    Z = f(X, Y)
    ax.contourf(X, Y, Z, levels=30, cmap="Blues_r", alpha=0.55)
    ax.contour(X, Y, Z, levels=18, colors=[C.grey], linewidths=0.5, alpha=0.6)
    for x0 in [(-2.0, 1.8), (1.9, 1.5), (-1.6, -1.9), (2.0, -0.4)]:
        camino = descenso(grad, x0, paso)
        ax.plot(camino[:, 0], camino[:, 1], "-", color=color, lw=1.4, alpha=0.9)
        ax.plot(*camino[0], "o", color=C.ink, ms=4)
        ax.plot(*camino[-1], "*", color=color, ms=11, mec=C.ink, mew=0.6)
    ax.set_title(titulo, fontsize=9.5)
    ax.set_xlabel("$x$"), ax.set_ylabel("$y$")
    ax.set_aspect("equal")
    ax.grid(False)

axes[1].text(-2.1, -2.05, "zigzag: el gradiente\nno apunta al mínimo",
             fontsize=8, color=C.ochre)
axes[2].text(-2.1, -2.05, "cada salida acaba\nen un sitio distinto",
             fontsize=8, color=C.red)
save(fig, "fig_paisajes")
