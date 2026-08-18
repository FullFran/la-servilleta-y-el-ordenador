"""¿Se puede sacar la energía de una bomba de una fotografía y un cronómetro?

Ajusta la ley de onda de choque R = C (E t^2 / rho)^(1/5) a los radios de la
bola de fuego de Trinity publicados por G. I. Taylor (1950), obtenidos de las
fotografías de alta velocidad de J. E. Mack.

La figura responde: ¿es realmente una recta de pendiente 2/5 en log-log, y qué
energía sale de ella?

Ejecutar:  python fig_taylor_trinity.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

# Datos transcritos de la tabla publicada en Taylor (1950), parte II.
# t en milisegundos, R en metros. Son los radios medidos sobre las fotografías.
t_ms = np.array([0.10, 0.24, 0.38, 0.52, 0.66, 0.94, 1.25, 1.50, 1.93,
                 3.53, 4.61, 15.0, 25.0, 34.0, 53.0, 62.0])
R_m = np.array([11.1, 19.9, 25.4, 28.8, 31.9, 36.3, 41.0, 44.4, 46.9,
                59.0, 65.6, 106.5, 130.0, 145.0, 175.0, 185.0])
t = t_ms * 1e-3

RHO = 1.25      # densidad del aire ambiente, kg/m^3
C_TAYLOR = 1.03  # constante adimensional para gamma = 1.4 (Taylor, 1950)

# Ajuste de log R = a + m log t.  La teoría predice m = 2/5.
m, a = np.polyfit(np.log10(t), np.log10(R_m), 1)
# Energía a partir de cada punto, fijando la pendiente teórica
E_por_punto = RHO * R_m**5 / (C_TAYLOR**5 * t**2)
E = np.median(E_por_punto)

print(f"pendiente ajustada = {m:.3f}   (teoría: {2/5:.3f})")
print(f"E = {E:.2e} J = {E / 4.184e12:.1f} kt")
print(f"dispersión punto a punto: {E_por_punto.min()/1e12:.0f}–"
      f"{E_por_punto.max()/1e12:.0f} TJ")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.0, 4.2))

# --- Panel 1: la ley de potencias ----------------------------------------
tt = np.logspace(-4.2, -1.1, 100)
ax1.loglog(t, R_m, "o", color=C.red, ms=6, label="Trinity (Taylor 1950)")
ax1.loglog(tt, 10**a * tt**m, "-", color=C.blue, lw=1.8,
           label=f"ajuste: $R \\propto t^{{{m:.2f}}}$")
# La teoría fija la pendiente en 2/5; sólo se ajusta la ordenada.
a_teoria = np.mean(np.log10(R_m) - 0.4 * np.log10(t))
ax1.loglog(tt, 10**a_teoria * tt**0.4, "--", color=C.green, lw=1.4,
           label="teoría: $R \\propto t^{2/5}$")
ax1.set_xlabel("tiempo desde la detonación (s)")
ax1.set_ylabel("radio del frente (m)")
ax1.set_title("Tres décadas de tiempo, una sola recta")
ax1.legend(loc="lower right")

# --- Panel 2: la energía deducida de cada punto ---------------------------
ax2.semilogx(t, E_por_punto / 4.184e12, "o", color=C.red, ms=6)
ax2.axhline(E / 4.184e12, color=C.blue, lw=1.8,
            label=f"mediana = {E / 4.184e12:.0f} kt")
ax2.axhspan(20, 22, color=C.green, alpha=0.18)
ax2.text(2e-4, 21, "valor aceptado hoy: ~21 kt", color=C.green, fontsize=8.6,
         va="center")
ax2.set_xlabel("tiempo desde la detonación (s)")
ax2.set_ylabel("energía deducida (kt de TNT)")
ax2.set_title("Cada foto da una energía. ¿Coinciden?")
ax2.set_ylim(0, 30)
ax2.legend(loc="lower right")

save(fig, "fig_taylor_trinity")
