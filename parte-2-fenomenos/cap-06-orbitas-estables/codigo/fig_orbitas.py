"""¿Por qué algunas órbitas son estables y otras son un artefacto numérico?

Órbita kepleriana excéntrica integrada 2000 periodos con RK4 y con Verlet, con
la energía y el momento angular.

La figura responde: ¿de quién es la precesión que veo, de la física o del
integrador?

Ejecutar:  python fig_orbitas.py
"""
import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

E_EXC = 0.8
q0 = np.array([1 - E_EXC, 0.0])
p0 = np.array([0.0, np.sqrt((1 + E_EXC) / (1 - E_EXC))])
H = 0.03
N = 1_200_000


def acel(q):
    r = np.linalg.norm(q)
    return -q / r**3


def energia(q, p):
    return 0.5 * p @ p - 1 / np.linalg.norm(q)


def integra(metodo):
    q, p = q0.copy(), p0.copy()
    qs, Es, Ls = [], [], []
    a = acel(q)
    for k in range(N):
        if metodo == "verlet":
            p = p + 0.5 * H * a
            q = q + H * p
            a = acel(q)
            p = p + 0.5 * H * a
        else:
            def der(y):
                qq, pp = y[:2], y[2:]
                return np.concatenate([pp, acel(qq)])
            y = np.concatenate([q, p])
            k1 = der(y); k2 = der(y + H * k1 / 2)
            k3 = der(y + H * k2 / 2); k4 = der(y + H * k3)
            y = y + H * (k1 + 2 * k2 + 2 * k3 + k4) / 6
            q, p = y[:2], y[2:]
            a = acel(q)
        if k % 200 == 0:
            qs.append(q.copy()), Es.append(energia(q, p))
            Ls.append(q[0] * p[1] - q[1] * p[0])
    return np.array(qs), np.array(Es), np.array(Ls)


fig, axes = plt.subplots(1, 3, figsize=(11.6, 4.0))
t = np.arange(0, N, 200) * H

for metodo, nombre, color in [("rk4", "Runge–Kutta 4", C.red),
                              ("verlet", "Verlet (simpléctico)", C.green)]:
    qs, Es, Ls = integra(metodo)
    axes[0].plot(qs[-3000:, 0], qs[-3000:, 1], color=color, lw=0.7,
                 label=nombre)
    axes[1].plot(t, Es, color=color, lw=1.2, label=nombre)
    axes[2].plot(t, np.abs(Ls / Ls[0] - 1) + 1e-17, color=color, lw=1.2,
                 label=nombre)
    pendiente = np.polyfit(t, Es, 1)[0]
    banda = Es.max() - Es.min()
    print(f"{nombre:22s}: deriva secular {pendiente:+.2e}/ut   "
          f"anchura de la banda {banda:.2e}   "
          f"deriva total {abs(Es[-1]/Es[0]-1):.2e}")

axes[0].plot(0, 0, "*", color=C.ochre, ms=15)
axes[0].set_aspect("equal")
axes[0].set_xlabel("$x$"), axes[0].set_ylabel("$y$")
axes[0].set_title("Últimas órbitas, tras 2500 periodos", fontsize=10)
axes[0].legend(fontsize=7.6)

axes[1].axhline(energia(q0, p0), color=C.ink, ls="--", lw=1.2)
axes[1].set_xlabel("tiempo"), axes[1].set_ylabel("energía")
axes[1].set_title("La energía debería ser constante", fontsize=10)
axes[1].legend(fontsize=7.6)

axes[2].set_yscale("log")
axes[2].set_xlabel("tiempo"), axes[2].set_ylabel("error relativo de $L$")
axes[2].set_title("Momento angular", fontsize=10)
axes[2].legend(fontsize=7.6)

save(fig, "fig_orbitas")
