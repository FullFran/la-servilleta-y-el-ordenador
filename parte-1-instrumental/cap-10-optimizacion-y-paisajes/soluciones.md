## Soluciones del capítulo 10

> Las soluciones son razonadas: el número final es lo menos importante. En los
> problemas ● y ★ con solución cerrada hay **Pista 1** y **Pista 2** antes de
> ella; tápalas con la mano y úsalas de una en una.
>
> Los de **Mundo real** (R) no llevan solución a propósito: su procedimiento
> está en el apéndice D.

---

### Calentamiento

**10.C1** $H=\operatorname{diag}(2,2a)$, $\kappa=\max(a,1/a)$. Tasas:
$a=1\Rightarrow\kappa=1$, tasa 0 (converge en un paso); $a=10\Rightarrow$
tasa $9/11=0{,}82$; $a=1000\Rightarrow$ tasa $0{,}998$, y hacen falta
$\sim\ln(10^{-6})/\ln(0{,}998)\approx6900$ iteraciones para seis cifras.

**10.C2** $x^2-y^2$: silla en el origen. $x^4+y^4$: mínimo, pero el hessiano es
**nulo** allí y la convergencia de Newton deja de ser cuadrática. $x^2+y^3$:
punto crítico degenerado; a lo largo de $y$ es un punto de inflexión, luego no
es ni mínimo ni máximo.

**10.C3** $e^{-0{,}5}=0{,}61$; $e^{-5}=0{,}0067$. Con $T=0{,}1$:
$e^{-5}=0{,}0067$ y $e^{-50}=2\times10^{-22}$. **La temperatura fija qué
tamaño de barrera es cruzable.**

**10.C4** Con $\rho\approx-1$, la **suma** $\theta_1+\theta_2$ está bien
determinada y la diferencia no. Es la situación del problema 5.C4 y la señal de
que hay que reparametrizar.

---

### Estimación

**10.E1** $20^8=2{,}6\times10^{10}$ evaluaciones. A 1 ms cada una, **300 días**.
BFGS con gradiente resuelve el mismo problema en decenas de iteraciones, es
decir, segundos. La búsqueda en rejilla en más de 4 o 5 dimensiones no es una
opción, y sin embargo se sigue viendo.

**10.E2** $(30-1)!/2\approx4{,}4\times10^{30}$. La Tierra tiene $\sim10^{50}$
átomos, así que aquí gana la Tierra; pero con 60 ciudades son $10^{80}$, del
orden de los átomos del universo observable. Y el viajante con 60 ciudades se
resuelve exactamente hoy en día, lo cual dice mucho sobre la diferencia entre
«número de posibilidades» y «dificultad real».

**10.E3** ● *Pista 1:* cuenta cuántas evaluaciones cuesta un gradiente por diferencias finitas cuando hay $n$ parámetros.
*Pista 2:* ahora piensa cuántas cuesta en modo inverso. La respuesta no contiene $n$, y ahí está toda la diferencia.
*Solución:* Diferencias finitas: cada gradiente cuesta $n+1=13$ evaluaciones,
13 s. Con 100 iteraciones, 22 minutos. Diferenciación automática en modo
inverso: **un gradiente cuesta del orden de 2–4 veces una evaluación**,
independientemente de $n$. Serían ~3 s por gradiente, 5 minutos en total. Y la
ventaja crece linealmente con $n$: con 1000 parámetros, el factor es 250.

---

### Modelado

**10.M1** (a) Minimizar energía potencial sujeto a longitud fija: **convexo**
(la catenaria). (b) Depende: con función de utilidad cóncava y restricciones
lineales, convexo; con recursos enteros, no. (c) Con pérdida de Huber,
**convexo**; con recuento de atípicos ($\ell_0$), no.

**10.M2** BFGS construye su aproximación del hessiano a partir de diferencias
de gradientes, y con ruido esas diferencias son basura: la aproximación se
corrompe y el método diverge o se para prematuramente. Métodos adecuados:
Nelder–Mead (tolerante al ruido, hasta ~10 dimensiones), CMA-ES, o algoritmos
de optimización estocástica con promediado. Y siempre: **fija las semillas** de
las simulaciones para que la función sea determinista.

**10.M3** ● *Pista 1:* un mínimo estrecho y otro ancho valen lo mismo en $f$, así que la función objetivo tal cual no distingue lo que te importa. Cámbiala.
*Pista 2:* promedia $f$ sobre perturbaciones del tamaño de tu tolerancia de fabricación. El mínimo estrecho no sobrevive al promedio.
*Solución:* Se penaliza la curvatura o se optimiza el valor **promediado sobre
perturbaciones**: $\tilde f(x)=E_{\delta}[f(x+\delta)]$ con $\delta$ del tamaño
de la incertidumbre real de implementación. Esto suaviza los mínimos estrechos
y deja intactos los anchos. El peso lo fija la magnitud física de $\delta$:
si tus componentes tienen tolerancia del 5 %, ese es el $\delta$. Es
optimización robusta, y es exactamente lo que faltaba en el anti-ejemplo.

---

### Derivación

**10.D1** Para $f=\tfrac12 x^TAx$, un paso da $x_{k+1}=(I-\alpha A)x_k$. El
factor de contracción en la dirección $i$ es $|1-\alpha\lambda_i|$; el $\alpha$
óptimo iguala los extremos, $\alpha=2/(\lambda_{\min}+\lambda_{\max})$, y el
factor resultante es $(\kappa-1)/(\kappa+1)$.

**10.D2** Minimizando $f(x)+g^T d+\tfrac12 d^THd$ respecto a $d$:
$Hd=-g$. Si $H$ no es definido positivo, ese $d$ puede ser una dirección de
**ascenso** ($d^Tg>0$), y el paso empeora. Remedios: modificar $H$ sumándole
$\mu I$ (Levenberg–Marquardt), o usar una región de confianza.

**10.D3** ● *Pista 1:* desarrolla la energía a segundo orden alrededor del mínimo y mete eso en $e^{-E/T}$.
*Pista 2:* sale una gaussiana. Mira cómo depende su anchura de $T$, y después compara las probabilidades de dos mínimos separados $\Delta E$.
*Solución:* Cerca del mínimo, $E\approx E_0+\tfrac12 k(x-x_0)^2$, luego
$p\propto e^{-k(x-x_0)^2/2T}$: una gaussiana de anchura
$\sigma=\sqrt{T/k}$. **La anchura va como $\sqrt T$**: al bajar la temperatura,
la distribución se estrecha alrededor del mínimo global, y el cociente de
probabilidades entre dos mínimos separados $\Delta E$ es $e^{-\Delta E/T}$, que
tiende a 0 o a $\infty$.

**10.D4** ● *Pista 1:* escribe las condiciones KKT con cuidado, incluida la holgura complementaria $\mu g=0$.
*Pista 2:* deriva el óptimo respecto del lado derecho de la restricción. Lo que salga **es** el multiplicador, y eso le da su significado físico.
*Solución:* $\nabla f+\mu\nabla g=0$, $\mu\ge0$, $\mu g=0$ (holgura
complementaria). El multiplicador $\mu$ es $-\partial f^*/\partial b$ cuando la
restricción es $g\le b$: **cuánto mejoraría el óptimo por relajar la
restricción una unidad**. En economía es el precio sombra; en física, una
fuerza de ligadura. La misma matemática con dos nombres.

---

### Computacional

**10.P1** Gradiente: la razón $\|e_{k+1}\|/\|e_k\|$ tiende a una constante
cercana a 1. Newton: $\|e_{k+1}\|/\|e_k\|^2$ tiende a una constante, y el
número de cifras correctas se duplica cada paso: 2, 4, 8, 16 cifras.

**10.P2** El enfriamiento geométrico $T_{k+1}=0{,}995\,T_k$ suele batir tanto
al rápido como al logarítmico en tiempo razonable. La curva típica muestra una
mejora rápida al principio y una larga cola de mejoras pequeñas: **saber cuándo
parar es parte del problema**, y el criterio honesto es «cuando el coste de
seguir supera el valor de la mejora esperada».

**10.P3** El histograma de $\tau_1$ y $\tau_2$ por separado es ancho y bimodal
(por la simetría de intercambio); el de $\tau_1+\tau_2$ es estrecho. La nube en
el plano $(\tau_1,\tau_2)$ dibuja el valle. Es el diagnóstico visual más
directo que existe.

---

### Experimento

**10.X1** Con ruido del 5 % y 25 puntos, la correlación supera 0,95 cuando las
dos constantes difieren menos de un factor ~2, y supera 0,99 por debajo de un
factor 1,5. Regla práctica ampliamente citada en cinética y farmacocinética:
**dos exponenciales sólo se separan si sus constantes difieren al menos un
factor 3**, y aun así hacen falta datos que cubran ambas escalas.

**10.X2** ● *Pista 1:* no barras sólo la dimensión: barre también la rugosidad del paisaje, con un parámetro que controle la amplitud del término oscilante.
*Pista 2:* dibuja el plano (dimensión, rugosidad) y marca quién gana en cada región. Verás que un eje manda mucho más que el otro.
*Solución:* BFGS gana en dimensión baja y con paisaje suave. Nelder–Mead
aguanta hasta $d\approx10$ y luego degenera. CMA-ES gana en paisajes rugosos a
partir de $d\approx5$, a costa de miles de evaluaciones. El cruce depende
mucho más de la **rugosidad** que de la dimensión, que es la moraleja del
capítulo.

---

### Detective

**10.T1** Tres posibilidades: (i) el «óptimo» está en la frontera de una
restricción y el gradiente no tiene que anularse allí; (ii) el criterio de
parada es por tamaño de paso y no por gradiente, y el método se ha atascado
en un valle; (iii) el gradiente que le pasas al optimizador **no es el
gradiente de la función que evalúa** —el error de implementación más frecuente
y el más difícil de ver—. Comprobación: compara tu gradiente analítico con uno
por diferencias finitas. Debería coincidir a 6–8 cifras.

**10.T2** El problema es que con 9 parámetros y 20 datos quedan 11 grados de
libertad; $\chi^2_\nu$ pasa de $45/17=2{,}6$ a $12/11=1{,}1$. Eso puede ser una
mejora real o sobreajuste. La comprobación que decide: **validación con datos
que no se han usado**, o un criterio que penalice parámetros (AIC/BIC), o mejor
las dos. Capítulo 15.

**10.T3** ● *Pista 1:* «siempre da lo mismo» tiene dos explicaciones aburridas antes que la interesante. Búscalas.
*Pista 2:* diseña un experimento que las separe: cambia el punto de partida dejando la semilla fija, y después al revés.
*Solución:* Explicaciones alternativas: (i) el enfriamiento es tan rápido que
el algoritmo es en realidad un descenso codicioso y siempre cae en el mismo
mínimo desde el mismo punto de partida; (ii) el generador aleatorio no está
sembrado con la semilla que cree. Cómo distinguirlas: cambiar el punto de
partida (si el resultado no cambia con arranque distinto **y** semilla
distinta, es (ii)); y medir la tasa de aceptación al principio (si empieza en
0,05 en vez de 0,8, el enfriamiento está mal calibrado).

---

### Feynman

**10.F1** Guion: «Imagina una canaleta larga y estrecha. La cuesta más
pronunciada no apunta hacia el fondo del valle, apunta hacia la pared de
enfrente, porque las paredes son mucho más empinadas que el suelo. Así que
cada vez que te dejas llevar por la pendiente cruzas de una pared a la otra y
sólo avanzas un poquito hacia el fondo. Cuanto más estrecha la canaleta, más
zigzag y menos avance.»

**10.F2** Guion: «Si enfrías un metal de golpe, cada átomo se queda donde
estaba y quedan defectos por todas partes. Si lo enfrías despacio, los átomos
tienen tiempo de moverse, deshacer las malas colocaciones y encontrar el sitio
que menos energía cuesta. El calor es lo que les permite deshacer errores. Un
algoritmo hace lo mismo: si sólo acepta mejoras se queda con el primer arreglo
que encuentra; si acepta empeorar un poco al principio, puede deshacer un mal
comienzo.»

---

### Extensión

**10.Z1** ★ *Pista 1:* calcula el hessiano en el óptimo y mira el espectro de autovalores en escala logarítmica.
*Pista 2:* si se reparten casi uniformemente sobre muchas décadas, la pregunta ya no es «¿está bien determinado el modelo?» sino «¿qué combinaciones lo están?».
*Solución:* Transtrum y colaboradores observan que en modelos con muchos
parámetros los autovalores del hessiano se reparten sobre muchos órdenes de
magnitud, casi uniformemente en escala logarítmica: hay unas pocas
combinaciones «rígidas» bien determinadas y muchísimas «blandas» que los datos
no tocan. La implicación es constructiva: **los modelos útiles son aquellos que
capturan las direcciones rígidas**, y a menudo existe un modelo reducido, con
muchos menos parámetros, que predice igual de bien. Es una justificación
cuantitativa del principio de modelo mínimo del capítulo 14.

**10.Z2** ★ *Pista 1:* lee el enunciado del teorema con lupa y subraya el «promediado sobre».
*Pista 2:* pregúntate si las funciones objetivo que aparecen en tu trabajo son una muestra uniforme de todas las funciones posibles. No lo son, y ahí está la salida.
*Solución:* El teorema dice que, **promediado sobre todas las funciones
objetivo posibles**, todos los algoritmos de búsqueda funcionan igual. Lo que
**no** dice es que todos funcionen igual en las funciones que aparecen en la
práctica. Y ahí está la salida: las funciones objetivo reales no son una
muestra uniforme del conjunto de todas las funciones; tienen estructura
—suavidad, jerarquía, cierta separabilidad— y los buenos algoritmos son los que
explotan esa estructura. El teorema es correcto y su moraleja práctica es la
contraria de la que se le suele atribuir.
