"""¿Cómo puede surgir un orden global sin que nadie lo coordine?

Modelo de Ising 2D con Metropolis: magnetización frente a temperatura,
configuraciones típicas y cómo se afila la transición al crecer el sistema.

Dos detalles que no son cosméticos y que costaron la primera versión de esta
figura:

1. El barrido de temperaturas va de CALIENTE A FRÍO, arrastrando la
   configuración anterior. Al revés —empezando en frío desde una configuración
   aleatoria— el sistema se congela en dominios y la magnetización sale próxima
   a cero justo donde debería valer 1. No es física: es falta de equilibrado, y
   es el error más común al simular este modelo.
2. Se mide el promedio de |m| sobre muchos barridos, no el valor instantáneo
   del último. Una sola configuración es una muestra, no una media.

Ejecutar:  python fig_ising.py
"""
import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(1925)

T_C = 2 / np.log(1 + np.sqrt(2))          # 2.269185..., resultado exacto de Onsager


def barrido(s, T, mascara):
    """Un barrido Metropolis en tablero de ajedrez.

    Los vecinos de un sitio negro son todos blancos, así que todos los sitios
    del mismo color se pueden proponer a la vez sin que se pisen. Es Metropolis
    exacto, sólo que vectorizado.
    """
    for color in (0, 1):
        vecinos = (np.roll(s, 1, 0) + np.roll(s, -1, 0) +
                   np.roll(s, 1, 1) + np.roll(s, -1, 1))
        dE = 2.0 * s * vecinos
        acepta = (dE <= 0) | (r.random(s.shape) < np.exp(-dE / T))
        s = np.where((mascara == color) & acepta, -s, s)
    return s


def magnetizacion(L, T, s=None, equilibrio=400, medida=400):
    """|m| promediado tras equilibrar. Devuelve también la configuración final."""
    i, j = np.indices((L, L))
    mascara = (i + j) % 2
    if s is None:
        s = r.choice([-1, 1], size=(L, L)).astype(np.int8)
    for _ in range(equilibrio):
        s = barrido(s, T, mascara)
    acumulado = 0.0
    for _ in range(medida):
        s = barrido(s, T, mascara)
        acumulado += abs(s.mean())
    return acumulado / medida, s


fig = plt.figure(figsize=(11.0, 4.6))
gs = fig.add_gridspec(2, 4, width_ratios=[1.7, 1, 1, 1], wspace=0.34, hspace=0.55)

# --- Panel principal: m(T) para L = 48 -----------------------------------
L = 48
Ts = np.linspace(1.4, 3.6, 26)
M = np.empty_like(Ts)
s = None
for k in range(len(Ts) - 1, -1, -1):          # de caliente a frío
    M[k], s = magnetizacion(L, Ts[k], s)

ax = fig.add_subplot(gs[:, 0])
ax.plot(Ts, M, "o-", color=C.blue, ms=5, lw=1.4, label=f"simulación $L={L}$")
tt = np.linspace(1.4, T_C, 200)
ax.plot(tt, (1 - np.sinh(2 / tt) ** -4) ** (1 / 8), color=C.ink, lw=2.0,
        label=r"Onsager (exacto, $L\to\infty$)")
ax.axvline(T_C, color=C.red, ls="--", lw=1.4)
ax.text(T_C + 0.06, 0.52, f"$T_c$ = {T_C:.3f}", color=C.red, fontsize=9)
ax.set_xlabel("temperatura $T$")
ax.set_ylabel("magnetización $|m|$")
ax.set_title("Orden global sin coordinación", fontsize=10)
ax.set_ylim(-0.03, 1.08)
ax.legend(fontsize=8, loc="lower left")

# --- Tres configuraciones típicas ----------------------------------------
for k, T in enumerate([1.6, T_C, 3.2]):
    _, conf = magnetizacion(L, T, equilibrio=600, medida=1)
    axx = fig.add_subplot(gs[0, 1 + k])
    axx.imshow(conf, cmap="binary", interpolation="nearest")
    axx.set_xticks([]), axx.set_yticks([]), axx.grid(False)
    axx.set_title(f"$T$ = {T:.2f}", fontsize=9)
    axx.set_xlabel(["ordenado", "crítico", "desordenado"][k], fontsize=8,
                   labelpad=3)

# --- Tamaño finito: la transición se afila -------------------------------
axx = fig.add_subplot(gs[1, 1:])
print("  L    T     |m|")
for L_ in (8, 16, 32, 48):
    Ms = np.empty_like(Ts)
    ss = None
    for k in range(len(Ts) - 1, -1, -1):
        Ms[k], ss = magnetizacion(L_, Ts[k], ss, equilibrio=300, medida=300)
    axx.plot(Ts, Ms, lw=1.6, label=f"$L={L_}$")
    print(f"{L_:3d}  {Ts[0]:.2f}  {Ms[0]:.3f}   (a T alta: {Ms[-1]:.3f})")

axx.axvline(T_C, color=C.red, ls="--", lw=1.2)
axx.set_xlabel("temperatura")
axx.set_ylabel("$|m|$")
axx.set_ylim(-0.03, 1.12)
axx.set_title("Cuanto mayor el sistema, más brusca la transición", fontsize=9.5)
axx.legend(fontsize=7.6, ncol=4, loc="lower left")

print(f"\nT_c exacta (Onsager) = {T_C:.6f}")
print(f"|m| simulada a T=1.4 (L=48): {M[0]:.3f}   Onsager: "
      f"{(1 - np.sinh(2 / 1.4) ** -4) ** (1 / 8):.3f}")
save(fig, "fig_ising")
