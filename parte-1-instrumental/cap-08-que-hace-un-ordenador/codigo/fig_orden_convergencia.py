"""¿Cómo se comprueba que un método numérico hace lo que promete?

Error global frente al paso, en ejes logarítmicos, para Euler, Euler mejorado
y Runge-Kutta 4, sobre un problema con solución exacta.

La figura responde: ¿qué es el «orden» de un método, y cómo se mide en dos
líneas?

Ejecutar:  python fig_orden_convergencia.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

# Problema de prueba: y' = -2y + sin(t),  y(0)=1,  con solución exacta
def f(t, y):
    return -2 * y + np.sin(t)


def exacta(t):
    # solución particular + homogénea, ajustada a y(0)=1
    a = (2 * np.sin(t) - np.cos(t)) / 5
    return (1 + 1 / 5) * np.exp(-2 * t) + a


def euler(f, y0, t0, t1, n):
    h = (t1 - t0) / n
    y, t = y0, t0
    for _ in range(n):
        y += h * f(t, y)
        t += h
    return y


def heun(f, y0, t0, t1, n):
    h = (t1 - t0) / n
    y, t = y0, t0
    for _ in range(n):
        k1 = f(t, y)
        k2 = f(t + h, y + h * k1)
        y += h * (k1 + k2) / 2
        t += h
    return y


def rk4(f, y0, t0, t1, n):
    h = (t1 - t0) / n
    y, t = y0, t0
    for _ in range(n):
        k1 = f(t, y)
        k2 = f(t + h / 2, y + h * k1 / 2)
        k3 = f(t + h / 2, y + h * k2 / 2)
        k4 = f(t + h, y + h * k3)
        y += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += h
    return y


T = 2.0
ns = np.array([2**k for k in range(2, 20)])
hs = T / ns
y_ref = exacta(T)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.2, 4.2))

for metodo, nombre, color, orden in [(euler, "Euler", C.red, 1),
                                     (heun, "Euler mejorado (Heun)", C.ochre, 2),
                                     (rk4, "Runge–Kutta 4", C.blue, 4)]:
    err = np.array([abs(metodo(f, 1.0, 0.0, T, int(n)) - y_ref) for n in ns])
    err = np.maximum(err, 1e-17)
    ax1.loglog(hs, err, "o-", color=color, ms=4, lw=1.5, label=nombre)
    # pendiente medida en la zona limpia
    m = (err > 1e-13) & (err < 1e-3)   # sólo el régimen asintótico limpio
    if m.sum() > 2:
        p = np.polyfit(np.log10(hs[m]), np.log10(err[m]), 1)[0]
        print(f"{nombre:24s} orden medido = {p:.2f}  (teórico {orden})")

for orden, color in [(1, C.red), (2, C.ochre), (4, C.blue)]:
    ax1.loglog(hs, 0.3 * hs**orden, ":", color=color, lw=1.0)
ax1.set_xlabel("paso $h$"), ax1.set_ylabel("error global en $t=2$")
ax1.set_title("La pendiente en log-log **es** el orden")
ax1.legend(fontsize=8, loc="lower right")
ax1.set_ylim(1e-17, 1e0)

# --- Panel 2: coste, no paso ---------------------------------------------
for metodo, nombre, color, evals in [(euler, "Euler", C.red, 1),
                                     (heun, "Heun", C.ochre, 2),
                                     (rk4, "RK4", C.blue, 4)]:
    err = np.array([abs(metodo(f, 1.0, 0.0, T, int(n)) - y_ref) for n in ns])
    ax2.loglog(ns * evals, np.maximum(err, 1e-17), "o-", color=color, ms=4,
               lw=1.5, label=nombre)
ax2.set_xlabel("evaluaciones de $f$ (coste real)")
ax2.set_ylabel("error global")
ax2.set_title("Lo que importa no es el paso: es el coste")
ax2.legend(fontsize=8)
ax2.set_ylim(1e-17, 1e0)
ax2.annotate("para el mismo coste,\nRK4 acierta $10^{9}$ veces mejor",
             xy=(1e3, 1e-13), xytext=(1.2e1, 1e-9), fontsize=8.4, color=C.blue,
             arrowprops=dict(arrowstyle="->", color=C.blue, lw=1.0))

save(fig, "fig_orden_convergencia")
