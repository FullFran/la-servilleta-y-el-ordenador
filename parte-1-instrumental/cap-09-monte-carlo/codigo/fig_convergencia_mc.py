"""1/sqrt(N): ¿es una ley de la naturaleza o se puede batir?

Compara Monte Carlo puro, Monte Carlo cuasi-aleatorio (Sobol) e integración por
rejilla, en dimensión creciente.

La figura responde: ¿cuándo gana Monte Carlo a una rejilla, y por qué?

Ejecutar:  python fig_convergencia_mc.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import qmc

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(9)


def integrando(x):
    """Función suave en [0,1]^d con integral exacta conocida."""
    return np.prod(np.cos(x * np.pi / 2) * (np.pi / 2), axis=-1)   # integral = 1


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))

# --- Panel 1: MC vs quasi-MC en d = 4 ------------------------------------
d = 4
Ns = np.unique(np.logspace(1.5, 5.5, 25).astype(int))
err_mc, err_qmc = [], []
for N in Ns:
    x = r.random((N, d))
    err_mc.append(abs(integrando(x).mean() - 1.0))
    s = qmc.Sobol(d=d, scramble=True, seed=3).random(N)
    err_qmc.append(abs(integrando(s).mean() - 1.0))

ax1.loglog(Ns, err_mc, "o-", color=C.blue, ms=4, lw=1.3,
           label="Monte Carlo puro")
ax1.loglog(Ns, err_qmc, "s-", color=C.green, ms=4, lw=1.3,
           label="cuasi-Monte Carlo (Sobol)")
ax1.loglog(Ns, 0.35 / np.sqrt(Ns), ":", color=C.ink, lw=1.4,
           label=r"$N^{-1/2}$")
ax1.loglog(Ns, 3.0 / Ns, ":", color=C.grey, lw=1.4, label=r"$N^{-1}$")
ax1.set_xlabel("número de muestras $N$")
ax1.set_ylabel("error absoluto")
ax1.set_title("Dimensión $d=" + str(d) + r"$: hay algo mejor que $1/\sqrt{N}$")
ax1.legend(fontsize=8, loc="lower left")

# --- Panel 2: la maldición (y la bendición) de la dimensión --------------
dims = np.arange(1, 13)
N_OBJETIVO = 10_000
err_mc_d, err_rejilla_d = [], []
for dd in dims:
    x = r.random((N_OBJETIVO, dd))
    err_mc_d.append(abs(integrando(x).mean() - 1.0))
    # rejilla con el mismo presupuesto de puntos: n por eje
    n_eje = max(int(round(N_OBJETIVO ** (1 / dd))), 2)
    ejes = (np.arange(n_eje) + 0.5) / n_eje
    malla = np.stack(np.meshgrid(*([ejes] * dd), indexing="ij"), axis=-1)
    err_rejilla_d.append(abs(integrando(malla.reshape(-1, dd)).mean() - 1.0))

ax2.semilogy(dims, err_mc_d, "o-", color=C.blue, ms=5, lw=1.6,
             label="Monte Carlo ($10^4$ puntos)")
ax2.semilogy(dims, err_rejilla_d, "s-", color=C.red, ms=5, lw=1.6,
             label="rejilla ($10^4$ puntos)")
ax2.set_xlabel("dimensión $d$")
ax2.set_ylabel("error absoluto")
ax2.set_title("El mismo presupuesto, dos estrategias")
ax2.set_ylim(1e-10, 3e1)
ax2.legend(fontsize=8, loc="lower right")
ax2.annotate("a partir de aquí\nla rejilla es inservible",
             xy=(6, err_rejilla_d[5]), xytext=(1.4, 4e0), fontsize=8.4,
             color=C.red, arrowprops=dict(arrowstyle="->", color=C.red, lw=1.0))
ax2.text(2.4, 8e-9, "el error de Monte Carlo\nNO depende de $d$",
         fontsize=8.6, color=C.blue)

print("d, err_MC, err_rejilla")
for dd, a, b in zip(dims, err_mc_d, err_rejilla_d):
    print(f"{dd:2d}  {a:.2e}  {b:.2e}")
save(fig, "fig_convergencia_mc")
