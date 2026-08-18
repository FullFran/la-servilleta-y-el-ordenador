"""SVD: la descomposición que explica compresión, ajuste y PCA a la vez.

Se aplica a una imagen sintética: espectro de valores singulares y
reconstrucciones con distintos rangos.

La figura responde: ¿cuánta información hay realmente en una matriz?

Ejecutar:  python fig_svd.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(11)

n = 200
y, x = np.mgrid[0:n, 0:n] / n
imagen = (np.sin(6 * np.pi * x) * np.cos(4 * np.pi * y)
          + 1.5 * np.exp(-((x - 0.3)**2 + (y - 0.7)**2) / 0.02)
          + 0.8 * (np.abs(x - y) < 0.05)
          + 0.05 * r.standard_normal((n, n)))

U, S, Vt = np.linalg.svd(imagen, full_matrices=False)

fig = plt.figure(figsize=(11.2, 5.0))
gs = fig.add_gridspec(2, 4, width_ratios=[1.3, 1, 1, 1], wspace=0.3, hspace=0.35)

ax = fig.add_subplot(gs[:, 0])
ax.semilogy(S, "o-", color=C.blue, ms=3, lw=1.0)
ax.set_xlabel("índice $k$"), ax.set_ylabel("valor singular $\\sigma_k$")
ax.set_title("Espectro de valores singulares")
ax.axhline(S[0] * 1e-2, color=C.grey, ls="--", lw=1.0)
ax.text(60, S[0] * 1.3e-2, "1 % del mayor", fontsize=8, color=C.grey)
ax.set_xlim(0, 200)

RANGOS = [1, 5, 20, 200]
for j, k in enumerate(RANGOS):
    ax = fig.add_subplot(gs[j // 2, 1 + (j % 2)])
    aprox = (U[:, :k] * S[:k]) @ Vt[:k]
    ax.imshow(aprox, cmap="gray", interpolation="nearest")
    ax.set_xticks([]), ax.set_yticks([]), ax.grid(False)
    guardado = 100 * (1 - k * (2 * n + 1) / n**2)
    ax.set_title(f"rango {k}  ({guardado:.0f} % menos datos)"
                 if k < n else "original (rango completo)", fontsize=9)

ax = fig.add_subplot(gs[0, 3])
energia = np.cumsum(S**2) / np.sum(S**2)
ax.plot(np.arange(1, len(S) + 1), energia, color=C.red, lw=1.8)
ax.axhline(0.99, color=C.grey, ls="--", lw=1.0)
k99 = int(np.searchsorted(energia, 0.99) + 1)
ax.axvline(k99, color=C.grey, ls="--", lw=1.0)
ax.text(k99 + 4, 0.5, f"99 % con\nrango {k99}", fontsize=8, color=C.ink)
ax.set_xlabel("rango $k$"), ax.set_ylabel("energía acumulada")
ax.set_title("Cuánto captura cada rango", fontsize=9)
ax.set_xlim(0, 120)

print(f"rango 99 % de energía: {k99} de {n}")
print(f"sigma_1/sigma_200 = {S[0]/S[-1]:.1f}  (número de condición)")
save(fig, "fig_svd")
