## Soluciones del capítulo 11

> Las soluciones son razonadas: el número final es lo menos importante. En los
> problemas ● y ★ con solución cerrada hay **Pista 1** y **Pista 2** antes de
> ella; tápalas con la mano y úsalas de una en una.
>
> Los de **Mundo real** (R) no llevan solución a propósito: su procedimiento
> está en el apéndice D.

---

### Calentamiento

**11.C1** $\lambda=3$ con $\mathbf{v}=(1,1)/\sqrt2$ y $\lambda=1$ con
$\mathbf{v}=(1,-1)/\sqrt2$. Interpretación: el modo simétrico (las dos masas en
fase) y el antisimétrico (en oposición). **La simetría del sistema aparece en
los autovectores sin haberla impuesto**, y ese es un patrón general: las
simetrías del problema estructuran su espectro.

**11.C2** $\kappa=10^6$; se pierden $\log_{10}10^6=6$ cifras. De 16 quedan 10.

**11.C3** El salto entre 12 y 0,3 sugiere rango efectivo 3. Pero para decidirlo
bien hace falta **el nivel de ruido de los datos**: si el ruido produce valores
singulares del orden de 0,25, entonces 0,3 es indistinguible de ruido y el
rango es 3. Si el ruido es de 0,01, ese 0,3 es señal débil pero real.

**11.C4** Los valores singulares de $A^TA$ son los cuadrados de los de $A$,
luego $\kappa(A^TA)=(\sigma_{\max}/\sigma_{\min})^2=\kappa(A)^2$.

---

### Estimación

**11.E1** Denso: $(10^5)^2\times8$ B $=80$ GB de memoria —imposible en un
portátil— y $\mathcal{O}(n^3)/3\approx3\times10^{14}$ flops, unas horas. Disperso
con 7 no nulos/fila: $7\times10^5\times8$ B $=5{,}6$ MB, y un método iterativo
converge en cientos de iteraciones de $\mathcal{O}(7n)$: **milisegundos**. Ocho
órdenes de magnitud de diferencia, por la estructura y no por el hardware.

**11.E2** $\kappa$ de Vandermonde crece exponencialmente con el grado; para
grado 20 en $[0,1]$ está en torno a $10^{16}$. **No se puede** ajustar un
polinomio de grado 20 en base de monomios en doble precisión. Sí se puede en
base de Chebyshev, donde $\kappa$ es modesto. La lección: el problema estaba
bien planteado; la **parametrización** era el desastre.

**11.E3** ● *Pista 1:* la pregunta no es cuántos píxeles tiene una cara, sino cuántos grados de libertad tiene **el conjunto** de caras.
*Pista 2:* piensa en qué varía de verdad entre dos retratos: iluminación, pose, identidad. Son pocas cosas, y cada una aporta unas cuantas dimensiones.
*Solución:* Con 10 000 píxeles por imagen, la experiencia de *eigenfaces*
(Turk y Pentland, 1991) indica que del orden de 50–150 componentes bastan para
reconstrucción visualmente aceptable. Es un factor de compresión ~100 y refleja
que las caras viven en una variedad de dimensión mucho menor que el espacio de
píxeles. Esa observación —**los datos reales ocupan una variedad de baja
dimensión**— es la base de casi todo el aprendizaje de representaciones.

---

### Modelado

**11.M1** Autovalores negativos = tasas de relajación; su inverso, los tiempos
característicos. Si el sistema es cerrado (conserva masa), la suma de cada
columna es cero y **hay un autovalor exactamente 0**, cuyo autovector es la
distribución de equilibrio. Ese cero no es un accidente numérico: es la ley de
conservación escrita en forma de álgebra lineal.

**11.M2** $\lambda_1=1$ siempre (Perron–Frobenius), y su autovector izquierdo
es la distribución estacionaria. El segundo autovalor en módulo, $|\lambda_2|$,
controla la velocidad de convergencia: el error decae como $|\lambda_2|^n$, y
$-1/\ln|\lambda_2|$ es el tiempo de mezcla. Es exactamente lo que gobierna la
autocorrelación de un MCMC (capítulo 9).

**11.M3** ● *Pista 1:* escribe la difusión en la red como $\dot x=-Lx$ con $L$ el laplaciano y diagonaliza.
*Pista 2:* el modo que manda a tiempos largos es el más lento, y su autovalor tiene nombre propio. Mira cuánto vale en una red con comunidades separadas.
*Solución:* La velocidad de homogeneización es $\lambda_2$ del laplaciano
(conectividad algebraica): el modo más lento decae como $e^{-\lambda_2 t}$. En
redes de mundo pequeño, $\lambda_2$ es grande y la propagación es rapidísima;
en redes con comunidades separadas, $\lambda_2$ es diminuto y aparecen dos
escalas: rápido dentro de cada comunidad, lentísimo entre ellas. La simulación
lo reproduce y **el autovector de $\lambda_2$ dibuja exactamente la frontera
entre comunidades**.

---

### Derivación

**11.D1** Si $A\mathbf{u}=\lambda\mathbf{u}$ y $A\mathbf{v}=\mu\mathbf{v}$ con
$\lambda\ne\mu$: $\lambda\mathbf{v}^T\mathbf{u}=\mathbf{v}^TA\mathbf{u}
=(A\mathbf{v})^T\mathbf{u}=\mu\mathbf{v}^T\mathbf{u}$, luego
$(\lambda-\mu)\mathbf{v}^T\mathbf{u}=0$ y el producto escalar es nulo.

**11.D2** $A^TA=V\Sigma^2V^T$ y $AA^T=U\Sigma^2U^T$. Los valores singulares son
las raíces porque $A^TA$ aplica la transformación **dos veces**: una vez $A$ y
otra su traspuesta.

**11.D3** ● *Pista 1:* escribe el error en norma de Frobenius en la base de vectores singulares; se convierte en una suma de cuadrados.
*Pista 2:* la parte no trivial es probar que ninguna $B$ de rango $k$ lo hace mejor. Ahí entra la desigualdad de Weyl.
*Solución:* Es la desigualdad de Weyl más un argumento de ortogonalidad: para
cualquier $B$ de rango $k$, $\|A-B\|_F^2\ge\sum_{j>k}\sigma_j^2$, con igualdad
al truncar. Nota importante: el teorema vale también en norma 2 (Mirsky), y en
general para toda norma unitariamente invariante. Es uno de los resultados más
usados de las matemáticas aplicadas.

**11.D4** ● *Pista 1:* diagonaliza y acota $\|e^{At}\|$ con la norma del cambio de base por delante y por detrás.
*Pista 2:* la cota que sale es correcta. Evalúala con $\kappa(V)=400$ y pregúntate si te dice algo útil.
*Solución:* $e^{At}=Ve^{\Lambda t}V^{-1}$, luego
$\|e^{At}\|\le\|V\|\|e^{\Lambda t}\|\|V^{-1}\|=\kappa(V)e^{\lambda_{\max}t}$.
La cota es correcta y **inútil** cuando $\kappa(V)$ es enorme: con
$\kappa(V)=400$, la cota permite amplificaciones de 400 sin decir nada sobre
cuándo ni cuánto ocurren de verdad. Por eso hacen falta los pseudoespectros:
dan información sobre el transitorio, no sólo una cota.

---

### Computacional

**11.P1** Con 10 masas, los modos son **senos discretizados**:
$v_j^{(k)}\propto\sin(jk\pi/(n+1))$. No es casualidad: la matriz de muelles es
el laplaciano discreto en 1D, cuyos autovectores son exactamente las funciones
propias del laplaciano continuo con condiciones de contorno fijas. **Ahí está
el puente al capítulo 12**: Fourier es la diagonalización del laplaciano.

**11.P2** Ecuaciones normales: el error crece como $\kappa^2\epsilon$. QR y SVD:
como $\kappa\epsilon$. Con $\kappa=10^8$, las normales dan cero cifras
correctas y QR da ocho. La diferencia es exactamente el cuadrado.

**11.P3** Para imágenes naturales, el error del 1 % en norma de Frobenius se
alcanza típicamente con un rango del 10–20 % del mínimo de las dimensiones.
Nota: el error en norma de Frobenius **no** coincide con el error perceptual;
el ojo es mucho más sensible a los bordes que a la energía total.

---

### Experimento

**11.X1** Para una matriz $m\times n$ de entradas i.i.d. con $m/n\to\gamma$,
los valores singulares al cuadrado se distribuyen según la ley de
Marchenko–Pastur, con soporte acotado en
$\sigma^2(1\pm\sqrt\gamma)^2$. **El resultado práctico es un umbral**: todo
valor singular por encima del borde superior es señal; todo lo de dentro es
compatible con ruido puro. Es el criterio principiado que faltaba en 11.C3.

**11.X2** ● *Pista 1:* construye matrices $2\times2$ con los mismos autovalores y autovectores cada vez menos ortogonales, y mide $\max_t\|e^{At}\|$.
*Pista 2:* haz también el caso ortogonal. Que dé exactamente 1 es la mitad de la respuesta.
*Solución:* La amplificación transitoria máxima crece aproximadamente de forma
lineal con $\kappa(V)$ para no normalidad moderada, y el instante del máximo
crece con el logaritmo. Con autovectores ortogonales ($\kappa(V)=1$) no hay
amplificación ninguna: la no normalidad es **condición necesaria** del
crecimiento transitorio.

---

### Detective

**11.T1** Las ecuaciones normales han elevado al cuadrado el condicionamiento;
con $\kappa(A)\sim10^8$ el sistema resultante es numéricamente singular y el
resultado depende del orden de las operaciones, que a su vez depende del orden
de las columnas. La solución es QR o SVD, no reordenar mejor.

**11.T2** Es un **artefacto de escalado**. En unidades del SI, las presiones
tienen valores numéricos $10^5$ veces mayores que los caudales, y el PCA sin
estandarizar maximiza varianza en esas unidades. El resultado se convierte en
«la variable con los números más grandes». Comprobación inmediata: repetir con
la matriz de correlación en lugar de la de covarianza.

**11.T3** ● *Pista 1:* «linealmente estable» y «estable» no son lo mismo cuando el operador no es normal.
*Pista 2:* dibuja $\|e^{At}\|$ frente a $t$. Si sube órdenes de magnitud antes de bajar, ya tienes la explicación.
*Solución:* Comprobaría la **no normalidad** del operador linealizado:
calcularía $\kappa(V)$ de la matriz de autovectores y, sobre todo, la curva
$\|e^{At}\|$ frente a $t$. Si hay amplificación transitoria de órdenes de
magnitud, el sistema es linealmente estable y prácticamente inestable, porque
cualquier perturbación finita alcanza amplitudes donde las no linealidades
mandan. Es exactamente el caso de Poiseuille, y la conclusión es que el
experimento estaba bien y el análisis respondía a otra pregunta.

---

### Feynman

**11.F1** Guion: «Coge tres pesos unidos por muelles. Si los sueltas de
cualquier manera, se mueven de una forma complicadísima. Pero hay tres maneras
especiales de soltarlos en las que todos oscilan a la vez, con la misma
frecuencia, manteniendo la forma: uno todos hacia el mismo lado, otro los
extremos en contra del centro, y otro alternando. Esas tres formas son los
autovectores. Y lo bonito es que **cualquier** movimiento posible es una mezcla
de esos tres, cada uno con su ritmo. Diagonalizar es encontrar esas maneras
especiales.»

**11.F2** Guion: «Resolver dos ecuaciones es cortar dos rectas. Si se cortan en
ángulo recto, mover un poco una de ellas mueve un poco el punto de corte. Si
son casi paralelas, moverla un pelo desplaza el corte kilómetros. El número de
condición mide exactamente eso: cuánto de paralelas son. Y no lo arregla ningún
algoritmo, porque el problema no está en cómo calculas: está en que la
pregunta, con esos datos, no tiene una respuesta bien definida.»

---

### Extensión

**11.Z1** ★ *Pista 1:* el pseudoespectro se define con la norma de la resolvente, y se calcula con el menor valor singular de $zI-A$ sobre una malla del plano.
*Pista 2:* lo que añade sobre el espectro es una pregunta que el espectro no responde: **cuánto se mueven los autovalores si perturbas la matriz**.
*Solución:* El $\epsilon$-pseudoespectro es el conjunto de $z$ tales que
$\|(zI-A)^{-1}\|>1/\epsilon$, o equivalentemente los autovalores de $A+E$ para
alguna perturbación con $\|E\|<\epsilon$. Se calcula evaluando el menor valor
singular de $zI-A$ sobre una malla del plano complejo. Añade la información
crucial: **cuánto se mueven los autovalores ante perturbaciones**. Para la
matriz del capítulo, el pseudoespectro se extiende muy hacia la derecha aunque
los autovalores estén en $-1$ y $-2$, y esa extensión es precisamente la que
predice la amplificación transitoria.

**11.Z2** ★ *Pista 1:* si sólo quieres los $k$ primeros valores singulares, no necesitas la matriz entera: proyéctala sobre un subespacio aleatorio de dimensión algo mayor que $k$.
*Pista 2:* cuenta las operaciones de las dos versiones y verás dónde está la ganancia. Sobremuestrear unas 10 dimensiones basta.
*Solución:* La SVD aleatorizada proyecta $A$ sobre un subespacio aleatorio de
dimensión $k+p$ (con $p\sim10$ de sobremuestreo), calcula una base ortonormal y
hace la SVD de la matriz pequeña resultante. Coste $\mathcal{O}(mnk)$ frente a
$\mathcal{O}(mn^2)$. Para $5000\times5000$ con rango efectivo 50, es unas cien
veces más rápida y el error queda a un factor pequeño del óptimo con
probabilidad altísima. Lo que se pierde: la garantía determinista, sustituida
por una cota probabilística. En la práctica, con un par de iteraciones de
potencia, la diferencia es indetectable.
