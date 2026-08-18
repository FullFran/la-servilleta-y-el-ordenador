---
title: "¿Cómo encontramos el camino más probable?"
subtitle: "Parte II · Fenómeno 8"
author: "La servilleta y el ordenador"
---

# El fenómeno

Un socorrista corre a 5 m/s y nada a 1,5 m/s.

\vspace{1em}
\Large
**¿Por dónde entra al agua?**

\normalsize
\vspace{1em}

No por la línea recta. Y el óptimo cumple **exactamente** la ley de Snell.

# La misma estructura, tres veces

\centering
![](../figuras/fig_caminos.pdf){width=100%}

\raggedright\small
$\sin\theta_1/\sin\theta_2 = v_1/v_2 = 3{,}333$ · Dijkstra · acción
estacionaria en $\alpha=1{,}003$

# Y la versión probabilística

$$P(\text{camino}) \propto e^{-S/\epsilon}$$

\vspace{0.8em}

El camino **más probable** es el de coste mínimo, y la probabilidad se
concentra con anchura $\sqrt\epsilon$.

\vspace{0.8em}

* **Cuántica**: $\sum_{\text{caminos}}e^{iS/\hbar}$ (Feynman)
* **Grandes desviaciones**: $e^{-S/\epsilon}$ (Freidlin–Wentzell)
* **Inferencia**: Viterbi = Dijkstra en (estado, tiempo)

# Programación dinámica

\Large
Principio de optimalidad (Bellman):

**cualquier tramo final de un camino óptimo es óptimo**

\normalsize
\vspace{1em}

De exponencial a polinómico. Condición: coste **aditivo** y sistema **Markov**.

\vspace{0.8em}

Viterbi · alineamiento de secuencias · control óptimo · Hamilton–Jacobi–Bellman

# La luz no elige

Fermat, 1662: la objeción de la época era que el principio atribuía a la luz un
conocimiento del destino.

\vspace{1em}

Euler y Lagrange: el principio integral y las ecuaciones locales son
**equivalentes**. Ninguna es más fundamental.

\vspace{1em}

Feynman: los caminos vecinos interfieren y se cancelan salvo cerca del
estacionario.

\vspace{0.5em}

\alert{La luz prueba todos. El resto se cancela.}

# Lo esencial

* «Minimizar a lo largo de un camino»: óptica, mecánica, logística, inferencia
* Optimizar y muestrear son lo mismo a dos temperaturas
* El principio de optimalidad exige coste aditivo y Markov
* Estacionario no es mínimo
* El principio variacional no implica teleología
