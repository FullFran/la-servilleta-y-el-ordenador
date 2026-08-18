# II.4 — ¿Cuánto podemos fiarnos de una detección?

> **El fenómeno:** un exceso de cuentas sobre el fondo.
> **Herramientas que convoca:** cap. 3 (Bayes), cap. 4 (Poisson), cap. 5
> (incertidumbre), cap. 15 (mala especificación).
> **Lo que hay que llevarse:** que la significancia estadística no es la
> probabilidad de haber descubierto algo, y que casi siempre el techo lo pone
> el sistemático y no la estadística.

---

## 1. Una pregunta

::: pregunta
Esperas 8 cuentas de fondo y observas 12.

Con la fórmula del capítulo 4, $s/\sqrt b=4/2{,}83=1{,}4\sigma$.

**¿Cuál es la probabilidad de que hayas detectado algo?**
:::

La pregunta está mal planteada, y ese es el contenido del capítulo.

---

## 2. Antes de calcular

::: antes
1. ¿Es 1,4 sigmas lo mismo que «un 92 % de probabilidad de que haya señal»?
2. Si mides diez veces más tiempo, ¿la significancia se multiplica por diez?
3. Si conoces el fondo con un 5 % de incertidumbre, ¿hay algún límite a la
   significancia que puedes alcanzar?
:::

---

## 3. Lo que dice y lo que no dice un p-valor

![Distribución de cuentas bajo las dos hipótesis, y el efecto de la incertidumbre del fondo. Izquierda: con $b=8$ y $s=4$, las dos distribuciones se solapan enormemente; observar 12 da $p=0{,}112$, es decir 1,22 sigmas. Derecha: la significancia frente al tiempo de medida, con el fondo conocido exactamente y con incertidumbre del 2 % y del 5 %. Lo que hay que concluir: la incertidumbre sistemática del fondo pone un techo que ninguna cantidad de datos supera.](figuras/fig_deteccion.pdf)

Con Poisson exacta, $P(N\ge12\mid b=8)=0{,}112$. La aproximación gaussiana daba
1,4 sigmas ($p=0{,}08$); la exacta da 1,22 sigmas. Con $\lambda<20$ hay que usar
Poisson.

Y lo que ese 0,112 significa es exactamente esto:

> Si no hubiera señal, vería un exceso así de grande o mayor el 11 % de las
> veces.

Lo que **no** significa:

* que haya un 11 % de probabilidad de que no haya señal;
* que haya un 89 % de probabilidad de que sí la haya;
* nada en absoluto sobre la hipótesis, sin una probabilidad previa.

Es la falacia del fiscal del capítulo 3, y es endémica.

---

## 4. La versión bayesiana, y por qué cambia el resultado

Para contestar «¿qué probabilidad hay de que exista la señal?» hace falta una
previa. Y el resultado depende fuertemente de ella:

$$\frac{P(S\mid n)}{P(\text{no }S\mid n)}
=\underbrace{\frac{P(n\mid S)}{P(n\mid\text{no }S)}}_{\text{factor de Bayes}}
\times\underbrace{\frac{P(S)}{P(\text{no }S)}}_{\text{previa}}$$

Con $n=12$, $b=8$ y $s=4$: el factor de Bayes es
$P(12\mid12)/P(12\mid8)=0{,}114/0{,}048=2{,}4$. Es decir, **los datos favorecen
la hipótesis con señal por un factor 2,4**. Nada más.

Si la señal era *a priori* improbable —una partícula nueva, una fuente
inesperada— con una previa de 1 entre 100, la posterior queda en 1 entre 42.
Sigue siendo muy improbable.

Ese es el argumento cuantitativo detrás del umbral de 5 sigmas en física de
partículas: **cuando buscas algo con previa muy baja y en muchos canales a la
vez, hacen falta factores de Bayes enormes para mover la posterior**. No es
tradición: es aritmética.

---

## 5. El techo sistemático

El panel derecho de la figura contiene el resultado más útil del capítulo.

Si el fondo se conoce con una incertidumbre relativa $\delta$, la significancia
es

$$\frac{s}{\sqrt{b+(\delta b)^2}}$$

y cuando $t\to\infty$, con $s=r_st$ y $b=r_bt$, el numerador crece como $t$ y
el denominador también:

$$\text{significancia}\to\frac{r_s}{\delta\,r_b}$$

**Un límite constante.** Con $r_s/r_b=0{,}5$ y $\delta=5\%$, el techo es 10
sigmas; con $\delta=20\%$, es 2,5 sigmas, y no hay tiempo de medida que lo
supere.

De aquí sale toda la estrategia experimental moderna en el régimen de señales
débiles: cuando el sistemático domina, **medir más no sirve de nada**. Lo que
hay que hacer es reducir $\delta$, y eso significa medir el fondo mejor,
normalmente en una región de control donde se sabe que no hay señal.

Es la misma estructura del capítulo 5: la parte aleatoria baja como
$1/\sqrt t$ y la sistemática no baja. Aquí, además, se puede calcular
exactamente cuándo deja de merecer la pena seguir.

---

## 6. Look-elsewhere, otra vez

Del capítulo 4: si buscas en muchos sitios, el umbral local debe subir.

La corrección se llama *trials factor*. Con $N$ búsquedas aproximadamente
independientes, la significancia global se relaciona con la local mediante
$p_{\text{global}}\approx N\,p_{\text{local}}$ para $p$ pequeño. Con $N=1000$
canales, un exceso local de 4,7 sigmas equivale a 3 sigmas globales.

La dificultad práctica es que $N$ no suele ser obvio: los canales no son
independientes, y el número efectivo depende de la resolución. Se estima
simulando: se generan muchos experimentos con sólo fondo y se mide la
distribución del máximo exceso. Es exactamente el ejercicio 4.X2.

---

## 7. ¿Cuándo falla?

::: falla
**Falla la aproximación gaussiana con pocas cuentas.** Con $\lambda<20$, usa
Poisson exacta. La diferencia entre 1,4 y 1,22 sigmas puede parecer pequeña, y
en la cola es un factor 1,4 en el p-valor.

**Falla ignorar la incertidumbre del fondo.** Es el error más caro y el más
frecuente. Una significancia calculada con $\sqrt b$ cuando $b$ se conoce al
10 % está sobreestimada, y a tiempos largos, sobreestimada por órdenes de
magnitud.

**Falla el fondo que no es Poisson.** Un fondo con deriva instrumental, con
contaminación intermitente o con estructura tiene mucha más varianza que
$\sqrt b$. Diagnóstico: mide el fondo repetidamente y comprueba su índice de
dispersión (capítulo 4).

**Falla el análisis no ciego.** Si has ajustado cortes mirando la región de
señal, tu significancia es ficción. El análisis ciego (capítulo 15) existe por
esto.
:::

---

## 8. Historia

::: historia
**El bosón de Higgs, y por qué se esperó a las 5 sigmas** ·
*Nivel de verificación: A.*

En diciembre de 2011, ATLAS y CMS presentaron excesos alrededor de 125 GeV con
significancias locales de 3,6 y 2,6 sigmas. No se anunció ningún
descubrimiento. En julio de 2012, con más datos, las significancias llegaron a
5,0 y 5,1 sigmas locales, y entonces sí.

La diferencia entre diciembre y julio no fue conceptual: fue estadística. Y la
razón de esperar es la del apartado 4: la búsqueda se hacía en un rango amplio
de masas —muchos canales— y con una previa que, aunque el Higgs estaba
predicho, requería un factor de Bayes muy grande para mover la posterior de
forma decisiva.

Las dos colaboraciones trabajaron **a ciegas** y sin comunicarse sus resultados
hasta la presentación conjunta, precisamente para que los dos análisis fueran
independientes.

**Y el contraejemplo: los 750 GeV** · *Nivel de verificación: A.*

En diciembre de 2015, ATLAS y CMS reportaron un exceso en el espectro de
difotones a 750 GeV, con significancias locales de 3,6 y 2,6 sigmas. En los
meses siguientes se publicaron **más de 500 artículos teóricos** proponiendo
explicaciones.

Con datos de 2016, el exceso desapareció por completo. Era una fluctuación.

El episodio se cuenta a veces como un fracaso de la comunidad, y es más
interesante verlo como lo que es: **el sistema funcionó exactamente como
debía**. Nadie anunció un descubrimiento; los experimentos publicaron
significancias locales y globales correctamente calculadas —la global era de
apenas 2 sigmas— y la comunidad teórica exploró un espacio de posibilidades
mientras se recogían más datos. Lo que falló fue la interpretación pública de
un exceso de 3 sigmas.

Que un 3 sigmas desaparezca no es un escándalo: es lo que ocurre
aproximadamente una de cada tres veces con excesos de 3 sigmas.
:::

---

## 9. Experimento computacional

::: experimento
**Calcula tu propio techo.**

Toma un experimento de conteo de tu campo, real o inventado con números
plausibles. Escribe $r_s$, $r_b$ y $\delta$.

Dibuja la significancia frente al tiempo con y sin sistemático. Encuentra el
tiempo a partir del cual sigues gastando y ya no ganas nada.

*Después:* calcula cuánto habría que reducir $\delta$ para alcanzar 5 sigmas, y
estima cuánto costaría esa reducción (más tiempo de calibración, una región de
control, otro detector).

*La pregunta final, que es la que importa:* con un presupuesto fijo, ¿conviene
gastarlo en medir más tiempo o en conocer mejor el fondo? La respuesta suele ser
la segunda y casi nunca se calcula.
:::

---

## 10. Lo esencial

::: esencial
* Un p-valor es $P(\text{datos}\mid\text{no hay señal})$. No es la probabilidad
  de que no haya señal, y sin previa no se puede convertir.
* El factor de Bayes mide cuánto favorecen los datos a una hipótesis frente a
  otra. Con $n=12$ y $b=8$: un factor 2,4. Poco.
* La incertidumbre del fondo pone un **techo** a la significancia:
  $r_s/(\delta r_b)$. Ninguna cantidad de datos lo supera.
* Cuando el sistemático domina, medir más no sirve: hay que medir mejor el
  fondo.
* Look-elsewhere: con 1000 canales, 4,7 sigmas locales son 3 globales.
* Con $\lambda<20$, Poisson exacta y no aproximación gaussiana.
* Un exceso de 3 sigmas desaparece aproximadamente un tercio de las veces. Eso
  no es un escándalo: es la definición.
:::

---

## 11. Preguntas abiertas

::: abierto
* ¿Cuál debería ser el umbral en campos donde no se pueden acumular más datos
  —una observación astronómica única, un ensayo clínico irrepetible—?
* ¿Cómo se elige una previa defendible para una hipótesis que nunca se ha
  observado?
* Si el techo lo pone el sistemático, ¿cómo se decide cuánto invertir en
  reducirlo frente a cuánto en estadística?
* ¿Es posible un análisis ciego en campos observacionales, donde los datos ya
  existen y son públicos?
:::

### Referencias

* **Cowan, Glen.** *Statistical Data Analysis.* Oxford UP, 1998, capítulos
  6–10. **La referencia del capítulo.**
* **Cowan, G.; Cranmer, K.; Gross, E.; Vitells, O.** *Asymptotic formulae for
  likelihood-based tests of new physics.* Eur. Phys. J. C **71** (2011), 1554.
  Las fórmulas que se usan hoy, incluida la corrección look-elsewhere.
* **Lyons, Louis.** *Discovering the Significance of 5 sigma.*
  arXiv:1310.1284, 2013. Por qué el umbral está donde está.
* **ATLAS Collaboration** y **CMS Collaboration.** Physics Letters B **716**
  (2012), 1–29 y 30–61. Los artículos del Higgs. **Nivel A (primaria).**
* **Strumia, Alessandro.** *Interpreting the 750 GeV digamma excess: a review.*
  arXiv:1605.09401. El episodio de los 750 GeV, contado desde dentro.
* **Sellke, T.; Bayarri, M. J.; Berger, J.** *Calibration of p Values for
  Testing Precise Null Hypotheses.* The American Statistician **55** (2001),
  62–71. La traducción cuantitativa entre p-valores y factores de Bayes.
