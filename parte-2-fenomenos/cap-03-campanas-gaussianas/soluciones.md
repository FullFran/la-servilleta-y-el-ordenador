## Soluciones de II.3

**II.3.1** $(220-175)/7=6{,}4$ sigmas. $P\approx8\times10^{-11}$, luego
$\sim0{,}8$ personas de $10^{10}$. La realidad: hay del orden de miles de
personas por encima de 2,20 m. **La cola real es mucho más gruesa que la
gaussiana**, y la razón es que existen condiciones médicas (acromegalia,
síndrome de Marfan) que no son parte de la variación normal. Lección general:
las gaussianas describen bien el centro y mal las colas, casi siempre.

**II.3.2** Con $b=1$: **10 veces más** de magnitud 7 que de 8. Energía:
$\log E=1{,}5M+4{,}8$, luego un magnitud 8 libera $10^{1,5}\approx32$ veces
más que uno de 7. Combinando: los terremotos de magnitud 8 liberan en total
**3,2 veces más energía** que todos los de magnitud 7 juntos. **La energía la
dominan los eventos raros**, y ese es el rasgo definitorio de una cola pesada.

**II.3.3** La media acumulada da saltos cada vez que aparece un valor grande, y
esos saltos no se hacen más pequeños con $n$: la media de $n$ Pareto con
$\alpha=1{,}5$ crece como $n^{1/1,5-1}=n^{-1/3}$... la **suma** crece como
$n^{1/\alpha}=n^{0,67}$, más deprisa que $n$ dividido... conviene comprobarlo
numéricamente. Para $1<\alpha<2$ la media sí existe y converge, pero **muy
despacio y a saltos**; para $\alpha<1$ ni siquiera existe.

**II.3.4** Se distinguen en la cola extrema, donde hay menos datos. Con dos o tres
décadas de rango y menos de $10^4$ puntos, **son prácticamente
indistinguibles**. Ese es el resultado incómodo del capítulo.

**II.3.5** El exponente del modelo de Yule es $1+1/(1-p)$ con $p$ la probabilidad
de que un elemento nuevo cree una categoría nueva. Con $p$ pequeño, exponente
cercano a 2, que es el rango observado en la mayoría de los sistemas reales.

**II.3.6** Para normales, $P(\max<x)=\Phi(x)^n$; imponiendo que sea $1/2$ sale
$x\approx\sigma\sqrt{2\ln n}$: crecimiento **logarítmico**, lentísimo. Para
Pareto, $P(X>x)=x^{-\alpha}$ da $\max\sim n^{1/\alpha}$: crecimiento en
potencia. Con $n=10^6$: la normal da 5,3σ; la Pareto con $\alpha=1{,}5$ da un
factor $10^4$ sobre el mínimo. **Es la diferencia entre «hay un récord difícil
de batir» y «no hay récord».**

**II.3.7** Resultado típico con datos reales: exponente entre 2 y 3, punto de
corte que descarta el 90 % de los datos, y $p$ del contraste que no permite
rechazar la log-normal. Reportar las tres cosas es lo honesto.

**II.3.8** Tres problemas: (i) el **binning** del histograma distorsiona la cola,
donde hay pocas cuentas por bin; (ii) los mínimos cuadrados suponen errores
gaussianos homocedásticos, y los errores de un histograma son de Poisson y
crecen relativamente en la cola; (iii) **no ha contrastado con alternativas**:
una log-normal produce rectas igual de convincentes en dos décadas. Además,
$R^2$ no es un criterio para nada (capítulo 5).

**II.3.9** ★ En latencias, tiempos de proceso y costes, la respuesta es casi
siempre que sí: la media está dominada por la cola y el percentil 95 o 99 es
mucho más informativo para tomar decisiones.

**II.3.10** ★ La criticalidad autoorganizada propone que ciertos sistemas
disipativos evolucionan espontáneamente hacia un estado crítico con leyes de
potencias, **sin ajuste de parámetros**. El modelo de la pila de arena es
elegante y, notablemente, **las pilas de arena reales no lo cumplen**: hay que
usar arroz alargado para observarlo. La evidencia empírica es fuerte en algunos
sistemas (terremotos, incendios forestales) y discutida en otros, y el debate
sobre si la SOC es un mecanismo o una descripción sigue abierto.
