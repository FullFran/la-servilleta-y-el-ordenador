## Problemas del capítulo 5

**Marcas:** ○ directo · ◐ requiere pensar · ● difícil · ★ abierto.

---

### Calentamiento

**5.C1** ○ Mides $L=(2{,}50\pm0{,}02)$ m y $T=(3{,}17\pm0{,}05)$ s. Calcula
$g=4\pi^2L/T^2$ con su incertidumbre. ¿Cuál de las dos medidas domina el error?

**5.C2** ○ Un instrumento tiene resolución de 0,1 mm. ¿Qué incertidumbre tipo B
le asignas a una única lectura, y por qué no es 0,1 mm?

**5.C3** ○ Un ajuste con 25 puntos y 3 parámetros da $\chi^2=87$. ¿Qué
concluyes? ¿Y si diera $\chi^2=6$?

**5.C4** ○ Dos parámetros con $\sigma_a=2$, $\sigma_b=3$ y $\rho=-0{,}8$.
Calcula la incertidumbre de $a+b$ y la de $a-b$. ¿Cuál te conviene medir?

---

### Estimación

**5.E1** ◐ Estima cuántas medidas necesitarías para determinar el tiempo de una
caída con un 0,1 % de precisión usando un cronómetro manual. ¿Es viable?

**5.E2** ◐ Estima la incertidumbre de tu propia estimación de la temperatura
ambiente sin termómetro. ¿Es tipo A o tipo B?

**5.E3** ● Estima el error sistemático que introduce medir una longitud con una
cinta metálica a 35 °C, calibrada a 20 °C. ¿A partir de qué longitud importa
más que tu error de lectura?

---

### Modelado

**5.M1** ◐ Quieres medir la conductividad térmica de un material. Enumera cinco
fuentes de error sistemático y di cómo detectarías cada una **sin** conocer el
valor verdadero.

**5.M2** ◐ Un sensor deriva linealmente con el tiempo. Diseña un protocolo de
medida que cancele la deriva sin necesidad de caracterizarla.

**5.M3** ● Tienes dos métodos independientes para medir la misma cantidad, con
resultados $A=10{,}2\pm0{,}3$ y $B=11{,}1\pm0{,}2$. ¿Los combinas? ¿Cómo?
¿Qué haces con el hecho de que difieren en 2,5 sigmas?

---

### Derivación

**5.D1** ◐ Deduce la fórmula de propagación a primer orden desde el desarrollo
de Taylor, y escribe explícitamente el término que se desprecia.

**5.D2** ◐ Demuestra que minimizar $\chi^2$ equivale a maximizar la
verosimilitud si los errores son gaussianos independientes. ¿Qué cambia si son
gaussianos correlacionados?

**5.D3** ● Deduce el sesgo de $E[f(x)]$ frente a $f(E[x])$ a segundo orden y
calcúlalo para $f=x^2$, $f=1/x$ y $f=\ln x$. ¿Para cuál de las tres es peor?

**5.D4** ● Demuestra que la media ponderada por $1/\sigma_i^2$ es el estimador
de mínima varianza entre los estimadores lineales insesgados, y calcula su
incertidumbre.

---

### Computacional

**5.P1** ○ Propaga por Monte Carlo la incertidumbre de $g=4\pi^2L/T^2$ del
problema 5.C1 y compara con la fórmula lineal. ¿Coinciden?

**5.P2** ◐ Reproduce la figura de residuos. Después genera datos con un valor
atípico y compara `curve_fit` con `least_squares(loss='soft_l1')`. ¿Cuánto se
mueve cada uno?

**5.P3** ◐ Ajusta la exponencial de la figura de covarianza 500 veces con
ruido distinto y comprueba que la nube de parámetros ajustados reproduce la
elipse de covarianza predicha por `curve_fit`.

---

### Experimento

**5.X1** ◐ Barre el rango temporal de los datos del enfriamiento y dibuja
$\sigma_\tau$ frente a $t_{\max}/\tau$. ¿A partir de qué fracción de $\tau$
deja de mejorar? Es la respuesta cuantitativa a «¿cuánto tiempo tengo que
medir?».

**5.X2** ● Implementa un bootstrap no paramétrico del ajuste del enfriamiento y
compara sus intervalos con los de la matriz de covarianza. ¿Cuándo divergen?

---

### Detective

**5.T1** ◐ Un informe presenta: «tras promediar 10 000 medidas, el resultado es
$(9{,}8123\pm0{,}0001)$ m/s²». El valor real en ese laboratorio es 9,8009.
¿Qué ha pasado y por qué el número de medidas es irrelevante?

**5.T2** ◐ Un ajuste de 8 puntos con 6 parámetros da $\chi^2_\nu=0{,}12$ y
$R^2=0{,}9999$. El autor concluye que el modelo es excelente. ¿Qué le dirías?

**5.T3** ● Una serie de determinaciones publicadas de una constante, ordenadas
por año, muestra barras de error que se estrechan monótonamente y valores
centrales que se desplazan sistemáticamente en la misma dirección, siempre
dentro de la barra anterior. ¿Qué patrón es este y qué lo produce?

---

### Mundo real

**5.R1** ★ Coge un resultado publicado de tu campo con su incertidumbre.
Reconstruye, hasta donde el artículo lo permita, cómo la calcularon. ¿Cuántas
de las fuentes son tipo A y cuántas tipo B? ¿Está el sesgo evaluado?

**5.R2** ★ Diseña un análisis ciego para una medida de tu trabajo. ¿Qué
información hay que ocultar, a quién, y hasta cuándo?

---

### Feynman

**5.F1** ○ Explica sin ecuaciones por qué medir mil veces no arregla un
termómetro descalibrado.

**5.F2** ◐ Explica la matriz de covarianza a alguien que sólo ha visto barras
de error, usando la imagen de la elipse.

---

### Extensión

**5.Z1** ★ Lee Henrion y Fischhoff (1986) sobre la historia de las medidas de
constantes fundamentales y la frecuencia con la que el valor aceptado quedó
fuera de las barras de error publicadas. Después estima cuál debería ser el
factor de seguridad honesto sobre una incertidumbre publicada.

**5.Z2** ★ Estudia la regresión de Deming (errores en ambas variables) y aplícala
a un conjunto de datos donde $x$ también tenga error. ¿Cuánto cambia la
pendiente respecto de mínimos cuadrados ordinarios?
