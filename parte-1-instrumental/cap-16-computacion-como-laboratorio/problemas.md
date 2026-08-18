## Problemas del capítulo 16

**Marcas:** ○ directo · ◐ requiere pensar · ● difícil · ★ abierto.

---

### Calentamiento

**16.C1** ○ Un modelo tiene 7 parámetros dimensionales y 3 dimensiones
independientes. ¿Cuántas simulaciones ahorras al adimensionalizar, con una
rejilla de 8 puntos por eje?

**16.C2** ○ Con 100 simulaciones, ¿cuántos valores distintos de cada parámetro
prueba una rejilla en 2, 3 y 4 dimensiones? ¿Y un hipercubo latino?

**16.C3** ○ Enumera cinco cosas que hay que registrar para que un resultado
computacional sea reproducible.

**16.C4** ○ Escribe tres pruebas para un código que integra $\dot y=-y$.

---

### Estimación

**16.E1** ◐ Estima cuánto costaría, en horas de CPU y en euros de nube, un
barrido de 6 parámetros con 10 puntos por eje si cada simulación tarda un
minuto.

**16.E2** ◐ Estima cuántas simulaciones necesitas para estimar índices de Sobol
de primer orden con un 10 % de precisión en un modelo de 5 parámetros.

**16.E3** ● Estima el tiempo de recurrencia de FPU en función de $N$ y de la no
linealidad, a partir de simulaciones cortas, y contrástalo con la literatura.

---

### Modelado

**16.M1** ◐ Diseña el experimento computacional que decidiría si un fenómeno
que has observado en una simulación es físico o numérico. Enumera las
comprobaciones en orden de coste.

**16.M2** ◐ Tienes presupuesto para 500 simulaciones de un modelo de 8
parámetros. Diseña la estrategia completa: cribado, exploración, refinamiento.

**16.M3** ● Diseña un protocolo de verificación completo para un código que
resuelve una EDP no lineal sin solución analítica conocida.

---

### Derivación

**16.D1** ◐ Deduce el número de grupos adimensionales de un modelo con
$n$ parámetros y $k$ dimensiones, y explica el ahorro en un barrido.

**16.D2** ◐ Demuestra que el hipercubo latino garantiza que cada parámetro se
muestrea una vez en cada uno de los $N$ intervalos equiprobables.

**16.D3** ● Deduce, para la cadena FPU, las frecuencias de los modos normales
y comprueba que la simulación las reproduce.

---

### Computacional

**16.P1** ○ Reproduce el experimento FPU. Cambia a Euler explícito y comprueba
que la recurrencia desaparece bajo la deriva de energía.

**16.P2** ◐ Compara rejilla, aleatorio, hipercubo latino y Sobol para estimar
la media de una función en 5 dimensiones con 200 puntos. Mide el error de cada
uno.

**16.P3** ◐ Implementa el método de soluciones manufacturadas para un código
de difusión 1D y verifica el orden en el interior y en el borde.

---

### Experimento

**16.X1** ◐ Barre la no linealidad $\alpha$ en FPU y encuentra el umbral por
encima del cual el sistema termaliza. Compara con Izrailev y Chirikov.

**16.X2** ● Toma un modelo tuyo, haz un cribado de sensibilidad con 200
evaluaciones (método de Morris) y comprueba cuántos parámetros puedes fijar sin
cambiar las conclusiones.

---

### Detective

**16.T1** ◐ Una simulación estocástica da resultados distintos cada vez, y el
autor promedia 5 realizaciones y publica. ¿Qué falta?

**16.T2** ◐ Un código reproduce un resultado experimental con un 2 % de error.
Al actualizar la versión de NumPy, el error pasa al 15 %. ¿Qué ha pasado y qué
implica sobre el resultado original?

**16.T3** ● Un barrido de 50 000 simulaciones encuentra una región del espacio
de parámetros con comportamiento anómalo. Antes de escribir el artículo, ¿qué
cinco cosas comprobarías?

---

### Mundo real

**16.R1** ★ Coge tu proyecto computacional actual y aplícale la lista de
reproducibilidad del apartado 4.4. ¿En qué nivel estás?

**16.R2** ★ Escribe la primera prueba automática que haya tenido nunca un
código tuyo. Empieza por un orden de convergencia.

---

### Feynman

**16.F1** ○ Explica en qué se diferencia una simulación de un experimento.

**16.F2** ◐ Explica por qué el resultado de FPU, que «falló», fue más valioso
que uno que hubiera confirmado lo esperado.

---

### Extensión

**16.Z1** ★ Lee el informe LA-1940 original. Fíjate en cómo describen las
comprobaciones que hicieron para descartar errores de la máquina. ¿Qué harías
tú hoy en su lugar?

**16.Z2** ★ Lee Zabusky y Kruskal (1965). ¿Cómo pasaron del sistema discreto a
la ecuación KdV, y qué papel jugó la visualización en su descubrimiento?
