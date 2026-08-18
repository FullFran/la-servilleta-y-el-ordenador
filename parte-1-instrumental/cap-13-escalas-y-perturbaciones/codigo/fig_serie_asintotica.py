"""Una serie que diverge y aun así es la mejor herramienta que tienes.

Serie asintótica de la integral exponencial: el error baja, alcanza un mínimo
y después crece sin límite.

La figura responde: ¿cuántos términos hay que sumar de una serie divergente?

Ejecutar:  python fig_serie_asintotica.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.special import exp1

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

# f(x) = e^x E1(x) ~ sum_{n>=0} (-1)^n n! / x^{n+1}
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))

for x0, color in zip([3.0, 5.0, 10.0], [C.red, C.ochre, C.blue]):
    exacto = np.exp(x0) * exp1(x0)
    parciales, errores = [], []
    s = 0.0
    for n in range(0, 26):
        s += (-1)**n * math.factorial(n) / x0**(n + 1)
        parciales.append(s)
        errores.append(abs(s - exacto))
    ax1.semilogy(range(len(errores)), errores, "o-", color=color, ms=4, lw=1.3,
                 label=f"$x$ = {x0:.0f}")
    n_opt = int(np.argmin(errores))
    ax1.plot(n_opt, errores[n_opt], "*", color=color, ms=15, zorder=5)
    print(f"x={x0}: mejor con {n_opt} términos, error {errores[n_opt]:.2e}; "
          f"con 25 términos, error {errores[-1]:.2e}")

ax1.set_xlabel("términos sumados $N$"), ax1.set_ylabel("error absoluto")
ax1.set_title("La serie diverge: el error tiene un mínimo")
ax1.legend(fontsize=8.5)

# --- Precisión óptima frente a x -----------------------------------------
xs = np.linspace(2, 25, 60)
mejores, n_opts = [], []
for x0 in xs:
    exacto = np.exp(x0) * exp1(x0)
    s, err = 0.0, []
    for n in range(0, 60):
        s += (-1)**n * math.factorial(n) / x0**(n + 1)
        err.append(abs(s - exacto))
    mejores.append(min(err)), n_opts.append(int(np.argmin(err)))

ax2.semilogy(xs, mejores, color=C.blue, lw=2.0, label="mejor error alcanzable")
ax2.semilogy(xs, np.exp(-xs) * np.sqrt(2 * np.pi / xs), "--", color=C.ink,
             lw=1.5, label=r"$\sim e^{-x}$")
ax2b = ax2.twinx()
ax2b.plot(xs, n_opts, color=C.red, lw=1.5)
ax2b.set_ylabel("términos óptimos", color=C.red)
ax2b.tick_params(axis="y", colors=C.red)
ax2b.grid(False)
ax2.set_xlabel("$x$"), ax2.set_ylabel("error mínimo")
ax2.set_title(r"El error óptimo decae como $e^{-x}$")
ax2.legend(fontsize=8.5, loc="upper right")

save(fig, "fig_serie_asintotica")
