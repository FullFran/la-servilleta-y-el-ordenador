"""¿Cuánto se gana usando la curvatura y no sólo la pendiente?

Convergencia de descenso por gradiente, gradiente con momento, BFGS y Newton
sobre la función de Rosenbrock.

La figura responde: ¿por qué la segunda derivada compensa su coste?

Ejecutar:  python fig_gradiente_newton.py
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
from estilo_libro import C, save, use_style  # noqa: E402

use_style()


def rosenbrock(v):
    x, y = v
    return (1 - x) ** 2 + 100 * (y - x**2) ** 2


def grad(v):
    x, y = v
    return np.array([-2 * (1 - x) - 400 * x * (y - x**2), 200 * (y - x**2)])


def hess(v):
    x, y = v
    return np.array([[2 - 400 * (y - 3 * x**2), -400 * x], [-400 * x, 200]])


X0 = np.array([-1.2, 1.0])
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))

# --- Paisaje y trayectorias ---------------------------------------------
X, Y = np.meshgrid(np.linspace(-1.6, 1.6, 400), np.linspace(-0.6, 1.8, 400))
Z = (1 - X) ** 2 + 100 * (Y - X**2) ** 2
ax1.contour(X, Y, Z, levels=np.logspace(-0.5, 3.5, 22), colors=[C.grey],
            linewidths=0.5, alpha=0.7)
ax1.plot(1, 1, "*", color=C.ink, ms=14, zorder=6)
ax1.grid(False)

def newton_amortiguado(x0, n=60):
    """Newton con búsqueda de línea por retroceso: 12 líneas."""
    x = np.array(x0, dtype=float)
    camino = [x.copy()]
    for _ in range(n):
        g = grad(x)
        if np.linalg.norm(g) < 1e-12:
            break
        d = np.linalg.solve(hess(x), -g)
        if d @ g > 0:                    # dirección no descendente
            d = -g
        alfa = 1.0
        while rosenbrock(x + alfa * d) > rosenbrock(x) + 1e-4 * alfa * (g @ d):
            alfa *= 0.5
            if alfa < 1e-12:
                break
        x = x + alfa * d
        camino.append(x.copy())
    return camino


historiales = {}
for nombre, metodo, color, kw in [
        ("Gradiente (paso fijo)", None, C.red, {}),
        ("BFGS (cuasi-Newton)", "BFGS", C.blue, {"jac": grad}),
        ("Newton con línea", "propio", C.green, {})]:
    camino = [X0.copy()]
    if metodo is None:
        x = X0.copy()
        for _ in range(20_000):
            x = x - 1.5e-3 * grad(x)
            camino.append(x.copy())
    elif metodo == "propio":
        camino = newton_amortiguado(X0)
    else:
        minimize(rosenbrock, X0, method=metodo,
                 callback=lambda xk: camino.append(np.array(xk)), **kw)
    camino = np.array(camino)
    historiales[nombre] = (camino, color)
    paso = max(len(camino) // 400, 1)
    ax1.plot(camino[::paso, 0], camino[::paso, 1], "-", color=color, lw=1.4,
             label=f"{nombre} ({len(camino)-1} pasos)")

ax1.plot(*X0, "o", color=C.ink, ms=6)
ax1.set_xlabel("$x$"), ax1.set_ylabel("$y$")
ax1.set_title("Función de Rosenbrock: el valle del plátano")
ax1.legend(fontsize=7.6, loc="upper left")

# --- Convergencia --------------------------------------------------------
for nombre, (camino, color) in historiales.items():
    err = np.linalg.norm(camino - np.array([1.0, 1.0]), axis=1)
    ax2.semilogy(np.maximum(err, 1e-16), color=color, lw=1.6, label=nombre)
    print(f"{nombre:24s} pasos = {len(camino)-1:6d}   error final = {err[-1]:.2e}")
ax2.set_xlabel("iteración"), ax2.set_ylabel("distancia al mínimo")
ax2.set_title("Lineal, superlineal, cuadrática")
ax2.set_xlim(0, 120), ax2.set_ylim(1e-16, 5)
ax2.legend(fontsize=8)

save(fig, "fig_gradiente_newton")
