# Capítulo 1 — Órdenes de magnitud y estimaciones de Fermi

> **Qué sabrás hacer al terminar**
> · Descomponer una pregunta imposible en factores estimables ·
> Trabajar en décadas y saber cuánto error arrastras ·
> Acotar por arriba y por abajo cuando no sabes estimar de frente ·
> Averiguar qué factor domina tu error antes de perder el tiempo afinando otro ·
> Detectar tu propio exceso de confianza contando, no sintiendo.
>
> **Herramientas que usa:** ninguna previa. Este es el punto de partida.
> **Disciplinas de los ejemplos:** meteorología, biología, ingeniería de
> tráfico, informática, astronomía.
> **Deuda que abre:** de dónde sale la ley $R\propto(Et^2/\rho)^{1/5}$ que
> aparece en la historia final (se paga en el capítulo 2); por qué la
> distribución del resultado sale log-normal (se paga en el capítulo 3).

---

## 1. Una pregunta

::: pregunta
Estás en una terraza en agosto. A lo lejos, sobre la sierra, se está montando
una tormenta: una de esas nubes con yunque que en media hora descarga y se
marcha. **¿Cuánta energía libera esa tormenta, y cómo se compara con la bomba
de Hiroshima?**
:::

Es una pregunta rara porque parece imposible y no lo es. No hay ningún dato a
mano. No sabes la masa de la nube, ni su temperatura, ni la termodinámica del
aire húmedo. Y sin embargo, dentro de diez minutos vas a tener una respuesta
que sitúa la energía en la década correcta, sin haber consultado nada. No un
número exacto: la década. Al final del capítulo verás por qué prometer más que
eso sería deshonesto, y por qué la década basta para casi todo.

La habilidad que hace eso posible es la más rentable de todo el libro, y la
razón es incómoda: en la mayoría de los problemas reales, **el paso que decide
si aciertas o fallas no es el cálculo, sino saber qué merece la pena
calcular**. Un modelo detallado de una tormenta con 10⁶ celdas de malla puede
darte un número precioso y equivocado si el planteamiento era malo. Diez
minutos con un lápiz te dicen si ese número es plausible.

---

## 2. Antes de calcular

::: antes
Apunta ahora tres cosas, antes de seguir leyendo:

1. Tu respuesta, en julios, con **una sola cifra significativa**:
   $E \sim 10^{?}$ J.
2. La cota más baja que te parece imposible de bajar.
3. La cota más alta que te parece imposible de superar.

No importa que falles. Importa que el número exista, porque todo lo que
aprenderás en este capítulo se mide como la distancia entre ese número y el
resultado. Si sigues leyendo sin apuntar nada, esto se convierte en
divulgación.
:::

---

## 3. La intuición

### 3.1 Vivimos en un mundo de sesenta décadas y sólo pensamos en tres

La escala de energías del universo abarca unos sesenta órdenes de magnitud,
desde el fotón de una luciérnaga hasta una supernova. Nuestra intuición está
calibrada para tres o cuatro: lo que pesa una bolsa de la compra, lo que tarda
un autobús, lo que cuesta un café. Fuera de esa ventana no tenemos ninguna
sensación fiable, y el cerebro compensa inventando una: por eso «un millón» y
«mil millones» suenan parecido cuando se diferencian en un factor mil.

![Sesenta décadas de energía en un solo eje. Lo que se ve: dónde cae cada cosa. Lo que hay que concluir: una tormenta de verano vive dos décadas por encima de Hiroshima, y catorce por debajo de un segundo de Sol.](figuras/fig_escala_energias.pdf)

El primer gesto del oficio consiste en dejar de pensar en números y empezar a
pensar en **exponentes**. Un orden de magnitud —una *década*— es un factor 10.
Cuando digo que algo vale $10^{15}$ J, no estoy diciendo un número: estoy
señalando un cajón de la estantería. El cajón siguiente contiene cosas diez
veces mayores. Casi todas las preguntas científicas interesantes son preguntas
sobre en qué cajón cae algo, no sobre cuál es su tercera cifra.

::: herramientas
**Logaritmos como cambio de unidad mental**

Trabajar en órdenes de magnitud es trabajar en $\log_{10}$. Las tres
propiedades que se usan todo el rato:

$$\log(ab)=\log a+\log b,\qquad \log(a/b)=\log a-\log b,\qquad \log(a^n)=n\log a$$

La primera es la importante: **el logaritmo convierte productos en sumas**. Y
como una estimación de Fermi es casi siempre un producto de factores, en
escala logarítmica se convierte en una suma de errores independientes. Todo lo
que sabemos sobre sumas de cosas independientes —que es mucho— pasa
inmediatamente a valer aquí.

Vocabulario: una **década** (o *dex*) es un factor 10. Media década es un
factor $10^{0{,}5}\approx 3{,}2$. Un cuarto de década, $\approx 1{,}8$.
Conviene aprenderse estos tres.
:::

### 3.2 Números que hay que tener en la cabeza

No se puede estimar sin un puñado de anclas. Son pocas, y con ellas se llega
sorprendentemente lejos.

::: numeros
| Cantidad | Valor | Cómo recordarlo |
|---|---|---|
| Segundos en un año | $3\times10^7$ | «$\pi\times10^7$», y es exacto al 0,5 % |
| Población mundial | $8\times10^9$ | — |
| Población de España | $4{,}8\times10^7$ | — |
| Radio de la Tierra | $6{,}4\times10^6$ m | 40 000 km de vuelta al mundo |
| $g$ | $10$ m/s² | y el error del 2 % no te matará |
| Densidad del agua | $10^3$ kg/m³ | y la del aire, mil veces menos |
| Calor específico del agua | $4{,}2\times10^3$ J/(kg·K) | y el del aire, $10^3$ |
| Calor latente de vaporización | $2{,}3\times10^6$ J/kg | 600 veces más que subir 1 K |
| Constante solar | $1{,}4\times10^3$ W/m² | 1 kW/m² a nivel del suelo |
| 1 tonelada de TNT | $4{,}2\times10^9$ J | y 1 kt = $4{,}2\times10^{12}$ J |
| Un ser humano en reposo | $\sim100$ W | como una bombilla vieja |
| Número de Avogadro | $6\times10^{23}$ | — |
| 1 eV | $1{,}6\times10^{-19}$ J | — |
| Un año-luz | $10^{16}$ m | — |
:::

Fíjate en la última columna: no son datos memorizados por fuerza bruta, son
datos anclados a algo. «$\pi\times10^7$ segundos en un año» es una
coincidencia numérica que se recuerda sola. «600 veces más que subir un grado»
convierte el calor latente en una comparación en vez de en una cifra suelta, y
eso es lo que hace que sobreviva en la memoria.

### 3.3 La estrategia: convertir una pregunta imposible en cuatro fáciles

Volvamos a la tormenta. No sabemos nada sobre tormentas. Pero sabemos que
llueve, y que la lluvia es agua que antes estaba en fase vapor. Cada kilogramo
de vapor que condensa libera su calor latente. Eso convierte la pregunta
imposible —¿cuánta energía tiene una tormenta?— en una pregunta contable:
**¿cuánta agua cae?**

Y esa se descompone en tres factores que sí sabemos aproximar: el área que
cubre la tormenta, la altura de lluvia que deja y la densidad del agua.

![La anatomía de una estimación. Lo que se ve: cómo una pregunta sin respuesta se convierte en un producto de cuatro cantidades acotables. Lo que hay que concluir: la creatividad de una estimación está en el paso 1, no en el 2.](figuras/fig_anatomia.pdf)

La descomposición es la parte creativa y la única que no se puede automatizar.
Multiplicar sabe multiplicar cualquiera.

---

## 4. La matemática

### 4.1 La estimación

Una célula tormentosa típica cubre del orden de 10 km × 10 km, o sea
$A\sim10^8$ m². Deja, en la media hora que dura, del orden de 20 mm de lluvia:
$h\sim2\times10^{-2}$ m. El agua tiene densidad $\rho=10^3$ kg/m³. Y cada
kilogramo que condensó liberó $L\approx2{,}3\times10^6$ J.

$$E = A\,h\,\rho\,L \approx 10^{8}\cdot 2\times10^{-2}\cdot 10^{3}\cdot 2{,}3\times10^{6}
\approx 5\times10^{15}\ \text{J}$$

Leído en voz alta: *la energía es la que hace falta para evaporar toda el agua
que ha caído*. Comprobación dimensional: m² · m · (kg/m³) · (J/kg) = J. Bien.

Comparemos: Hiroshima liberó unos 15 kt, es decir $6{,}3\times10^{13}$ J. La
tormenta va **unas setenta veces por encima**. Y no es una tormenta
excepcional: es la tormenta de una tarde de agosto.

Este es el momento en el que uno debería desconfiar, así que desconfiemos. El
número es grande, pero la comparación es tramposa, y conviene decir en voz alta
por qué: la energía de la bomba se liberó en microsegundos y en unos cientos de
metros; la de la tormenta, en media hora y en cien kilómetros cuadrados. No es
lo mismo.

La magnitud que decide el daño no es la energía, es la **densidad de potencia**,
$E/(t\,V)$. Y como es una comparación importante, no la afirmemos: hagámosla.

$$\frac{E}{tV}\bigg|_{\text{bomba}}
\sim\frac{6{,}3\times10^{13}}{10^{-6}\cdot\tfrac43\pi(200)^3}
\approx 2\times10^{12}\ \mathrm{W/m^3}$$

$$\frac{E}{tV}\bigg|_{\text{tormenta}}
\sim\frac{4{,}5\times10^{15}}{1800\cdot(10^{8}\cdot10^{4})}
\approx 2{,}5\ \mathrm{W/m^3}$$

Unos **doce órdenes de magnitud**. Y como todo en este capítulo, el número
tiene su intervalo: moviendo la duración de la explosión entre $10^{-7}$ y
$10^{-5}$ s, su radio entre 100 y 300 m, y la altura de la nube entre 1 y
10 km, sale un rango de **10 a 13 décadas**. Doce es el centro, no una cifra
exacta.

Una tormenta no destruye una ciudad por la misma razón que un radiador de 2 kW
tampoco la destruye: lo que hace daño no es la energía, es la prisa con la que
se entrega. Un buen orden de magnitud viene acompañado siempre de la pregunta
*«¿energía de qué, en qué tiempo, en qué volumen?»*.

### 4.2 Por qué esto funciona: la aritmética del error

Aquí está el resultado central del capítulo, y es genuinamente
contraintuitivo. Hemos multiplicado cuatro números inventados. ¿Por qué el
resultado no es basura?

Escribamos la estimación como un producto de $n$ factores:

$$Q=\prod_{i=1}^{n}x_i \qquad\Longrightarrow\qquad
\log Q=\sum_{i=1}^{n}\log x_i$$

Supongamos que cada factor lo conocemos con un error logarítmico de desviación
típica $\sigma_i$ (en décadas), y que **los errores son independientes**. La
varianza de una suma de variables independientes es la suma de las varianzas,
así que

$$\boxed{\ \sigma_{\log Q}=\sqrt{\sum_{i=1}^{n}\sigma_i^{2}}\ }$$

Si todos los factores son igual de malos, $\sigma_i=\sigma$, esto se reduce a

$$\sigma_{\log Q}=\sigma\sqrt{n}$$

Compara las dos posibilidades. Si los errores se acumularan en el peor de los
casos —todos hacia el mismo lado— el error total crecería como $n\sigma$. Como
son independientes, crece como $\sqrt{n}\,\sigma$. Con seis factores, la
diferencia entre $6\sigma$ y $\sqrt6\,\sigma$ es un factor 2,4 en el exponente,
que es un factor 250 en la respuesta.

Póngamosle números. Supón que conoces cada factor «dentro de un factor 3», que
en décadas es $\sigma\approx\log_{10}3\approx0{,}48$. Si tuvieras mala suerte y
los seis errores conspirasen, tu resultado estaría mal por $3^6\approx730$. Con
errores independientes, la desviación típica del resultado es
$0{,}48\sqrt6\approx1{,}2$ décadas: un factor 16. Y eso es una desviación
típica; la mitad de las veces harás bastante mejor.

![Cómo crece el error de una estimación al añadir factores. Izquierda: la simulación (puntos) sigue la curva $\sqrt n\,\sigma$ y no la recta $n\sigma$. Derecha: distribución del error con uno y con seis factores. Lo que hay que concluir: multiplicar seis números mediocres no multiplica la mediocridad; la reparte.](figuras/fig_cancelacion.pdf)

La razón por la que esto funciona no es magia estadística. Es que **al
descomponer, la mayoría de tus errores son honestos**: unas veces te pasas y
otras te quedas corto, sin ninguna razón para que todos se equivoquen en la
misma dirección. La palabra clave de todo el argumento es *independientes*, y
en la sección 8 veremos qué ocurre cuando deja de ser cierta, que es cuando las
estimaciones se van al garete de verdad.

### 4.3 Cuando no sabes estimar: el sándwich

A veces no tienes ni idea de un factor. Entonces no lo estimes: **acótalo**.
Es mucho más fácil decir «esto seguro que está entre A y B» que decir «esto
vale C». Y luego se toma la **media geométrica**:

$$\hat{x}=\sqrt{x_{\min}\,x_{\max}},\qquad
\text{factor de error} = \sqrt{x_{\max}/x_{\min}}$$

La media geométrica y no la aritmética, porque en escala logarítmica la media
geométrica *es* la media aritmética: $\log\sqrt{ab}=\tfrac12(\log a+\log b)$.
Si tus cotas son $10^3$ y $10^7$, la media aritmética te daría $5\times10^6$,
que está pegadísima a la cota superior y no representa tu ignorancia. La
geométrica da $10^5$, justo en el centro de tu ignorancia, que es donde debe
estar.

![Tres niveles de acotación para el mismo problema. Lo que se ve: cómo cada refinamiento del razonamiento estrecha el intervalo. Lo que hay que concluir: acotar con argumentos absurdos pero seguros ya te sitúa a un factor 200; con dos ideas más, a un factor 2.](figuras/fig_sandwich.pdf)

Fíjate en la primera fila de esa figura. «Más de mil coches y menos que la
población de España» es un razonamiento que no requiere saber absolutamente
nada, y ya deja la respuesta dentro de un factor 187. Ese es el suelo de la
técnica: **incluso el razonamiento más tonto que puedas defender acota**.

### 4.4 ¿Dónde está tu error? Sensibilidad de servilleta

Como $\log Q=\sum\log x_i$, todos los factores tienen la misma sensibilidad
logarítmica: $\partial\log Q/\partial\log x_i = 1$. Duplicar cualquiera de
ellos duplica el resultado. Pero eso no significa que todos importen igual,
porque la contribución de cada uno al **error** es

$$\text{contribución}_i = \frac{\sigma_i^2}{\sum_j\sigma_j^2}$$

y las $\sigma_i$ son muy distintas entre sí. En la tormenta conocemos $\rho$ y
$L$ con una precisión ridícula —son constantes tabuladas— y no tenemos ni idea
de $A$ ni de $h$. Toda la incertidumbre está en dos de los cuatro factores.

De aquí sale la regla operativa más útil del capítulo:

> **Afina siempre el factor peor conocido. Todo lo demás es perder el tiempo.**

Parece obvio escrito así, y sin embargo es exactamente lo que no se hace en la
práctica: se refina lo que se sabe refinar, no lo que domina el error. Un
modelo climático con parametrizaciones de nubes de dudosa calidad puede tener
la ecuación de estado del aire implementada a doble precisión. Es un caso
particular de una enfermedad general: **optimizamos donde tenemos herramientas,
no donde está el problema**.

---

## 5. El ordenador entra en escena

Hasta aquí, lápiz. Ahora hagamos algo que a mano no sale: propagar la
incertidumbre completa en lugar de sólo su desviación típica.

::: antes
Predicción antes de ejecutar. Vamos a sortear 200 000 veces los cuatro
factores, cada uno alrededor de su valor central y con la incertidumbre que le
hemos asignado, y a mirar la distribución de $E$. Escribe:

* ¿Qué forma tendrá la distribución de $E$? ¿Y la de $\log E$?
* ¿Será simétrica alrededor de $5\times10^{15}$ J?
* ¿Cuánto valdrá el cociente entre el percentil 95 y el percentil 5?
:::

```python
import numpy as np
rng = np.random.default_rng(1945)

# (valor central, factor de incertidumbre a 1 sigma)
factores = {"A": (1e8, 2.5), "h": (2e-2, 2.0),
            "rho": (1e3, 1.02), "L": (2.26e6, 1.02)}

log_E = np.zeros(200_000)
for centro, factor in factores.values():
    b = np.log10(factor) / np.sqrt(2)        # Laplace: sigma = b*raiz(2)
    log_E += np.log10(centro) + rng.laplace(0.0, b, log_E.size)

E = 10**log_E
p05, p50, p95 = np.percentile(E, [5, 50, 95])
print(f"mediana {p50:.1e} J   P5 {p05:.1e} J   P95 {p95:.1e} J")
print(f"factor P95/P5 = {p95/p05:.0f}   Hiroshimas = {p50/6.3e13:.0f}")
```

Lo que imprime:

```text
mediana 4.5e+15 J   P5 6.9e+14 J   P95 3.0e+16 J
factor P95/P5 = 42   Hiroshimas = 72
exceso de curtosis de log E: +1.540   (0 seria normal exacta)
```

![Propagación completa de la incertidumbre. Izquierda: la distribución es simétrica en $\log E$, no en $E$. Derecha: el 64 % de la varianza viene del área y el 36 % de la lluvia; las dos constantes tabuladas no aportan nada. Lo que hay que concluir: el resultado honesto no es un número, es «entre $7\times10^{14}$ y $3\times10^{16}$ J, con centro en $4{,}5\times10^{15}$».](figuras/fig_tormenta_mc.pdf)

Dos cosas ocurrieron, y conviene detenerse en las dos.

**La distribución es simétrica en el exponente**, con una cola larguísima a la
derecha en el valor. Y aquí hay que tener cuidado con lo que se afirma, porque
es fácil afirmar de más.

La tentación es decir «es el teorema central del límite actuando sobre
$\log E=\sum\log x_i$». Pero mira el tercer panel de la figura. Cada factor se
ha sorteado de una distribución de Laplace —picuda y de colas pesadas— y con
$n=4$ la suma **todavía no es normal**: el exceso de curtosis vale $+1{,}54$,
y una normal lo tiene en cero. Con $n=20$ sí. Cuatro factores no son «muchos».

Esto importa más de lo que parece. Si hubiéramos sorteado cada $\log x_i$ de
una normal, la suma habría salido normal *exactamente*, para cualquier $n$, y
el histograma no habría demostrado nada: la campana estaría metida en los
supuestos, no emergiendo de ellos. **Un experimento que sólo puede confirmar lo
que le has metido no es un experimento.** Es un error frecuente y difícil de
ver, y volveremos a él en el capítulo 16.

Lo que sí es cierto, y se demuestra en el capítulo 3 con sus condiciones: un
producto de muchos factores independientes tiende a log-normal, igual que una
suma de muchos sumandos independientes tiende a normal. Los tamaños de las
gotas de lluvia, los ingresos, los tamaños de los ficheros, la abundancia de
especies. Aquí, con cuatro factores, tenemos una **aproximación decente**, no
un teorema. Quédate con que **la campana de tu ignorancia vive en el
exponente**, y con que «tiende a» no es «es».

**El intervalo del 90 % abarca un factor 42.** Que suena fatal hasta que
recuerdas la alternativa: no tener ni idea. Y hay algo más importante: ese
factor 42 es *honesto*. Es lo que de verdad sabemos. La tentación de escribir
«$E=4{,}5\times10^{15}$ J» y quedarse tan anchos es exactamente el vicio contra
el que el libro entero está escrito.

::: juega
Con el script delante:

1. Cambia la incertidumbre del área de un factor 2,5 a un factor 1,5 (imagina
   que has mirado el radar). ¿Cuánto se estrecha el intervalo? ¿Y si en vez de
   eso afinas $L$ a la cuarta cifra?
2. Pon los cuatro factores con la misma $\sigma$. ¿Reconoces $\sqrt n$ en el
   ancho resultante?
3. Sustituye la normal por una uniforme en el exponente. ¿Cambia mucho la
   distribución final? ¿Por qué te esperabas que no?
4. Añade un quinto factor «fracción del agua que se evapora antes de llegar al
   suelo», entre 0,3 y 1. ¿Sube o baja la estimación? ¿En qué dirección se
   mueve el error?
:::

---

## 6. Calibración: el único entrenamiento que funciona

Estimar bien tiene dos componentes, y sólo se habla de una. La primera es
acertar el número. La segunda, más importante, es **saber cuánto te fías de tu
número**, y ahí casi todo el mundo es sistemáticamente demasiado optimista. La
buena noticia es que el exceso de confianza se mide contando, sin filosofía:
haces veinte estimaciones con su intervalo del 90 %, cuentas cuántas veces el
valor real cae dentro, y si no son unas dieciocho, tus intervalos mienten.

![Detectar el exceso de confianza sin psicología. Izquierda: la curva de calibración de tres personas con el mismo acierto medio y distinta honestidad. Derecha: los intervalos «del 90 %» de quien declara un tercio de su incertidumbre real aciertan menos de la mitad de las veces. Lo que hay que concluir: la anchura del intervalo es una afirmación comprobable, no una impresión.](figuras/fig_calibracion.pdf)

La curva de calibración es diagnóstica: por encima de la diagonal, eres
prudente de más y tus intervalos no informan; por debajo, tus intervalos son
propaganda. Casi todo el mundo empieza muy por debajo. El capítulo 5 volverá a
esto con el vocabulario formal de la incertidumbre, pero la práctica se empieza
hoy y con las manos.

---

## 7. ¿Qué estamos suponiendo?

::: supuestos
1. **Que toda la lluvia viene de vapor que condensó dentro del sistema.**
   Válido para una célula convectiva aislada; falso para un frente que arrastra
   humedad de fuera continuamente, donde la energía total puede ser mucho mayor.
2. **Que el calor latente es la contribución dominante.** La energía cinética
   del viento y la potencial de la masa de aire son órdenes de magnitud
   menores; conviene comprobarlo (problema 1.D2) y no creérselo.
3. **Que los cuatro factores son independientes.** Es discutible: tormentas
   grandes tienden a descargar más, así que $A$ y $h$ correlacionan
   positivamente y el intervalo real es **más ancho** que el que hemos
   calculado.
4. **Que una incertidumbre «de factor 2,5» significa una $\sigma$ logarítmica
   de $\log_{10}2{,}5$.** Es una convención nuestra, y hay que declararla:
   cambia el resultado del intervalo, no el del centro.
5. **Que la distribución de cada factor es log-normal.** Cómoda y no
   demostrada. Con cuatro factores importa poco (lo comprobaste en el punto 3
   de *Juega con el modelo*); con uno solo, importaría mucho.
6. **Que la comparación con Hiroshima es informativa.** Sólo lo es para la
   energía total. Para cualquier otra pregunta —daño, alcance, duración— es
   engañosa, como discutimos en 4.1.
:::

---

## 8. ¿Cuándo falla?

::: falla
La aritmética de la sección 4.2 tiene una hipótesis y tres enemigos.

**Enemigo 1: los errores correlacionados.** Si el mismo dato equivocado entra
dos veces, su error no se cancela: se eleva al cuadrado. Estimar el consumo
eléctrico de un país como (hogares) × (consumo por hogar) usando en ambos una
misma cifra de población mal recordada es el ejemplo clásico. Regla práctica:
**cuenta cuántas veces aparece cada dato primitivo en tu descomposición**; si
alguno aparece dos veces, replantea.

**Enemigo 2: las diferencias de números grandes.** Toda la teoría vale para
productos. En cuanto haces $Q=A-B$ con $A\approx B$, el error relativo explota:
si $A$ y $B$ se conocen al 10 % y difieren en un 5 %, el resultado no se conoce
ni en orden de magnitud. Estimar el saldo migratorio como (entradas) −
(salidas) es un desastre garantizado. Cuando veas una resta de cantidades
parecidas, busca otra descomposición.

**Enemigo 3: las colas pesadas.** $\sqrt n$ sale de que las varianzas se suman,
y eso exige que las varianzas existan. Si un factor tiene una distribución muy
sesgada —el tamaño de una ciudad, la riqueza de una persona, el número de
seguidores de una cuenta— la media no representa nada y la estimación puede
fallar por órdenes de magnitud sin previo aviso. Volveremos a esto en 3.12 y en
el capítulo II.3.

**Y el fallo más frecuente de todos, que no es estadístico:** haber olvidado un
factor entero. Ninguna aritmética de errores te protege de un término ausente.
Por eso el paso 3 del diagrama de la sección 3.3 —«¿dónde está mi error?»—
incluye siempre la pregunta *¿qué me he dejado?*, y por eso conviene estimar la
misma cantidad **por dos caminos distintos** siempre que se pueda.
:::

### Un anti-ejemplo: cuando el orden de magnitud engaña

Estimemos cuánta energía ahorra apagar el móvil por la noche. Cargador: 5 W.
Ocho horas: $5\times8\times3600\approx1{,}4\times10^5$ J. Sale un número
correcto y una conclusión falsa, porque la pregunta interesante no era esa. Un
móvil consume del orden de $10^4$ J al día; una ducha caliente,
$4{,}2\times10^3\cdot 50\cdot 30\approx6\times10^6$ J, unas cuatrocientas veces
más. La estimación era impecable y la decisión que sugiere —preocuparse por el
cargador— es un error de escala.

Este fallo tiene nombre propio y aparecerá muchas veces: **estimar bien la
cantidad equivocada**. Es el modo de fallo dominante en la vida profesional, y
ninguna técnica de cálculo lo cura. Sólo lo cura preguntarse, antes de empezar,
*¿comparado con qué?*.

---

## 9. Historia

::: historia
**Fermi, Trinity y unos trozos de papel** · *Nivel de verificación: A (fuente
primaria).*

El 16 de julio de 1945, a unos 16 km del punto cero, en Jornada del Muerto,
Enrico Fermi esperaba tumbado la detonación del primer artefacto nuclear. En
su informe de aquellos días escribió (traducción del original, conservado en
los archivos de Los Álamos):

> «Unos 40 segundos después de la explosión me alcanzó la onda de choque.
> Intenté estimar su intensidad dejando caer desde una altura de unos seis pies
> pequeños trozos de papel antes, durante y después del paso de la onda. Como
> en aquel momento no había viento, pude observar con claridad y medir de hecho
> el desplazamiento de los trozos de papel que estaban cayendo mientras pasaba
> la onda. El desplazamiento fue de unos dos metros y medio, que en ese momento
> estimé que correspondía a la onda que produciría una explosión de diez mil
> toneladas de TNT.»

El rendimiento aceptado hoy para Trinity ronda los 21 kt. Fermi falló por un
factor 2.

Es tentador contar esto como una hazaña de cálculo mental, y es justo lo
contrario de lo interesante. Lo interesante es la **estructura de la decisión**:
Fermi sabía que en las horas siguientes habría una cifra oficial obtenida con
instrumentación cara, y aun así hizo su medida. Porque una estimación
independiente, hecha con papel y con física de primeros principios, es lo único
que permite detectar que la medida cara está mal. Un número sin un número
independiente al lado es un acto de fe.

Conviene añadir dos matices que el mito suele borrar. El primero: Fermi no era
el único midiendo; había docenas de instrumentos, y su estimación fue una entre
varias. El segundo: **el cálculo detallado que hizo Fermi no se conserva**. Lo
que circula en los libros son reconstrucciones plausibles a partir de las
relaciones de onda de choque, no su razonamiento. El problema 1.X1 te propone
reconstruirlo, que es mucho más instructivo que leerlo.

**El problema de los afinadores de pianos** · *Nivel de verificación: C
(folclore).*

El ejercicio que todo el mundo asocia a Fermi —«¿cuántos afinadores de pianos
hay en Chicago?»— **no aparece en ninguna fuente primaria de Fermi**. Está
documentado que planteaba problemas de estimación a sus estudiantes y que
valoraba enormemente esa capacidad; el enunciado concreto es una atribución
posterior, repetida hasta convertirse en dato. Lo contamos porque el ejercicio
es bueno, no porque sea histórico, y la diferencia entre esas dos cosas es
precisamente lo que este libro intenta enseñar.

**«¿Dónde está todo el mundo?»** · *Nivel de verificación: B (reconstrucción
documentada).*

La famosa pregunta de Fermi sobre las civilizaciones extraterrestres, planteada
durante una comida en Los Álamos en 1950, se conoce a través de una
reconstrucción de 1985 que Eric Jones elaboró pidiendo por carta sus recuerdos
a Emil Konopinski, Edward Teller y Herbert York. Los tres coincidían en el
episodio y discrepaban en los detalles. La frase exacta que se cita en todas
partes es, literalmente, el mejor recuerdo de tres personas treinta y cinco años
después. Lo que sí es sólido y sí es útil es el método: Fermi estimó en voz alta
una cadena de factores —estrellas, planetas, vida, inteligencia, tecnología,
tiempo— y concluyó que la ausencia de visitas era el dato raro. Once años
después, Frank Drake escribiría esa misma cadena como ecuación.
:::

---

## 10. Problemas

Los enunciados están en `problemas.md` y las soluciones razonadas, con pistas
graduadas para los problemas ● y ★, en `soluciones.md`.

---

## 11. Experimento computacional

::: experimento
**Calíbrate.**

*Pregunta:* ¿son honestos tus intervalos?

*Diseño.* Elige veinte cantidades que puedas comprobar después: la altura del
edificio más alto de tu ciudad, el número de farmacias de España, la masa de un
avión comercial vacío, el consumo eléctrico de un centro de datos mediano, el
número de células de tu cuerpo, los litros de café que se beben al día en tu
país. Para cada una, **antes de buscar nada**, apunta tu mediana y tu intervalo
del 90 %.

*Criterio de parada.* Veinte cantidades, y ni una más antes de comprobar.

*Análisis.* Cuenta los aciertos. Con intervalos honestos deberían caer dentro
unos 18 de 20. Dibuja tu curva de calibración con el código de
`codigo/fig_calibracion.py` sustituyendo la simulación por tus datos.

*Qué falsaría la hipótesis «estoy calibrado».* Menos de 14 aciertos de 20. Con
20 pruebas y una tasa real del 90 %, la probabilidad de bajar de 14 por azar es
inferior al 1 %: si te pasa, no es mala suerte.

*Después.* Repite el ejercicio dentro de un mes. La corrección típica consiste
en ensanchar los intervalos por un factor 3, y duele.
:::

---

## 12. Explícalo

::: explica
Sin ecuaciones, en voz alta, a alguien que sabe cálculo y nunca ha visto esto:

1. ¿Por qué multiplicar seis números mal estimados puede dar un resultado
   bueno, y qué haría falta para que no lo diera?
2. ¿Qué significa físicamente que la distribución del resultado sea simétrica
   en el logaritmo pero no en el valor?
3. ¿Por qué la media geométrica y no la aritmética, cuando lo único que tienes
   son dos cotas?
4. Si pudieras afinar un solo factor de tu estimación, ¿cómo decides cuál, y
   por qué no es «el que más influye en el resultado»?
5. ¿Qué le dirías a alguien que responde «no se puede saber sin datos»?
6. ¿En qué se diferencia una estimación buena de una adivinanza afortunada, si
   ambas dan el mismo número?
:::

---

## 13. Lo esencial

::: esencial
* Un orden de magnitud es un cajón, no un número. Pensar en décadas es cambiar
  de unidad mental, y casi todas las preguntas interesantes son preguntas sobre
  el cajón.
* Estimar es **descomponer en un producto**. Lo creativo es la descomposición;
  multiplicar sabe multiplicar cualquiera.
* Los errores independientes se acumulan como $\sqrt n$, no como $n$: seis
  factores conocidos a un factor 3 dan un resultado conocido a un factor 16.
* Cuando no sepas estimar, **acota** y toma la media geométrica. Incluso una
  cota tonta acota.
* La contribución de cada factor al error va como $\sigma_i^2$. Afina siempre el
  peor conocido; refinar lo que ya sabías es trabajo que se siente productivo y
  no lo es.
* Una estimación honesta es un intervalo, y la anchura de ese intervalo es una
  afirmación comprobable: cuéntala.
* La aritmética del error no protege de tres cosas: errores correlacionados,
  diferencias de números grandes y factores olvidados. Estima por dos caminos.
* El modo de fallo dominante no es estimar mal: es **estimar bien la cantidad
  equivocada**. Antes de empezar, pregúntate «¿comparado con qué?».
:::

---

## 14. Preguntas que quedan abiertas

::: abierto
* Hemos supuesto que sabemos qué incertidumbre asignar a cada factor. ¿De dónde
  sale esa asignación? ¿Puede uno estimar su propia ignorancia sin caer en un
  regreso infinito?
* La onda de choque de Fermi: ¿cómo se pasa de un desplazamiento de 2,5 m de un
  papel a una energía en kilotones? (Capítulo 2.)
* ¿Por qué exactamente aparece la log-normal? ¿Con cuántos factores empieza a
  ser buena la aproximación, y qué la estropea? (Capítulo 3.)
* Si el error de una estimación baja como $\sqrt n$ al descomponer más, ¿por qué
  no descomponer indefinidamente? ¿Qué se paga al añadir factores?
* ¿Existen preguntas cuantitativas genuinamente no estimables, o sólo preguntas
  que todavía no hemos sabido descomponer?
:::
