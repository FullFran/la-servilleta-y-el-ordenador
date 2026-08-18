# Capítulo 3 — Probabilidad como modelo del desconocimiento y del azar

> **Qué sabrás hacer al terminar**
> · Distinguir las dos cosas que llamamos probabilidad y saber cuál usas ·
> Construir el espacio muestral antes de escribir ninguna fórmula ·
> Reconocer una distribución por su **mecanismo generador**, no por su fórmula ·
> Saber exactamente qué promete la ley de los grandes números y qué no ·
> Detectar cuándo el teorema central del límite no se aplica.
>
> **Herramientas que usa:** capítulo 1 (órdenes de magnitud, log-normal).
> **Disciplinas de los ejemplos:** medicina, telecomunicaciones, física,
> ecología, informática, economía.
> **Deuda que paga:** por qué salió una log-normal en el capítulo 1.
> **Deuda que abre:** el proceso de Poisson en serio (capítulo 4); la
> inferencia de parámetros (capítulo 5); el muestreo como método de cálculo
> (capítulo 9).

---

## 1. Una pregunta

::: pregunta
Una prueba diagnóstica detecta al 99 % de los enfermos y da negativo al 99 % de
los sanos. Te la haces en un cribado poblacional y **das positivo**. La
enfermedad afecta a una persona de cada mil.

**¿Qué probabilidad tienes de estar enfermo?**
:::

Casi todo el mundo, incluidos profesionales sanitarios en estudios repetidos
desde los años setenta, contesta «99 %» o algo parecido. La respuesta correcta
es **8 %**, y la distancia entre esas dos cifras no es un fallo de cálculo: es
un fallo de modelado. Se ha confundido $P(+\mid \text{enfermo})$ con
$P(\text{enfermo}\mid +)$, que son cantidades distintas relacionadas por una
identidad que ocupa una línea.

Este capítulo no va de fórmulas de probabilidad. Va de aprender a construir el
modelo probabilístico correcto antes de aplicar ninguna.

---

## 2. Antes de calcular

::: antes
Contesta antes de seguir, sin cuentas:

1. Tu número para la pregunta de arriba.
2. Si la prevalencia fuese del 10 % en vez del 0,1 %, ¿cambiaría mucho?
3. Lanzo una moneda, la tapo con la mano y no la miro. ¿Cuál es la
   probabilidad de que sea cara? ¿Y si yo sí la he mirado?

La tercera parece una tontería y es la pregunta más profunda de las tres.
:::

---

## 3. La intuición

### 3.1 Dos cosas distintas con el mismo nombre

Cuando decimos «la probabilidad de que salga cara es 1/2» y «la probabilidad de
que llueva mañana es del 30 %», estamos usando la misma palabra para dos ideas
que no son la misma.

La primera es **probabilidad aleatoria** (u *óntica*): una propiedad del
proceso. Si repites el lanzamiento un millón de veces, la frecuencia tiende a
1/2. Tiene sentido hablar de repetición.

La segunda es **probabilidad epistémica**: un estado de tu conocimiento. Mañana
sólo hay un mañana; no se puede repetir. El 30 % describe tu ignorancia, no una
propiedad del clima.

La moneda tapada es el caso límite que lo deja claro. Ya ha caído: es cara o es
cruz, con certeza. La probabilidad 1/2 no está en la moneda, está en ti. Y si yo
la he mirado, mi probabilidad es 0 o 1 mientras la tuya sigue siendo 1/2. **Dos
observadores racionales pueden asignar probabilidades distintas al mismo hecho
sin que ninguno se equivoque**, porque la probabilidad no es una propiedad del
hecho.

Esta distinción lleva doscientos años generando peleas —Laplace era claramente
epistémico, Venn y Fisher frecuentistas, Jaynes escribió un libro entero
militando— y este libro no la va a resolver. Lo que sí va a hacer es exigir
que declares cuál estás usando. Casi todos los errores prácticos de
probabilidad vienen de mezclarlas sin darse cuenta.

### 3.2 El espacio muestral es el modelo

Antes de cualquier fórmula hay una decisión de modelado: **qué cuenta como un
resultado posible**. Esa decisión es el espacio muestral $\Omega$, y es donde
está toda la física del problema.

Un ejemplo clásico, y no una anécdota: tienes dos hijos, al menos uno es niña,
¿probabilidad de que los dos sean niñas? La respuesta depende íntegramente de
cómo obtuviste esa información. Si preguntaste «¿tienes al menos una hija?» y
te dijeron que sí, $\Omega=\{NN, NV, VN\}$ y la respuesta es 1/3. Si te
encontraste a una hija por la calle, el espacio es otro y la respuesta es 1/2.
No hay una respuesta correcta a la pregunta mal planteada: **hay que
especificar el mecanismo que generó la información**.

Este es el patrón que se repetirá todo el capítulo. La aritmética es fácil; el
modelo, no.

---

## 4. La matemática

### 4.1 Lo mínimo imprescindible

Un modelo probabilístico son tres cosas: un conjunto $\Omega$ de resultados
posibles, una familia de subconjuntos a los que sabemos asignar probabilidad
(los *sucesos*), y una función $P$ que cumple

$$P(A)\ge0,\qquad P(\Omega)=1,\qquad
P\Big(\bigcup_i A_i\Big)=\sum_i P(A_i)\ \text{si los } A_i \text{ son disjuntos}$$

Eso es todo lo que Kolmogórov necesitó en 1933. Lo llamativo es lo tarde que
llegó: la probabilidad llevaba tres siglos funcionando sin axiomas.

Una **variable aleatoria** no es aleatoria ni es una variable: es una *función*
$X:\Omega\to\mathbb{R}$ que asigna un número a cada resultado. Insisto porque
esa definición aclara muchas confusiones: cuando escribimos $P(X>3)$ estamos
diciendo $P(\{\omega: X(\omega)>3\})$, es decir, la probabilidad del conjunto de
resultados cuya imagen supera 3.

**Esperanza y varianza** son los dos primeros momentos de tu ignorancia:

$$E[X]=\sum_\omega X(\omega)P(\omega),\qquad
\operatorname{Var}(X)=E[(X-E[X])^2]=E[X^2]-E[X]^2$$

Las dos propiedades que se usan constantemente:

$$E[aX+bY]=aE[X]+bE[Y]\quad\text{(siempre)},\qquad
\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)\quad\text{(si son independientes)}$$

La primera vale **siempre**, incluso con dependencia total. La segunda necesita
independencia —en realidad, sólo covarianza nula—. Esa asimetría es la razón de
que el error de la estimación del capítulo 1 creciera como $\sqrt n$.

### 4.2 Independencia: el supuesto que más se viola en silencio

$A$ y $B$ son independientes si $P(A\cap B)=P(A)P(B)$. Escrito así parece
inofensivo. En la práctica es el supuesto que rompe más modelos, porque **se
asume por omisión**: nadie escribe «supongo independencia», simplemente
multiplica.

Tres ejemplos de lo caro que sale:

* En 2007, los modelos de riesgo de hipotecas titulizadas suponían que los
  impagos de distintas regiones eran casi independientes. Cuando dejaron de
  serlo, la probabilidad de pérdidas simultáneas resultó ser órdenes de
  magnitud mayor que la modelada.
* En fiabilidad, dos sistemas redundantes con probabilidad de fallo $10^{-3}$
  cada uno dan $10^{-6}$ si son independientes... y $10^{-3}$ si comparten la
  misma fuente de alimentación.
* En estadística de partículas, dos detectores «independientes» que comparten
  electrónica de lectura no lo son, y la significancia calculada es demasiado
  optimista.

Regla operativa: **cada vez que multipliques probabilidades, escribe en el
margen por qué crees que son independientes.** Si no sabes escribirlo, no lo
son.

### 4.3 Condicionar es actualizar

$$P(A\mid B)=\frac{P(A\cap B)}{P(B)}$$

De ahí, en dos líneas y sin más ingredientes:

$$\boxed{\ P(A\mid B)=\frac{P(B\mid A)\,P(A)}{P(B)}\ }$$

El teorema de Bayes no es una teoría: es una identidad algebraica. Lo
interesante no es la fórmula, es lo que hace: **invierte el sentido del
condicionamiento**. Tú conoces $P(\text{síntoma}\mid\text{causa})$ —eso lo
mide el fabricante del test— y quieres $P(\text{causa}\mid\text{síntoma})$
—eso es lo que le importa al paciente—.

Vamos al problema del principio. Con prevalencia $p=0{,}001$, sensibilidad
$s=0{,}99$ y especificidad $e=0{,}99$:

$$P(\text{enf}\mid+)=\frac{s\,p}{s\,p+(1-e)(1-p)}
=\frac{0{,}99\cdot0{,}001}{0{,}99\cdot0{,}001+0{,}01\cdot0{,}999}
=\frac{0{,}00099}{0{,}01098}\approx 9\,\%$$

Pero la fórmula no convence a nadie. Lo que convence es contar personas.

![El mismo test en tres poblaciones. Cada panel son 10 000 personas. Lo que se ve: cuántos positivos son verdaderos y cuántos falsos. Lo que hay que concluir: la calidad del test no cambia entre paneles; lo que cambia es cuánta gente sana hay disponible para producir falsos positivos.](figuras/fig_bayes_frecuencias.pdf)

La clave está en el tamaño de los dos grupos. Con prevalencia 0,1 % hay 10
enfermos y 9990 sanos. El test acierta con 9,9 de los enfermos y se equivoca
con 99,9 de los sanos. Hay **diez veces más falsos positivos que verdaderos**,
sencillamente porque hay mil veces más sanos.

::: herramientas
**Piensa en frecuencias naturales, no en probabilidades**

Gigerenzer y colaboradores demostraron en los años noventa que reformular un
problema bayesiano en frecuencias («de cada 1000 personas...») multiplica por
tres o cuatro la tasa de respuestas correctas, incluso entre médicos con
experiencia. No es que la gente sea mala con Bayes: es que la notación de
probabilidades condicionadas oculta los tamaños de los grupos.

**Truco práctico:** cuando te den porcentajes condicionados, tradúcelos
inmediatamente a una tabla de 10 000 personas. Casi siempre la respuesta se ve
sin dividir nada.
:::

### 4.4 El zoo mínimo, contado por su mecanismo

Aprenderse fórmulas de distribuciones es inútil. Lo que hay que saber es **qué
proceso las genera**, porque entonces las reconoces en un problema nuevo.

![Seis mecanismos generadores, simulados desde cero. Lo que se ve: histogramas de simulación con la ley teórica encima. Lo que hay que concluir: no hay que memorizar seis fórmulas, hay que reconocer seis situaciones.](figuras/fig_mecanismos.pdf)

| Distribución | El mecanismo | Dónde aparece |
|---|---|---|
| Bernoulli | un intento, dos resultados | cualquier decisión binaria |
| Binomial | contar éxitos en $n$ intentos independientes | control de calidad, encuestas |
| **Poisson** | $n\to\infty$, $p\to0$, con $np$ fijo | desintegraciones, llamadas, mutaciones |
| Geométrica | ¿cuántos intentos hasta el primer éxito? | reintentos de red |
| Exponencial | tiempo hasta el primer suceso, **sin memoria** | vida de un componente, colas |
| Normal | **suma** de muchas contribuciones comparables | errores de medida, alturas |
| Log-normal | **producto** de muchos factores | tamaños de gota, ingresos, ficheros |
| Ley de potencias | crecimiento proporcional, «el que más tiene más recibe» | ciudades, redes, terremotos |
| Uniforme | ignorancia total dentro de un rango | fases, posiciones iniciales |

Fíjate en la pareja normal/log-normal: la diferencia entre ellas no es una
fórmula, es una operación. **Suma → normal. Producto → log-normal.** Eso paga
la deuda del capítulo 1: la energía de la tormenta era un producto de cuatro
factores, así que su logaritmo era una suma, así que su logaritmo era normal.

::: aviso
La exponencial es la única distribución continua **sin memoria**:
$P(T>t+s\mid T>t)=P(T>s)$. Si la vida de un componente es exponencial, un
componente usado durante diez años es exactamente igual de bueno que uno nuevo.

Esto es cierto para la desintegración radiactiva —un núcleo no «envejece»— y es
falso para casi todo lo demás. Modelar la vida de un rodamiento como
exponencial es un error habitual y caro: los rodamientos sí envejecen, y para
eso está la distribución de Weibull.
:::

### 4.5 Ley de los grandes números: qué promete y qué no

Si $X_1,X_2,\dots$ son independientes con media $\mu$ y varianza finita,

$$\bar X_n=\frac1n\sum_{i=1}^n X_i \;\longrightarrow\; \mu$$

**Lo que promete:** la media muestral se acerca a la media verdadera.

**Lo que no promete:** nada sobre la velocidad, y nada en absoluto si la
varianza no existe. La velocidad la da el teorema central del límite:
$\sigma_{\bar X}=\sigma/\sqrt n$. Esa raíz es una mala noticia permanente: para
ganar una cifra decimal hay que multiplicar el esfuerzo por cien. Volveremos a
tropezar con ella en el capítulo 9, donde será la limitación central del método
de Monte Carlo.

![Lo que la ley de los grandes números promete y a qué velocidad. Izquierda: cinco medias acumuladas de muestras uniformes, con la banda $\pm2\sigma/\sqrt n$. Derecha: el TCL actuando sobre tres distribuciones de partida muy distintas, con sólo doce sumandos. Lo que hay que concluir: la campana aparece deprisa cuando la partida es simétrica y despacio cuando es muy asimétrica.](figuras/fig_lgn_tcl.pdf)

### 4.6 Teorema central del límite: por qué es cierto

Sea $S_n=\sum_i X_i$ con $X_i$ independientes, media 0 y varianza $\sigma^2$.
La función característica $\varphi(t)=E[e^{itX}]$ tiene la propiedad de que la
de una suma es el producto de las de los sumandos. Desarrollando,

$$\varphi_X(t)=1-\tfrac{\sigma^2t^2}{2}+o(t^2)
\;\Longrightarrow\;
\varphi_{S_n/\sqrt n}(t)=\Big[\varphi_X\!\big(t/\sqrt n\big)\Big]^n
=\Big[1-\tfrac{\sigma^2t^2}{2n}+o(1/n)\Big]^n
\longrightarrow e^{-\sigma^2t^2/2}$$

que es la función característica de una normal. **Toda la demostración cabe en
tres líneas y descansa en un solo hecho**: que el desarrollo de $\varphi$
empiece por $1-\sigma^2t^2/2$, es decir, que la varianza exista y sea finita.

Ahí está el punto débil. Si la varianza no existe, el argumento se cae entero, y
con él la campana.

### 4.7 Cuando la campana no aparece

La distribución de Cauchy, $f(x)=1/[\pi(1+x^2)]$, tiene colas tan gruesas que
$\int x f(x)\,dx$ no converge: **no tiene media**. No es que la media sea
difícil de estimar; es que no existe.

![La ley de los grandes números funcionando y fallando. Izquierda: seis medias acumuladas de muestras normales, que se asientan. Derecha: seis de Cauchy, que no se asientan nunca. Lo que hay que concluir: promediar más datos no siempre mejora la respuesta, y el gráfico lo delata a simple vista.](figuras/fig_cauchy.pdf)

El panel derecho es el que hay que tener grabado. Con 100 000 muestras de
Cauchy, la media acumulada da saltos igual de grandes que con 100. La razón es
que la mayor de $n$ muestras de Cauchy crece como $n$, así que **cada dato nuevo
puede dominar a todos los anteriores juntos**. Promediar no ayuda.

Esto no es una curiosidad matemática. Aparece en:

* tamaños de ficheros, de ciudades y de empresas (Pareto);
* magnitudes de terremotos (Gutenberg–Richter);
* pérdidas en seguros y en finanzas;
* grados de nodos en redes reales;
* tiempos de respuesta en sistemas distribuidos, donde la latencia media es
  una estadística casi inútil y por eso se reportan percentiles.

La señal de alarma práctica: **si la media muestral cambia mucho al añadir un
solo dato, no promedies, mira la distribución**. El capítulo II.3 dedica medio
capítulo a esto.

### 4.8 Entropía: cuantificar la ignorancia

Si la probabilidad mide desconocimiento, debería poder medirse *cuánto*
desconocimiento hay. Shannon (1948) demostró que, bajo tres condiciones
razonables —continuidad, monotonía en el número de opciones equiprobables y
aditividad al descomponer la elección— la única medida posible es

$$H=-\sum_i p_i\log p_i$$

Con logaritmo en base 2 se mide en bits. Un dado equilibrado tiene
$\log_2 6=2{,}58$ bits de entropía; uno cargado, menos. Una distribución
uniforme es la de máxima entropía sobre un conjunto finito: **la ignorancia
máxima es no tener preferencias**.

Esto tiene una consecuencia práctica que usaremos en el capítulo 10: si sólo
conoces ciertos promedios de un sistema, la distribución menos comprometida
compatible con ellos es la de máxima entropía sujeta a esas restricciones. Con
la media fijada sale la exponencial; con media y varianza, la normal; con la
energía media, la de Boltzmann. Casi todo el zoo del apartado 4.4 reaparece
como respuesta a la pregunta *«¿qué es lo mínimo que puedo suponer?»*.

---

## 5. El ordenador entra en escena

::: antes
Vamos a simular el problema del test. Antes de ejecutar:

* ¿Cuántas de las 10 000 personas simuladas darán positivo?
* De esas, ¿cuántas estarán realmente enfermas?
* Si duplicas la especificidad del error (de 1 % a 0,5 % de falsos positivos),
  ¿se duplica el valor predictivo positivo?
:::

```python
import numpy as np
rng = np.random.default_rng(0)

N, prevalencia, sensibilidad, especificidad = 1_000_000, 0.001, 0.99, 0.99

enfermo = rng.random(N) < prevalencia
positivo = np.where(enfermo,
                    rng.random(N) < sensibilidad,        # verdadero positivo
                    rng.random(N) < 1 - especificidad)   # falso positivo

print(f"positivos: {positivo.sum():,}")
print(f"de ellos enfermos: {(positivo & enfermo).sum():,}")
print(f"P(enfermo | +) = {(positivo & enfermo).sum() / positivo.sum():.1%}")
```

```text
positivos: 10,928
de ellos enfermos: 1,008
P(enfermo | +) = 9.2%
```

El valor exacto por Bayes es 9,0 %. La simulación da 9,2 %, y la diferencia no
es un error: es el ruido de contar sólo mil enfermos. Con $\sqrt{1008}\approx32$,
la incertidumbre relativa del numerador es del 3 %, que sobre 9,0 % son
0,3 puntos. **La discrepancia está exactamente donde debía estar**, y esa
comprobación —¿mi simulación se desvía de la teoría más de lo que su propio
ruido permite?— es la que hay que hacer siempre.

Ocho líneas de simulación convencen más que la fórmula de Bayes, y ese es un
argumento pedagógico serio: **una simulación es una definición operativa de un
modelo probabilístico**. Si no sabes simularlo, probablemente no lo has
especificado del todo.

::: juega
1. Sube la especificidad a 99,9 %. ¿Cuánto sube el valor predictivo? ¿Y si en
   vez de eso subes la sensibilidad a 99,9 %?
2. Pon prevalencia 50 % (población de riesgo, no cribado). ¿Qué pasa?
3. Haz dos tests independientes y condiciona a que ambos den positivo. ¿Es
   legítimo suponerlos independientes si usan la misma técnica?
4. Cambia la exponencial por una Weibull en el ejemplo de fiabilidad del
   apartado 4.4 y mira cómo cambia la probabilidad de fallo en el segundo año.
:::

---

## 6. ¿Qué estamos suponiendo?

::: supuestos
1. **Que la prevalencia que usamos es la de la población a la que perteneces.**
   Si te haces el test por tener síntomas, tu prevalencia previa no es la
   poblacional, y el resultado cambia radicalmente. Es el error más frecuente
   al aplicar este cálculo a un caso real.
2. **Que sensibilidad y especificidad son constantes.** Dependen del umbral, del
   estadio de la enfermedad y del laboratorio.
3. **Que los tests repetidos son independientes.** Casi nunca lo son: dos tests
   de la misma técnica fallan en los mismos pacientes.
4. **Que la varianza existe**, cada vez que usamos $\sigma/\sqrt n$.
5. **Que las muestras son independientes e idénticamente distribuidas.** En
   series temporales, en muestreos espaciales y en datos de encuestas, casi
   nunca.
6. **Que el espacio muestral está bien definido**, es decir, que sabemos qué
   mecanismo generó la información que tenemos.
:::

---

## 7. ¿Cuándo falla?

::: falla
**Falla cuando la probabilidad previa no es la que crees.** Un cribado
poblacional y una consulta por síntomas tienen previas distintas por órdenes de
magnitud. Aplicar la del cribado a un paciente sintomático subestima
gravemente el riesgo, y al revés.

**Falla con dependencia oculta.** Multiplicar probabilidades es cómodo y casi
siempre optimista. El caso de Sally Clark en el Reino Unido (1999) es el
ejemplo canónico y trágico: se presentó como prueba la probabilidad de dos
muertes súbitas en la misma familia calculada como el cuadrado de la
individual, ignorando factores genéticos y ambientales compartidos. La condena
fue anulada en 2003 y la Royal Statistical Society emitió un comunicado formal
criticando el uso de la estadística en el juicio.

**Falla sin varianza finita.** Todo el aparato $\sigma/\sqrt n$ —barras de
error, intervalos de confianza, tamaños muestrales— presupone momentos que a
veces no existen.

**Falla al confundir $P(A\mid B)$ con $P(B\mid A)$.** Tiene nombre propio,
*falacia del fiscal*, y es endémica: un p-valor no es la probabilidad de que la
hipótesis sea falsa, exactamente igual que la sensibilidad de un test no es la
probabilidad de estar enfermo.
:::

### Un anti-ejemplo: el problema de las dos monedas mal contado

«Lanzo dos monedas. Al menos una es cara. ¿Probabilidad de que las dos lo
sean?» Se contesta 1/3 y se queda tan ancho. Pero la respuesta depende del
mecanismo: si yo miro las dos monedas y te informo de que hay al menos una
cara, es 1/3. Si destapo una moneda al azar y resulta ser cara, es 1/2. Mismos
datos, distinta respuesta, porque **el dato no es «hay al menos una cara», el
dato es «he recibido esta información de esta manera»**. Este es exactamente el
problema de Monty Hall con otro traje, y explica por qué genera discusiones tan
encendidas: se discute sobre aritmética cuando el desacuerdo es sobre el
espacio muestral.

---

## 8. Historia

::: historia
**Trescientos años funcionando sin axiomas** · *Nivel de verificación: A.*

La probabilidad nació de un problema de apuestas. En 1654, Blaise Pascal y
Pierre de Fermat intercambiaron cartas sobre el «problema de los puntos»: cómo
repartir el bote de un juego interrumpido. La correspondencia se conserva y es
el acta de nacimiento del cálculo de probabilidades.

Ian Hacking (1975) planteó una pregunta incómoda: ¿por qué tan tarde? Los dados
llevaban milenios existiendo, y los griegos tenían matemáticas de sobra. Su
tesis es que faltaba el concepto: la idea de que el azar es cuantificable, y no
una manifestación de designios inaccesibles, es una invención cultural del
siglo XVII.

**Bayes, y lo que Bayes no escribió** · *Nivel de verificación: A, con matiz.*

El ensayo de Thomas Bayes se publicó en 1763, dos años después de su muerte,
enviado por Richard Price, que añadió una introducción y un apéndice
sustanciales. El «teorema de Bayes» tal como se enseña hoy no aparece en esa
forma en el texto, y la contribución de Price fue mayor de lo que su papel de
mero editor sugiere. Laplace redescubrió y generalizó el resultado de forma
independiente en 1774 y le dio la forma que usamos.

**Kolmogórov y por qué hicieron falta axiomas** · *Nivel de verificación: A.*

Hasta 1933 la probabilidad era una colección de técnicas eficaces sobre
fundamentos discutibles. El problema no era filosófico sino técnico: sin teoría
de la medida no se sabía tratar consistentemente los espacios continuos, y
aparecían paradojas —la de Bertrand es la más famosa— donde «elegir al azar»
daba respuestas distintas según cómo se parametrizara.

Kolmogórov resolvió el asunto poniendo la probabilidad sobre la teoría de la
medida en un librito de 62 páginas. La moraleja para un modelador es directa:
**«al azar» no significa nada hasta que digas respecto a qué medida**. La
paradoja de Bertrand no es una paradoja, es un espacio muestral mal
especificado, que es justo el error del apartado 3.2.

**Y una anécdota que se cuenta como si fuera un hecho** · *Nivel C.*

Se dice que Paul Erdős rechazó la solución correcta del problema de Monty Hall
hasta que le enseñaron una simulación por ordenador. La fuente es la biografía
de Hoffman (1998), basada en recuerdos de terceros. La contamos porque ilustra
algo cierto —que simular convence donde argumentar no— pero no es un documento.
:::

---

## 9. Problemas

En `problemas.md`; soluciones en `soluciones.md`.

---

## 10. Experimento computacional

::: experimento
**Construye tu propio zoo.**

*Pregunta:* ¿puedes generar cada distribución del apartado 4.4 **sin usar** la
función de NumPy que la genera?

*Diseño.* Sólo se permite `rng.random()`, que da uniformes en $[0,1)$. A partir
de ahí:
Bernoulli por comparación; binomial sumando Bernoullis; geométrica contando
hasta el primer éxito; exponencial por transformada inversa
($T=-\ln U/\lambda$); Poisson contando sucesos exponenciales en un intervalo
unidad; normal por Box–Muller; log-normal exponenciando una normal.

*Criterio de parada:* cuando cada histograma se superponga a la teórica.

*Análisis.* Para cada una, compara media y varianza empíricas con las
teóricas, y comprueba que la diferencia baja como $1/\sqrt N$.

*Qué falsaría el resultado:* una discrepancia que **no** baje como $1/\sqrt N$
indica un sesgo en el generador, no ruido. Ese diagnóstico —¿el error baja
como debe?— es el que usaremos en los capítulos 8 y 9 una y otra vez.
:::

---

## 11. Explícalo

::: explica
1. ¿Por qué dos personas racionales pueden asignar probabilidades distintas al
   mismo suceso sin que ninguna se equivoque?
2. Explica sin fórmulas por qué un test excelente puede dar más falsos
   positivos que verdaderos.
3. ¿Qué significa que la exponencial «no tiene memoria», y por qué es falso para
   un rodamiento y cierto para un núcleo radiactivo?
4. ¿Por qué la suma de cosas da campanas y el producto da log-normales?
5. ¿Qué le dirías a alguien que promedia mil medidas y afirma que su resultado
   es mil veces mejor?
6. ¿Por qué existen distribuciones sin media, y cómo lo notarías mirando datos?
:::

---

## 12. Lo esencial

::: esencial
* Hay dos probabilidades con el mismo nombre: la del proceso y la de tu
  conocimiento. Declara siempre cuál usas.
* El espacio muestral es el modelo. Casi todas las paradojas famosas son
  espacios muestrales mal especificados.
* Bayes es una identidad algebraica, no una teoría. Lo que hace es invertir el
  condicionamiento.
* Piensa en frecuencias naturales: traduce todo condicionamiento a una tabla de
  10 000 casos.
* Cada distribución es la huella de un mecanismo. Suma → normal. Producto →
  log-normal. Sucesos raros e independientes → Poisson.
* La independencia se asume por omisión y es el supuesto que más modelos rompe.
  Escribe siempre por qué la crees.
* La ley de los grandes números promete convergencia, no velocidad; el TCL da
  la velocidad, $1/\sqrt n$, y exige varianza finita.
* Sin varianza finita no hay campana, no hay barras de error y promediar no
  ayuda.
:::

---

## 13. Preguntas que quedan abiertas

::: abierto
* Si la probabilidad epistémica describe tu conocimiento, ¿de dónde sale la
  primera previa? ¿Existe una previa «objetiva»?
* ¿Cuántos sumandos hacen falta para que el TCL sea buena aproximación? ¿De qué
  depende exactamente, si la respuesta no es sólo la asimetría?
* Las colas pesadas aparecen por todas partes. ¿Hay algún mecanismo común, o son
  historias distintas que producen la misma forma?
* ¿Es la entropía de Shannon la misma cosa que la de Boltzmann, o sólo tienen la
  misma fórmula? (Volvemos en el capítulo 10.)
* Si simular es una definición operativa de un modelo, ¿qué modelos
  probabilísticos no se pueden simular?
:::
