# II.3 — ¿Por qué hay campanas por todas partes… y dónde no las hay?

> **El fenómeno:** alturas, errores de medida, notas de examen y ruido térmico
> tienen la misma forma. Los tamaños de ciudades, las magnitudes de terremotos
> y las fortunas, no.
> **Herramientas que convoca:** cap. 3 (TCL), cap. 1 (log-normal), cap. 9.
> **Lo que hay que llevarse:** que la forma límite la decide el mecanismo, y
> que reconocer cuál se aplica cambia todo lo que puedes afirmar después.

---

## 1. Una pregunta

::: pregunta
La persona más alta del mundo mide 2,5 veces la media. El terremoto más grande
registrado liberó $10^{5}$ veces la energía del terremoto medio.

**¿Por qué las alturas tienen un máximo y los terremotos no?**
:::

---

## 2. Antes de calcular

::: antes
1. ¿Cuántas desviaciones típicas por encima de la media está la persona más
   alta del mundo?
2. Si sumas 200 variables independientes, ¿siempre sale una campana?
3. ¿Qué distribución esperas para el tamaño de los ficheros de tu disco duro?
:::

---

## 3. Tres mecanismos, tres formas

![Tres sumas de 200 términos, tres resultados distintos. Izquierda: exponenciales, varianza finita, sale normal. Centro: variables de Lévy con $\alpha=1{,}5$, sin varianza, sale otra Lévy. Derecha: producto de 60 factores, sale log-normal. Lo que hay que concluir: el número de términos no determina la forma; la determina el mecanismo y la existencia de momentos.](figuras/fig_dominios_atraccion.pdf)

**Suma con varianza finita → normal.** Es el teorema central del límite del
capítulo 3. Condición: la varianza existe y ningún término domina.

**Producto → log-normal.** Porque el logaritmo convierte el producto en suma.
Es el mecanismo del capítulo 1.

**Suma con cola pesada → distribución estable de Lévy.** Si las colas van como
$x^{-\alpha-1}$ con $\alpha<2$, la varianza no existe y el TCL no aplica. La
suma converge, pero a otra cosa: una **ley estable**, que conserva las colas
pesadas por muchos términos que sumes.

Y hay un cuarto mecanismo que aparece constantemente:

**Crecimiento proporcional → ley de potencias.** Si algo crece a un ritmo
proporcional a su tamaño y hay entrada continua de elementos nuevos, la
distribución resultante es de potencias. Es el modelo de Yule (1925), el
«ricos más ricos» de Simon (1955) y el enganche preferencial de Barabási y
Albert (1999): el mismo mecanismo redescubierto tres veces en tres campos.

---

## 4. Por qué importa tanto la distinción

Porque **casi todo lo que sabes hacer deja de valer sin varianza finita**:

| Herramienta | Requiere | Qué pasa sin ella |
|---|---|---|
| Barras de error $\sigma/\sqrt n$ | varianza finita | no significan nada |
| Intervalos de confianza normales | TCL | cobertura incorrecta |
| Media muestral | media finita | no converge (capítulo 3) |
| $\chi^2$, mínimos cuadrados | errores gaussianos | dominados por atípicos |
| Monte Carlo con barras | varianza finita | error no baja como $1/\sqrt N$ |

Y el diagnóstico práctico es el del capítulo 3: **dibuja la media acumulada**.
Si da saltos al añadir datos, no promedies.

Un segundo diagnóstico, más informativo: dibuja la **función de supervivencia**
$P(X>x)$ en ejes log-log. Una cola de potencias es una recta; una normal o una
exponencial caen mucho más deprisa que cualquier recta.

::: aviso
**Casi todo lo que parece una ley de potencias no lo es.**

Clauset, Shalizi y Newman (2009) reanalizaron 24 conjuntos de datos publicados
como leyes de potencias. Sólo unos pocos resistían un contraste estadístico
riguroso frente a alternativas como la log-normal. Una recta en un histograma
log-log es una prueba muy débil: la log-normal, con parámetros razonables,
produce rectas convincentes en dos o tres décadas.

El procedimiento correcto —estimación por máxima verosimilitud del exponente y
del punto de corte, más contraste con alternativas— está en su artículo, y hay
código publicado. **Si vas a afirmar que algo es una ley de potencias, úsalo.**
:::

---

## 5. La respuesta a la pregunta del principio

**Las alturas son suma.** Muchos factores genéticos y ambientales, cada uno con
un efecto pequeño, se suman. Varianza finita, campana, y una cola que cae como
$e^{-x^2/2}$. Con $\sigma\approx7$ cm sobre una media de 175, la persona más
alta documentada (2,72 m) está a **14 sigmas**. Que exista alguien a 14 sigmas
en una población de $10^{10}$ personas ya indica que la cola real es algo más
gruesa que la gaussiana —hay condiciones médicas específicas—, pero el orden es
el correcto.

**Los terremotos son un proceso de umbral con crecimiento.** Una ruptura
sísmica se propaga mientras encuentre tensión acumulada suficiente; cada
incremento de tamaño hace más probable el siguiente. Es crecimiento
proporcional, y da la ley de Gutenberg–Richter: $\log N=a-bM$ con
$b\approx1$, es decir, una ley de potencias en la energía con exponente
$\approx2/3$.

**La diferencia física es si el mecanismo suma o multiplica.** Y esa pregunta se
puede hacer antes de mirar ningún dato.

---

## 6. Valores extremos: la pregunta que casi nunca se hace

Para diseñar un dique, un margen de seguridad o un límite de detección, no
interesa la media: interesa **el máximo**.

Y hay un teorema paralelo al TCL, mucho menos conocido. El máximo de $n$
variables independientes, adecuadamente normalizado, converge a una de **tres**
distribuciones (Fisher–Tippett–Gnedenko):

* **Gumbel**, si la cola decae exponencialmente (normal, exponencial);
* **Fréchet**, si la cola es de potencias;
* **Weibull**, si la distribución tiene un extremo acotado.

La consecuencia práctica es fuerte: **la clase de la cola determina cómo crecen
los récords**. Con cola de Gumbel, el máximo crece como $\ln n$: muy despacio,
y los récords son cada vez más difíciles. Con cola de Fréchet, crece como
$n^{1/\alpha}$: los récords siguen batiéndose y el «máximo posible» no existe.

El diseño de infraestructuras críticas —diques, presas, sistemas de
refrigeración nuclear— depende de acertar en esa clasificación. Y el desastre de
las inundaciones de los Países Bajos de 1953, con 1836 muertos, motivó
precisamente el desarrollo de la teoría de valores extremos aplicada al diseño
de diques.

---

## 7. ¿Cuándo falla?

::: falla
**Falla el TCL con colas pesadas**, y falla despacio y sin avisar: con
$\alpha$ cerca de 2, la suma parece normal durante muchísimos términos antes de
delatar sus colas.

**Falla la estimación del exponente con pocos datos.** El exponente de una ley
de potencias se estima con las observaciones de la cola, que son pocas por
construcción. Con 100 puntos totales y 10 en la cola, la incertidumbre del
exponente es enorme.

**Falla el ajuste por mínimos cuadrados en el histograma log-log.** Es lo que
hace casi todo el mundo y está sesgado: el binning distorsiona, los bins de la
cola tienen muy pocas cuentas y el ajuste pesa mal. Hay que usar máxima
verosimilitud.

**Falla suponer que «tiene cola pesada» significa «no hay estructura».** Una
ley de potencias es tan informativa como una gaussiana: dice que hay
crecimiento proporcional. El error es tratarla como una anomalía en lugar de
como un mecanismo.
:::

---

## 8. Historia

::: historia
**Quetelet, y el hombre medio** · *Nivel de verificación: A.*

Adolphe Quetelet observó en 1835 que las alturas de los reclutas del ejército
escocés seguían una campana, e introdujo el concepto de *homme moyen*. Fue la
primera aplicación sistemática de la distribución normal a datos humanos, y
contribuyó decisivamente a que la estadística se aplicara a las ciencias
sociales.

También produjo un siglo de malentendidos: Quetelet interpretaba las
desviaciones respecto de la media como «errores» de la naturaleza respecto de
un ideal, en analogía con los errores de medida astronómicos. Fue Francis
Galton quien invirtió la interpretación —la variación no es error, es el objeto
de estudio— y de ahí salió la biometría.

**Pareto, Zipf, Gutenberg–Richter, Yule** · *Nivel de verificación: A.*

Las leyes de potencias se descubrieron independientemente en al menos cinco
campos: distribución de la renta (Pareto, 1896), frecuencia de palabras (Estoup
1916, Zipf 1935), tamaños de ciudades (Auerbach 1913), magnitudes sísmicas
(Gutenberg y Richter, 1944) y número de especies por género (Willis y Yule,
1922).

Yule fue el primero en dar un **mecanismo** —crecimiento proporcional con
entrada de elementos nuevos— en 1925, y Herbert Simon lo redescubrió y
generalizó en 1955. La red de citas de todo este asunto es un caso de estudio
sobre lo poco que se comunican los campos: Barabási y Albert lo redescubrieron
otra vez en 1999 para redes, y su artículo, excelente, no citaba ni a Yule ni a
Simon porque sencillamente no los conocían.
:::

---

## 9. Experimento computacional

::: experimento
**Clasifica tus propias colas.**

Coge tres conjuntos de datos de tu entorno: tamaños de ficheros de tu disco,
duración de tus reuniones, y cualquier serie de tu trabajo.

Para cada uno: dibuja el histograma, la función de supervivencia en log-log, y
la media acumulada al ir añadiendo datos en orden aleatorio.

*Después,* aplica el procedimiento de Clauset et al.: estima el exponente por
máxima verosimilitud, estima el punto de corte, y contrasta contra log-normal y
exponencial mediante la razón de verosimilitudes.

*Qué esperar:* en la mayoría de los casos, la log-normal ganará o empatará. Y
eso es un resultado, no un fracaso.
:::

---

## 10. Lo esencial

::: esencial
* La forma límite la decide el **mecanismo**: suma → normal, producto →
  log-normal, suma con colas pesadas → Lévy, crecimiento proporcional →
  potencias.
* Sin varianza finita se caen las barras de error, los intervalos, los mínimos
  cuadrados y la convergencia $1/\sqrt N$ del Monte Carlo.
* Diagnóstico: media acumulada (¿da saltos?) y supervivencia en log-log (¿es
  recta?).
* Casi nada de lo que se publica como ley de potencias resiste un contraste
  riguroso frente a la log-normal.
* Para diseñar contra el extremo, la distribución relevante no es la de los
  valores sino la del máximo: Gumbel, Fréchet o Weibull.
* Con cola exponencial los récords crecen como $\ln n$; con cola de potencias,
  como $n^{1/\alpha}$. No hay «máximo posible».
:::

---

## 11. Preguntas abiertas

::: abierto
* ¿Hay un mecanismo común detrás de todas las leyes de potencias observadas, o
  son historias distintas con la misma forma?
* ¿Cómo se decide, con datos reales y finitos, entre log-normal y ley de
  potencias, si ambas ajustan?
* ¿Qué distribución de valores extremos hay que usar para el clima futuro, si
  la distribución de partida está cambiando?
* La «criticalidad autoorganizada» explicaría leyes de potencias sin ajuste de
  parámetros. ¿Cuánta evidencia hay realmente a su favor?
:::

### Referencias

* **Clauset, Aaron; Shalizi, Cosma Rohilla; Newman, M. E. J.** *Power-law
  distributions in empirical data.* SIAM Review **51** (2009), 661–703.
  **Nivel A.** El artículo que hay que leer antes de afirmar nada sobre leyes de
  potencias. Con código.
* **Yule, G. Udny.** *A mathematical theory of evolution.* Phil. Trans. R. Soc.
  B **213** (1925), 21–87. **Nivel A (primaria).** El primer mecanismo.
* **Simon, Herbert A.** *On a class of skew distribution functions.* Biometrika
  **42** (1955), 425–440. **Nivel A (primaria).**
* **Gutenberg, B. y Richter, C.** *Frequency of earthquakes in California.*
  Bull. Seism. Soc. Am. **34** (1944), 185–188. **Nivel A (primaria).**
* **Coles, Stuart.** *An Introduction to Statistical Modeling of Extreme
  Values.* Springer, 2001. La referencia de valores extremos.
* **Mitzenmacher, Michael.** *A brief history of generative models for power law
  and lognormal distributions.* Internet Mathematics **1** (2004), 226–251.
  Panorámica excelente sobre los mecanismos y su historia.
