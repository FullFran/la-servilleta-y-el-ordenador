---
title: "Incertidumbre y medida"
subtitle: "Capítulo 5 · Qué sabes, cuánto y por qué"
author: "La servilleta y el ordenador"
date: "Parte I — El instrumental del modelador"
---

# La pregunta

Diez medidas del mismo objeto. Desviación típica de la media: 0,005 mm.

\vspace{1em}
\Large
**¿Puedes escribir $12{,}304 \pm 0{,}005$ mm?**

\normalsize
\vspace{1em}

Esos diez números miden la **repetibilidad de tu procedimiento**.
No miden tu distancia a la verdad.

# Dos palabras que no son sinónimos

**Error** — la diferencia con el valor verdadero. Desconocida y no cognoscible.

**Incertidumbre** — la anchura que declaras. La calculas tú.

\vspace{1em}

El GUM clasifica por **cómo la evaluaste**, no por su origen:

* **Tipo A** — análisis estadístico de repeticiones
* **Tipo B** — todo lo demás: certificado, manual, juicio

# El sesgo es un suelo

$$\sigma_{\text{total}}=\sqrt{b^{2}+\frac{\sigma^{2}}{n}}$$

\centering
![](../figuras/fig_sesgo_dispersion.pdf){height=58%}

\raggedright\small
A partir de $n\approx(\sigma/b)^2$, seguir midiendo no sirve de nada.
Esa cuenta se hace **antes** de empezar.

# Cuándo miente la propagación lineal

\centering
![](../figuras/fig_propagacion.pdf){height=72%}

# Dos formas distintas de fallar

**Sesgo por curvatura.** $E[f(x)]\neq f(E[x])$. Para $f=x^2$:
sesgo $=\tfrac12 f''\sigma^2$.

\vspace{0.8em}

**Pérdida de sentido.** Si $x$ puede acercarse a 0, $1/x$ **no tiene media ni
varianza finitas**. Los dos números que calculas no significan nada.

\vspace{0.8em}

\alert{Más de un 20 \% de incertidumbre relativa en un denominador: deja de
propagar y simula.}

# Mínimos cuadrados no es neutro

$$\chi^2(\theta)=\sum_i\frac{(y_i-f(x_i;\theta))^2}{\sigma_i^2}$$

\vspace{0.8em}

Es **máxima verosimilitud** bajo el supuesto de errores gaussianos
independientes con varianzas conocidas.

\vspace{0.5em}

Si eso no se cumple, sigue funcionando pero deja de ser óptimo.

# $R^2$ no diagnostica nada

\centering
![](../figuras/fig_residuos.pdf){width=100%}

\raggedright\small
$R^2$: 0,981 vs 0,991. $\chi^2_\nu$: 2,15 vs 1,04. Los residuos: una parábola
vs ruido.

# Y el $\chi^2_\nu$ corta por los dos lados

$\chi^2_\nu \gg 1$ — el modelo está mal, o subestimaste los errores

$\chi^2_\nu \ll 1$ — **sobreestimaste los errores**, o los datos venían
ajustados, seleccionados o suavizados

\vspace{1em}

\alert{Un $\chi^2_\nu$ de 0,3 no es un ajuste buenísimo. Es una señal de
alarma.}

# Lo que las barras de error no dicen

\centering
![](../figuras/fig_covarianza.pdf){width=100%}

\raggedright\small
$\rho = -0{,}71$: si sube la amplitud, tiene que bajar $\tau$. Guardar sólo las
diagonales inventa combinaciones que los datos excluyen.

# La taza de café, primera visita

\centering
![](../figuras/fig_taza_cafe.pdf){width=100%}

\raggedright\small
$\tau$ = 24,2 · 24,4 · 24,2 min. **El tiempo característico no depende del
punto de partida.**

# Historia

**Gauss y Ceres, 1801.** 41 días de arco, un objeto perdido, una predicción que
acertó. Y una disputa de prioridad con Legendre que Stigler documentó:
Legendre publicó antes; la justificación probabilística sí es de Gauss.

\vspace{0.8em}

**«Student», 1908.** William Gosset, cervecería Guinness, Dublín. Publicó bajo
seudónimo porque la empresa lo prohibía. Su problema: decir algo honesto con
**cuatro datos**.

\vspace{0.5em}

Con muestras infinitas no habría inventado nada.

# Lo esencial

* Error es lo que no sabes; incertidumbre es lo que declaras
* El sesgo es un suelo: no se cruza midiendo más
* La propagación lineal falla por curvatura y por no linealidad
* $R^2$ no diagnostica; el $\chi^2_\nu$ y los residuos, sí
* Guarda la matriz de covarianza completa
* El sesgo no se detecta repitiendo: se detecta **cambiando de método**

# Para llevarse a casa

\Large

Ante cualquier resultado, el tuyo incluido:

\vspace{0.5em}

**¿Qué parte de este error se reduce midiendo más?**

\vspace{1.5em}

\normalsize
Pregunta abierta: si las $\sigma_i$ se estiman de los propios datos, ¿cómo se
propaga la incertidumbre de la incertidumbre?
