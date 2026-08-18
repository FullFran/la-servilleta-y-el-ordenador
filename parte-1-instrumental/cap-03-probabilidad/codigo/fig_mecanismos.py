"""¿De dónde sale cada distribución?

Seis mecanismos generadores simulados desde cero, cada uno con su histograma y
la ley teórica superpuesta. La figura responde: no «cuál es la fórmula», sino
«qué proceso físico produce esta forma».

Ejecutar:  python fig_mecanismos.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, rng, save, use_style  # noqa: E402

use_style()
r = rng(3)
N = 200_000

fig, axes = plt.subplots(2, 3, figsize=(10.8, 6.0))

# --- 1. Binomial: contar éxitos en n intentos independientes --------------
ax = axes[0, 0]
n, p = 20, 0.3
x = r.binomial(n, p, N)
bins = np.arange(-0.5, n + 1.5)
ax.hist(x, bins=bins, density=True, color=C.blue, alpha=0.6, edgecolor="none")
k = np.arange(0, n + 1)
ax.plot(k, stats.binom.pmf(k, n, p), "o", color=C.ink, ms=3.5)
ax.set_title("Binomial\n«cuento éxitos en $n$ intentos»", fontsize=9.5)

# --- 2. Poisson: muchos intentos, cada uno improbable --------------------
ax = axes[0, 1]
n_grande, p_pequena = 10_000, 3e-4      # n*p = 3
x = r.binomial(n_grande, p_pequena, N)
bins = np.arange(-0.5, 15.5)
ax.hist(x, bins=bins, density=True, color=C.blue, alpha=0.6, edgecolor="none")
k = np.arange(0, 15)
ax.plot(k, stats.poisson.pmf(k, 3.0), "o", color=C.ink, ms=3.5)
ax.set_title("Poisson\n«$n\\to\\infty$, $p\\to0$, con $np$ fijo»", fontsize=9.5)

# --- 3. Exponencial: tiempo hasta el primer suceso -----------------------
ax = axes[0, 2]
# Simulamos ensayos discretos y contamos cuántos hasta el primer éxito
p_exito = 1e-3
x = r.geometric(p_exito, N) * p_exito      # reescalado -> exponencial(1)
ax.hist(x, bins=120, density=True, color=C.blue, alpha=0.6, edgecolor="none",
        range=(0, 6))
t = np.linspace(0, 6, 200)
ax.plot(t, np.exp(-t), color=C.ink, lw=1.6)
ax.set_title("Exponencial\n«cuánto espero hasta el primero»", fontsize=9.5)

# --- 4. Normal: suma de muchas contribuciones ----------------------------
ax = axes[1, 0]
n_sumandos = 40
x = r.uniform(-1, 1, size=(N, n_sumandos)).sum(axis=1)
x /= x.std()
ax.hist(x, bins=140, density=True, color=C.blue, alpha=0.6, edgecolor="none")
z = np.linspace(-4.5, 4.5, 200)
ax.plot(z, stats.norm.pdf(z), color=C.ink, lw=1.6)
ax.set_title("Normal\n«sumo 40 cosas cualesquiera»", fontsize=9.5)

# --- 5. Log-normal: producto de muchos factores --------------------------
ax = axes[1, 1]
x = np.exp(r.normal(0, 0.15, size=(N, 20)).sum(axis=1))
ax.hist(x, bins=160, density=True, color=C.blue, alpha=0.6, edgecolor="none",
        range=(0, 8))
v = np.linspace(0.01, 8, 300)
ax.plot(v, stats.lognorm.pdf(v, s=0.15 * np.sqrt(20)), color=C.ink, lw=1.6)
ax.set_title("Log-normal\n«multiplico 20 factores»", fontsize=9.5)

# --- 6. Ley de potencias: crecimiento proporcional -----------------------
ax = axes[1, 2]
# Modelo de Yule: los ricos se hacen más ricos
tamanos = np.ones(1, dtype=float)
for _ in range(20_000):
    if r.random() < 0.15:
        tamanos = np.append(tamanos, 1.0)
    else:
        idx = r.choice(len(tamanos), p=tamanos / tamanos.sum())
        tamanos[idx] += 1
b = np.logspace(0, np.log10(tamanos.max() + 1), 30)
h, _ = np.histogram(tamanos, bins=b, density=True)
centros = np.sqrt(b[1:] * b[:-1])
bueno = h > 0
ax.loglog(centros[bueno], h[bueno], "o", color=C.blue, ms=4)
ax.loglog(centros[bueno], 0.6 * centros[bueno] ** -2.2, color=C.ink, lw=1.6)
ax.set_title("Ley de potencias\n«el que más tiene, más recibe»", fontsize=9.5)

for ax in axes.ravel():
    ax.set_yticks([])
    ax.tick_params(labelsize=8)

fig.suptitle("Cada distribución es la huella de un mecanismo, no una fórmula",
             fontsize=11.5, y=1.0)
save(fig, "fig_mecanismos")
