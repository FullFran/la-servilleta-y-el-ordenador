## Soluciones de II.5

**II.5.1** $r=(R_0-1)\gamma=(2-1)/5=0{,}2$/día. $t_2=\ln2/0{,}2=3{,}5$ días.

**II.5.2** $1-1/12=91{,}7\%$. Tamaño final sin vacunar: resolviendo
$1-x=e^{-12x}$ sale $x>0{,}99999$: **prácticamente todo el mundo**. Por eso el
sarampión, antes de la vacuna, era una enfermedad universal de la infancia.

**II.5.3** Con `brentq` sobre $f(x)=x+e^{-R_0x}-1$. Los valores coinciden con la
tabla.

**II.5.4** De $\dot I=(\beta S-\gamma)I$, el signo de $\dot I$ en $t=0$ depende de
$\beta S_0-\gamma$. Con $S_0\approx1$: crece si y sólo si $\beta/\gamma>1$.
**No hace falta resolver nada**: es el signo de un autovalor, capítulo 7.

**II.5.5** $dS/dR=-\beta S/\gamma=-R_0S$, luego $S=S_0e^{-R_0(R-R_0^{ini})}$.
En $t\to\infty$, $I\to0$ y $S_\infty+R_\infty=1$, de donde
$1-R_\infty=e^{-R_0R_\infty}$: la ecuación de tamaño final con
$x=R_\infty$.

**II.5.6** Con $R_0=2$, la probabilidad de extinción partiendo de 1 infectado es
$1/R_0=0{,}5$; de 5, $0{,}5^5=3\%$; de 20, $10^{-6}$. **Con $R_0=2$, la mitad
de las introducciones se extinguen solas**, y eso el modelo determinista no
puede decirlo.

**II.5.7** Con binomial negativa de parámetro $k$, la probabilidad de extinción
partiendo de un caso es la raíz de $s=(1+\frac{R_0}{k}(1-s))^{-k}$. Con
$R_0=2$ y $k=0{,}1$: $s\approx0{,}89$. **Casi el 90 % de las introducciones se
extinguen**, frente al 50 % del caso Poisson. La sobredispersión hace las
epidemias más difíciles de arrancar y más explosivas cuando arrancan.

**II.5.8** Porque el intervalo mide la incertidumbre de los parámetros **dentro
de un modelo**, y la incertidumbre dominante es la del modelo. En 20 días todos
los modelos están en fase exponencial y no se distinguen; sus predicciones del
pico difieren en órdenes de magnitud.

**II.5.9** ★ Preguntas que un ajuste SIR **sí** puede contestar: el orden de
magnitud de la tasa de crecimiento inicial, la comparación relativa entre
escenarios de intervención, y el signo del efecto de una medida. Preguntas que
**no** puede: la altura y la fecha exactas del pico, el número absoluto de
casos, y cualquier cosa a más de unas pocas semanas.
