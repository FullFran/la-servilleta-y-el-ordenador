## Problemas del capítulo 13

**Marcas:** ○ directo · ◐ requiere pensar · ● difícil · ★ abierto.

---

### Calentamiento

**13.C1** ○ ¿Hasta qué valor de $x$ vale $e^x\approx1+x$ con error del 1 %?
¿Y con error del 0,1 %?

**13.C2** ○ Desarrolla $\sqrt{1+\epsilon}$ hasta segundo orden y estima el
error para $\epsilon=0{,}1$ y $\epsilon=0{,}5$.

**13.C3** ○ Para cada ecuación, di si la perturbación es regular o singular:
(a) $x^2+\epsilon x-1=0$; (b) $\epsilon x^2+x-1=0$; (c) $\epsilon y''+y=0$;
(d) $y''+\epsilon y=0$.

**13.C4** ○ Un término de una serie asintótica vale $n!/x^{n+1}$. ¿Para qué $n$
es mínimo si $x=8$?

---

### Estimación

**13.E1** ◐ Estima el grosor de la capa límite en el ala de un avión comercial
en crucero. Compáralo con el espesor del ala.

**13.E2** ◐ En un péndulo real, ¿a partir de qué amplitud el error de la
aproximación de ángulo pequeño en el **periodo** supera el 1 %? Compara con el
14° de la aproximación de $\sin\theta$ y explica la diferencia.

**13.E3** ● Estima durante cuántas órbitas puede despreciarse la resistencia
atmosférica para un satélite a 400 km, y a partir de qué momento el efecto
acumulado exige incluirla.

---

### Modelado

**13.M1** ◐ Una reacción química tiene una etapa muy rápida y otra lenta.
Formula la aproximación de estado cuasi-estacionario e identifica el parámetro
pequeño y la capa límite temporal.

**13.M2** ◐ En un circuito RC con una inductancia parásita muy pequeña, ¿dónde
está la capa límite? ¿Qué pasa si la desprecias desde el principio?

**13.M3** ● Un modelo de población tiene reproducción rápida y migración lenta.
Adimensionaliza, identifica el parámetro pequeño y deduce el modelo reducido.
¿Qué información se pierde?

---

### Derivación

**13.D1** ◐ Deduce los dos primeros términos de la raíz «regular» de
$\epsilon x^2+x-1=0$ y compáralos con la raíz exacta para $\epsilon=0{,}1$.

**13.D2** ◐ Resuelve $\epsilon y''+y'+y=0$ con $y(0)=0$, $y(1)=1$ de forma
exacta y comprueba el resultado asintótico del capítulo.

**13.D3** ● Aplica el método de Poincaré–Lindstedt al oscilador de Duffing
$\ddot x+x+\epsilon x^3=0$ y deduce la corrección de frecuencia
$\omega\approx1+\tfrac38\epsilon a^2$. Explica por qué el desarrollo ingenuo
falla.

**13.D4** ● Deduce la serie asintótica de $e^xE_1(x)$ integrando por partes
repetidamente, y obtén una cota del resto que explique el truncamiento óptimo.

---

### Computacional

**13.P1** ○ Reproduce la figura del error de Taylor y determina numéricamente
el radio de validez al 0,1 % para $\sin$, $\cos$ y $\tan$.

**13.P2** ◐ Resuelve el problema de capa límite con malla uniforme y con malla
graduada. ¿Cuántos nodos necesita cada una para el mismo error?

**13.P3** ◐ Implementa el truncamiento óptimo de la serie asintótica y compara
con `scipy.special.exp1`. Dibuja el error óptimo frente a $x$.

---

### Experimento

**13.X1** ◐ Barre $\epsilon$ y mide la anchura de la capa límite como se
describe en la sección 10. Comprueba el exponente 1. Después repite con el
problema $\epsilon y''+xy'+y=0$ y descubre el exponente $1/2$.

**13.X2** ● Compara, para el mismo $\epsilon$, la precisión de la solución
asintótica compuesta y la de un solucionador numérico con presupuesto fijo de
nodos. Encuentra el $\epsilon$ por debajo del cual gana la asintótica.

---

### Detective

**13.T1** ◐ Alguien desprecia la viscosidad en un flujo con $Re=10^6$ y
concluye que la resistencia es cero. ¿Dónde está el error, y cómo se llama?

**13.T2** ◐ Un desarrollo perturbativo de un oscilador da
$x(t)=\cos t+\epsilon t\sin t$. El autor lo usa para $t=100/\epsilon$. ¿Qué
falla?

**13.T3** ● Un cálculo perturbativo sumando 40 términos da un resultado que
difiere del experimento en un factor 10. El autor concluye que la teoría es
incorrecta. Da una explicación alternativa y di cómo comprobarla.

---

### Mundo real

**13.R1** ★ Coge un modelo que uses y haz la lista de todo lo que desprecia.
Para cada término, escribe el número adimensional que justifica despreciarlo.
¿Cuántos puedes justificar de verdad?

**13.R2** ★ Busca en tu campo un caso donde una aproximación estándar se use
fuera de su régimen de validez. Cuantifica el error.

---

### Feynman

**13.F1** ○ Explica sin ecuaciones qué es una capa límite.

**13.F2** ◐ Explica cómo una serie que diverge puede ser útil.

---

### Extensión

**13.Z1** ★ Lee el artículo de Prandtl de 1904 (hay traducciones). ¿Cómo
justifica su hipótesis? ¿Qué evidencia experimental aporta?

**13.Z2** ★ Estudia la resumación de Borel y aplícala a la serie asintótica del
capítulo. ¿Cuánto mejora respecto al truncamiento óptimo, y a qué coste?
