"""Cuatro modelos que coinciden en los datos y divergen fuera.

Ajuste de exponencial, logística, ley de potencias y polinomio a los mismos 20
puntos, con las predicciones extendidas al doble del rango.

La figura responde: ¿qué parte de una extrapolación viene de los datos y qué
parte de la física que has supuesto?

Ejecutar:  python fig_extrapolacion.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(151)

# "Verdad": logística en fase inicial
K, R, N0 = 4000.0, 0.42, 12.0
t_datos = np.arange(0, 11, 0.5)   # sólo la fase inicial: ahí todos coinciden
verdad = K / (1 + (K / N0 - 1) * np.exp(-R * t_datos))
y = verdad * np.exp(r.normal(0, 0.08, t_datos.size))

MODELOS = [
    ("exponencial", lambda t, a, b: a * np.exp(b * t), [10, 0.4], C.red),
    ("logística", lambda t, k, rr, n0: k / (1 + (k / n0 - 1) * np.exp(-rr * t)),
     [3000, 0.4, 12], C.green),
    ("ley de potencias", lambda t, a, p: a * (t + 1)**p, [10, 2.5], C.ochre),
    ("polinomio grado 3", lambda t, a, b, c, d: a + b * t + c * t**2 + d * t**3,
     [10, 1, 1, 1], C.purple),
]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))
tt = np.linspace(0, 40, 400)

for nombre, f, p0, color in MODELOS:
    try:
        p, _ = curve_fit(f, t_datos, y, p0=p0, maxfev=60000)
    except Exception:
        continue
    ajuste = f(t_datos, *p)
    rms = np.sqrt(np.mean((np.log(y) - np.log(np.abs(ajuste) + 1e-9))**2))
    ax1.plot(t_datos, ajuste, color=color, lw=1.8, label=f"{nombre} (rms {rms:.3f})")
    ax2.semilogy(tt, np.abs(f(tt, *p)), color=color, lw=1.8, label=nombre)
    print(f"{nombre:20s} rms(log) en los datos = {rms:.4f}   "
          f"predicción en t=40: {f(40.0, *p):.3g}")

ax1.plot(t_datos, y, "o", color=C.ink, ms=5, label="datos")
ax1.set_xlabel("$t$"), ax1.set_ylabel("$N$")
ax1.set_title("Dentro del rango: tres se distinguen a duras penas")
ax1.legend(fontsize=7.6)

verdad_larga = K / (1 + (K / N0 - 1) * np.exp(-R * tt))
ax2.semilogy(tt, verdad_larga, "--", color=C.ink, lw=2.0, label="verdad")
ax2.axvspan(0, 10, color=C.grey, alpha=0.18)
ax2.text(0.6, 3e6, "rango medido", fontsize=8.6, color=C.ink)
ax2.set_xlabel("$t$"), ax2.set_ylabel("$N$")
ax2.set_title("Fuera del rango: cuatro órdenes y medio de diferencia")
ax2.legend(fontsize=7.6, loc="lower right")
ax2.set_ylim(1, 1e9)

save(fig, "fig_extrapolacion")
