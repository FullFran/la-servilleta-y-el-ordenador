---
title: "Cuando el modelo miente"
subtitle: "Capítulo 15 · Cómo desconfiar del propio trabajo"
author: "La servilleta y el ordenador"
date: "Parte I — El instrumental del modelador"
---

# La pregunta

Tu modelo ajusta con $R^2=0{,}998$. Reproduce todas las observaciones. Tus
colegas están impresionados.

\vspace{1em}
\Large
**¿Cómo sabes si es correcto?**

\normalsize
\vspace{1em}
Respuesta honesta: con esa información, no puedes.

# La asimetría desagradable

\Large

Un modelo incorrecto **no da error**.

\normalsize
\vspace{0.8em}

No lanza excepciones. No avisa.

Da números plausibles con barras de error pequeñas.

\vspace{0.8em}

Y sólo el mundo real, a veces años después, desmiente.

# Seis modos de mentir

| Modo | Diagnóstico |
|---|---|
| Sobreajuste | validación con datos nuevos |
| No identificabilidad | perfiles de verosimilitud |
| Mala especificación | residuos, predicciones cualitativas |
| Extrapolación | comparar varios modelos fuera |
| Confusión causal | diagrama causal, experimento |
| Artefacto numérico | convergencia, invariancias |

\vspace{0.5em}

\alert{Ninguno se detecta mirando el ajuste.}

# Sobreajuste

\centering
![](../figuras/fig_sobreajuste.pdf){width=100%}

| Grado | Sobre los 14 datos | Sobre datos nuevos |
|---|---|---|
| 4 | 0,236 | **0,286** |
| 12 | **0,033** | **785,9** |

# Extrapolación

\centering
![](../figuras/fig_extrapolacion.pdf){width=100%}

\raggedright\small
Mismos datos, ajustes comparables. En $t=40$: $1{,}6\times10^3$,
$5{,}5\times10^4$, $4{,}3\times10^7$.

# La regla

\Large

Toda extrapolación es una afirmación sobre **física**, no sobre datos.

\normalsize
\vspace{1em}

Si no puedes justificar el mecanismo fuera del rango medido, no puedes
extrapolar.

\vspace{0.8em}

Y si extrapolas: hazlo con **varios modelos plausibles** y reporta el rango
completo. Esa banda es la incertidumbre honesta, y siempre es mucho mayor que
la de la covarianza.

# Sensibilidad: local engaña

\centering
![](../figuras/fig_sensibilidad.pdf){width=100%}

\raggedright\small
Derivada parcial de $b$: **exactamente cero**. Índice de Sobol de $b$: **0,24**.

# Confusor y colisionador exigen lo contrario

**Confusor**: $Z\to X$, $Z\to Y$.
Helados y ahogamientos, con el calor detrás.
$\Rightarrow$ **hay que controlar por $Z$**

\vspace{0.8em}

**Colisionador**: $X\to Z$, $Y\to Z$.
Entre los admitidos, notas y deporte anticorrelacionan.
$\Rightarrow$ **controlar por $Z$ es exactamente lo que NO hay que hacer**

\vspace{0.8em}

\alert{«Controlar por todo lo que tengas» es una receta incorrecta.}

# Antes de creerte un resultado numérico

1. Reduce el paso a la mitad
2. Cambia de método
3. Comprueba las conservaciones
4. Comprueba las invariancias (unidades, ejes, orden)
5. Cambia la semilla
6. Ejecuta el caso trivial con solución conocida

\vspace{0.8em}

Cuestan minutos.

\vspace{0.3em}

\alert{La resistencia a hacerlos es psicológica: nadie quiere someter a prueba
un resultado bonito.}

# Cuatro casos

**Millikan** — la carga del electrón subió poco a poco durante años. Nadie
mintió: el procedimiento de búsqueda de errores era asimétrico.

**Rayos N, 1903** — 300 artículos. Wood retiró el prisma y el experimentador
siguió viendo líneas.

**Kelvin** — cálculo impecable, física ausente. La incertidumbre estaba en la
**lista de mecanismos**, no en los parámetros.

**OPERA, 2011** — 6 sigmas y un conector de fibra flojo.

# Y la lección de OPERA

\Large

**Seis sigmas estadísticas no protegen de un error sistemático.**

\normalsize
\vspace{1em}

La barra de error sólo cubre lo que has modelado.

\vspace{0.5em}

Un cable flojo no está en ninguna matriz de covarianza.

\vspace{1em}
\small
Nota justa: OPERA publicó como **anomalía sin explicación** pidiendo
verificación independiente. Se comportaron bien.

# La prueba que mataría tu modelo

1. Escribe la predicción más **arriesgada** que hace
2. Comprueba que es falsable
3. Estima cuántos datos harían falta
4. **Preregistra el criterio de abandono**
5. Hazla
6. Publica el resultado sea cual sea

\vspace{0.8em}

\alert{El paso 4 es el que más duele y el que más vale.}

# Lo esencial

* Un modelo incorrecto no da error
* El error de entrenamiento mide flexibilidad, no calidad
* Extrapolar es afirmar física
* La sensibilidad local sólo vale si el modelo es casi lineal
* Controlar por un colisionador **crea** sesgo
* La incertidumbre dominante está en la **estructura**, y ninguna barra de
  error la cubre

# Para llevarse a casa

\Large

Antes de creerte tu propio resultado:

\vspace{0.5em}

**¿Qué observación lo mataría, y la he hecho?**

\vspace{1.2em}

\normalsize
Pregunta abierta: si un modelo mal especificado predice bien, ¿es útil?
¿Es ciencia?
