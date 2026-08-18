# Apéndice B — Recetario de Python científico para modeladores

> No es un tutorial. Es la lista de cosas que hacen falta una y otra vez en
> este libro, con la forma correcta de hacerlas.

---

## B.1 Lo mínimo

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate, optimize, signal, stats, linalg

rng = np.random.default_rng(42)      # SIEMPRE con semilla explícita
```

Nada de `np.random.seed()`: el generador global es un estado compartido y
produce resultados que dependen del orden de ejecución.

---

## B.2 Integrar una EDO

```python
from scipy.integrate import solve_ivp

def f(t, y):
    return [y[1], -y[0]]

sol = solve_ivp(f, (0, 10), [1, 0], dense_output=True, rtol=1e-10, atol=1e-12)
t = np.linspace(0, 10, 500)
y = sol.sol(t)
```

**Elección de método:**

| Situación | Método |
|---|---|
| No rígido, general | `RK45` (por defecto) |
| No rígido, alta precisión | `DOP853` |
| **Rígido** | `Radau` o `BDF` |
| Hamiltoniano, tiempos largos | **escribe Verlet a mano** |

**Señal de rigidez:** el paso adaptativo se hace diminuto sin razón aparente.

**Eventos:** `events=` con `terminal=True` para parar en un cruce.

---

## B.3 Ajustar

```python
from scipy.optimize import curve_fit

popt, pcov = curve_fit(modelo, x, y, p0=[1, 1],
                       sigma=sigmas, absolute_sigma=True)
perr = np.sqrt(np.diag(pcov))
rho = pcov[0, 1] / (perr[0] * perr[1])       # correlación: MÍRALA
```

* `absolute_sigma=True` si tus `sigma` son incertidumbres reales.
* **Guarda `pcov` entera**, no sólo la diagonal.
* Ajuste robusto: `least_squares(..., loss='soft_l1')`.
* Después: **dibuja los residuos**.

---

## B.4 Monte Carlo

```python
N = 200_000
x = rng.normal(mu, sigma, N)
y = f(x)
p05, p50, p95 = np.percentile(y, [5, 50, 95])
```

Correlaciones: `rng.multivariate_normal(media, cov, N)`.

Cuasi-aleatorio:

```python
from scipy.stats import qmc
puntos = qmc.Sobol(d=4, scramble=True, seed=1).random(2**12)
```

Hipercubo latino: `qmc.LatinHypercube(d=6, seed=1).random(200)`.

---

## B.5 Señales

```python
f, P = signal.welch(x, fs=1000, nperseg=4096)   # sí
P = np.abs(np.fft.rfft(x))**2                   # no: no converge
```

* Frecuencias: `np.fft.rfftfreq(n, 1/fs)`.
* Ventana: `signal.get_window('hann', n)`.
* Filtro de fase cero: `signal.filtfilt`.
* Espectrograma: `signal.spectrogram`.

---

## B.6 Álgebra lineal

```python
np.linalg.cond(A)              # ANTES de resolver
np.linalg.solve(A, b)          # nunca inv(A) @ b
np.linalg.lstsq(A, b, rcond=None)   # mínimos cuadrados: QR, no normales
U, S, Vt = np.linalg.svd(A, full_matrices=False)
lam, V = np.linalg.eigh(A)     # eigh para simétricas: más rápido y estable
```

Dispersas: `scipy.sparse` y `scipy.sparse.linalg.spsolve` / `cg` / `gmres`.

---

## B.7 Optimización

```python
from scipy.optimize import minimize, differential_evolution

res = minimize(coste, x0, jac=grad, method='BFGS')
res = minimize(coste, x0, method='Nelder-Mead')          # sin gradiente, d<10
res = differential_evolution(coste, bounds)              # global, caro
```

**Siempre**: comprueba tu gradiente analítico contra uno numérico. Debería
coincidir a 6–8 cifras.

---

## B.8 Las cinco comprobaciones de rutina

```python
# 1. Orden de convergencia
print(np.log2(error(h) / error(h/2)))

# 2. Conservación
print(np.ptp(energia), np.polyfit(t, energia, 1)[0])   # banda y deriva secular

# 3. Invariancia de unidades
assert np.allclose(resolver(L=1.0), resolver(L=100.0) / 100.0)

# 4. Caso trivial con solución conocida
assert np.allclose(resolver(caso_trivial), solucion_analitica, rtol=1e-6)

# 5. Independencia de la semilla
resultados = [simular(semilla=s) for s in range(10)]
print(np.mean(resultados), np.std(resultados) / np.sqrt(10))
```

---

## B.9 Higiene

```python
# Cabecera de todo script de figura
"""Qué pregunta responde esta figura.

Ejecutar:  python fig_nombre.py
"""
```

* Un script por figura, con el mismo nombre que la salida.
* Parámetros arriba, en MAYÚSCULAS.
* Semilla explícita.
* Guarda en PDF (para LaTeX) y PNG (para todo lo demás).
* `pip freeze > requirements.txt` con las versiones exactas.

---

## B.10 Cosas que no hacen falta

* **Clases**, salvo que haya estado real que mantener.
* **`if __name__ == "__main__":`** en un script de 20 líneas.
* **argparse**, salvo que sea una herramienta de verdad.
* **Frameworks de configuración**. Un diccionario o un YAML basta.
* **pandas para arrays numéricos.** Es para datos tabulares heterogéneos.
* **Optimizar antes de medir.** `%timeit` primero, y casi siempre el problema
  está en un bucle que se podía vectorizar.
