# III.3 — Cómo construir un modelo mínimo

---

## El problema

«Lo más simple que podría funcionar» es un criterio precioso y vacío hasta que
se convierte en procedimiento. Este capítulo lo convierte.

---

## La definición operativa

Un modelo es mínimo si **quitarle cualquier ingrediente lo rompe**.

Esa definición es comprobable: para cada término, quítalo y mira si la
predicción que te importa cambia más que tu precisión objetivo. Si no cambia,
sobraba.

Es exactamente un análisis de sensibilidad, y se puede hacer antes de tener
datos.

---

## El procedimiento

### 1. Empieza por el modelo más estúpido que se te ocurra

En serio. Una constante. Una proporcionalidad. Un solo mecanismo.

La razón no es pedagógica: es que **el modelo estúpido establece la línea
base**. Si tu modelo elaborado no la bate claramente, no has ganado nada, y con
frecuencia no la bate.

En predicción de series, la línea base es «mañana como hoy». En clasificación,
«siempre la clase mayoritaria». En modelado físico, «proporcional a la variable
obvia». Sorprende cuántos trabajos publicados no la reportan.

### 2. Añade un ingrediente cada vez

Y para cada uno, **antes de añadirlo**, escribe:

* qué fenómeno observado no explica el modelo actual;
* qué predicción nueva hace el ingrediente;
* cómo se falsaría.

Si no puedes escribir las tres, no lo añadas.

### 3. Para cuando los residuos sean ruido

Capítulo 14: residuos del tamaño del error de medida **y sin estructura**. Las
dos condiciones.

### 4. Vuelve a quitar

El paso que nadie hace. Una vez que funciona, quita ingredientes uno a uno y
comprueba si alguno ha dejado de hacer falta. Es frecuente que un término
añadido pronto se vuelva redundante cuando se añade otro después.

---

## Las cuatro tentaciones

**Añadir realismo.** «Ya que estamos, incluyamos también…». Cada término
adicional debe justificarse por una predicción, no por fidelidad a la realidad.
Un mapa a escala 1:1 es inútil.

**Añadir generalidad.** Hacer el modelo para el caso general antes de resolver
el particular. Casi siempre es más lento y a veces imposible.

**Añadir parámetros para ajustar mejor.** Capítulo 15. Bajar el $\chi^2$
añadiendo libertad no es progreso.

**Copiar la complejidad del vecino.** «Todo el mundo en este campo usa el modelo
de N compartimentos.» Puede que todo el mundo esté arrastrando complejidad
heredada que nadie ha vuelto a justificar.

---

## Qué hace bueno a un modelo mínimo

No es que acierte. Es que **falla de forma informativa**.

Un modelo mínimo correcto tiene tres propiedades:

* Sus supuestos son explícitos y comprobables.
* Cuando falla, la forma del fallo apunta al mecanismo que falta.
* Se puede entender entero, y por tanto se puede criticar.

Un modelo de 40 parámetros que ajusta bien no tiene ninguna de las tres.

---

## Lista de comprobación

```text
MODELO MÍNIMO

□ ¿Cuál es mi línea base estúpida, y la he calculado?
□ ¿Bate mi modelo a la línea base, y por cuánto?
□ Para cada ingrediente:
    □ ¿qué observación no explicaba el modelo sin él?
    □ ¿qué predicción nueva hace?
    □ ¿cómo se falsaría?
□ ¿He quitado cada término y comprobado que hace falta?
□ ¿Son los residuos del tamaño del ruido Y sin estructura?
□ ¿Puedo explicar el modelo entero en cinco minutos?
□ ¿Cuántos datos tengo por parámetro?
□ ¿He vuelto a quitar después de terminar?
```

---

## Ejercicios de campo

**A.** Coge tu modelo actual y quita, uno a uno, cada término. Documenta cuánto
empeora la predicción que te importa. Los que no empeoren nada, fuera.

**B.** Calcula la línea base estúpida de un problema de tu trabajo. ¿Cuánto la
bate el modelo que estás usando?

**C.** Modela un fenómeno cotidiano con un modelo deliberadamente demasiado
simple. Documenta **cómo** falla, y comprueba si la forma del fallo apunta al
mecanismo ausente.

---

### Referencias

* **Box, George E. P.** *Science and Statistics.* JASA **71** (1976). Sobre la
  parsimonia y la sobreelaboración.
* **Edelstein-Keshet, Leah.** *Mathematical Models in Biology.* SIAM, 2005.
* **Burnham, K. y Anderson, D.** *Model Selection and Multimodel Inference.*
  2.ª ed., Springer, 2002. AIC y parsimonia, con criterio.
* **Gelman, Andrew y Shalizi, Cosma.** *Philosophy and the practice of Bayesian
  statistics.* Br. J. Math. Stat. Psychol. **66** (2013), 8–38. Sobre construir
  modelos por iteración crítica en lugar de por selección.
