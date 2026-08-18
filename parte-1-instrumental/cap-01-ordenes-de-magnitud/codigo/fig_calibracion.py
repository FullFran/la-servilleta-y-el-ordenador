"""¿Son honestos tus intervalos de confianza?

Simula tres estimadores con el mismo acierto medio pero distinta honestidad
al declarar su incertidumbre, y dibuja la curva de calibración: qué fracción
de los intervalos del x % contiene realmente el valor verdadero.

La figura responde: ¿cómo se detecta el exceso de confianza sin hacer
psicología, sólo contando?

Ejecutar:  python fig_calibracion.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
aleatorio = rng(2024)

N_PREGUNTAS = 5000
SIGMA_REAL = 0.55        # dispersión real del error, en décadas

# Tres personas: declaran una sigma distinta de la que realmente tienen
PERSONAS = {
    "Exceso de confianza\n(declara $\\sigma/3$)": SIGMA_REAL / 3,
    "Calibrado\n(declara su $\\sigma$)": SIGMA_REAL,
    "Exceso de prudencia\n(declara $2\\sigma$)": SIGMA_REAL * 2,
}
COLORES = [C.red, C.green, C.blue]

errores = aleatorio.normal(0.0, SIGMA_REAL, N_PREGUNTAS)
niveles = np.linspace(0.05, 0.99, 40)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.8, 4.1),
                               gridspec_kw={"width_ratios": [1, 1]})

# --- Curva de calibración -------------------------------------------------
ax1.plot([0, 1], [0, 1], "--", color=C.grey, lw=1.2,
         label="honestidad perfecta")
for (etiqueta, sigma_declarada), color in zip(PERSONAS.items(), COLORES):
    cobertura = [
        np.mean(np.abs(errores) <= norm.ppf(0.5 + p / 2) * sigma_declarada)
        for p in niveles
    ]
    ax1.plot(niveles, cobertura, color=color, lw=2.0, label=etiqueta)
ax1.set_xlabel("nivel declarado del intervalo")
ax1.set_ylabel("fracción que contiene el valor real")
ax1.set_title("Curva de calibración")
ax1.legend(fontsize=8, loc="lower right")
ax1.set_xlim(0, 1), ax1.set_ylim(0, 1)

# --- Lo que se mide en la práctica: 20 estimaciones, intervalo del 90 % ----
n_test = 20
verdad = np.zeros(n_test)
estimado = aleatorio.normal(0.0, SIGMA_REAL, n_test)
sigma_declarada = SIGMA_REAL / 3
medio_ancho = norm.ppf(0.95) * sigma_declarada

dentro = np.abs(estimado - verdad) <= medio_ancho
for i in range(n_test):
    color = C.green if dentro[i] else C.red
    ax2.plot([estimado[i] - medio_ancho, estimado[i] + medio_ancho],
             [i, i], color=color, lw=2.4, alpha=0.85)
    ax2.plot(estimado[i], i, "o", color=color, ms=4)
ax2.axvline(0, color=C.ink, lw=1.6)
ax2.text(0.04, n_test - 0.5, "valor real", color=C.ink, fontsize=8.6)
ax2.set_yticks([])
ax2.set_xlabel("error de la estimación (décadas)")
ax2.set_title(f"Intervalos «del 90 %» de alguien con exceso de confianza:\n"
              f"aciertan {dentro.sum()} de {n_test}", fontsize=10)
ax2.grid(axis="y", alpha=0)

print(f"cobertura real del intervalo declarado al 90 %: {dentro.mean():.0%}")

save(fig, "fig_calibracion")
