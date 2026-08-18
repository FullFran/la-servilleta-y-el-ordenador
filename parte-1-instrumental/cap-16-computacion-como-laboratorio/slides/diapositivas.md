---
title: "Computación como laboratorio"
subtitle: "Capítulo 16 · El ordenador como instrumento"
author: "La servilleta y el ordenador"
date: "Parte I — El instrumental del modelador"
---

# La pregunta

1953, Los Álamos. Tres físicos y una programadora simulan una cadena de
osciladores ligeramente no lineales.

Esperan el resultado más seguro de la física estadística: equipartición.

\vspace{1em}
\Large
**No ocurre. ¿Qué haces cuando el ordenador contradice algo de lo que estabas
seguro?**

# Simular no es experimentar ni demostrar

**No es un experimento** — interroga a tu modelo, no a la naturaleza

**No es una demostración** — mil casos no son un teorema

**Sí es un instrumento** — para ver lo irresoluble, generar hipótesis y, sobre
todo, **falsar intuiciones**

# El patrón

```text
hipótesis → predicción escrita → simulación
   → observación → explicación → nueva hipótesis
```

\vspace{1em}

La diferencia con «ejecutar y mirar la gráfica» son dos puntos:

* **predicción escrita** antes de ejecutar
* **explicación** antes de pasar a lo siguiente

\vspace{0.5em}

\alert{Sin lo primero, cualquier resultado parece razonable a posteriori.
Sin lo segundo, acumulas gráficas y no conocimiento.}

# FPU, reproducido

\centering
![](../figuras/fig_fpu.pdf){width=100%}

\raggedright\small
93,7 % de la energía vuelve al modo 1. El 80 % sigue en los tres primeros
modos, frente al 9 % de la equipartición.

# Lo importante no es el resultado

Fermi, Pasta, Ulam y Tsingou **no** publicaron un artículo triunfal.

Escribieron un informe interno diciendo que el resultado era sorprendente y no
tenían explicación.

\vspace{1em}

De ahí salieron:

* los **solitones** (Zabusky y Kruskal, 1965) $\to$ fibra óptica
* la teoría **KAM**
* el estudio del caos hamiltoniano

\vspace{0.5em}

\alert{Un experimento numérico que falló abrió más ciencia que mil que
confirman.}

# Adimensionaliza antes de barrer

6 parámetros dimensionales $\to$ 2 grupos $\pi$

\vspace{0.5em}

Rejilla de 10 puntos por eje: $10^6$ frente a $10^2$ simulaciones.

\vspace{1em}
\Large

**Cuatro órdenes de magnitud por veinte minutos de álgebra.**

# Y la rejilla es peor de lo que parece

\centering
![](../figuras/fig_muestreo_parametros.pdf){width=100%}

\raggedright\small
25 simulaciones: la rejilla prueba **5** valores distintos de cada parámetro.
El hipercubo latino, **25**.

# Reproducibilidad: el mínimo

1. Semilla fija y explícita
2. Versiones registradas
3. Parámetros en un fichero, no dispersos
4. Un script por figura, sin pasos manuales
5. Datos intermedios con su configuración
6. Control de versiones

\vspace{0.8em}

\alert{Un resultado que sólo existe en la carpeta de descargas de alguien es un
rumor.}

# Probar código científico

`assert resultado > 0` no es una prueba.

\vspace{0.8em}

* **Soluciones analíticas** en casos límite
* **Orden de convergencia** — detecta la mitad de los errores
* **Soluciones manufacturadas** — interior **y** bordes
* **Invariancias**: unidades, rotación, orden, inversión temporal
* **Casos degenerados** — un elemento, tiempo cero, parámetro nulo
* **Regresión** — guarda la salida de un caso pequeño

# Dos formas de visualizar

**Para descubrir**: rápido, feo, mucho de todo. Que algo te llame la atención.

**Para comunicar**: una figura, una pregunta, unidades, anotación.

\vspace{1em}

\alert{El error habitual es publicar la primera. Una figura de descubrimiento
tiene seis paneles porque el autor no sabía qué buscaba.}

# La señora del MANIAC

El informe firma Fermi, Pasta y Ulam. En los agradecimientos:
«la eficiente cooperación de la señora Mary Tsingou».

\vspace{0.8em}

Durante cincuenta años se llamó FPU. Desde Dauxois (2008), cada vez más
**FPUT**.

\vspace{0.8em}

Programar en 1954: diseñar el flujo de operaciones sin lenguaje de alto nivel,
gestionar la precisión y decidir cómo comprobar que no era un error de la
máquina.

\vspace{0.3em}

\alert{Es decir: parte sustancial del diseño del experimento.}

# Lo esencial

* Una simulación sirve para falsar intuiciones
* Predicción escrita antes; explicación después
* Adimensionaliza antes de barrer
* Hipercubo latino, no rejilla
* Semilla, versiones, un script por figura
* Prueba con soluciones conocidas y órdenes de convergencia
* El resultado que no esperabas es el valioso

# Para llevarse a casa

\Large

Antes de lanzar cualquier simulación:

\vspace{0.5em}

**¿Qué espero que ocurra, y qué haría si no ocurre?**

\vspace{1.2em}

\normalsize
Pregunta abierta: ¿cuándo constituye una simulación evidencia, y de qué
exactamente?
