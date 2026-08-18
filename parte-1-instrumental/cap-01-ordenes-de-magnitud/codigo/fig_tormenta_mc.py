"""¿Qué forma tiene la incertidumbre de una estimación de Fermi?

Propaga la incertidumbre de los cuatro factores de la tormenta por Monte
Carlo y dibuja la distribución del resultado. La figura responde: si no sé
los factores con exactitud, ¿qué intervalo puedo defender para la energía?

Ejecutar:  python fig_tormenta_mc.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
aleatorio = rng(1945)
N = 200_000

# Cada factor: (valor central, factor de incertidumbre a 1 sigma)
# «factor 2» significa: creo que está entre valor/2 y valor*2 con ~68 % de
# confianza. En décadas, sigma = log10(factor).
FACTORES = {
    "Área $A$ (m$^2$)":            (1.0e8, 2.5),
    "Lluvia $h$ (m)":              (2.0e-2, 2.0),
    "Densidad $\\rho$ (kg/m$^3$)": (1.0e3, 1.02),
    "Calor latente $L$ (J/kg)":    (2.26e6, 1.02),
}

log_total = np.zeros(N)
sigmas = {}
for nombre, (centro, factor) in FACTORES.items():
    sigma = np.log10(factor)
    sigmas[nombre] = sigma
    log_total += np.log10(centro) + aleatorio.normal(0.0, sigma, N)

energia = 10**log_total
p05, p50, p95 = np.percentile(energia, [5, 50, 95])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.0, 4.1),
                               gridspec_kw={"width_ratios": [1.5, 1]})

# --- Distribución ---------------------------------------------------------
ax1.hist(log_total, bins=140, color=C.blue, alpha=0.6, edgecolor="none")
alto = ax1.get_ylim()[1]
ax1.set_ylim(0, alto * 1.30)
etiquetas = [
    (np.log10(p05), f"P5\n{p05:.0e} J", C.grey, "--", 1.06, "right"),
    (np.log10(p50), f"mediana\n{p50:.0e} J", C.ink, "-", 1.22, "center"),
    (np.log10(p95), f"P95\n{p95:.0e} J", C.grey, "--", 1.06, "left"),
]
for x, etiqueta, color, estilo, altura, ali in etiquetas:
    ax1.axvline(x, color=color, lw=1.4, ls=estilo)
    ax1.text(x, alto * altura, etiqueta, ha=ali, va="bottom",
             fontsize=8.2, color=color, linespacing=1.25)

ax1.axvline(np.log10(6.3e13), color=C.red, lw=1.6)
ax1.annotate("Hiroshima", xy=(np.log10(6.3e13), alto * 0.45),
             xytext=(np.log10(6.3e13) - 1.6, alto * 0.72), color=C.red,
             fontsize=8.6,
             arrowprops=dict(arrowstyle="->", color=C.red, lw=1.0))

ax1.set_xlabel("$\\log_{10}$ de la energía liberada (J)")
ax1.set_ylabel("frecuencia")
ax1.set_title("La incertidumbre es log-normal, no normal")
ax1.set_yticks([])

# --- ¿Quién manda en el error? -------------------------------------------
nombres = list(sigmas)
varianzas = np.array([sigmas[n] ** 2 for n in nombres])
contrib = 100 * varianzas / varianzas.sum()
orden = np.argsort(contrib)
colores = [C.red if c > 20 else C.grey for c in contrib[orden]]
ax2.barh([nombres[i] for i in orden], contrib[orden], color=colores, height=0.6)
for i, (idx) in enumerate(orden):
    ax2.text(contrib[idx] + 1.5, i, f"{contrib[idx]:.0f} %",
             va="center", fontsize=8.6, color=C.ink)
ax2.set_xlabel("contribución a la varianza total (%)")
ax2.set_xlim(0, 100)
ax2.set_title("Mejorar $\\rho$ o $L$ no sirve de nada")
ax2.grid(axis="y", alpha=0)

print(f"mediana = {p50:.2e} J   P5 = {p05:.2e} J   P95 = {p95:.2e} J")
print(f"factor entre P5 y P95: {p95/p05:.0f}")
print(f"equivalente en Hiroshimas: {p50/6.3e13:.0f}")

save(fig, "fig_tormenta_mc")
