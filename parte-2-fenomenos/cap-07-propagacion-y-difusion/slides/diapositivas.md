---
title: "¿Cómo se propaga una sustancia?"
subtitle: "Parte II · Fenómeno 7"
author: "La servilleta y el ordenador"
---

# El fenómeno

El perfume difunde en aire quieto con $D\approx10^{-5}$ m²/s.

\vspace{1em}
\Large
**¿Cuánto tarda en cruzar una habitación de 5 m?**

\vspace{0.8em}
\normalsize
Y si la respuesta es la que sospechas: **¿por qué lo hueles en segundos?**

# Tres descripciones, una física

\centering
![](../figuras/fig_difusion.pdf){width=100%}

\raggedright\small
Paseo aleatorio · EDP · Langevin. Elegir entre ellas es **conveniencia**, no
verdad.

# La raíz del tiempo

$$\langle x^2\rangle = 2Dt \quad\Longrightarrow\quad t \sim \frac{L^2}{2D}$$

| Distancia | Tiempo (aire) |
|---|---|
| 1 μm | 0,05 ms |
| 1 mm | 50 s |
| 1 m | **14 días** |
| 5 m | **1 año** |

\vspace{0.5em}

\alert{Hueles el perfume en segundos porque el aire **no está quieto**.}

# El mismo número, invertido por el tamaño

$$Pe = \frac{UL}{D}$$

**Habitación**: $Pe\sim5\times10^4$. La difusión es irrelevante.

**Bacteria de 1 μm**: $Pe\sim10^{-2}$. La difusión es instantánea y nadar no
sirve para transportar nada al interior.

\vspace{1em}

\alert{Y por eso todo organismo mayor de unos milímetros necesita bombear: la
difusión no llega.}

# El exponente como diagnóstico

$$\langle x^2\rangle \propto t^{\alpha}$$

* $\alpha=1$ — difusión normal
* $\alpha<1$ — **subdifusión**: citoplasma, trampas, memoria
* $\alpha>1$ — **superdifusión**: vuelos de Lévy, turbulencia
* $\alpha=2$ — balístico

# Brown, Einstein, Perrin

**1827** — Brown ve el movimiento y descarta que sea vital (repite con polvo de
una esfinge egipcia)

**1905** — Einstein lo explica. Y su objetivo no era el movimiento browniano:
era **demostrar que los átomos existen**

**1908–13** — Perrin lo verifica y mide $N_A$. Nobel en 1926

\vspace{0.5em}

Ochenta años de observación a consecuencia conceptual.

# Lo esencial

* Tres descripciones equivalentes
* El tiempo va como el **cuadrado** de la distancia
* Péclet decide quién manda, y se invierte con el tamaño
* El exponente del MSD es un diagnóstico
* Difusión + degradación genera una longitud $\sqrt{D/k}$
