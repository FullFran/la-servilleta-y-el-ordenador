"""Convolución y filtrado: ¿por qué el teorema de convolución lo cambia todo?

Una señal con ruido, filtrada por convolución en el dominio del tiempo y por
multiplicación en el de la frecuencia, con el coste computacional comparado.

La figura responde: ¿qué es exactamente un filtro?

Ejecutar:  python fig_convolucion.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(12)

N = 2000
t = np.linspace(0, 4, N)
limpia = np.sin(2 * np.pi * 1.5 * t) + 0.6 * np.sin(2 * np.pi * 4.0 * t)
ruido = 0.9 * r.standard_normal(N)
señal = limpia + ruido

# Núcleo gaussiano
ancho = 25
k = np.exp(-0.5 * (np.arange(-3 * ancho, 3 * ancho + 1) / ancho) ** 2)
k /= k.sum()
filtrada = np.convolve(señal, k, mode="same")

fig, axes = plt.subplots(2, 2, figsize=(10.6, 5.6),
                         gridspec_kw={"hspace": 0.45})

ax = axes[0, 0]
ax.plot(t, señal, color=C.grey, lw=0.6, label="con ruido")
ax.plot(t, limpia, color=C.ink, lw=1.6, label="verdad")
ax.set_xlabel("tiempo"), ax.set_title("La señal", fontsize=10)
ax.legend(fontsize=7.6)

ax = axes[0, 1]
ax.plot(np.arange(len(k)) - len(k) // 2, k, color=C.blue, lw=1.8)
ax.set_xlabel("retardo (muestras)")
ax.set_title("El núcleo del filtro $h$", fontsize=10)

ax = axes[1, 0]
ax.plot(t, filtrada, color=C.red, lw=1.6, label="filtrada")
ax.plot(t, limpia, color=C.ink, lw=1.2, alpha=0.7, label="verdad")
ax.set_xlabel("tiempo")
ax.set_title("Convolución: promedio con memoria", fontsize=10)
ax.legend(fontsize=7.6)

ax = axes[1, 1]
frec = np.fft.rfftfreq(N, t[1] - t[0])
H = np.abs(np.fft.rfft(np.roll(np.pad(k, (0, N - len(k))), -(len(k) // 2))))
ax.plot(frec, np.abs(np.fft.rfft(señal)) / N * 2, color=C.grey, lw=0.8,
        label="espectro de la señal")
ax.plot(frec, H, color=C.blue, lw=2.0, label="$|H(f)|$: respuesta del filtro")
ax.set_xlim(0, 12), ax.set_xlabel("frecuencia (Hz)")
ax.set_title("En frecuencia, el filtro es una multiplicación", fontsize=10)
ax.legend(fontsize=7.6)

for n in [1_000, 10_000, 1_000_000]:
    print(f"N={n:>9,}:  directo N^2 = {n**2:.1e},  FFT N log2 N = "
          f"{n*np.log2(n):.1e},  factor {n / np.log2(n):.0f}")
save(fig, "fig_convolucion")
