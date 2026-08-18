"""Muestreo: ¿por qué las ruedas de las películas giran al revés?

Una sinusoide muestreada por encima y por debajo de Nyquist, y el espectro
resultante con la frecuencia replegada.

La figura responde: ¿qué información se pierde exactamente al muestrear, y se
puede recuperar?

Ejecutar:  python fig_aliasing.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

FS = 10.0                     # frecuencia de muestreo, Hz
T = 2.0
t_fino = np.linspace(0, T, 4000)
t_muestra = np.arange(0, T, 1 / FS)

fig, axes = plt.subplots(2, 2, figsize=(10.4, 5.6),
                         gridspec_kw={"hspace": 0.45})

for fila, f0 in enumerate([3.0, 8.0]):
    ax = axes[fila, 0]
    ax.plot(t_fino, np.sin(2 * np.pi * f0 * t_fino), color=C.blue, lw=1.2,
            label=f"señal real, {f0:.0f} Hz")
    ax.plot(t_muestra, np.sin(2 * np.pi * f0 * t_muestra), "o", color=C.red,
            ms=6, label=f"muestras a {FS:.0f} Hz")
    f_alias = abs(f0 - FS * round(f0 / FS))
    ax.plot(t_fino, np.sin(2 * np.pi * f_alias * t_fino) *
            np.sign(np.cos(np.pi * round(f0 / FS))), "--", color=C.ochre,
            lw=1.6, label=f"alias, {f_alias:.0f} Hz")
    ax.set_xlim(0, 1), ax.set_ylim(-1.6, 1.6)
    ax.set_xlabel("tiempo (s)")
    ax.set_title(f"$f_0$ = {f0:.0f} Hz  "
                 f"({'por debajo' if f0 < FS/2 else 'POR ENCIMA'} de Nyquist "
                 f"= {FS/2:.0f} Hz)", fontsize=9.5)
    ax.legend(fontsize=7.4, loc="upper right")

    # espectro de las muestras
    ax = axes[fila, 1]
    n = 512
    tt = np.arange(n) / FS
    x = np.sin(2 * np.pi * f0 * tt)
    esp = np.abs(np.fft.rfft(x * np.hanning(n)))
    frec = np.fft.rfftfreq(n, 1 / FS)
    ax.plot(frec, esp / esp.max(), color=C.blue, lw=1.6)
    ax.axvline(FS / 2, color=C.red, ls="--", lw=1.4)
    ax.text(FS / 2 - 0.15, 0.85, "Nyquist", rotation=90, fontsize=8,
            color=C.red, ha="right")
    ax.set_xlabel("frecuencia (Hz)"), ax.set_ylabel("amplitud")
    ax.set_title(f"Lo que ve el analizador: un pico en {f_alias:.0f} Hz",
                 fontsize=9.5)
    print(f"f0={f0} Hz  ->  alias en {f_alias} Hz")

save(fig, "fig_aliasing")
