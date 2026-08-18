## Soluciones del capítulo 9

> Las soluciones son razonadas: el número final es lo menos importante. En los
> problemas ● y ★ con solución cerrada hay **Pista 1** y **Pista 2** antes de
> ella; tápalas con la mano y úsalas de una en una.
>
> Los de **Mundo real** (R) no llevan solución a propósito: su procedimiento
> está en el apéndice D.

---

### Calentamiento

**9.C1** $\sigma=\sqrt{p(1-p)/N}=\sqrt{0{,}21/10^4}=0{,}0046$. Para
$\pm0{,}001$ hace falta $N=p(1-p)/10^{-6}=2{,}1\times10^{5}$.

**9.C2** $N=(\sigma_f/\epsilon)^2=(2/10^{-3})^2=4\times10^6$. Con
$\sigma_f=0{,}2$: $4\times10^4$. **Reducir la varianza por 10 ahorra un factor
100 de tiempo**, y ese es todo el argumento de la sección 4.4.

**9.C3** $V_{\text{esfera}}/V_{\text{cubo}}=\pi^{d/2}/(2^d\Gamma(d/2+1))$:
$d=2$: 0,785; $d=3$: 0,524; $d=5$: 0,164; $d=10$: 0,0025;
$d=20$: $2{,}5\times10^{-8}$. En dimensión 20, el rechazo con un cubo
envolvente acepta uno de cada 40 millones.

**9.C4** $N_{\text{ef}}=10^5/250=400$. La barra correcta es
$\sqrt{250}\approx16$ veces mayor que la ingenua.

---

### Estimación

**9.E1** Seis decimales son $\epsilon=5\times10^{-7}$, luego
$N\sim(\sigma/\epsilon)^2\sim(1{,}6/5\times10^{-7})^2\approx10^{13}$. A $10^9$
muestras por segundo, unas **3 horas**. Es viable, pero es absurdo: una serie
de Chudnovsky da mil millones de cifras en el mismo tiempo. La conclusión es
la del capítulo: **Monte Carlo no compite en dimensión baja**.

**9.E2** $2^{400}\approx2{,}6\times10^{120}$. El Sol tiene $\sim10^{57}$
átomos. Es decir, hay más configuraciones de una rejilla de espines de
$20\times20$ que átomos en $10^{63}$ soles. Esa es la razón de que exista este
capítulo.

**9.E3** ● *Pista 1:* la magnitud a estimar es un factor de multiplicación
próximo a 1; el error relativo del 1 % exige... piensa en cuántas historias
independientes.
*Pista 2:* y una historia no es un neutrón: es una cadena de generaciones. Multiplica.
*Solución:* con un estimador de varianza relativa $\sim1$ por historia, un 1 %
exige $\sim10^4$ historias por generación, y hacen falta varias generaciones:
del orden de $10^5$–$10^6$ trayectorias. Cada una con decenas de colisiones y
varias operaciones por colisión: $10^7$–$10^8$ operaciones. El ENIAC hacía
$\sim300$ multiplicaciones/s, luego entre 10 y 100 horas de cálculo. Coincide
con lo documentado: los primeros cálculos Monte Carlo en el ENIAC duraban días.

---

### Modelado

**9.M1** El suceso tiene probabilidad $\sim20\times10^{-3}=2\%$ si basta con
que falle uno, y $\sim10^{-60}$ si tienen que fallar todos. En el primer caso el
muestreo directo va bien. En el segundo es imposible y hay que usar importancia
(sesgando las probabilidades de fallo hacia arriba y corrigiendo con pesos) o
*splitting*. **La decisión depende del suceso, no del sistema**, y esa
distinción es la clave del problema.

**9.M2** Ordenadas por eficiencia esperada: (1) muestreo por importancia con
una propuesta centrada en el pico; (2) estratificación con una región fina
alrededor del pico; (3) Monte Carlo puro. La primera puede ganar varios órdenes
de magnitud; la tercera puede no encontrar el pico jamás.

**9.M3** ● *Pista 1:* calcula qué fracción de un cubo ocupa la bola inscrita en dimensión 20 y verás por qué el rechazo desde un cubo envolvente es inviable.
*Pista 2:* si no puedes muestrear de golpe, camina. Una cadena de Markov confinada al cuerpo no necesita conocer su volumen para explorarlo.
*Solución:* El rechazo desde un cubo envolvente en $d=20$ no funciona. La
solución práctica es **una cadena de Markov confinada al politopo**: propone
movimientos y rechaza los que salen (algoritmo *hit-and-run*), que en cuerpos
convexos tiene garantías teóricas de mezcla polinómica en $d$. Es uno de los
resultados más bonitos del área: el volumen de un convexo en dimensión alta es
aproximable en tiempo polinómico por MCMC, y **no** por ningún método
determinista conocido (Dyer, Frieze y Kannan, 1991).

---

### Derivación

**9.D1** Sea $y$ la distancia del centro de la aguja a la línea más cercana,
uniforme en $[0,D/2]$, y $\theta$ el ángulo, uniforme en $[0,\pi/2]$. Cruza si
$y\le(L/2)\sin\theta$. Entonces
$$P=\frac{2}{D}\cdot\frac{2}{\pi}\int_0^{\pi/2}\frac{L}{2}\sin\theta\,d\theta
=\frac{2L}{\pi D}$$
Nótese que $\pi$ aparece **por la integral sobre el ángulo**: ahí está la
geometría.

**9.D2** $E[\hat I]=\frac{1}{N}\sum E[f(x_i)]=E[f]=I$: insesgado sin necesidad
de independencia. La varianza sí la necesita:
$\operatorname{Var}(\sum f_i)=\sum\operatorname{Var}(f_i)$ requiere covarianzas
nulas. **Por eso el sesgo no es el problema en MCMC y la varianza sí.**

**9.D3** ● *Pista 1:* escribe la probabilidad de transición completa $T(x\to y)=q(y|x)\alpha(x\to y)$ y separa los casos $p(y)<p(x)$ y $p(y)>p(x)$.
*Pista 2:* comprueba primero el balance detallado, y después súmalo sobre $x$: la estacionariedad sale sola.
*Solución:* Con $T(x\to y)=q(y|x)\min(1,p(y)/p(x))$ y $q$ simétrica, si
$p(y)<p(x)$: $p(x)T(x\to y)=p(x)q\,\frac{p(y)}{p(x)}=q\,p(y)$ y
$p(y)T(y\to x)=p(y)q\cdot1=q\,p(y)$. Iguales. Sumando el balance detallado
sobre $x$: $\sum_x p(x)T(x\to y)=p(y)\sum_x T(y\to x)=p(y)$, luego $p$ es
estacionaria.
**No es necesario**: es suficiente. Existen cadenas sin balance detallado
(*lifting*, MCMC no reversible) que convergen a la misma $p$ y a veces mezclan
mucho mejor. Es un área activa.

**9.D4** ● *Pista 1:* escribe la varianza del estimador de muestreo por importancia y pregúntate qué $q$ la anula exactamente.
*Pista 2:* cuando la encuentres, mira su constante de normalización. Ahí está el chiste.
*Solución:* La varianza es cero si $q^*(x)\propto |f(x)|p(x)$. Pero la constante
de normalización de esa $q^*$ es precisamente $\int|f|p$, es decir,
esencialmente la integral que queríamos calcular. **La propuesta óptima
requiere conocer la respuesta.** La lección práctica: no busques la óptima,
busca una que se le parezca en la región donde $|f|p$ es grande y que tenga
colas más pesadas. La segunda condición no es opcional.

---

### Computacional

**9.P1** Sale $-0{,}50\pm0{,}02$ con suficiente rango. Si sale distinto,
sospecha del generador o de que estés midiendo el error de una sola realización
en lugar de la desviación típica sobre repeticiones.

**9.P2** Con $d$ dimensiones independientes, $M$ se eleva a la $d$ y la
aceptación cae como $M^{-d}$. Con $M=1{,}75$ por dimensión, en $d=10$ la
aceptación es $1{,}75^{-10}=0{,}3\%$; en $d=20$, $10^{-5}$.

**9.P3** RANDU cumple $x_{n+2}=6x_{n+1}-9x_n \pmod{2^{31}}$, y esa relación
lineal exacta confina las tripletas a 15 planos. Con PCG64 no se ve ninguna
estructura. Es una demostración visual de por qué las pruebas espectrales
existen.

---

### Experimento

**9.X1** Orden típico de eficiencia para una función suave en $d$ moderada:
Sobol > estratificado > antitéticas > puro. Las antitéticas sólo ayudan si la
función es monótona; con funciones simétricas pueden no ayudar nada. La
estratificación nunca empeora.

**9.X2** ● *Pista 1:* no compares tiempos de ejecución: compara $N_{\text{ef}}$ por unidad de coste, contando las $K$ cadenas del templado.
*Pista 2:* haz el barrido en altura de barrera. Hay un punto por debajo del cual la técnica sofisticada pierde.
*Solución:* El templado paralelo consigue un factor 10–100 en $N_{\text{ef}}$
para barreras moderadas, a costa de correr $K$ cadenas. La ganancia neta es
positiva si la barrera es lo bastante alta; con barreras pequeñas, el
Metropolis simple con paso grande es más eficiente. **La técnica sofisticada no
siempre gana**, y medir es la única forma de saberlo.

---

### Detective

**9.T1** Falta $\tau_{\text{int}}$ o $N_{\text{ef}}$. La barra puede estar
subestimada por un factor $\sqrt{\tau_{\text{int}}}$, que en problemas
realistas está entre 3 y 100. Es el error más frecuente en la literatura que
usa MCMC, y produce discrepancias aparentes de muchas sigmas entre trabajos
perfectamente compatibles.

**9.T2** Los pesos de importancia tienen varianza infinita o casi: la propuesta
tiene colas más ligeras que el objetivo, así que unas pocas muestras con peso
gigantesco dominan el estimador. El diagnóstico estándar es el **tamaño
efectivo de muestra de los pesos**,
$N_{\text{ef}}=(\sum w)^2/\sum w^2$: si sale del orden de 1 o 2 con $10^6$
muestras, el estimador está dominado por una sola muestra. Hay que cambiar la
propuesta, no aumentar $N$.

**9.T3** ● *Pista 1:* con $N$ tiradas y probabilidad de cruce $p$, el número de cruces es binomial. Calcula su desviación típica.
*Pista 2:* ahora calcula cuánto mueve la estimación de $\pi$ **un solo cruce** y compáralo con la precisión que Lazzarini anunció.
*Solución:* Con $N=3408$ y $p=2/\pi$, la desviación típica del número de cruces
es $\sqrt{Np(1-p)}=\sqrt{3408\times0{,}637\times0{,}363}=28{,}1$. Para obtener
$\pi=355/113$ hace falta un número exacto de cruces; la sensibilidad es
$d(\text{estimación})/d(\text{cruces})\approx\pi/N_{\text{cruces}}\approx1{,}4
\times10^{-3}$ por cruce. Es decir, **un solo cruce de diferencia mueve la
estimación en $10^{-3}$**, mil veces más que el error reportado de
$2{,}7\times10^{-7}$. La conclusión es inmediata: ningún experimento con 3408
agujas puede resolver seis decimales, hiciera lo que hiciera. Sólo se obtiene
ese número si se para exactamente cuando aparece, y el número 3408 lo delata:
es $113\times k$ con $k$ elegido para que salga la fracción de Zu Chongzhi.

---

### Feynman

**9.F1** Guion: «Imagina que quieres saber qué superficie tiene un lago de
forma rarísima. Puedes medirlo con precisión, que es dificilísimo, o puedes
tirar piedras al azar dentro de un rectángulo que lo contenga y contar cuántas
caen en el agua. La proporción te da el área. El lago no tiene nada de
aleatorio: lo aleatorio es tu manera de mirarlo, y funciona porque preguntando
al azar muchas veces acabas preguntando en todas partes.»

**9.F2** Guion: «Para saber si prefieres A o B no hace falta saber cuánto vale
todo lo demás: basta comparar A con B. La constante que falta aparece arriba y
abajo en la comparación y se va. Como el método sólo hace comparaciones, nunca
necesita el número imposible de calcular. Por eso se puede simular un sistema
con más configuraciones que átomos hay en el universo.»

---

### Extensión

**9.Z1** ★ *Pista 1:* separa lo que la carta dice sobre la **máquina** de lo que dice sobre el **método**.
*Pista 2:* tacha todo lo que sea específico del ENIAC. Lo que queda es lo que escribirías hoy, y esa es la respuesta.
*Solución:* Lo que ha cambiado: la carta de von Neumann especifica el orden de
las operaciones, el uso de registros y el formato de los números, porque el
ENIAC se programaba con cables. Lo que **no** ha cambiado: la estructura
lógica del cálculo —muestrear una trayectoria, seguirla, acumular estadística—
es exactamente la que se escribiría hoy, y la discusión sobre estimadores y
varianza es reconocible sin esfuerzo. La lección: la parte perecedera de un
programa es la implementación; la parte duradera es el diseño del estimador.

**9.Z2** ★ *Pista 1:* HMC gana donde la geometría es suave y el problema es la dimensión, porque usa el gradiente para proponer movimientos lejanos.
*Pista 2:* pregúntate qué hace una trayectoria de energía constante frente a una barrera de energía alta. La respuesta explica por qué la bimodal no mejora.
*Solución:* En una gaussiana de dimensión 50, HMC consigue $N_{\text{ef}}$ por
gradiente órdenes de magnitud mejor que Metropolis, porque explota la geometría
y propone movimientos lejanos con aceptación alta. En la bimodal **falla igual
que Metropolis**: HMC sigue trayectorias de energía constante, y una barrera de
energía alta sigue siendo una barrera. La lección general: HMC resuelve el
problema de la dimensión, no el de la multimodalidad. Para eso hacen falta
técnicas de temperatura (templado) o de saltos de modo.
