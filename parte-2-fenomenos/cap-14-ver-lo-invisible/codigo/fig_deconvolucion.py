"""¿Cómo se ve lo que no se puede ver?

Deconvolución de una señal borrosa con ruido: la inversión ingenua explota, la
regularizada funciona, y la curva L da el parámetro.

La figura responde: ¿por qué deshacer un desenfoque no es simplemente dividir?

Ejecutar:  python fig_deconvolucion.py
"""
import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(140)

N = 1024
x = np.linspace(0, 1, N)
verdad = (np.exp(-((x - 0.3) / 0.012) ** 2) + 0.7 * np.exp(-((x - 0.35) / 0.012) ** 2)
          + 0.9 * np.exp(-((x - 0.65) / 0.03) ** 2)
          + 0.5 * ((x > 0.8) & (x < 0.86)))

ANCHO = 0.02
k = np.exp(-((x - 0.5) / ANCHO) ** 2)
k /= k.sum()
K = np.fft.rfft(np.fft.ifftshift(k))
S = np.fft.rfft(verdad)
RUIDO = 2e-3
medido = np.fft.irfft(K * S, N) + r.normal(0, RUIDO, N)

# La inversión ingenua es cuatro órdenes de magnitud mayor que la señal: si se
# dibuja en los mismos ejes tapa todo lo demás y no se ve nada. Va en su propio
# panel, con su propia escala. Que necesite otra escala ES el resultado.
fig = plt.figure(figsize=(10.6, 4.6))
gs = fig.add_gridspec(2, 2, height_ratios=[1, 1.9], width_ratios=[1, 1],
                      hspace=0.45, wspace=0.28)
ax0 = fig.add_subplot(gs[0, 0])
ax1 = fig.add_subplot(gs[1, 0])
ax2 = fig.add_subplot(gs[:, 1])

M = np.fft.rfft(medido)
ingenua = np.fft.irfft(M / K, N)
ax0.plot(x, ingenua, color=C.red, lw=0.7)
ax0.set_xlim(0.2, 0.95)
ax0.set_ylabel("$M/K$", fontsize=9)
ax0.set_xticklabels([])
ax0.set_title("Inversión ingenua: mira la escala del eje", fontsize=9.5)

ax1.plot(x, verdad, color=C.ink, lw=1.8, label="verdad")
ax1.plot(x, medido, color=C.grey, lw=1.2, label="medido (borroso + ruido)")

lambdas = np.logspace(-8, 1, 60)
residuos, normas, soluciones = [], [], []
for lam in lambdas:
    W = np.conj(K) / (np.abs(K) ** 2 + lam)
    sol = np.fft.irfft(W * M, N)
    soluciones.append(sol)
    residuos.append(np.linalg.norm(np.fft.irfft(K * np.fft.rfft(sol), N) - medido))
    normas.append(np.linalg.norm(np.diff(sol)))
residuos, normas = np.array(residuos), np.array(normas)

# Esquina de la curva L: máxima curvatura en log-log
lr, ln_ = np.log(residuos), np.log(normas)
curv = np.gradient(np.gradient(ln_, lr), lr)
i_opt = int(np.argmax(np.abs(curv[3:-3]))) + 3
ax1.plot(x, soluciones[i_opt], color=C.green, lw=1.8,
         label=f"Tikhonov, $\\lambda$={lambdas[i_opt]:.1e}")
ax1.set_xlim(0.2, 0.95), ax1.set_ylim(-0.35, 1.35)
ax1.set_xlabel("$x$"), ax1.set_ylabel("señal")
ax1.set_title("Regularizar sí recupera la señal", fontsize=9.5)
ax1.legend(fontsize=7.6, loc="upper right")

ax2.loglog(residuos, normas, "o-", color=C.blue, ms=3.5, lw=1.2)
ax2.plot(residuos[i_opt], normas[i_opt], "*", color=C.red, ms=16)
ax2.annotate(f"esquina: $\\lambda$={lambdas[i_opt]:.1e}",
             (residuos[i_opt], normas[i_opt]), textcoords="offset points",
             xytext=(12, 10), fontsize=8.6, color=C.red)
ax2.set_xlabel("norma del residuo $\\|Kf-m\\|$")
ax2.set_ylabel("rugosidad de la solución $\\|f'\\|$")
ax2.set_title("Curva L: el compromiso, dibujado")

print(f"lambda óptimo por curva L: {lambdas[i_opt]:.2e}")
print(f"error de la ingenua: {np.linalg.norm(ingenua-verdad):.2e}")
print(f"amplitud máxima de la ingenua: {np.abs(ingenua).max():.1f} "
      f"(la señal vale {verdad.max():.1f})")
print(f"error de la regularizada: {np.linalg.norm(soluciones[i_opt]-verdad):.2e}")
save(fig, "fig_deconvolucion")
