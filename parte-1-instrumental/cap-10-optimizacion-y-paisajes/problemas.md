## Problemas del capítulo 10

**Marcas:** ○ directo · ◐ requiere pensar · ● difícil · ★ abierto.

---

### Calentamiento

**10.C1** ○ Para $f=x^2+ay^2$, calcula el número de condición del hessiano y la
tasa de convergencia del descenso por gradiente con $a=1$, $a=10$ y $a=1000$.

**10.C2** ○ Clasifica los puntos críticos de $f(x,y)=x^2-y^2$,
$f=x^4+y^4$ y $f=x^2+y^3$.

**10.C3** ○ En recocido simulado con $T=1$, ¿con qué probabilidad se acepta un
empeoramiento de 0,5? ¿Y de 5? ¿Y si $T=0{,}1$?

**10.C4** ○ Un ajuste da $\rho(\theta_1,\theta_2)=-0{,}997$. ¿Qué combinación
de parámetros está bien determinada y cuál no?

---

### Estimación

**10.E1** ◐ Estima cuántas evaluaciones necesitaría una búsqueda exhaustiva en
rejilla con 20 puntos por eje para un problema de 8 parámetros. Compáralo con
lo que tarda BFGS.

**10.E2** ◐ Estima el número de rutas posibles en un problema del viajante con
30 ciudades. Compáralo con el número de átomos de la Tierra.

**10.E3** ● Estima cuánto tiempo de cálculo cuesta ajustar un modelo de 12
parámetros con gradiente por diferencias finitas frente a diferenciación
automática, si cada evaluación del modelo cuesta 1 segundo.

---

### Modelado

**10.M1** ◐ Formula como optimización: (a) el equilibrio de una cadena colgante;
(b) el reparto óptimo de $N$ recursos entre $M$ tareas; (c) el ajuste robusto de
una recta con valores atípicos. Di cuál es convexo.

**10.M2** ◐ Tu función objetivo es la media de simulaciones estocásticas y por
tanto es ruidosa. ¿Qué le pasa a BFGS? ¿Qué método usarías?

**10.M3** ● Diseña una función objetivo que penalice explícitamente la
fragilidad, de forma que el optimizador prefiera un mínimo ancho a uno profundo
y estrecho. ¿Qué introduces, y cómo eliges su peso?

---

### Derivación

**10.D1** ◐ Deduce la tasa de convergencia del descenso por gradiente en una
cuadrática y comprueba que es $(\kappa-1)/(\kappa+1)$.

**10.D2** ◐ Deduce el paso de Newton minimizando el modelo cuadrático local.
¿Qué ocurre si el hessiano no es definido positivo?

**10.D3** ● Demuestra que la distribución de Boltzmann $p\propto e^{-E/T}$
se concentra en el mínimo global cuando $T\to0$, y estima el ancho de la
distribución alrededor del mínimo en función de $T$ y de la curvatura.

**10.D4** ● Deduce las condiciones KKT para minimizar $f$ sujeto a $g(x)\le0$ e
interpreta el multiplicador como un precio sombra.

---

### Computacional

**10.P1** ○ Implementa descenso por gradiente y Newton para Rosenbrock y
reproduce la figura del capítulo. Mide la razón de convergencia de cada uno.

**10.P2** ◐ Implementa recocido simulado para el viajante con 40 ciudades.
Compara tres programas de enfriamiento y dibuja la mejor longitud frente al
tiempo.

**10.P3** ◐ Ajusta la suma de dos exponenciales desde 100 puntos de partida
aleatorios y dibuja el histograma de los parámetros obtenidos. ¿Reconoces el
valle?

---

### Experimento

**10.X1** ◐ Barre la separación entre las dos constantes de tiempo y dibuja la
correlación $\rho(\tau_1,\tau_2)$ frente a esa separación. ¿Dónde está el
umbral práctico de identificabilidad?

**10.X2** ● Compara BFGS, Nelder–Mead y CMA-ES en la misma función rugosa, en
dimensión 2, 5, 10 y 20. Dibuja la calidad del óptimo frente al número de
evaluaciones. ¿Dónde se cruzan las curvas?

---

### Detective

**10.T1** ◐ Un optimizador «converge» siempre al mismo punto pero el gradiente
allí no es cero. ¿Qué está pasando?

**10.T2** ◐ Un ajuste mejora su $\chi^2$ de 45 a 12 al pasar de 3 a 9
parámetros, con 20 datos. El autor concluye que el modelo nuevo es mejor.
¿Cuál es el problema, y qué comprobación pedirías?

**10.T3** ● Un algoritmo de recocido devuelve siempre la misma solución
independientemente de la semilla, y el autor concluye que es el óptimo global.
Da dos explicaciones alternativas, y di cómo distinguirlas.

---

### Mundo real

**10.R1** ★ Busca en tu organización una métrica que se optimice activamente.
¿Ha empezado a divergir de lo que pretendía medir? Documenta el mecanismo.

**10.R2** ★ Coge un ajuste que uses habitualmente y calcula sus perfiles de
verosimilitud. ¿Todos tus parámetros existen?

---

### Feynman

**10.F1** ○ Explica sin ecuaciones por qué el descenso por gradiente zigzaguea
en un valle estrecho.

**10.F2** ◐ Explica la relación entre enfriar un metal y resolver un problema
de optimización.

---

### Extensión

**10.Z1** ★ Lee Transtrum et al. (2015) sobre «sloppiness». ¿Por qué los
paisajes de ajuste de modelos con muchos parámetros tienen casi siempre valles
planos? ¿Qué implica eso sobre qué modelos son útiles?

**10.Z2** ★ Estudia el teorema *No Free Lunch* de Wolpert y Macready. ¿Qué dice
exactamente, qué **no** dice, y por qué en la práctica unos optimizadores son
mejores que otros?
