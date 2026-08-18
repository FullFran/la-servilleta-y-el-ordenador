## Problemas del capítulo 15

**Marcas:** ○ directo · ◐ requiere pensar · ● difícil · ★ abierto.

---

### Calentamiento

**15.C1** ○ Con 20 datos y ruido $\sigma=1$, ¿qué $\chi^2$ esperas de un modelo
correcto con 3 parámetros? ¿Y con 18?

**15.C2** ○ Un modelo con 8 parámetros da AIC 142 y otro con 3 da AIC 138.
¿Cuál eliges? ¿Y si los BIC son 158 y 145?

**15.C3** ○ Clasifica cada situación como confusor o colisionador: (a) el calor
causa helados y ahogamientos; (b) talento y suerte causan el éxito, y estudias
sólo a los exitosos; (c) la edad causa canas y riesgo cardiovascular.

**15.C4** ○ Una simulación produce un efecto que desaparece al reducir el paso
a la mitad. ¿Qué era?

---

### Estimación

**15.E1** ◐ Estima cuántos parámetros libres puedes permitirte con 50 datos y
ruido del 5 %, si quieres que la validación sea informativa.

**15.E2** ◐ Estima cuántas comparaciones se hacen implícitamente en un estudio
que mide 20 variables y prueba todas las correlaciones. ¿Cuántas saldrán
«significativas» al 5 % por puro azar?

**15.E3** ● Estima el sesgo de publicación en un campo donde el 90 % de los
artículos publicados reportan resultados positivos y la potencia típica es del
40 %. ¿Qué fracción de los positivos publicados serán falsos?

---

### Modelado

**15.M1** ◐ Para un modelo de tu campo, escribe: (a) su predicción más
arriesgada; (b) el experimento que la falsaría; (c) el criterio de abandono,
por escrito.

**15.M2** ◐ Diseña un análisis ciego para una medida de tu campo. ¿Qué se
oculta, a quién y hasta cuándo?

**15.M3** ● Construye un caso sintético de paradoja de Simpson con números
realistas de tu propio campo. ¿Qué variable habría que estratificar?

---

### Derivación

**15.D1** ◐ Deduce el AIC a partir de la divergencia de Kullback–Leibler
esperada y explica de dónde sale el término $2k$.

**15.D2** ◐ Demuestra que condicionar por un colisionador induce correlación
entre dos variables independientes, con un ejemplo gaussiano explícito.

**15.D3** ● Deduce la descomposición de la varianza de Sobol y demuestra que
los índices de primer orden suman menos de 1 cuando hay interacciones.

---

### Computacional

**15.P1** ○ Reproduce la figura de sobreajuste. Repítela con 100 datos en vez
de 14. ¿Cómo cambia el grado óptimo?

**15.P2** ◐ Implementa validación cruzada dejando uno fuera y compárala con
AIC y BIC en la selección del grado. ¿Coinciden?

**15.P3** ◐ Genera datos de una logística, ajusta los cuatro modelos de la
figura y calcula la banda de predicción **entre modelos** a $t=40$. Compárala
con la banda de covarianza de cada uno.

---

### Experimento

**15.X1** ◐ Toma un modelo con dos parámetros correlacionados y calcula sus
perfiles de verosimilitud. Compara el intervalo del perfil con el de la
covarianza. ¿Cuándo divergen?

**15.X2** ● Implementa el análisis de sensibilidad global de Sobol para un
modelo tuyo y compáralo con el análisis local «un factor cada vez». ¿Cambia
alguna conclusión?

---

### Detective

**15.T1** ◐ Una serie de determinaciones de una constante, ordenadas por año,
converge suavemente con barras que se estrechan. ¿Es evidencia de progreso?

**15.T2** ◐ Un modelo climático reproduce la temperatura observada del siglo XX
con un error de 0,05 °C. El autor concluye que sus parametrizaciones son
correctas. ¿Qué falta?

**15.T3** ● Un ensayo clínico encuentra un efecto significativo en el subgrupo
de mujeres mayores de 65 años con diabetes. No estaba preespecificado. ¿Qué
probabilidad hay de encontrar algún subgrupo significativo por azar, si se
examinan 30 subgrupos?

---

### Mundo real

**15.R1** ★ Coge un resultado tuyo publicado o interno. Aplícale las seis
comprobaciones numéricas del apartado 4.5. ¿Sobrevive?

**15.R2** ★ Busca en tu campo un resultado que se retractó o no se replicó.
Reconstruye cuál de los seis modos de mentir estaba operando.

---

### Feynman

**15.F1** ○ Explica el sobreajuste a alguien que nunca ha ajustado nada.

**15.F2** ◐ Explica por qué controlar por más variables puede empeorar un
análisis.

---

### Extensión

**15.Z1** ★ Lee Kapoor y Narayanan (2023) sobre fugas de información. ¿Cuáles
de los ocho tipos que catalogan podrían estar en tu propio trabajo?

**15.Z2** ★ Lee Ioannidis (2005) y al menos una crítica publicada. Forma tu
propia opinión sobre si su conclusión está bien calibrada, y escribe media
página con tu argumento.
