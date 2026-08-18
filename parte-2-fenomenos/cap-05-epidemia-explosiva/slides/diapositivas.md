---
title: "¿Por qué una epidemia puede explotar?"
subtitle: "Parte II · Fenómeno 5"
author: "La servilleta y el ordenador"
---

# El fenómeno

$R_0=3$, población totalmente susceptible.

\vspace{1em}
\Large
**¿Qué fracción acaba infectada?**

\normalsize
\vspace{1em}

Respuesta intuitiva: 67 %, el umbral de inmunidad de grupo $1-1/R_0$.

\vspace{0.5em}

\alert{Respuesta correcta: 94 \%.}

# El umbral es una bifurcación

$$\dot I=\gamma(R_0-1)I \quad\text{al principio}$$

\centering
![](../figuras/fig_sir.pdf){width=100%}

# El sobrepaso

La epidemia deja de **crecer** cuando $S=1/R_0$.

Pero en ese instante todavía hay muchísima gente infecciosa.

\vspace{1em}

$$1-x=e^{-R_0 x}$$

| $R_0$ | Umbral de vacunación | Tamaño final |
|---|---|---|
| 1,5 | 33 % | **58 %** |
| 3,0 | 67 % | **94 %** |
| 5,0 | 80 % | **99 %** |

\vspace{0.5em}

\alert{Es la diferencia entre vacunar y dejar que pase. Y es dinámica, no
epidemiología.}

# Por qué extrapolan tan mal

En la fase inicial **todos los modelos son exponenciales**. Ajustan igual y
predicen picos que difieren en órdenes de magnitud.

\vspace{0.8em}

Tres razones por las que el SIR simple sobreestima:

* **Heterogeneidad** de contactos
* **Sobredispersión**: con $k=0{,}1$, el 80 % de los brotes se extingue solo
* **Cambio de comportamiento**: $\beta$ no es constante

\vspace{0.5em}

\alert{Sirven para entender mecanismos y comparar escenarios. No para predecir
números a dos meses.}

# Kermack y McKendrick, 1927

Antes: se creía que las epidemias terminaban porque **el patógeno perdía
virulencia**.

\vspace{1em}

Demostraron que no hace falta ninguna hipótesis sobre el patógeno: la epidemia
se apaga porque **se queda sin susceptibles**.

\vspace{1em}

\alert{Un modelo mínimo elimina la necesidad de un mecanismo postulado sin
evidencia.}

# Lo esencial

* $R_0=1$ es una bifurcación transcrítica
* La epidemia se pasa de frenada
* Un solo parámetro relevante al adimensionalizar
* En fase exponencial, los modelos no se distinguen
* $R_0$ no es una constante del patógeno
