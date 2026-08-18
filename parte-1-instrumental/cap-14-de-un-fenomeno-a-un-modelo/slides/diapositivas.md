---
title: "De un fenómeno a un modelo"
subtitle: "Capítulo 14 · El taller"
author: "La servilleta y el ordenador"
date: "Parte I — El instrumental del modelador"
---

# La pregunta

Te dan un fenómeno sin ecuaciones: **una taza de café se enfría**.

Nadie te dice qué modelo usar, qué variables importan, ni qué precisión hace
falta.

\vspace{1em}
\Large
**¿Por dónde empiezas?**

\normalsize
\vspace{1em}
Trece capítulos de herramientas. Este es el procedimiento.

# El ciclo entero

\centering
![](../figuras/fig_ciclo.pdf){width=100%}

# Dos observaciones sobre el diagrama

**El bucle rojo.** Cuando el modelo falla, el reflejo es revisar las ecuaciones.
Casi nunca es eso: la flecha va **a los supuestos**.

\vspace{1em}

**El bucle ocre casi nadie lo dibuja.** El número que sale del ordenador se
compara con la estimación del principio. Si no coinciden, uno está mal y hay que
saber cuál **antes** de seguir.

\vspace{0.5em}

\alert{Ese contraste es gratis y es el detector de errores más eficaz que
existe.}

# La pregunta lleva una precisión

«¿Cuánto tarda en enfriarse?» no es una pregunta: es un tema.

\vspace{1em}

> ¿Cuánto tarda un café de 92 °C en llegar a 60 °C, **con un error menor de dos
> minutos**?

\vspace{1em}

Con media hora de tolerancia sirve el modelo más burdo. Con dos minutos, no.

\vspace{0.5em}

\alert{Sin precisión declarada no hay criterio de parada.}

# La lista de descartes es donde se decide el modelo

| Descartada | Por qué |
|---|---|
| Forma exacta de la taza | entra sólo por $A$ |
| Material | capacidad térmica $\sim10\,\%$ de la del café |
| Color | afecta a radiación, estimada en 20 % |
| Presión | irrelevante salvo en altura |
| **Agitación** | **no descartada**: cambia $h$ por 3 |

\vspace{0.5em}

La última fila es la que importa: ahí aparecen las variables que hay que
**controlar en el experimento**.

# El modelo mínimo, y lo que deja fuera

\centering
![](../figuras/fig_cafe_progresivo.pdf){width=100%}

\raggedright\small
Newton: $\tau = 26{,}3$ min, rms 0,79 °C. Ruido de medida: 0,35 °C.
**Y los residuos tienen forma.**

# El diagnóstico

Los residuos dicen: el enfriamiento inicial es **más rápido** de lo que predice
Newton.

\vspace{0.8em}

¿Qué crece con $\Delta T$ más deprisa que linealmente?

* **Radiación**: $T^4 - T_a^4$ — unos 19 W a 92 °C
* **Evaporación**: presión de vapor exponencial — unos 30 W a 92 °C

\vspace{0.8em}

\alert{Los dos ajustan igual. Con estos datos **no se pueden separar**.}

# Y por eso vas a buscar una balanza

Para separarlos no hace falta un ajuste mejor: hace falta **otro experimento**.

\vspace{1em}

* Pesar la taza: la evaporación quita masa, la radiación no
* Poner tapa: elimina evaporación, apenas toca la radiación

\vspace{1em}

8 g perdidos en 2 h $\times$ 2,4 MJ/kg = 19 kJ, el **26 %** del calor total.

\vspace{0.5em}

Cinco euros de báscula cierran el caso.

# Cuándo parar

\Large

Deja de añadir complejidad cuando los residuos sean del tamaño del ruido
**y** no tengan estructura.

\normalsize
\vspace{1em}

Corolario incómodo: si tus datos son ruidosos, **no puedes distinguir
modelos**.

\vspace{0.5em}

Mejorar la medida es a menudo más rentable que mejorar el modelo. Esa decisión
es parte del modelado.

# Tres palabras que no son sinónimos

**Verificación** — ¿resuelvo bien mis ecuaciones?

**Calibración** — ¿qué parámetros ajustan estos datos?

**Validación** — ¿predice datos que **no** he usado?

\vspace{1em}

\alert{Sólo la tercera autoriza a usar el modelo para decidir algo.}

\vspace{0.5em}
\small
Un modelo de 40 parámetros con 3 % de error sobre sus propios datos de
calibración no ha demostrado nada.

# Kepler, ocho minutos de arco

Ocho años ajustando la órbita de Marte con círculos. Llega a un error de
**8 minutos de arco**: mejor que casi cualquier observación anterior a Tycho.

\vspace{1em}

No lo publica. Porque **sabía que los datos de Tycho eran mejores que eso**.

\vspace{1em}

\alert{Trató una discrepancia que cualquiera habría llamado error de medida
como información. De ahí salieron las elipses.}

\vspace{0.5em}
\small
Para eso no hace falta más matemática: hace falta conocer la incertidumbre de
tus datos mejor que nadie.

# Lo esencial

* La pregunta lleva una precisión declarada
* La estimación previa es el patrón de juicio
* Los descartes, con motivo escrito
* Empieza por el modelo mínimo
* Residuos con forma = falta física
* Si dos mecanismos ajustan igual: **otro experimento**
* Calibrar no es validar

# Para llevarse a casa

\Large

Ante cualquier fenómeno nuevo:

\vspace{0.5em}

**¿Qué quiero saber, con qué precisión,
y cuál es el modelo más simple que podría bastar?**

\vspace{1.2em}

\normalsize
Pregunta abierta: si dos modelos con mecanismos distintos ajustan igual de
bien, ¿en qué sentido uno es mejor?
