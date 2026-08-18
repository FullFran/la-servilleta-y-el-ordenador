# III.9 — Cómo diseñar experimentos computacionales

---

## El problema

Tienes presupuesto para $N$ simulaciones y un espacio de parámetros. Cómo
gastes esas $N$ ejecuciones determina cuánto aprendes, y la diferencia entre un
diseño bueno y uno malo es de órdenes de magnitud.

Un barrido de parámetros **es** un diseño de experimentos, y tiene los mismos
principios que uno de laboratorio.

---

## Los seis pasos

### 1. La pregunta, con precisión

¿Qué quieres saber y con qué resolución? «Explorar el espacio de parámetros» no
es una pregunta. «¿Cuál de los cinco parámetros controla la aparición de la
inestabilidad, y dónde está el umbral con un 5 % de precisión?» sí.

### 2. Adimensionaliza

Antes de nada. Capítulos 2 y 16. Reduce la dimensión del espacio y evita
repetir casos físicamente idénticos.

### 3. Criba

Con 8 parámetros, no barras: **criba primero**. El método de Morris (efectos
elementales) identifica con ~100 evaluaciones cuáles son irrelevantes. Fíjalos
en su valor nominal y sigue con los que quedan.

Este paso ahorra órdenes de magnitud y casi nadie lo da.

### 4. Muestrea bien

Capítulo 16: hipercubo latino para exploración, secuencias de Sobol si vas a
calcular índices de sensibilidad, rejilla sólo con uno o dos parámetros cuando
quieras dibujar un mapa.

Y **nunca** una rejilla en más de tres dimensiones.

### 5. Replica lo estocástico

Si el modelo tiene ruido, cada punto necesita varias realizaciones. ¿Cuántas?
Estima primero $\sigma$ con unas pocas, y después calcula
$n=(\sigma/\text{precisión objetivo})^2$. Hacerlo al revés —fijar $n=10$ porque
sí— es tirar simulaciones o quedarse corto, y no se sabe cuál.

### 6. Analiza como analizarías un experimento real

Con barras de error, con análisis de sensibilidad, con residuos. Una simulación
no está exenta de estadística por ser determinista: en cuanto hay muestreo del
espacio de parámetros, hay incertidumbre.

---

## Los principios prestados del laboratorio

**Aleatorización.** Si ejecutas los casos en orden de parámetro creciente y hay
una deriva del sistema —una actualización de biblioteca, un cambio de máquina,
memoria que se degrada— el efecto se confunde con el parámetro. Ejecuta en
orden aleatorio.

**Bloqueo.** Si tienes que usar dos máquinas, reparte los casos de forma que la
máquina no esté confundida con ningún parámetro.

**Réplicas frente a repeticiones.** Una réplica es una ejecución independiente
completa; una repetición es medir dos veces lo mismo. Sólo la primera estima la
variabilidad real.

**Control.** Incluye siempre un caso cuya respuesta conoces, y ejecútalo mezclado
con los demás. Si sale mal, sabes que algo cambió a mitad del barrido.

---

## Diseño secuencial

El mejor diseño casi nunca se decide de una vez. La estrategia estándar:

1. **Exploración gruesa** con pocos puntos bien repartidos.
2. **Análisis de sensibilidad** para descartar parámetros.
3. **Refinamiento** en la región interesante.
4. Si hace falta, **diseño adaptativo**: elegir el siguiente punto donde el
   modelo sustituto tiene más incertidumbre o donde se espera más información.

Esa última técnica —optimización bayesiana, diseño secuencial— es
particularmente rentable cuando cada simulación es cara.

---

## Lista de comprobación

```text
DISEÑO DE EXPERIMENTO COMPUTACIONAL

□ ¿Cuál es la pregunta, con precisión objetivo?
□ ¿He adimensionalizado? ¿Cuántos parámetros quedan?
□ ¿He cribado para descartar parámetros irrelevantes?
□ ¿Uso hipercubo latino o Sobol, y no rejilla?
□ Si es estocástico: ¿he estimado σ antes de decidir el número de réplicas?
□ ¿Ejecuto en orden aleatorio?
□ ¿Hay un caso de control mezclado con los demás?
□ ¿He guardado la configuración exacta de cada ejecución?
□ ¿Voy a analizar esto con barras de error?
□ ¿Qué haré si el resultado es el contrario del esperado?
```

---

## Ejercicios de campo

**A.** Coge un barrido que hayas hecho. ¿Cuántos de sus puntos eran físicamente
distintos tras adimensionalizar? ¿Cuántos parámetros resultaron irrelevantes?

**B.** Diseña, sobre el papel, un experimento computacional con presupuesto de
200 ejecuciones para un modelo de 6 parámetros. Reparte las 200 entre las
cuatro fases.

**C.** Añade un caso de control a tu próximo barrido y ejecútalo cada 20
simulaciones. Comprueba que da siempre lo mismo.

---

### Referencias

* **Saltelli, A. et al.** *Global Sensitivity Analysis: The Primer.* Wiley,
  2008. Cribado de Morris e índices de Sobol.
* **Santner, T.; Williams, B.; Notz, W.** *The Design and Analysis of Computer
  Experiments.* 2.ª ed., Springer, 2018. **La referencia** del capítulo.
* **McKay, M.; Beckman, R.; Conover, W.** Technometrics **21** (1979). El
  hipercubo latino.
* **Box, G.; Hunter, J. S.; Hunter, W. G.** *Statistics for Experimenters.*
  2.ª ed., Wiley, 2005. Los principios de diseño experimental clásico, que se
  transfieren enteros.
