"""Metropolis: ¿cómo se muestrea algo que no sabes normalizar?

Cadena de Metropolis sobre una distribución bimodal, con tres tamaños de
paso. Se muestran la traza, el histograma y la autocorrelación.

La figura responde: ¿cómo se ve una cadena que parece convergida y no lo está?

Ejecutar:  python fig_metropolis.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(1953)


def log_p(x):
    """Bimodal: dos gaussianas separadas. No está normalizada, y da igual."""
    return np.logaddexp(-0.5 * ((x + 3) / 0.6) ** 2,
                        -0.5 * ((x - 3) / 0.6) ** 2)


def metropolis(paso, n=60_000, x0=-3.0):
    """Metropolis con paso gaussiano. Los sorteos se generan de golpe."""
    saltos = r.normal(0.0, paso, n)
    log_u = np.log(r.random(n))
    x, lp = x0, log_p(x0)
    cadena = np.empty(n)
    aceptados = 0
    for i in range(n):
        propuesta = x + saltos[i]
        lp_nuevo = log_p(propuesta)
        if log_u[i] < lp_nuevo - lp:
            x, lp = propuesta, lp_nuevo
            aceptados += 1
        cadena[i] = x
    return cadena, aceptados / n


def autocorr(x, maxlag=400):
    """Autocorrelación por FFT: O(N log N) en lugar de O(N^2)."""
    x = x - x.mean()
    n = 1 << (2 * len(x) - 1).bit_length()
    f = np.fft.rfft(x, n)
    c = np.fft.irfft(f * np.conj(f), n)[:maxlag]
    return c / c[0]


PASOS = [(0.2, "paso 0,2 — apenas se mueve"),
         (1.5, "paso 1,5 — aceptación «de manual»"),
         (8.0, "paso 8,0 — el único que cruza")]
fig, axes = plt.subplots(3, 3, figsize=(11.4, 6.6),
                         gridspec_kw={"width_ratios": [1.5, 1, 1],
                                      "hspace": 0.55, "wspace": 0.3})

xx = np.linspace(-6, 6, 400)
densidad = np.exp(log_p(xx))
densidad /= np.trapezoid(densidad, xx) if hasattr(np, "trapezoid") else np.trapz(densidad, xx)

for fila, (paso, titulo) in enumerate(PASOS):
    cadena, tasa = metropolis(paso)
    color = [C.red, C.green, C.ochre][fila]

    ax = axes[fila, 0]
    ax.plot(cadena[:8000], color=color, lw=0.5)
    ax.set_ylabel("$x$")
    ax.set_title(f"{titulo} — aceptación {tasa:.0%}", fontsize=9.5)
    ax.set_ylim(-6, 6)
    if fila == 2:
        ax.set_xlabel("iteración")

    ax = axes[fila, 1]
    ax.hist(cadena[5000:], bins=80, density=True, color=color, alpha=0.55,
            edgecolor="none")
    ax.plot(xx, densidad, color=C.ink, lw=1.6)
    ax.set_yticks([])
    ax.set_title("histograma frente a la verdad", fontsize=9)
    if fila == 2:
        ax.set_xlabel("$x$")

    ax = axes[fila, 2]
    ac = autocorr(cadena[5000:])
    ax.plot(ac, color=color, lw=1.4)
    ax.axhline(0, color=C.ink, lw=0.9)
    tau = 1 + 2 * np.sum(ac[:200])
    ax.set_title(f"autocorrelación, $\\tau_{{int}}\\approx${tau:.0f}",
                 fontsize=9)
    ax.set_ylim(-0.2, 1.05)
    if fila == 2:
        ax.set_xlabel("retardo")
    print(f"{titulo:24s} aceptación {tasa:5.1%}  tau_int ≈ {tau:6.0f}  "
          f"N_eficaz ≈ {len(cadena[5000:]) / max(tau, 1):.0f}")

save(fig, "fig_metropolis")
