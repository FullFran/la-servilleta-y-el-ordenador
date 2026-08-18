## Problemas del capítulo 9

**Marcas:** ○ directo · ◐ requiere pensar · ● difícil · ★ abierto.

---

### Calentamiento

**9.C1** ○ Estimas una probabilidad $p\approx0{,}3$ con $N=10^4$ muestras.
¿Cuál es tu barra de error? ¿Y para llegar a $\pm0{,}001$?

**9.C2** ○ Un integrando tiene $\sigma_f=2$ y necesitas error $10^{-3}$.
¿Cuántas muestras? ¿Y si consigues reducir $\sigma_f$ a 0,2?

**9.C3** ○ ¿Qué fracción del volumen de un cubo de lado 2 ocupa la esfera de
radio 1 inscrita, en $d=2,3,5,10,20$?

**9.C4** ○ Una cadena de MCMC tiene $N=10^5$ y $\tau_{\text{int}}=250$. ¿Cuál
es su tamaño efectivo? ¿Por cuánto hay que multiplicar la barra de error
ingenua?

---

### Estimación

**9.E1** ◐ Estima cuánto tiempo de CPU costaría calcular $\pi$ con seis
decimales por Monte Carlo. Compáralo con la edad del universo si hace falta.

**9.E2** ◐ Estima el número de configuraciones de un modelo de Ising de
$20\times20$ espines. Compáralo con el número de átomos del Sol.

**9.E3** ● Estima cuántas trayectorias de neutrones habría que simular para
calcular la masa crítica de una esfera de uranio con un 1 % de precisión.
Compáralo con lo que podía hacer el ENIAC (unas 300 multiplicaciones por
segundo).

---

### Modelado

**9.M1** ◐ Quieres estimar la probabilidad de que un sistema con 20 componentes
falle. Cada uno falla con probabilidad $10^{-3}$. Diseña la estrategia de
muestreo: ¿directo o por importancia? Justifica con números.

**9.M2** ◐ Tienes que integrar una función con un pico estrecho y alto en una
región pequeña de un dominio grande. Enumera tres estrategias y ordénalas por
eficiencia esperada.

**9.M3** ● Diseña un método de Monte Carlo para estimar el volumen de la
intersección de 50 semiespacios en dimensión 20. ¿Funciona el rechazo? ¿Qué
harías si la tasa de aceptación fuese $10^{-9}$?

---

### Derivación

**9.D1** ◐ Deduce la probabilidad de cruce en el problema de Buffon,
$P=2L/(\pi D)$, integrando sobre posición y ángulo.

**9.D2** ◐ Demuestra que el estimador de Monte Carlo es insesgado y que su
varianza es $\operatorname{Var}(f)/N$. ¿Dónde se usa la independencia?

**9.D3** ● Demuestra que la elección de Metropolis satisface el balance
detallado, y que el balance detallado implica que $p$ es estacionaria. ¿Es el
balance detallado necesario, o sólo suficiente?

**9.D4** ● Deduce la propuesta óptima del muestreo por importancia (la que da
varianza cero) y explica por qué en general no se puede usar. ¿Qué te dice eso
sobre cómo elegirla en la práctica?

---

### Computacional

**9.P1** ○ Estima $\pi$ por Monte Carlo, dibuja el error frente a $N$ en
log-log y mide la pendiente. ¿Sale $-1/2$?

**9.P2** ◐ Implementa muestreo por rechazo de una distribución bimodal y mide
la tasa de aceptación en función de la dimensión al extenderla a $d$
dimensiones independientes. Comprueba la caída exponencial.

**9.P3** ◐ Reproduce el experimento de RANDU: genera tripletas consecutivas y
dibújalas en 3D. Encuentra el ángulo desde el que se ven los 15 planos.
Repítelo con PCG64.

---

### Experimento

**9.X1** ◐ Compara Monte Carlo puro, antitéticas, estratificado y Sobol sobre
la misma integral. Dibuja error frente a coste. Ordena por eficiencia.

**9.X2** ● Implementa templado paralelo (varias cadenas a distintas
«temperaturas» que intercambian estados) sobre la distribución bimodal y
compara $N_{\text{ef}}$ con el Metropolis simple. ¿Cuánto ganas, y a qué coste?

---

### Detective

**9.T1** ◐ Un resultado de MCMC con $10^6$ muestras se publica con barra
$\sigma/\sqrt{10^6}$. ¿Qué falta, y por cuánto puede estar equivocada la barra?

**9.T2** ◐ Una estimación por importancia de un suceso raro da un valor con una
barra de error minúscula, pero al repetir con otra semilla cambia por un factor
100. ¿Qué está pasando?

**9.T3** ● Un artículo estima $\pi$ con 3408 lanzamientos de aguja y obtiene
$355/113$. Construye el argumento estadístico completo que demuestra que el
resultado no puede ser honesto, y calcula la probabilidad correspondiente.

---

### Mundo real

**9.R1** ★ Coge un cálculo de incertidumbre de tu trabajo que se haga con
propagación de fórmulas. Rehazlo por Monte Carlo. ¿Coinciden? ¿Dónde no?

**9.R2** ★ Busca en tu campo un resultado publicado obtenido con MCMC. ¿Reporta
$N_{\text{ef}}$ o $\hat R$? ¿Qué fracción de los artículos lo hace?

---

### Feynman

**9.F1** ○ Explica sin fórmulas cómo puede el azar calcular algo determinista.

**9.F2** ◐ Explica por qué en Metropolis no hace falta conocer la constante de
normalización, y por qué eso es tan importante.

---

### Extensión

**9.Z1** ★ Lee la carta de von Neumann a Richtmyer de 1947 (reproducida en
Eckhardt 1987). Compara su plan de cálculo con cómo escribirías hoy el mismo
programa. ¿Qué ha cambiado y qué no?

**9.Z2** ★ Estudia Hamiltonian Monte Carlo (Betancourt 2017) e impleméntalo
para una gaussiana en dimensión 50. Compara $N_{\text{ef}}$ por evaluación de
gradiente con Metropolis. Después pruébalo en la bimodal: ¿qué pasa, y por qué?
