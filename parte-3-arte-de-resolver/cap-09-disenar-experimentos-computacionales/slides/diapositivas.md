---
title: "Cómo diseñar experimentos computacionales"
subtitle: "Parte III · Manual de campo 9"
author: "La servilleta y el ordenador"
---

# Un barrido **es** un diseño de experimentos

Y tiene los mismos principios que uno de laboratorio.

\vspace{1em}

Cómo gastes tus $N$ ejecuciones determina cuánto aprendes, y la diferencia
entre un diseño bueno y uno malo es de **órdenes de magnitud**.

# Los seis pasos

1. **La pregunta**, con precisión objetivo
2. **Adimensionaliza** — antes de nada
3. **Criba** — Morris, ~100 evaluaciones, descarta irrelevantes
4. **Muestrea bien** — hipercubo latino o Sobol, nunca rejilla en $d>3$
5. **Replica** — estima $\sigma$ **antes** de decidir $n$
6. **Analiza como un experimento real** — barras de error incluidas

# Prestado del laboratorio

**Aleatorización** — si ejecutas en orden de parámetro y el sistema deriva, el
efecto se confunde

**Bloqueo** — que la máquina no esté confundida con ningún parámetro

**Réplicas $\neq$ repeticiones** — sólo la primera estima variabilidad

**Control** — un caso de respuesta conocida, mezclado con los demás

# Diseño secuencial

1. Exploración gruesa
2. Análisis de sensibilidad
3. Refinamiento donde importa
4. Diseño adaptativo si cada simulación es cara

\vspace{1em}

El mejor diseño casi nunca se decide de una vez.
