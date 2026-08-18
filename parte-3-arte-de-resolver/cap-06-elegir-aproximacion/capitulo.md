# III.6 — Cómo decidir qué aproximación utilizar

---

## El problema

Aproximar no es opcional: todo modelo aproxima. Lo que se decide es **cuál**, y
esa decisión tiene criterios.

---

## Las seis aproximaciones básicas, y cuándo usar cada una

| Aproximación | Se usa cuando | Error típico | Se rompe si |
|---|---|---|---|
| **Linealizar** | estás cerca de un equilibrio | $\mathcal{O}(\delta^2)$ | te alejas o hay bifurcación |
| **Despreciar un término** | hay un cociente $\ll1$ | del orden del cociente | cambias de régimen, o es singular |
| **Promediar la escala rápida** | hay separación de tiempos | $\mathcal{O}(\tau_r/\tau_l)$ | las escalas se acercan |
| **Continuo en lugar de discreto** | hay muchos elementos | $\mathcal{O}(1/\sqrt N)$ | quedan pocos |
| **Estacionario en lugar de transitorio** | observas $t\gg\tau$ | despreciable | miras el arranque |
| **Homogéneo en lugar de espacial** | mezcla rápida | según el Péclet | hay gradientes |

Esta tabla es el resumen operativo de los capítulos 6, 7 y 13, y merece tenerla
a mano.

---

## Los cuatro criterios de decisión

### 1. ¿Cuánto error introduce, comparado con mi objetivo?

Si tu precisión objetivo es del 10 % y la aproximación introduce un 2 %, es
buena. Si introduce un 15 %, no lo es. **La misma aproximación puede ser
excelente o inaceptable según la pregunta**, y por eso la precisión objetivo se
declara en el paso 1 del ciclo.

### 2. ¿Es controlable?

Una buena aproximación viene con una estimación de su error y un parámetro que
lo controla. «Despreciamos la viscosidad porque $Re=10^6$» es controlable.
«Usamos un factor de corrección de 1,3 obtenido empíricamente» no lo es.

Prefiere siempre aproximaciones controlables, aunque sean menos precisas: se
pueden mejorar y se pueden auditar.

### 3. ¿Preserva lo que me importa?

Una aproximación puede ser numéricamente pequeña y destruir una propiedad
esencial. Ejemplos:

* Linealizar destruye la posibilidad de múltiples equilibrios.
* Promediar destruye la varianza, que a veces **es** la respuesta.
* Un integrador no simpléctico destruye la conservación (capítulo II.6).
* Suponer normalidad destruye las colas, que a veces son el objeto de estudio.

**Pregunta siempre qué propiedad estructural se pierde**, no sólo cuánto error
se comete.

### 4. ¿Puedo comprobarla después?

Una aproximación que se puede verificar *a posteriori* —sustituyendo la
solución, comparando con un caso resuelto, midiendo— vale mucho más que una que
hay que creerse.

---

## El error de las aproximaciones sucesivas

Cuando se encadenan varias, los errores se combinan. Y hay dos casos muy
distintos:

* **Independientes:** los errores se suman en cuadratura, como en el capítulo 1.
  Seis aproximaciones del 2 % dan un 5 %.
* **Correlacionados o en el mismo sentido:** se suman linealmente. Seis del 2 %
  dan un 12 %.

Y el caso peligroso: **aproximaciones que se refuerzan**. Si linealizas y además
promedias, y ambas cosas sesgan hacia abajo, el error total puede ser mayor que
la suma. Merece la pena preguntarse por el **signo** de cada aproximación, no
sólo por su magnitud.

---

## Lista de comprobación

```text
ELEGIR APROXIMACIÓN

□ ¿Cuál es mi precisión objetivo?
□ ¿Qué error introduce esta aproximación, en números?
□ ¿Cuál es el parámetro pequeño que la controla, y cuánto vale?
□ ¿Qué propiedad estructural pierdo (equilibrios, varianza, conservación,
  colas)?
□ ¿Puedo comprobarla a posteriori? ¿Cómo?
□ Si encadeno varias: ¿son independientes o van en el mismo sentido?
□ ¿He escrito en el margen el rango de validez de cada una?
□ ¿Sigue siendo válido ese rango en el régimen en que voy a usarla?
```

---

## Ejercicios de campo

**A.** Lista todas las aproximaciones de un modelo tuyo. Para cada una: el
parámetro pequeño, su valor y el error estimado. Suma.

**B.** Encuentra en tu modelo una aproximación que destruya una propiedad
estructural, no sólo precisión. ¿Importa?

**C.** Toma un modelo con tres aproximaciones y calcula el error total
suponiendo independencia y suponiendo que van en el mismo sentido. ¿Cuánto
difieren?

---

### Referencias

* **Bender, C. M. y Orszag, S. A.** *Advanced Mathematical Methods.* 1978.
* **Hinch, E. J.** *Perturbation Methods.* Cambridge UP, 1991.
* **Segel, L. A. y Slemrod, M.** *The Quasi-Steady-State Assumption.* SIAM
  Review **31** (1989). Un caso trabajado de aproximación con su error acotado.
