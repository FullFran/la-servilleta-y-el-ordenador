---
title: "Análisis dimensional y similitud"
subtitle: "Capítulo 2 · Contar unidades para deducir leyes"
author: "La servilleta y el ordenador"
date: "Parte I — El instrumental del modelador"
---

# La pregunta

Una fotografía de una explosión, con una regla y un cronómetro.

\vspace{1em}
\Large
**¿Cuánta energía se liberó?**

\normalsize
\vspace{1em}

Sin composición del explosivo. Sin presión. Sin temperatura.
Sin resolver ninguna ecuación.

# La idea entera

Una ley física no puede depender de si mides en metros o en pies.

\vspace{1em}

Esa invariancia es una **simetría**.

\vspace{1em}

Y toda simetría **elimina grados de libertad**.

# Teorema $\pi$ de Buckingham

$n$ variables, $k$ dimensiones independientes $\Rightarrow$ $n-k$ grupos
adimensionales

\vspace{0.8em}

| | $R$ | $t$ | $E$ | $\rho$ |
|---|---|---|---|---|
| $\mathsf{M}$ | 0 | 0 | 1 | 1 |
| $\mathsf{L}$ | 1 | 0 | 2 | −3 |
| $\mathsf{T}$ | 0 | 1 | −2 | 0 |

\vspace{0.6em}

Rango 3, cuatro variables $\Rightarrow$ **un** grupo $\Rightarrow$ constante.

$$\pi_1=\frac{Et^2}{\rho R^5}=\text{const}
\qquad\Longrightarrow\qquad
R=C\left(\frac{Et^2}{\rho}\right)^{1/5}$$

# Es álgebra lineal disfrazada

Buscar un grupo adimensional = buscar un vector del **núcleo** de la matriz
dimensional.

\vspace{1em}

$$\dim(\text{núcleo}) = n - \operatorname{rango}$$

\vspace{1em}

$k$ es un **rango**, no «el número de dimensiones que se me ocurren».

# Trinity, 1945: la ley contra los datos

\centering
![](../figuras/fig_taylor_trinity.pdf){width=100%}

\raggedright\small
Pendiente medida 0,408 · teoría 0,400 · tres décadas de tiempo.

# El reparto de trabajo

**El análisis dimensional da la forma.**
$R \propto t^{2/5}$, con precisión de laboratorio.

\vspace{0.8em}

**La constante la da la física o el experimento.**
$C\approx1{,}03$ exige resolver la onda autosemejante.

\vspace{0.8em}

\alert{Vender lo primero como si fuera lo segundo es la exageración habitual
del método.}

# Adimensionalizar: el paso que más problemas salva

$$m\frac{dv}{dt}=mg-\tfrac12\rho C_D A v^2
\qquad\xrightarrow{\ \hat v = v/v_t,\ \hat t = t g/v_t\ }\qquad
\frac{d\hat v}{d\hat t}=1-\hat v^2$$

\vspace{1em}

Cuatro parámetros $\rightarrow$ **cero**.

\vspace{0.5em}

Todas las gotas del universo siguen la misma curva. Lo que cambia es la regla
con la que las mides.

# El colapso de datos

\centering
![](../figuras/fig_colapso_pendulo.pdf){width=100%}

\raggedright\small
Si los datos **no** colapsan, has olvidado una variable. Es el diagnóstico más
barato que existe.

# Un grupo adimensional es una pregunta

\small

| Grupo | La pregunta |
|---|---|
| $Re = UL/\nu$ | ¿puedo despreciar la viscosidad? |
| $Pe = UL/D$ | ¿transporta el flujo o la difusión? |
| $Ma = U/c$ | ¿es compresible? |
| $Fr = U/\sqrt{gL}$ | ¿importan las olas? |
| $Bi = hL/k$ | ¿temperatura uniforme dentro? |
| $Kn = \lambda/L$ | ¿es el gas un continuo? |

# Quince décadas de Reynolds

\centering
![](../figuras/fig_mapa_reynolds.pdf){width=88%}

# Las maquetas mienten

Para que una maqueta 1:100 represente al barco hacen falta a la vez:

$$Re \text{ igual} \Rightarrow U_m = 100\,U
\qquad\qquad
Fr \text{ igual} \Rightarrow U_m = U/10$$

\vspace{0.8em}

\alert{Incompatibles por un factor 1000.}

\vspace{0.8em}

Solución real (Froude, 1870): ensayar a $Fr$ igual y **corregir** la parte
viscosa aparte.

> Cuando no puedas cumplirlo todo, incumple lo que sepas corregir.

# Cuándo falla

* **Si olvidas una variable** — y falla en silencio
* **Con lo que ya es adimensional** — ángulos, cocientes, $\gamma$
* **Si necesitas la constante** — el método da la forma
* **Autosemejanza de segunda especie** — el exponente no sale de contar
* **Si mezclas unidades** — Mars Climate Orbiter, 1999, 125 M\$

# Historia: la misma solución, tres veces

* **G. I. Taylor** — informe británico de 1941, publicado en 1950
* **John von Neumann** — Los Álamos, 1941–43, informe interno
* **Leonid Sedov** — URSS, 1946, solución general

\vspace{1em}

Cuando un problema está maduro, se resuelve en varios sitios a la vez.

\vspace{0.5em}

\small
Y el «teorema de Buckingham» ya lo usaba Rayleigh. *Ley de Stigler.*

# Lo esencial

* $n$ variables, rango $k$ $\Rightarrow$ $n-k$ grupos
* Un solo grupo $\Rightarrow$ ley de potencias exacta
* Adimensionalizar una ecuación **elimina parámetros**
* Cada grupo es una pregunta física
* El colapso de datos es la prueba
* El método amplifica tu criterio físico; no lo sustituye

# Para llevarse a casa

\Large

Antes de resolver nada:

\vspace{0.5em}

**¿Cuántos parámetros tiene realmente este problema?**

\vspace{1.5em}

\normalsize
Pregunta abierta: ¿cómo se decide qué variables entran en la lista, sin hacer
trampa?
