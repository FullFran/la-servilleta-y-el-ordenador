"""¿Sale el mismo tiempo característico partiendo de temperaturas distintas?

Tres tazas idénticas que empiezan a 88, 65 y 45 grados, enfriándose en la misma
habitación. Se ajusta la ley de Newton a cada una por separado. La pregunta es
si el tau ajustado depende de la condición inicial: no debería, porque un
sistema lineal de primer orden olvida de dónde viene.

A la derecha, la misma medida en escala logarítmica frente a la temperatura
ambiente ajustada: tres rectas paralelas, y la pendiente comun es -1/tau.
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, anota, rng, save, use_style

use_style((9.4, 4.0))

T_AMB = 21.0        # grados, la habitacion
TAU = 24.0          # minutos, propiedad de la taza y del aire
SIGMA = 0.4         # grados, ruido del termometro
INICIALES = [88.0, 65.0, 45.0]

t = np.arange(0.0, 61.0, 2.0)
g = rng(11)


def modelo(t, T_amb, T0, tau):
    return T_amb + (T0 - T_amb) * np.exp(-t / tau)


fig, (ax1, ax2) = plt.subplots(1, 2)
colores = [C.red, C.ochre, C.blue]
ajustes = []

for T0, color in zip(INICIALES, colores):
    T = modelo(t, T_AMB, T0, TAU) + g.normal(0.0, SIGMA, t.size)
    popt, pcov = curve_fit(modelo, t, T, p0=[20.0, T0, 20.0])
    err = np.sqrt(np.diag(pcov))
    ajustes.append((T0, popt, err))
    print(f"T0={T0:5.1f}  ->  T_amb={popt[0]:.2f}  tau={popt[2]:.2f} min"
          f"  (sigma_tau={err[2]:.2f})")

    fino = np.linspace(0.0, 60.0, 400)
    ax1.plot(t, T, "o", color=color, ms=4, alpha=0.75)
    ax1.plot(fino, modelo(fino, *popt), color=color, lw=1.6,
             label=rf"$T_0={T0:.0f}$ °C,  $\tau={popt[2]:.1f}$ min")

    # Escala logaritmica: log(T - T_amb) frente a t es una recta de pendiente -1/tau.
    exceso = T - popt[0]
    valido = exceso > 0.6            # por debajo del ruido el logaritmo miente
    ax2.semilogy(t[valido], exceso[valido], "o", color=color, ms=4, alpha=0.75)
    ax2.semilogy(fino, (popt[1] - popt[0]) * np.exp(-fino / popt[2]),
                 color=color, lw=1.6)

ax1.axhline(T_AMB, color=C.grey, ls="--", lw=1.0, zorder=0)
ax1.text(1.0, T_AMB + 1.2, "temperatura ambiente", ha="left", fontsize=8, color=C.grey)
ax1.set_xlabel("tiempo (min)")
ax1.set_ylabel("temperatura (°C)")
ax1.set_title("Tres tazas, tres puntos de partida")
ax1.legend(loc="upper right")

ax2.set_xlabel("tiempo (min)")
ax2.set_ylabel(r"$T-T_{\mathrm{amb}}$ (°C)")
ax2.set_title("En logaritmo: tres rectas paralelas")
anota(ax2, "misma pendiente = mismo $\\tau$", xy=(30, 12.0), xytext=(4, 3.2),
      color=C.ink)

taus = np.array([p[2] for _, p, _ in ajustes])
print(f"\ntau medio = {taus.mean():.2f} min, dispersion = {taus.std(ddof=1):.2f} min"
      f"  (valor verdadero {TAU:.1f})")

save(fig, "fig_taza_cafe")
