# Capítulo 12 — Fourier: ver el mundo en frecuencias

> **Qué sabrás hacer al terminar**
> · Entender por qué las sinusoides son especiales y no una elección arbitraria ·
> Leer un espectro y saber qué pregunta responde ·
> Reconocer aliasing antes de que arruine una medida ·
> Estimar una densidad espectral correctamente, y no con el módulo de la FFT ·
> Resolver la ecuación del calor en dos líneas.
>
> **Herramientas que usa:** capítulos 6, 8 y 11.
> **Disciplinas de los ejemplos:** acústica, imagen, sismología,
> instrumentación, comunicaciones, cristalografía.
> **Deuda que paga:** la ecuación del calor que quedó sin resolver en el
> capítulo 6; los autovectores del capítulo 11.
> **Deuda que abre:** la deconvolución como problema inverso (capítulo II.14).

---

## 1. Una pregunta

::: pregunta
Grabas con el móvil el zumbido de un motor. El fichero son 44 100 números por
segundo, y mirarlo no dice absolutamente nada: es una maraña.

**¿Cómo se averigua, a partir de esa maraña, a cuántas revoluciones gira el
motor y si le falta un diente a un engranaje?**
:::

La respuesta es cambiar de base. Y la razón por la que ese cambio de base
concreto funciona no es estética ni histórica: es que las sinusoides son los
**autovectores de la derivada**, y por tanto de cualquier sistema lineal
invariante en el tiempo. El capítulo 11 ya lo prometió; aquí se cobra.

---

## 2. Antes de calcular

::: antes
1. Si muestreas a 100 Hz una señal de 130 Hz, ¿qué ves?
2. Si tomas 10 veces más datos, ¿mejora 10 veces tu estimación del espectro?
3. ¿Puedes conocer a la vez, con precisión arbitraria, la frecuencia de una
   señal y el instante en que ocurre?

Las respuestas son «30 Hz», «no, no mejora nada» y «no», y las tres son
importantes.
:::

---

## 3. La intuición

### 3.1 Por qué las sinusoides y no otra cosa

Cualquier base sirve para descomponer una señal. Podríamos usar polinomios,
ondículas, funciones escalón. ¿Por qué las sinusoides han acabado dominando?

Porque cumplen algo que ninguna otra familia cumple: si derivas una
exponencial compleja, obtienes la misma exponencial multiplicada por un número.

$$\frac{d}{dt}e^{i\omega t}=i\omega\,e^{i\omega t}$$

Es decir: **$e^{i\omega t}$ es un autovector del operador derivada, con
autovalor $i\omega$**. Y como toda EDO lineal con coeficientes constantes está
hecha de derivadas, esas exponenciales son sus autovectores. En esa base,
derivar es multiplicar, y una ecuación diferencial se convierte en una ecuación
algebraica.

Eso es literalmente el capítulo 11 aplicado a un espacio de funciones:
**Fourier es diagonalizar**. Y explica por qué la transformada aparece
exactamente donde hay linealidad e invariancia temporal, y no aparece —o
aparece mucho peor— cuando alguna de las dos falla.

### 3.2 Un espectro es una respuesta a una pregunta

Un espectro no es «la señal vista de otra manera» sin más. Es la respuesta a
una pregunta concreta: *¿cuánta energía hay a cada ritmo?*

* En el motor: los picos están en la frecuencia de giro y sus armónicos. Un
  diente roto añade una banda lateral a la frecuencia de engrane, y ese es
  literalmente el diagnóstico industrial.
* En una estrella: las frecuencias de oscilación dan la estructura interna
  (astrosismología).
* En un cristal: los picos de difracción dan las distancias interatómicas.
* En un electroencefalograma: las bandas alfa, beta y theta.
* En una serie económica: la estacionalidad.

En todos, la operación matemática es la misma y la pregunta física es distinta.

---

## 4. La matemática

### 4.1 Serie, transformada y el paso al continuo

Para una función periódica de periodo $2\pi$:

$$f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}\big(a_n\cos nx+b_n\sin nx\big),
\qquad a_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\cos nx\,dx$$

La fórmula de los coeficientes no se memoriza, se deduce: las sinusoides son
**ortogonales**, $\int\cos nx\cos mx\,dx=\pi\delta_{nm}$, así que proyectar
sobre cada una es tomar un producto escalar. Exactamente como se calculan las
componentes de un vector en una base ortogonal.

Cuando el periodo tiende a infinito, la suma sobre $n$ discretos se convierte en
una integral y aparece la transformada:

$$\hat f(\omega)=\int_{-\infty}^{\infty}f(t)e^{-i\omega t}\,dt$$

### 4.2 Gibbs: la esquina que no se deja hacer

![Construyendo una onda cuadrada. Izquierda: sumas parciales con 1, 2, 5 y 26 armónicos. Derecha: zoom en la discontinuidad. Lo que hay que concluir: el sobrepaso no baja de 1,17898 por muchos armónicos que sumes; sólo se estrecha.](figuras/fig_series_fourier.pdf)

Los números lo dicen sin ambigüedad:

| Armónicos | Sobrepaso máximo |
|---|---|
| 6 | 1,181302 |
| 26 | 1,179103 |
| 101 | 1,178988 |
| 2501 | 1,178956 |

Converge a $\tfrac12+\tfrac1\pi\int_0^\pi\frac{\sin t}{t}dt=1{,}178979\ldots$,
un sobrepaso permanente del **8,9 %**.

Esto no es un defecto del cálculo: es una propiedad de la convergencia. La
serie converge **puntualmente** en todo punto de continuidad y **en media
cuadrática** en todo el intervalo, pero **no uniformemente**. La diferencia
entre esos tres tipos de convergencia, que en un curso de análisis parece una
sutileza, aquí tiene consecuencias visibles: por eso los bordes de una imagen
comprimida en JPEG tienen halos, y por eso un filtro ideal en frecuencia produce
oscilaciones en el tiempo.

### 4.3 Convolución: el teorema que lo hace útil

$$(f*g)(t)=\int f(\tau)g(t-\tau)\,d\tau
\qquad\Longleftrightarrow\qquad
\widehat{f*g}=\hat f\cdot\hat g$$

**Convolucionar en el tiempo es multiplicar en frecuencia.** Ese teorema es
probablemente el resultado más rentable de todo el análisis aplicado.

![Filtrado. Arriba: la señal ruidosa y el núcleo del filtro. Abajo: el resultado en el tiempo y la respuesta en frecuencia. Lo que hay que concluir: un filtro es una convolución, y en frecuencia es simplemente multiplicar por una curva.](figuras/fig_convolucion.pdf)

Y ahí está la razón de que exista todo el tratamiento de señales moderno: una
convolución directa cuesta $\mathcal{O}(N^2)$ y vía FFT cuesta
$\mathcal{O}(N\log N)$.

| $N$ | directo | vía FFT | factor |
|---|---|---|---|
| $10^3$ | $10^6$ | $10^4$ | 100 |
| $10^4$ | $10^8$ | $1{,}3\times10^5$ | 753 |
| $10^6$ | $10^{12}$ | $2\times10^7$ | **50 000** |

La FFT de Cooley y Tukey (1965) no es una optimización menor: es lo que hizo
posible el procesado digital de señales, la tomografía, la resonancia
magnética, el radar moderno y la compresión de audio y vídeo. Un algoritmo de
tres páginas con más impacto tecnológico que la mayoría de los descubrimientos
físicos del siglo.

### 4.4 Muestreo y aliasing: el error que se ve

Al muestrear a $f_s$, cualquier frecuencia por encima de $f_s/2$ **se hace pasar
por otra más baja**.

![Aliasing. Arriba: 3 Hz muestreados a 10 Hz, bien. Abajo: 8 Hz muestreados a 10 Hz, que aparecen como 2 Hz. Derecha: el espectro que ve el analizador. Lo que hay que concluir: la señal falsa es indistinguible de una señal verdadera de 2 Hz, y ningún procesado posterior puede separarlas.](figuras/fig_aliasing.pdf)

El teorema de muestreo (Nyquist–Shannon) dice que si la señal está limitada en
banda por debajo de $f_s/2$, **se puede reconstruir exactamente** a partir de
las muestras. Es un resultado sorprendentemente fuerte: infinitos valores
recuperados a partir de una lista discreta.

Y la letra pequeña es lo que importa en la práctica: **la información perdida
por aliasing no se recupera nunca**. Por eso todo sistema de adquisición serio
lleva un filtro **analógico** antialiasing antes del conversor. Filtrar después,
en el ordenador, no sirve de nada: la señal ya se ha corrompido.

::: aviso
**La rueda de la diligencia.** En el cine, a 24 fotogramas por segundo, una
rueda que gire a algo más de 24 vueltas por segundo aparece girando despacio
hacia atrás. Es aliasing puro, y es la demostración cotidiana de que el
fenómeno no tiene nada de abstracto.

Lo mismo ocurre con las hélices en vídeo, con los muestreos de datos diarios de
un proceso con ciclo semanal, y con cualquier medida periódica tomada a
intervalos regulares. **Cada vez que muestrees algo periódico, pregúntate cuál
es tu frecuencia de Nyquist.**
:::

### 4.5 Estimar un espectro: por qué el periodograma no basta

Este apartado es el que más error práctico ahorra.

La tentación es calcular $|\text{FFT}(x)|^2$ y llamarlo espectro. El problema:
ese estimador —el **periodograma**— tiene una varianza que **no baja al
aumentar el número de datos**. Con más muestras se obtiene más resolución en
frecuencia, pero cada punto del espectro sigue teniendo un error relativo del
100 %.

![Estimación espectral. Izquierda: el periodograma con 4096 y con 65 536 muestras; dieciséis veces más datos y el mismo ruido. Derecha: el método de Welch con tres tamaños de ventana. Lo que hay que concluir: el periodograma no converge; hay que promediar.](figuras/fig_psd.pdf)

La razón es que cada punto del periodograma se estima esencialmente con **dos
grados de libertad**, independientemente de $N$. Al aumentar $N$ se añaden
puntos de frecuencia, no precisión por punto.

La solución (Bartlett, 1948; Welch, 1967) es partir la señal en $K$ segmentos,
calcular el periodograma de cada uno y promediarlos: la varianza baja como
$1/K$. Y el compromiso es el de siempre: más segmentos, menos varianza y peor
resolución en frecuencia.

En Python: `scipy.signal.welch`, no `np.abs(np.fft.fft(x))**2`. La diferencia
en la desviación típica del logaritmo del espectro, en el ejemplo, es de 0,71 a
0,42, y con más promediado sigue bajando.

### 4.6 Tiempo o frecuencia: no puedes tener las dos

Una señal muy localizada en el tiempo tiene un espectro muy ancho, y al revés.
Cuantitativamente:

$$\Delta t\,\Delta\omega\ge\tfrac12$$

Es una propiedad matemática de la transformada de Fourier, y el principio de
incertidumbre de Heisenberg es un **caso particular** de ella aplicado a la
relación entre posición y momento —cuya conexión es precisamente una
transformada de Fourier—.

Consecuencia práctica: para resolver dos frecuencias separadas $\Delta f$ hace
falta observar durante al menos $T\approx1/\Delta f$. Si quieres distinguir
dos tonos separados 1 Hz, necesitas un segundo de señal, y no hay ningún
algoritmo que lo evite. De ahí salen los espectrogramas y las ondículas: no
resuelven el compromiso, lo **gestionan** eligiendo dónde gastar la resolución.

### 4.7 La ecuación del calor, en dos líneas

Aquí se paga la deuda del capítulo 6. La ecuación

$$\frac{\partial u}{\partial t}=D\frac{\partial^2u}{\partial x^2}$$

es una EDP, difícil. Transformando en el espacio, $\partial_x\to ik$:

$$\frac{\partial \hat u(k,t)}{\partial t}=-Dk^2\,\hat u(k,t)
\qquad\Longrightarrow\qquad
\hat u(k,t)=\hat u(k,0)\,e^{-Dk^2t}$$

**Cada modo de Fourier evoluciona independientemente**, y lo hace con la
ecuación más sencilla del capítulo 6. La EDP se ha convertido en infinitas EDO
desacopladas, que es exactamente lo que hacían los modos normales del capítulo
11 con las tres masas.

Y la solución dice una cosa físicamente enorme: el factor $e^{-Dk^2t}$ amortigua
los modos **proporcionalmente al cuadrado del número de onda**. Los detalles
finos (k grande) desaparecen muchísimo más deprisa que los gruesos. Por eso la
difusión borra estructura de pequeña escala primero, por eso el tiempo de
difusión escala como $L^2$, y por eso el problema inverso —reconstruir el pasado
a partir del presente— es **irremediablemente mal condicionado**: hay que
dividir por $e^{-Dk^2t}$, un número minúsculo, y eso amplifica el ruido de
forma explosiva. El capítulo II.14 vive entero de esa observación.

---

## 5. El ordenador entra en escena

::: antes
Vamos a analizar una señal con dos tonos débiles enterrados en ruido $1/f$.
Antes de ejecutar:

* ¿Los verás en el periodograma crudo?
* ¿Cuántas muestras hacen falta para separar dos tonos a 120 y 122 Hz?
* Si promedias segmentos, ¿qué pierdes?
:::

```python
import numpy as np
from scipy import signal

f, P = signal.welch(x, fs=1000, nperseg=4096)   # promedia segmentos
# NO:  P = np.abs(np.fft.rfft(x))**2            # varianza que no baja
```

Separar 120 de 122 Hz exige $T\ge1/2\ \text{Hz}=0{,}5$ s, es decir 500 muestras
a 1 kHz. Con ventanas de 256 muestras es imposible aunque promedies mil veces:
la resolución la fija la **longitud de la ventana**, no el número total de
datos. Ese es el compromiso de Welch en su forma más concreta.

::: juega
1. Cambia el tamaño de ventana de 256 a 8192. ¿Cuándo aparecen los dos tonos
   por separado? ¿Qué pasa con el ruido de fondo?
2. Aplica una ventana de Hann y compárala con la rectangular. Fíjate en las
   faldas alrededor de los picos: eso es *fuga espectral*.
3. Muestrea a 200 Hz una señal con contenido hasta 300 Hz y comprueba que el
   espectro es mentira. Después filtra **antes** de muestrear y compruébalo.
4. Resuelve la ecuación del calor por Fourier y compara con las diferencias
   finitas del capítulo 8. ¿Cuál es más rápido? ¿Cuál admite condiciones de
   contorno arbitrarias?
:::

---

## 6. ¿Qué estamos suponiendo?

::: supuestos
1. **Que el sistema es lineal e invariante en el tiempo.** Si los parámetros
   cambian o hay no linealidad, la descomposición modal deja de desacoplar y
   aparecen armónicos e intermodulación.
2. **Que la señal es estacionaria.** El espectro de una señal cuya frecuencia
   cambia es un promedio sin significado. Ahí hacen falta espectrogramas.
3. **Que la señal está limitada en banda** por debajo de Nyquist.
4. **Que el registro es lo bastante largo** para la resolución que pretendes.
5. **Que el muestreo es uniforme.** Con muestreo irregular —frecuente en
   astronomía— la FFT no vale y hay que usar Lomb–Scargle.
6. **Que la señal es periódica en la ventana**, cosa que casi nunca es cierta
   y produce fuga espectral. Por eso se enventana.
:::

---

## 7. ¿Cuándo falla?

::: falla
**Falla con señales no estacionarias.** El espectro de una sirena que sube de
tono es una banda ancha sin significado. La herramienta correcta es el
espectrograma (STFT) o las ondículas.

**Falla el aliasing, y falla en silencio.** Un pico a 30 Hz puede ser una señal
de 30 Hz o una de 130 Hz mal muestreada, y **no hay forma de distinguirlas a
posteriori**. La única defensa es un filtro analógico antes del conversor.

**Falla la fuga espectral.** Si la señal no completa un número entero de ciclos
en la ventana, la discontinuidad de los extremos reparte energía por todo el
espectro y puede enterrar picos débiles. Se corrige enventanando, a costa de
ensanchar los picos.

**Falla el periodograma como estimador.** No converge. Ya lo hemos dicho, pero
merece decirlo dos veces porque se sigue haciendo constantemente.

**Falla con no linealidad.** Un sistema no lineal genera frecuencias que no
estaban en la entrada. Ver un armónico a $2f_0$ no significa que hubiera un
$2f_0$ en la señal: significa que hay una no linealidad, y esa es a menudo la
información más interesante.

**Y falla la deconvolución ingenua.** Dividir por $\hat h$ para «deshacer» un
filtro amplifica el ruido allí donde $\hat h$ es pequeño, que es justamente
donde el filtro ha borrado la señal. Capítulo II.14.
:::

### Un anti-ejemplo: el ciclo de 11 años que no existía

Un equipo analiza una serie mensual de 30 años, calcula su periodograma y
encuentra un pico prominente a un periodo de 11 años. Coincide con el ciclo
solar. Se publica una correlación.

Tres problemas, cada uno suficiente para invalidar el resultado. Primero: con
30 años de datos sólo caben **2,7 ciclos** de 11 años; la resolución en
frecuencia es tan mala que el pico abarca desde 8 hasta 20 años. Segundo: en
ruido $1/f$ —que describe casi toda serie geofísica— los picos espurios en
frecuencias bajas son **la norma**, no la excepción, porque ahí es donde está
toda la potencia. Tercero: no se ha calculado ningún nivel de significancia
frente a un modelo nulo de ruido coloreado.

La comprobación honesta es la del capítulo 7: **datos sustitutos**. Genera 1000
series con el mismo espectro de potencias pero fases aleatorias, calcula el
máximo del periodograma en cada una y mira en qué percentil cae tu pico. Casi
siempre, en el 40.

---

## 8. Historia

::: historia
**Fourier, 1807: una idea correcta rechazada por los mejores** ·
*Nivel de verificación: A.*

En diciembre de 1807, Joseph Fourier presentó a la Académie des Sciences una
memoria sobre la propagación del calor donde afirmaba que **cualquier** función,
incluso con esquinas, podía representarse como suma de senos y cosenos.

El comité evaluador estaba compuesto por Lagrange, Laplace, Monge y Lacroix.
Lagrange se opuso. Su objeción era razonable y en cierto sentido correcta: no se
podía admitir que una suma de funciones analíticas y suaves representara una
función con discontinuidades; y en efecto, Fourier no tenía una noción precisa
de convergencia con la que responder, porque esa noción no existía todavía. La
memoria **no se publicó**.

Fourier ganó el premio de la Académie en 1812 con una versión ampliada, con las
mismas objeciones anotadas en el dictamen. Sólo en 1822, ya secretario
perpetuo de la Académie, publicó la *Théorie analytique de la chaleur*.

El desenlace es instructivo por partida doble. **Fourier tenía razón en lo
esencial**: la representación existe y funciona. **Lagrange tenía razón en el
detalle**: hacía falta un concepto de convergencia que sólo llegó con Dirichlet
en 1829. La necesidad de precisar qué significa que una serie converja fue uno
de los motores del rigor del siglo XIX, y de ahí salieron la definición de
límite, la integral de Riemann, la de Lebesgue y buena parte del análisis
moderno.

La lección que interesa aquí es que **una objeción técnica correcta puede
retrasar quince años una idea correcta**, y que el desacuerdo era productivo:
ambas partes estaban viendo algo real.

**Cooley, Tukey y una historia con doble fondo** ·
*Nivel de verificación: A.*

El artículo de James Cooley y John Tukey de 1965 tiene tres páginas y es uno de
los más citados de la historia de la computación. Redujo el coste de la
transformada discreta de $\mathcal{O}(N^2)$ a $\mathcal{O}(N\log N)$.

El contexto merece contarse: Tukey desarrolló la idea en el marco del comité
asesor científico de la presidencia estadounidense, trabajando en la detección
sísmica de ensayos nucleares soviéticos, un problema que exigía analizar
enormes cantidades de datos de sismógrafos. La motivación era la verificación
de un tratado de prohibición de ensayos.

Y hay un doble fondo excelente. En 1984, Heideman, Johnson y Burrus
descubrieron que **Gauss había desarrollado el mismo algoritmo en 1805**, para
interpolar las órbitas de los asteroides Palas y Juno. Lo escribió en latín, en
una notación oscura, y no lo publicó: apareció póstumamente en sus obras
completas en 1866. Es anterior incluso al trabajo de Fourier.

Un algoritmo que habría ahorrado siglo y medio de cálculo, escondido en un
cuaderno.
:::

---

## 9. Problemas

En `problemas.md`; soluciones en `soluciones.md`.

---

## 10. Experimento computacional

::: experimento
**Diagnostica una máquina por su sonido.**

*Pregunta:* ¿se puede detectar un defecto mecánico con el micrófono del móvil?

*Diseño.* Graba un ventilador, un motor o un electrodoméstico con rotación.
Calcula su densidad espectral con Welch. Identifica la frecuencia fundamental
de giro (compárala con las revoluciones nominales) y sus armónicos.

*Análisis.* Repite la grabación en dos condiciones distintas: con el aparato
limpio y con un pequeño desequilibrio añadido (un trozo de cinta en un aspa).
Compara los espectros. El desequilibrio debe aparecer como un aumento del
armónico a la frecuencia de giro.

*Criterio de parada:* tres grabaciones de 10 s por condición.

*Qué falsaría el resultado:* si la diferencia entre grabaciones de la **misma**
condición es comparable a la diferencia entre condiciones, no has detectado
nada. Mide esa variabilidad primero: es el equivalente espectral de la barra de
error del capítulo 5, y casi nadie la calcula.
:::

---

## 11. Explícalo

::: explica
1. ¿Por qué las sinusoides y no otra base? Explícalo sin usar la palabra
   «autovector» y luego con ella.
2. ¿Por qué una esquina necesita infinitas frecuencias?
3. Explica el aliasing con la rueda de la diligencia.
4. ¿Por qué el periodograma no mejora con más datos, si todo lo demás en
   estadística sí?
5. ¿Por qué no se puede conocer a la vez la frecuencia exacta y el instante
   exacto?
6. ¿Por qué la difusión borra los detalles finos antes que los gruesos?
:::

---

## 12. Lo esencial

::: esencial
* Las sinusoides son los autovectores de la derivada. Fourier es
  diagonalizar, y por eso funciona donde hay linealidad e invariancia temporal.
* Los coeficientes salen de proyectar sobre una base ortogonal: es el producto
  escalar de siempre.
* Gibbs: el sobrepaso del 8,9 % no desaparece nunca, sólo se estrecha. Es la
  diferencia entre convergencia puntual y uniforme, y se ve en los halos del
  JPEG.
* Convolucionar en el tiempo es multiplicar en frecuencia. Con FFT, factor
  50 000 a $N=10^6$.
* Por encima de Nyquist, las frecuencias se hacen pasar por otras y **eso no se
  arregla después**. Filtro analógico antes del conversor.
* El periodograma no converge. Usa Welch, y entiende el compromiso entre
  resolución y varianza.
* $\Delta t\,\Delta\omega\ge1/2$: para separar dos tonos a $\Delta f$ hay que
  medir $1/\Delta f$. No hay algoritmo que lo evite.
* En Fourier, la ecuación del calor se desacopla en modos con
  $e^{-Dk^2t}$: los detalles finos mueren primero, y el problema inverso está
  mal condicionado por construcción.
:::

---

## 13. Preguntas que quedan abiertas

::: abierto
* Si la señal no es estacionaria, ¿qué significa exactamente «su espectro»?
* ¿Cuándo conviene una base de ondículas en lugar de Fourier, y qué se gana
  exactamente?
* El muestreo comprimido (*compressed sensing*) recupera señales por debajo de
  Nyquist si son dispersas. ¿Contradice el teorema de muestreo, o cambia la
  pregunta?
* ¿Cómo se establece la significancia de un pico espectral frente a ruido
  coloreado, de forma que resista una revisión?
* Si Gauss tenía la FFT en 1805 y no la publicó, ¿cuántas ideas equivalentes
  hay hoy en cuadernos y repositorios sin leer?
:::
