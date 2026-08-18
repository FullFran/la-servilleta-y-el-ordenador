"""¿Por qué hay campanas por todas partes, y dónde no las hay?

Sumas de variables con varianza finita (van a la normal), con cola pesada
(van a una Lévy estable) y productos (van a la log-normal).

La figura responde: ¿qué determina la forma límite de una suma?

Ejecutar:  python fig_dominios_atraccion.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(303)
M, K = 200_000, 200

fig, axes = plt.subplots(1, 3, figsize=(11.4, 3.9))

# --- 1. Varianza finita: normal -----------------------------------------
ax = axes[0]
x = r.exponential(1.0, (M, K)).sum(axis=1)
x = (x - x.mean()) / x.std()
ax.hist(x, bins=180, density=True, color=C.blue, alpha=0.6, edgecolor="none",
        range=(-5, 5))
z = np.linspace(-5, 5, 300)
ax.plot(z, stats.norm.pdf(z), color=C.ink, lw=1.8)
ax.set_title("Suma de 200 exponenciales\n$\\Rightarrow$ normal", fontsize=9.5)
ax.set_yticks([])

# --- 2. Cola pesada: Lévy estable ---------------------------------------
ax = axes[1]
alfa = 1.5
y = stats.levy_stable.rvs(alfa, 0, size=(20_000, K), random_state=7).sum(axis=1)
y = y / K**(1 / alfa)
ax.hist(y, bins=250, density=True, color=C.red, alpha=0.6, edgecolor="none",
        range=(-12, 12))
zz = np.linspace(-12, 12, 300)
ax.plot(zz, stats.levy_stable.pdf(zz, alfa, 0), color=C.ink, lw=1.8)
ax.plot(zz, stats.norm.pdf(zz / 1.5) / 1.5, "--", color=C.grey, lw=1.4,
        label="normal (para comparar)")
ax.set_title(r"Suma de 200 Lévy ($\alpha=1{,}5$)"
             "\n$\\Rightarrow$ Lévy, NO normal", fontsize=9.5)
ax.set_yticks([]), ax.legend(fontsize=7.4)

# --- 3. Producto: log-normal --------------------------------------------
ax = axes[2]
p = np.exp(r.normal(0, 0.2, (M, 60)).sum(axis=1))
ax.hist(p, bins=200, density=True, color=C.green, alpha=0.6, edgecolor="none",
        range=(0, 15))
v = np.linspace(0.01, 15, 400)
ax.plot(v, stats.lognorm.pdf(v, s=0.2 * np.sqrt(60)), color=C.ink, lw=1.8)
ax.set_title("Producto de 60 factores\n$\\Rightarrow$ log-normal", fontsize=9.5)
ax.set_yticks([])

fig.suptitle("La forma límite la decide el mecanismo, no el número de términos",
             fontsize=11, y=1.0)
save(fig, "fig_dominios_atraccion")
