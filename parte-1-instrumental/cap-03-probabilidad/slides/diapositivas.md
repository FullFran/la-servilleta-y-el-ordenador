---
title: "Probabilidad"
subtitle: "Capítulo 3 · Modelo del desconocimiento y del azar"
author: "La servilleta y el ordenador"
date: "Parte I — El instrumental del modelador"
---

# La pregunta

Un test detecta al 99 % de los enfermos y da negativo al 99 % de los sanos.

La enfermedad afecta a 1 de cada 1000.

\vspace{1em}
\Large
**Das positivo. ¿Qué probabilidad tienes de estar enfermo?**

\normalsize
\vspace{1em}
Casi todo el mundo dice 99 %.

# Dos cosas distintas con el mismo nombre

**Aleatoria** — propiedad del proceso. Tiene sentido repetir.

**Epistémica** — estado de tu conocimiento. No hay repetición.

\vspace{1em}

Lanzo una moneda y la tapo. Ya ha caído.

\vspace{0.5em}

\alert{La probabilidad 1/2 no está en la moneda: está en ti.}

\vspace{0.5em}

Dos observadores racionales pueden asignar probabilidades distintas al mismo
hecho sin que ninguno se equivoque.

# El espacio muestral es el modelo

«Tengo dos hijos, al menos uno es niña. ¿Probabilidad de dos niñas?»

\vspace{0.8em}

* Pregunté «¿tienes al menos una hija?» $\Rightarrow$ **1/3**
* Me encontré a una hija por la calle $\Rightarrow$ **1/2**

\vspace{0.8em}

Mismos datos. Distinta respuesta.

\vspace{0.5em}

\alert{El dato no es «hay una niña». El dato es «he recibido esta información
de esta manera».}

# Bayes no es una teoría, es una identidad

$$P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}$$

\vspace{0.8em}

Lo que hace: **invertir el sentido del condicionamiento**.

\vspace{0.5em}

Tú conoces $P(\text{síntoma}\mid\text{causa})$.
Te importa $P(\text{causa}\mid\text{síntoma})$.

# Cuenta personas, no probabilidades

\centering
![](../figuras/fig_bayes_frecuencias.pdf){width=100%}

\raggedright\small
10 enfermos, 9990 sanos. El test acierta con 9,9 enfermos y falla con 99,9
sanos. **Diez veces más falsos positivos que verdaderos.**

# Cada distribución es la huella de un mecanismo

\centering
![](../figuras/fig_mecanismos.pdf){width=95%}

# La pareja que hay que recordar

$$\textbf{suma} \longrightarrow \text{normal}
\qquad\qquad
\textbf{producto} \longrightarrow \text{log-normal}$$

\vspace{1em}

Por eso la tormenta del capítulo 1 salió log-normal: era un producto de cuatro
factores, así que su logaritmo era una suma.

# Independencia: el supuesto que nadie escribe

$$P(A\cap B)=P(A)P(B)$$

\vspace{0.8em}

Dos sistemas redundantes con $p_\text{fallo}=10^{-3}$:

* independientes $\Rightarrow$ $10^{-6}$
* misma fuente de alimentación $\Rightarrow$ $10^{-3}$

\vspace{0.8em}

\alert{Cada vez que multipliques probabilidades, escribe en el margen por qué
crees que son independientes.}

# LGN y TCL: qué prometen

\centering
![](../figuras/fig_lgn_tcl.pdf){width=100%}

\raggedright\small
Convergencia sí. Velocidad, $1/\sqrt{n}$: una cifra decimal más cuesta cien
veces más esfuerzo.

# Y cuándo no se cumplen

\centering
![](../figuras/fig_cauchy.pdf){width=100%}

\raggedright\small
Cauchy no tiene media. Un solo dato puede dominar a todos los anteriores
juntos. **Promediar no ayuda.**

# Dónde aparecen las colas pesadas

* tamaños de ciudades, empresas y ficheros
* magnitudes de terremotos
* pérdidas en seguros
* grados de nodos en redes
* latencias en sistemas distribuidos

\vspace{1em}

Por eso se reportan percentiles y no medias.

\vspace{0.5em}

\alert{Si la media muestral se mueve mucho al añadir un dato, no promedies.}

# Historia

* **1654** — Pascal y Fermat, por un problema de apuestas
* **1763** — Bayes, publicado por Price tras su muerte
* **1774** — Laplace redescubre y generaliza
* **1933** — Kolmogórov: 62 páginas de axiomas

\vspace{0.8em}

Hacking: ¿por qué tan tarde? Los dados llevaban milenios existiendo.

\vspace{0.5em}

Kolmogórov no resolvió un problema filosófico: resolvió que «al azar» no
significa nada hasta que digas **respecto a qué medida**.

# Lo esencial

* Dos probabilidades distintas. Declara cuál usas
* El espacio muestral **es** el modelo
* Bayes invierte el condicionamiento
* Traduce todo a frecuencias naturales
* Reconoce el mecanismo, no la fórmula
* La independencia se asume por omisión
* Sin varianza finita no hay campana ni barras de error

# Para llevarse a casa

\Large

Antes de escribir ninguna fórmula:

\vspace{0.5em}

**¿Qué mecanismo generó este dato?**

\vspace{1.5em}

\normalsize
Pregunta abierta: si la probabilidad epistémica describe tu conocimiento,
¿de dónde sale la primera previa?
