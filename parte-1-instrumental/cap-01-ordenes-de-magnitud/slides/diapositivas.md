---
title: "Órdenes de magnitud"
subtitle: "Capítulo 1 · Estimaciones de Fermi"
author: "La servilleta y el ordenador"
date: "Parte I — El instrumental del modelador"
---

# La pregunta

Estás en una terraza en agosto. Se está montando una tormenta.

\vspace{1em}
\Large
**¿Cuánta energía libera, comparada con la bomba de Hiroshima?**

\normalsize
\vspace{1em}

No hay ningún dato a mano. Y aun así, en diez minutos tendremos una respuesta
que no falla por más de un factor 5.

# Antes de calcular

\Large

Apunta tres cosas. Ahora.

\normalsize
\vspace{0.6em}

1. Tu respuesta, con **una** cifra: $E \sim 10^{?}$ J
2. La cota que te parece imposible de bajar
3. La cota que te parece imposible de superar

\vspace{1em}

Sin ese número, lo que viene es divulgación.

# Vivimos en 60 décadas y pensamos en 3

\centering
![](../figuras/fig_escala_energias.pdf){height=72%}

# La idea: no estimar, descomponer

\centering
![](../figuras/fig_anatomia.pdf){width=92%}

\raggedright\small
La parte creativa es el paso 1. Multiplicar sabe multiplicar cualquiera.

# El modelo mínimo

$$E = A\,h\,\rho\,L$$

\vspace{0.5em}

| | | |
|---|---|---|
| Área | $A \sim 10^{8}$ m² | 10 km × 10 km |
| Lluvia | $h \sim 2\times10^{-2}$ m | 20 mm |
| Densidad | $\rho = 10^{3}$ kg/m³ | tabulada |
| Calor latente | $L = 2{,}3\times10^{6}$ J/kg | tabulada |

\vspace{0.8em}

$$E \approx 5\times10^{15}\ \text{J} \approx 70 \times \text{Hiroshima}$$

# ¿Por qué no es basura multiplicar cuatro números inventados?

$$\log Q = \sum_i \log x_i
\qquad\Longrightarrow\qquad
\sigma_{\log Q} = \sqrt{\textstyle\sum_i \sigma_i^2}$$

\vspace{0.8em}

Con $n$ factores igual de malos: $\;\sigma_{\log Q} = \sigma\sqrt{n}$

\vspace{0.8em}

Seis factores conocidos «a un factor 3»:

* si los errores conspirasen: $3^6 \approx 730$
* como son independientes: **factor 16**

# El error crece como $\sqrt{n}$, no como $n$

\centering
![](../figuras/fig_cancelacion.pdf){width=100%}

# Si no sabes estimar, acota

$$\hat{x} = \sqrt{x_{\min}x_{\max}}
\qquad \text{factor de error} = \sqrt{x_{\max}/x_{\min}}$$

\centering
![](../figuras/fig_sandwich.pdf){width=90%}

\raggedright\small
Incluso el razonamiento más tonto que puedas defender **acota**.

# ¿Dónde está tu error?

$$\text{contribución}_i = \frac{\sigma_i^2}{\sum_j \sigma_j^2}$$

\centering
![](../figuras/fig_tormenta_mc.pdf){width=100%}

\raggedright\small
Afina el factor **peor conocido**. Refinar lo que ya sabías se siente
productivo y no lo es.

# Lo que supone

1. Toda la lluvia viene de vapor condensado **dentro** del sistema
2. El calor latente domina (comprobado: lo demás está una década por debajo)
3. Los factores son independientes — *y no lo son del todo*
4. La comparación con Hiroshima sólo vale para energía total

\vspace{0.8em}

\alert{Densidad de potencia: 20 órdenes de magnitud de diferencia.}
Lo que hace daño no es la energía.

# Cuándo falla

\small

**Errores correlacionados** — el mismo dato malo entrando dos veces

**Diferencias de números grandes** — $A-B$ con $A\approx B$: el error explota

**Colas pesadas** — sin varianza no hay $\sqrt{n}$

\vspace{0.6em}

**Y el fallo dominante, que no es estadístico:**

\vspace{0.3em}

\Large\alert{estimar bien la cantidad equivocada}

# Fermi, Trinity, 16 de julio de 1945

\small

> «Intenté estimar su intensidad dejando caer desde una altura de unos seis
> pies pequeños trozos de papel antes, durante y después del paso de la onda.
> […] El desplazamiento fue de unos dos metros y medio, que estimé que
> correspondía a diez mil toneladas de TNT.»

\normalsize
\vspace{0.6em}

Valor aceptado hoy: **21 kt**. Fermi falló por un factor 2.

\vspace{0.6em}

Lo interesante no es que acertara. Es **por qué midió** habiendo
instrumentación cara: un número sin un número independiente al lado es un acto
de fe.

# Y lo que el mito borra

* El cálculo detallado de Fermi **no se conserva**. Lo que circula son
  reconstrucciones.
* Los afinadores de pianos de Chicago: **sin fuente primaria**. Folclore.
* «¿Dónde está todo el mundo?»: reconstruido en 1985 a partir de tres
  recuerdos de 35 años después.

\vspace{0.8em}

Distinguir estas tres cosas **es** la lección.

# Lo esencial

* Un orden de magnitud es un cajón, no un número
* Estimar es **descomponer en un producto**
* Los errores independientes crecen como $\sqrt{n}$
* Cuando no sepas estimar, **acota** y toma la media geométrica
* Afina el factor peor conocido
* Una estimación honesta es un intervalo, y su anchura es comprobable
* Estima por dos caminos

# Para llevarse a casa

\Large

Antes de calcular nada:

\vspace{0.5em}

**¿Qué orden de magnitud espero, y comparado con qué?**

\vspace{1.5em}

\normalsize
Pregunta abierta: si el error baja como $\sqrt{n}$ al descomponer más,
¿por qué no descomponer indefinidamente?
