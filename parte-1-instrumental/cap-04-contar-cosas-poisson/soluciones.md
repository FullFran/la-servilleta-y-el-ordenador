## Soluciones del capítulo 4

> Las soluciones son razonadas: el número final es lo menos importante. En los
> problemas ● y ★ con solución cerrada hay **Pista 1** y **Pista 2** antes de
> ella; tápalas con la mano y úsalas de una en una.
>
> Los de **Mundo real** (R) no llevan solución a propósito: su procedimiento
> está en el apéndice D.

---

### Calentamiento

**4.C1** $\sigma=\sqrt{2500}=50$; resultado $2500\pm50$, es decir un 2 %. Para
llegar al 0,5 % hace falta $N=(1/0{,}005)^2=40\,000$ cuentas: dieciséis veces
más. Ese factor 16 es la ley económica del capítulo entero.

**4.C2** $\lambda=1$ cuenta por segundo. $P(0)=e^{-1}=0{,}37$.
$P(\ge3)=1-e^{-1}(1+1+0{,}5)=1-0{,}92=0{,}08$.

**4.C3** No: $D=9/4=2{,}25$. Sobredispersión. Sospecha de tasa variable, de
agrupamiento o de mezcla de dos poblaciones. Antes de modelar nada, trocea los
datos y mira si $\lambda$ deriva.

**4.C4** En 10 ms se esperan 2 peticiones, $\sigma=\sqrt2=1{,}41$, ruido
relativo del 71 %. Por eso las métricas de latencia por ventanas cortas son
tan ruidosas y por eso hay que agregar antes de sacar conclusiones.

---

### Estimación

**4.E1** Píxel de 1 μm², $f/2$, escena interior a 100 lux, 1/60 s. El flujo que
llega al sensor es del orden de $10^{3}$–$10^{4}$ fotones por píxel, con
eficiencia cuántica ~0,7. Ruido relativo $\sim1$–3 %. Sí explica el grano
visible en zonas oscuras, donde el número de fotones baja uno o dos órdenes de
magnitud y el ruido relativo sube al 10–30 %.

**4.E2** $^{40}$K: el cuerpo humano contiene ~140 g de potasio, del que el
0,0117 % es $^{40}$K, con vida media $1{,}25\times10^9$ años. Sale
$\sim4{,}4\times10^3$ Bq. $^{14}$C: $\sim3{,}7\times10^3$ Bq. En total, unas
**8000 desintegraciones por segundo** dentro de ti, todo el rato. Es un buen
dato para tener a mano cuando alguien habla de radiación.

**4.E3** Del orden de 50–70 mutaciones puntuales *de novo* por generación. Es
aproximadamente Poisson, pero con sobredispersión conocida: la tasa depende
fuertemente de la edad paterna (las divisiones de la línea germinal masculina
continúan toda la vida). Ahí está la violación de «tasa constante».

**4.E4** ● *Pista 1:* $t\propto r_b/r_s^2$, y aquí $r_b$ es el mismo.
*Pista 2:* el cuadrado es lo importante. Antes de hacer la cuenta, decide si el fondo se mantiene o también cambia al observar más débil.
*Solución:* si $r_s$ baja un factor 10, $t$ sube un factor 100. De una hora se
pasa a 100 horas. Y si además el fondo aumenta porque hay que abrir el campo,
peor. Esta cuenta de treinta segundos decide si una propuesta de tiempo de
observación es realista, y por eso se hace antes que ninguna otra.

---

### Modelado

**4.M1** Supuestos: independencia (buena: los rayos cósmicos primarios no
interaccionan entre sí), tasa constante (regular: hay modulación solar y
barométrica de varios por ciento) y ausencia de tiempo muerto (depende del
detector). **El que más preocupa es la tasa constante**: la presión atmosférica
modula el flujo de muones un ~1 % por cada 10 hPa, y en una serie larga eso
produce sobredispersión y estructura temporal falsa.

**4.M2** Poisson es razonable si las erratas son independientes. Sobredispersión:
un capítulo escrito con prisas tiene más erratas que otro, es decir, tasa
variable por página. Subdispersión: si un corrector revisa y garantiza «no más
de dos por página», el mecanismo regulador suprime la cola.

**4.M3** ● *Pista 1:* la distribución del número de contagios secundarios no es
Poisson, es muy sesgada.
*Pista 2:* dale a cada individuo su propia infecciosidad sacada de una gamma. La mezcla te dará una binomial negativa, y su parámetro de dispersión es lo que decide la estrategia de control.
*Solución:* modelo mínimo — cada individuo tiene una infecciosidad $\nu$
sacada de una gamma, y contagia a Poisson($\nu$). Resulta una binomial negativa
con parámetro de dispersión $k$. Con $k\approx0{,}1$, el 10 % de los infectados
causa el 80 % de los contagios. **Consecuencia para el control:** con
sobredispersión alta, el rastreo hacia atrás (buscar la fuente que infectó al
caso, que probablemente sea un supercontagiador) es mucho más eficiente que el
rastreo hacia delante, y las medidas dirigidas a evitar eventos multitudinarios
rinden más que las restricciones uniformes. Es un resultado con consecuencias
políticas que sale de un índice de dispersión.

---

### Derivación

**4.D1** Con $G(z,t)=\sum_k P_k z^k$, la ecuación maestra da
$\partial_t G = \lambda(z-1)G$, luego $G=e^{\lambda t(z-1)}$, que es la función
generatriz de Poisson($\lambda t$). Desarrollando en potencias de $z$ se leen
las $P_k$.

**4.D2** Con generatrices: $G_1G_2=e^{\lambda_1(z-1)}e^{\lambda_2(z-1)}
=e^{(\lambda_1+\lambda_2)(z-1)}$. Para señal más fondo esto significa que el
total sigue siendo Poisson con $\lambda=s+b$, y que la varianza del total es
$s+b$, no $b$. Por eso la fórmula rigurosa de significancia usa
$s/\sqrt{s+b}$, y $s/\sqrt b$ es la aproximación válida cuando $s\ll b$.

**4.D3** ● *Pista 1:* en tiempo muerto no paralizable, cada suceso **registrado** cuesta un tiempo $\tau$. Cuenta el tiempo vivo en un intervalo $T$.
*Pista 2:* para la subdispersión, piensa en la distribución de huecos entre registros: ya no puede haber huecos menores que $\tau$.
*Solución:* No paralizable: de cada suceso registrado se pierde un tiempo
$\tau$. En un tiempo $T$ hay $m T$ registros y por tanto $mT\tau$ de tiempo
muerto; los sucesos reales en el tiempo vivo son $r(T-mT\tau)=mT$, luego
$m=r/(1+r\tau)$. La subdispersión sale de que los registros ya no pueden estar
arbitrariamente juntos: la distribución de huecos es una exponencial desplazada
en $\tau$, cuya varianza relativa es menor.

**4.D4** ● *Pista 1:* escribe la mezcla como una integral de una Poisson sobre la distribución gamma de $\lambda$.
*Pista 2:* la integral es una gamma disfrazada. Cuando la resuelvas reconocerás la distribución, y su índice de dispersión será mayor que 1 pase lo que pase.
*Solución:* $P(N=n)=\int_0^\infty \frac{\lambda^n e^{-\lambda}}{n!}
\frac{\beta^\alpha\lambda^{\alpha-1}e^{-\beta\lambda}}{\Gamma(\alpha)}d\lambda$.
La integral es una gamma y da
$\binom{n+\alpha-1}{n}(\frac{\beta}{1+\beta})^\alpha(\frac{1}{1+\beta})^n$: una
binomial negativa. Media $\alpha/\beta$, varianza
$\alpha(1+\beta)/\beta^2$, luego $D=1+1/\beta>1$ siempre. **Mezclar Poissons
siempre sobredispersa**, cualquiera que sea la mezcla: es una consecuencia de
la ley de la varianza total.

---

### Computacional

**4.P1** El algoritmo de Knuth: multiplica uniformes hasta bajar de
$e^{-\lambda}$. Es exactamente «cuenta sucesos exponenciales hasta agotar el
intervalo», escrito de forma eficiente.

**4.P2** El ruido de lectura $\sigma_r$ deja de dominar cuando
$\sqrt{N}>\sigma_r$, es decir $N>\sigma_r^2$. Con 5 electrones de lectura, a
partir de 25 fotones el ruido de fotones manda. Por eso los sensores modernos
con lectura sub-electrón sólo aportan en el régimen de muy poca luz.

**4.P3** La probabilidad exacta es $P(N\ge12\mid\lambda=8)=1-\sum_{k=0}^{11}
e^{-8}8^k/k!\approx 0{,}112$, es decir un 11 %. La aproximación normal daba
1,4 sigmas, o sea un 8 %. La aproximación es mala porque con $\lambda=8$ la
distribución todavía es visiblemente asimétrica: la regla práctica es que hacen
falta $\lambda\gtrsim20$ para fiarse de la normal, y por debajo hay que usar
Poisson exacta.

---

### Experimento

**4.X1** Con la tasa medida sola **no se pueden distinguir** los dos modelos en
el régimen de tasas bajas, donde ambos coinciden a primer orden; sí en el de
tasas altas, donde uno satura y el otro decrece. La medida adicional que lo
resuelve limpiamente es la **distribución de intervalos entre sucesos**, que en
el caso no paralizable es una exponencial desplazada y en el paralizable no.

**4.X2** ● *Pista 1:* el máximo de muchas variables independientes no sigue la distribución de una de ellas: sigue una distribución de valores extremos.
*Pista 2:* traduce la significancia global que quieres a la local que necesitas con 1000 canales. El resultado explica de dónde sale el umbral de 5 sigmas.
*Solución:* Con 1000 canales independientes, el máximo local sigue
aproximadamente una distribución de Gumbel. Para una significancia global de
3 sigmas ($p_{\text{global}}=1{,}35\times10^{-3}$) hace falta un
$p_{\text{local}}\approx1{,}35\times10^{-6}$, es decir **4,7 sigmas locales**.
Ese es el «impuesto» del look-elsewhere y es la razón práctica del umbral de
5 sigmas.

---

### Detective

**4.T1** El error está en confundir la precisión relativa del total con la
incertidumbre de la **diferencia**. $\sigma_{n_1}=100$, $\sigma_{n_2}=99$, y la
diferencia tiene $\sigma=\sqrt{100^2+99^2}=141$. El exceso de 200 es
$200/141=1{,}4$ sigmas: no significativo. Es el enemigo 2 del capítulo 1
—diferencias de números grandes— en su versión de conteo.

**4.T2** Contando 100 s a 1523 cuentas/s se registran $1{,}5\times10^5$
cuentas, cuya incertidumbre estadística es $\sqrt{1{,}5\times10^5}=390$
cuentas, es decir 3,9 cuentas/s. La incertidumbre declarada, 0,12 cuentas/s, es
**treinta veces menor que el límite de Poisson**. O han contado mucho más
tiempo del que dicen, o han calculado la incertidumbre de otra cosa (por
ejemplo, la dispersión de la media de varias ventanas mal propagada). En
cualquier caso, la frase no puede ser cierta.

**4.T3** ● *Pista 1:* España tiene más de 8000 municipios.
*Pista 2:* calcula primero cuántos casos se esperan en **un** municipio pequeño y la probabilidad de ver un exceso allí. Después multiplica por 8000 y verás que lo raro sería no encontrar ninguno.
*Solución:* con 3000 habitantes y una incidencia de $10^{-4}$/año, se esperan
0,3 casos al año. Observar 1 caso ya es un exceso de factor 3, y ocurre por
azar con probabilidad $\approx26\,\%$. Con 8000 municipios, es **inevitable**
que decenas presenten excesos aparentemente significativos cada año. Es
look-elsewhere puro, se llama en epidemiología «problema de los conglomerados
de cáncer» y ha generado un número enorme de alarmas infundadas. El artículo
clásico de Gawande (*The Cancer-Cluster Myth*, The New Yorker, 1999) lo cuenta
bien; la corrección estadística correcta requiere ajustar por comparaciones
múltiples y, sobre todo, tener una hipótesis **antes** de mirar los datos.

---

### Feynman

**4.F1** Guion: «Cada suceso que cuentas aporta una pizca de información, pero
también aporta su propia fluctuación. Al contar el doble, la señal se duplica y
la fluctuación crece sólo la raíz de dos, porque unas veces sobra y otras
falta, y se estorban entre sí. Así que ganas, pero ganas despacio: el doble de
tiempo te da un 40 % de mejora, no el doble.»

**4.F2** Guion: «Si haces una lista de todas las amistades del mundo y coges una
al azar, es más probable que en ella aparezca alguien muy popular, simplemente
porque los populares están en muchísimas más parejas. Tus amigos no son gente
normal: son gente elegida por el hecho de tener amigos. No dice nada sobre ti;
dice cómo se ha hecho la muestra.»

---

### Extensión

**4.Z1** ★ *Pista 1:* fíjate en el **procedimiento**, no en el resultado: dos observadores contando centelleos a ojo, en oscuridad, en turnos cortos.
*Pista 2:* haz la lista de errores sistemáticos que hoy exigiríamos descartar: fatiga, sesgo del observador que sabe qué espera, coincidencias perdidas.
*Solución:* El punto más interesante del artículo de 1910 es el procedimiento:
dos observadores contando centelleos a ojo en oscuridad, con turnos cortos por
fatiga visual. Errores sistemáticos plausibles hoy: fatiga (deriva de la
eficiencia con el tiempo), sesgo del observador que conoce el resultado
esperado, y pérdida de centelleos coincidentes. Que el resultado siga siendo
correcto un siglo después dice mucho sobre el diseño del experimento, no sobre
la suerte.

**4.Z2** ★ *Pista 1:* la binomial negativa explica un exceso de varianza, pero no dice nada sobre **cuándo** ocurren los sucesos.
*Pista 2:* mira la autocorrelación temporal de tus datos. Si un suceso aumenta la probabilidad de otro inmediatamente después, necesitas un modelo con memoria.
*Solución:* La binomial negativa captura el **exceso de varianza** pero no la
**estructura temporal**: predice que los sucesos están agrupados en número,
no en el tiempo. Un proceso de Hawkes, en cambio, modela explícitamente que un
suceso aumenta la intensidad durante un rato. Con datos de réplicas sísmicas o
de incidencias en cascada, el Hawkes ajusta muchísimo mejor la autocorrelación
temporal. El criterio para elegir no es el ajuste global, sino **qué residuo
estructurado deja cada uno**, que es la lección del capítulo 5.
