"""¿Qué promete exactamente la ley de los grandes números, y qué no?

Izquierda: medias muestrales convergiendo (o no). Derecha: el teorema central
del límite actuando sobre tres distribuciones de partida muy distintas.

La figura responde: ¿por qué la campana aparece en todas partes, y a qué
velocidad?

Ejecutar:  python fig_lgn_tcl.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(11)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.2, 4.2))

# --- Panel 1: convergencia de la media muestral --------------------------
N = 20_000
n = np.arange(1, N + 1)
for i, color in enumerate([C.blue, C.green, C.ochre, C.purple, C.teal]):
    x = r.uniform(0, 1, N)
    ax1.plot(n, np.cumsum(x) / n, color=color, lw=0.9, alpha=0.8)
ax1.axhline(0.5, color=C.ink, lw=1.4)
ax1.fill_between(n, 0.5 - 2 * (1 / np.sqrt(12)) / np.sqrt(n),
                 0.5 + 2 * (1 / np.sqrt(12)) / np.sqrt(n),
                 color=C.red, alpha=0.15, label=r"$\pm 2\sigma/\sqrt{n}$")
ax1.set_xscale("log")
ax1.set_xlim(1, N), ax1.set_ylim(0.2, 0.8)
ax1.set_xlabel("número de muestras $n$")
ax1.set_ylabel("media acumulada")
ax1.set_title("La media converge, pero el margen sólo baja como $1/\\sqrt{n}$")
ax1.legend(loc="upper right")

# --- Panel 2: TCL desde tres puntos de partida ---------------------------
M = 100_000
partidas = {
    "uniforme": lambda k: r.uniform(-1, 1, (M, k)),
    "exponencial": lambda k: r.exponential(1.0, (M, k)) - 1,
    "Bernoulli p=0,05": lambda k: r.binomial(1, 0.05, (M, k)) - 0.05,
}
K = 12
for (nombre, gen), color in zip(partidas.items(), [C.blue, C.green, C.ochre]):
    s = gen(K).sum(axis=1)
    s = (s - s.mean()) / s.std()
    ax2.hist(s, bins=160, density=True, histtype="step", lw=1.6, color=color,
             label=f"suma de {K} · {nombre}", range=(-4.5, 4.5))
z = np.linspace(-4.5, 4.5, 300)
ax2.plot(z, stats.norm.pdf(z), color=C.ink, lw=2.0, ls="--", label="normal")
ax2.set_xlabel("suma tipificada")
ax2.set_ylabel("densidad")
ax2.set_title("Doce sumandos bastan… salvo si la partida es muy asimétrica")
ax2.legend(fontsize=8, loc="upper left")

save(fig, "fig_lgn_tcl")
