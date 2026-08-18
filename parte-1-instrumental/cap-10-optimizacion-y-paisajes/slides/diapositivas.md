---
title: "Optimización y paisajes"
subtitle: "Capítulo 10 · Mirar antes de descender"
author: "La servilleta y el ordenador"
date: "Parte I — El instrumental del modelador"
---

# La pregunta

Un ajuste devuelve $\tau_1=1{,}03$, $\tau_2=1{,}12$, barras del 2 %.

Cambias el punto de partida: $\tau_1=0{,}71$, $\tau_2=1{,}54$, barras del 2 %.

\vspace{1em}
\Large
**¿Cuál de los dos es el bueno?**

\normalsize
\vspace{0.8em}
Ninguno. Y el algoritmo ha funcionado perfectamente las dos veces.

# Casi todo es una optimización disfrazada

| Lo que parece | Lo que es |
|---|---|
| Ajustar un modelo | minimizar $\chi^2$ |
| Un sistema en equilibrio | minimizar energía |
| Un rayo refractándose | minimizar tiempo (Fermat) |
| Un cristal formándose | minimizar energía libre |
| Una ruta de reparto | minimizar distancia |
| Inferencia bayesiana | maximizar la posterior |

# Mira el paisaje antes de elegir el algoritmo

\centering
![](../figuras/fig_paisajes.pdf){width=100%}

\raggedright\small
Convexidad · condicionamiento · rugosidad. Las tres deciden si el problema es
fácil.

# La frontera real

\Large

No es lineal / no lineal.

No es baja / alta dimensión.

\vspace{0.5em}

Es **convexo / no convexo**.

\normalsize
\vspace{1em}

Convexo con $10^5$ variables: se resuelve.
No convexo con 50: puede ser intratable.

# La curvatura compensa

$$\text{gradiente: } \frac{\kappa-1}{\kappa+1}
\qquad
\text{Newton: } \|e_{k+1}\|\propto\|e_k\|^2$$

\centering
![](../figuras/fig_gradiente_newton.pdf){width=95%}

\raggedright\small
20 000 pasos · 32 · **22**.

# ¿Y entonces por qué el ML usa gradiente?

* $n\sim10^9$: el hessiano tiene $10^{18}$ elementos y no cabe
* La objetivo es una suma sobre datos: se estima con un lote
* El ruido del gradiente **ayuda** a escapar de sillas y mesetas

\vspace{1em}

\alert{En un ajuste de 5 parámetros a 200 datos, usar SGD es un error.
El optimizador depende del régimen, no de la moda.}

# Recocido: física convertida en algoritmo

$$P(\text{aceptar }\Delta E>0)=e^{-\Delta E/T}$$

\centering
![](../figuras/fig_recocido.pdf){width=93%}

# Los tres resultados

| Estrategia | Mejor $E$ |
|---|---|
| $T=10^{-4}$ (casi cero) | **+0,70** — atrapado donde empezó |
| $T=6$ (muy caliente) | −2,97 — la encuentra, no se posa |
| Enfriamiento exponencial | **−2,97** — la encuentra y se queda |

\vspace{0.8em}

La temperatura es una **escala de exploración**: cuánto estás dispuesto a
empeorar para mirar más lejos.

# Optimizar y muestrear son lo mismo

$$p(x)\propto e^{-E(x)/T}$$

\vspace{0.5em}

$T\to\infty$: uniforme, todos los estados igual.

$T\to 0$: se concentra en el **mínimo global**.

\vspace{1em}

Muestrear a temperatura cero **es** optimizar.

\vspace{0.5em}

Y al revés: cualquier función objetivo define una distribución a la que puedes
aplicarle todo el capítulo 9.

# El paisaje te dice si tu parámetro existe

\centering
![](../figuras/fig_identificabilidad.pdf){width=100%}

\raggedright\small
En el valle, todos los puntos ajustan igual. El «resultado» es donde al
optimizador le dio por pararse.

# Diagnóstico, por orden de coste

1. **Arranca desde varios puntos.** Un minuto.
2. **Mira $\rho$ en la covarianza.** $|\rho|>0{,}95$: bandera roja.
3. **Autovalores del hessiano.** $\kappa>10^6$: direcciones sin determinar.
4. **Perfil de verosimilitud.** Lo correcto, y lo que casi nadie hace.

\vspace{1em}

\alert{Este fallo no parece un fallo: converge, no da errores y devuelve
barras pequeñas.}

# Y una advertencia final

\Large

**Ley de Goodhart**

\normalsize
\vspace{0.5em}

Cuando una medida se convierte en objetivo, deja de ser una buena medida.

\vspace{1em}

Optimizar agresivamente una función objetivo aproximada **explota sus
errores**.

\vspace{0.5em}

Casi siempre interesa un mínimo **ancho** antes que uno profundo y estrecho, y
eso hay que ponerlo en la objetivo: el optimizador no lo va a adivinar.

# Lo esencial

* Mira el paisaje antes de elegir el algoritmo
* Convexo/no convexo es la frontera
* El condicionamiento cambia el número de pasos
* La temperatura es exploración; $T\to0$ es optimizar
* Valle plano $\Rightarrow$ el parámetro no existe
* Goodhart: la objetivo también es un modelo

# Para llevarse a casa

\Large

Antes de lanzar un optimizador:

\vspace{0.5em}

**¿Qué forma tiene este paisaje, y estoy optimizando lo que quiero medir?**

\vspace{1.2em}

\normalsize
Pregunta abierta: ¿cómo se formula «quiero un óptimo robusto» dentro de la
propia función objetivo?
