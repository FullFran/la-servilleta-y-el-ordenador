"""¿Por qué un paso «pequeño» a veces explota?

Regiones de estabilidad absoluta en el plano complejo y un ejemplo rígido
donde Euler explícito revienta y el implícito no se inmuta.

La figura responde: ¿qué limita el paso, la precisión que quiero o la
estabilidad del método?

Ejecutar:  python fig_estabilidad.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.3))

# --- Regiones de estabilidad ---------------------------------------------
re = np.linspace(-3.5, 1.5, 700)
im = np.linspace(-3.5, 3.5, 700)
Z = re[None, :] + 1j * im[:, None]

R_euler = 1 + Z
R_heun = 1 + Z + Z**2 / 2
R_rk4 = 1 + Z + Z**2 / 2 + Z**3 / 6 + Z**4 / 24

for R, nombre, color in [(R_euler, "Euler explícito", C.red),
                         (R_heun, "Heun (RK2)", C.ochre),
                         (R_rk4, "RK4", C.blue)]:
    ax1.contour(re, im, np.abs(R), levels=[1.0], colors=[color], linewidths=2)
    ax1.contourf(re, im, np.abs(R), levels=[0, 1.0], colors=[color], alpha=0.13)
    ax1.plot([], [], color=color, lw=2, label=nombre)

ax1.axhline(0, color=C.ink, lw=0.8), ax1.axvline(0, color=C.ink, lw=0.8)
ax1.set_xlabel(r"$\mathrm{Re}(h\lambda)$")
ax1.set_ylabel(r"$\mathrm{Im}(h\lambda)$")
ax1.set_title("Regiones de estabilidad absoluta")
ax1.legend(fontsize=8, loc="upper left")
ax1.set_aspect("equal")
ax1.text(-2.6, -3.1, "el implícito es estable\nen TODO el semiplano izquierdo",
         fontsize=8.2, color=C.green)

# --- Un problema rígido ---------------------------------------------------
LAMBDA = -1000.0        # modo rápido
T = 0.05


def exacta(t):
    return np.exp(LAMBDA * t)


for h, color, estilo in [(0.0018, C.red, "-"), (0.0022, C.ink, "-")]:
    n = int(T / h)
    t = np.arange(n + 1) * h
    y = np.empty(n + 1)
    y[0] = 1.0
    for i in range(n):
        y[i + 1] = y[i] + h * LAMBDA * y[i]
    ax2.plot(t, y, estilo, color=color, lw=1.6, marker="o", ms=3,
             label=f"Euler explícito, $h\\lambda$ = {h*LAMBDA:.1f}")

# Euler implícito con el paso grande
h = 0.0022
n = int(T / h)
t = np.arange(n + 1) * h
y = np.empty(n + 1)
y[0] = 1.0
for i in range(n):
    y[i + 1] = y[i] / (1 - h * LAMBDA)
ax2.plot(t, y, color=C.green, lw=2.0, marker="s", ms=3,
         label=f"Euler implícito, $h\\lambda$ = {h*LAMBDA:.1f}")

tt = np.linspace(0, T, 400)
ax2.plot(tt, exacta(tt), "--", color=C.grey, lw=1.4, label="exacta")
ax2.set_yscale("symlog", linthresh=1e-3)
ax2.set_xlabel("$t$"), ax2.set_ylabel("$y$")
ax2.set_title(r"$\dot y = -1000\,y$: el paso lo fija la estabilidad")
ax2.legend(fontsize=7.6, loc="lower left")

print(f"límite de estabilidad de Euler explícito: h < 2/|lambda| = "
      f"{2/abs(LAMBDA):.4f}")
save(fig, "fig_estabilidad")
