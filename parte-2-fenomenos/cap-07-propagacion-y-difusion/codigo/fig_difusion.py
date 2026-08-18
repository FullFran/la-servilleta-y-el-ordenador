"""¿Cómo se propaga una sustancia? Tres descripciones del mismo fenómeno.

Paseos aleatorios individuales, su desplazamiento cuadrático medio, y la
comparación entre la solución de la EDP y el histograma de las partículas.

La figura responde: ¿por qué la difusión va como raíz del tiempo, y qué
significa eso para el transporte?

Ejecutar:  python fig_difusion.py
"""
import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(27)

N_PART, N_PASOS = 20_000, 4000
pasos = r.choice([-1.0, 1.0], size=(N_PART, N_PASOS))
x = np.cumsum(pasos, axis=1)

fig, axes = plt.subplots(1, 3, figsize=(11.6, 4.0))

for k in range(40):
    axes[0].plot(x[k, ::10], lw=0.6, alpha=0.7)
axes[0].set_xlabel("paso / 10"), axes[0].set_ylabel("posición")
axes[0].set_title("40 paseos aleatorios", fontsize=10)

n = np.arange(1, N_PASOS + 1)
msd = (x**2).mean(axis=0)
axes[1].loglog(n, msd, color=C.blue, lw=1.8, label="simulación")
axes[1].loglog(n, n, "--", color=C.ink, lw=1.6, label=r"$\langle x^2\rangle = n$")
axes[1].loglog(n, 0.6 * n**1.5, ":", color=C.red, lw=1.4,
               label=r"$n^{1{,}5}$ (superdifusivo)")
axes[1].set_xlabel("número de pasos $n$")
axes[1].set_ylabel(r"$\langle x^2\rangle$")
axes[1].set_title(r"$\langle x^2\rangle = 2Dt$: la firma de la difusión",
                  fontsize=10)
axes[1].legend(fontsize=8)

D = 0.5
for k, color in zip([100, 500, 2000], [C.blue, C.green, C.red]):
    axes[2].hist(x[:, k - 1], bins=80, density=True, color=color, alpha=0.4,
                 edgecolor="none")
    xx = np.linspace(-160, 160, 400)
    sigma = np.sqrt(2 * D * k)
    axes[2].plot(xx, np.exp(-xx**2 / (4 * D * k)) / np.sqrt(4 * np.pi * D * k),
                 color=color, lw=1.8, label=f"EDP, $t={k}$")
axes[2].set_xlabel("posición"), axes[2].set_ylabel("densidad")
axes[2].set_title("Partículas frente a la solución de la EDP", fontsize=10)
axes[2].legend(fontsize=8)
axes[2].set_xlim(-160, 160)

p = np.polyfit(np.log(n[100:]), np.log(msd[100:]), 1)
print(f"exponente medido del MSD: {p[0]:.4f}  (teoría: 1)")
print(f"tiempo para difundir 1 m con D=1e-9 m^2/s: {1/(2*1e-9)/3.15e7:.0f} años")
print(f"tiempo para difundir 1 mm: {1e-6/(2*1e-9)/60:.1f} min")
save(fig, "fig_difusion")
