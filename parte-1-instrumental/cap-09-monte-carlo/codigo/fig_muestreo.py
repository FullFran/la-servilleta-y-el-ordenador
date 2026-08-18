"""¿Cómo se generan muestras de una distribución que no viene en la biblioteca?

Tres técnicas: transformada inversa, rechazo y muestreo por importancia, con
la reducción de varianza que consigue la tercera.

La figura responde: ¿por qué muestrear «donde importa» reduce el error sin
introducir sesgo?

Ejecutar:  python fig_muestreo.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(13)

fig, axes = plt.subplots(1, 3, figsize=(11.6, 3.9))

# --- 1. Transformada inversa ---------------------------------------------
ax = axes[0]
u = np.linspace(0.001, 0.999, 400)
x = -np.log(1 - u)                       # inversa de la exponencial
ax.plot(u, x, color=C.blue, lw=2)
for uu in [0.2, 0.5, 0.8, 0.95]:
    xx = -np.log(1 - uu)
    ax.plot([0, uu, uu], [xx, xx, 0], color=C.red, lw=1.0, alpha=0.8)
    ax.plot(uu, 0, "o", color=C.red, ms=4)
ax.set_xlabel("$u$ uniforme en [0,1]"), ax.set_ylabel("$x = F^{-1}(u)$")
ax.set_title("Transformada inversa\n$x=-\\ln(1-u)$", fontsize=9.5)
ax.set_xlim(0, 1), ax.set_ylim(0, 3.5)

# --- 2. Rechazo -----------------------------------------------------------
ax = axes[1]
def objetivo(x):
    return np.exp(-x**2 / 2) * (1 + 0.7 * np.sin(4 * x)**2)

xx = np.linspace(-3.5, 3.5, 400)
M = 1.75
ax.plot(xx, objetivo(xx), color=C.blue, lw=2, label="$p(x)$ (sin normalizar)")
ax.plot(xx, M * np.exp(-xx**2 / 2), "--", color=C.ochre, lw=1.6,
        label="$M q(x)$ propuesta")
n = 500
xs = r.normal(0, 1, n)
us = r.uniform(0, M * np.exp(-xs**2 / 2), n)
acepta = us <= objetivo(xs)
ax.plot(xs[acepta], us[acepta], ".", color=C.green, ms=3, alpha=0.75)
ax.plot(xs[~acepta], us[~acepta], ".", color=C.red, ms=3, alpha=0.5)
ax.set_xlabel("$x$"), ax.set_ylabel("altura sorteada")
ax.set_title(f"Rechazo\naceptación = {acepta.mean():.0%}", fontsize=9.5)
ax.legend(fontsize=7.4, loc="upper right")

# --- 3. Importancia -------------------------------------------------------
ax = axes[2]
# Estimar P(X > 4) para una normal estándar: suceso raro
UMBRAL = 4.0
exacto = 3.167124e-5
Ns = np.unique(np.logspace(2, 6, 20).astype(int))
err_directo, err_import = [], []
for N in Ns:
    directo = (r.normal(0, 1, N) > UMBRAL).mean()
    err_directo.append(abs(directo - exacto) / exacto)
    # propuesta desplazada al umbral
    y = r.normal(UMBRAL, 1, N)
    peso = np.exp(-y**2 / 2) / np.exp(-(y - UMBRAL)**2 / 2)
    estimador = (peso * (y > UMBRAL)).mean()
    err_import.append(abs(estimador - exacto) / exacto)

ax.loglog(Ns, np.maximum(err_directo, 1e-6), "o-", color=C.red, ms=4, lw=1.4,
          label="muestreo directo")
ax.loglog(Ns, err_import, "s-", color=C.green, ms=4, lw=1.4,
          label="por importancia")
ax.set_xlabel("número de muestras $N$")
ax.set_ylabel("error relativo")
ax.set_title(r"Suceso raro: $P(X>4)=3{,}2\times10^{-5}$", fontsize=9.5)
ax.legend(fontsize=8)
ax.annotate("con $10^3$ muestras el directo\nno ve ni un suceso",
            xy=(1e3, 1.0), xytext=(3e3, 0.12), fontsize=8, color=C.red,
            arrowprops=dict(arrowstyle="->", color=C.red, lw=1.0))

save(fig, "fig_muestreo")
