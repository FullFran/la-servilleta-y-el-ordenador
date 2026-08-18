"""¿Cuánto error llevas puesto antes de empezar a calcular?

Tres caras de la aritmética de coma flotante: el espaciado de los números
representables, la cancelación catastrófica y su remedio algebraico.

La figura responde: ¿por qué dos fórmulas matemáticamente idénticas dan
resultados distintos, y cuál hay que usar?

Ejecutar:  python fig_coma_flotante.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()
fig, axes = plt.subplots(1, 3, figsize=(11.4, 3.9))

# --- 1. Espaciado de los flotantes ---------------------------------------
ax = axes[0]
x = np.logspace(-8, 8, 200)
ax.loglog(x, np.spacing(x), color=C.blue, lw=2)
ax.axhline(np.spacing(1.0), color=C.grey, ls="--", lw=1.1)
ax.text(1e-7, np.spacing(1.0) * 1.6, r"$\epsilon_{\mathrm{maq}}=2{,}2\times10^{-16}$",
        fontsize=8.4, color=C.grey)
ax.set_xlabel("valor $x$")
ax.set_ylabel("distancia al siguiente double")
ax.set_title("La resolución depende del tamaño", fontsize=10)
ax.annotate("cerca de $10^8$ el hueco\nya es $10^{-8}$", xy=(1e8, np.spacing(1e8)),
            xytext=(1e-6, 1e-10), fontsize=8.2, color=C.ink,
            arrowprops=dict(arrowstyle="->", color=C.ink, lw=1.0))

# --- 2. Cancelación catastrófica -----------------------------------------
ax = axes[1]
h = np.logspace(-12, 0, 300)
ingenua = (1 - np.cos(h)) / h**2
estable = 2 * (np.sin(h / 2) / h) ** 2
ax.semilogx(h, ingenua, color=C.red, lw=1.6, label=r"$(1-\cos h)/h^2$")
ax.semilogx(h, estable, color=C.blue, lw=2.0,
            label=r"$2\,[\sin(h/2)/h]^2$")
ax.axhline(0.5, color=C.ink, ls="--", lw=1.1)
ax.text(2e-12, 0.53, "valor exacto: 1/2", fontsize=8.4, color=C.ink)
ax.set_ylim(-0.15, 0.75)
ax.set_xlabel("$h$"), ax.set_ylabel("valor calculado")
ax.set_title("Dos fórmulas idénticas en el papel", fontsize=10)
ax.legend(fontsize=8, loc="lower right")

# --- 3. Derivada numérica: el compromiso ---------------------------------
ax = axes[2]
h = np.logspace(-16, 0, 400)
x0 = 1.0
adelante = np.abs((np.sin(x0 + h) - np.sin(x0)) / h - np.cos(x0))
centrada = np.abs((np.sin(x0 + h) - np.sin(x0 - h)) / (2 * h) - np.cos(x0))
ax.loglog(h, np.maximum(adelante, 1e-18), color=C.red, lw=1.6,
          label="hacia delante, $O(h)$")
ax.loglog(h, np.maximum(centrada, 1e-18), color=C.blue, lw=1.8,
          label="centrada, $O(h^2)$")
ax.loglog(h, h / 2, ":", color=C.grey, lw=1.2)
ax.loglog(h, 2.2e-16 / h, ":", color=C.grey, lw=1.2)
ax.text(8e-1, 2e-12, "manda el error\nde truncamiento", fontsize=7.8,
        color=C.grey, ha="right", va="bottom")
ax.text(3e-16, 2e-12, "manda el error\nde redondeo", fontsize=7.8,
        color=C.grey, ha="left", va="bottom")
ax.set_xlabel("paso $h$"), ax.set_ylabel("error absoluto")
ax.set_title("Ni muy grande ni muy pequeño", fontsize=10)
ax.legend(fontsize=8, loc="upper center")
ax.set_ylim(1e-13, 1e1)

print(f"0.1 + 0.2 == 0.3 ?  {0.1 + 0.2 == 0.3}")
print(f"0.1 + 0.2 = {0.1 + 0.2:.20f}")
print(f"h óptimo centrada ≈ {(2.2e-16)**(1/3):.2e}, "
      f"error mínimo ≈ {centrada.min():.2e}")
save(fig, "fig_coma_flotante")
