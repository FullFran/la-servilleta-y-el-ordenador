---
title: "¿Cómo puede surgir orden del azar?"
subtitle: "Parte II · Fenómeno 9"
author: "La servilleta y el ordenador"
---

# El fenómeno

Cada átomo de un imán sólo «sabe» de sus vecinos, y cambia de orientación
constantemente y al azar.

\vspace{1em}
\Large
**¿Cómo consiguen millones ponerse de acuerdo?**

# El modelo más simple posible

$$E=-J\sum_{\langle ij\rangle}s_is_j,\qquad s_i=\pm1$$

\centering
![](../figuras/fig_ising.pdf){width=92%}

# La competencia

$$F = E - TS$$

**La energía** prefiere el orden. **La entropía**, el desorden.

\vspace{0.8em}

Y el paso entre ambos regímenes **no es gradual**.

\vspace{1em}

* **1D**: no hay transición a $T>0$
* **2D**: $T_c=2/\ln(1+\sqrt2)=2{,}269$, exacto (Onsager, 1944)
* **3D**: hay transición y **no** hay solución exacta

# Universalidad

$$m\sim(T_c-T)^{\beta},\quad \chi\sim|T-T_c|^{-\gamma},\quad
\xi\sim|T-T_c|^{-\nu}$$

\vspace{0.8em}

Esos exponentes son **idénticos** para el Ising 3D, el punto crítico del agua y
una mezcla binaria.

\vspace{0.8em}

Cerca del punto crítico $\xi$ diverge y el sistema deja de ver la escala
atómica. Sólo importan **dimensión y simetría**.

\vspace{0.5em}

\alert{Es una justificación profunda del modelo mínimo: ahí los detalles
microscópicos son literalmente irrelevantes.}

# Ising, 1925: un error de extrapolación

Resolvió el caso 1D, no encontró transición, y concluyó que el modelo no servía
para el ferromagnetismo.

\vspace{1em}

**1D es el caso excepcional.**

\vspace{1em}

Dejó la investigación, fue profesor de instituto, huyó del nazismo, y descubrió
que su modelo era famoso leyendo la literatura años después.

# La misma estructura, fuera de la física

* **Percolación** — conectividad que aparece de golpe
* **Segregación de Schelling** — preferencia del 30 % $\Rightarrow$ segregación
  casi total
* **Kuramoto** — sincronización súbita de osciladores
* **Turing** — manchas y rayas espontáneas

\vspace{0.8em}

Reglas locales simples · umbral crítico · orden global emergente

# Lo esencial

* Orden global desde interacciones locales, por balance energía–entropía
* La dimensión decide si hay transición
* Los exponentes son universales
* Metropolis se ralentiza críticamente; los cúmulos lo resuelven
* El orden espontáneo no necesita organizador
