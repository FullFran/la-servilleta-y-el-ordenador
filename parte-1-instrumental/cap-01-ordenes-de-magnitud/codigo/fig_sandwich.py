"""¿Sirve de algo acotar cuando no sé estimar?

Compara dos estrategias para el mismo problema (número de coches circulando
simultáneamente en España a las 8 de la mañana): estimar de frente, o acotar
por arriba y por abajo y tomar la media geométrica.

La figura responde: ¿cuánto se estrecha la respuesta al usar cotas absurdas
pero seguras?

Ejecutar:  python fig_sandwich.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

CASOS = [
    # etiqueta, cota inferior, cota superior, razonamiento
    ("Cota trivial\n(no puede ser)", 1e3, 3.5e7,
     "más de mil, y menos que\nla población de España"),
    ("Cota razonada\n(parque móvil)", 1e5, 2.5e7,
     "no más que los coches\nmatriculados (≈25 M)"),
    ("Cota afinada\n(hora punta)", 1.5e6, 8e6,
     "entre el 5 % y el 30 %\ndel parque, a las 8:00"),
]
VALOR_REAL = 3.5e6      # estimación independiente por horas-coche anuales

fig, ax = plt.subplots(figsize=(8.2, 4.0))

for i, (etiqueta, lo, hi, razon) in enumerate(CASOS):
    y = len(CASOS) - i
    media_geo = np.sqrt(lo * hi)
    factor = np.sqrt(hi / lo)
    ax.plot([lo, hi], [y, y], color=C.blue, lw=7, alpha=0.28,
            solid_capstyle="butt")
    ax.plot([lo, lo], [y - 0.16, y + 0.16], color=C.blue, lw=2)
    ax.plot([hi, hi], [y - 0.16, y + 0.16], color=C.blue, lw=2)
    ax.plot(media_geo, y, "D", color=C.ink, ms=7, zorder=5)
    ax.text(media_geo, y + 0.26, f"media geométrica · factor {factor:.0f}",
            ha="center", fontsize=8.2, color=C.ink)
    ax.text(1.2e2, y, etiqueta, ha="left", va="center", fontsize=8.8,
            color=C.ink)
    ax.text(6e7, y, razon, ha="left", va="center", fontsize=8.0, color=C.grey)

ax.axvline(VALOR_REAL, color=C.red, lw=1.8)
ax.text(VALOR_REAL * 1.15, 0.42, "estimación independiente\n≈ 3–4 millones", color=C.red,
        fontsize=8.6, va="bottom")

ax.set_xscale("log")
ax.set_xlim(1e2, 6e8)
ax.set_ylim(0.3, len(CASOS) + 0.85)
ax.set_yticks([])
ax.set_xlabel("coches circulando simultáneamente en España a las 8:00")
ax.set_title("Acotar y tomar la media geométrica: cada refinamiento divide\n"
             "el factor de error, no la respuesta")
ax.grid(axis="y", alpha=0)

save(fig, "fig_sandwich")
