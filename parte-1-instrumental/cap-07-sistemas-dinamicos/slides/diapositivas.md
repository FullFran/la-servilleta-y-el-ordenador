---
title: "Sistemas dinámicos"
subtitle: "Capítulo 7 · Geometría, umbrales y el límite de la predicción"
author: "La servilleta y el ordenador"
date: "Parte I — El instrumental del modelador"
---

# La pregunta

La predicción del tiempo a 3 días es buena. A 15 días es inútil.

\vspace{1em}
\Large
**¿Por qué existe ese muro, y dónde está exactamente?**

\normalsize
\vspace{1em}

Los modelos son deterministas. El muro no viene del azar ni de la complejidad.

# Geometría en lugar de fórmulas

Un sistema dinámico es un **campo de vectores**. En cada punto, una flecha.

\vspace{1em}

Casi todo lo cualitativo —cuántos equilibrios, si oscila, si es robusto— es
geometría del campo.

\vspace{0.5em}

No requiere integrar nada.

# Lo que la dimensión prohíbe

* **1D** — sólo puntos fijos. No oscila.
* **2D** — puntos fijos y ciclos límite. **No hay caos** (Poincaré–Bendixson).
* **3D+** — ya cabe todo.

\vspace{1em}

La razón es topológica: en el plano una curva cerrada separa dentro de fuera, y
una trayectoria no puede cortarse a sí misma.

\vspace{0.5em}

\alert{El caos necesita tres dimensiones **y** no linealidad.}

# Los autovalores lo dicen todo

$$\dot{\boldsymbol\eta}=J\boldsymbol\eta,
\qquad J_{ij}=\partial f_i/\partial x_j$$

\vspace{0.5em}

**Parte real = tasa. Parte imaginaria = frecuencia.**

\vspace{0.5em}

$\lambda = -0{,}1 \pm 2i$: oscila con periodo 3,1 y se amortigua con
$\tau = 10$.

\vspace{0.8em}

\alert{Si $\operatorname{Re}\lambda = 0$, la linealización **no decide**. Y ese
es justo el caso interesante.}

# Cuatro bifurcaciones, cuatro fenómenos

\centering
![](../figuras/fig_bifurcaciones.pdf){width=100%}

\raggedright\small
Silla-nodo: colapso irreversible · Transcrítica: umbral · Horquilla: ruptura de
simetría · Hopf: nace una oscilación

# Y una alarma temprana

Cerca de una bifurcación, el autovalor dominante $\to 0$.

\vspace{0.5em}

Luego el tiempo de recuperación $\to \infty$.

\vspace{1em}

**Ralentización crítica**: sube la autocorrelación, sube la varianza, el
sistema tarda cada vez más en volver.

\vspace{0.8em}

Se ha propuesto para lagos, clima, poblaciones al borde del colapso y crisis
epilépticas.

# El camino al caos, en una parábola

\centering
![](../figuras/fig_mapa_logistico.pdf){width=100%}

# Y un número universal

$$\delta = 4{,}669\,201\,6\ldots$$

\vspace{0.8em}

El mismo para **cualquier** mapa unimodal suave con máximo cuadrático.

\vspace{0.5em}

Feigenbaum lo encontró en 1975 con una HP-65, notando que los números se
repetían al cambiar de función.

\vspace{0.8em}

\small
Y: **periodo 3 implica caos** (Li y Yorke, 1975).

# Lorenz: tres ecuaciones y un muro

\centering
![](../figuras/fig_lorenz.pdf){width=100%}

\raggedright\small
$\lambda$ medido = 0,905. Valor aceptado = 0,906.

# El precio del caos

$$t_h=\frac{1}{\lambda}\ln\frac{\Delta}{\epsilon}$$

\centering
![](../figuras/fig_horizonte.pdf){width=72%}

\raggedright\small
Mil veces mejor medida = 7,7 unidades más de predicción.

# La consecuencia metodológica

Si no se puede predecir la **trayectoria**, se predice la **distribución**.

\vspace{1em}

De ahí vienen las predicciones por conjuntos y los porcentajes de probabilidad
de lluvia.

\vspace{1em}

\alert{El clima se puede calcular aunque el tiempo no se pueda predecir.}

# Lorenz, 1961: qué pasó realmente

Royal McBee LGP-30. La impresora daba 3 decimales; la máquina usaba 6.

Tecleó 0,506 donde había 0,506127.

\vspace{0.8em}

Lo importante: **sospechó primero de una avería del hardware**. Sólo después
de descartarla aceptó que el comportamiento era real.

\vspace{0.8em}

\small
Y el título de la mariposa (1972) no era suyo: se lo puso el organizador de la
sesión porque Lorenz no lo envió a tiempo.

# Poincaré, cuarenta años antes

1890, problema de los tres cuerpos, premio del rey Óscar II.

La memoria premiada tenía un **error**. Poincaré lo descubrió ya impresa, pagó
de su bolsillo la retirada —más de lo que había ganado— y la versión corregida
contiene el descubrimiento.

\vspace{0.8em}

\small
*Science et Méthode*, 1908: «una causa pequeñísima que se nos escapa determina
un efecto considerable, y entonces decimos que se debe al azar».

# Lo esencial

* Un sistema dinámico es geometría, no integración
* La dimensión limita lo posible
* Cuatro bifurcaciones, cuatro fenómenos físicos
* Ralentización crítica: la alarma es medible
* El caos es determinista; lo que crece es tu ignorancia
* $t_h \propto \ln(1/\epsilon)$: el horizonte crece como el logaritmo
* Trayectorias no; estadísticas sí

# Para llevarse a casa

\Large

Ante cualquier sistema que evoluciona:

\vspace{0.5em}

**¿Cuál es mi horizonte, y qué lo limita?**

\vspace{1.5em}

\normalsize
Pregunta abierta: si toda trayectoria numérica de un sistema caótico es falsa,
¿en qué sentido confiamos en las simulaciones climáticas?
