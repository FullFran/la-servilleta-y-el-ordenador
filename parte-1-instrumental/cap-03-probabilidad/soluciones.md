## Soluciones del capítulo 3

> Las soluciones son razonadas: el número final es lo menos importante. En los
> problemas ● y ★ con solución cerrada hay **Pista 1** y **Pista 2** antes de
> ella; tápalas con la mano y úsalas de una en una.
>
> Los de **Mundo real** (R) no llevan solución a propósito: su procedimiento
> está en el apéndice D.

---

### Calentamiento

**3.C1** De 1000 personas, 200 enfermas y 800 sanas. Positivos verdaderos:
$200\times0{,}95=190$. Falsos positivos: $800\times0{,}10=80$. Total de
positivos: 270. VPP $=190/270=\mathbf{70\,\%}$. Con prevalencia alta el test
sirve; el problema del capítulo era la prevalencia, no el test.

**3.C2** Bernoulli: $p$, $p(1-p)$. Binomial: $np$, $np(1-p)$. Poisson:
$\lambda$, $\lambda$ —media y varianza iguales, que es la firma del capítulo 4—.
Exponencial: $1/\lambda$, $1/\lambda^2$. Uniforme: $(a+b)/2$, $(b-a)^2/12$.

**3.C3** 13 en ambos casos si son independientes: **restar no reduce la
varianza**. Con $\rho=0{,}5$: $\operatorname{Var}(X+Y)=4+9+2(0{,}5)(2)(3)=19$ y
$\operatorname{Var}(X-Y)=4+9-6=7$. Restar cantidades correlacionadas positivamente
sí reduce la varianza, y en eso se basan las medidas diferenciales.

**3.C4** Moneda justa: 1 bit. Cargada $p=0{,}9$:
$-0{,}9\log_2 0{,}9-0{,}1\log_2 0{,}1=0{,}47$ bits. Dado de 20:
$\log_2 20=4{,}32$ bits.

---

### Estimación

**3.E1** Con 30 personas la probabilidad es del **70 %**, y casi todo el mundo
estima muchísimo menos. El error de intuición viene de contar personas en vez de
**parejas**: hay $\binom{30}{2}=435$ parejas, y cada una coincide con
probabilidad $1/365$. El número esperado de coincidencias es $435/365\approx1{,}2$.
La lección transferible: cuando algo depende de coincidencias, cuenta parejas,
no elementos, y la cuenta crece como $n^2$.

**3.E2** Del orden de decenas de miles de coincidencias al año en un país de
48 millones. Con 48 millones de personas hay $\sim10^{15}$ parejas; aunque la
probabilidad de coincidir en nombre y fecha sea $\sim10^{-8}$, salen millones de
coincidencias existentes. La conclusión operativa —la de Diaconis y Mosteller
(1989)— es que **con poblaciones grandes, lo asombroso es que no ocurran
coincidencias asombrosas**.

**3.E3** ● *Pista 1:* 99,9 % mensual son unos 43 minutos de caída al mes.
*Pista 2:* haz la cuenta dos veces: con los tres servidores independientes y con los tres compartiendo el suministro eléctrico. La diferencia entre ambas es la respuesta real.
*Solución:* si el lanzamiento dura 2 h, la probabilidad de solaparse con una
caída es $\approx 43\,\text{min}/(30\times24\times60)\times$(factor de
solapamiento) $\sim0{,}3\,\%$. Con tres servidores independientes,
$\sim10^{-8}$; con tres en el mismo centro de datos y un corte de suministro
común, la probabilidad conjunta vuelve a ser esencialmente la del corte del
centro, $\sim10^{-3}$. **Cinco órdenes de magnitud de diferencia según una
hipótesis que nadie escribe.**

---

### Modelado

**3.M1** (a) Poisson: sucesos raros e independientes en un soporte continuo.
(b) Exponencial, si las llegadas son un proceso de Poisson; en la práctica los
correos llegan a ráfagas y la exponencial subestima los huecos largos.
(c) Normal: la altura es suma de muchas contribuciones genéticas y ambientales.
(d) Log-normal: los tamaños de fichero se generan multiplicativamente.
(e) Ley de potencias: crecimiento proporcional, los que ya tienen seguidores
ganan más. (f) Binomial.

**3.M2** $\Omega$: sucesiones de instantes de detección. $X$: número de cuentas
en un intervalo. Supuestos: (i) los núcleos se desintegran independientemente
—**físico**, y muy bien fundado—; (ii) la tasa es constante durante el
experimento —físico, válido si $t\ll$ vida media—; (iii) el detector no tiene
tiempo muerto —**de conveniencia**, y falso: todo detector real lo tiene—;
(iv) la eficiencia es constante —de conveniencia—. El capítulo 4 muestra qué
pasa cuando (iii) falla.

**3.M3** ● *Pista 1:* llegadas y salidas, no sólo llegadas.
*Pista 2:* enumera los supuestos del modelo de Erlang y pregúntate cuál se rompe primero un sábado a mediodía. Hay dos candidatos, y se arreglan de formas distintas.
*Solución:* el modelo natural es una cola con $s=200$ servidores y sin espera
(pérdida de Erlang). Supuestos: llegadas de Poisson con tasa constante y
duraciones independientes. El primero que se rompe un sábado es **la tasa
constante**: hay un pico enorme a mediodía. El segundo es la independencia:
la gente llega en grupos. Un modelo con tasa dependiente del tiempo,
$\lambda(t)$, arregla lo primero; lo segundo exige llegadas por lotes.

---

### Derivación

**3.D1** $P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}$ con $p=\lambda/n$:
$$\binom{n}{k}\frac{\lambda^k}{n^k}\Big(1-\frac{\lambda}{n}\Big)^{n-k}
=\underbrace{\frac{n(n-1)\cdots(n-k+1)}{n^k}}_{\to 1}
\frac{\lambda^k}{k!}
\underbrace{\Big(1-\frac{\lambda}{n}\Big)^{n}}_{\to e^{-\lambda}}
\underbrace{\Big(1-\frac{\lambda}{n}\Big)^{-k}}_{\to 1}$$
Se usa que $p$ es pequeño en los tres límites a la vez, y en particular en que
$k\ll n$: la aproximación falla en la cola derecha, donde $k$ se acerca a $n$.

**3.D2** Sea $S(t)=P(T>t)$. La falta de memoria dice
$S(t+s)=S(t)S(s)$. Es la ecuación funcional de Cauchy multiplicativa; con $S$
continua y $S(0)=1$, la única solución es $S(t)=e^{-\lambda t}$. Nótese que la
propiedad se traduce en «tasa de fallo constante»: $-S'/S=\lambda$.

**3.D3** ● *Pista 1:* la demostración del TCL usa un desarrollo de la función característica hasta orden $t^2$. Escríbelo y mira qué hace falta para que exista.
*Pista 2:* la función característica de Cauchy es $e^{-|t|}$. Intenta derivarla dos veces en el origen y verás dónde se rompe todo.
*Solución:* Ver apartado 4.6. El paso que falla en Cauchy es el desarrollo
$\varphi(t)=1-\sigma^2t^2/2+o(t^2)$: la función característica de Cauchy es
$e^{-|t|}$, que **no es derivable dos veces en el origen** porque la varianza no
existe. Al elevar a $n$ y reescalar por $\sqrt n$ no se obtiene una gaussiana:
se obtiene otra Cauchy. Por eso la media de $n$ Cauchy es una Cauchy con la
misma anchura, y por eso promediar no ayuda nada.

**3.D4** ● *Pista 1:* maximiza $-\int p\ln p$ con multiplicadores de Lagrange para las dos restricciones: normalización y media fija.
*Pista 2:* la condición estacionaria te da $\ln p$ lineal en $x$. Después repite la cuenta cambiando «media» por «energía media» y reconocerás el resultado.
*Solución:* Maximizar $-\int p\ln p$ con $\int p=1$ y $\int xp=\mu$. El
lagrangiano da $\ln p = -1-\alpha-\beta x$, luego $p\propto e^{-\beta x}$, la
exponencial. La misma cuenta con la restricción de energía media da Boltzmann,
que es exactamente la conexión que usaremos en el capítulo 10.

---

### Computacional

**3.P1** $T=-\ln(1-U)/\lambda$. Para la falta de memoria: filtra las muestras
con $T>2$, réstales 2 y comprueba que el histograma resultante es idéntico al
original. Si lo es, no hay envejecimiento.

**3.P2** Box–Muller: $Z_1=\sqrt{-2\ln U_1}\cos(2\pi U_2)$,
$Z_2=\sqrt{-2\ln U_1}\sin(2\pi U_2)$. Distinguir una normal de una $t_5$ por
curtosis requiere del orden de $10^4$ muestras, porque la curtosis es un
estadístico de cuarto orden y converge muy despacio. Es una lección sobre lo
caro que resulta caracterizar colas.

**3.P3** La **mediana** acumulada de muestras de Cauchy sí converge, y lo hace
como $1/\sqrt n$. La mediana existe siempre (es un cuantil, no un momento). Es
la razón práctica por la que en sistemas con colas pesadas se reportan
percentiles y no medias.

---

### Experimento

**3.X1** Regla empírica razonable: el número de sumandos necesario crece como
el cuadrado de la asimetría de la distribución de partida. Con una Bernoulli de
$p=0{,}05$ (asimetría $\approx4{,}1$) hacen falta cientos de sumandos; con una
uniforme (asimetría 0), tres o cuatro ya son casi indistinguibles a ojo. La
cota formal la da la desigualdad de Berry–Esseen.

**3.X2** ● *Pista 1:* los dos casos producen exactamente el mismo dato observado: una puerta abierta y vacía. Aun así las respuestas difieren.
*Pista 2:* condiciona correctamente. En el caso (b) tienes que incluir en el condicionamiento el hecho de que la puerta abierta al azar **resultó** estar vacía.
*Solución:* Caso (a): cambiar gana con probabilidad 2/3. Caso (b): condicionado
a que la puerta abierta al azar estuviera vacía, cambiar gana con probabilidad
1/2. **Los datos observados son idénticos** —una puerta abierta y vacía— y la
respuesta es distinta, porque el mecanismo que generó el dato es distinto. Es
la lección del apartado 3.2 en su forma más pura, y explica por qué el problema
genera discusiones interminables: la gente discute de aritmética cuando el
desacuerdo es sobre $\Omega$.

---

### Detective

**3.T1** Falta el denominador: el 80 % de los **kilómetros** también se hacen
cerca de casa. Sin exposición no hay riesgo. Es el error de comparar numeradores
sin normalizar, y es probablemente el error estadístico más frecuente en prensa.

**3.T2** Tres hipótesis: (i) los fallos son independientes; (ii) la
probabilidad de fallo es constante en el tiempo (no hay envejecimiento);
(iii) el sistema sólo falla si fallan los cuatro (no hay modos de fallo comunes
aguas arriba). La que más preocupa es (i)–(iii) juntas bajo la forma de **fallo
de causa común**: un pico de tensión, un lote defectuoso, un error de software
compartido. En la industria nuclear y aeroespacial se modela explícitamente con
factores beta, precisamente porque la hipótesis ingenua es optimista por varios
órdenes de magnitud.

**3.T3** ● *Pista 1:* construye dos subgrupos, graves y leves, y reparte.
*Pista 2:* reparte de forma desigual: muchos leves en un brazo y muchos graves en el otro. Con eso puedes hacer que el tratamiento empeore a los dos subgrupos y aun así parezca bueno en el agregado.
*Solución:* Sea el grupo tratado 90 leves (mejoran 80 % sin tratar, 75 % con) y
10 graves (mejoran 30 % sin, 25 % con). Tratados:
$0{,}75\cdot90+0{,}25\cdot10=70$ de 100, 70 %. No tratados: 10 leves y 90
graves: $0{,}80\cdot10+0{,}30\cdot90=35$ de 100, 35 %. Con números así el
tratamiento **empeora a ambos subgrupos** y aun así el agregado parece
favorable. Es la paradoja de Simpson, y su lección es que la agregación puede
invertir el signo de un efecto. Volveremos en el capítulo 15.

---

### Feynman

**3.F1** Guion: «Imagina mil personas y una sola enferma. El test acierta con
ella. Pero de las 999 sanas se equivoca con un 1 %, que son diez personas. Así
que hay once positivos y sólo uno está enfermo. El test es buenísimo; lo que
pasa es que hay muchísima más gente sana disponible para equivocarse.»

**3.F2** Guion: «Casi todo lo que medimos es la suma de muchas cosas pequeñas
que no tienen nada que ver entre sí. Cuando sumas muchas cosas así, los
detalles de cada una se borran y sólo sobrevive su tamaño típico: por eso sale
siempre la misma forma. Falla cuando una sola de esas cosas puede ser
gigantesca comparada con las demás —el tamaño de una ciudad, la magnitud de un
terremoto—: entonces la suma la domina un único término y no se borra nada.»

---

### Extensión

**3.Z1** ★ *Pista 1:* construye las tres cuerdas al azar de tres maneras distintas y calcula la probabilidad en cada una. Salen tres números.
*Pista 2:* no hay contradicción: «al azar» no especifica una medida. La pregunta interesante es si algún criterio adicional selecciona una, y si ese criterio te convence.
*Solución:* Las tres construcciones de Bertrand (extremos al azar, punto medio
uniforme en el radio, punto medio uniforme en el disco) dan 1/3, 1/2 y 1/4.
No hay contradicción: son tres modelos distintos porque «cuerda al azar» no
especifica una medida. Jaynes propuso en 1973 un criterio de invariancia que
selecciona 1/2; el argumento es elegante y no todo el mundo lo acepta como
resolución general, lo cual es a su vez un buen ejemplo de que las cuestiones
de fundamentos siguen abiertas.

**3.Z2** ★ *Pista 1:* el teorema de Cox deriva las reglas de la probabilidad de requisitos de consistencia. Localiza en la derivación las hipótesis de regularidad.
*Pista 2:* lee después la crítica de Halpern (1999). La cuestión no es quién tiene razón, sino cómo presenta Jaynes un debate abierto.
*Solución:* El teorema de Cox deduce las reglas de la probabilidad a partir de
requisitos de consistencia sobre grados de creencia. Las críticas técnicas
—Halpern (1999) es la más citada— señalan que la derivación original requiere
hipótesis de regularidad adicionales que Jaynes no explicita. La conclusión
razonable no es que Jaynes esté equivocado, sino que **su libro presenta como
cerrado un debate que no lo está**, y leerlo sabiéndolo lo hace mucho más útil.
