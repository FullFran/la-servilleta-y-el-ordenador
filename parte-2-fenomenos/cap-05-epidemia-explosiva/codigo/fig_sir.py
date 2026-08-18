"""¿Por qué una epidemia puede explotar, y por qué se para sola?

Modelo SIR: curvas para varios R0, el umbral epidémico y la relación de tamaño
final, con la fracción que hay que vacunar.

La figura responde: ¿qué decide si un brote se apaga o despega, y cuánta gente
enferma al final?

Ejecutar:  python fig_sir.py
"""
import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()
GAMMA = 1 / 7.0            # recuperación: 7 días


def sir(t, y, beta):
    s, i, _r = y
    return [-beta * s * i, beta * s * i - GAMMA * i, GAMMA * i]


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))

for R0, color in zip([0.8, 1.3, 2.0, 3.0, 5.0],
                     [C.grey, C.teal, C.green, C.ochre, C.red]):
    sol = solve_ivp(sir, (0, 200), [1 - 1e-4, 1e-4, 0.0], args=(R0 * GAMMA,),
                    dense_output=True, rtol=1e-9)
    t = np.linspace(0, 200, 800)
    ax1.plot(t, sol.sol(t)[1] * 100, color=color, lw=2.0, label=f"$R_0$={R0}")
ax1.set_xlabel("días"), ax1.set_ylabel("% de población infectada")
ax1.set_title("El umbral está en $R_0=1$, y es abrupto")
ax1.legend(fontsize=8.5)

# --- Tamaño final ---------------------------------------------------------
R0s = np.linspace(0.2, 6, 400)
final = []
for R0 in R0s:
    if R0 <= 1:
        final.append(0.0)
    else:
        final.append(brentq(lambda x: x + np.exp(-R0 * x) - 1, 1e-9, 1 - 1e-12))
final = np.array(final)

ax2.plot(R0s, 100 * final, color=C.blue, lw=2.4, label="tamaño final (SIR)")
ax2.plot(R0s[R0s > 1], 100 * (1 - 1 / R0s[R0s > 1]), "--", color=C.red, lw=1.8,
         label="inmunidad de grupo $1-1/R_0$")
ax2.axvline(1, color=C.ink, lw=1.4)
ax2.text(1.08, 5, "umbral epidémico", fontsize=8.6, color=C.ink, rotation=90)
for R0 in (1.5, 2.5, 3.0, 5.0):
    f = brentq(lambda x: x + np.exp(-R0 * x) - 1, 1e-9, 1 - 1e-12)
    ax2.plot(R0, 100 * f, "o", color=C.ink, ms=5)
    print(f"R0={R0}: tamaño final {100*f:.1f} %, umbral de vacunación "
          f"{100*(1-1/R0):.1f} %")
ax2.set_xlabel("$R_0$"), ax2.set_ylabel("% de la población")
ax2.set_title("Tamaño final: siempre mayor que el umbral")
ax2.legend(fontsize=8.5, loc="lower right")
ax2.annotate("la epidemia se pasa\nde frenada (overshoot)",
             xy=(2.5, 100 * brentq(lambda x: x + np.exp(-2.5 * x) - 1, 1e-9, 1 - 1e-12)),
             xytext=(2.9, 42), fontsize=8.4, color=C.blue,
             arrowprops=dict(arrowstyle="->", color=C.blue, lw=1.0))
save(fig, "fig_sir")
