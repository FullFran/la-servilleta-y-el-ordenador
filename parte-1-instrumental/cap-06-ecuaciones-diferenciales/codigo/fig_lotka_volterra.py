"""Dos ecuaciones acopladas: ¿por qué oscilan los linces y las liebres?

Modelo de Lotka-Volterra: series temporales, retrato de fases y la cantidad
conservada que explica las órbitas cerradas.

La figura responde: ¿por qué las oscilaciones no se amortiguan, y qué le pasa
al sistema si matas depredadores?

Ejecutar:  python fig_lotka_volterra.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

ALFA, BETA, GAMMA, DELTA = 1.1, 0.4, 0.4, 0.1


def lv(_t, y):
    presa, depredador = y
    return [ALFA * presa - BETA * presa * depredador,
            DELTA * presa * depredador - GAMMA * depredador]


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.2, 4.2))

sol = solve_ivp(lv, (0, 60), [10, 5], dense_output=True, rtol=1e-10)
tt = np.linspace(0, 60, 2000)
y = sol.sol(tt)
ax1.plot(tt, y[0], color=C.green, lw=2, label="presas")
ax1.plot(tt, y[1], color=C.red, lw=2, label="depredadores")
ax1.set_xlabel("tiempo"), ax1.set_ylabel("población")
ax1.set_title("Las presas van por delante; los depredadores, detrás")
ax1.legend(fontsize=8.5)

for x0 in [6, 10, 16, 24]:
    s = solve_ivp(lv, (0, 60), [x0, 5], dense_output=True, rtol=1e-10)
    ts = np.linspace(0, 60, 3000)
    ax2.plot(*s.sol(ts), lw=1.5)
ax2.plot(GAMMA / DELTA, ALFA / BETA, "o", color=C.ink, ms=7, zorder=5)
ax2.annotate("punto fijo\n(coexistencia)", (GAMMA / DELTA, ALFA / BETA),
             textcoords="offset points", xytext=(10, 6), fontsize=8.4)
ax2.set_xlabel("presas"), ax2.set_ylabel("depredadores")
ax2.set_title("Órbitas cerradas: hay una cantidad conservada")

# Campo de direcciones
X, Y = np.meshgrid(np.linspace(0.5, 30, 18), np.linspace(0.2, 9, 14))
U = ALFA * X - BETA * X * Y
V = DELTA * X * Y - GAMMA * Y
norma = np.hypot(U, V)
ax2.quiver(X, Y, U / norma, V / norma, color=C.grey, alpha=0.45,
           width=0.003, scale=38)

save(fig, "fig_lotka_volterra")
