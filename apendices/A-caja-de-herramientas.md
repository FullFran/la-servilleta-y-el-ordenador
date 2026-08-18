# Apéndice A — Caja de herramientas matemática

> Todo lo que el libro usa, recopilado. No es un curso: es un recordatorio con
> las condiciones de validez incluidas, que es lo que suele faltar.

---

## A.1 Logaritmos y órdenes de magnitud

$$\log(ab)=\log a+\log b,\quad \log(a/b)=\log a-\log b,\quad \log(a^n)=n\log a$$

**Décadas útiles de memoria:** $\log_{10}2=0{,}30$, $\log_{10}3=0{,}48$,
$\log_{10}7=0{,}85$. Media década es un factor 3,2.

**Media geométrica:** $\sqrt{ab}$. Es la media aritmética en escala
logarítmica, y es el estimador correcto cuando sólo tienes cotas.

**Propagación multiplicativa:** si $Q=\prod x_i$ con errores logarítmicos
independientes, $\sigma_{\log Q}=\sqrt{\sum\sigma_i^2}$. *(Capítulo 1.)*

---

## A.2 Análisis dimensional

**Teorema π.** $n$ magnitudes con $k$ dimensiones independientes ($k$ = rango
de la matriz dimensional) dan $n-k$ grupos adimensionales.

**Receta:** lista variables → matriz dimensional → rango → elige $k$ variables
repetidas que contengan todas las dimensiones y no formen un grupo entre ellas
→ un grupo por cada variable restante → recombina para que signifiquen algo.

**Adimensionalizar una ecuación:** sustituye cada variable por (escala) ×
(adimensional) y elige las escalas para anular coeficientes. *(Capítulo 2.)*

---

## A.3 Probabilidad

$$E[aX+bY]=aE[X]+bE[Y]\ \text{(siempre)}$$
$$\operatorname{Var}(X+Y)=\operatorname{Var} X+\operatorname{Var} Y+2\operatorname{Cov}(X,Y)$$

**Bayes:** $P(A\mid B)=P(B\mid A)P(A)/P(B)$.

**Distribuciones y sus mecanismos:**

| Distribución | Media | Varianza | Mecanismo |
|---|---|---|---|
| Bernoulli($p$) | $p$ | $p(1-p)$ | un intento binario |
| Binomial($n,p$) | $np$ | $np(1-p)$ | contar éxitos |
| Poisson($\lambda$) | $\lambda$ | $\lambda$ | sucesos raros e independientes |
| Geométrica($p$) | $1/p$ | $(1-p)/p^2$ | intentos hasta el primer éxito |
| Exponencial($\lambda$) | $1/\lambda$ | $1/\lambda^2$ | espera sin memoria |
| Normal($\mu,\sigma$) | $\mu$ | $\sigma^2$ | suma de muchos |
| Log-normal | $e^{\mu+\sigma^2/2}$ | — | producto de muchos |
| Pareto($\alpha$) | $\frac{\alpha}{\alpha-1}$ si $\alpha>1$ | sólo si $\alpha>2$ | crecimiento proporcional |

**TCL:** $\sum X_i$ tiende a normal **si la varianza es finita**. Velocidad
$1/\sqrt n$. *(Capítulo 3.)*

---

## A.4 Conteo y ruido

$$\sigma_N=\sqrt N,\qquad \frac{\sigma_N}{N}=\frac1{\sqrt N}$$

**Índice de dispersión:** $D=\operatorname{Var}/E$. $D>1$ sobredispersión,
$D<1$ subdispersión.

**Significancia:** $s/\sqrt b$, y con sistemático $s/\sqrt{b+(\delta b)^2}$,
con techo $r_s/(\delta r_b)$.

**Tiempo para 5σ:** $t=25\,r_b/r_s^2$. *(Capítulo 4, II.4.)*

---

## A.5 Incertidumbre

**Propagación a primer orden:**
$$\sigma_y^2=\sum_i\left(\frac{\partial f}{\partial x_i}\right)^2\sigma_i^2
+2\sum_{i<j}\frac{\partial f}{\partial x_i}\frac{\partial f}{\partial x_j}\sigma_{ij}$$

**Para productos y cocientes:** los errores **relativos** se suman en cuadratura.

**Sesgo por curvatura:** $E[f(x)]\approx f(\bar x)+\tfrac12 f''\sigma^2$.

**$\chi^2$:** $\sum (y_i-f_i)^2/\sigma_i^2$; con $N$ datos y $k$ parámetros,
$\chi^2_\nu=\chi^2/(N-k)\approx1$ si todo va bien. *(Capítulo 5.)*

---

## A.6 Ecuaciones diferenciales

**Lineal de primer orden:** $\dot x=a-bx$ tiene $x_\infty=a/b$, $\tau=1/b$ y
$$x(t)=x_\infty+(x_0-x_\infty)e^{-t/\tau}$$
Con $t=\tau$ se ha recorrido el 63 %; con $3\tau$, el 95 %; con $5\tau$,
el 99,3 %.

**Estabilidad 1D:** $f'(x^*)<0$ estable. $|f'|=1/\tau$ local.

**Sistemas:** $\lambda$ del jacobiano; parte real = tasa, imaginaria =
frecuencia.

**Logística:** $\dot N=rN(1-N/K)$, inflexión en $K/2$.

**Un sistema autónomo 1D no oscila.** *(Capítulos 6 y 7.)*

---

## A.7 Métodos numéricos

**Orden:** medir con `log2(e(h)/e(h/2))`.

**Euler:** orden 1, estable si $|1+h\lambda|<1$.
**RK4:** orden 4, cuatro evaluaciones.
**Verlet simpléctico:** orden 2, conserva el volumen de fases.

**Regla:** compara métodos a igual **coste**, no a igual paso.

**CFL parabólica:** $D\Delta t/\Delta x^2\le1/2$.
**CFL hiperbólica:** $c\Delta t/\Delta x\le1$.

**Derivada numérica:** óptimo en $h\sim\epsilon_{\text{maq}}^{1/3}$, error
mínimo $\sim10^{-11}$. *(Capítulo 8.)*

---

## A.8 Monte Carlo

$$\hat I=\frac{|\Omega|}{N}\sum f(x_i),\qquad
\epsilon=\frac{\sigma_f}{\sqrt N}$$

**No depende de la dimensión.** Cruce con rejilla en $d\approx4$–5.

**Metropolis:** acepta con $\min(1,p(y)/p(x))$; sólo cocientes, así que $Z$ se
cancela.

**Diagnóstico:** $N_{\text{ef}}=N/\tau_{\text{int}}$ con
$\tau_{\text{int}}=1+2\sum\rho_k$. Barras con $N_{\text{ef}}$, nunca con $N$.
*(Capítulo 9.)*

---

## A.9 Optimización

**Gradiente:** tasa $(\kappa-1)/(\kappa+1)$.
**Newton:** convergencia cuadrática, coste $\mathcal{O}(n^3)$.

**Condiciones:** $\nabla f=0$ y hessiano semidefinido positivo.

**Recocido:** acepta empeorar con probabilidad $e^{-\Delta E/T}$.

**Boltzmann:** $p\propto e^{-E/T}$ se concentra en el mínimo global cuando
$T\to0$, con anchura $\sqrt{T/k}$. *(Capítulo 10.)*

---

## A.10 Álgebra lineal

**SVD:** $A=U\Sigma V^T$. Toda transformación lineal es rotar, estirar, rotar.

**Condicionamiento:** $\kappa=\sigma_{\max}/\sigma_{\min}$.
**Cifras perdidas** $\approx\log_{10}\kappa$.

**No resuelvas por ecuaciones normales:** $\kappa(A^TA)=\kappa(A)^2$.

**Sistema lineal:** $\mathbf{x}(t)=\sum c_ke^{\lambda_kt}\mathbf{v}_k$.

**No normalidad:** los autovalores describen el infinito; para el transitorio,
$\|e^{At}\|$. *(Capítulo 11.)*

---

## A.11 Fourier

$$\hat f(\omega)=\int f(t)e^{-i\omega t}dt,\qquad
\widehat{f*g}=\hat f\hat g$$

**Nyquist:** $f_s>2f_{\max}$, o hay aliasing irreversible.

**Resolución:** $\Delta f=1/T$. Para separar dos tonos a $\Delta f$, mide
$1/\Delta f$.

**Incertidumbre:** $\Delta t\,\Delta\omega\ge1/2$, con igualdad para la
gaussiana.

**Gibbs:** sobrepaso del 8,9 %, permanente.

**Estimación espectral:** Welch, no periodograma. *(Capítulo 12.)*

---

## A.12 Taylor y perturbaciones

$$f(x_0+h)=\sum_{n}\frac{f^{(n)}(x_0)}{n!}h^n,\qquad
|R_n|\le\frac{|f^{(n+1)}|_{\max}}{(n+1)!}|h|^{n+1}$$

**Rangos útiles al 1 %:** $\sin x\approx x$ hasta 14°;
$\sin x\approx x-x^3/6$ hasta 58°; $e^x\approx1+x$ hasta $x=0{,}14$.

**Balance dominante:** supón cuáles dos términos dominan, resuelve,
**comprueba**.

**Perturbación singular:** $\epsilon$ multiplica la derivada más alta, o el
término de mayor grado, o sobran condiciones de contorno. Reescala.

**Serie asintótica:** suma hasta el término más pequeño y para. Error mínimo
$\sim e^{-x}$. *(Capítulo 13.)*

---

## A.13 Constantes y conversiones

| | |
|---|---|
| $\pi\times10^7$ s | segundos en un año (exacto al 0,5 %) |
| $c=3{,}00\times10^8$ m/s | |
| $g=9{,}81$ m/s² | |
| $N_A=6{,}022\times10^{23}$ | |
| $k_B=1{,}381\times10^{-23}$ J/K | $kT=4{,}11\times10^{-21}$ J a 298 K |
| $R=8{,}314$ J/(mol·K) | |
| $\sigma=5{,}67\times10^{-8}$ W/(m²·K⁴) | Stefan–Boltzmann |
| $h=6{,}626\times10^{-34}$ J·s | |
| 1 eV $=1{,}602\times10^{-19}$ J | |
| 1 cal $=4{,}184$ J | 1 kcal $=4{,}184$ kJ |
| 1 kWh $=3{,}6$ MJ | |
| 1 t TNT $=4{,}184$ GJ | 1 kt $=4{,}184$ TJ |
| 1 atm $=1{,}013\times10^5$ Pa | |
| 1 año-luz $=9{,}46\times10^{15}$ m | 1 pc $=3{,}086\times10^{16}$ m |
