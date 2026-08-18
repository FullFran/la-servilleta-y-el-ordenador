## Problemas del capítulo 4

**Marcas:** ○ directo · ◐ requiere pensar · ● difícil · ★ abierto.

---

### Calentamiento

**4.C1** ○ Cuentas 2500 sucesos. Da el resultado con su incertidumbre absoluta
y relativa. ¿Cuántos tendrías que contar para bajar al 0,5 %?

**4.C2** ○ Un detector registra 60 cuentas por minuto. ¿Cuál es la probabilidad
de que en un segundo concreto no registre ninguna? ¿Y de que registre 3 o más?

**4.C3** ○ Un proceso tiene media 4,0 y varianza 9,0 en conteos. ¿Es Poisson?
¿Qué sospechas?

**4.C4** ○ Un servidor recibe 200 peticiones por segundo. ¿Cuál es la
desviación típica del número de peticiones en una ventana de 10 ms? ¿Y el
ruido relativo?

---

### Estimación

**4.E1** ◐ Estima cuántos fotones recoge el sensor de tu móvil por píxel en una
foto de interior con 1/60 s de exposición. ¿Explica el grano que ves?

**4.E2** ◐ Estima cuántas desintegraciones de $^{40}$K ocurren en tu cuerpo cada
segundo. ¿Y cuántas de $^{14}$C?

**4.E3** ◐ Estima cuántas mutaciones puntuales nuevas lleva un recién nacido
respecto de sus padres. ¿Es un proceso de Poisson? ¿Qué violaría la
independencia?

**4.E4** ● Estima cuánto tiempo de telescopio haría falta para detectar a
5 sigmas una fuente diez veces más débil que el fondo de cielo, si una fuente
igual de brillante que el fondo se detecta en una hora.

---

### Modelado

**4.M1** ◐ Los rayos cósmicos que atraviesan un detector, ¿son Poisson? Enumera
los tres supuestos y di cuál te preocupa más y por qué.

**4.M2** ◐ El número de erratas por página de un libro. ¿Poisson? ¿Qué
mecanismo produciría sobredispersión aquí? ¿Y subdispersión?

**4.M3** ● Modela el número de contagios producidos por un infectado. Los datos
de varias epidemias muestran fuerte sobredispersión ($D\gg1$): unos pocos
individuos causan la mayoría de los contagios. Construye un modelo mínimo que
lo produzca y explica qué consecuencia tiene para las medidas de control.

---

### Derivación

**4.D1** ◐ Deduce Poisson desde la ecuación maestra
$dP_k/dt=\lambda(P_{k-1}-P_k)$ con $P_k(0)=\delta_{k0}$. (Pista: función
generatriz $G(z,t)=\sum_k P_k z^k$.)

**4.D2** ◐ Demuestra que la suma de dos variables Poisson independientes es
Poisson, y que la varianza de la suma es la suma de las varianzas. ¿Qué
implica esto para sumar señal y fondo?

**4.D3** ● Deduce la relación entre tasa medida y tasa real para un detector no
paralizable con tiempo muerto $\tau$, y demuestra que el índice de dispersión
resultante es menor que 1.

**4.D4** ● Demuestra que si $\lambda$ se distribuye como una gamma y $N\mid
\lambda \sim$ Poisson($\lambda$), entonces $N$ es binomial negativa. Calcula su
índice de dispersión en función de los parámetros de la gamma.

---

### Computacional

**4.P1** ○ Genera Poisson contando sucesos exponenciales en un intervalo
unidad. Comprueba que la distribución es la correcta y que media y varianza
coinciden.

**4.P2** ◐ Reproduce la figura de la imagen con ruido de fotones. Añade después
ruido de lectura gaussiano y determina numéricamente a partir de qué señal deja
de dominar.

**4.P3** ◐ Simula 10 000 experimentos de conteo con $b=8$ y comprueba
empíricamente qué fracción produce $n\ge12$ por puro azar. Compáralo con la
estimación de 1,4 sigmas del texto. ¿Coinciden? ¿Por qué la aproximación normal
es mala aquí?

---

### Experimento

**4.X1** ◐ Barre la tasa de un proceso con tiempo muerto y reproduce la curva
de saturación. Después intenta distinguir el modelo paralizable del no
paralizable **usando sólo la tasa medida**. ¿Se puede? ¿Qué medida adicional lo
resolvería?

**4.X2** ● Simula el efecto look-elsewhere: busca el máximo exceso local en
1000 canales de fondo puro, repite el experimento 1000 veces y construye la
distribución del máximo. ¿Qué umbral local corresponde a una significancia
global de 3 sigmas?

---

### Detective

**4.T1** ◐ Un informe dice: «medimos 10 000 cuentas en la muestra y 9 800 en el
blanco. El exceso de 200 cuentas es del 2 %, muy por encima de nuestra
precisión del 1 %, así que la detección es sólida». ¿Es sólida?

**4.T2** ◐ Un experimento de conteo reporta una tasa de $(1523{,}47\pm0{,}12)$
cuentas por segundo, obtenida contando durante 100 s. Hay algo imposible en esa
frase. ¿Qué?

**4.T3** ● Un estudio observa que la incidencia de una enfermedad rara es tres
veces mayor en un municipio pequeño que en la media nacional, con $p<0{,}01$, y
concluye que hay un factor ambiental local. El municipio tiene 3000 habitantes
y la incidencia nacional es de 1 caso por cada 10 000 habitantes y año. ¿Qué
está mal? (Pista: ¿cuántos municipios hay en España?)

---

### Mundo real

**4.R1** ★ Coge una métrica de conteo de tu trabajo (errores, peticiones,
eventos) y calcula su índice de dispersión por ventanas temporales. ¿Es
Poisson? Si no, ¿qué mecanismo lo explica?

**4.R2** ★ Busca en la literatura de tu campo un resultado anunciado con
3 sigmas que después no se confirmó. Reconstruye cuántas búsquedas
independientes había detrás.

---

### Feynman

**4.F1** ○ Explica sin ecuaciones por qué contar más tiempo mejora la precisión
sólo con la raíz del tiempo, y no proporcionalmente.

**4.F2** ◐ Explica por qué tus amigos tienen, en promedio, más amigos que tú, y
por qué no es un insulto.

---

### Extensión

**4.Z1** ★ Lee el artículo original de Rutherford, Geiger y Bateman (1910).
Fíjate en cómo describen el procedimiento experimental —dos observadores
turnándose para contar centelleos a ojo— y evalúa qué fuentes de error
sistemático tendría hoy ese experimento.

**4.Z2** ★ Estudia los procesos de Hawkes (autoexcitados) y aplícalos a un
conjunto de datos con agrupamiento: réplicas sísmicas, retuits o incidencias de
un sistema. Compara el ajuste con el de una binomial negativa: ¿cuál captura
mejor la estructura temporal, y por qué?
