## Soluciones del capítulo 13

> Las soluciones son razonadas: el número final es lo menos importante. En los
> problemas ● y ★ con solución cerrada hay **Pista 1** y **Pista 2** antes de
> ella; tápalas con la mano y úsalas de una en una.
>
> Los de **Mundo real** (R) no llevan solución a propósito: su procedimiento
> está en el apéndice D.

---

### Calentamiento

**13.C1** El error de $e^x-(1+x)$ es $\approx x^2/2$, y el relativo $x^2/2$.
Al 1 %: $x\approx0{,}14$. Al 0,1 %: $x\approx0{,}045$. **Las aproximaciones
lineales son válidas en rangos mucho más estrechos de lo que la intuición
sugiere.**

**13.C2** $\sqrt{1+\epsilon}\approx1+\epsilon/2-\epsilon^2/8$. Con
$\epsilon=0{,}1$: 1,048750 frente a 1,048809, error $6\times10^{-5}$. Con
$\epsilon=0{,}5$: 1,21875 frente a 1,224745, error $6\times10^{-3}$, cien veces
mayor. El error escala como $\epsilon^3$: multiplicar $\epsilon$ por 5
multiplica el error por 125.

**13.C3** (a) regular; (b) **singular** (baja el grado); (c) **singular**
(baja el orden de la EDO); (d) regular.

**13.C4** El término $n!/x^{n+1}$ es mínimo cuando $n\approx x$, es decir
$n\approx8$. Regla general: **el truncamiento óptimo está en $n\approx x$** y el
error mínimo es del orden de $e^{-x}$.

---

### Estimación

**13.E1** Ala de cuerda 4 m, $U=250$ m/s, $\nu_{aire}=1{,}5\times10^{-5}$ m²/s
(menos a altura de crucero). $Re\approx7\times10^{7}$. Capa turbulenta:
$\delta\approx0{,}37\,c/Re^{1/5}\approx4{,}5$ cm. Espesor del ala:
$\sim0{,}5$ m. La capa es el 10 % del espesor: **fina, y absolutamente
determinante**, porque es donde se genera toda la resistencia de fricción y
donde se decide si el flujo se desprende.

**13.E2** El periodo va como
$T/T_0=1+\theta_0^2/16+\dots$, así que el 1 % se alcanza en
$\theta_0=\sqrt{0{,}16}=0{,}4$ rad $=23°$. Frente a los 14° de la aproximación
de $\sin\theta$. **La diferencia viene de que el periodo integra el efecto y
las desviaciones se promedian parcialmente**: la cantidad que te interesa
determina el dominio de validez, no sólo la función que aproximas.

**13.E3** ● *Pista 1:* compara la desaceleración por arrastre con la gravedad local. Sale una parte en $10^7$, así que parece despreciable.
*Pista 2:* pero el arrastre **siempre frena**. El criterio correcto no es $\epsilon\ll1$, es $\epsilon t\ll1$: pon el tiempo de misión y vuelve a mirar.
*Solución:* A 400 km, la densidad atmosférica es $\sim3\times10^{-12}$ kg/m³.
La desaceleración por arrastre es $\sim10^{-6}$ m/s² frente a $g\approx8{,}7$
m/s²: **una parte en $10^7$**. Por órbita, despreciable. Pero es un efecto
**secular** (siempre frena, nunca acelera): la altura decae de forma acumulativa
y la vida orbital sin reboost es de meses. El criterio no es $\epsilon\ll1$
sino $\epsilon\,N_{\text{órbitas}}\ll1$, que da unas $10^{4}$–$10^{5}$ órbitas,
es decir, del orden de un año.

---

### Modelado

**13.M1** Con $S+E\rightleftharpoons C\to P$, el parámetro pequeño es
$\epsilon=e_0/(s_0+K_M)$. La capa límite temporal tiene anchura
$\tau\sim1/(k_1(s_0+K_M))$: en ese tiempo el complejo $C$ alcanza su valor
cuasi-estacionario, y a partir de ahí sigue la dinámica lenta del sustrato.
Es exactamente la figura de escalas temporales del capítulo 6.

**13.M2** La capa límite está en el **tiempo**, en los primeros instantes tras
un cambio brusco, con duración $L/R$. Si desprecias $L$ desde el principio, la
corriente puede cambiar instantáneamente, lo que es físicamente imposible y
produce derivadas infinitas en la simulación. Es el mismo fenómeno que las
condiciones de contorno perdidas.

**13.M3** ● *Pista 1:* identifica los dos tiempos característicos —reproducción y migración— y forma su cociente. Ese es tu $\epsilon$.
*Pista 2:* la reducción consiste en dar por hecho que lo rápido ya ha terminado. Pregúntate entonces qué información se pierde justo después de una perturbación.
*Solución:* Con reproducción rápida ($1/\tau_r$) y migración lenta
($1/\tau_m$), $\epsilon=\tau_r/\tau_m\ll1$. La reducción consiste en suponer
que cada parcela está en su equilibrio local de reproducción, y quedarse con la
dinámica lenta de migración entre parcelas. **Lo que se pierde:** los
transitorios rápidos tras una perturbación —justo lo que ocurre después de una
catástrofe local— y cualquier acoplamiento resonante entre las dos escalas.

---

### Derivación

**13.D1** $x=1-\epsilon+2\epsilon^2$. Con $\epsilon=0{,}1$: $1-0{,}1+0{,}02
=0{,}92$ frente a la raíz exacta $0{,}91608$. Error del 0,4 %, y el siguiente
término ($-5\epsilon^3=-0{,}005$) lo reduce a 0,07 %.

**13.D2** Las raíces del polinomio característico son
$m_{1,2}=\frac{-1\pm\sqrt{1-4\epsilon}}{2\epsilon}$. Desarrollando:
$m_1\approx-1-\epsilon$ (lenta) y $m_2\approx-1/\epsilon+1$ (rápida). La
solución exacta es combinación de las dos exponenciales, y la separación de
escalas $|m_2/m_1|\approx1/\epsilon$ es exactamente la rigidez del capítulo 8.

**13.D3** ● *Pista 1:* haz primero el desarrollo ingenuo y verás aparecer un término $t\sin t$ que crece sin límite. Ese es el síntoma.
*Pista 2:* el problema es suponer que la frecuencia no cambia. Desarróllala también, $\omega=1+\epsilon\omega_1$, y elige $\omega_1$ para matar el término secular.
*Solución:* El desarrollo ingenuo $x=x_0+\epsilon x_1$ da
$x_1\propto t\sin t$: un **término secular** que crece sin límite y hace que la
aproximación falle para $t\sim1/\epsilon$. Poincaré–Lindstedt lo arregla
suponiendo que la **frecuencia también se desarrolla**,
$\omega=1+\epsilon\omega_1$, y eligiendo $\omega_1$ para cancelar el término
resonante. Sale $\omega_1=\tfrac38a^2$.
La lección física: la no linealidad no añade una corrección pequeña a la
amplitud, **cambia la frecuencia**, y una frecuencia ligeramente distinta
integrada mucho tiempo produce una diferencia de fase enorme.

**13.D4** ● *Pista 1:* integra por partes repetidamente y no tires el resto: acótalo.
*Pista 2:* la cota resulta ser el primer término omitido. Minimízala respecto al número de términos con Stirling y verás dónde está el truncamiento óptimo.
*Solución:* Integrando por partes $n$ veces,
$e^xE_1(x)=\sum_{k=0}^{n-1}\frac{(-1)^kk!}{x^{k+1}}+R_n$ con
$|R_n|\le\frac{n!}{x^{n+1}}$: **el resto está acotado por el primer término
omitido**. Minimizando esa cota respecto a $n$ con la fórmula de Stirling sale
$n\approx x$ y $|R|\sim\sqrt{2\pi/x}\,e^{-x}$: el error mínimo alcanzable, y
coincide con la curva de la figura.

---

### Computacional

**13.P1** Al 0,1 %: $\sin x\approx x$ hasta 0,077 rad (4,4°);
$\cos x\approx1-x^2/2$ hasta 0,39 rad (22°); $\tan x\approx x$ hasta 0,055 rad
(3,2°). La tangente es la peor porque su tercera derivada es mayor.

**13.P2** Con $\epsilon=10^{-3}$ y tolerancia $10^{-4}$, la malla uniforme
necesita del orden de $10^4$ nodos (hay que resolver una capa de $10^{-3}$ con
varios puntos dentro). Una malla graduada con densidad $\propto1/(x+\epsilon)$
lo consigue con ~200. **Factor 50, y el análisis asintótico es lo que te dice
cómo graduar.**

**13.P3** El error óptimo sigue $\sqrt{2\pi/x}\,e^{-x}$. Para $x=20$ da
$\sim10^{-9}$; para $x=40$, $\sim10^{-18}$, por debajo de la precisión de
máquina. Para $x$ grande, la serie asintótica **es** el mejor método
disponible; para $x$ pequeño, no sirve y hay que usar otra representación.

---

### Experimento

**13.X1** El primer caso da pendiente 1 limpia. El segundo,
$\epsilon y''+xy'+y=0$, tiene el coeficiente de $y'$ anulándose en $x=0$: la
capa aparece **ahí dentro**, no en el borde, y su anchura escala como
$\sqrt\epsilon$ porque el balance dominante es ahora entre $\epsilon y''$ y
$xy'$ con $x\sim\delta$: $\epsilon/\delta^2\sim\delta/\delta$, luego
$\delta\sim\sqrt\epsilon$. Descubrir el exponente $1/2$ midiendo, sin haberlo
derivado, es el objetivo del ejercicio.

**13.X2** ● *Pista 1:* fija el presupuesto de cálculo —el mismo número de nodos para las dos— y barre $\epsilon$ en varias décadas.
*Pista 2:* busca el cruce. La lección no es cuál gana, sino que hay un régimen intermedio donde las dos sufren.
*Solución:* Con presupuesto fijo de unos 100 nodos, la asintótica compuesta gana
por debajo de $\epsilon\approx10^{-3}$, y por encima gana la numérica. El
mensaje: **no compiten, se complementan**, y el régimen intermedio es donde
ambas sufren. Ahí es donde hay que gastar la potencia de cálculo.

---

### Detective

**13.T1** Es la **paradoja de d'Alembert**, y el error es despreciar la
viscosidad *uniformemente*. La viscosidad es despreciable en casi todo el
dominio y absolutamente dominante en la capa límite junto a la pared, que es
donde se genera la resistencia. Es una perturbación singular tratada como
regular.

**13.T2** El término $\epsilon t\sin t$ es **secular**: crece sin límite. La
aproximación sólo vale para $t\ll1/\epsilon$, y el autor la está usando cien
veces más allá. Lo que ocurre físicamente es un cambio de frecuencia (problema
13.D3), y la solución correcta es Poincaré–Lindstedt o escalas múltiples.

**13.T3** ● *Pista 1:* «he sumado 40 términos» debería alarmarte, no tranquilizarte, si la serie es asintótica.
*Pista 2:* dibuja la suma parcial frente al número de términos. Si baja, se estabiliza y después se dispara, ya tienes el diagnóstico y el número correcto de términos.
*Solución:* Explicación alternativa: **ha sumado demasiados términos de una
serie asintótica divergente**. El truncamiento óptimo está en $n\approx1/g$ con
$g$ el acoplamiento; sumar 40 términos con $g$ moderado garantiza que el
resultado sea basura. Comprobación: dibujar el valor de la suma parcial frente
al número de términos. Si baja, se estabiliza y luego diverge, la teoría está
bien y el uso está mal. Es literalmente la figura de la sección 4.4.

---

### Feynman

**13.F1** Guion: «Cuando el aire pasa junto a un ala, muy lejos de la superficie
la viscosidad no importa nada: el aire se desliza como si fuera un fluido
ideal. Pero justo pegado al ala, el aire tiene que estar quieto, porque se
adhiere. Así que en una franja finísima —milímetros— la velocidad pasa de cero
a la del vuelo. En esa franja los cambios son tan bruscos que la viscosidad, que
en todo lo demás era despreciable, se convierte en la protagonista. Y como toda
la fricción ocurre ahí, esa franja decide la resistencia del avión entero.»

**13.F2** Guion: «Los primeros términos de la serie son cada vez más pequeños y
te acercan mucho a la respuesta. A partir de cierto punto empiezan a crecer y
te alejan. Así que la serie funciona si sabes cuándo parar: sumas mientras los
términos bajen y te detienes en el más pequeño. Lo que te da no es la respuesta
exacta, pero es lo mejor que esa serie puede darte, y muchas veces es más
preciso que cualquier método alternativo.»

---

### Extensión

**13.Z1** ★ *Pista 1:* busca en el artículo original el balance de términos en las ecuaciones adimensionalizadas; de ahí sale el espesor $\delta\sim L/\sqrt{Re}$.
*Pista 2:* fíjate en qué aporta Prandtl como **evidencia**, no como argumento. Es menos de lo que la fama del resultado hace suponer.
*Solución:* Prandtl justifica la hipótesis por un argumento de balance
dominante en las ecuaciones adimensionalizadas: en una región de espesor
$\delta\sim L/\sqrt{Re}$, el término viscoso $\nu\partial_y^2u$ es del mismo
orden que el inercial $u\partial_xu$. Como evidencia aporta observaciones de
flujo con partículas en un canal de agua que él mismo construyó, y en
particular la observación del **desprendimiento** de la capa. El artículo es un
modelo de cómo se presenta una idea nueva: hipótesis, justificación por
escalas, consecuencias comprobables y evidencia experimental, en ocho páginas.

**13.Z2** ★ *Pista 1:* el truco de Borel es dividir cada coeficiente por $n!$ para que la serie converja, y deshacerlo después con una integral.
*Pista 2:* pregúntate qué hace falta para que ese camino funcione: que la transformada se pueda continuar y que no haya singularidades en el eje positivo.
*Solución:* La resumación de Borel transforma $\sum a_n g^n$ en
$\int_0^\infty e^{-t}B(gt)\,dt$ con $B(z)=\sum a_nz^n/n!$, cuya serie sí
converge. Si $B$ se puede continuar analíticamente y no hay singularidades en
el eje positivo, la integral recupera la función exacta y **rompe la barrera
$e^{-x}$**. El coste: hay que conocer muchos términos de la serie y hacer una
continuación analítica no trivial, y en muchos casos físicos importantes
—incluida la QCD— hay singularidades en el eje (renormalones) que lo impiden.
La existencia misma de esas singularidades es información física.
