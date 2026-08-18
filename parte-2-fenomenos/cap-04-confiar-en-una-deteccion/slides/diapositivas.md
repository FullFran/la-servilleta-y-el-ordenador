---
title: "¿Cuánto podemos fiarnos de una detección?"
subtitle: "Parte II · Fenómeno 4"
author: "La servilleta y el ordenador"
---

# El fenómeno

Esperas 8 cuentas de fondo. Observas 12.

$$\frac{s}{\sqrt b}=\frac{4}{2{,}83}=1{,}4\sigma$$

\vspace{1em}
\Large
**¿Cuál es la probabilidad de que hayas detectado algo?**

\vspace{0.8em}
\normalsize
La pregunta está mal planteada. Ese es el capítulo.

# Lo que dice y lo que no

\centering
![](../figuras/fig_deteccion.pdf){width=100%}

\raggedright\small
Poisson exacta: $p=0{,}112$, es decir 1,22σ (no 1,4: con $\lambda<20$ la
gaussiana miente).

# Lo que significa ese 0,112

> Si no hubiera señal, vería un exceso así o mayor el 11 % de las veces.

\vspace{1em}

Lo que **no** significa:

* que haya un 11 % de probabilidad de que no haya señal
* que haya un 89 % de que sí la haya
* nada sobre la hipótesis, sin una previa

# La versión bayesiana

$$\frac{P(S\mid n)}{P(\bar S\mid n)}
=\underbrace{\frac{P(n\mid S)}{P(n\mid \bar S)}}_{\text{factor de Bayes}}
\times\underbrace{\frac{P(S)}{P(\bar S)}}_{\text{previa}}$$

\vspace{0.8em}

Con $n=12$, $b=8$, $s=4$: factor de Bayes = **2,4**.

\vspace{0.5em}

Con previa 1:100, la posterior queda en 1:42. Sigue siendo improbable.

\vspace{0.5em}

\alert{El umbral de 5σ no es tradición: es aritmética.}

# El techo sistemático

$$\frac{s}{\sqrt{b+(\delta b)^2}}
\;\xrightarrow[t\to\infty]{}\;
\frac{r_s}{\delta\,r_b}$$

\vspace{1em}

**Un límite constante.** Con $\delta=5\,\%$ y $r_s/r_b=0{,}5$: techo de 10σ.
Con $\delta=20\,\%$: 2,5σ, y no hay tiempo que lo supere.

\vspace{0.8em}

\alert{Cuando el sistemático domina, medir más no sirve. Hay que medir mejor
el fondo.}

# Higgs, 2011–2012

Diciembre 2011: 3,6σ y 2,6σ locales. **No se anuncia nada.**

Julio 2012: 5,0σ y 5,1σ. Entonces sí.

\vspace{0.8em}

Las dos colaboraciones trabajaron **a ciegas** y sin comunicarse.

# 750 GeV, 2015–2016

Diciembre 2015: 3,6σ y 2,6σ locales en difotones.

Más de **500 artículos teóricos** en los meses siguientes.

2016: el exceso desaparece.

\vspace{1em}

\alert{El sistema funcionó como debía: nadie anunció un descubrimiento y la
significancia global era de 2σ. Lo que falló fue la interpretación pública.}

\vspace{0.5em}

Un 3σ desaparece aproximadamente **una de cada tres veces**. Es la definición.

# Lo esencial

* Un p-valor no es la probabilidad de estar equivocado
* Factor de Bayes: cuánto favorecen los datos. Aquí, 2,4
* La incertidumbre del fondo pone un techo que no se supera midiendo
* Look-elsewhere: 4,7σ locales = 3σ globales con 1000 canales
* Con $\lambda<20$, Poisson exacta

\vspace{0.8em}

\alert{Con presupuesto fijo: ¿más tiempo, o mejor conocimiento del fondo?
Casi siempre lo segundo, y casi nunca se calcula.}
