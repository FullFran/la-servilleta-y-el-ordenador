"""¿Por qué no se estima un espectro con el módulo de la FFT a secas?

Comparación entre el periodograma crudo y la estimación de Welch para ruido
coloreado más dos tonos.

La figura responde: ¿por qué el periodograma no mejora al tomar más datos?

Ejecutar:  python fig_psd.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(19)

FS = 1000.0
N = 2**16
t = np.arange(N) / FS

# Ruido 1/f más dos tonos débiles
blanco = r.standard_normal(N)
espectro = np.fft.rfft(blanco)
frec = np.fft.rfftfreq(N, 1 / FS)
espectro[1:] /= np.sqrt(frec[1:])
x = np.fft.irfft(espectro, N)
x = x / x.std()
x += 0.35 * np.sin(2 * np.pi * 120 * t) + 0.25 * np.sin(2 * np.pi * 250 * t)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))

# --- Periodograma crudo: no converge -------------------------------------
for n_usar, color, alpha in [(2**12, C.grey, 0.5), (2**16, C.red, 0.8)]:
    f, P = signal.periodogram(x[:n_usar], FS)
    ax1.loglog(f[1:], P[1:], color=color, lw=0.5, alpha=alpha,
               label=f"periodograma, N = {n_usar}")
ax1.set_xlabel("frecuencia (Hz)"), ax1.set_ylabel("densidad espectral")
ax1.set_title("Periodograma: más datos, igual de ruidoso")
ax1.legend(fontsize=8)
ax1.set_ylim(1e-9, 1e1)

# --- Welch: promedia segmentos -------------------------------------------
for nperseg, color in [(256, C.ochre), (1024, C.green), (4096, C.blue)]:
    f, P = signal.welch(x, FS, nperseg=nperseg)
    ax2.loglog(f[1:], P[1:], color=color, lw=1.4,
               label=f"Welch, ventana {nperseg}")
ax2.loglog(f[1:], 2e-3 / f[1:], "--", color=C.ink, lw=1.2, label="$1/f$")
for f0 in (120, 250):
    ax2.axvline(f0, color=C.red, lw=0.8, alpha=0.5)
ax2.set_xlabel("frecuencia (Hz)"), ax2.set_ylabel("densidad espectral")
ax2.set_title("Welch: promediar reduce la varianza")
ax2.legend(fontsize=8)
ax2.set_ylim(1e-9, 1e1)

f1, P1 = signal.periodogram(x, FS)
f2, P2 = signal.welch(x, FS, nperseg=1024)
print(f"desv. típica de log10(P) — periodograma: {np.std(np.log10(P1[10:])):.3f}")
print(f"desv. típica de log10(P) — Welch(1024): {np.std(np.log10(P2[5:])):.3f}")
save(fig, "fig_psd")
