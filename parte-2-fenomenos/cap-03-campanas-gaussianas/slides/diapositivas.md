---
title: "¿Por qué hay campanas por todas partes?"
subtitle: "Parte II · Fenómeno 3 · Y dónde no las hay"
author: "La servilleta y el ordenador"
---

# El fenómeno

La persona más alta del mundo mide **2,5 veces** la media.

El terremoto más grande liberó **$10^5$ veces** la energía del medio.

\vspace{1em}
\Large
**¿Por qué las alturas tienen un máximo y los terremotos no?**

# Tres mecanismos, tres formas

\centering
![](../figuras/fig_dominios_atraccion.pdf){width=100%}

\raggedright\small
El número de términos no determina la forma. La determinan el mecanismo y la
existencia de momentos.

# El cuarto mecanismo

**Crecimiento proporcional** $\Rightarrow$ ley de potencias

\vspace{0.8em}

Yule (1925) · Simon (1955) · Barabási y Albert (1999)

\vspace{0.5em}

El mismo mecanismo redescubierto tres veces en tres campos, sin citarse.

# Por qué importa

| Herramienta | Requiere | Sin ella |
|---|---|---|
| $\sigma/\sqrt n$ | varianza finita | no significa nada |
| Intervalos normales | TCL | cobertura falsa |
| Media muestral | media finita | no converge |
| Mínimos cuadrados | errores gaussianos | dominados por atípicos |
| Monte Carlo | varianza finita | no baja como $1/\sqrt N$ |

# Diagnóstico en dos gráficas

**Media acumulada**: ¿da saltos al añadir datos?

**Supervivencia $P(X>x)$ en log-log**: ¿es una recta?

\vspace{1.5em}

\alert{Y casi nada de lo que se publica como ley de potencias resiste un
contraste frente a la log-normal.}

\vspace{0.5em}
\small
Clauset, Shalizi y Newman (2009): de 24 conjuntos publicados, muy pocos
sobreviven.

# La respuesta

**Las alturas son suma.** Muchos factores pequeños. Varianza finita. Campana.
La persona más alta está a 14σ, y eso ya indica que la cola real es más gruesa.

\vspace{0.8em}

**Los terremotos son crecimiento.** Una ruptura se propaga mientras encuentre
tensión; cada incremento hace más probable el siguiente.

\vspace{0.8em}

\Large
La diferencia física es si el mecanismo **suma** o **multiplica**.

# Y para diseñar, no interesa la media

Interesa el **máximo**. Teorema de Fisher–Tippett–Gnedenko: tres clases.

* **Gumbel** — cola exponencial. Récords crecen como $\ln n$
* **Fréchet** — cola de potencias. Récords crecen como $n^{1/\alpha}$
* **Weibull** — extremo acotado

\vspace{0.8em}

\alert{Con Fréchet no existe «el máximo posible».}

\vspace{0.5em}
\small
Las inundaciones de Países Bajos de 1953, con 1836 muertos, motivaron el
desarrollo de esta teoría aplicada al diseño de diques.

# Lo esencial

* La forma la decide el mecanismo, no el número de términos
* Sin varianza finita se cae medio arsenal estadístico
* Media acumulada y supervivencia log-log: dos gráficas
* Log-normal y potencias son casi indistinguibles con datos reales
* Para el extremo, otra distribución y otra teoría
