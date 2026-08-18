---
title: "¿Por qué cae una gota como cae?"
subtitle: "Parte II · Fenómeno 1"
author: "La servilleta y el ordenador"
---

# El fenómeno

Llovizna de 0,2 mm: cae a **0,7 m/s**. La sientes como humedad.

Gota de tormenta de 5 mm: cae a **9 m/s**. La sientes como un golpe.

\vspace{1em}

Diámetro $\times 25$. Velocidad $\times 13$.

\vspace{1em}
\Large
**¿Por qué no $\times 25$? ¿Y por qué no $\times 625$?**

# La estimación, primero

$$\tfrac43\pi r^3\rho_w g=\tfrac12 C_D \pi r^2\rho_a v_t^2
\;\Longrightarrow\;
v_t=\sqrt{\tfrac83\tfrac{r\rho_w g}{C_D\rho_a}}$$

\vspace{0.8em}

Con $r=1$ mm y $C_D=0{,}5$: **6,6 m/s**. El dato: 6,49 m/s.

\vspace{0.5em}

Un 2 % de error con una línea de álgebra.

# Dos regímenes

\centering
![](../figuras/fig_gota.pdf){width=100%}

\raggedright\small
$Re\ll1$: Stokes, $v_t\propto d^2$. $Re\gg1$: cuadrático,
$v_t\propto\sqrt d$. Frontera: $d\approx80$ μm.

# Y por eso las nubes no caen

Las gotitas de nube miden **10–20 μm**: están en régimen de Stokes y caen a
menos de 1 cm/s.

\vspace{0.8em}

Cualquier corriente ascendente las sostiene.

\vspace{0.8em}

Para que llueva hace falta que crezcan hasta ~100 μm. Ese crecimiento es el
problema central de la física de nubes.

# Toda gota llega a velocidad terminal

| Diámetro | $v_t$ | $\tau$ | Distancia hasta el 99 % |
|---|---|---|---|
| 0,2 mm | 0,72 m/s | 0,073 s | 0,10 m |
| 2 mm | 6,49 m/s | 0,66 s | **8,4 m** |
| 5 mm | 9,09 m/s | 0,93 s | **16,5 m** |

\vspace{0.8em}

Las nubes están a kilómetros.

\alert{La altura de la nube no influye en la fuerza del impacto.}

# Y no existen gotas de 1 cm

$$We=\frac{\rho_a v^2 d}{\gamma}\approx 10 \;\Longrightarrow\; d_{\max}\approx 6\text{ mm}$$

\vspace{1em}

Por encima, la presión dinámica vence a la tensión superficial y la gota se
rompe.

\vspace{0.5em}

Por eso $v_t$ se satura en 9–10 m/s.

# Lo esencial

* Un mismo objeto, dos físicas, según un número adimensional
* Las nubes flotan porque sus gotas miden micras
* $\hat v = \tanh\hat t$: una curva para todas
* Toda gota llega a velocidad terminal
* El tamaño máximo lo fija la rotura

\vspace{1em}

\alert{Antes de aplicar una fórmula asintótica: comprueba el número
adimensional.}
