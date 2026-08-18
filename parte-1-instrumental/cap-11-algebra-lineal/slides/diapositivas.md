---
title: "Álgebra lineal"
subtitle: "Capítulo 11 · El lenguaje de los modelos"
author: "La servilleta y el ordenador"
date: "Parte I — El instrumental del modelador"
---

# La pregunta

Dos ecuaciones, dos incógnitas. Los datos con un 1 % de error.

\vspace{1em}
\Large
**¿Con qué error conocerás la solución?**

\normalsize
\vspace{1em}

Respuesta correcta: depende de la matriz. Y puede ser un 1000 %.

# La traducción

| Objeto | En un modelo |
|---|---|
| Vector $\mathbf{x}$ | el **estado** |
| Matriz $A$ | una **regla** |
| $A\mathbf{x}=\mathbf{b}$ | ¿qué estado produce esta observación? |
| Autovector | dirección que la regla **no mezcla** |
| Autovalor | cuánto la estira |

\vspace{0.8em}

\alert{Casi todo problema lineal es trivial en la base correcta. Toda la
técnica consiste en encontrarla.}

# Autovectores = modos naturales

\centering
![](../figuras/fig_modos_normales.pdf){width=100%}

\raggedright\small
Izquierda abajo: un lío. Centro: **tres cosenos**. Es el mismo movimiento, otro
sistema de coordenadas.

# Y reaparece en todas partes

* Sistema dinámico: tasas y frecuencias (cap. 7)
* Cadena de Markov: distribución estacionaria y velocidad de mezcla (cap. 9)
* Molécula: modos de vibración y espectro infrarrojo
* Red: comunidades vía el laplaciano
* **Fourier: las exponenciales son los autovectores de la derivada**

\vspace{0.8em}

\alert{Fourier es un caso particular de diagonalización.}

# SVD: rotar, estirar, rotar

$$A = U\Sigma V^{T}$$

\centering
![](../figuras/fig_svd.pdf){width=95%}

# Cinco cosas que son la misma

* **Rango efectivo** — cuántos $\sigma_k$ superan el ruido
* **Mejor aproximación de rango $k$** — Eckart–Young
* **PCA** — la SVD de los datos centrados
* **Mínimos cuadrados estables** — pseudoinversa, no ecuaciones normales
* **Número de condición** — $\sigma_{\max}/\sigma_{\min}$

# Condicionamiento

$$\frac{\|\delta \mathbf{x}\|}{\|\mathbf{x}\|}\le\kappa(A)\,
\frac{\|\delta \mathbf{b}\|}{\|\mathbf{b}\|}$$

\centering
![](../figuras/fig_condicionamiento.pdf){width=88%}

\raggedright\small
$\kappa=1{,}5$ vs $\kappa=1999$: la misma perturbación, dispersión 1300 veces
mayor.

# La regla que hay que recordar

$$\text{cifras perdidas} \approx \log_{10}\kappa(A)$$

\vspace{0.8em}

Doble precisión: 16 cifras. $\kappa=10^{12}$ $\to$ te quedan 4.

\vspace{1em}

`np.linalg.cond(A)` antes de resolver. Es una línea.

\vspace{0.8em}

\alert{Y buena parte del mal condicionamiento es culpa de las unidades.
Adimensionalizar **es** precondicionar.}

# El fallo que los autovalores no ven

\centering
![](../figuras/fig_no_normal.pdf){width=100%}

\raggedright\small
Autovalores $-1$ y $-2$, ambos estables. Amplificación transitoria: **×50**.

# Y no es una patología de laboratorio

Flujo de Poiseuille: el análisis lineal predice estabilidad hasta
$Re\approx5772$. El experimento da turbulencia hacia $Re\approx2000$.

\vspace{0.8em}

Trefethen et al., *Science* 1993: el operador es fuertemente **no normal**.
Las perturbaciones crecen por factores de $10^3$ antes de que las no
linealidades manden.

\vspace{0.8em}

\alert{Una herramienta estándar respondiendo a la pregunta equivocada durante
cien años.}

# Errores que se cometen todos los días

* **Ecuaciones normales**: $\kappa(A^TA)=\kappa(A)^2$. Usa QR o SVD
* **`inv(A) @ b`**: más lento y menos preciso que `solve`
* **Análisis modal con matrices no normales**
* **PCA sin estandarizar**: maximiza varianza *en tus unidades*
* **Truncar sin criterio**: el umbral lo da el nivel de ruido

# Historia

**La SVD, descubierta cuatro veces**: Beltrami 1873, Jordan 1874, Sylvester
1889, Schmidt 1907. Se volvió central en **1965**, cuando Golub y Kahan
publicaron un algoritmo estable.

\vspace{0.5em}
\small
La utilidad de un concepto depende de que exista forma fiable de computarlo.

\vspace{0.8em}
\normalsize
**Wilkinson, 1961**: se temía que la eliminación gaussiana fuera inestable.
Demostró que la solución calculada es la **exacta** de un sistema ligeramente
perturbado.

\vspace{0.3em}
\small
La misma idea que los integradores simplécticos: *¿qué problema resuelve
exactamente mi algoritmo?*

# Lo esencial

* Un vector es un estado; una matriz, una regla
* Autovector = dirección que no se mezcla
* Toda transformación es rotar, estirar, rotar
* $\kappa$ dice cuántas cifras pierdes
* No normal $\Rightarrow$ los autovalores sólo describen el infinito
* No resuelvas por ecuaciones normales

# Para llevarse a casa

\Large

Antes de resolver cualquier sistema:

\vspace{0.5em}

**¿Cuánto amplifica esta matriz mis errores?**

\vspace{1.2em}

\normalsize
Pregunta abierta: la no normalidad explicó la turbulencia. ¿Dónde más estamos
usando autovalores donde harían falta pseudoespectros?
