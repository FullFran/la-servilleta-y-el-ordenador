"""Das positivo en un test con 99 % de acierto. ¿Estás enfermo?

Representa 10 000 personas como puntos y colorea los cuatro cuadrantes de la
tabla de contingencia. La figura responde: ¿por qué el resultado depende
tantísimo de la prevalencia, y no sólo de la calidad del test?

Ejecutar:  python fig_bayes_frecuencias.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

N = 10_000
SENSIBILIDAD = 0.99      # P(+ | enfermo)
ESPECIFICIDAD = 0.99     # P(- | sano)
PREVALENCIAS = [0.001, 0.01, 0.10]

fig, axes = plt.subplots(1, 3, figsize=(10.6, 4.0))

for ax, prev in zip(axes, PREVALENCIAS):
    enfermos = int(N * prev)
    vp = int(enfermos * SENSIBILIDAD)              # verdaderos positivos
    fn = enfermos - vp
    fp = int((N - enfermos) * (1 - ESPECIFICIDAD))  # falsos positivos
    vn = N - enfermos - fp

    # Mosaico de 100 x 100 puntos
    lado = 100
    rejilla = np.zeros(lado * lado, dtype=int)
    rejilla[:vp] = 3
    rejilla[vp:vp + fn] = 2
    rejilla[vp + fn:vp + fn + fp] = 1
    rejilla = rejilla.reshape(lado, lado)

    colores = np.array([C.light, C.ochre, C.grey, C.red])
    from matplotlib.colors import ListedColormap
    ax.imshow(rejilla, cmap=ListedColormap(colores), interpolation="nearest",
              origin="lower")
    ax.set_xticks([]), ax.set_yticks([])
    ax.grid(False)
    vpp = vp / (vp + fp) if vp + fp else 0
    ax.set_title(f"prevalencia {prev:.1%}\n"
                 f"P(enfermo | +) = {vpp:.0%}", fontsize=10)
    ax.text(2, 96, f"VP {vp}   FP {fp}", fontsize=8, color=C.ink, va="top")

# Leyenda común
from matplotlib.patches import Patch  # noqa: E402
fig.legend(handles=[
    Patch(color=C.red, label="enfermo y positivo (VP)"),
    Patch(color=C.ochre, label="sano y positivo (FP)"),
    Patch(color=C.grey, label="enfermo y negativo (FN)"),
    Patch(color=C.light, label="sano y negativo (VN)"),
], loc="lower center", ncol=4, fontsize=8.5, frameon=False,
    bbox_to_anchor=(0.5, -0.04))
fig.suptitle("El mismo test, tres poblaciones: 10 000 personas por panel",
             fontsize=11, y=1.0)
fig.subplots_adjust(bottom=0.14)

for prev in PREVALENCIAS:
    e = int(N * prev); vp = int(e * SENSIBILIDAD)
    fp = int((N - e) * (1 - ESPECIFICIDAD))
    print(f"prevalencia {prev:.3%}: P(enf|+) = {vp/(vp+fp):.1%}")

save(fig, "fig_bayes_frecuencias")
