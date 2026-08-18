---
title: "Monte Carlo"
subtitle: "Capítulo 9 · Calcular mediante azar"
author: "La servilleta y el ordenador"
date: "Parte I — El instrumental del modelador"
---

# La pregunta

El volumen de la intersección de una bola y un cubo en **diez dimensiones**.

Un problema puramente determinista. La respuesta es un número fijo.

\vspace{1em}
\Large
**¿Por qué la mejor manera de calcularlo es tirar dados?**

# El método entero, en una línea

$$I=\int_\Omega f(x)\,dx = |\Omega|\,E[f(X)]
\qquad\Longrightarrow\qquad
\hat I=\frac{|\Omega|}{N}\sum_{i=1}^N f(x_i)$$

\vspace{1em}

Toda integral es una esperanza. Toda esperanza se estima muestreando.

\vspace{0.8em}

\alert{El azar no está en el problema: está en el algoritmo.}

# Buffon, 1733

\centering
![](../figuras/fig_buffon.pdf){width=100%}

\raggedright\small
$P = 2L/(\pi D)$. Y ese punto rojo es Lazzarini, 1901: 3408 agujas,
$\pi = 355/113$, seis decimales.

# Por qué Lazzarini es imposible

Con 3408 agujas, $\sigma \approx 0{,}041$.

Su error: $2{,}7\times10^{-7}$.

\vspace{0.8em}

Un solo cruce de diferencia mueve la estimación $10^{-3}$: **mil veces más que
el error que reporta**.

\vspace{0.8em}

Y $355/113$ es la aproximación de Zu Chongzhi, conocida desde el siglo V.

\vspace{0.5em}

\alert{Detención selectiva. Un resultado demasiado bueno es tan sospechoso
como uno demasiado malo.}

# El error, y sus tres lecturas

$$\epsilon = \frac{\sigma_f}{\sqrt N}$$

\vspace{0.8em}

**Malo:** $1/\sqrt N$ es lentísimo. Una cifra más $\to$ 100 veces más muestras.

**Sutil:** la constante $\sigma_f$ importa tanto como el exponente. Ahí está
todo el oficio.

**Y lo que lo cambia todo:** en esa fórmula **no aparece la dimensión**.

# El cruce está antes de lo que crees

\centering
![](../figuras/fig_convergencia_mc.pdf){width=100%}

\raggedright\small
Rejilla: error $\mathcal{O}(N^{-k/d})$ — el exponente se divide por $d$.
Monte Carlo: $N^{-1/2}$, siempre.

# Y $1/\sqrt{N}$ no es una ley de la naturaleza

Secuencias de baja discrepancia (Sobol, Halton): error $\sim (\log N)^d/N$.

\vspace{0.8em}

Casi $1/N$. Un orden de magnitud mejor con $10^5$ puntos.

\vspace{0.8em}

`scipy.stats.qmc.Sobol`. Es gratis.

\vspace{0.5em}

\alert{Si integras en dimensión moderada con Monte Carlo puro, probablemente
estás tirando muestras.}

# Cómo se generan las muestras

\centering
![](../figuras/fig_muestreo.pdf){width=100%}

\raggedright\small
Inversa si puedes · rechazo si no · importancia si el suceso es raro.
La propuesta debe tener colas **al menos tan pesadas** como el objetivo.

# El problema que lo cambió todo

$$p(\mathbf{s})=\frac{e^{-E(\mathbf{s})/kT}}{Z},
\qquad Z=\sum_{\mathbf{s}}e^{-E(\mathbf{s})/kT}$$

\vspace{0.5em}

Con 100 espines, $Z$ tiene $10^{30}$ términos. **No se puede normalizar.**

\vspace{1em}

Metropolis (1953): no generes muestras independientes. Construye una cadena de
Markov cuya estacionaria sea $p$.

$$T(x\to y)=q(y|x)\min\!\left(1,\frac{p(y)}{p(x)}\right)$$

\alert{Sólo aparece el cociente. Y en el cociente, $Z$ se cancela.}

# El diagnóstico es la parte difícil

\centering
![](../figuras/fig_metropolis.pdf){width=93%}

# Los números

| Paso | Aceptación | $\tau_{\text{int}}$ | $N_{\text{ef}}$ de 55 000 |
|---|---|---|---|
| 0,2 | 89 % | 384 | 143 |
| 1,5 | 43 % | 291 | **189** |
| 8,0 | 17 % | 17 | **3143** |

\vspace{0.8em}

La regla de manual —«aceptación del 25–40 %»— da aquí **el peor resultado**.

\vspace{0.5em}

\alert{La tasa de aceptación no diagnostica convergencia. $N_{\text{ef}}$ y
varias cadenas, sí.}

# Quién hizo qué en 1953

Cinco firmantes. Marshall Rosenbluth, en 2003:

\vspace{0.5em}

* Metropolis: **tiempo de máquina**
* Edward Teller: la sugerencia inicial
* Augusta Teller: parte de la programación inicial
* **Marshall y Arianna Rosenbluth: el algoritmo y el código**

\vspace{0.8em}

Arianna Rosenbluth, doctora en física por Harvard, programó el MANIAC entero.

\vspace{0.5em}

\small
Orden alfabético + citar por el primer autor = cincuenta años corrigiendo.

# Ulam, 1946

Convaleciente de una encefalitis, jugando al solitario Canfield.

Intentó el cálculo combinatorio. Era intratable.

\vspace{0.8em}

«Sería mucho más práctico jugar cien manos y contar.»

\vspace{0.8em}

Y de ahí, inmediatamente: la difusión de neutrones también es intratable, y
también se puede muestrear.

# Lo esencial

* Toda integral es una esperanza
* $\epsilon = \sigma_f/\sqrt N$: mejora la constante, no el exponente
* La dimensión no aparece. El cruce con la rejilla está en $d\approx4$–5
* Usa Sobol si la función es suave
* Metropolis funciona porque sólo necesita cocientes
* Barras de error con $N_{\text{ef}}$, **nunca** con $N$
* Un resultado demasiado bueno es sospechoso

# Para llevarse a casa

\Large

Antes de aceptar un resultado de simulación estocástica:

\vspace{0.5em}

**¿Cuántas muestras **independientes** tengo de verdad?**

\vspace{1.2em}

\normalsize
Pregunta abierta: ¿se puede demostrar alguna vez que una cadena ha convergido,
o sólo que no lo ha hecho?
