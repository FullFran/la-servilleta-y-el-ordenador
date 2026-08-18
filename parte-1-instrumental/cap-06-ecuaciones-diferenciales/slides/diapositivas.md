---
title: "Ecuaciones diferenciales"
subtitle: "Capítulo 6 · El lenguaje del cambio"
author: "La servilleta y el ordenador"
date: "Parte I — El instrumental del modelador"
---

# La pregunta

Tres situaciones sin nada en común:

* una taza de café enfriándose
* un condensador descargándose
* una muestra radiactiva

\vspace{1em}
\Large
**¿Por qué las tres tienen la misma gráfica?**

# Porque las tres frases dicen lo mismo

«pierde calor tanto más deprisa cuanto más caliente está»

«se descarga tanto más deprisa cuanta más carga tiene»

«cuantos más núcleos quedan, más se desintegran»

\vspace{1em}

$$\frac{dx}{dt}=-\frac{x}{\tau}$$

# Cómo se lee una ecuación diferencial

$$\frac{dx}{dt}=f(x,t)$$

\vspace{1em}
\Large

**«Dime dónde estás y te digo hacia dónde vas.»**

\normalsize
\vspace{1em}

Es una regla **local**. No contiene la trayectoria: la genera.

# El estado, y lo que su dimensión prohíbe

El estado es la información mínima que determina el futuro.

\vspace{1em}

* 1 variable $\Rightarrow$ **no puede oscilar**
* 2 variables $\Rightarrow$ puede oscilar
* 3 variables $\Rightarrow$ puede ser caótico

\vspace{1em}

Restricciones fuertes sobre el comportamiento posible, deducidas **antes** de
escribir ninguna ecuación concreta.

# Los cuatro modelos que explican medio mundo

\centering
![](../figuras/fig_cuatro_modelos.pdf){width=100%}

\raggedright\small
La línea de fases se dibuja **sin resolver nada** y ya contiene todo el
comportamiento cualitativo.

# El café, derivado

$$mc\frac{dT}{dt}=-hA(T-T_{\text{amb}})
\qquad\Longrightarrow\qquad
\dot\theta = -\frac{\theta}{\tau},\quad \tau=\frac{mc}{hA}$$

\vspace{0.8em}

$\tau$ grande si hay **mucha masa** que enfriar.
$\tau$ pequeño si hay **mucha superficie** por la que perder.

\vspace{0.5em}

Por eso una taza grande se enfría despacio, los animales pequeños pasan frío y
los radiadores llevan aletas.

# $\tau$ como herramienta de decisión

* $t \ll \tau$ — el sistema apenas cambia: trátalo como constante
* $t \gg \tau$ — ya está en equilibrio: ignora el transitorio
* $t \sim \tau$ — sólo aquí hay que resolver de verdad

\vspace{1em}

Y con **varios** $\tau$ muy distintos, la variable rápida se puede tachar del
modelo.

# Dos relojes, un modelo más pequeño

\centering
![](../figuras/fig_escalas_temporales.pdf){width=100%}

\raggedright\small
$k_1/k_2 = 60$. Tras unas décimas de segundo, A ya no existe. Estado
cuasi-estacionario, eliminación adiabática, modelos reducidos: la misma idea.

# Adimensionalizar: tres parámetros que eran uno

$$\frac{dN}{dt}=rN\left(1-\frac{N}{K}\right)
\quad\xrightarrow{\ u=N/K,\ s=rt\ }\quad
\frac{du}{ds}=u(1-u)$$

\vspace{1em}

Barrer $r$ y $K$ es tirar el tiempo: **todos esos casos son el mismo caso.**

# Estabilidad en una línea

$$\dot\eta = f'(x^*)\,\eta
\qquad
\begin{cases} f'(x^*)<0 & \text{estable}\\ f'(x^*)>0 & \text{inestable}\end{cases}$$

\vspace{0.8em}

Y $|f'(x^*)|$ es el inverso del tiempo característico local.

\vspace{0.8em}

\alert{Si tu modelo de una variable oscila: o no es autónomo, o tiene un
retardo, o hay un error.}

# Lotka–Volterra

\centering
![](../figuras/fig_lotka_volterra.pdf){width=100%}

\raggedright\small
$\bar P=\gamma/\delta$, $\bar D=\alpha/\beta$: la media de presas **no depende
de los parámetros de las presas**.

# Volterra, su yerno y los peces del Adriático

1926. D'Ancona observa que durante la guerra, con **menos pesca**, la
proporción de depredadores **subió**.

\vspace{0.8em}

Volterra demuestra que pescar de todo por igual sube la media de presas y baja
la de depredadores.

\vspace{0.8em}

\alert{Corolario práctico: fumigar con insecticida de amplio espectro puede
aumentar la plaga.}

\vspace{0.5em}
\small
Lotka había publicado las mismas ecuaciones en 1920, para cinética química.

# Cuándo falla

* **Newton del enfriamiento** — con $\Delta T$ grande manda la radiación, $T^4$
* **Una sola temperatura** — sólo si $Bi \lesssim 0{,}1$
* **Lotka–Volterra** — órbitas **estructuralmente inestables**: cualquier
  perturbación las destruye
* **El continuo** — con 3 individuos, $dN/dt$ es ficción

# Lo esencial

* $\dot x = f(x)$: una regla local que genera la trayectoria
* El estado, y su dimensión, limitan lo que puede pasar
* Dibuja la línea de fases antes de resolver
* $\tau$ es la unidad natural y decide qué ignorar
* Adimensionaliza antes de barrer
* Busca cantidades conservadas: resuelven, o comprueban tu código

# Para llevarse a casa

\Large

Ante cualquier sistema que cambia:

\vspace{0.5em}

**¿Cuántos números necesito hoy para predecir mañana,
y cuál es el reloj del sistema?**

\vspace{1.2em}

\normalsize
Pregunta abierta: si casi todo lo que observamos está cerca de un equilibrio,
¿vemos el mundo o su linealización?
