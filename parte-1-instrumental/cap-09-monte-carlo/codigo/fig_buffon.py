"""La aguja de Buffon: ¿cómo puede tirar agujas darte pi?

Simulación del experimento y convergencia del estimador, con el resultado
«demasiado bueno» de Lazzarini (1901) marcado para comparar.

La figura responde: ¿cuántas agujas hacen falta para dos decimales de pi, y por
qué el resultado de Lazzarini es sospechoso?

Ejecutar:  python fig_buffon.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(1777)

L, D = 1.0, 1.0          # longitud de la aguja y separación entre líneas
N = 2_000_000

# Centro uniforme respecto a la línea más cercana, ángulo uniforme
y = r.uniform(0, D / 2, N)
theta = r.uniform(0, np.pi / 2, N)
cruza = y <= (L / 2) * np.sin(theta)

n = np.arange(1, N + 1)
p_estimada = np.cumsum(cruza) / n
with np.errstate(divide="ignore"):
    pi_estimada = 2 * L / (D * p_estimada)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2),
                               gridspec_kw={"width_ratios": [1, 1.35]})

# --- Panel 1: el experimento ---------------------------------------------
m = 220
for k in range(m):
    xc = r.uniform(0.2, 3.8)
    yc = r.uniform(0.2, 3.8)
    th = r.uniform(0, np.pi)
    dx, dy = (L / 2) * np.cos(th), (L / 2) * np.sin(th)
    corta = int(np.floor(yc - dy)) != int(np.floor(yc + dy))
    ax1.plot([xc - dx, xc + dx], [yc - dy, yc + dy],
             color=C.red if corta else C.grey, lw=1.0,
             alpha=0.9 if corta else 0.5)
for yl in range(5):
    ax1.axhline(yl, color=C.ink, lw=1.2)
ax1.set_xlim(0, 4), ax1.set_ylim(-0.1, 4.1)
ax1.set_aspect("equal"), ax1.axis("off")
ax1.set_title("220 agujas: en rojo las que cruzan", fontsize=10)

# --- Panel 2: convergencia -----------------------------------------------
paso = np.unique(np.logspace(0, np.log10(N), 400).astype(int)) - 1
ax2.semilogx(n[paso], pi_estimada[paso], color=C.blue, lw=1.2,
             label="estimación acumulada")
ax2.axhline(np.pi, color=C.ink, lw=1.4)
ax2.text(2, np.pi + 0.06, r"$\pi$", fontsize=11, color=C.ink)

# Banda teórica +-1 sigma
p = 2 * L / (np.pi * D)
sigma_pi = (2 * L / (D * p**2)) * np.sqrt(p * (1 - p) / n)
ax2.fill_between(n[paso], np.pi - sigma_pi[paso], np.pi + sigma_pi[paso],
                 color=C.blue, alpha=0.18, label=r"$\pm\sigma$ teórica")

ax2.plot(3408, 355 / 113, "*", color=C.red, ms=15, zorder=5)
ax2.annotate("Lazzarini (1901): 3408 agujas,\n"
             r"$\pi = 355/113$, seis decimales",
             xy=(3408, 355 / 113), xytext=(30, 3.55), fontsize=8.4, color=C.red,
             arrowprops=dict(arrowstyle="->", color=C.red, lw=1.0))
ax2.set_ylim(2.6, 3.75)
ax2.set_xlabel("número de agujas $N$")
ax2.set_ylabel(r"estimación de $\pi$")
ax2.set_title(r"Convergencia: el margen baja como $1/\sqrt{N}$")
ax2.legend(fontsize=8, loc="lower right")

print(f"con N={N:,}: pi ≈ {pi_estimada[-1]:.5f}")
print(f"sigma teórica en N=3408: {(2*L/(D*p**2))*np.sqrt(p*(1-p)/3408):.4f}")
print(f"error de Lazzarini: {abs(355/113 - np.pi):.2e}")
save(fig, "fig_buffon")
