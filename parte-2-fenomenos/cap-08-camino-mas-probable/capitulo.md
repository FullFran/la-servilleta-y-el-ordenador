# II.8 — ¿Cómo encontramos el camino más probable?

> **El fenómeno:** la luz se dobla al entrar en el agua; el GPS te da una ruta;
> una pelota describe una parábola.
> **Herramientas:** cap. 3 (probabilidad), cap. 9 (muestreo), cap. 10
> (optimización).
> **Lo que hay que llevarse:** que «minimizar algo a lo largo de un camino» es
> una estructura que aparece en óptica, mecánica, logística y probabilidad, y
> que la misma matemática resuelve las cuatro.

---

## 1. Una pregunta

::: pregunta
Un socorrista está en la arena y ve a alguien en el agua, en diagonal. Corre a
5 m/s y nada a 1,5 m/s.

**¿Por dónde debe entrar al agua?**

No por la línea recta. Y el punto óptimo cumple exactamente la ley de Snell.
:::

---

## 2. Antes de calcular

::: antes
1. ¿Entrará el socorrista antes o después del punto de la línea recta?
2. ¿Qué tienen en común la refracción, un GPS y una trayectoria balística?
3. ¿Por qué la naturaleza «minimizaría» algo?
:::

---

## 3. La misma estructura, tres veces

![Tres problemas con la misma forma. Izquierda: el socorrista, cuyo óptimo cumple $\sin\theta_1/\sin\theta_2 = v_1/v_2 = 3{,}333$. Centro: camino más corto en una red, resuelto con Dijkstra. Derecha: la acción de una trayectoria deformada, estacionaria exactamente en la trayectoria física. Lo que hay que concluir: son el mismo problema matemático con tres vestidos.](figuras/fig_caminos.pdf)

Los tres consisten en **minimizar una suma a lo largo de un camino**:

$$\text{coste}=\int_{\text{camino}} L\,ds \qquad\text{o}\qquad
\sum_{\text{aristas}} w_{ij}$$

* **Fermat:** $L=1/v$, y minimizar el tiempo da la ley de Snell. La simulación
  reproduce $\sin\theta_1/\sin\theta_2=v_1/v_2$ con cuatro cifras.
* **Dijkstra:** $w_{ij}$ es la longitud de la arista, y el algoritmo encuentra
  el mínimo en tiempo $\mathcal{O}(E\log V)$ sin explorar todos los caminos.
* **Mecánica:** $L=T-V$ es el lagrangiano, y la trayectoria física hace la
  acción **estacionaria**. La simulación lo confirma: el mínimo está en
  $\alpha=1{,}003$.

---

## 4. Y la versión probabilística

Aquí está la conexión que da título al capítulo.

Si a cada camino se le asigna una probabilidad $P\propto e^{-S/\epsilon}$ con
$S$ el coste y $\epsilon$ pequeño, entonces **el camino más probable es el de
coste mínimo**, y la probabilidad se concentra a su alrededor con anchura
$\sqrt\epsilon$.

Es exactamente la relación entre Boltzmann y optimización del capítulo 10, y
aparece en tres sitios distintos:

* **Mecánica cuántica.** Feynman: la amplitud es $\sum_{\text{caminos}}
  e^{iS/\hbar}$. En el límite $\hbar\to0$, la interferencia destruye todo salvo
  el entorno del camino estacionario, y reaparece la mecánica clásica.
* **Procesos estocásticos.** La teoría de grandes desviaciones
  (Freidlin–Wentzell) da la probabilidad de una trayectoria rara como
  $e^{-S/\epsilon}$ con $S$ una acción. El camino más probable para una
  transición rara —el *instantón*— es un problema variacional.
* **Inferencia.** El camino de máxima verosimilitud en un modelo oculto de
  Markov se calcula con el algoritmo de Viterbi, que es **programación
  dinámica**: exactamente Dijkstra en un grafo de estados y tiempos.

**Cuatro campos, una estructura.** Y los algoritmos se transfieren: Viterbi y
Dijkstra son el mismo esquema, y la aproximación de punto de silla en física es
la misma idea que la aproximación de Laplace en estadística.

---

## 5. Programación dinámica: por qué no hay que explorar todos los caminos

El número de caminos en una red crece exponencialmente. La razón por la que se
pueden encontrar mínimos sin explorarlos todos es el **principio de
optimalidad** de Bellman:

> Cualquier tramo final de un camino óptimo es a su vez óptimo.

Eso permite construir la solución hacia atrás, guardando sólo el mejor camino
hasta cada nodo. El coste pasa de exponencial a polinómico.

Es el mismo principio que hay detrás de Viterbi, del alineamiento de secuencias
biológicas (Needleman–Wunsch), del control óptimo y de la ecuación de
Hamilton–Jacobi–Bellman. Y su condición de validez es que **el coste sea
aditivo a lo largo del camino y que el futuro dependa sólo del estado
presente**: es decir, Markov.

Cuando esa condición falla —cuando el coste de una arista depende de por dónde
has venido— la programación dinámica deja de aplicarse y el problema se vuelve
mucho más difícil.

---

## 6. ¿Cuándo falla?

::: falla
**Falla la intuición de «mínimo».** El principio de Fermat es de tiempo
**estacionario**, no mínimo: hay configuraciones —espejos cóncavos, lentes
gravitacionales— donde el camino real es un máximo local o un punto de silla.

**Falla Dijkstra con pesos negativos**, porque el principio de optimalidad
requiere que añadir aristas no mejore. Hay que usar Bellman–Ford.

**Falla la programación dinámica sin propiedad de Markov.**

**Y falla la interpretación teleológica.** Que la luz «elija» el camino más
rápido no significa que tenga preferencias: el principio variacional es
matemáticamente equivalente a las ecuaciones locales de propagación de ondas, y
la equivalencia va en los dos sentidos.
:::

---

## 7. Historia

::: historia
**Fermat, 1662, y una discusión que duró un siglo** ·
*Nivel de verificación: A.*

Fermat enunció que la luz sigue el camino de tiempo mínimo y dedujo de ahí la
ley de refracción, que Snell y Descartes habían obtenido antes empíricamente.

La objeción de la época era seria: la formulación parecía atribuir a la luz un
conocimiento del destino. Descartes, y después Maupertuis con su principio de
mínima acción de 1744, sostuvieron interpretaciones teleológicas o teológicas
que Euler y Lagrange sustituyeron por matemáticas: el cálculo de variaciones
demuestra que el principio integral y las ecuaciones diferenciales locales son
**equivalentes**, y ninguna es más fundamental que la otra.

La cuestión se cerró definitivamente con Huygens y la óptica ondulatoria, y
después con Feynman: los caminos vecinos interfieren, y sólo cerca del
estacionario la fase varía despacio y la interferencia es constructiva. **La luz
no elige: prueba todos y el resto se cancela.**

**Bellman, 1953, y el nombre** · *Nivel B.*

Richard Bellman contó en su autobiografía que eligió el nombre «programación
dinámica» por razones de política presupuestaria: trabajaba para RAND bajo un
secretario de Defensa hostil a la investigación matemática, y necesitaba un
nombre que sonara a ingeniería aplicada y no a matemáticas. El relato es
autobiográfico y se acepta generalmente, aunque conviene citarlo como lo que es.
:::

---

## 8. Experimento computacional

::: experimento
**Del camino óptimo a la distribución de caminos.**

Toma una red con pesos y calcula el camino más corto con Dijkstra. Después
muestrea caminos con probabilidad $\propto e^{-S/\epsilon}$ usando Metropolis
sobre el espacio de caminos, para varios $\epsilon$.

*Predice antes:* ¿qué le pasa a la distribución de caminos muestreados cuando
$\epsilon\to0$? ¿Y cuando $\epsilon$ es grande?

*Qué medir:* la fracción de muestras que coinciden con el óptimo, y la anchura
de la distribución de costes, frente a $\epsilon$.

*La conexión:* acabas de construir la relación entre optimización y muestreo del
capítulo 10, y de paso una versión discreta de la integral de caminos.
:::

---

## 9. Lo esencial

::: esencial
* «Minimizar una suma a lo largo de un camino» es una estructura común a la
  óptica, la mecánica, la logística y la inferencia.
* El principio de Fermat da Snell exactamente; la acción estacionaria da la
  trayectoria física.
* El camino más probable con $P\propto e^{-S/\epsilon}$ es el de coste mínimo:
  optimizar y muestrear son la misma cosa a dos «temperaturas».
* Programación dinámica: el principio de optimalidad convierte un problema
  exponencial en polinómico, **si el coste es aditivo y el sistema es Markov**.
* Viterbi, Dijkstra, alineamiento de secuencias y Hamilton–Jacobi–Bellman son
  el mismo esquema.
* Estacionario no es mínimo, y el principio variacional no implica teleología.
:::

---

## 10. Preguntas abiertas

::: abierto
* ¿Qué problemas de camino óptimo **no** admiten programación dinámica, y qué
  los hace difíciles?
* En grandes desviaciones, ¿cómo se calcula el instantón de una transición rara
  cuando el paisaje tiene muchos mínimos?
* ¿Hay una versión útil del principio de mínima acción para sistemas
  disipativos?
* Si los caminos vecinos se cancelan por interferencia, ¿qué anchura tiene el
  «tubo» de caminos que contribuyen, y de qué depende?
:::

### Referencias

* **Feynman, R. P.** *The Feynman Lectures on Physics*, vol. II, cap. 19, y
  **QED**, 1985. La explicación de por qué la luz «elige».
* **Bellman, Richard.** *Dynamic Programming.* Princeton UP, 1957.
  **Nivel A (primaria).**
* **Viterbi, Andrew.** *Error bounds for convolutional codes…* IEEE Trans.
  Inf. Theory **13** (1967), 260–269. **Nivel A (primaria).**
* **Touchette, Hugo.** *The large deviation approach to statistical mechanics.*
  Physics Reports **478** (2009), 1–69. La conexión probabilidad–acción.
* **Lanczos, Cornelius.** *The Variational Principles of Mechanics.* Dover,
  1970. Clásico y muy legible.
