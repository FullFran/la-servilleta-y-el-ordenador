"""¿Por qué multiplicar seis números malos puede dar un resultado bueno?

Simula estimaciones con n factores, cada uno con el mismo error logarítmico
independiente, y compara el error total con las dos hipótesis extremas:
que los errores se sumen (peor caso) o que se cancelen en raíz de n.

La figura responde: ¿cuánto crece realmente el error de una estimación al
añadir factores?

Ejecutar:  python fig_cancelacion.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
aleatorio = rng(7)

SIGMA = 0.30            # incertidumbre de cada factor, en décadas (dex)
N_MAX = 12
N_MUESTRAS = 40_000
ns = np.arange(1, N_MAX + 1)

# Cada factor aporta un error log-normal de anchura SIGMA dex
errores = aleatorio.normal(0.0, SIGMA, size=(N_MUESTRAS, N_MAX))
acumulado = np.cumsum(errores, axis=1)
sigma_simulada = acumulado.std(axis=0)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 4.0))

# --- Panel 1: crecimiento del error ---------------------------------------
ax1.plot(ns, SIGMA * ns, "--", color=C.red, lw=1.6,
         label="si los errores se sumaran:  $n\\sigma$")
ax1.plot(ns, SIGMA * np.sqrt(ns), "-", color=C.blue, lw=2.0,
         label="si son independientes:  $\\sqrt{n}\\,\\sigma$")
ax1.plot(ns, sigma_simulada, "o", color=C.ink, ms=5,
         label="simulación (40 000 estimaciones)")
ax1.set_xlabel("número de factores $n$")
ax1.set_ylabel("incertidumbre total (décadas)")
ax1.set_title("El error crece como $\\sqrt{n}$, no como $n$")
ax1.legend(loc="upper left")

# Eje derecho: la misma incertidumbre leída como «factor de error»
sec = ax1.secondary_yaxis(
    "right", functions=(lambda d: d, lambda d: d))
sec.set_yticks([np.log10(f) for f in (2, 3, 10, 30, 100, 1000)])
sec.set_yticklabels([f"×{f}" for f in (2, 3, 10, 30, 100, 1000)], fontsize=8)
sec.set_ylabel("factor de error equivalente", fontsize=9)

# --- Panel 2: distribución del resultado para n = 6 -----------------------
n_demo = 6
muestras = acumulado[:, n_demo - 1]
ax2.hist(muestras, bins=90, color=C.blue, alpha=0.55, density=True,
         edgecolor="none", label=f"$n={n_demo}$ factores")
ax2.hist(acumulado[:, 0], bins=90, color=C.grey, alpha=0.45, density=True,
         edgecolor="none", label="$n=1$ factor")

for q, estilo in [(0.05, ":"), (0.95, ":")]:
    ax2.axvline(np.quantile(muestras, q), color=C.red, ls=estilo, lw=1.3)
p05, p95 = np.quantile(muestras, [0.05, 0.95])
ax2.annotate(
    f"el 90 % cae dentro\nde un factor {10**((p95-p05)/2):.0f} arriba o abajo",
    xy=(p95, 0.35), xytext=(p95 + 0.15, 0.95), color=C.red, fontsize=8.6,
    arrowprops=dict(arrowstyle="->", color=C.red, lw=1.0))
ax2.set_xlabel("error del resultado (décadas)")
ax2.set_ylabel("densidad")
ax2.set_title("Seis factores mediocres, un resultado decente")
ax2.legend(loc="upper left")
ax2.set_xlim(-3, 3)

save(fig, "fig_cancelacion")
