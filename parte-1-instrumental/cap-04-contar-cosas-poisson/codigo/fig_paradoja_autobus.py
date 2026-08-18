"""Si los autobuses pasan cada 10 minutos, ¿cuánto esperas de media?

Simula llegadas de Poisson y mide (a) el intervalo medio entre autobuses y
(b) el intervalo en el que cae un pasajero que llega en un instante al azar.

La figura responde: ¿por qué esperas más de lo que dice el horario, incluso si
el horario es honesto?

Ejecutar:  python fig_paradoja_autobus.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(17)

TASA = 1 / 10.0            # un autobús cada 10 minutos de media
T_TOTAL = 200_000.0

# Instantes de llegada de un proceso de Poisson
huecos = r.exponential(1 / TASA, int(T_TOTAL * TASA * 1.2))
llegadas = np.cumsum(huecos)
llegadas = llegadas[llegadas < T_TOTAL]
huecos = np.diff(llegadas)

# Un millón de pasajeros llegan en instantes uniformes
pasajeros = np.sort(r.uniform(0, llegadas[-1], 1_000_000))
idx = np.searchsorted(llegadas, pasajeros) - 1
valido = (idx >= 0) & (idx < len(huecos))
hueco_visto = huecos[idx[valido]]
espera = llegadas[idx[valido] + 1] - pasajeros[valido]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.2, 4.0))

ax1.hist(huecos, bins=100, density=True, color=C.blue, alpha=0.55,
         edgecolor="none", label=f"huecos reales (media {huecos.mean():.1f} min)")
ax1.hist(hueco_visto, bins=100, density=True, histtype="step", lw=1.8,
         color=C.red,
         label=f"hueco que ve el pasajero (media {hueco_visto.mean():.1f} min)")
ax1.set_xlim(0, 60)
ax1.set_xlabel("duración del intervalo entre autobuses (min)")
ax1.set_ylabel("densidad")
ax1.set_title("El pasajero no ve un hueco cualquiera:\nve uno grande, porque "
              "son más anchos", fontsize=10)
ax1.legend(fontsize=8)

ax2.hist(espera, bins=100, density=True, color=C.ochre, alpha=0.6,
         edgecolor="none")
ax2.axvline(espera.mean(), color=C.ink, lw=1.8)
ax2.text(espera.mean() * 1.05, ax2.get_ylim()[1] * 0.8,
         f"espera media = {espera.mean():.1f} min\n"
         f"(el horario dice 10; la mitad serían 5)",
         fontsize=8.8, color=C.ink)
ax2.set_xlim(0, 50)
ax2.set_xlabel("tiempo de espera del pasajero (min)")
ax2.set_ylabel("densidad")
ax2.set_title("Y por eso espera 10 minutos, no 5", fontsize=10)

print(f"hueco medio real:     {huecos.mean():.2f} min")
print(f"hueco medio visto:    {hueco_visto.mean():.2f} min")
print(f"espera media:         {espera.mean():.2f} min")

save(fig, "fig_paradoja_autobus")
