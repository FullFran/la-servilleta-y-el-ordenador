## Soluciones de II.4

**II.4.1** Gaussiana: $15/5=3{,}0\sigma$. Poisson exacta:
$P(N\ge40\mid25)=0{,}0060$, que corresponde a $2{,}51\sigma$. **Media sigma de
diferencia**, y en la cola es un factor 4 en el p-valor. Con $\lambda=25$
estamos justo en el límite donde la aproximación empieza a ser aceptable.

**II.4.2** $t_{5\sigma}=25 r_b/r_s^2=25\times50/0{,}25=5000$ h $\approx$ **7
meses** de medida continua.

**II.4.3** Techo $=r_s/(\delta r_b)=0{,}5/(0{,}03\times50)=0{,}33$ sigmas.
**No se alcanzan las 5 sigmas jamás**, ni con siglos de medida. Con un fondo
conocido al 3 % y una señal cien veces menor que él, el experimento es
inviable tal como está planteado. Esa conclusión, obtenida en treinta segundos,
vale más que siete meses de datos.

**II.4.4** $P(20\mid20)/P(20\mid12)=0{,}0888/0{,}0176=5{,}0$. Con previa 1:50, la
posterior queda en 5:50 = 1:10, es decir un 9 %. Sigue siendo mayoritariamente
improbable, y sin embargo el exceso son $8/\sqrt{12}=2{,}3$ sigmas, que mucha
gente presentaría como «evidencia».

**II.4.5** El máximo de 200 canales sigue aproximadamente una Gumbel. Para una
significancia global de 3 sigmas hace falta una local de unas 4,3.

**II.4.6** $s/\sqrt{b+(\delta b)^2}$ con $s=r_st$, $b=r_bt$:
$$\frac{r_st}{\sqrt{r_bt+\delta^2r_b^2t^2}}
\xrightarrow[t\to\infty]{}\frac{r_st}{\delta r_b t}=\frac{r_s}{\delta r_b}$$
No depende de $t$ porque **el sistemático escala igual que la señal**: los dos
son proporcionales al tiempo, así que su cociente es constante. La estadística,
que va como $\sqrt t$, acaba siendo irrelevante.

**II.4.7** ● Si se dedica una fracción $f$ al control, la incertidumbre del fondo
baja como $1/\sqrt{f\,t}$ pero la señal recogida baja como $(1-f)$. Optimizando,
la fracción óptima resulta ser $f^*=1/(1+\sqrt{r_{\text{on}}/r_{\text{off}}})$
en el caso simétrico, que para tasas parecidas da $f^*\approx0{,}5$. **La mitad
del tiempo midiendo el fondo** sorprende a mucha gente y es el resultado
estándar en astronomía de rayos gamma y en espectrometría.

**II.4.8** Con 6 pruebas, $p_{\text{global}}\approx6\,p_{\text{local}}$. Un
$4{,}2\sigma$ local es $p=1{,}3\times10^{-5}$; multiplicado por 6 da
$8\times10^{-5}$, que corresponde a **3,8 sigmas**. Y eso suponiendo que sólo
probaron 6 cosas y que las contaron todas, cosa que casi nunca ocurre: la
cuenta honesta incluye todas las decisiones de análisis que se tomaron mirando
los datos.

**II.4.9** ★ La tasa de supervivencia de los resultados de 3 sigmas es
notoriamente baja, y eso es esperable: con $p=0{,}0013$ y muchas búsquedas, la
mayoría de los 3 sigmas anunciados son fluctuaciones. Lo que distingue a un
campo maduro es que lo diga en el propio anuncio.

**II.4.10** ★ El método CLs resuelve un problema concreto: cuando la sensibilidad
del experimento es pobre, un test frecuentista puro puede **excluir** una
hipótesis que el experimento no tenía capacidad de detectar, simplemente por
una fluctuación a la baja del fondo. CLs penaliza esa situación dividiendo por
la probabilidad bajo la hipótesis nula, lo que produce límites conservadores.
No es un procedimiento frecuentista estándar y se justifica por su
comportamiento práctico, lo cual genera debate periódico entre estadísticos.
