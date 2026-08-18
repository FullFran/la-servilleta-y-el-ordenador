---
title: "¿Cuánto hay que esperar?"
subtitle: "Parte II · Fenómeno 12"
author: "La servilleta y el ordenador"
---

# El fenómeno

Un servidor procesa 100 peticiones/s. Le llegan 90.

Está al 90 % de utilización: un 10 % de margen.

\vspace{1em}
\Large
**¿Cuánto espera una petición frente a un servidor al 50 %?**

\vspace{0.5em}
\normalsize
Diez veces más. No dos.

# La divergencia

$$W=\frac{1/\mu}{1-\rho}$$

\centering
![](../figuras/fig_colas.pdf){width=95%}

# Los números

| $\rho$ | $W$ |
|---|---|
| 0,50 | 2 |
| 0,80 | 5 |
| 0,90 | **10** |
| 0,95 | **20** |
| 0,99 | **100** |

\vspace{0.5em}

\alert{No hay degradación gradual. Ningún sistema con variabilidad se opera
cerca del 100 \%.}

# La variabilidad pesa tanto como la carga

$$W_q=\frac{\rho}{1-\rho}\cdot\frac{1+c_v^2}{2}\cdot\frac1\mu$$

| Servicio | $c_v$ | Espera medida ($\rho=0{,}85$) |
|---|---|---|
| Determinista | 0 | **3,7** |
| Exponencial | 1 | 6,9 |
| Muy variable | 2 | **13,7** |

\vspace{0.5em}

\alert{Estandarizar los tiempos de servicio es tan eficaz como añadir
capacidad, y mucho más barato.}

# Una cola o varias

La cola única **siempre** gana:

* nunca hay servidor ocioso con gente esperando
* nadie queda atrapado detrás del cliente lento

\vspace{0.8em}

Y la diferencia en el **p95** es mucho mayor que en la media.

\vspace{0.8em}

\small
Y sin embargo los supermercados usan colas separadas: la cola única **parece**
más larga aunque avance más deprisa.

# Y por eso se reportan percentiles

Sesgo de longitud (capítulo 4): quien llega al azar experimenta los periodos
malos con más probabilidad.

\vspace{0.8em}

99 % de peticiones en 10 ms + 1 % en 10 s $\Rightarrow$ media de 110 ms.

\vspace{0.5em}

Y **todos** los que se quejan están en ese 1 %.

\vspace{0.8em}

p50, p95, p99, p999. No medias.

# Erlang, 1909, y Little, 1961

**Erlang**: ¿cuántas líneas necesita la centralita de Copenhague? Midió con
cronómetro antes de escribir ninguna fórmula. Sus fórmulas B y C se usan hoy
igual.

\vspace{1em}

**Little**: $L = \lambda W$.

\vspace{0.5em}

No supone Poisson, ni exponencial, ni independencia, ni disciplina de servicio.
**Sólo estacionariedad.**

# Lo esencial

* La espera diverge como $1/(1-\rho)$
* La variabilidad pesa tanto como la carga
* Una cola única bate a varias, sobre todo en el p95
* Reporta percentiles, no medias
* $L=\lambda W$: sirve en cualquier sistema con flujo
