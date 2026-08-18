---
title: "¿Cómo se ve lo que no se puede ver?"
subtitle: "Parte II · Fenómeno 14"
author: "La servilleta y el ordenador"
---

# El fenómeno

El instrumento registra $m = f * h + \text{ruido}$, con $h$ conocido.

Por el teorema de convolución: $\hat f = \hat m / \hat h$.

\vspace{1em}
\Large
**¿Por qué eso no funciona?**

# Porque el inverso amplifica

$$\frac{\hat m}{\hat h} = \hat f_{\text{real}} + \frac{\hat n}{\hat h}$$

\centering
![](../figuras/fig_deconvolucion.pdf){width=95%}

\raggedright\small
Error de la ingenua: $6\times10^{15}$. De la regularizada: 2,2.

# Regularizar es cambiar la pregunta

$$\min_f\;\|Kf-m\|^2+\lambda\|Lf\|^2$$

\vspace{0.8em}

No se resuelve el problema original —ese no tiene solución estable— sino un
problema bien planteado próximo, indexado por $\lambda$.

\vspace{0.8em}

Elección de $\lambda$: curva L, discrepancia de Morozov, validación cruzada.

\vspace{0.5em}

\alert{Es una decisión de modelado, no un detalle técnico.}

# Toda penalización es una hipótesis

| Penalización | Hipótesis | Uso |
|---|---|---|
| $\|f\|^2$ | solución pequeña | genérica |
| $\|\nabla f\|^2$ | solución suave | señales |
| Variación total | plana a trozos | imágenes con bordes |
| $\|f\|_1$ | dispersa | espectros |
| $f\ge 0$ | sin negativos | conteos |

\vspace{0.5em}

\alert{La positividad es gratis, físicamente obvia y muy potente. Y se olvida.}

# Y determina lo que verás

Si penalizas rugosidad, tu resultado será suave — tenga o no bordes la realidad.

Si penalizas $\ell_1$, tu resultado tendrá picos.

\vspace{1em}
\Large

**Nunca se puede concluir que la solución tiene la estructura que tu
regularizador impone.**

# El Hubble, 1990–1993

Aberración esférica de 2,2 μm por un instrumento de prueba mal montado.

\vspace{0.8em}

Tres años de deconvolución (Richardson–Lucy) hasta la reparación. Funcionó, y
funcionó **por dos razones**:

* la PSF se medía con precisión sobre estrellas de campo
* la positividad es una restricción física fuerte

\vspace{0.8em}

Y de paso se catalogaron los artefactos característicos: anillos alrededor de
puntos, estructura espuria en objetos extensos.

# Lo esencial

* El operador directo suaviza; el inverso amplifica
* Regularizar es resolver otra pregunta, bien planteada
* $\lambda$ es modelado
* Declara tu penalización: determina lo que verás
* Por encima del corte no hay información: lo que aparece es tu previa
