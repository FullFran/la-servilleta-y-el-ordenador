# Capítulo 9 — Monte Carlo: calcular mediante azar

> **Qué sabrás hacer al terminar**
> · Convertir un problema determinista en una esperanza y estimarla ·
> Saber cuándo Monte Carlo gana a una rejilla y por qué ·
> Muestrear de distribuciones que no vienen en la biblioteca ·
> Reducir varianza sin introducir sesgo ·
> Construir una cadena de Metropolis y **diagnosticarla**, que es lo difícil.
>
> **Herramientas que usa:** capítulos 1, 3, 4 y 5.
> **Disciplinas de los ejemplos:** geometría, física estadística, finanzas,
> fiabilidad, inferencia bayesiana, transporte de radiación.
> **Deuda que paga:** la propagación de incertidumbre por simulación del
> capítulo 5.
> **Deuda que abre:** el recocido simulado (capítulo 10) y el modelo de Ising
> (capítulo II.9).

---

## 1. Una pregunta

::: pregunta
Quieres calcular el volumen de la intersección de una bola y un cubo en
**diez dimensiones**.

Es un problema puramente determinista: no hay azar por ninguna parte. La
respuesta es un número fijo.

**¿Por qué la mejor manera de calcularlo es tirar dados?**
:::

La respuesta corta es que una rejilla de sólo diez puntos por eje en diez
dimensiones son $10^{10}$ evaluaciones, y con veinte puntos por eje son
$10^{26}$: más que átomos hay en tu cuerpo. La respuesta larga ocupa este
capítulo, y contiene una de las ideas más productivas del siglo XX.

---

## 2. Antes de calcular

::: antes
1. Para estimar $\pi$ con dos decimales correctos por Monte Carlo, ¿cuántas
   muestras necesitas? Da un orden de magnitud.
2. Si cuadruplicas el número de muestras, ¿cuánto mejora tu resultado?
3. ¿En qué dimensión empieza Monte Carlo a ser mejor que una rejilla?

La tercera respuesta sorprende: es más pequeña de lo que casi todo el mundo
dice.
:::

---

## 3. La intuición

### 3.1 Toda integral es una esperanza

El truco entero cabe en una línea:

$$I=\int_\Omega f(x)\,dx = |\Omega|\int_\Omega f(x)\frac{dx}{|\Omega|}
= |\Omega|\;E[f(X)],\qquad X\sim\text{uniforme}(\Omega)$$

Una integral es un promedio multiplicado por un volumen. Y un promedio se
estima muestreando:

$$\hat I=\frac{|\Omega|}{N}\sum_{i=1}^N f(x_i)$$

Eso es todo el método de Monte Carlo. Lo demás son refinamientos.

Lo notable es la inversión conceptual: **usamos el azar para calcular algo que
no tiene nada de azaroso**. El azar no está en el problema, está en el
algoritmo. Es la misma idea que usar un sorteo para hacer una encuesta: no
porque la población sea aleatoria, sino porque preguntar a todos es imposible.

### 3.2 La aguja de Buffon: la primera integral por azar

En 1733, Georges-Louis Leclerc, conde de Buffon, presentó a la Académie un
problema: si dejas caer una aguja de longitud $L$ sobre un suelo con líneas
paralelas separadas $D\ge L$, ¿cuál es la probabilidad de que la aguja cruce
una línea?

$$P=\frac{2L}{\pi D}$$

Y de ahí, despejando, un método para estimar $\pi$ tirando agujas.

![La aguja de Buffon. Izquierda: 220 lanzamientos, en rojo los que cruzan. Derecha: la estimación acumulada de $\pi$ con su banda teórica $\pm\sigma$, y el resultado publicado por Lazzarini en 1901. Lo que hay que concluir: la convergencia es desesperadamente lenta, y el punto rojo es estadísticamente imposible.](figuras/fig_buffon.pdf)

Merece la pena mirar ese punto rojo. En 1901, Mario Lazzarini publicó que con
**3408 lanzamientos** había obtenido $\pi=355/113$, exacto hasta la sexta
cifra decimal.

Con 3408 agujas, la desviación típica del estimador es $\sigma\approx0{,}041$.
Obtener un error de $2{,}7\times10^{-7}$ es estar a $6\times10^{-6}$ sigmas del
valor correcto: la probabilidad es del orden de $10^{-6}$. Y hay más pistas.
El número 3408 es sospechosamente específico, y $355/113$ es precisamente la
famosa aproximación de Zu Chongzhi, conocida desde el siglo V. Badger (1994)
analizó el asunto y la conclusión es difícil de eludir: **Lazzarini fue
parando y reanudando hasta que le salió el número que ya conocía**.

Es un caso perfecto de detención selectiva, y anticipa entero el capítulo 15:
un resultado demasiado bueno es tan sospechoso como uno demasiado malo.

---

## 4. La matemática

### 4.1 El estimador y su error

$\hat I$ es insesgado: $E[\hat I]=I$. Su varianza es

$$\operatorname{Var}(\hat I)=\frac{|\Omega|^2\operatorname{Var}(f)}{N}
\qquad\Longrightarrow\qquad
\boxed{\ \epsilon\propto\frac{1}{\sqrt N}\ }$$

Este resultado tiene una buena noticia y dos malas, y conviene entender bien
las tres.

**La mala noticia obvia:** $1/\sqrt N$ es lentísimo. Para una cifra decimal más
hacen falta 100 veces más muestras. Para seis cifras, $10^{12}$ evaluaciones.
Monte Carlo **nunca** es el método de elección cuando existe otro.

**La mala noticia sutil:** la constante importa tanto como el exponente.
$\epsilon = \sigma_f/\sqrt N$, y $\sigma_f$ depende de la función. Casi todo el
oficio del Monte Carlo avanzado consiste en **reducir $\sigma_f$** sin cambiar
la respuesta, y eso es la sección 4.4.

**La buena noticia, que lo cambia todo:** en esa fórmula **no aparece la
dimensión**. Ninguna rejilla puede decir lo mismo.

### 4.2 La maldición y la bendición de la dimensionalidad

Una rejilla con $n$ puntos por eje en dimensión $d$ tiene $N=n^d$ puntos y
error $\mathcal{O}(n^{-k})=\mathcal{O}(N^{-k/d})$ para un método de orden $k$.
El exponente **se divide por la dimensión**.

Monte Carlo tiene error $\mathcal{O}(N^{-1/2})$, y ese $1/2$ no cambia nunca.

![Monte Carlo frente a alternativas. Izquierda: en $d=4$, el muestreo cuasi-aleatorio de Sobol supera claramente al Monte Carlo puro. Derecha: con el mismo presupuesto de $10^4$ puntos, la rejilla es mejor en dimensión baja y catastrófica a partir de $d\approx5$, mientras que el error de Monte Carlo no depende de $d$. Lo que hay que concluir: el cruce está mucho antes de lo que la gente supone.](figuras/fig_convergencia_mc.pdf)

El cruce está en torno a $d\approx4$–$5$ para una función suave, **no en
dimensión 20**. Y en cuanto la función tiene singularidades o el dominio es
complicado, el cruce se adelanta todavía más.

Esta es la razón por la que Monte Carlo domina en física estadística
(dimensión = número de partículas), en finanzas (dimensión = número de factores
de riesgo), en inferencia bayesiana (dimensión = número de parámetros) y en
transporte de radiación (dimensión = espacio de fases completo). En todos esos
sitios, $d$ es 20, o 1000, o $10^{23}$.

::: aviso
**Cuasi-Monte Carlo: $1/\sqrt N$ no es una ley de la naturaleza.**

Las secuencias de baja discrepancia (Sobol, Halton) llenan el espacio de forma
deliberadamente uniforme en lugar de aleatoria, y consiguen error
$\mathcal{O}((\log N)^d/N)$: **casi $1/N$**. En el panel izquierdo, con $10^5$
puntos, Sobol es un orden de magnitud mejor.

La letra pequeña: funciona bien para funciones suaves y dimensiones moderadas
(hasta unas decenas), y no da una estimación natural del error —hay que
aleatorizar la secuencia (*scrambling*) y repetir para obtener barras—. Pero es
gratis: `scipy.stats.qmc.Sobol`. Si estás integrando en dimensión moderada con
Monte Carlo puro, probablemente estás tirando muestras.
:::

### 4.3 Cómo se generan las muestras

Todo parte de un generador de uniformes, y de ahí se construye lo demás.

![Tres técnicas de muestreo. Izquierda: transformada inversa. Centro: rechazo, con los puntos aceptados en verde. Derecha: muestreo por importancia para un suceso raro. Lo que hay que concluir: para $P(X>4)$, el muestreo directo necesita $10^5$ muestras para ver algo y el de importancia acierta con $10^2$.](figuras/fig_muestreo.pdf)

**Transformada inversa.** Si $U\sim\text{unif}(0,1)$, entonces $X=F^{-1}(U)$
tiene distribución $F$. Elegante y exacto cuando $F^{-1}$ se puede escribir
(exponencial, Weibull, Cauchy, Pareto). Inútil cuando no.

**Rechazo.** Encuentra una $q$ fácil de muestrear y un $M$ con $p(x)\le Mq(x)$.
Muestrea de $q$, acepta con probabilidad $p(x)/(Mq(x))$. Funciona siempre y
**no necesita normalizar $p$**. Su problema: la eficiencia es $1/M$, y en
dimensión alta $M$ crece exponencialmente. En 20 dimensiones puedes estar
rechazando el 99,999 % de las propuestas.

**Importancia.** No cambies el estimador: cambia dónde miras y corrige con un
peso.

$$E_p[f]=\int f(x)p(x)\,dx=\int \underbrace{f(x)\frac{p(x)}{q(x)}}_{\text{con peso}}q(x)\,dx=E_q\!\left[f\frac{p}{q}\right]$$

Muestreando de $q$ en vez de $p$ y pesando por $p/q$, el estimador sigue siendo
insesgado. Si eliges $q$ concentrada donde $|f|p$ es grande, la varianza se
desploma. En el panel derecho, estimar $P(X>4)$ con muestreo directo es
imposible con $10^3$ muestras —no aparece ni un suceso— y con importancia se
consigue un 1 % de error.

**Cuidado con la elección de $q$:** si $q$ tiene colas más ligeras que $p$, los
pesos $p/q$ pueden tener varianza infinita y el estimador falla
catastróficamente **sin dar ninguna señal de alarma**. Regla: la propuesta debe
tener colas al menos tan pesadas como el objetivo.

### 4.4 Reducir varianza sin hacer trampa

Cuatro técnicas que se aplican en este orden de rentabilidad:

1. **Variables antitéticas.** Usa $u$ y $1-u$. Si $f$ es monótona, los errores
   se cancelan parcialmente. Coste: cero líneas de código.
2. **Variables de control.** Si conoces $E[g]$ para una $g$ correlacionada con
   $f$, usa $\hat I = \overline{f} - c(\overline{g}-E[g])$ con
   $c=\operatorname{Cov}(f,g)/\operatorname{Var}(g)$. Reduce la varianza en un
   factor $1-\rho^2$.
3. **Estratificación.** Divide el dominio y muestrea cada trozo por separado.
   Siempre reduce (o iguala) la varianza.
4. **Importancia.** La más potente y la más peligrosa.

**Ninguna de las cuatro introduce sesgo**, y ese es el punto: no se está
aproximando más, se está estimando mejor. Un factor 100 de reducción de
varianza equivale a un factor 100 en tiempo de cálculo, que es la diferencia
entre una noche y tres meses.

### 4.5 Cuando no se puede muestrear directamente: cadenas de Markov

Aquí llega el salto conceptual del capítulo. En física estadística queremos
muestrear de la distribución de Boltzmann

$$p(\mathbf{s})=\frac{e^{-E(\mathbf{s})/kT}}{Z},\qquad
Z=\sum_{\mathbf{s}}e^{-E(\mathbf{s})/kT}$$

y $Z$ es una suma sobre $2^{N}$ configuraciones. Para $N=100$ espines son
$10^{30}$ términos. **No se puede normalizar, luego no se puede muestrear por
los métodos anteriores.**

La solución de 1953: no intentes generar muestras independientes. Construye una
**cadena de Markov** cuya distribución estacionaria sea $p$, y déjala correr.

La condición que basta es el **balance detallado**:

$$p(x)\,T(x\to y)=p(y)\,T(y\to x)$$

Si se cumple, $p$ es estacionaria. Y la elección de Metropolis satisface el
balance detallado sin conocer $Z$:

$$T(x\to y)=q(y\mid x)\cdot\min\!\left(1,\frac{p(y)}{p(x)}\right)$$

**Sólo aparece el cociente $p(y)/p(x)$, y en ese cociente $Z$ se cancela.** Ese
es el truco entero, y es el que abrió medio siglo de física computacional y
toda la estadística bayesiana moderna.

::: herramientas
**Metropolis en nueve líneas**

```python
def metropolis(log_p, x0, paso, n, rng):
    x, lp = x0, log_p(x0)
    cadena = np.empty(n)
    for i in range(n):
        y = x + rng.normal(0, paso)          # propuesta simétrica
        lp_y = log_p(y)
        if np.log(rng.random()) < lp_y - lp:  # min(1, p(y)/p(x))
            x, lp = y, lp_y
        cadena[i] = x
    return cadena
```

Trabajar con `log_p` y no con `p` no es un detalle de estilo: es obligatorio.
Con energías grandes, $e^{-E/kT}$ desborda o se anula, y el cociente en el
espacio logarítmico es la única forma numéricamente estable de hacerlo.
**Metropolis–Hastings** generaliza esto a propuestas no simétricas añadiendo un
factor $q(x\mid y)/q(y\mid x)$ al cociente.
:::

### 4.6 El diagnóstico es la parte difícil

Escribir Metropolis lleva diez minutos. Saber si su resultado sirve para algo
es donde está el trabajo.

![Metropolis sobre una distribución bimodal con tres tamaños de paso. Izquierda: la traza. Centro: el histograma frente a la verdad. Derecha: la autocorrelación. Lo que hay que concluir: la cadena con la tasa de aceptación «de manual» es la peor de las tres.](figuras/fig_metropolis.pdf)

Los números son elocuentes:

| Paso | Aceptación | $\tau_{\text{int}}$ | Muestras efectivas de 55 000 |
|---|---|---|---|
| 0,2 | 89 % | 384 | **143** |
| 1,5 | 43 % | 291 | **189** |
| 8,0 | 17 % | 17 | **3143** |

La regla que se enseña en todas partes —«ajusta el paso para una aceptación
del 25–40 %»— da aquí **el peor resultado posible**. Con paso 1,5 la cadena
acepta cómodamente, la traza parece sana y el histograma parece razonable... y
sólo ha visto un modo. Con paso 8,0 se rechazan cinco de cada seis propuestas,
pero las que se aceptan cruzan el valle.

De aquí salen las reglas de diagnóstico que hay que aplicar siempre:

* **La tasa de aceptación no es un diagnóstico de convergencia.** Es un
  indicador de eficiencia local, y sólo eso.
* **Lo que importa es el tamaño efectivo de muestra**,
  $N_{\text{ef}}=N/\tau_{\text{int}}$ con
  $\tau_{\text{int}}=1+2\sum_k\rho_k$. Cincuenta y cinco mil muestras con
  $\tau_{\text{int}}=291$ equivalen a **189 muestras independientes**, y la
  barra de error hay que calcularla con 189, no con 55 000.
* **Arranca varias cadenas desde puntos muy distintos** y compara. Es el
  estadístico $\hat R$ de Gelman–Rubin, y es la única forma barata de detectar
  que una cadena se ha quedado atrapada.
* **Descarta el burn-in**, pero no te fíes de que la traza «parezca
  estacionaria»: en el panel superior lo parece y es falso.

---

## 5. El ordenador entra en escena

::: antes
Vamos a estimar $\pi$ por el método del círculo. Antes de ejecutar:

* ¿Cuántas muestras para dos decimales correctos?
* Si dibujas el error frente a $N$ en log-log, ¿qué pendiente esperas?
* ¿Cambiaría algo si el círculo fuera una esfera en 10 dimensiones?
:::

```python
import numpy as np
rng = np.random.default_rng(42)

N = 10_000_000
x, y = rng.random((2, N))
dentro = (x**2 + y**2) <= 1.0
pi_est = 4 * dentro.mean()
error_teorico = 4 * np.sqrt(np.pi/4 * (1 - np.pi/4) / N)
print(f"pi ≈ {pi_est:.5f} ± {error_teorico:.5f}")
```

Para dos decimales correctos, es decir $\epsilon\approx0{,}005$, hace falta
$N\approx(1{,}64/0{,}005)^2\approx10^5$. Para seis decimales,
$N\approx10^{13}$. **Es un método pésimo para calcular $\pi$**, y ese es
precisamente el mensaje: Monte Carlo no compite en dimensión baja.

::: juega
1. Repite en dimensión 10: estima el volumen de la esfera unidad. ¿Qué
   fracción de puntos cae dentro? (Prepárate para una sorpresa: casi ninguno.)
2. Aplica variables antitéticas al cálculo de $\pi$. ¿Cuánta varianza ahorras?
3. Usa Sobol en lugar de uniformes. Mide la pendiente del error.
4. En Metropolis, arranca dos cadenas en $x=-3$ y $x=+3$ con paso 1,5 y
   compara sus medias. ¿Cuánto tarda en notarse que no han convergido?
:::

---

## 6. ¿Qué estamos suponiendo?

::: supuestos
1. **Que el generador de números pseudoaleatorios es bueno.** Los modernos
   (PCG64 en NumPy, Mersenne Twister) lo son. Los antiguos no lo eran, y
   RANDU produjo una generación de resultados incorrectos.
2. **Que la varianza del integrando es finita.** Si no lo es, el TCL no aplica,
   las barras de error mienten y la convergencia no es $1/\sqrt N$.
3. **Que las muestras son independientes.** Falso en MCMC, y por eso hace falta
   $\tau_{\text{int}}$.
4. **Que la cadena ha convergido.** Es indecidible en general: se puede
   demostrar que no ha convergido, nunca que sí.
5. **Que la cadena es irreducible.** Si el espacio tiene regiones separadas por
   barreras altas, puede tardar más que la edad del universo en cruzar.
6. **Que la propuesta de importancia tiene colas suficientes.** Si no, la
   varianza es infinita y el estimador falla en silencio.
:::

---

## 7. ¿Cuándo falla?

::: falla
**Falla con generadores malos.** RANDU, distribuido por IBM en los años
sesenta, generaba tripletas $(x_n,x_{n+1},x_{n+2})$ que caen **todas en 15
planos** del cubo unidad. Cualquier simulación tridimensional con RANDU daba
resultados sistemáticamente sesgados, y se publicaron muchas. Prueba visual:
dibuja las tripletas en 3D y gíralas.

**Falla con varianza infinita.** Estimar $E[1/X]$ con $X$ normal, o una
integral con singularidad no integrable, produce una media muestral que se mueve
a saltos —igual que la Cauchy del capítulo 3— y barras de error que se
estrechan mintiendo. Diagnóstico: dibuja la media acumulada. Si da saltos, no
promedies.

**Falla el MCMC multimodal.** Es el fallo más común y el más difícil de
detectar, porque produce resultados que **parecen** correctos. Remedios:
templado paralelo, muestreo por cúmulos, o simplemente varias cadenas desde
puntos muy separados.

**Falla el rechazo en dimensión alta.** La eficiencia cae exponencialmente. En
$d=30$, envolver una gaussiana con otra un 10 % más ancha da una tasa de
aceptación del orden de $10^{-3}$.

**Y falla la intuición geométrica en dimensión alta.** En $d=10$, la esfera
unidad ocupa el 0,25 % del cubo que la contiene; en $d=20$, $2\times10^{-8}$.
Casi todo el volumen de un cubo de dimensión alta está en sus esquinas, y casi
toda la masa de una gaussiana multivariante está en una cáscara fina lejos del
centro. **Muestrear «al azar» en dimensión alta casi nunca cae donde crees.**
:::

### Un anti-ejemplo: la barra de error que mentía

Un grupo estima una integral con MCMC, obtiene $10^6$ muestras y publica el
resultado con la barra $\sigma/\sqrt{10^6}$. Tres años después, otro grupo
repite el cálculo con un algoritmo distinto y obtiene un valor a 8 sigmas.

El error: las $10^6$ muestras de MCMC **no son independientes**. Con
$\tau_{\text{int}}=500$, el tamaño efectivo era 2000 y la barra correcta era
$\sqrt{500}\approx22$ veces mayor. Los dos resultados eran perfectamente
compatibles a 0,36 sigmas.

Este error es endémico. La regla es sencilla y hay que aplicarla siempre:
**en MCMC, toda barra de error se calcula con $N_{\text{ef}}$, nunca con $N$.**

---

## 8. Historia

::: historia
**Ulam, el solitario y una convalecencia** · *Nivel de verificación: A.*

En 1946, Stanisław Ulam se recuperaba de una encefalitis que le había obligado
a una craneotomía de urgencia. Convaleciente y sin poder trabajar en serio,
jugaba al solitario Canfield. Se preguntó cuál era la probabilidad de que
saliera.

Lo cuenta él mismo en *Adventures of a Mathematician* (1976): tras intentar el
cálculo combinatorio y ver que era intratable, se le ocurrió que sería mucho
más práctico jugar cien manos y contar. Y de ahí, inmediatamente, la conexión
con los problemas de difusión de neutrones en los que trabajaba: también allí
la integración directa era imposible y también allí se podía muestrear
trayectorias.

Ulam se lo contó a von Neumann. En marzo de 1947, von Neumann escribió a Robert
Richtmyer una carta de once páginas con un plan de cálculo completo para el
ENIAC, incluyendo el diagrama de flujo. La carta se conserva y está
reproducida en Los Alamos Science (Eckhardt, 1987).

**De dónde viene el nombre** · *Nivel de verificación: A (memoria de
Metropolis).*

Nicholas Metropolis cuenta en su artículo de 1987 que propuso llamarlo «Monte
Carlo» por un tío de Ulam que pedía dinero prestado a la familia porque «tenía
que ir a Monte Carlo». El proyecto necesitaba un nombre en clave, y ese quedó.

**El paper de 1953, y quién hizo qué** · *Nivel de verificación: A.*

*Equation of State Calculations by Fast Computing Machines* (J. Chem. Phys.
21, 1087) firma cinco autores: Nicholas Metropolis, Arianna W. Rosenbluth,
Marshall N. Rosenbluth, Augusta H. Teller y Edward Teller.

En una entrevista de 2003, poco antes de morir, Marshall Rosenbluth describió
así el reparto (recogido en Gubernatis, Phys. Plasmas 12, 057303, 2005):
Metropolis no participó en el desarrollo más allá de proporcionar tiempo de
máquina; Edward Teller aportó la sugerencia inicial de muestrear en el espacio
de configuraciones en lugar de en el de momentos; Augusta Teller empezó parte
de la programación; y **el algoritmo y la programación completa fueron obra de
Marshall y Arianna Rosenbluth**. Arianna Rosenbluth, doctora en física por
Harvard, escribió el código del MANIAC entera.

El algoritmo se conoce universalmente como «de Metropolis». La convención de
ordenar los autores alfabéticamente, combinada con la costumbre de citar por el
primer autor, produjo una atribución que Marshall Rosenbluth pasó cincuenta
años corrigiendo cuando le preguntaban. Se cuenta aquí no por afán
revisionista, sino porque **entender cómo se produce el conocimiento incluye
entender cómo se reparte el crédito**.

**Von Neumann y el estado de pecado** · *Nivel de verificación: A.*

Von Neumann inventó el método del «cuadrado medio» para generar dígitos
pseudoaleatorios: coge un número, elévalo al cuadrado, quédate con los dígitos
centrales, repite. Es un método malísimo —cae en ciclos cortos con facilidad—
y él lo sabía. En su artículo de 1951 escribió la frase que se ha citado desde
entonces: cualquiera que considere métodos aritméticos para producir dígitos
aleatorios está, por supuesto, en estado de pecado.

Su argumento no era místico sino práctico: una secuencia determinista no es
aleatoria, y el único aval de que sirva es que pase las pruebas estadísticas
que importan para tu problema. Setenta años después, el argumento sigue siendo
exactamente ese.
:::

---

## 9. Problemas

En `problemas.md`; soluciones en `soluciones.md`.

---

## 10. Experimento computacional

::: experimento
**Rompe tu propio MCMC.**

*Pregunta:* ¿cuánto tarda una cadena en delatar que no ha convergido?

*Diseño.* Toma la distribución bimodal del capítulo con dos modos separados una
distancia $\Delta$ ajustable. Para cada $\Delta$, arranca cuatro cadenas desde
puntos distintos y corre $10^5$ pasos con paso de propuesta fijo.

*Análisis.* Calcula $\hat R$ de Gelman–Rubin y $N_{\text{ef}}$ para cada
$\Delta$. Dibuja el número de saltos entre modos frente a $\Delta$.

*Qué esperar:* el número de saltos cae exponencialmente con $\Delta$ (es un
problema de barrera). A partir de cierto $\Delta$, ninguna cadena cruza y
**$\hat R$ lo detecta pero la traza individual no**.

*Qué falsaría la conclusión:* si una sola cadena bastara para detectarlo,
$\hat R$ sería innecesario. Compruébalo: ¿hay algún diagnóstico de cadena
única que funcione aquí? (Respuesta corta: no de forma fiable, y esa es la
razón de que se recomienden siempre varias cadenas.)
:::

---

## 11. Explícalo

::: explica
1. ¿Cómo puede un método aleatorio dar la respuesta a un problema determinista?
2. ¿Por qué el error de Monte Carlo no depende de la dimensión, y por qué el de
   una rejilla sí?
3. Explica el muestreo por importancia sin fórmulas, usando la idea de «mirar
   donde pasan las cosas y corregir después».
4. ¿Por qué en Metropolis se cancela la constante de normalización, y por qué
   eso lo cambia todo?
5. ¿Por qué una tasa de aceptación del 40 % puede corresponder a una cadena
   inservible?
6. ¿Qué le dirías a alguien que presenta un resultado de MCMC con barras
   calculadas como $\sigma/\sqrt N$?
:::

---

## 12. Lo esencial

::: esencial
* Toda integral es una esperanza, y toda esperanza se estima muestreando. Ese
  es el método entero.
* $\epsilon=\sigma_f/\sqrt N$. El exponente es malo y no se puede mejorar
  fácilmente; **la constante sí**, y ahí está el oficio.
* La dimensión no aparece en la fórmula. El cruce con una rejilla está en
  $d\approx4$–$5$, mucho antes de lo que la gente cree.
* Cuasi-Monte Carlo (Sobol) consigue casi $1/N$ para funciones suaves en
  dimensión moderada. Es gratis: úsalo.
* Muestreo: inversa si puedes, rechazo si no, importancia si el suceso es raro.
  La propuesta debe tener colas al menos tan pesadas como el objetivo.
* Metropolis funciona porque sólo necesita cocientes, y en el cociente se
  cancela $Z$.
* La tasa de aceptación **no** diagnostica convergencia. $N_{\text{ef}}$ y
  varias cadenas, sí.
* En MCMC, toda barra de error se calcula con $N_{\text{ef}}$, nunca con $N$.
* Un resultado demasiado bueno es tan sospechoso como uno demasiado malo
  (Lazzarini).
:::

---

## 13. Preguntas que quedan abiertas

::: abierto
* ¿Se puede demostrar alguna vez que una cadena ha convergido, o sólo que no lo
  ha hecho?
* ¿Cuál es la propuesta óptima en muestreo por importancia, y por qué en
  general no se puede construir?
* Si cuasi-Monte Carlo es mejor, ¿por qué no se usa siempre? ¿Qué se pierde al
  renunciar a la aleatoriedad?
* Hamiltonian Monte Carlo usa gradientes para proponer movimientos lejanos con
  alta aceptación. ¿Qué le impide resolver el problema multimodal?
* Si el ordenador no puede generar azar de verdad, ¿en qué sentido son
  correctos nuestros resultados? (Von Neumann tenía una respuesta pragmática.
  ¿Es suficiente?)
:::
