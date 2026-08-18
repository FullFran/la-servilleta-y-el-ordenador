"""¿Cuánto hay que esperar en una cola?

Tiempo de espera frente a la utilización en M/M/1, efecto de la variabilidad,
y comparación con una simulación por eventos discretos.

La figura responde: ¿por qué una cola no se degrada gradualmente al saturar?

Ejecutar:  python fig_colas.py
"""
import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(1909)


def simula_cola(lam, mu, n=200_000, cv_servicio=1.0):
    """M/G/1 por eventos discretos. cv=1 exponencial, cv=0 determinista."""
    llegadas = np.cumsum(r.exponential(1 / lam, n))
    if cv_servicio == 0:
        servicio = np.full(n, 1 / mu)
    else:
        k = 1 / cv_servicio**2
        servicio = r.gamma(k, 1 / (mu * k), n)
    salida = np.empty(n)
    libre = 0.0
    for i in range(n):
        inicio = max(llegadas[i], libre)
        salida[i] = inicio + servicio[i]
        libre = salida[i]
    return (salida - llegadas).mean()


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))

rho = np.linspace(0.05, 0.97, 200)
ax1.plot(rho, 1 / (1 - rho), color=C.blue, lw=2.4,
         label=r"M/M/1:  $W=\frac{1/\mu}{1-\rho}$")
ax1.plot(rho, (1 + rho) / (2 * (1 - rho)), color=C.green, lw=2.0,
         label="M/D/1 (servicio determinista)")
for rr, color in [(0.5, C.grey), (0.8, C.ochre), (0.95, C.red)]:
    ax1.plot(rr, 1 / (1 - rr), "o", color=color, ms=8)
    ax1.annotate(f"$\\rho$={rr}: {1/(1-rr):.0f}×", (rr, 1 / (1 - rr)),
                 textcoords="offset points", xytext=(-52, 4), fontsize=8.4,
                 color=color)
ax1.set_yscale("log")
ax1.set_xlabel(r"utilización $\rho=\lambda/\mu$")
ax1.set_ylabel("tiempo en el sistema (en unidades de $1/\\mu$)")
ax1.set_title("La espera diverge, no se degrada")
ax1.legend(fontsize=8.5)

rhos = np.array([0.3, 0.5, 0.7, 0.85, 0.92])
for cv, color, etiqueta in [(1.0, C.blue, "exponencial (cv=1)"),
                            (0.0, C.green, "determinista (cv=0)"),
                            (2.0, C.red, "muy variable (cv=2)")]:
    W = [simula_cola(rr, 1.0, 60_000, cv) for rr in rhos]
    ax2.plot(rhos, W, "o-", color=color, ms=5, lw=1.5, label=etiqueta)
    print(f"cv={cv}: W en rho=0.85 -> {W[3]:.2f} (M/M/1 teórico: "
          f"{1/(1-0.85):.2f})")
ax2.set_yscale("log")
ax2.set_xlabel(r"utilización $\rho$")
ax2.set_ylabel("tiempo medio en el sistema")
ax2.set_title("La variabilidad del servicio manda tanto como la carga")
ax2.legend(fontsize=8.5)

save(fig, "fig_colas")
