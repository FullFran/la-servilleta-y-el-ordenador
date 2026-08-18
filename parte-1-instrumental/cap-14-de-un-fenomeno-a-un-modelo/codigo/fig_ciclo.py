"""El ciclo completo del modelador, en un diagrama.

Diagrama conceptual de las quince etapas, con las preguntas asociadas a cada
una y los bucles de realimentación.

La figura responde: ¿en qué orden se hacen las cosas, y dónde se vuelve atrás?

Ejecutar:  python fig_ciclo.py
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, caja, flecha, lienzo, save, use_style  # noqa: E402

use_style()
fig, ax = lienzo(ancho=10.5, alto=6.2, xlim=(0, 14), ylim=(1.6, 10))
ax.set_aspect("auto")

ETAPAS = [
    (2.2, 9.2, "FENÓMENO", "algo que observas", C.ink),
    (2.2, 8.0, "Pregunta", "¿qué quiero saber,\ncon qué precisión?", C.blue),
    (2.2, 6.8, "Orden de magnitud", "¿qué número espero?", C.blue),
    (2.2, 5.6, "Variables", "¿de qué depende?\n¿de qué NO?", C.blue),
    (2.2, 4.4, "Supuestos", "escritos, numerados,\ncon su condición", C.blue),
    (2.2, 3.2, "Modelo mínimo", "lo más simple que\npodría funcionar", C.blue),
    (7.0, 3.2, "Ecuaciones", "y su análisis\nde escalas", C.green),
    (7.0, 4.4, "Solución aproximada", "límites, casos\nextremos", C.green),
    (7.0, 5.6, "Simulación", "predicción escrita\nANTES", C.green),
    (7.0, 6.8, "Validación", "¿contra qué dato?", C.ochre),
    (7.0, 8.0, "Incertidumbre", "¿cuánto me fío?", C.ochre),
    (11.8, 8.0, "Interpretación", "¿qué significa?", C.red),
    (11.8, 6.8, "Límites", "¿dónde deja\nde valer?", C.red),
    (11.8, 5.6, "NUEVA PREGUNTA", "y vuelta a empezar", C.ink),
]

for x, y, titulo, sub, color in ETAPAS:
    destacado = titulo.isupper()
    caja(ax, x, y, 3.5, 0.95,
         f"{titulo}\n{sub}",
         color=color, fontsize=8.2,
         relleno="#f2f5f9" if destacado else "white", lw=2.0 if destacado else 1.3)

# Flujo principal
for i in range(5):
    flecha(ax, (2.2, ETAPAS[i][1] - 0.5), (2.2, ETAPAS[i + 1][1] + 0.5),
           color=C.grey, lw=1.3)
flecha(ax, (3.95, 3.2), (5.25, 3.2), color=C.grey, lw=1.3)
for i in range(6, 10):
    flecha(ax, (7.0, ETAPAS[i][1] + 0.5), (7.0, ETAPAS[i + 1][1] - 0.5),
           color=C.grey, lw=1.3)
flecha(ax, (8.75, 8.0), (10.05, 8.0), color=C.grey, lw=1.3)
flecha(ax, (11.8, 7.5), (11.8, 7.3), color=C.grey, lw=1.3)
flecha(ax, (11.8, 6.3), (11.8, 6.1), color=C.grey, lw=1.3)

# Bucles de realimentación
flecha(ax, (10.05, 5.6), (3.95, 4.4), color=C.red, lw=1.6, rad=-0.25)
ax.text(7.0, 2.05, "si el modelo falla: vuelve a los supuestos, no a las "
        "ecuaciones", fontsize=8.4, color=C.red, ha="center")
flecha(ax, (5.25, 6.8), (3.95, 6.8), color=C.ochre, lw=1.4, rad=0.0,
       texto="¿coincide con\nla estimación?", fontsize=7.6, desplaza=(0, 0.62))

ax.text(0.15, 1.75, "Las tres primeras etapas y las tres últimas distinguen a "
        "un modelador de alguien que sabe resolver ecuaciones.",
        fontsize=9.0, color=C.ink, style="italic")

save(fig, "fig_ciclo")
