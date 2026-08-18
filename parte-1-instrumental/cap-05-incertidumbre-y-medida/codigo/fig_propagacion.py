"""¿Cuándo miente la fórmula de propagación de errores?

Compara la propagación lineal (derivadas parciales) con Monte Carlo, para una
función suave y para otra fuertemente no lineal.

La figura responde: ¿bajo qué condición la fórmula de la primera derivada da
la respuesta correcta?

Ejecutar:  python fig_propagacion.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(8)
N = 400_000

fig, axes = plt.subplots(2, 2, figsize=(10.2, 6.2))

CASOS = [
    # (nombre, f, df, x0, sigma_x, rango)
    (r"$f(x)=x^2$,  $\sigma_x/x_0 = 5\,\%$",
     lambda x: x**2, lambda x: 2 * x, 10.0, 0.5, (60, 145)),
    (r"$f(x)=1/x$,  $\sigma_x/x_0 = 40\,\%$",
     lambda x: 1 / x, lambda x: -1 / x**2, 1.0, 0.4, (0, 6)),
]

for fila, (nombre, f, df, x0, sx, rango) in enumerate(CASOS):
    x = r.normal(x0, sx, N)
    y = f(x)
    sigma_lineal = abs(df(x0)) * sx

    # Panel izquierdo: la función y la anchura de entrada
    ax = axes[fila, 0]
    xx = np.linspace(x0 - 3.2 * sx, x0 + 3.2 * sx, 300)
    xx = xx[xx > 1e-3] if x0 == 1.0 else xx
    ax.plot(xx, f(xx), color=C.blue, lw=2, label="$f(x)$")
    ax.plot(xx, f(x0) + df(x0) * (xx - x0), "--", color=C.ochre, lw=1.6,
            label="aproximación lineal")
    ax.axvspan(x0 - sx, x0 + sx, color=C.red, alpha=0.15)
    ax.set_xlabel("$x$"), ax.set_ylabel("$f(x)$")
    ax.set_title(nombre, fontsize=10)
    ax.legend(fontsize=8)

    # Panel derecho: distribución de salida
    ax = axes[fila, 1]
    ax.hist(y, bins=200, range=rango, density=True, color=C.blue, alpha=0.55,
            edgecolor="none", label="Monte Carlo")
    zz = np.linspace(*rango, 400)
    gauss = np.exp(-0.5 * ((zz - f(x0)) / sigma_lineal) ** 2) / (
        sigma_lineal * np.sqrt(2 * np.pi))
    ax.plot(zz, gauss, color=C.ochre, lw=2, label="propagación lineal")
    ax.axvline(f(x0), color=C.ink, lw=1.4)
    ax.axvline(np.median(y), color=C.red, lw=1.4, ls="--")
    ax.set_xlabel("$f(x)$"), ax.set_ylabel("densidad")
    ax.set_yticks([])
    ax.legend(fontsize=8)
    sesgo = np.mean(y) - f(x0)
    ax.set_title(f"media MC − $f(x_0)$ = {sesgo:+.3g};  "
                 f"$\\sigma_{{MC}}/\\sigma_{{lin}}$ = {y.std()/sigma_lineal:.2f}",
                 fontsize=9.5)
    print(f"{nombre}: sesgo={sesgo:+.4g}  sigma_MC/sigma_lin="
          f"{y.std()/sigma_lineal:.3f}")

save(fig, "fig_propagacion")
