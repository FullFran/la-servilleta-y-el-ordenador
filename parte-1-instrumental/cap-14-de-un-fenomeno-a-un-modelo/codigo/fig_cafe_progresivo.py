"""La taza de café, cuarta visita: cuando el modelo mínimo no basta.

Datos sintéticos realistas de enfriamiento con evaporación. Ajuste con el
modelo de Newton, sus residuos, y el modelo mejorado.

La figura responde: ¿cómo se sabe que hace falta más modelo, y cuánto más?

Ejecutar:  python fig_cafe_progresivo.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(140)

T_AMB = 21.0
t = np.arange(0, 121, 3.0)

# "Verdad" sintética: convección lineal MÁS evaporación, que depende de forma
# no lineal del salto térmico. Coeficientes en K/min, ajustados para reproducir
# un enfriamiento realista (92 -> 70 °C en unos 15 minutos).
TAU_CONV = 32.0          # min, término de Newton puro
K_EVAP = 3.0e-4          # K^{-0.9} min^{-1}, evaporación


def verdad(t):
    """Integra la EDO 'real' con paso fino y devuelve los valores en t."""
    dt = 0.02
    Ti, tt, idx = 92.0, 0.0, 0
    salida = []
    while idx < len(t):
        if tt >= t[idx] - 1e-9:
            salida.append(Ti)
            idx += 1
            continue
        d = Ti - T_AMB
        Ti += (-d / TAU_CONV - K_EVAP * d**1.9) * dt
        tt += dt
    return np.array(salida)


T_datos = verdad(t) + r.normal(0, 0.35, t.size)


def newton(t, T0, tau):
    return T_AMB + (T0 - T_AMB) * np.exp(-t / tau)


def dos_exp(t, T0, tau1, f, tau2):
    a = (T0 - T_AMB)
    return T_AMB + a * (f * np.exp(-t / tau1) + (1 - f) * np.exp(-t / tau2))


p1, _ = curve_fit(newton, t, T_datos, p0=[92, 25])
p2, _ = curve_fit(dos_exp, t, T_datos, p0=[92, 10, 0.4, 40],
                  maxfev=40000)
res1 = T_datos - newton(t, *p1)
res2 = T_datos - dos_exp(t, *p2)

fig, axes = plt.subplots(2, 2, figsize=(10.4, 6.0), sharex=True,
                         gridspec_kw={"height_ratios": [1.7, 1], "hspace": 0.12})

for col, (nombre, modelo, p, res) in enumerate([
        ("Modelo mínimo: Newton", newton, p1, res1),
        ("Dos escalas de tiempo", dos_exp, p2, res2)]):
    ax = axes[0, col]
    ax.plot(t, T_datos, "o", color=C.red, ms=3.5, label="datos")
    tt = np.linspace(0, 120, 400)
    ax.plot(tt, modelo(tt, *p), color=C.blue, lw=1.8, label="ajuste")
    ax.axhline(T_AMB, color=C.grey, ls="--", lw=1.0)
    ax.set_ylabel("temperatura (°C)")
    rms = np.std(res)
    ax.set_title(f"{nombre}\nrms de los residuos = {rms:.2f} °C", fontsize=10)
    ax.legend(fontsize=8)

    ax = axes[1, col]
    ax.axhline(0, color=C.ink, lw=1.1)
    ax.axhspan(-0.35, 0.35, color=C.grey, alpha=0.2)
    ax.plot(t, res, "o-", color=C.ochre if col == 0 else C.green, ms=3.5, lw=1)
    ax.set_xlabel("tiempo (min)"), ax.set_ylabel("residuo (°C)")
    ax.set_ylim(-2.2, 2.2)
    print(f"{nombre:26s} rms={rms:.3f} °C   parámetros={np.round(p,3)}")

axes[1, 0].text(35, 1.35, "estructura clara:\nel modelo está incompleto",
                fontsize=8.6, color=C.red)
axes[1, 1].text(35, 1.35, "ruido: el modelo agota\nla información de los datos",
                fontsize=8.6, color=C.green)
axes[1, 0].text(3, -2.0, "banda gris: ruido de medida declarado (0,35 °C)",
                fontsize=7.6, color=C.grey)

save(fig, "fig_cafe_progresivo")
