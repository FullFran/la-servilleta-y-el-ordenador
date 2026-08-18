"""¿Qué forma tiene la incertidumbre de una estimación de Fermi?

Propaga la incertidumbre de los cuatro factores de la tormenta por Monte Carlo
y dibuja la distribución del resultado.

Un detalle que no es cosmético. La primera versión de esta figura sorteaba cada
log-factor de una NORMAL y después el texto presentaba la campana resultante
como si fuera el teorema central del límite en acción. No lo era: una suma de
normales es normal exactamente, para cualquier número de sumandos. La
normalidad estaba metida en los supuestos, no emergía de nada.

Aquí cada factor se sortea de una LAPLACE en el exponente. Se mantiene la misma
convención de siempre —«factor 2,5» sigue significando una desviación típica de
log10(2,5)— pero la forma es picuda y de colas pesadas, con exceso de curtosis
+3, así que no hay ninguna normalidad escondida en los supuestos. Con cuatro
factores la suma todavía NO es normal, y el tercer panel enseña a partir de
cuántos empieza a serlo.

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

# Cada factor: (valor central, factor de incertidumbre a 1 sigma).
# «factor 2,5» significa: creo que está entre valor/2,5 y valor*2,5 con ~68 %
# de confianza. En décadas, sigma = log10(factor).
FACTORES = {
    "Área $A$ (m$^2$)":            (1.0e8, 2.5),
    "Lluvia $h$ (m)":              (2.0e-2, 2.0),
    "Densidad $\\rho$ (kg/m$^3$)": (1.0e3, 1.02),
    "Calor latente $L$ (J/kg)":    (2.26e6, 1.02),
}


def sortea_log_laplace(centro, factor, n):
    """Laplace en el exponente, con la desviación típica pedida.

    Se elige a propósito una forma NO normal: si se sorteara de una normal, la
    suma sería normal exactamente y la campana del resultado no demostraría
    nada. Para Laplace, sigma = b*sqrt(2).
    """
    b = np.log10(factor) / np.sqrt(2.0)
    return np.log10(centro) + aleatorio.laplace(0.0, b, n)


log_total = np.zeros(N)
sigmas = {}
for nombre, (centro, factor) in FACTORES.items():
    sigmas[nombre] = np.log10(factor)
    log_total += sortea_log_laplace(centro, factor, N)

energia = 10**log_total
p05, p50, p95 = np.percentile(energia, [5, 50, 95])

fig = plt.figure(figsize=(12.6, 4.1))
gs = fig.add_gridspec(1, 3, width_ratios=[1.45, 1, 1.15], wspace=0.32)
ax1, ax2, ax3 = (fig.add_subplot(gs[0, i]) for i in range(3))

# --- 1. La distribución del resultado ------------------------------------
ax1.hist(log_total, bins=140, color=C.blue, alpha=0.6, edgecolor="none")
alto = ax1.get_ylim()[1]
ax1.set_ylim(0, alto * 1.30)
for x, etiqueta, color, estilo, altura, ali in [
    (np.log10(p05), f"P5\n{p05:.0e} J", C.grey, "--", 1.04, "center"),
    (np.log10(p50), f"mediana\n{p50:.0e} J", C.ink, "-", 1.22, "center"),
    (np.log10(p95), f"P95\n{p95:.0e} J", C.grey, "--", 1.04, "center"),
]:
    ax1.axvline(x, color=color, lw=1.4, ls=estilo)
    ax1.text(x, alto * altura, etiqueta, ha=ali, va="bottom",
             fontsize=8.2, color=color, linespacing=1.25)

ax1.axvline(np.log10(6.3e13), color=C.red, lw=1.6)
ax1.annotate("Hiroshima", xy=(np.log10(6.3e13), alto * 0.30),
             xytext=(np.log10(6.3e13) - 1.7, alto * 0.55), color=C.red,
             fontsize=8.6,
             arrowprops=dict(arrowstyle="->", color=C.red, lw=1.0))
ax1.set_xlabel("$\\log_{10}$ de la energía liberada (J)")
ax1.set_ylabel("frecuencia")
ax1.set_title("Simétrica en el exponente, no en el valor", fontsize=9.5)
ax1.set_yticks([])

# --- 2. ¿Quién manda en el error? ----------------------------------------
nombres = list(sigmas)
varianzas = np.array([sigmas[n] ** 2 for n in nombres])
contrib = 100 * varianzas / varianzas.sum()
orden = np.argsort(contrib)
colores = [C.red if c > 20 else C.grey for c in contrib[orden]]
ax2.barh([nombres[i] for i in orden], contrib[orden], color=colores, height=0.6)
for i, idx in enumerate(orden):
    ax2.text(contrib[idx] + 1.5, i, f"{contrib[idx]:.0f} %",
             va="center", fontsize=8.6, color=C.ink)
ax2.set_xlabel("contribución a la varianza total (%)")
ax2.set_xlim(0, 100)
ax2.set_title("Mejorar $\\rho$ o $L$ no sirve de nada", fontsize=9.5)
ax2.grid(axis="y", alpha=0)

# --- 3. ¿Cuándo emerge la campana? ---------------------------------------
# Mismo experimento con n factores idénticos, Laplace en el exponente, y la
# varianza total fija: lo único que cambia es EN CUÁNTOS TROZOS se reparte.
SIGMA_TOTAL = 0.35
malla = np.linspace(-4, 4, 400)
gauss = np.exp(-malla**2 / 2) / np.sqrt(2 * np.pi)
for n, color in zip((1, 2, 4, 20), (C.red, C.ochre, C.green, C.blue)):
    b = SIGMA_TOTAL / np.sqrt(2.0 * n)          # var de Laplace(b) = 2b²
    s = aleatorio.laplace(0.0, b, (N, n)).sum(axis=1) / SIGMA_TOTAL
    ax3.hist(s, bins=170, range=(-4, 4), density=True, histtype="step",
             color=color, lw=1.6, label=f"$n={n}$")
ax3.plot(malla, gauss, ":", color=C.ink, lw=1.8, label="normal")
ax3.set_xlim(-3.6, 3.6)
ax3.set_ylim(0, ax3.get_ylim()[1] * 1.34)
ax3.set_xlabel("desviaciones típicas desde el centro")
ax3.set_ylabel("densidad")
ax3.set_title("La campana emerge; con 4 factores aún no está", fontsize=9.5)
ax3.legend(fontsize=7.6, ncol=2, loc="upper right", columnspacing=1.0)
ax3.set_yticks([])

print(f"mediana = {p50:.2e} J   P5 = {p05:.2e} J   P95 = {p95:.2e} J")
print(f"factor entre P5 y P95: {p95/p05:.0f}")
print(f"equivalente en Hiroshimas: {p50/6.3e13:.0f}")
print(f"exceso de curtosis de log E: {float(((log_total-log_total.mean())**4).mean()/log_total.var()**2 - 3):+.3f}"
      "   (0 seria normal exacta)")
save(fig, "fig_tormenta_mc")
