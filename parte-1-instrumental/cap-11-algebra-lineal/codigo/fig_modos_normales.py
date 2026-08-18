"""¿Qué es un autovector, físicamente?

Tres masas unidas por muelles: se calculan los modos normales y se muestra que
cualquier movimiento es una superposición de ellos.

La figura responde: ¿por qué diagonalizar una matriz es elegir el punto de
vista en el que el problema se desacopla?

Ejecutar:  python fig_modos_normales.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

N = 3
K = np.array([[2.0, -1.0, 0.0], [-1.0, 2.0, -1.0], [0.0, -1.0, 2.0]])
w2, V = np.linalg.eigh(K)
w = np.sqrt(w2)

fig, axes = plt.subplots(2, 3, figsize=(11.2, 5.4),
                         gridspec_kw={"hspace": 0.45})

# --- Fila 1: los tres modos ----------------------------------------------
for k in range(N):
    ax = axes[0, k]
    x = np.arange(1, N + 1)
    ax.axhline(0, color=C.grey, lw=1.0)
    for i in range(N):
        ax.plot([x[i], x[i]], [0, V[i, k]], color=C.ink, lw=1.0, alpha=0.5)
    ax.plot(x, V[:, k], "o-", color=[C.blue, C.green, C.red][k], ms=11, lw=2)
    ax.set_ylim(-0.9, 0.9)
    ax.set_xticks(x), ax.set_xticklabels(["$m_1$", "$m_2$", "$m_3$"])
    ax.set_title(f"Modo {k+1}: $\\omega$ = {w[k]:.3f}", fontsize=10)
    if k == 0:
        ax.set_ylabel("amplitud")

# --- Fila 2: una condición inicial arbitraria y su descomposición --------
t = np.linspace(0, 30, 1500)
x0 = np.array([1.0, 0.0, 0.0])          # sólo la primera masa desplazada
coef = V.T @ x0                          # proyección sobre los modos
trayectoria = np.array([sum(coef[k] * np.cos(w[k] * ti) * V[:, k]
                            for k in range(N)) for ti in t])

ax = axes[1, 0]
for i in range(N):
    ax.plot(t, trayectoria[:, i], lw=1.2, label=f"$m_{i+1}$")
ax.set_xlabel("tiempo"), ax.set_ylabel("desplazamiento")
ax.set_title("Movimiento real: complicado", fontsize=10)
ax.legend(fontsize=7.6, ncol=3)

ax = axes[1, 1]
for k in range(N):
    ax.plot(t, coef[k] * np.cos(w[k] * t), lw=1.4,
            color=[C.blue, C.green, C.red][k], label=f"modo {k+1}")
ax.set_xlabel("tiempo"), ax.set_ylabel("amplitud del modo")
ax.set_title("En la base de modos: tres cosenos", fontsize=10)
ax.legend(fontsize=7.6, ncol=3)

ax = axes[1, 2]
ax.bar(np.arange(1, N + 1), coef**2 / (coef**2).sum(),
       color=[C.blue, C.green, C.red], width=0.6)
ax.set_xticks(np.arange(1, N + 1))
ax.set_xlabel("modo"), ax.set_ylabel("fracción de energía")
ax.set_title("Cuánto pesa cada modo", fontsize=10)

print("frecuencias:", np.round(w, 4))
print("coeficientes:", np.round(coef, 4))
save(fig, "fig_modos_normales")
