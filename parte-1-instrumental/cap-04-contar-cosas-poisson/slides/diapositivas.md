---
title: "Contar cosas"
subtitle: "Capítulo 4 · Poisson, ruido y fluctuaciones"
author: "La servilleta y el ordenador"
date: "Parte I — El instrumental del modelador"
---

# La pregunta

Miras una zona oscura del cielo durante una hora: **12 fotones**.

El fondo instrumental produce **8 fotones** por hora.

\vspace{1em}
\Large
**¿Has detectado una fuente, o has visto ruido?**

# La propiedad que lo gobierna todo

Para Poisson, media y varianza **coinciden**:

$$\sigma_N = \sqrt{N}
\qquad\Longrightarrow\qquad
\frac{\sigma_N}{N}=\frac{1}{\sqrt N}$$

\vspace{0.8em}

El ruido absoluto **crece**. El ruido relativo **baja**.

\vspace{0.5em}

Ganar un factor 10 de precisión cuesta contar 100 veces más.

# Tres caminos, la misma respuesta

**1. Límite de la binomial** — $n\to\infty$, $p\to0$, $np$ fijo

**2. Ecuación maestra** — $\dot P_k = \lambda(P_{k-1}-P_k)$

**3. Máxima entropía** — lo mínimo que puedo suponer con media dada

\vspace{1em}

Cuando una distribución sale por tres caminos, no es un accidente de modelado:
es **estructural**.

# Dos conjuntos de datos, un siglo de antigüedad

\centering
![](../figuras/fig_poisson_datos.pdf){width=100%}

\raggedright\small
Laboratorio de Rutherford y registro administrativo prusiano. Var/media = 0,95
y 1,00. **La estructura matemática no pertenece al dominio.**

# El test más barato del mundo

$$D=\frac{\operatorname{Var}(N)}{E[N]}$$

\vspace{0.8em}

* $D\approx1$ — compatible con Poisson
* $D>1$ — **sobredispersión**: tasa variable, contagio, mezcla
* $D<1$ — **subdispersión**: tiempo muerto, refractariedad

\vspace{0.8em}

Una línea de código. Detecta el 80 % de los modelos de conteo mal
especificados.

# El grano no es del sensor

\centering
![](../figuras/fig_imagen_fotones.pdf){width=78%}

\raggedright\small
No hay ningún modelo de cámara en este código. Sólo `rng.poisson`.

# La paradoja del autobús

\centering
![](../figuras/fig_paradoja_autobus.pdf){width=100%}

\raggedright\small
Un hueco de 20 min ocupa el doble de línea temporal que uno de 10: tienes el
doble de probabilidad de caer en él.

# Dónde aparece disfrazada

* tus amigos tienen más amigos que tú
* las clases parecen más llenas de lo que dice la media
* los usuarios reportan latencias peores que la media real
* la duración de las relaciones de las que la gente te habla

\vspace{1em}

\alert{Muestrear un instante al azar $\neq$ muestrear un suceso al azar.}

# El coste de detectar

$$\frac{s}{\sqrt b}=\frac{r_s}{\sqrt{r_b}}\sqrt t
\qquad\Longrightarrow\qquad
t_{5\sigma}=\frac{25\,r_b}{r_s^2}$$

\centering
![](../figuras/fig_deteccion_fondo.pdf){width=92%}

# La consecuencia estratégica

El fondo entra **linealmente**. La señal, **al cuadrado**.

\vspace{1em}

Por eso, en experimentos de señal débil, el esfuerzo se dedica
obsesivamente a **reducir el fondo**.

\vspace{1em}

Y por eso, antes de pedir tiempo de telescopio, la primera cuenta que se hace
es $t_{5\sigma}$.

# Dos trampas

**La falacia del fiscal.** «5 sigmas» = $P(\text{datos}\mid\text{sin señal})$.
**No** es $P(\text{sin señal}\mid\text{datos})$.

\vspace{0.8em}

**Look-elsewhere.** Con 1000 canales de fondo puro:

$$P(\text{alguno}\ge3\sigma)\approx 74\,\%$$

\vspace{0.5em}

Por eso el umbral está en 5 sigmas y no en 3.

# Historia

**Bortkiewicz, 1898** — muertes por coz de caballo. Eligió un registro
administrativo absurdo para demostrar que el mecanismo importa más que el
dominio.

\vspace{0.6em}

**Rutherford, Geiger y Bateman, 1910** — contando centelleos a ojo, por turnos,
en una habitación oscura. La concordancia con Poisson **es la prueba de que los
núcleos no envejecen**.

\vspace{0.6em}

**Erlang, 1909** — cuántas líneas necesita la centralita de Copenhague. La
ingeniería creando teoría.

# Lo esencial

* El ruido de contar es el proceso, no el aparato
* $\sigma_N=\sqrt N$: relativo baja como $1/\sqrt N$
* Índice de dispersión: un test de una línea
* Significancia $\propto\sqrt t$; duplicarla cuesta $\times 4$
* Reducir fondo rinde más que aumentar señal
* Sesgo de longitud: sospecha siempre
* Un p-valor no es la probabilidad de estar equivocado

# Para llevarse a casa

\Large

Ante cualquier conteo:

\vspace{0.5em}

**¿Cuánto vale $\sqrt N$, y qué me permite afirmar?**

\vspace{1.5em}

\normalsize
Pregunta abierta: ¿por qué 5 sigmas y no 4 o 6? ¿Es una cuestión estadística o
sociológica?
