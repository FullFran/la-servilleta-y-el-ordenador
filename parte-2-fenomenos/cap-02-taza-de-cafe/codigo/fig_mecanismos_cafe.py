"""¿Qué mecanismo domina el enfriamiento de una taza, y cuándo?

Potencia perdida por convección, radiación y evaporación en función de la
temperatura, con la frontera de dominancia.

La figura responde: ¿bastaba con la ley de Newton?

Ejecutar:  python fig_mecanismos_cafe.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

T_AMB = 294.15                # 21 °C
A_SUP, A_LAT = 0.0064, 0.020  # m^2 (superficie libre y pared)
H_CONV, EPS, SIGMA = 6.0, 0.90, 5.67e-8   # h efectivo: la pared
                                          # de la taza añade su propia
                                          # resistencia térmica
L_VAP = 2.4e6                 # J/kg

T = np.linspace(295, 368, 400)


def p_sat(T):
    """Presión de vapor de saturación (Pa), aproximación de Tetens."""
    Tc = T - 273.15
    return 610.78 * np.exp(17.27 * Tc / (Tc + 237.3))


conv = H_CONV * (A_SUP + A_LAT) * (T - T_AMB)
rad = EPS * SIGMA * (A_SUP + A_LAT) * (T**4 - T_AMB**4)
# Evaporación: flujo difusivo proporcional a la diferencia de humedad absoluta
K_M = 0.0013                  # m/s, coeficiente de transferencia de masa
R_V = 461.5
evap = (L_VAP * K_M * A_SUP *
        (p_sat(T) / (R_V * T) - 0.5 * p_sat(T_AMB) / (R_V * T_AMB)))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))

Tc = T - 273.15
ax1.plot(Tc, conv, color=C.blue, lw=2.0, label="convección")
ax1.plot(Tc, rad, color=C.green, lw=2.0, label="radiación")
ax1.plot(Tc, evap, color=C.red, lw=2.0, label="evaporación")
ax1.plot(Tc, conv + rad + evap, color=C.ink, lw=1.4, ls="--", label="total")
ax1.set_xlabel("temperatura del café (°C)")
ax1.set_ylabel("potencia perdida (W)")
ax1.set_title("Tres mecanismos, tres dependencias distintas")
ax1.legend(fontsize=8.5)

fracciones = np.vstack([conv, rad, evap]) / (conv + rad + evap)
ax2.stackplot(Tc, fracciones, colors=[C.blue, C.green, C.red], alpha=0.75,
              labels=["convección", "radiación", "evaporación"])
ax2.set_xlabel("temperatura del café (°C)")
ax2.set_ylabel("fracción de la pérdida")
ax2.set_title("Quién manda a cada temperatura")
ax2.legend(fontsize=8.5, loc="lower left")
ax2.set_ylim(0, 1)

for Tc0 in (90, 70, 50, 30):
    i = int(np.argmin(np.abs(Tc - Tc0)))
    print(f"{Tc0:3d} °C: conv {100*fracciones[0,i]:4.1f} %  "
          f"rad {100*fracciones[1,i]:4.1f} %  evap {100*fracciones[2,i]:4.1f} %  "
          f"total {conv[i]+rad[i]+evap[i]:5.1f} W")
save(fig, "fig_mecanismos_cafe")
