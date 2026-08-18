# Capítulo 15 — Cuando el modelo miente

> **Qué sabrás hacer al terminar**
> · Detectar sobreajuste sin conocer la verdad ·
> Saber qué parte de una extrapolación viene de los datos y cuál de tus
> supuestos · Distinguir sensibilidad local de global, y por qué importa ·
> Reconocer un parámetro que no existe · Diseñar la prueba que mataría tu
> propio modelo.
>
> **Herramientas que usa:** capítulos 5, 8, 10 y 14.
> **Disciplinas de los ejemplos:** epidemiología, física de partículas,
> geología, medicina, economía, ingeniería.
> **Deuda que paga:** las advertencias sueltas de todos los capítulos
> anteriores, reunidas y sistematizadas.

---

## 1. Una pregunta

::: pregunta
Tu modelo ajusta los datos con un $R^2$ de 0,998. Reproduce todas las
observaciones disponibles. Tus colegas están impresionados.

**¿Cómo sabes si es correcto?**
:::

La respuesta honesta —«con esa información, no puedes saberlo»— es el contenido
de este capítulo. Todos los anteriores han enseñado a construir. Este enseña a
desconfiar, y es el más importante de los dieciséis.

La razón es asimétrica y desagradable: **construir mal un modelo produce
resultados que parecen buenos**. Un modelo incorrecto no da error, no lanza
excepciones, no avisa. Da números plausibles con barras de error pequeñas, y
sólo el mundo real —a veces años después— desmiente.

---

## 2. Antes de calcular

::: antes
1. Ajustas 14 datos con un polinomio de grado 12. El error sobre esos 14 datos
   es 0,03. ¿Qué error esperas sobre datos nuevos?
2. Cuatro modelos ajustan igual de bien los mismos datos. ¿Cuál usas para
   extrapolar?
3. Mueves un parámetro un 1 % y la salida no cambia. ¿Puedes concluir que ese
   parámetro no importa?
:::

---

## 3. La intuición

### 3.1 Los seis modos de mentir

Un modelo puede estar mal de seis maneras cualitativamente distintas, y cada
una tiene su diagnóstico propio:

| Modo | Síntoma | Diagnóstico |
|---|---|---|
| **Sobreajuste** | ajusta perfecto, predice fatal | validación con datos nuevos |
| **No identificabilidad** | resultados que dependen del arranque | perfiles de verosimilitud |
| **Mala especificación** | ajusta bien y el mecanismo es falso | residuos, predicciones cualitativas |
| **Extrapolación** | correcto dentro, absurdo fuera | comparar varios modelos fuera |
| **Confusión causal** | correlación fuerte, intervención nula | diagrama causal, experimento |
| **Artefacto numérico** | «física» que depende del paso | convergencia, invariancias |

Los seis producen resultados convincentes. Ninguno se detecta mirando el
ajuste.

---

## 4. La matemática

### 4.1 Sobreajuste: el modelo que aprende el ruido

![Sobreajuste. Izquierda: tres polinomios ajustados a 14 datos; el de grado 12 pasa exactamente por todos. Derecha: el error sobre los datos usados baja siempre; el error sobre datos nuevos tiene un mínimo. Lo que hay que concluir: el error de entrenamiento no es un indicador de calidad, es un indicador de flexibilidad.](figuras/fig_sobreajuste.pdf)

Los números:

| Grado | Error sobre los 14 datos | Error sobre datos nuevos |
|---|---|---|
| 1 | 0,712 | 0,781 |
| **4** | 0,236 | **0,286** |
| 12 | **0,033** | **785,9** |

El grado 12 es 20 veces mejor en entrenamiento y **2700 veces peor** en
predicción. Y nada en el ajuste lo delata: pasa por todos los puntos.

El diagnóstico es conceptualmente trivial y operativamente incómodo:
**reserva datos que no uses para ajustar**. Con muchos datos, un conjunto de
validación. Con pocos, validación cruzada dejando uno fuera. Con series
temporales, validación hacia adelante —nunca aleatoria, porque el futuro no
puede informar al pasado—.

Los criterios de información (AIC, BIC) son una alternativa cuando no puedes
permitirte reservar datos. Penalizan el número de parámetros:

$$\text{AIC}=2k-2\ln\hat{\mathcal{L}},\qquad
\text{BIC}=k\ln n-2\ln\hat{\mathcal{L}}$$

BIC penaliza más y tiende a elegir modelos más pequeños. **Ninguno de los dos
sustituye a la validación**, y ambos suponen que el modelo verdadero está entre
los candidatos, cosa que casi nunca es cierta.

::: aviso
**El sobreajuste no es sólo cosa del aprendizaje automático.**

Ocurre exactamente igual con: un modelo físico al que se le añaden términos
correctivos hasta que ajusta; un ajuste de fondo con un polinomio de grado alto
en un espectro; un modelo climático con parametrizaciones calibradas al mismo
periodo con el que se valida; una estrategia de inversión ajustada a datos
históricos.

En todos, el mecanismo es idéntico: **más libertad que información**.
:::

### 4.2 Extrapolación: dónde acaba el dato y empieza tu fe

![Cuatro modelos ajustados a la misma fase inicial. Izquierda: dentro del rango medido, tres de ellos se distinguen a duras penas —la ley de potencias sí falla, y se ve—. Derecha: extrapolados al cuádruple del rango, los tres buenos difieren en cuatro órdenes y medio de magnitud. Lo que hay que concluir: la extrapolación no la determinan los datos, la determina el modelo que elegiste.](figuras/fig_extrapolacion.pdf)

Con datos hasta $t=10$, los rms del ajuste son 0,22 (exponencial), 0,16
(logística) y 0,09 (polinomio): comparables. La ley de potencias, con 1,19, sí
se puede rechazar. Pero en $t=40$ las predicciones son
$4{,}3\times10^{7}$, $1{,}6\times10^{3}$ y $5{,}6\times10^{4}$.

**Cuatro órdenes y medio de magnitud, con los mismos datos y ajustes igual de
buenos.** Y fíjate en lo que eso significa para el caso más incómodo: rechazar
el peor de los cuatro modelos no te ha servido de nada, porque los tres que
sobreviven siguen sin ponerse de acuerdo.

De aquí sale la regla que hay que aplicar sin excepciones:

> Toda extrapolación es una afirmación sobre **física**, no sobre datos. Si no
> puedes justificar el mecanismo fuera del rango medido, no puedes
> extrapolar; y si lo justificas, la incertidumbre relevante es la de ese
> mecanismo, no la de los parámetros del ajuste.

Y el corolario práctico: **cuando tengas que extrapolar, hazlo con varios
modelos plausibles y reporta el rango completo**. Esa banda es la incertidumbre
honesta, y es siempre mucho mayor que la de la matriz de covarianza.

### 4.3 Sensibilidad local frente a global

![Sensibilidad. Izquierda: variando cada parámetro por separado desde el punto nominal, la salida no depende de $b$: su derivada es cero. Derecha: el análisis global sobre todo el espacio dice que $b$ explica el 24 % de la varianza. Lo que hay que concluir: mover un parámetro cada vez sólo es válido si el modelo es aproximadamente lineal.](figuras/fig_sensibilidad.pdf)

El análisis local —derivadas parciales en el punto nominal, «un factor cada
vez»— es lo que se hace casi siempre, y es correcto **sólo si el modelo es
aproximadamente lineal en el rango de incertidumbre de los parámetros**. En
cuanto hay interacciones, engaña.

El análisis global (índices de Sobol) descompone la varianza de la salida:

$$\operatorname{Var}(Y)=\sum_i V_i+\sum_{i<j}V_{ij}+\dots,\qquad
S_i=\frac{V_i}{\operatorname{Var}(Y)}$$

$S_i$ es la fracción de varianza que se eliminaría si conocieras exactamente el
parámetro $i$. En el ejemplo, $S_a=0{,}70$, $S_b=0{,}24$ y un 6 % de
interacción, mientras que la derivada local de $b$ es **exactamente cero**.

Coste: el análisis global necesita miles de evaluaciones del modelo. Con
modelos caros, se hace sobre un sustituto (*surrogate*). Pero hacerlo mal —o no
hacerlo— produce afirmaciones como «el parámetro $b$ no influye» que son
sencillamente falsas.

### 4.4 Correlación, causalidad y las dos trampas

Todo el mundo sabe que correlación no implica causalidad. Mucha menos gente
sabe **qué hacer con eso**, y hay dos estructuras que conviene distinguir
porque exigen acciones opuestas:

**Confusor.** $Z$ causa $X$ y también $Y$. Entonces $X$ e $Y$ correlacionan sin
que uno cause al otro. Ejemplo: helados y ahogamientos, con el calor como
confusor. **Hay que controlar por $Z$.**

**Colisionador.** $X$ e $Y$ causan ambos a $Z$. Si condicionas por $Z$,
**aparece** una correlación espuria entre $X$ e $Y$ que no existía. Ejemplo:
entre los admitidos en una universidad selectiva, la nota y la habilidad
deportiva correlacionan negativamente, porque hace falta destacar en algo.
**Controlar por $Z$ es exactamente lo que NO hay que hacer.**

La lección incómoda: **«controlar por todo lo que tengas» es una receta
incorrecta**. Controlar por un colisionador introduce sesgo donde no lo había.
Sin un diagrama causal explícito, no se sabe cuál es cuál, y ningún método
estadístico lo decide por ti.

**Y la paradoja de Simpson** es la manifestación agregada: una asociación puede
invertir su signo al agregar subgrupos. El caso documentado más famoso es el de
las admisiones de posgrado en Berkeley en 1973 (Bickel, Hammel y O'Connell,
*Science* 1975): globalmente parecía haber sesgo contra las mujeres, y
departamento por departamento no lo había o iba en sentido contrario. La
explicación era que las mujeres solicitaban en mayor proporción a departamentos
con tasas de admisión más bajas.

### 4.5 Artefactos numéricos disfrazados de física

Del capítulo 8, ahora como diagnóstico sistemático. Antes de creerte un
resultado numérico interesante:

1. **Reduce el paso a la mitad.** ¿El efecto se mantiene?
2. **Cambia de método.** ¿Sobrevive con un integrador distinto?
3. **Comprueba las conservaciones.** ¿Se conserva lo que debería?
4. **Comprueba las invariancias.** Cambia las unidades, gira los ejes, permuta
   el orden de las partículas: la física no debe cambiar.
5. **Cambia la semilla.** Si es estocástico, ¿es un efecto o una realización?
6. **Ejecuta el caso trivial.** ¿Reproduce el resultado analítico conocido?

Cuestan minutos y detectan la mayoría de los descubrimientos falsos. La
resistencia a hacerlos es psicológica, no técnica: **nadie quiere someter a
prueba un resultado bonito**, y ese es exactamente el sesgo que hay que
combatir.

---

## 5. Casos históricos

::: historia
**Millikan, y la deriva de la carga del electrón** ·
*Nivel de verificación: A.*

Feynman lo contó en 1974 y sigue siendo el mejor ejemplo. Millikan midió la
carga del electrón con un valor algo bajo porque usó un valor incorrecto de la
viscosidad del aire. Los experimentos posteriores no saltaron al valor
correcto: **subieron poco a poco durante años**.

El mecanismo, como vimos en el capítulo 5, es un procedimiento asimétrico:
cuando un resultado se aleja del aceptado se busca el error hasta encontrarlo;
cuando coincide, no se busca. Nadie miente, y el resultado colectivo está
sesgado.

El remedio moderno es el **análisis ciego**: se aplica un desplazamiento
desconocido a los datos, se congelan todos los cortes y correcciones, y sólo
entonces se revela. Es hoy estándar en física de partículas y se está
extendiendo a otros campos.

**Los rayos N** · *Nivel de verificación: A.*

En 1903, René Blondlot anunció el descubrimiento de una nueva radiación. En
poco tiempo se publicaron unos 300 artículos de una treintena de autores,
principalmente franceses, describiendo sus propiedades.

En 1904, Robert W. Wood visitó el laboratorio. Durante una demostración en la
oscuridad, retiró disimuladamente el prisma de aluminio esencial del aparato.
El experimentador siguió describiendo las líneas espectrales que veía. Wood
publicó una nota de una página en *Nature*.

Lo interesante no es la anécdota, es el mecanismo: la observación era visual, en
la oscuridad, en el límite de la percepción, y el observador sabía qué esperaba
ver. **Todo experimento en el que el observador conoce el resultado esperado y
la señal está en el límite de la detección es vulnerable**, y eso incluye
muchísimos experimentos modernos con análisis complejos.

**Kelvin y la edad de la Tierra** · *Nivel de verificación: A.*

Entre 1862 y 1897, William Thomson calculó la edad de la Tierra a partir de su
enfriamiento y obtuvo entre 20 y 100 millones de años, en contra de lo que
geólogos y biólogos evolutivos necesitaban.

Su cálculo era **correcto**. Las matemáticas eran impecables, la física de la
conducción era la buena, los datos de conductividad eran razonables. Lo que
faltaba era una fuente de calor que nadie conocía —la radiactividad, descubierta
en 1896— y la convección del manto.

Es el caso más limpio de un modelo bien resuelto y mal especificado. Y contiene
una advertencia que Kelvin no podía ver y nosotros sí: **la incertidumbre
dominante no estaba en sus parámetros, estaba en su lista de mecanismos**, y
ninguna barra de error puede cubrir un mecanismo desconocido.

**OPERA y el cable suelto** · *Nivel de verificación: A.*

En septiembre de 2011, la colaboración OPERA anunció que los neutrinos
llegaban a Gran Sasso 60 ns antes que la luz, con una significancia de 6
sigmas. Fue portada mundial.

Lo que se cuenta menos es lo bien que se comportó la colaboración: publicaron
el resultado **como una anomalía sin explicación**, pidiendo verificación
independiente, y no como un descubrimiento. En febrero de 2012 identificaron
dos problemas: un conector de fibra óptica mal apretado y un oscilador con
deriva. Corregidos, los neutrinos viajaban a la velocidad de la luz.

La lección práctica es la del apartado 4.5 llevada al extremo: **seis sigmas
estadísticas no protegen de un error sistemático**, porque la barra de error
sólo cubre lo que has modelado. Un cable flojo no está en ninguna matriz de
covarianza.
:::

---

## 6. ¿Qué estamos suponiendo? (al desconfiar)

::: supuestos
1. **Que los datos de validación son realmente independientes.** Si vienen del
   mismo experimento, el mismo día, con el mismo instrumento, comparten
   sistemáticos y la validación es optimista.
2. **Que el modelo verdadero está entre los candidatos.** AIC y BIC lo suponen,
   y casi nunca es cierto.
3. **Que podemos muestrear el espacio de parámetros** para hacer sensibilidad
   global. Con modelos caros, no.
4. **Que conocemos las relaciones causales** lo bastante para dibujar el
   diagrama. Si no, no se sabe por qué controlar.
5. **Que las comprobaciones numéricas son independientes del error.** Si el
   error está en la formulación, todas las mallas convergen a lo mismo
   incorrecto.
:::

---

## 7. ¿Cuándo falla la desconfianza misma?

::: falla
**Falla el escepticismo indiscriminado.** Si toda incertidumbre se infla «por
prudencia», el modelo deja de informar y no se puede decidir nada. El objetivo
no es no equivocarse: es **saber cuánto puedes equivocarte**.

**Falla la validación con datos contaminados.** Si has mirado los datos de
validación aunque sea una vez para decidir algo, ya no son de validación. El
sesgo por selección de modelo es real y sutil.

**Falla el análisis de sensibilidad sobre el modelo equivocado.** Puedes hacer
un Sobol perfecto sobre un modelo con la física mal, y obtendrás índices
precisos y una conclusión falsa.

**Y falla, sobre todo, la incertidumbre estructural.** Todo lo de este capítulo
cuantifica la incertidumbre **dentro** de un modelo. La mayor de todas casi
siempre es la de haber elegido ese modelo, y no hay técnica que la cubra. Lo
único que ayuda es **usar varios modelos con estructuras distintas y comparar**,
y aun así el conjunto de modelos que se te han ocurrido no es el conjunto de
modelos posibles.
:::

### Un anti-ejemplo: la validación que estaba envenenada

Un equipo entrena un modelo predictivo con datos de pacientes de un hospital,
lo valida en un conjunto reservado y obtiene un AUC de 0,94. Excelente. En
producción, en otro hospital, cae a 0,71.

La causa habitual, documentada muchas veces: el modelo había aprendido algo del
**proceso**, no de la enfermedad. Por ejemplo, que las radiografías tomadas con
el equipo portátil —usado para pacientes que no pueden bajar— tienen un
marcador visible, y esos pacientes están más graves. El modelo detecta el tipo
de equipo, no la patología.

Es *fuga de información* (*leakage*), y no lo detecta ninguna validación
interna, porque la fuga está en los dos conjuntos. Sólo lo detecta **validación
externa**, en otro sitio, con otro proceso. Que es cara y por eso casi nunca se
hace.

---

## 8. Cómo diseñar la prueba que mataría tu modelo

Este es el apartado operativo del capítulo.

1. **Escribe la predicción más arriesgada que hace tu modelo.** No la que sabes
   que cumple: la que te sorprendería si se cumpliera.
2. **Comprueba que es falsable.** ¿Existe un resultado observable que la
   contradiga? Si no, no es una predicción.
3. **Estima cuántos datos harían falta** para distinguirla de la alternativa
   (capítulo 4: significancia y $\sqrt N$).
4. **Preregistra el criterio.** Escribe *antes* qué resultado te haría abandonar
   el modelo. Sin eso, siempre habrá una explicación *a posteriori*.
5. **Hazla.**
6. **Publica el resultado sea cual sea.**

El paso 4 es el que más duele y el que más vale. Un modelo del que no sabes
decir qué lo mataría no es un modelo científico: es una descripción flexible.

---

## 9. Problemas

En `problemas.md`; soluciones en `soluciones.md`.

---

## 10. Experimento computacional

::: experimento
**Envenena tu propio análisis, a propósito.**

*Pregunta:* ¿detectarías una fuga de información si la tuvieras?

*Diseño.* Genera un conjunto de datos con una variable predictora legítima y
otra que sea una **fuga**: correlacionada con la etiqueta por el proceso de
generación pero sin relación causal (por ejemplo, un identificador que se
asignó por orden de gravedad). Entrena un modelo con validación interna.

*Análisis.* Comprueba que la validación interna da un resultado excelente.
Después evalúa sobre un conjunto generado con un proceso distinto —otro orden
de asignación— y mira cómo se desploma.

*Qué falsaría tu confianza:* que el modelo pierda poco al eliminar la variable
legítima y mucho al eliminar la fuga. Ese diagnóstico —**importancia de
variables comparada con lo que la física permite**— es el más útil, y exige
saber qué es plausible: la estadística sola no puede decirlo.
:::

---

## 11. Explícalo

::: explica
1. ¿Por qué un modelo que pasa por todos los puntos es sospechoso?
2. Explica la diferencia entre un confusor y un colisionador, y por qué exigen
   acciones opuestas.
3. ¿Por qué seis sigmas no protegen de un cable flojo?
4. ¿Qué parte de una extrapolación viene de los datos?
5. ¿Por qué la derivada parcial puede decir que un parámetro no importa cuando
   sí importa?
6. ¿Qué le dirías a alguien que ha validado su modelo con los mismos datos con
   los que lo calibró?
:::

---

## 12. Lo esencial

::: esencial
* Un modelo incorrecto no da error: da números plausibles con barras pequeñas.
* Seis modos de mentir, seis diagnósticos. Ninguno se ve mirando el ajuste.
* El error de entrenamiento mide flexibilidad, no calidad. Valida con datos que
  no hayas usado.
* Toda extrapolación es una afirmación sobre física. Extrapola con varios
  modelos y reporta el rango.
* La sensibilidad local sólo vale si el modelo es casi lineal. Con
  interacciones, engaña.
* «Controlar por todo» es incorrecto: controlar por un colisionador **crea**
  sesgo.
* Antes de creerte un resultado numérico: medio paso, otro método,
  conservaciones, invariancias, otra semilla, caso trivial.
* La incertidumbre dominante casi nunca está en los parámetros: está en la
  estructura del modelo, y ninguna barra de error la cubre.
* Escribe, antes de medir, qué resultado te haría abandonar tu modelo.
:::

---

## 13. Preguntas que quedan abiertas

::: abierto
* ¿Se puede cuantificar la incertidumbre estructural, o sólo acotarla usando
  varios modelos?
* Si el modelo verdadero nunca está entre los candidatos, ¿qué estamos midiendo
  exactamente con AIC o BIC?
* ¿Cuánta validación externa es suficiente? ¿Cuántos sitios, cuántos procesos?
* El análisis ciego funciona en física de partículas. ¿Por qué no se ha
  extendido a otros campos, y qué costaría?
* Si un modelo mal especificado predice bien, ¿es útil? ¿Es ciencia?
:::
