# III.4 — Cómo encontrar la escala correcta

---

## El problema

Casi todo error de modelado grave es un error de escala: usar una ecuación
fuera de su rango, despreciar algo que dominaba, o refinar donde no importaba.

Encontrar las escalas de un problema **antes** de resolverlo es la operación
con mejor relación beneficio/esfuerzo de todo este libro.

---

## Las cinco escalas que hay que buscar siempre

### 1. Escala de longitud

¿Cuál es el tamaño característico? ¿Y hay más de uno? Si hay dos muy distintos,
casi seguro hay una capa límite (capítulo 13) o una separación de escalas
explotable.

Pregunta operativa: **¿sobre qué distancia cambia apreciablemente la magnitud
que me interesa?**

### 2. Escala de tiempo

Igual. ¿Cuánto tarda el sistema en olvidar su condición inicial? Con varios
tiempos característicos muy distintos, el rápido se elimina y el lento manda
(capítulo 6).

Pregunta operativa: **¿cuánto tengo que esperar para ver algo cambiar?**

### 3. Escala de energía

¿Cuál es la energía típica del proceso? Comparada con $kT$ decide si las
fluctuaciones térmicas importan; comparada con la barrera decide si el sistema
la cruza; comparada con la de enlace decide si algo se rompe.

### 4. Escala de la magnitud de salida

¿Cuál es el valor típico de lo que quieres calcular? Sin él, no puedes juzgar
si un resultado es razonable ni cuánta precisión necesitas.

### 5. Escala de la incertidumbre

¿Cuánto vale la barra de error de lo que puedes medir? Determina qué modelos se
pueden distinguir (capítulo 14) y dónde merece la pena refinar.

---

## Cómo se encuentran

**Adimensionalizando.** Capítulo 2. Es el método sistemático: escribe las
ecuaciones, sustituye cada variable por su valor típico multiplicado por una
adimensional, y las escalas aparecen solas como los factores que hacen los
coeficientes iguales a 1.

**Igualando términos.** El balance dominante del capítulo 13. Si dos términos
se equilibran, la escala es la que los iguala.

**Preguntando por el mecanismo.** ¿Qué distancia recorre una molécula antes de
chocar? ¿Cuánto tarda una perturbación en cruzar el sistema? A menudo la escala
tiene una interpretación física directa y se puede estimar sin ecuaciones.

**Mirando los datos.** Si tienes una serie, su autocorrelación da el tiempo
característico; su espectro, las frecuencias dominantes; su variograma, la
escala espacial.

---

## La pregunta que resuelve casi todo

Una vez tienes dos escalas, la pregunta operativa es siempre la misma:

> ¿Cuál es el cociente, y es grande, pequeño o de orden 1?

* **Grande o pequeño:** hay un parámetro pequeño y se puede aproximar
  (capítulo 13). El problema es tratable.
* **De orden 1:** no hay simplificación posible y hay que calcular. Ese es el
  régimen difícil, y merece la pena reconocerlo pronto para no perder tiempo
  buscando una aproximación que no existe.

---

## Lista de comprobación

```text
ESCALAS

□ ¿Cuál es la longitud característica? ¿Hay más de una?
□ ¿Cuál es el tiempo característico? ¿Hay más de uno?
□ ¿Cuál es la energía típica, comparada con kT y con la barrera?
□ ¿Cuál es el valor típico de la salida?
□ ¿Cuál es mi incertidumbre experimental?
□ ¿He adimensionalizado y mirado qué grupos π quedan?
□ Para cada par de escalas: ¿el cociente es grande, pequeño o de orden 1?
□ ¿Estoy operando dentro del rango de validez de las aproximaciones que uso?
□ ¿He comprobado que sigo estando ahí después de cambiar de régimen?
```

---

## Ejercicios de campo

**A.** Para un sistema de tu trabajo, escribe las cinco escalas. Si no puedes
escribir alguna, ahí está tu siguiente pregunta.

**B.** Toma un modelo que uses y localiza el cociente de escalas que justifica
cada aproximación. ¿Sigue siendo pequeño en tu régimen actual?

**C.** Coge tres fenómenos de tu entorno y estima sus tiempos característicos
sin calcular nada. Después compruébalos.

---

### Referencias

* **Barenblatt, G. I.** *Scaling.* Cambridge UP, 2003.
* **Bender, C. M. y Orszag, S. A.** *Advanced Mathematical Methods.* 1978,
  capítulo 3.
* **Mahajan, Sanjoy.** *The Art of Insight.* MIT Press, 2014, partes II y III.
* **Vogel, Steven.** *Comparative Biomechanics.* 2.ª ed., Princeton UP, 2013.
  Escalas y regímenes en sistemas vivos, con muchos ejemplos.
