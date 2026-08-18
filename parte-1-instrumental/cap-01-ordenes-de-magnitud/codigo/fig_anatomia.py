"""¿Cómo se descompone un problema imposible en cinco problemas fáciles?

Diagrama de la anatomía de una estimación de Fermi, con el ejemplo de la
energía de una tormenta. Responde: ¿qué se hace exactamente cuando alguien
dice «descomponer el problema»?

Ejecutar:  python fig_anatomia.py
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, caja, flecha, lienzo, save, use_style  # noqa: E402

use_style()
fig, ax = lienzo(ancho=9.2, alto=5.4, xlim=(0, 12), ylim=(0, 7))
ax.set_aspect("auto")

# --- Pregunta imposible ---------------------------------------------------
caja(ax, 6, 6.3, 7.4, 0.9,
     "¿Cuánta energía libera una tormenta de verano?",
     color=C.ink, relleno="white", fontsize=10.5)

# --- Los factores ---------------------------------------------------------
FACTORES = [
    ("Área\nde la célula", "$A \\sim 10\\times10$ km\n$=10^{8}$ m$^2$", C.blue),
    ("Lluvia\ncaída", "$h \\sim 20$ mm\n$=2\\times10^{-2}$ m", C.blue),
    ("Densidad\ndel agua", "$\\rho = 10^{3}$\nkg/m$^3$", C.green),
    ("Calor latente\nde condensación", "$L = 2{,}3\\times10^{6}$\nJ/kg", C.green),
]
x0, dx = 1.7, 2.9
for i, (titulo, valor, color) in enumerate(FACTORES):
    x = x0 + i * dx
    caja(ax, x, 4.3, 2.5, 1.5, f"{titulo}\n\n{valor}", color=color, fontsize=8.6)
    flecha(ax, (6, 5.85), (x, 5.05), color=C.grey, rad=0.0, lw=1.0)

ax.text(0.35, 4.3, "1. Descomponer", fontsize=9, color=C.ink,
        rotation=90, va="center", ha="center", weight="bold")

# --- Combinación ----------------------------------------------------------
caja(ax, 6, 2.5, 8.4, 1.0,
     "$E \\;=\\; A \\cdot h \\cdot \\rho \\cdot L \\;=\\; "
     "10^{8}\\cdot 2\\!\\times\\!10^{-2}\\cdot 10^{3}\\cdot 2{,}3\\!\\times\\!10^{6}"
     "\\;\\approx\\; 5\\times10^{15}\\ \\mathrm{J}$",
     color=C.red, relleno="#fdf3f2", fontsize=10.5)
for i in range(4):
    flecha(ax, (x0 + i * dx, 3.55), (6, 3.05), color=C.grey, lw=1.0)
ax.text(0.35, 2.5, "2. Multiplicar", fontsize=9, color=C.ink,
        rotation=90, va="center", ha="center", weight="bold")

# --- Contraste ------------------------------------------------------------
caja(ax, 3.1, 0.8, 4.4, 1.0,
     "¿Contra qué lo comparo?\n70 bombas de Hiroshima", color=C.ochre, fontsize=9)
caja(ax, 8.6, 0.8, 4.4, 1.0,
     "¿Dónde está mi error?\nen $h$ y en $A$, no en $\\rho$ ni en $L$",
     color=C.purple, fontsize=9)
flecha(ax, (6, 1.95), (3.1, 1.35), color=C.grey, lw=1.0)
flecha(ax, (6, 1.95), (8.6, 1.35), color=C.grey, lw=1.0)
ax.text(0.35, 0.8, "3. Criticar", fontsize=9, color=C.ink,
        rotation=90, va="center", ha="center", weight="bold")

save(fig, "fig_anatomia")
