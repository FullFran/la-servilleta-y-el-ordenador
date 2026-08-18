---
title: "Escalas y perturbaciones"
subtitle: "Capítulo 13 · Qué se puede ignorar"
author: "La servilleta y el ordenador"
date: "Parte I — El instrumental del modelador"
---

# La pregunta

Llevamos doce capítulos diciendo «para ángulos pequeños,
$\sin\theta\approx\theta$».

\vspace{1em}
\Large
**¿Cuánto de pequeño es pequeño?**

\normalsize
\vspace{1em}

Y algo peor: a veces el término pequeño **es el que manda**.

# La respuesta, en números

| Aproximación | Error $<1\,\%$ hasta |
|---|---|
| $\sin\theta\approx\theta$ | 0,248 rad = **14°** |
| $\sin\theta\approx\theta-\theta^3/6$ | 1,010 rad = **58°** |
| Un término más | 1,757 rad = **101°** |

\vspace{0.8em}

Catorce grados. Bastante menos de lo que casi todo el mundo supone.

\vspace{0.5em}

\alert{Y para el **periodo** del péndulo aguanta hasta 23°: el dominio de
validez depende de qué cantidad te importa.}

# Hasta dónde vale, y cuándo empeora

\centering
![](../figuras/fig_taylor_validez.pdf){width=100%}

# Balance dominante

1. Escribe todos los términos
2. **Supón** cuáles dos dominan
3. Resuelve ese balance
4. **Comprueba** que los despreciados son pequeños

\vspace{1em}

\alert{El paso 4 es lo que distingue el método de adivinar.}

# Regular frente a singular

\centering
![](../figuras/fig_balance_dominante.pdf){width=100%}

\raggedright\small
$\epsilon x^2+x-1=0$. Al hacer $\epsilon=0$ la ecuación **baja de grado** y una
raíz se escapa al infinito. Reescalando $x=X/\epsilon$ vuelve.

# Las señales de alarma

Es singular si:

* $\epsilon$ multiplica **la derivada de orden más alto**
* $\epsilon$ multiplica el término de mayor grado
* al poner $\epsilon=0$ **sobran condiciones de contorno**
* hay una región estrecha donde todo varía deprisa

# Capas límite

\centering
![](../figuras/fig_capa_limite.pdf){width=100%}

\raggedright\small
Dos escalas: $1$ y $\epsilon$. La solución exterior no puede cumplir $y(0)=0$.

# Prandtl, 1904

Paradoja de d'Alembert: un fluido ideal no ofrece resistencia. Contradice la
mano por la ventanilla.

\vspace{0.8em}

Ocho páginas en Heidelberg: la viscosidad es despreciable **salvo en una capa
finísima junto a la pared**, donde los gradientes son enormes.

\vspace{0.8em}

$\delta \sim L/\sqrt{Re}$.

\vspace{0.5em}

\alert{No resolvió Navier–Stokes. Identificó dos regiones, resolvió cada una
y las empalmó.}

# Series que divergen y funcionan

\centering
![](../figuras/fig_serie_asintotica.pdf){width=100%}

| $x$ | mejor $N$ | error mínimo | con 25 términos |
|---|---|---|---|
| 10 | 9 | $1{,}8\times10^{-5}$ | 0,11 |

# Convergencia $\neq$ utilidad

Una serie **convergente** puede necesitar $10^6$ términos para tres cifras.

Una **divergente** puede dar cinco cifras con cuatro términos.

\vspace{1em}

Regla: **suma hasta el término más pequeño y para**. El error alcanzable decae
como $e^{-x}$.

\vspace{0.8em}

\small
Dyson, 1952: la serie de la QED **tiene** que divergir. Y predice el momento
magnético del electrón con doce cifras. La serie divergente más exitosa de la
historia.

# Lo que el análisis asintótico te da gratis

\Large

**Te dice dónde poner los puntos de malla antes de calcular nada.**

\normalsize
\vspace{1em}

Malla uniforme para una capa de $10^{-3}$: $10^4$ nodos.
Malla graduada sabiendo dónde está la capa: 200.

\vspace{0.8em}

En problemas grandes, esa diferencia decide si el cálculo es viable.

# El término pequeño que se acumula

Achatamiento terrestre: $10^{-3}$ del término principal.

Una órbita: error del 0,1 %, irrelevante.

500 órbitas: **precesión de varios grados**.

\vspace{1em}

\alert{¿Este término se promedia a cero o se acumula? Si se acumula, el
criterio pasa de $\epsilon\ll1$ a $\epsilon t\ll1$.}

# Lo esencial

* «Pequeño» sin decir comparado con qué no significa nada
* Taylor sirve para decidir: lo que importa es el resto
* Balance dominante: supón, resuelve, **comprueba**
* Singular = $\epsilon$ en la derivada más alta $\Rightarrow$ reescala
* Una capa límite es donde el término pequeño deja de serlo
* Las series asintóticas divergen y funcionan
* Un término pequeño acumulativo no es pequeño

# Para llevarse a casa

\Large

Cada vez que desprecies algo:

\vspace{0.5em}

**Escribe el número adimensional que lo justifica,
y pregúntate si se acumula.**

\vspace{1.2em}

\normalsize
Pregunta abierta: si el error mínimo de una asintótica es $e^{-1/\epsilon}$,
¿qué información hay en esa parte exponencialmente pequeña?
