"""¿Cuántas cuentas hacen falta para poder decir «hemos detectado algo»?

Dibuja la significancia s/sqrt(b) frente al tiempo de medida para varias
relaciones señal/fondo, y el mínimo tiempo necesario para llegar a 5 sigma.

La figura responde: ¿por qué medir el doble de tiempo no duplica la
significancia?

Ejecutar:  python fig_deteccion_fondo.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()

TASA_FONDO = 100.0                       # cuentas por hora
COCIENTES = [0.30, 0.10, 0.03, 0.01]     # tasa de señal / tasa de fondo
t = np.logspace(-1, 4, 400)              # horas

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.2, 4.1))

for cociente, color in zip(COCIENTES, [C.blue, C.green, C.ochre, C.red]):
    s = cociente * TASA_FONDO * t
    b = TASA_FONDO * t
    significancia = s / np.sqrt(b)
    ax1.loglog(t, significancia, color=color, lw=1.9,
               label=f"$s/b$ = {cociente:.2f}")
    t5 = 25 / (cociente**2 * TASA_FONDO)
    ax1.plot(t5, 5, "o", color=color, ms=6)

ax1.axhline(5, color=C.ink, ls="--", lw=1.2)
ax1.text(0.12, 5.5, "umbral de descubrimiento, 5$\\sigma$", fontsize=8.4,
         color=C.ink)
ax1.axhline(3, color=C.grey, ls=":", lw=1.0)
ax1.text(0.12, 3.1, "«indicio», 3$\\sigma$", fontsize=8, color=C.grey)
ax1.set_xlabel("tiempo de medida (h)")
ax1.set_ylabel(r"significancia $s/\sqrt{b}$")
ax1.set_title(r"La significancia crece como $\sqrt{t}$")
ax1.legend(fontsize=8, loc="lower right")

# --- Coste: horas necesarias para 5 sigma --------------------------------
cocientes = np.logspace(-3, 0, 200)
horas = 25 / (cocientes**2 * TASA_FONDO)
ax2.loglog(cocientes, horas, color=C.red, lw=2.0)
for c, etiqueta in [(0.3, "señal fuerte"), (0.03, "señal débil"),
                    (0.003, "señal muy débil")]:
    h = 25 / (c**2 * TASA_FONDO)
    ax2.plot(c, h, "o", color=C.ink, ms=5)
    txt = f"{h:.0f} h" if h < 8760 else f"{h/8760:.0f} años"
    ax2.annotate(f"{etiqueta}\n{txt}", (c, h), textcoords="offset points",
                 xytext=(-6, 8), fontsize=8, ha="right")
ax2.set_xlabel("cociente señal/fondo  $s/b$")
ax2.set_ylabel("horas de medida para 5$\\sigma$")
ax2.set_title("Dividir la señal por 10 multiplica el tiempo por 100")

save(fig, "fig_deteccion_fondo")
