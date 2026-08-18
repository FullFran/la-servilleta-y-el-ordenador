"""¿Por qué hay atascos donde no hay obstáculo?

Modelo de seguimiento de vehículos en una vía circular: aparición espontánea de
una onda de parada, y el diagrama fundamental.

La figura responde: ¿qué inestabilidad produce un atasco de la nada?

Ejecutar:  python fig_trafico.py
"""
import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(44)

L, N = 400.0, 30            # circunferencia (m) y número de coches
V0, T_H, S0, A, BB = 25.0, 1.2, 4.0, 1.0, 1.5   # modelo IDM


def idm(x, v):
    orden = np.argsort(x)
    s = np.empty(N)
    dv = np.empty(N)
    for i in range(N):
        j = orden[(np.where(orden == i)[0][0] + 1) % N]
        s[i] = (x[j] - x[i]) % L - S0
        dv[i] = v[i] - v[j]
    s = np.maximum(s, 0.1)
    s_est = S0 + np.maximum(0, v * T_H + v * dv / (2 * np.sqrt(A * BB)))
    return A * (1 - (v / V0) ** 4 - (s_est / (s + S0)) ** 2)


x = np.linspace(0, L, N, endpoint=False) + r.normal(0, 0.3, N)
v = np.full(N, 12.0)
dt, pasos = 0.05, 24_000
hist_x, hist_t = [], []
for k in range(pasos):
    a = idm(x, v)
    v = np.maximum(v + a * dt, 0.0)
    x = (x + v * dt) % L
    if k % 20 == 0:
        hist_x.append(x.copy()), hist_t.append(k * dt)
hist_x = np.array(hist_x); hist_t = np.array(hist_t)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))
for i in range(N):
    ax1.plot(hist_x[:, i], hist_t, ".", color=C.blue, ms=0.35, alpha=0.6)
ax1.set_xlabel("posición en la vía (m)"), ax1.set_ylabel("tiempo (s)")
ax1.set_title("Trayectorias: la onda de parada viaja hacia atrás")
ax1.set_ylim(0, hist_t[-1])
ax1.annotate("aquí nace el atasco\nsin ningún obstáculo",
             xy=(hist_x[len(hist_t) // 3, 0], hist_t[len(hist_t) // 3]),
             xytext=(55, hist_t[-1] * 0.80), fontsize=8.4, color=C.red,
             bbox=dict(facecolor=C.paper, edgecolor="none", alpha=0.85, pad=2),
             arrowprops=dict(arrowstyle="->", color=C.red, lw=1.0))

# --- Diagrama fundamental ------------------------------------------------
densidades = np.linspace(0.008, 0.14, 22)
flujos = []
for dens in densidades:
    n = max(int(dens * L), 2)
    xx = np.linspace(0, L, n, endpoint=False) + r.normal(0, 0.2, n)
    vv = np.full(n, min(V0, 1 / (dens * T_H) if dens > 0 else V0))
    N_g = N
    globals()["N"] = n
    for _ in range(6000):
        aa = idm(xx, vv)
        vv = np.maximum(vv + aa * dt, 0.0)
        xx = (xx + vv * dt) % L
    flujos.append(dens * vv.mean() * 3600)
    globals()["N"] = N_g
ax2.plot(densidades * 1000, flujos, "o-", color=C.blue, ms=5, lw=1.5)
i_max = int(np.argmax(flujos))
ax2.plot(densidades[i_max] * 1000, flujos[i_max], "*", color=C.red, ms=15)
ax2.annotate("capacidad máxima", (densidades[i_max] * 1000, flujos[i_max]),
             textcoords="offset points", xytext=(14, 6), fontsize=8.6,
             color=C.red, ha="left")
ax2.set_xlabel("densidad (vehículos/km)")
ax2.set_ylabel("flujo (vehículos/h)")
ax2.set_title("Diagrama fundamental: más coches, menos flujo")

print(f"capacidad máxima: {flujos[i_max]:.0f} veh/h a "
      f"{densidades[i_max]*1000:.0f} veh/km")
save(fig, "fig_trafico")
