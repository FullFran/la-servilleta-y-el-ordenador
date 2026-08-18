"""¿Qué significa exactamente que dos sistemas sean «semejantes»?

Integra el péndulo no lineal para muchas longitudes, gravedades y amplitudes.
Primero se dibuja el periodo crudo (un desastre de curvas) y después el
periodo adimensional frente a la amplitud (una sola curva).

La figura responde: ¿cuántos parámetros tiene realmente el problema?

Ejecutar:  python fig_colapso_pendulo.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()


def periodo(longitud: float, gravedad: float, amplitud: float) -> float:
    """Periodo del péndulo simple no lineal, por cruce por cero."""
    def f(_t, y):
        return [y[1], -(gravedad / longitud) * np.sin(y[0])]

    def cruce(_t, y):
        return y[0]
    cruce.direction = 1.0          # sólo cruces ascendentes

    t_max = 20 * 2 * np.pi * np.sqrt(longitud / gravedad)
    sol = solve_ivp(f, (0, t_max), [amplitud, 0.0], events=cruce,
                    rtol=1e-10, atol=1e-12, dense_output=True)
    cruces = sol.t_events[0]
    return float(np.mean(np.diff(cruces))) if len(cruces) > 2 else np.nan


LONGITUDES = [0.25, 0.5, 1.0, 2.0]
GRAVEDADES = [1.62, 3.72, 9.81, 24.8]      # Luna, Marte, Tierra, Júpiter
amplitudes = np.linspace(0.05, 3.0, 24)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.0, 4.2))
colores = [C.blue, C.red, C.green, C.ochre]

for L, color in zip(LONGITUDES, colores):
    for g, marca in zip(GRAVEDADES, ["o", "s", "^", "d"]):
        T = np.array([periodo(L, g, a) for a in amplitudes])
        ax1.plot(amplitudes, T, marca, color=color, ms=3, alpha=0.6)
        ax2.plot(amplitudes, T / (2 * np.pi * np.sqrt(L / g)), marca,
                 color=color, ms=3, alpha=0.6)

ax1.set_xlabel(r"amplitud inicial $\theta_0$ (rad)")
ax1.set_ylabel("periodo $T$ (s)")
ax1.set_title("16 combinaciones de $L$ y $g$: 16 curvas")
ax1.set_yscale("log")

# Curva teórica del colapso: T/T_0 = (2/pi) K(sin^2(theta0/2))
from scipy.special import ellipk  # noqa: E402
th = np.linspace(0.01, 3.0, 200)
ax2.plot(th, (2 / np.pi) * ellipk(np.sin(th / 2) ** 2), "-", color=C.ink,
         lw=1.8, label=r"$\frac{2}{\pi}K\!\left(\sin^2\frac{\theta_0}{2}\right)$")
ax2.axhline(1.0, color=C.grey, ls="--", lw=1.0)
ax2.text(0.1, 1.02, "aproximación de ángulo pequeño", color=C.grey, fontsize=8)
ax2.set_xlabel(r"amplitud inicial $\theta_0$ (rad)")
ax2.set_ylabel(r"$T\,/\,2\pi\sqrt{L/g}$")
ax2.set_title("Las mismas 16: una sola curva")
ax2.legend(loc="upper left")

save(fig, "fig_colapso_pendulo")
