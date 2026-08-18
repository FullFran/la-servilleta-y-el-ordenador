"""¿Cómo puede un sistema cambiar de comportamiento de golpe?

Las cuatro bifurcaciones locales básicas: silla-nodo, transcrítica, horquilla
y Hopf. Para cada una, el diagrama de puntos fijos frente al parámetro.

La figura responde: ¿qué le ocurre a un sistema cuando cruza un umbral, y por
qué a veces no se puede volver atrás?

Ejecutar:  python fig_bifurcaciones.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()
fig, axes = plt.subplots(1, 4, figsize=(12.0, 3.4))

def dibuja(ax, r_est, x_est, r_ines, x_ines, titulo, ecuacion):
    ax.plot(r_est, x_est, color=C.blue, lw=2.2, label="estable")
    ax.plot(r_ines, x_ines, "--", color=C.red, lw=2.0, label="inestable")
    ax.axvline(0, color=C.grey, ls=":", lw=1.1)
    ax.set_xlabel("parámetro $r$"), ax.set_ylabel("puntos fijos $x^*$")
    ax.set_title(f"{titulo}\n{ecuacion}", fontsize=9.5)

# --- Silla-nodo: dos puntos fijos que chocan y desaparecen ---------------
r = np.linspace(0, 2, 200)
dibuja(axes[0], r, np.sqrt(r), r, -np.sqrt(r),
       "Silla-nodo", r"$\dot x = r + x^2$  (aquí $\dot x = r - x^2$)")
axes[0].annotate("aquí desaparecen\nlos dos a la vez", xy=(0, 0),
                 xytext=(0.55, -1.05), fontsize=8.2, color=C.ink,
                 arrowprops=dict(arrowstyle="->", color=C.ink, lw=1.0))
axes[0].set_xlim(-1.2, 2)

# --- Transcrítica: dos puntos fijos que se cruzan e intercambian ---------
r = np.linspace(-2, 2, 200)
axes[1].plot(r[r < 0], np.zeros_like(r[r < 0]), color=C.blue, lw=2.2)
axes[1].plot(r[r >= 0], np.zeros_like(r[r >= 0]), "--", color=C.red, lw=2.0)
axes[1].plot(r[r < 0], r[r < 0], "--", color=C.red, lw=2.0)
axes[1].plot(r[r >= 0], r[r >= 0], color=C.blue, lw=2.2)
axes[1].axvline(0, color=C.grey, ls=":", lw=1.1)
axes[1].set_xlabel("parámetro $r$")
axes[1].set_title("Transcrítica\n$\\dot x = rx - x^2$", fontsize=9.5)
axes[1].annotate("se intercambian\nla estabilidad", xy=(0, 0),
                 xytext=(-1.9, 1.2), fontsize=8.2, color=C.ink,
                 arrowprops=dict(arrowstyle="->", color=C.ink, lw=1.0))

# --- Horquilla supercrítica ---------------------------------------------
r = np.linspace(-2, 2, 200)
axes[2].plot(r[r < 0], np.zeros_like(r[r < 0]), color=C.blue, lw=2.2)
axes[2].plot(r[r >= 0], np.zeros_like(r[r >= 0]), "--", color=C.red, lw=2.0)
rp = r[r >= 0]
axes[2].plot(rp, np.sqrt(rp), color=C.blue, lw=2.2)
axes[2].plot(rp, -np.sqrt(rp), color=C.blue, lw=2.2)
axes[2].axvline(0, color=C.grey, ls=":", lw=1.1)
axes[2].set_xlabel("parámetro $r$")
axes[2].set_title("Horquilla\n$\\dot x = rx - x^3$", fontsize=9.5)
axes[2].annotate("ruptura de simetría", xy=(1.0, 1.0), xytext=(-1.9, 1.15),
                 fontsize=8.2, color=C.ink,
                 arrowprops=dict(arrowstyle="->", color=C.ink, lw=1.0))

# --- Hopf: nace un ciclo límite ------------------------------------------
r = np.linspace(-2, 2, 200)
axes[3].plot(r[r < 0], np.zeros_like(r[r < 0]), color=C.blue, lw=2.2)
axes[3].plot(r[r >= 0], np.zeros_like(r[r >= 0]), "--", color=C.red, lw=2.0)
rp = r[r >= 0]
axes[3].plot(rp, np.sqrt(rp), color=C.green, lw=2.2)
axes[3].plot(rp, -np.sqrt(rp), color=C.green, lw=2.2)
axes[3].fill_between(rp, -np.sqrt(rp), np.sqrt(rp), color=C.green, alpha=0.10)
axes[3].axvline(0, color=C.grey, ls=":", lw=1.1)
axes[3].set_xlabel("parámetro $r$")
axes[3].set_title("Hopf\namplitud del ciclo límite", fontsize=9.5)
axes[3].annotate("nace una oscilación\nsostenida", xy=(1.2, 1.1),
                 xytext=(-1.9, -1.3), fontsize=8.2, color=C.green,
                 arrowprops=dict(arrowstyle="->", color=C.green, lw=1.0))

axes[0].legend(fontsize=8, loc="upper left")
save(fig, "fig_bifurcaciones")
