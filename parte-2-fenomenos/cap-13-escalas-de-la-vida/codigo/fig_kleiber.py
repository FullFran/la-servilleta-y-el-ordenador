"""¿Por qué no hay mamíferos del tamaño de un edificio?

Ley de Kleiber con datos clásicos, y comparación con los exponentes 2/3 y 3/4.

La figura responde: ¿cuál es el exponente correcto, y qué mecanismo lo explica?

Ejecutar:  python fig_kleiber.py
"""
import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

# Masa (kg) y tasa metabólica basal (W). Valores representativos de la
# literatura clásica (Kleiber 1932; Brody 1945; recopilaciones posteriores).
animales = [
    ("ratón", 0.021, 0.20), ("rata", 0.28, 1.45), ("cobaya", 0.41, 1.9),
    ("conejo", 2.5, 7.5), ("gato", 3.0, 8.6), ("mono", 4.2, 11.4),
    ("perro", 15.5, 30.0), ("cerdo", 128.0, 130.0), ("humano", 70.0, 84.0),
    ("oveja", 46.4, 63.0), ("vaca", 500.0, 380.0), ("caballo", 650.0, 460.0),
    ("elefante", 3670.0, 1800.0),
]
m = np.array([a[1] for a in animales])
P = np.array([a[2] for a in animales])

p = np.polyfit(np.log10(m), np.log10(P), 1)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))

mm = np.logspace(-2, 4, 200)
ax1.loglog(m, P, "o", color=C.red, ms=7)
# Los puntos se apelotonan en el centro: se alterna arriba/abajo para que las
# etiquetas no se pisen.
for i, (nombre, mi, Pi) in enumerate(animales):
    dy = 7 if i % 2 else -11
    ax1.annotate(nombre, (mi, Pi), textcoords="offset points", xytext=(7, dy),
                 fontsize=7.2, color=C.ink)
ax1.loglog(mm, 10**p[1] * mm**p[0], color=C.blue, lw=2.0,
           label=f"ajuste: exponente {p[0]:.3f}")
ax1.loglog(mm, P[0] * (mm / m[0]) ** 0.75, "--", color=C.green, lw=1.6,
           label="3/4 (Kleiber)")
ax1.loglog(mm, P[0] * (mm / m[0]) ** (2 / 3), ":", color=C.ochre, lw=1.6,
           label="2/3 (geométrico)")
ax1.set_xlabel("masa corporal (kg)")
ax1.set_ylabel("tasa metabólica basal (W)")
ax1.set_title("Ley de Kleiber: cinco décadas de masa")
ax1.legend(fontsize=8)

# --- Consecuencias: potencia específica y tiempo de vida ----------------
ax2.loglog(mm, (mm / 1.0) ** (p[0] - 1), color=C.blue, lw=2.2,
           label=r"potencia por kg $\propto M^{-1/4}$")
ax2.loglog(mm, (mm / 1.0) ** 0.25, color=C.red, lw=2.2,
           label=r"tiempos biológicos $\propto M^{1/4}$")
ax2.axhline(1, color=C.grey, ls=":", lw=1.2)
for mi, nombre in [(0.021, "ratón"), (70, "humano"), (3670, "elefante")]:
    ax2.plot(mi, mi**0.25, "o", color=C.ink, ms=5)
    ax2.annotate(nombre, (mi, mi**0.25), textcoords="offset points",
                 xytext=(6, 2), fontsize=7.6)
ax2.set_xlabel("masa corporal (kg)")
ax2.set_ylabel("valor relativo (normalizado a 1 kg)")
ax2.set_title("Por eso el ratón vive deprisa y poco")
ax2.legend(fontsize=8)

print(f"exponente ajustado: {p[0]:.4f} ± "
      f"{np.sqrt(np.sum((np.log10(P)-np.polyval(p,np.log10(m)))**2)/(len(m)-2)/np.sum((np.log10(m)-np.log10(m).mean())**2)):.4f}")
print(f"latidos por vida, ratón vs elefante: relación "
      f"{(3670/0.021)**0.25/(3670/0.021)**0.25:.2f} (constante)")
save(fig, "fig_kleiber")
