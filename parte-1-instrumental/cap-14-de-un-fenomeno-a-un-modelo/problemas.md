## Problemas del capítulo 14

**Marcas:** ○ directo · ◐ requiere pensar · ● difícil · ★ abierto.

> En este capítulo casi todos los problemas son de modelado. Es deliberado: la
> parte que falta entrenar no es resolver, es formular.

---

### Calentamiento

**14.C1** ○ Para cada pregunta, reescríbela de forma que sea cuantitativa y
lleve una precisión declarada: (a) «¿cuánto contamina un coche eléctrico?»;
(b) «¿es rentable poner placas?»; (c) «¿funciona este fármaco?».

**14.C2** ○ Un ajuste deja residuos con rms 0,8 y ruido de medida 0,3. ¿Qué
concluyes? ¿Y si el ruido fuese 1,2?

**14.C3** ○ Enumera tres cosas que un modelo puede predecir y que sirvan para
falsarlo, para el caso de la taza de café.

---

### Estimación

**14.E1** ◐ Estima el tiempo característico de enfriamiento de: una taza con
tapa, una taza en un termo, un cadáver (medicina forense usa esto), un lingote
de acero al aire.

**14.E2** ◐ Estima cuántas cajas necesita un supermercado con 3 clientes/min y
2 min de servicio para que la espera media sea menor de 3 min. Compara con el
mínimo teórico.

**14.E3** ● Estima cuánta información hace falta —cuántos datos, con qué
precisión— para distinguir evaporación de radiación en el enfriamiento del
café.

---

### Modelado

**14.M1** ◐ Recorre las quince etapas para: «¿cuánto tarda en cargarse la
batería de un coche eléctrico?». Escribe todas.

**14.M2** ◐ Lo mismo para: «¿cuánta gente cabe en un vagón de metro antes de
que la gente empiece a dejar pasar trenes?».

**14.M3** ● Lo mismo para un fenómeno de tu campo profesional que nunca hayas
modelado. Presta especial atención a la lista de variables **descartadas**.

**14.M4** ● Construye dos modelos distintos del mismo fenómeno que ajusten
igual de bien y predigan cosas distintas fuera del rango medido. Diseña el
experimento que los separa.

---

### Derivación

**14.D1** ◐ Deduce el modelo de Newton del enfriamiento desde el balance de
energía, y añade el término de radiación linealizado. ¿Cuándo es válida esa
linealización?

**14.D2** ◐ Deduce la fracción final de gente que se entera de un rumor en el
modelo de Daley–Kendall y comprueba que es menor que 1.

**14.D3** ● Deduce, para una cola M/M/c, la espera media en función de la
utilización, y demuestra que diverge cuando $\rho\to1$.

---

### Computacional

**14.P1** ○ Reproduce el ajuste de la taza con los dos modelos y comprueba los
residuos. Añade un tercer término y mira si mejora algo significativo.

**14.P2** ◐ Simula la cola del supermercado por eventos discretos y compárala
con la fórmula M/M/c. ¿Dónde discrepan y por qué?

**14.P3** ◐ Simula los tres modelos de rumor y encuentra qué observación
mínima los distingue.

---

### Experimento

**14.X1** ◐ Mide de verdad el enfriamiento de una taza con y sin tapa. La tapa
elimina la evaporación casi por completo. ¿Cambian los residuos como predice el
capítulo?

**14.X2** ● Pesa la taza al principio y al final del experimento. Con el calor
latente, convierte la masa perdida en energía y compárala con el déficit que
dejaba el modelo de Newton. ¿Cuadra?

---

### Detective

**14.T1** ◐ Un modelo con 40 parámetros calibrado con un año de datos da un
error del 3 % **sobre ese año**. ¿Qué falta antes de poder usarlo?

**14.T2** ◐ Un ajuste de la taza da $\tau=26$ min y el modelo predice que a las
3 horas el café estará a 21,0 °C. La medida da 21,8 °C. ¿Está mal el modelo?

**14.T3** ● Dos grupos modelan el mismo proceso. Uno usa 3 parámetros y obtiene
$\chi^2_\nu=1{,}8$; el otro usa 12 y obtiene $\chi^2_\nu=0{,}6$. ¿Cuál es
mejor? ¿Qué información pedirías para decidir?

---

### Mundo real

**14.R1** ★ Elige un fenómeno de tu entorno, mídelo esta semana y recorre el
ciclo entero por escrito.

**14.R2** ★ Coge un modelo que uses en el trabajo y escribe, por primera vez,
la lista completa de sus supuestos con su condición de validez. ¿Cuántos
sobreviven al escrutinio?

---

### Feynman

**14.F1** ○ Explica a alguien por qué un modelo sencillo que falla puede ser
más útil que uno complicado que ajusta.

**14.F2** ◐ Explica la diferencia entre calibrar y validar con un ejemplo
cotidiano.

---

### Extensión

**14.Z1** ★ Lee el capítulo 19 de *Astronomia Nova* (hay traducciones). ¿Cómo
argumenta Kepler que ocho minutos de arco son inaceptables? ¿Qué necesitaba
saber para poder afirmarlo?

**14.Z2** ★ Busca en tu campo un modelo estándar y rastrea el artículo original
donde se propuso. ¿Qué supuestos declaraba entonces y cuáles se han olvidado
por el camino?
