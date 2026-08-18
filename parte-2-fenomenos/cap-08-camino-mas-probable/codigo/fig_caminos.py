"""¿Cómo encontramos el camino más probable?

Tres problemas con la misma estructura: refracción (Fermat), camino más corto
en una red (Dijkstra) y trayectoria de mínima acción.

La figura responde: ¿por qué tantos problemas distintos son «minimizar una
integral a lo largo de un camino»?

Ejecutar:  python fig_caminos.py
"""
import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize_scalar

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(88)
fig, axes = plt.subplots(1, 3, figsize=(11.6, 4.0))

# --- 1. Fermat / socorrista ---------------------------------------------
ax = axes[0]
V1, V2 = 5.0, 1.5          # correr y nadar
A, B = np.array([0.0, 4.0]), np.array([10.0, -3.0])


def tiempo(x):
    return (np.hypot(x - A[0], A[1]) / V1 + np.hypot(B[0] - x, B[1]) / V2)


x_opt = minimize_scalar(tiempo, bounds=(0, 10), method="bounded").x
xs = np.linspace(0, 10, 400)
ax.plot(xs, tiempo(xs), color=C.blue, lw=2.0)
ax.plot(x_opt, tiempo(x_opt), "*", color=C.red, ms=15)
ax.axvline(np.interp(0, [A[1], B[1]], [A[0], B[0]]), color=C.grey, ls=":",
           lw=1.2)
ax.text(4.6, tiempo(x_opt) + 0.6, "línea recta", fontsize=8, color=C.grey)
sin1 = (x_opt - A[0]) / np.hypot(x_opt - A[0], A[1])
sin2 = (B[0] - x_opt) / np.hypot(B[0] - x_opt, B[1])
ax.set_xlabel("punto de entrada al agua (m)")
ax.set_ylabel("tiempo total (s)")
ax.set_title(f"Fermat / socorrista\n"
             f"$\\sin\\theta_1/\\sin\\theta_2$ = {sin1/sin2:.3f}, "
             f"$v_1/v_2$ = {V1/V2:.3f}", fontsize=9.5)

# --- 2. Camino más corto en una red ruidosa -----------------------------
ax = axes[1]
n = 26
puntos = r.random((n, 2))
puntos[0] = [0.03, 0.05]
puntos[-1] = [0.97, 0.95]
D = np.hypot(puntos[:, None, 0] - puntos[None, :, 0],
             puntos[:, None, 1] - puntos[None, :, 1])
adj = D < 0.34
np.fill_diagonal(adj, False)

import heapq  # noqa: E402
dist = np.full(n, np.inf); dist[0] = 0
prev = np.full(n, -1)
cola = [(0.0, 0)]
while cola:
    d, u = heapq.heappop(cola)
    if d > dist[u]:
        continue
    for v in np.where(adj[u])[0]:
        nd = d + D[u, v]
        if nd < dist[v]:
            dist[v], prev[v] = nd, u
            heapq.heappush(cola, (nd, int(v)))
camino, k = [n - 1], n - 1
while prev[k] >= 0:
    k = prev[k]; camino.append(k)
camino = camino[::-1]

for i in range(n):
    for j in np.where(adj[i])[0]:
        if j > i:
            ax.plot(*puntos[[i, j]].T, color=C.grey, lw=0.4, alpha=0.5)
ax.plot(*puntos.T, "o", color=C.ink, ms=4)
ax.plot(*puntos[camino].T, "-o", color=C.red, lw=2.2, ms=6)
ax.set_xticks([]), ax.set_yticks([]), ax.grid(False)
ax.set_title(f"Dijkstra: camino más corto\nlongitud = {dist[-1]:.3f}",
             fontsize=9.5)

# --- 3. Acción: la trayectoria real minimiza ----------------------------
ax = axes[2]
T, g = 2.0, 9.81
t = np.linspace(0, T, 200)
y_real = 0.5 * g * t * (T - t)                    # tiro vertical, y(0)=y(T)=0


def accion(alfa):
    y = alfa * y_real
    v = np.gradient(y, t)
    return np.trapezoid(0.5 * v**2 - g * y, t) if hasattr(np, "trapezoid") \
        else np.trapz(0.5 * v**2 - g * y, t)


alfas = np.linspace(0.2, 1.8, 300)
S = np.array([accion(a) for a in alfas])
ax.plot(alfas, S, color=C.blue, lw=2.0)
ax.plot(1.0, accion(1.0), "*", color=C.red, ms=15)
ax.axvline(1.0, color=C.red, ls=":", lw=1.2)
ax.set_xlabel(r"factor de escala de la trayectoria $\alpha$")
ax.set_ylabel("acción $S=\\int(T-V)dt$")
ax.set_title("La trayectoria real es estacionaria\nfrente a deformaciones",
             fontsize=9.5)

print(f"Snell: sin1/sin2 = {sin1/sin2:.4f}, v1/v2 = {V1/V2:.4f}")
print(f"acción mínima en alfa = {alfas[np.argmin(S)]:.4f} (teoría: 1)")
save(fig, "fig_caminos")
