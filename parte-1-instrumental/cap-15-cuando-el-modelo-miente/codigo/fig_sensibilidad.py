"""Sensibilidad local frente a global: la derivada parcial que engaña.

Un modelo no lineal donde la derivada parcial en el punto nominal dice que un
parámetro no importa, y el análisis global dice lo contrario.

La figura responde: ¿basta con mover un parámetro cada vez?

Ejecutar:  python fig_sensibilidad.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(155)


def modelo(a, b):
    """Salida con interacción fuerte entre a y b."""
    return np.sin(a) * np.sin(b) + 0.3 * a


A0, B0 = np.pi / 2, np.pi / 2       # punto nominal: derivada de b nula

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))

# --- Sensibilidad local (un parámetro cada vez) --------------------------
d = np.linspace(-1.5, 1.5, 300)
ax1.plot(d, modelo(A0 + d, B0), color=C.blue, lw=2.0, label="variando $a$")
ax1.plot(d, modelo(A0, B0 + d), color=C.red, lw=2.0, label="variando $b$")
ax1.plot(0, modelo(A0, B0), "o", color=C.ink, ms=7)
ax1.set_xlabel("desviación desde el punto nominal")
ax1.set_ylabel("salida del modelo")
ax1.set_title("Local: «$b$ no influye, su derivada es cero»")
ax1.legend(fontsize=8.5)
ax1.annotate("plana en el nominal", xy=(0, modelo(A0, B0)),
             xytext=(-1.35, 1.05), fontsize=8.4, color=C.red,
             arrowprops=dict(arrowstyle="->", color=C.red, lw=1.0))

# --- Sensibilidad global (muestreo del espacio completo) ------------------
N = 30_000
a = r.uniform(0, np.pi, N)
b = r.uniform(0, np.pi, N)
y = modelo(a, b)

# Índices de primer orden por binning (estimador de la varianza condicional)
def sobol_primer_orden(x, y, nbins=25):
    bins = np.linspace(x.min(), x.max(), nbins + 1)
    idx = np.digitize(x, bins) - 1
    medias = np.array([y[idx == k].mean() for k in range(nbins)
                       if np.any(idx == k)])
    return np.var(medias) / np.var(y)


S_a = sobol_primer_orden(a, y)
S_b = sobol_primer_orden(b, y)
ax2.bar(["$a$", "$b$"], [S_a, S_b], color=[C.blue, C.red], width=0.5)
ax2.set_ylabel("índice de Sobol de primer orden")
ax2.set_title("Global: los dos importan, y hay interacción")
ax2.text(0.5, max(S_a, S_b) * 0.75,
         f"$S_a$ = {S_a:.2f}\n$S_b$ = {S_b:.2f}\n"
         f"interacción = {1 - S_a - S_b:.2f}",
         fontsize=9.5, ha="center", color=C.ink,
         bbox=dict(boxstyle="round,pad=0.4", fc=C.light, ec=C.grey, lw=0.6))
ax2.set_ylim(0, max(S_a, S_b) * 1.35)

print(f"derivada parcial local en b: {(modelo(A0, B0+1e-6)-modelo(A0, B0))/1e-6:.2e}")
print(f"S_a = {S_a:.3f}, S_b = {S_b:.3f}, interacción = {1-S_a-S_b:.3f}")
save(fig, "fig_sensibilidad")
