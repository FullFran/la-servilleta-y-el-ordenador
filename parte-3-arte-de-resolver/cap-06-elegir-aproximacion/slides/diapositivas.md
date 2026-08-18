---
title: "Cómo decidir qué aproximación usar"
subtitle: "Parte III · Manual de campo 6"
author: "La servilleta y el ordenador"
---

# Las seis aproximaciones básicas

| Aproximación | Cuándo | Se rompe si |
|---|---|---|
| Linealizar | cerca de un equilibrio | te alejas |
| Despreciar un término | cociente $\ll1$ | cambias de régimen |
| Promediar lo rápido | separación de tiempos | las escalas se acercan |
| Continuo | muchos elementos | quedan pocos |
| Estacionario | $t\gg\tau$ | miras el arranque |
| Homogéneo | mezcla rápida | hay gradientes |

# Cuatro criterios

1. **¿Cuánto error, comparado con mi objetivo?**
2. **¿Es controlable?** — con parámetro pequeño explícito
3. **¿Preserva lo que me importa?**
4. **¿Puedo comprobarla después?**

# El tercero es el que se olvida

Una aproximación puede ser numéricamente pequeña y destruir algo esencial:

* linealizar $\to$ adiós a los múltiples equilibrios
* promediar $\to$ adiós a la varianza, que a veces **es** la respuesta
* integrador no simpléctico $\to$ adiós a la conservación
* suponer normalidad $\to$ adiós a las colas

\vspace{0.8em}

\alert{Pregunta qué propiedad estructural pierdes, no sólo cuánto error
cometes.}

# Y el signo importa

Aproximaciones **independientes**: los errores se suman en cuadratura. Seis del
2 % $\to$ 5 %.

Aproximaciones **en el mismo sentido**: se suman linealmente. Seis del 2 %
$\to$ 12 %.

\vspace{1em}

Pregunta por el **signo** de cada una, no sólo por su magnitud.
