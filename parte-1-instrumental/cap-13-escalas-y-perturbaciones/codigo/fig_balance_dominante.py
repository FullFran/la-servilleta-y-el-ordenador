"""¿Qué término domina? La pregunta que resuelve medio problema.

Ecuación cuadrática con un parámetro pequeño: la perturbación regular encuentra
una raíz y pierde la otra. El balance dominante la recupera.

La figura responde: ¿cómo se detecta que una perturbación es singular?

Ejecutar:  python fig_balance_dominante.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

eps = np.logspace(-6, -0.3, 300)

# eps x^2 + x - 1 = 0  -> raíces exactas
raiz_pos = (-1 + np.sqrt(1 + 4 * eps)) / (2 * eps)
raiz_neg = (-1 - np.sqrt(1 + 4 * eps)) / (2 * eps)

# Perturbación regular: x = x0 + eps x1 + ...
regular = 1 - eps + 2 * eps**2

# Reescalado singular: x = X/eps  ->  X^2 + X - eps = 0  ->  X ~ -1
singular = -1 / eps - 1

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))

ax1.semilogx(eps, raiz_pos, color=C.ink, lw=2.4, label="raíz exacta 1")
ax1.semilogx(eps, regular, "--", color=C.blue, lw=1.8,
             label=r"regular: $1-\epsilon+2\epsilon^2$")
ax1.set_xlabel(r"$\epsilon$"), ax1.set_ylabel("raíz")
ax1.set_title(r"$\epsilon x^2+x-1=0$: la raíz que sí se ve")
ax1.legend(fontsize=8.5)
ax1.set_ylim(0.6, 1.05)

ax2.loglog(eps, -raiz_neg, color=C.ink, lw=2.4, label="raíz exacta 2")
ax2.loglog(eps, -singular, "--", color=C.red, lw=1.8,
           label=r"reescalando $x=X/\epsilon$:  $-1/\epsilon-1$")
ax2.set_xlabel(r"$\epsilon$"), ax2.set_ylabel("$-$raíz")
ax2.set_title("La raíz que la perturbación regular pierde")
ax2.legend(fontsize=8.5)
ax2.annotate(r"se escapa a $\infty$ cuando $\epsilon\to0$",
             xy=(1e-5, 1e5), xytext=(3e-4, 3e2), fontsize=8.6, color=C.red,
             arrowprops=dict(arrowstyle="->", color=C.red, lw=1.0))

for e in (1e-2, 1e-4):
    exactas = np.roots([e, 1, -1])
    print(f"eps={e:.0e}: raíces exactas = {np.sort(exactas)}, "
          f"regular = {1-e+2*e**2:.6f}, singular = {-1/e-1:.1f}")
save(fig, "fig_balance_dominante")
