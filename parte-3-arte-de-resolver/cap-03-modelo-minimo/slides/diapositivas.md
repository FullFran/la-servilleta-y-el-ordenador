---
title: "Cómo construir un modelo mínimo"
subtitle: "Parte III · Manual de campo 3"
author: "La servilleta y el ordenador"
---

# La definición operativa

\Large
Un modelo es mínimo si **quitarle cualquier ingrediente lo rompe**.

\normalsize
\vspace{1em}

Y eso es comprobable: quita cada término y mira si la predicción que te importa
cambia más que tu precisión objetivo.

# El procedimiento

1. **Empieza por el modelo más estúpido** — establece la línea base
2. **Añade un ingrediente cada vez** — con las tres preguntas
3. **Para cuando los residuos sean ruido** — y sin estructura
4. **Vuelve a quitar** — el paso que nadie hace

# Las tres preguntas, antes de añadir

* ¿Qué fenómeno observado **no** explica el modelo actual?
* ¿Qué predicción nueva hace este ingrediente?
* ¿Cómo se falsaría?

\vspace{1em}

\alert{Si no puedes escribir las tres, no lo añadas.}

# Las cuatro tentaciones

* **Añadir realismo** — un mapa 1:1 es inútil
* **Añadir generalidad** — resuelve el particular primero
* **Añadir parámetros** — bajar $\chi^2$ con libertad no es progreso
* **Copiar la complejidad del vecino** — puede ser complejidad heredada que
  nadie ha vuelto a justificar

# Qué hace bueno a un modelo mínimo

No es que acierte. Es que **falla de forma informativa**.

\vspace{1em}

* supuestos explícitos y comprobables
* la forma del fallo apunta al mecanismo que falta
* se puede entender entero, y por tanto criticar

\vspace{0.8em}

Un modelo de 40 parámetros que ajusta bien no tiene ninguna de las tres.
