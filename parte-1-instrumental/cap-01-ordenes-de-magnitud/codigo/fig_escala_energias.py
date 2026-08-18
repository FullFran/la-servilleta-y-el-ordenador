"""¿Cabe una tormenta en la misma escala que una bomba y que un mosquito?

Escalera logarítmica de energías: 60 órdenes de magnitud en un solo eje.
La figura responde: ¿dónde cae una tormenta de verano en el mapa de las
energías, y qué tiene al lado?

Ejecutar:  python fig_escala_energias.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

# (energía en julios, etiqueta, familia)
ENERGIAS = [
    (1.6e-19, "1 eV · enlace químico débil", "micro"),
    (3.2e-19, "Fotón visible (≈2 eV)", "micro"),
    (3.2e-11, "Fisión de un núcleo de $^{235}$U", "micro"),
    (3.0e-7,  "Mosquito volando", "cotidiano"),
    (1.5e0,   "Manzana cayendo desde 1 m", "cotidiano"),
    (3.6e5,   "Barrita de cereales (≈85 kcal)", "cotidiano"),
    (2.3e6,   "Evaporar 1 L de agua", "cotidiano"),
    (8.6e6,   "Una persona en un día (100 W)", "cotidiano"),
    (4.2e9,   "1 tonelada de TNT", "grande"),
    (5.0e9,   "Un rayo", "grande"),
    (6.3e13,  "Hiroshima (≈15 kt)", "grande"),
    (4.5e15,  "TORMENTA DE VERANO (calor latente)", "destacado"),
    (6.3e16,  "Terremoto de magnitud 8", "grande"),
    (2.1e17,  "Tsar Bomba (50 Mt)", "grande"),
    (5.0e18,  "España: energía primaria en un año", "grande"),
    (5.2e19,  "Huracán, un día (calor latente)", "grande"),
    (1.5e22,  "Luz solar sobre la Tierra en un día", "grande"),
    (3.8e26,  "El Sol durante un segundo", "cosmico"),
    (2.1e29,  "Energía de rotación de la Tierra", "cosmico"),
    (1.0e44,  "Supernova (energía cinética)", "cosmico"),
]

COLORES = {"micro": C.grey, "cotidiano": C.blue, "grande": C.ochre,
           "cosmico": C.purple, "destacado": C.red}

fig, ax = plt.subplots(figsize=(7.4, 8.8))

datos = sorted(ENERGIAS)
y_real = np.array([np.log10(e) for e, _, _ in datos])
lo, hi = y_real.min() - 3, y_real.max() + 3

# --- Colocación de etiquetas sin solape -----------------------------------
# Alternamos columnas y después separamos verticalmente dentro de cada una.
SEPARACION = 2.6          # décadas mínimas entre etiquetas de la misma columna


def separar(ys: np.ndarray, sep: float) -> np.ndarray:
    """Empuja etiquetas hacia arriba hasta respetar la separación mínima."""
    y = ys.astype(float).copy()
    for _ in range(200):
        movido = False
        for i in range(1, len(y)):
            hueco = y[i] - y[i - 1]
            if hueco < sep:
                ajuste = (sep - hueco) / 2
                y[i - 1] -= ajuste
                y[i] += ajuste
                movido = True
        if not movido:
            break
    return y


idx_der = list(range(0, len(datos), 2))
idx_izq = list(range(1, len(datos), 2))
y_etiqueta = np.zeros(len(datos))
y_etiqueta[idx_der] = separar(y_real[idx_der], SEPARACION)
y_etiqueta[idx_izq] = separar(y_real[idx_izq], SEPARACION)

# --- Eje ------------------------------------------------------------------
ax.vlines(0, lo, hi, color=C.ink, lw=1.6, zorder=2)
for d in range(-20, 46, 10):
    if lo < d < hi:
        ax.hlines(d, -0.045, 0.045, color=C.ink, lw=1.1, zorder=3)
        ax.text(-0.062, d, rf"$10^{{{d}}}$", ha="right", va="center",
                fontsize=8, color=C.ink, alpha=0.55)

# --- Puntos y etiquetas ---------------------------------------------------
X_COL = 0.36
for i, (energia, etiqueta, familia) in enumerate(datos):
    y0 = y_real[i]
    y1 = y_etiqueta[i]
    lado = 1 if i in idx_der else -1
    color = COLORES[familia]
    destacado = familia == "destacado"

    # conector en codo: del eje al texto
    ax.plot([0, lado * X_COL * 0.55, lado * X_COL * 0.92],
            [y0, y1, y1], color=color, lw=0.9, alpha=0.7, zorder=2)
    ax.plot(0, y0, "o", color=color, ms=8 if destacado else 5,
            mec=C.paper, mew=0.8, zorder=5)
    ax.text(lado * X_COL, y1, etiqueta,
            ha="left" if lado > 0 else "right", va="center",
            fontsize=9.2 if destacado else 8.4, color=color,
            weight="bold" if destacado else "normal")

# --- La comparación que da título al capítulo -----------------------------
y_h, y_t = np.log10(6.3e13), np.log10(4.5e15)
ax.annotate("", xy=(0.05, y_t), xytext=(0.05, y_h),
            arrowprops=dict(arrowstyle="<->", color=C.red, lw=1.4))
ax.text(0.078, (y_h + y_t) / 2 + 0.35, "1,9 décadas\n≈ factor 70",
        color=C.red, fontsize=8.4, va="center", ha="left", linespacing=1.3,
        bbox=dict(facecolor=C.paper, edgecolor="none", pad=1.5))

ax.set_xlim(-1.05, 1.05)
ax.set_ylim(lo, hi)
ax.axis("off")
ax.set_title("Energía en julios. Cada marca del eje es un factor $10^{10}$",
             fontsize=10, pad=14)

save(fig, "fig_escala_energias")
