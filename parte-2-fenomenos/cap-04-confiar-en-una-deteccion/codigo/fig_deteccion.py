"""¿Cuánto podemos fiarnos de una detección?

Distribución del número de cuentas bajo hipótesis nula y con señal, el
p-valor exacto de Poisson, y el efecto de la incertidumbre del fondo.

La figura responde: ¿por qué 3 sigmas no es lo mismo que 99,9 % de confianza en
que hay señal?

Ejecutar:  python fig_deteccion.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

B, S = 8.0, 4.0
k = np.arange(0, 30)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))

ax1.bar(k - 0.2, stats.poisson.pmf(k, B), width=0.4, color=C.blue, alpha=0.8,
        label=f"sólo fondo ($b={B:.0f}$)")
ax1.bar(k + 0.2, stats.poisson.pmf(k, B + S), width=0.4, color=C.red,
        alpha=0.8, label=f"fondo + señal ($s={S:.0f}$)")
n_obs = 12
ax1.axvline(n_obs, color=C.ink, lw=2.0)
p_val = 1 - stats.poisson.cdf(n_obs - 1, B)
ax1.text(n_obs + 0.4, 0.12,
         f"observado: {n_obs}\n$p$ = {p_val:.3f}\n"
         f"= {stats.norm.isf(p_val):.2f}$\\sigma$",
         fontsize=9, color=C.ink)
ax1.set_xlabel("cuentas observadas"), ax1.set_ylabel("probabilidad")
ax1.set_title("Las dos hipótesis se solapan muchísimo")
ax1.legend(fontsize=8.5)

# --- Cuentas necesarias, con y sin incertidumbre en el fondo -------------
t = np.logspace(-1, 3, 300)
rb, rs = 8.0, 4.0                       # por unidad de tiempo
sig_ideal = rs * t / np.sqrt(rb * t)
for delta, color, etiqueta in [(0.0, C.blue, "fondo conocido exactamente"),
                               (0.02, C.ochre, "fondo conocido al 2 %"),
                               (0.05, C.red, "fondo conocido al 5 %")]:
    sig = rs * t / np.sqrt(rb * t + (delta * rb * t) ** 2)
    ax2.loglog(t, sig, color=color, lw=2.0, label=etiqueta)
ax2.axhline(5, color=C.ink, ls="--", lw=1.2)
ax2.text(0.12, 5.6, "5$\\sigma$", fontsize=8.6, color=C.ink)
ax2.set_xlabel("tiempo de medida (unidades arbitrarias)")
ax2.set_ylabel(r"significancia")
ax2.set_title("La incertidumbre del fondo pone un techo")
ax2.legend(fontsize=8, loc="lower right")
ax2.set_ylim(0.1, 100)

print(f"n=12 con b=8: p = {p_val:.4f} = {stats.norm.isf(p_val):.2f} sigmas")
for delta in (0.0, 0.02, 0.05):
    sig_max = rs / (delta * np.sqrt(rb)) if delta > 0 else np.inf
    print(f"fondo al {100*delta:.0f} %: significancia máxima alcanzable = "
          f"{'ilimitada' if delta==0 else f'{rs/(delta*rb):.1f} sigma'}")
save(fig, "fig_deteccion")
