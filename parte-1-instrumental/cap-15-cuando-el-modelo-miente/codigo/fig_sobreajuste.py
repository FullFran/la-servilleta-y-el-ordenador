"""Sobreajuste: el modelo que aprende el ruido.

Ajuste polinómico de grado creciente a pocos datos: error en entrenamiento, en
validación, y el comportamiento fuera del rango.

La figura responde: ¿cómo se detecta el sobreajuste sin conocer la verdad?

Ejecutar:  python fig_sobreajuste.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(15)

SIGMA = 0.25


def verdad(x):
    return np.sin(1.6 * x) + 0.25 * x


x_ent = np.sort(r.uniform(0, 5, 14))
y_ent = verdad(x_ent) + r.normal(0, SIGMA, x_ent.size)
x_val = np.sort(r.uniform(0, 5, 200))
y_val = verdad(x_val) + r.normal(0, SIGMA, x_val.size)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))

xx = np.linspace(-0.3, 5.6, 500)
for grado, color, ancho in [(1, C.grey, 1.2), (4, C.green, 2.0),
                            (12, C.red, 1.6)]:
    c = np.polyfit(x_ent, y_ent, grado)
    ax1.plot(xx, np.polyval(c, xx), color=color, lw=ancho,
             label=f"grado {grado}")
ax1.plot(xx, verdad(xx), "--", color=C.ink, lw=1.6, label="verdad")
ax1.plot(x_ent, y_ent, "o", color=C.blue, ms=6, label="14 datos")
ax1.set_ylim(-2.6, 3.4), ax1.set_xlim(-0.3, 5.6)
ax1.set_xlabel("$x$"), ax1.set_ylabel("$y$")
ax1.set_title("El grado 12 pasa por todos los puntos")
ax1.legend(fontsize=8, loc="lower left")

grados = np.arange(0, 13)
err_ent, err_val = [], []
for g in grados:
    c = np.polyfit(x_ent, y_ent, g)
    err_ent.append(np.sqrt(np.mean((y_ent - np.polyval(c, x_ent))**2)))
    err_val.append(np.sqrt(np.mean((y_val - np.polyval(c, x_val))**2)))

ax2.semilogy(grados, err_ent, "o-", color=C.blue, ms=5, lw=1.6,
             label="error sobre los 14 datos usados")
ax2.semilogy(grados, err_val, "s-", color=C.red, ms=5, lw=1.6,
             label="error sobre datos nuevos")
ax2.axhline(SIGMA, color=C.ink, ls="--", lw=1.2)
ax2.text(0.2, SIGMA * 1.15, "ruido de medida", fontsize=8.4, color=C.ink)
g_opt = int(np.argmin(err_val))
ax2.axvline(g_opt, color=C.green, lw=1.2)
ax2.text(g_opt + 0.15, 3, f"óptimo: grado {g_opt}", fontsize=8.4, color=C.green)
ax2.set_xlabel("grado del polinomio"), ax2.set_ylabel("error rms")
ax2.set_title("El error de entrenamiento siempre baja")
ax2.legend(fontsize=8)

print(f"grado óptimo por validación: {g_opt}")
for g in (1, 4, 12):
    c = np.polyfit(x_ent, y_ent, g)
    print(f"grado {g:2d}: entrenamiento {np.sqrt(np.mean((y_ent-np.polyval(c,x_ent))**2)):.3f}, "
          f"validación {np.sqrt(np.mean((y_val-np.polyval(c,x_val))**2)):.3f}")
save(fig, "fig_sobreajuste")
