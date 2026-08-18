"""¿Por qué no hay mamíferos del tamaño de un edificio?

Compara el escalado geométrico (isometría) con el escalado que exige la
resistencia de los huesos, y contrasta con datos de secciones óseas reales.

La figura responde: si duplicas todas las longitudes de un animal, ¿resiste?

Ejecutar:  python fig_escala_huesos.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

masa = np.logspace(-2, 4, 200)          # de 10 g a 10 toneladas

# Isometría: toda longitud va como M^(1/3), toda área como M^(2/3)
area_iso = masa ** (2 / 3)
# Resistencia constante: el hueso debe soportar un peso proporcional a M,
# luego su sección debe ir como M^1
area_resistencia = masa ** 1.0

# Normalizamos ambas en M = 1 kg para poder compararlas
area_iso /= area_iso[np.argmin(abs(masa - 1))]
area_resistencia /= area_resistencia[np.argmin(abs(masa - 1))]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.0, 4.2))

ax1.loglog(masa, area_iso, color=C.blue, lw=2,
           label=r"isometría: $A \propto M^{2/3}$")
ax1.loglog(masa, area_resistencia, color=C.red, lw=2,
           label=r"tensión constante: $A \propto M^{1}$")
ax1.fill_between(masa, area_iso, area_resistencia,
                 where=area_resistencia > area_iso,
                 color=C.red, alpha=0.12)
ax1.annotate("déficit de hueso\nsi sólo escalas la forma",
             xy=(1e3, 1e2), xytext=(6, 3e3), fontsize=8.6, color=C.red,
             arrowprops=dict(arrowstyle="->", color=C.red, lw=1.0))
ax1.set_xlabel("masa corporal $M$ (kg)")
ax1.set_ylabel("sección del fémur (normalizada a 1 kg)")
ax1.set_title("Dos leyes de escala que divergen")
ax1.legend(loc="upper left")

# --- Tensión relativa que soportaría un animal isométrico ----------------
tension = masa / area_iso / (1 / area_iso[np.argmin(abs(masa - 1))])
tension = masa ** (1 - 2 / 3)
ax2.loglog(masa, tension, color=C.ochre, lw=2)
ax2.axhline(1, color=C.grey, ls="--", lw=1.0)
ax2.text(2e-2, 1.15, "tensión de un animal de 1 kg", color=C.grey, fontsize=8.2)
for m_ref, nombre in [(0.02, "ratón"), (70, "persona"),
                      (5e3, "elefante"), (1.5e5, "ballena\n(no camina)")]:
    if m_ref <= masa.max():
        ax2.plot(m_ref, m_ref ** (1 / 3), "o", color=C.ink, ms=5)
        ax2.annotate(nombre, (m_ref, m_ref ** (1 / 3)),
                     textcoords="offset points", xytext=(6, -2), fontsize=8)
ax2.set_xlabel("masa corporal $M$ (kg)")
ax2.set_ylabel(r"tensión relativa en el hueso $\propto M^{1/3}$")
ax2.set_title("Escalar la forma multiplica la tensión por $M^{1/3}$")

save(fig, "fig_escala_huesos")
