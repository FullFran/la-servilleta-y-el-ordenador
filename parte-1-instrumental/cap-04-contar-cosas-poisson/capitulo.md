# Capítulo 4 — Contar cosas: Poisson, ruido y fluctuaciones

> **Qué sabrás hacer al terminar**
> · Reconocer un proceso de Poisson por su mecanismo y no por su fórmula ·
> Usar $\sigma_N=\sqrt N$ como herramienta de diseño experimental ·
> Calcular cuánto tiempo hay que medir para detectar algo sobre un fondo ·
> Detectar sobredispersión y saber qué significa físicamente ·
> No caer en la paradoja del autobús, que aparece disfrazada por todas partes.
>
> **Herramientas que usa:** capítulos 1 y 3.
> **Disciplinas de los ejemplos:** física nuclear, astronomía, telefonía,
> biología molecular, informática de sistemas, transporte, epidemiología.
> **Deuda que abre:** la inferencia de la tasa con pocos sucesos (capítulo 5) y
> la comparación de hipótesis (capítulo II.4).

---

## 1. Una pregunta

::: pregunta
Miras una zona oscura del cielo con un telescopio durante una hora y detectas
**12 fotones**. El fondo instrumental, medido apuntando a una pared, produce
**8 fotones** por hora.

**¿Has detectado una fuente, o has visto ruido?**
:::

La respuesta —«probablemente ruido»— no depende de la astronomía. Depende de una
sola propiedad de los procesos de conteo, y esa propiedad gobierna el diseño de
experimentos en física de partículas, la calidad de una imagen médica, el
dimensionado de una centralita telefónica, la secuenciación de ADN y el número
de réplicas que necesitas en un ensayo clínico.

La propiedad cabe en cuatro caracteres: $\sigma=\sqrt{N}$.

---

## 2. Antes de calcular

::: antes
Antes de seguir:

1. Si cuentas 100 sucesos, ¿cuál es tu incertidumbre? ¿Y si cuentas 10 000?
2. Si mides el doble de tiempo, ¿mejora tu precisión relativa al doble?
3. Los autobuses pasan cada 10 minutos de media, sin horario fijo. Llegas a la
   parada en un instante cualquiera. ¿Cuánto esperas de media?

La tercera respuesta es 10 minutos y no 5, y la razón es más profunda de lo que
parece.
:::

---

## 3. La intuición

### 3.1 Contar es medir

Hay dos formas de medir una intensidad. Puedes medir una magnitud continua —una
tensión, una temperatura— y entonces tu error depende del instrumento. O puedes
**contar sucesos discretos**, y entonces tu error no depende del instrumento en
absoluto: está impuesto por la naturaleza discreta del proceso.

Esa segunda situación es más común de lo que parece. Fotones en un detector,
desintegraciones, moléculas que cruzan una membrana, clientes que entran,
paquetes que llegan a un servidor, mutaciones en un genoma, coches que pasan por
un peaje. En todos ellos, el «ruido» no es un defecto del aparato: **es física
del proceso**, y no se puede reducir comprando algo mejor. Sólo se puede reducir
contando más.

### 3.2 Tres maneras de llegar a Poisson

La distribución de Poisson aparece siempre que se cumplen tres condiciones:
sucesos **raros**, **independientes** y con **tasa constante**. Conviene verla
salir por tres caminos distintos, porque cada uno ilumina una faceta.

**Camino 1: límite de la binomial.** Divide un intervalo de tiempo $T$ en $n$
trocitos diminutos. En cada trocito hay un suceso con probabilidad $p=\lambda
T/n$, muy pequeña. El número total de sucesos es binomial$(n,p)$, y en el límite
$n\to\infty$ con $\lambda T$ fijo se obtiene Poisson. Este camino explica por
qué la distribución no depende de $n$: los detalles de cómo troceas se borran.

**Camino 2: la ecuación maestra.** Sea $P_k(t)$ la probabilidad de llevar $k$
sucesos en el instante $t$. En un $dt$ ocurre un suceso con probabilidad
$\lambda\,dt$:

$$\frac{dP_k}{dt}=\lambda P_{k-1}-\lambda P_k$$

Con $P_k(0)=\delta_{k0}$, la solución es $P_k(t)=e^{-\lambda t}(\lambda
t)^k/k!$. Este camino es el más físico y es el que conecta con las ecuaciones
diferenciales del capítulo 6.

**Camino 3: máxima entropía.** De todas las distribuciones sobre los enteros no
negativos con media fijada y con la propiedad de ser infinitamente divisible,
Poisson es la que menos supone. Este camino conecta con el apartado 4.8 del
capítulo anterior.

Tres derivaciones, la misma respuesta. Cuando eso ocurre, la distribución no es
un accidente de modelado: es estructural.

### 3.3 La consecuencia que lo gobierna todo

Para Poisson, media y varianza **coinciden**:

$$E[N]=\lambda,\qquad \operatorname{Var}(N)=\lambda
\qquad\Longrightarrow\qquad \sigma_N=\sqrt{\lambda}\approx\sqrt N$$

De ahí sale el hecho que hay que tener tatuado:

$$\frac{\sigma_N}{N}=\frac{1}{\sqrt N}$$

**El ruido absoluto crece; el ruido relativo decrece.** Cuenta 100 y tendrás un
10 % de error. Cuenta 10 000 y tendrás un 1 %. Para ganar un factor 10 en
precisión hay que contar 100 veces más. Es la misma raíz cuadrada del capítulo 3
y la misma que gobernará Monte Carlo en el capítulo 9, y no es casualidad:
siempre es el teorema central del límite trabajando por debajo.

---

## 4. La matemática

### 4.1 Poisson contra el mundo real, dos veces

La teoría está muy bien, pero la pregunta interesante es si esto describe algo.
Dos conjuntos de datos clásicos, ambos con más de un siglo, contestan que sí.

![Poisson frente a datos reales. Izquierda: 2608 intervalos de 7,5 s contando partículas alfa (Rutherford, Geiger y Bateman, 1910). Derecha: 200 cuerpo-años de muertes por coz de caballo en el ejército prusiano (Bortkiewicz, 1898). Lo que hay que concluir: el cociente varianza/media vale 0,95 y 1,00. No es una idealización.](figuras/fig_poisson_datos.pdf)

Merece la pena detenerse en la pareja. Uno de los conjuntos procede del
laboratorio de Rutherford con instrumentación de vanguardia; el otro, de un
registro administrativo de bajas militares. Los dos siguen la misma ley con la
misma precisión, y ninguno de los dos fenómenos tiene nada que ver con el otro.

Eso es exactamente lo que este libro intenta enseñar: **la estructura
matemática no pertenece al dominio**. Cuando reconoces el mecanismo —sucesos
raros, independientes, tasa constante— sabes la respuesta antes de saber de qué
va el problema.

::: herramientas
**El test más barato del mundo: el índice de dispersión**

$$D=\frac{\operatorname{Var}(N)}{E[N]}$$

* $D\approx1$: compatible con Poisson.
* $D>1$ (**sobredispersión**): hay algo que agrupa los sucesos. Tasa variable,
  contagio, correlación positiva, mezcla de poblaciones.
* $D<1$ (**subdispersión**): hay algo que los regulariza. Tiempo muerto del
  detector, refractariedad, regulación activa.

Es una línea de código y detecta el 80 % de los modelos de conteo mal
especificados. Hazlo siempre antes de ajustar nada.
:::

### 4.2 Tiempos entre sucesos, y la paradoja del autobús

Si los sucesos son Poisson con tasa $\lambda$, el tiempo hasta el siguiente es
exponencial con media $1/\lambda$. Hasta aquí, previsible. Ahora la parte que
sorprende a todo el mundo.

Los autobuses pasan cada 10 minutos **de media**, sin horario. Llegas en un
instante al azar. ¿Cuánto esperas?

La respuesta intuitiva es 5 minutos: la mitad del intervalo. La respuesta
correcta es **10 minutos**.

![La paradoja del autobús. Izquierda: los intervalos reales entre autobuses frente a los intervalos «vistos» por un pasajero que llega al azar. Derecha: la distribución del tiempo de espera. Lo que hay que concluir: el pasajero espera un intervalo medio completo, no medio intervalo, porque tiene el doble de probabilidad de caer en un hueco el doble de largo.](figuras/fig_paradoja_autobus.pdf)

El razonamiento es geométrico y no requiere ninguna cuenta: un intervalo de 20
minutos ocupa el doble de línea temporal que uno de 10, así que un pasajero que
llega al azar tiene **el doble de probabilidad de caer dentro de él**. El
pasajero no muestrea intervalos: muestrea *tiempo*, y eso sesga la muestra hacia
los intervalos largos. En la simulación, el hueco medio real es 9,8 minutos y
el hueco medio visto por el pasajero es 19,6.

Este sesgo se llama **paradoja de la inspección** y aparece disfrazado por todas
partes:

* Tus amigos tienen de media más amigos que tú (paradoja de la amistad, Feld
  1991), porque la gente popular aparece en más listas de amigos.
* Las clases de tu universidad parecen más llenas de lo que dice la media,
  porque más estudiantes experimentan las clases grandes.
* Si preguntas a los usuarios de un servidor cuánto tarda una petición, te
  darán un número peor que la media real: las peticiones lentas afectan a más
  gente por unidad de tiempo.
* Los tiempos de espera en urgencias, los tiempos de vida de los componentes
  encontrados en servicio, la duración de las relaciones de las que la gente
  te habla.

Regla operativa: **cada vez que muestrees «un instante al azar» en lugar de «un
suceso al azar», sospecha del sesgo de longitud.**

### 4.3 Señal, fondo y significancia

Volvamos a la pregunta del principio. Cuentas $n=12$ fotones donde esperabas un
fondo $b=8$. El exceso es $s=n-b=4$. ¿Es significativo?

La fluctuación típica del fondo es $\sigma_b=\sqrt{b}=2{,}83$. Así que el exceso
vale

$$\frac{s}{\sqrt b}=\frac{4}{2{,}83}\approx 1{,}4\ \sigma$$

Un exceso de 1,4 sigmas ocurre por azar aproximadamente una de cada seis veces.
No has detectado nada.

Ahora la parte útil. Si mides durante un tiempo $t$, tanto la señal como el
fondo crecen proporcionalmente a $t$, pero el ruido sólo como $\sqrt t$:

$$\frac{s}{\sqrt b}=\frac{r_s t}{\sqrt{r_b t}}=\frac{r_s}{\sqrt{r_b}}\sqrt{t}
\;\propto\;\sqrt{t}$$

![El coste de detectar. Izquierda: la significancia crece como $\sqrt t$, con los puntos marcando cuándo se alcanzan las 5 sigmas. Derecha: horas necesarias para un descubrimiento en función del cociente señal/fondo. Lo que hay que concluir: dividir la señal por 10 multiplica el tiempo de medida por 100.](figuras/fig_deteccion_fondo.pdf)

Ese $\sqrt t$ es la ley económica de todo experimento de conteo. Duplicar la
significancia exige **cuadruplicar** el tiempo. Y de aquí sale la fórmula de
diseño que conviene saberse:

$$t_{5\sigma}=\frac{25\,r_b}{r_s^{2}}$$

Con ella se decide, antes de pedir tiempo de telescopio o de acelerador, si el
experimento es viable o es una fantasía. Y explica por qué en experimentos de
señal muy débil el esfuerzo se dedica obsesivamente a **reducir el fondo** en
vez de a aumentar la señal: el fondo entra en la ecuación linealmente y la señal
al cuadrado.

::: aviso
**El p-valor y la falacia del fiscal.** «Un exceso de 5 sigmas» significa: *si
no hubiera señal, la probabilidad de ver un exceso así de grande sería
$3\times10^{-7}$*. **No** significa que la probabilidad de que la señal sea
falsa sea $3\times10^{-7}$. Es exactamente la confusión entre
$P(\text{datos}\mid\text{hipótesis})$ y $P(\text{hipótesis}\mid\text{datos})$
del capítulo 3, y volveremos sobre ella en los capítulos 5 y II.4.

Y hay un segundo efecto que muerde: si buscas un exceso en 1000 canales
distintos, esperas ver varios de 3 sigmas **por puro azar**. Se llama efecto
*look-elsewhere* y es la razón de que en física de partículas el umbral esté en
5 sigmas y no en 3.
:::

### 4.4 Sobredispersión: cuando la varianza excede la media

Si mides $D=\operatorname{Var}/E > 1$, el modelo de Poisson está mal, y el
diagnóstico es informativo:

**La tasa no es constante.** Si $\lambda$ varía (por hora del día, por
paciente, por región), el conteo agregado es una **mezcla** de Poissons. La
mezcla más habitual —$\lambda$ distribuida como una gamma— da exactamente la
**binomial negativa**, y por eso esa distribución aparece en epidemiología, en
ecología y en conteos de RNA-seq. La sobredispersión mide la heterogeneidad de
la población.

**Los sucesos se agrupan.** Contagio, ráfagas, réplicas de terremotos, retuits.
Un suceso aumenta la probabilidad de otro, y eso viola la independencia. Los
modelos de Hawkes (procesos autoexcitados) capturan esto.

**Hay mezcla de poblaciones.** Contar juntos dos procesos con tasas distintas
produce sobredispersión aunque cada uno por separado sea Poisson perfecto.

En la dirección contraria, **la subdispersión** ($D<1$) delata un mecanismo
regulador: el tiempo muerto de un detector, que impide contar dos sucesos muy
seguidos, o el periodo refractario de una neurona. Es la firma de que algo está
suprimiendo activamente las coincidencias.

---

## 5. El ordenador entra en escena

::: antes
Vamos a simular una imagen recogida con números crecientes de fotones por
píxel. Antes de mirar:

* ¿Con cuántos fotones por píxel empiezas a distinguir un objeto de bajo
  contraste?
* ¿Cuánto tienes que subir la exposición para que el grano se reduzca a la
  mitad?
* ¿Por qué las fotos nocturnas de tu móvil salen con grano y las diurnas no,
  si el sensor es el mismo?
:::

```python
import numpy as np
rng = np.random.default_rng(4)

escena = ...                       # imagen ideal, valores entre 0 y 1
for n_medio in [1, 10, 100, 1000, 10_000, 100_000]:
    imagen = rng.poisson(escena * n_medio)     # el único ruido es el conteo
    print(f"{n_medio:>7,}: ruido relativo ≈ {100/np.sqrt(n_medio):.1f} %")
```

![La misma escena con seis exposiciones. Lo que se ve: el grano desapareciendo. Lo que hay que concluir: no hay ningún modelo de sensor en este código. Todo el grano que ves es la estadística de contar fotones.](figuras/fig_imagen_fotones.pdf)

Esta figura merece un momento de atención porque contiene un mensaje que suele
sorprender: **no hay ningún modelo de cámara en la simulación**. No hay ruido de
lectura, ni corriente oscura, ni electrónica. Sólo `rng.poisson`. Todo lo que
se ve es la naturaleza discreta de la luz.

Y de ahí sale una conclusión práctica: por debajo de cierto nivel de luz,
**ninguna cámara puede hacerlo mejor**, porque el límite no es tecnológico. Es
la misma razón por la que una radiografía con menos dosis tiene más grano, y por
la que existe un compromiso irreductible entre dosis al paciente y calidad de
imagen. No es un problema de ingeniería: es $\sqrt N$.

::: juega
1. Cambia el contraste de la escena a la mitad. ¿Cuántos fotones necesitas
   ahora para ver lo mismo? ¿Sale el factor 4 que predice la teoría?
2. Suma un fondo constante a la escena. ¿Ayuda o estorba? ¿Por qué el fondo
   empeora la imagen aunque «aporte señal»?
3. Añade ruido de lectura gaussiano de 5 electrones. ¿A partir de qué nivel de
   señal deja de importar?
4. Promedia 100 imágenes de 100 fotones. ¿Es igual que una imagen de 10 000?
   ¿Bajo qué condiciones sí, y bajo cuáles no?
:::

---

## 6. ¿Qué estamos suponiendo?

::: supuestos
1. **Tasa constante durante la medida.** Válido si el tiempo de observación es
   mucho menor que cualquier escala de variación (vida media, ciclo diario,
   deriva instrumental).
2. **Independencia entre sucesos.** Falla con contagio, con ráfagas y con
   apilamiento en el detector.
3. **Sin tiempo muerto.** Todo detector real tiene un intervalo tras cada
   suceso en el que no puede registrar otro. A tasas altas esto produce
   subdispersión y **subestimación sistemática** de la tasa.
4. **Fondo bien conocido.** En la fórmula $s/\sqrt b$ hemos supuesto $b$ exacto.
   Si $b$ se ha medido, su propia incertidumbre entra en el cálculo y la
   significancia baja.
5. **Un solo canal de búsqueda.** Si buscas en muchos sitios a la vez, el umbral
   debe subir.
6. **Eficiencia de detección constante y conocida.** Si varía con la energía,
   la posición o el tiempo, el conteo mide una mezcla.
:::

---

## 7. ¿Cuándo falla?

::: falla
**Falla con tasas variables.** Contar llamadas telefónicas a lo largo del día
con una única $\lambda$ produce sobredispersión garantizada. La solución no es
un modelo más complicado: es **trocear** el tiempo en tramos donde la tasa sea
aproximadamente constante.

**Falla con apilamiento.** A tasas altas, dos sucesos separados por menos que el
tiempo de resolución se cuentan como uno. La tasa medida $m$ y la real $r$ se
relacionan por $m = r\,e^{-r\tau}$ (modelo paralizable) o $m=r/(1+r\tau)$ (no
paralizable). En ambos casos **la tasa medida satura**, y un experimentador
despistado puede concluir que la fuente se ha estabilizado cuando lo que ha
saturado es su electrónica.

**Falla si el fondo no es Poisson.** Un fondo con deriva lenta o con
contaminación intermitente tiene mucha más varianza que $\sqrt b$, y la
significancia calculada es fantasía.

**Falla por el efecto look-elsewhere.** Buscar en 1000 sitios y quedarse con el
mejor es un procedimiento distinto de mirar en uno. Con 1000 canales,
$P(\text{algún canal} \ge 3\sigma)\approx 1-(1-0{,}00135)^{1000}\approx 74\,\%$:
casi seguro que encuentras «algo».
:::

### Un anti-ejemplo: el detector que mejoraba con el tiempo

Un grupo mide la tasa de una fuente y observa que, al aumentar el tiempo de
medida, la tasa estimada **converge a un valor menor** que el de las primeras
medidas cortas. Se concluye que la fuente decae. La tentación es ajustar una
exponencial y publicar una vida media.

Lo que ocurría era otra cosa: las medidas cortas se habían tomado con la fuente
más cerca del detector, con más apilamiento... y menos cuentas registradas de
las reales, no más. En realidad el efecto era el contrario y el signo del
«decaimiento» procedía de un cambio de geometría no documentado.

La moraleja es del capítulo 15 y conviene adelantarla: **cuando encuentres un
efecto interesante, la primera hipótesis siempre debe ser que es tuyo**.

---

## 8. Historia

::: historia
**Bortkiewicz y los caballos** · *Nivel de verificación: A (fuente primaria).*

En 1898, Ladislaus von Bortkiewicz publicó *Das Gesetz der kleinen Zahlen* («la
ley de los pequeños números»). Buscaba demostrar que los sucesos raros siguen
una regularidad estadística, y para ello usó un conjunto de datos
maravillosamente absurdo: las muertes por coz de caballo en catorce cuerpos del
ejército prusiano a lo largo de veinte años.

Doscientos cuerpo-años, 122 muertes, media 0,61. El ajuste de Poisson es
excelente: 109 cuerpo-años con cero muertes frente a 108,7 predichos.

Lo interesante del episodio no es el ajuste, sino la elección del dato. Nadie
había pensado que ese registro administrativo contuviera una ley. Bortkiewicz
entendió que **el mecanismo importa más que el dominio**: sucesos raros,
independientes, tasa aproximadamente constante. Es la mentalidad que este libro
persigue.

**Rutherford, Geiger y Bateman, 1910** · *Nivel de verificación: A.*

Rutherford y Geiger contaron centelleos producidos por partículas alfa en 2608
intervalos de 7,5 segundos —a ojo, en una habitación oscura, turnándose porque
la vista se cansaba—. Harry Bateman aportó el tratamiento matemático. El
resultado es el mismo: media 3,87, varianza 3,69.

El experimento tiene una implicación física profunda que a veces se pasa por
alto: **la concordancia con Poisson es la prueba de que las desintegraciones son
independientes**. Un núcleo no sabe lo que hacen los demás, y no envejece. Toda
la datación radiométrica descansa sobre eso, y la evidencia empírica está en
esa tabla de 1910.

**Erlang y la centralita de Copenhague** · *Nivel de verificación: A.*

En 1909, Agner Krarup Erlang, matemático empleado por la compañía telefónica de
Copenhague, publicó *The Theory of Probabilities and Telephone Conversations*.
El problema era mundano: cuántas líneas hacen falta para que casi nadie
encuentre la centralita ocupada. Erlang modeló las llamadas como un proceso de
Poisson y dedujo las fórmulas que hoy dimensionan centros de llamadas,
servidores web y camas de hospital.

Es uno de los ejemplos más limpios de que **la ingeniería crea teoría**, y no al
revés. La unidad de tráfico telefónico se llama *erlang*, y las fórmulas B y C
de Erlang siguen usándose exactamente igual que en 1917. El capítulo II.12 las
desarrolla.
:::

---

## 9. Problemas

En `problemas.md`; soluciones en `soluciones.md`.

---

## 10. Experimento computacional

::: experimento
**Mide el tiempo muerto de un detector que no existe.**

*Pregunta:* ¿puedes deducir el tiempo muerto de un detector observando sólo su
tasa de conteo?

*Diseño.* Simula un proceso de Poisson con tasa real $r$ y descarta todo
suceso que ocurra a menos de $\tau$ del anterior registrado (modelo no
paralizable). Barre $r$ desde 10 hasta $10^6$ s⁻¹ con $\tau=1\ \mu$s.

*Análisis.* Dibuja tasa medida frente a tasa real. Comprueba la saturación.
Después ajusta $m=r/(1+r\tau)$ y recupera $\tau$. Calcula además el índice de
dispersión en función de $r$ y comprueba que baja por debajo de 1.

*Qué falsaría el modelo:* si simulas el caso paralizable (el reloj se reinicia
con cada suceso, registrado o no) la curva **no satura, decrece**. Distinguir
los dos comportamientos con datos reales es un problema clásico y no trivial de
metrología nuclear.
:::

---

## 11. Explícalo

::: explica
1. ¿Por qué el ruido de una imagen no se arregla comprando un sensor mejor?
2. Explica sin fórmulas por qué esperas 10 minutos y no 5 en la parada del
   autobús.
3. ¿Por qué en un experimento de señal débil se invierte más esfuerzo en
   reducir el fondo que en aumentar la señal?
4. ¿Qué te dice físicamente que la varianza de tus conteos sea el doble de la
   media?
5. ¿Por qué la concordancia con Poisson demuestra que los núcleos no envejecen?
6. ¿Qué le dirías a alguien que ha encontrado un exceso de 3 sigmas después de
   mirar en trescientos sitios?
:::

---

## 12. Lo esencial

::: esencial
* Contar es medir, y el ruido de contar no es un defecto del aparato: es el
  proceso.
* Poisson = sucesos raros, independientes, tasa constante. Sale por tres
  caminos distintos, así que es estructural.
* $\sigma_N=\sqrt N$: el ruido absoluto crece, el relativo baja como
  $1/\sqrt N$.
* El índice de dispersión $D=\operatorname{Var}/E$ es un test de una línea:
  $D>1$ delata agrupamiento o tasa variable; $D<1$, un mecanismo regulador.
* La significancia crece como $\sqrt t$: duplicarla cuesta cuadruplicar el
  tiempo. $t_{5\sigma}=25\,r_b/r_s^2$.
* Reducir el fondo es más rentable que aumentar la señal, porque el fondo entra
  linealmente y la señal al cuadrado.
* Muestrear un instante al azar no es lo mismo que muestrear un suceso al azar.
  Sesgo de longitud: sospecha siempre.
* Un p-valor no es la probabilidad de que tu hipótesis sea falsa, y buscar en
  mil sitios no es lo mismo que mirar en uno.
:::

---

## 13. Preguntas que quedan abiertas

::: abierto
* Si la sobredispersión indica heterogeneidad, ¿se puede recuperar la
  distribución de tasas a partir de los conteos agregados? ¿Siempre?
* ¿Cuál es el umbral de significancia «correcto»? ¿Por qué 5 sigmas y no 4 o 6?
  ¿Es una cuestión estadística o sociológica?
* La paradoja de la inspección sesga lo que observamos. ¿Cuántas estadísticas
  publicadas que usas a diario están afectadas y no lo sabes?
* Si el ruido de conteo es irreductible, ¿cómo consiguen las técnicas modernas
  de imagen «superar» el límite? ¿Qué información adicional están usando?
* ¿Hay algún proceso genuinamente aleatorio que no sea Poisson en su límite
  raro? ¿Qué tendría que fallar?
:::
