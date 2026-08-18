## Problemas del capítulo 3

**Marcas:** ○ directo · ◐ requiere pensar · ● difícil · ★ abierto.

---

### Calentamiento

**3.C1** ○ Un test tiene sensibilidad 95 % y especificidad 90 %. En una
población con prevalencia del 20 %, ¿cuál es el valor predictivo positivo?
Hazlo con una tabla de 1000 personas, sin usar la fórmula de Bayes.

**3.C2** ○ Calcula media y varianza de: Bernoulli($p$), binomial($n,p$),
Poisson($\lambda$), exponencial($\lambda$), uniforme($a,b$).

**3.C3** ○ $X$ e $Y$ independientes con varianzas 4 y 9. ¿Cuánto vale
$\operatorname{Var}(X+Y)$? ¿Y $\operatorname{Var}(X-Y)$? ¿Y si están
correlacionadas con $\rho=0{,}5$?

**3.C4** ○ ¿Cuántos bits de entropía tiene una moneda equilibrada? ¿Y una
cargada con $p=0{,}9$? ¿Y un dado de veinte caras?

---

### Estimación

**3.E1** ◐ En una sala con 30 personas, estima la probabilidad de que al menos
dos cumplan años el mismo día **antes** de calcularla. Después calcúlala.
¿Falló tu intuición y en qué dirección?

**3.E2** ◐ Estima cuántas veces al año, en España, coinciden en un mismo día
dos personas que se llaman igual y nacieron el mismo día. Después decide si el
número que te sale hace que una «coincidencia asombrosa» sea asombrosa.

**3.E3** ● Estima la probabilidad de que un servidor con 99,9 % de
disponibilidad mensual esté caído justo cuando lanzas tu producto. Después
estima lo mismo para tres servidores redundantes, primero suponiendo
independencia y después suponiendo que comparten centro de datos.

---

### Modelado

**3.M1** ◐ Para cada situación, di qué distribución usarías y **por qué
mecanismo**: (a) número de erratas por página; (b) tiempo entre dos correos;
(c) altura de los adultos de un país; (d) tamaño de los ficheros de un disco;
(e) número de seguidores de las cuentas de una red social; (f) número de caras
en 100 lanzamientos.

**3.M2** ◐ Un contador Geiger registra 3 cuentas por segundo de media. Modela
el proceso desde cero: define $\Omega$, la variable aleatoria y los supuestos.
¿Cuáles de esos supuestos son físicos y cuáles son de conveniencia?

**3.M3** ● Modela la probabilidad de que un aparcamiento de 200 plazas se
llene. ¿Qué necesitas suponer sobre las llegadas? ¿Sigue valiendo el modelo un
sábado por la tarde? Identifica qué supuesto se rompe primero.

---

### Derivación

**3.D1** ◐ Deduce la distribución de Poisson como límite de la binomial con
$n\to\infty$, $p\to0$ y $np=\lambda$ fijo. ¿Dónde exactamente se usa que $p$ es
pequeño?

**3.D2** ◐ Demuestra que la exponencial es la única distribución continua sin
memoria. (Pista: la condición funcional $S(t+s)=S(t)S(s)$ con $S$ continua
sólo tiene una familia de soluciones.)

**3.D3** ● Deduce el teorema central del límite con funciones características,
como en el apartado 4.6, y señala exactamente el paso que falla para la
distribución de Cauchy.

**3.D4** ● Demuestra que, entre todas las distribuciones sobre $[0,\infty)$
con media fijada, la de máxima entropía es la exponencial. (Pista:
multiplicadores de Lagrange sobre el funcional de entropía.)

---

### Computacional

**3.P1** ○ Genera exponenciales por transformada inversa y comprueba con un
histograma que la distribución es la correcta. Verifica también la propiedad de
falta de memoria condicionando a $T>2$.

**3.P2** ◐ Implementa Box–Muller y compáralo con `rng.normal`. Comprueba media,
varianza, asimetría y curtosis. ¿Cuántas muestras necesitas para distinguir una
normal de una $t$ de Student con 5 grados de libertad?

**3.P3** ◐ Reproduce el panel de Cauchy. Después calcula la **mediana**
acumulada en vez de la media. ¿Converge? ¿Qué te dice eso sobre qué estadístico
usar con colas pesadas?

---

### Experimento

**3.X1** ◐ Simula el TCL con distintas distribuciones de partida y mide cuántos
sumandos hacen falta para que la desviación respecto a la normal baje de un
umbral. Relaciona ese número con la asimetría de la distribución de partida.
¿Encuentras una regla empírica?

**3.X2** ● Simula el problema de Monty Hall de dos formas: (a) el presentador
sabe dónde está el premio y siempre abre una puerta vacía; (b) el presentador
abre una puerta al azar y resulta estar vacía. Comprueba que las dos dan
respuestas distintas y explica por qué el enunciado verbal no distingue los
casos.

---

### Detective

**3.T1** ◐ «El 80 % de los accidentes de coche ocurren a menos de 20 km de
casa. Luego conducir cerca de casa es peligrosísimo». ¿Qué falla?

**3.T2** ◐ Un informe de fiabilidad: «cada uno de los cuatro sensores falla con
probabilidad $10^{-2}$ al año. La probabilidad de que fallen los cuatro es
$10^{-8}$, así que el sistema es seguro». Enumera las tres hipótesis
implícitas y di cuál te preocupa más.

**3.T3** ● Un estudio afirma: «entre los pacientes que recibieron el
tratamiento, el 70 % mejoró; entre los que no, el 50 %. El tratamiento
funciona». Después se descubre que los médicos daban el tratamiento
preferentemente a los pacientes menos graves. Explica con un ejemplo numérico
concreto cómo puede el tratamiento ser **perjudicial** y aun así producir esos
porcentajes.

---

### Mundo real

**3.R1** ★ Busca en tu campo un modelo que multiplique probabilidades. Rastrea
la hipótesis de independencia hasta su origen. ¿Está justificada en algún sitio,
o se heredó?

**3.R2** ★ Coge una métrica de tu trabajo que se reporte como media (latencia,
tiempo de proceso, coste). Dibuja su distribución completa. ¿Tiene sentido la
media? ¿Qué percentil deberías estar reportando?

---

### Feynman

**3.F1** ○ Explica sin fórmulas por qué, con un test buenísimo y una enfermedad
rara, la mayoría de los positivos son sanos.

**3.F2** ◐ Explica por qué la campana de Gauss aparece por todas partes, y da
un ejemplo concreto donde no aparece y se sabe por qué.

---

### Extensión

**3.Z1** ★ Lee la paradoja de Bertrand (1889) y resuélvela de las tres maneras
clásicas. Después explica por qué no es una paradoja, en términos del apartado
3.2 de este capítulo.

**3.Z2** ★ Lee el capítulo 1 de Jaynes (2003), donde deduce las reglas de la
probabilidad a partir de axiomas de «sentido común» (teorema de Cox). Después
busca una crítica técnica a esa derivación —hay varias publicadas— y forma tu
propia opinión. Es un buen entrenamiento para el capítulo III.11.
