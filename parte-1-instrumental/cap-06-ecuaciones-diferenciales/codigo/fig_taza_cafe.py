"""¿Cuánto tarda un café en enfriarse, y qué es exactamente tau?

Ajusta la ley de Newton del enfriamiento a datos sintéticos con ruido realista
y muestra que en escala logarítmica es una recta cuya pendiente es -1/tau.

La figura responde: ¿por qué el tiempo característico no depende de la
temperatura inicial?

Ejecutar:  python fig_taza_cafe.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(60)

T_AMB, TAU = 21.0, 24.0          # °C y minutos
t = np.arange(0, 91, 5.0)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.2, 4.1))

for T0, color in [(88.0, C.red), (65.0, C.ochre), (45.0, C.blue)]:
    T = T_AMB + (T0 - T_AMB) * np.exp(-t / TAU) + r.normal(0, 0.6, t.size)
    ax1.plot(t, T, "o", color=color, ms=4, label=f"$T_0$ = {T0:.0f} °C")

    def modelo(tt, T_amb, T0_, tau):
        return T_amb + (T0_ - T_amb) * np.exp(-tt / tau)

    popt, _ = curve_fit(modelo, t, T, p0=[20, T0, 20])
    tt = np.linspace(0, 90, 200)
    ax1.plot(tt, modelo(tt, *popt), color=color, lw=1.4, alpha=0.8)
    ax2.semilogy(t, np.maximum(T - popt[0], 1e-2), "o", color=color, ms=4)
    ax2.semilogy(tt, (popt[1] - popt[0]) * np.exp(-tt / popt[2]), color=color,
                 lw=1.4, alpha=0.8)
    print(f"T0={T0:5.1f}  ->  T_amb={popt[0]:5.2f}  tau={popt[2]:5.2f} min")

ax1.axhline(T_AMB, color=C.grey, ls="--", lw=1.1)
ax1.text(70, T_AMB + 1.2, "temperatura ambiente", fontsize=8.4, color=C.grey)
ax1.set_xlabel("tiempo (min)"), ax1.set_ylabel("temperatura (°C)")
ax1.set_title("Tres cafés distintos")
ax1.legend(fontsize=8)

ax2.set_xlabel("tiempo (min)")
ax2.set_ylabel(r"$T-T_{\mathrm{amb}}$ (°C)")
ax2.set_title(r"En escala log: tres rectas paralelas de pendiente $-1/\tau$")
ax2.annotate(r"la misma $\tau$ para los tres:"
             "\nel sistema olvida su condición inicial",
             xy=(60, 5), xytext=(8, 1.4), fontsize=8.6, color=C.ink,
             arrowprops=dict(arrowstyle="->", color=C.ink, lw=1.0))

save(fig, "fig_taza_cafe")
