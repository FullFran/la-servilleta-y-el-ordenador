"""El primer experimento numérico que sorprendió a todo el mundo.

Reproduce el experimento de Fermi, Pasta, Ulam y Tsingou (1955): una cadena de
osciladores no lineales que, en lugar de termalizar, vuelve casi exactamente a
su estado inicial.

La figura responde: ¿qué pasa cuando el ordenador contradice la intuición de
tres físicos de primera fila?

Ejecutar:  python fig_fpu.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

N = 32                     # osciladores interiores
ALFA = 0.25                # no linealidad cuadrática
DT = 0.05
PASOS = 1_600_000

# Condición inicial: sólo el primer modo excitado
j = np.arange(1, N + 1)
modos = np.arange(1, N + 1)
x = np.sin(np.pi * j / (N + 1))
v = np.zeros(N)


def fuerzas(x):
    xe = np.concatenate(([0.0], x, [0.0]))
    d = np.diff(xe)                        # x_{i+1} - x_i
    f_lineal = d[1:] - d[:-1]
    f_no_lineal = ALFA * (d[1:]**2 - d[:-1]**2)
    return f_lineal + f_no_lineal


def energia_modos(x, v):
    """Energía en cada modo normal de la cadena lineal."""
    s = np.sqrt(2 / (N + 1)) * np.sin(np.pi * np.outer(modos, j) / (N + 1))
    a, adot = s @ x, s @ v
    w = 2 * np.sin(np.pi * modos / (2 * (N + 1)))
    return 0.5 * (adot**2 + (w * a) ** 2)


guardar_cada = 2000
tiempos, historial = [], []
a = fuerzas(x)
for paso in range(PASOS):
    v += 0.5 * DT * a                      # Verlet de velocidades
    x += DT * v
    a = fuerzas(x)
    v += 0.5 * DT * a
    if paso % guardar_cada == 0:
        historial.append(energia_modos(x, v))
        tiempos.append(paso * DT)

historial = np.array(historial)
tiempos = np.array(tiempos)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.6, 4.2),
                               gridspec_kw={"width_ratios": [1.5, 1]})

for k, color in zip([1, 2, 3, 4, 5],
                    [C.blue, C.red, C.green, C.ochre, C.purple]):
    ax1.plot(tiempos, historial[:, k - 1], color=color, lw=1.0,
             label=f"modo {k}")
ax1.set_xlabel("tiempo")
ax1.set_ylabel("energía del modo")
ax1.set_title("Cadena no lineal de 32 osciladores: sólo el modo 1 excitado")
ax1.legend(fontsize=8, ncol=5, loc="upper center")

# Recurrencia: cuánta energía vuelve al modo 1
e1 = historial[:, 0]
e_total = historial.sum(axis=1)
frac = e1 / e_total
i_rec = np.argmax(frac[len(frac) // 6:]) + len(frac) // 6
ax1.annotate(f"vuelve el {100*frac[i_rec]:.0f} % al modo inicial",
             xy=(tiempos[i_rec], e1[i_rec]),
             xytext=(tiempos[i_rec] * 0.25, e1[i_rec] * 0.72),
             fontsize=8.6, color=C.ink,
             arrowprops=dict(arrowstyle="->", color=C.ink, lw=1.0))

# --- Lo que se esperaba: equipartición -----------------------------------
ax2.bar(modos - 0.2, historial[-1] / e_total[-1], width=0.4, color=C.blue,
        label="al final de la simulación")
ax2.axhline(1 / N, color=C.red, lw=2.0, ls="--",
            label="equipartición esperada")
ax2.set_xlabel("modo"), ax2.set_ylabel("fracción de energía")
ax2.set_title("Lo que se esperaba, y lo que salió")
ax2.legend(fontsize=8)
ax2.set_xlim(0, 12)

print(f"fracción de energía en los 3 primeros modos al final: "
      f"{historial[-1, :3].sum()/e_total[-1]:.3f}")
print(f"recurrencia máxima al modo 1: {100*frac[i_rec]:.1f} % "
      f"en t = {tiempos[i_rec]:.0f}")
print(f"deriva de la energía total: "
      f"{(e_total[-1]-e_total[0])/e_total[0]:.2e}")
save(fig, "fig_fpu")
