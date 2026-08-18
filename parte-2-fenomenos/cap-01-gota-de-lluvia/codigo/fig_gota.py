"""¿Por qué cae una gota de lluvia como cae?

Velocidad terminal frente al tamaño en los dos regímenes (Stokes y cuadrático),
con datos experimentales clásicos, y la trayectoria temporal adimensionalizada.

La figura responde: ¿por qué la llovizna flota y la lluvia gruesa duele?

Ejecutar:  python fig_gota.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

G, RHO_A, RHO_W, MU = 9.81, 1.20, 1000.0, 1.8e-5

d = np.logspace(-6, -2.3, 400)            # diámetro, m
r = d / 2

v_stokes = 2 * r**2 * (RHO_W - RHO_A) * G / (9 * MU)
CD = 0.5
v_cuad = np.sqrt(8 * r * RHO_W * G / (3 * CD * RHO_A))

# Datos clásicos de velocidad terminal de gotas (Gunn y Kinzer, 1949)
d_gk = np.array([0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.5, 2.0, 2.6, 3.0,
                 4.0, 5.0, 5.8]) * 1e-3
v_gk = np.array([0.27, 0.72, 1.62, 2.47, 3.27, 4.03, 5.65, 6.49, 7.57, 8.06,
                 8.83, 9.09, 9.17])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))

ax1.loglog(d * 1e3, v_stokes, "--", color=C.blue, lw=1.8,
           label=r"Stokes:  $v\propto d^{2}$")
ax1.loglog(d * 1e3, v_cuad, "--", color=C.red, lw=1.8,
           label=r"cuadrático:  $v\propto d^{1/2}$")
ax1.loglog(d_gk * 1e3, v_gk, "o", color=C.ink, ms=6,
           label="datos (Gunn y Kinzer, 1949)")
ax1.set_xlabel("diámetro de la gota (mm)")
ax1.set_ylabel("velocidad terminal (m/s)")
ax1.set_title("Dos regímenes, un cruce")
ax1.legend(fontsize=8, loc="upper left")
ax1.set_ylim(1e-4, 3e1)

# Número de Reynolds y frontera
Re_stokes = RHO_A * v_stokes * d / MU
i_cruce = int(np.argmin(np.abs(Re_stokes - 1)))
ax1.axvline(d[i_cruce] * 1e3, color=C.grey, ls=":", lw=1.4)
ax1.text(d[i_cruce] * 1e3 * 1.25, 3e-3, "$Re=1$", fontsize=8.4, color=C.grey)
print(f"Re=1 en d = {d[i_cruce]*1e6:.0f} micras, v = {v_stokes[i_cruce]*100:.2f} cm/s")

# --- Trayectoria adimensional --------------------------------------------
t = np.linspace(0, 4, 400)
ax2.plot(t, np.tanh(t), color=C.blue, lw=2.4, label=r"$\hat v=\tanh\hat t$")
ax2.axhline(1, color=C.ink, ls="--", lw=1.2)
ax2.axhline(0.99, color=C.grey, ls=":", lw=1.0)
ax2.axvline(2.65, color=C.grey, ls=":", lw=1.0)
ax2.text(2.75, 0.5, "el 99 % de $v_t$\nen $2{,}6\\,\\tau$", fontsize=8.6,
         color=C.ink)
ax2.set_xlabel(r"tiempo adimensional $\hat t=t/(v_t/g)$")
ax2.set_ylabel(r"$v/v_t$")
ax2.set_title("Todas las gotas del universo, una sola curva")
ax2.legend(fontsize=9)

for dd, vt in [(0.2e-3, 0.72), (2e-3, 6.49), (5e-3, 9.09)]:
    tau = vt / G
    print(f"d={dd*1e3:.1f} mm: v_t={vt:.2f} m/s, tau={tau:.3f} s, "
          f"distancia hasta 99% = {tau*vt*np.log(np.cosh(2.65)):.2f} m")
save(fig, "fig_gota")
