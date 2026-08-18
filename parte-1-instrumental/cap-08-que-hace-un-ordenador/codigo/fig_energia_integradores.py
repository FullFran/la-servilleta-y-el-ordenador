"""¿Qué pasa si integras una órbita durante mucho tiempo?

Oscilador armónico integrado con Euler explícito, Euler implícito, RK4 y Euler
simpléctico. Se dibuja la energía y el retrato de fases.

La figura responde: ¿por qué un método de orden 1 puede batir a uno de orden 4
en el largo plazo?

Ejecutar:  python fig_energia_integradores.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

H, N = 0.05, 40_000          # paso y número de pasos
t = np.arange(N + 1) * H


def integra(metodo):
    q = np.empty(N + 1)
    p = np.empty(N + 1)
    q[0], p[0] = 1.0, 0.0
    for i in range(N):
        if metodo == "euler":
            q[i + 1] = q[i] + H * p[i]
            p[i + 1] = p[i] - H * q[i]
        elif metodo == "implicito":
            den = 1 + H**2
            q[i + 1] = (q[i] + H * p[i]) / den
            p[i + 1] = (p[i] - H * q[i]) / den
        elif metodo == "simplectico":
            p[i + 1] = p[i] - H * q[i]           # primero p, con q antiguo
            q[i + 1] = q[i] + H * p[i + 1]       # después q, con p nuevo
        elif metodo == "rk4":
            def der(y):
                return np.array([y[1], -y[0]])
            y = np.array([q[i], p[i]])
            k1 = der(y); k2 = der(y + H * k1 / 2)
            k3 = der(y + H * k2 / 2); k4 = der(y + H * k3)
            y = y + H * (k1 + 2 * k2 + 2 * k3 + k4) / 6
            q[i + 1], p[i + 1] = y
    return q, p


METODOS = [("euler", "Euler explícito (orden 1)", C.red),
           ("implicito", "Euler implícito (orden 1)", C.ochre),
           ("rk4", "Runge–Kutta 4 (orden 4)", C.blue),
           ("simplectico", "Euler simpléctico (orden 1)", C.green)]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))

for clave, nombre, color in METODOS:
    q, p = integra(clave)
    E = 0.5 * (q**2 + p**2)
    ax1.plot(t, E, color=color, lw=1.5, label=nombre)
    ax2.plot(q[-2000:], p[-2000:], color=color, lw=1.0, alpha=0.85)
    print(f"{nombre:32s} E final = {E[-1]:.4f}  (exacta 0.5)")

ax1.set_yscale("log")
ax1.axhline(0.5, color=C.ink, ls="--", lw=1.2)
ax1.text(50, 0.55, "energía exacta", fontsize=8.4, color=C.ink)
ax1.set_xlabel("tiempo"), ax1.set_ylabel("energía")
ax1.set_title("2000 periodos de un oscilador armónico")
ax1.legend(fontsize=7.8, loc="center left")
ax1.set_ylim(1e-3, 1e3)

ax2.set_xlabel("$q$"), ax2.set_ylabel("$p$")
ax2.set_title("Últimos 2000 pasos en el plano de fases")
ax2.set_aspect("equal")
ax2.set_xlim(-2.2, 2.2), ax2.set_ylim(-2.2, 2.2)
circulo = np.linspace(0, 2 * np.pi, 200)
ax2.plot(np.cos(circulo), np.sin(circulo), "--", color=C.ink, lw=1.2)

save(fig, "fig_energia_integradores")
