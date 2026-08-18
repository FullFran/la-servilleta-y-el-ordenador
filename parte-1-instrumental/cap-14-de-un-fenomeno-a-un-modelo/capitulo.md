# Capítulo 14 — De un fenómeno a un modelo

> **Qué sabrás hacer al terminar**
> · Recorrer el ciclo completo sin saltarte las etapas que se saltan siempre ·
> Construir un modelo mínimo y defender por escrito cada término ·
> Decidir con un criterio cuándo hace falta más modelo y cuánto más ·
> Reconocer el momento en que añadir complejidad deja de mejorar nada.
>
> **Herramientas que usa:** todas las anteriores. Es un capítulo-taller.
> **Disciplinas de los ejemplos:** física térmica, servicios, sociología,
> ingeniería.
> **Deuda que paga:** la taza de café, cuarta visita, ahora con crítica.

---

## 1. Una pregunta

::: pregunta
Te dan un fenómeno sin ecuaciones: **una taza de café se enfría**.

Nadie te dice qué modelo usar, ni qué variables importan, ni qué precisión
hace falta.

**¿Por dónde empiezas?**
:::

Los trece capítulos anteriores han entregado herramientas. Este entrega el
**procedimiento**, y lo hace de la única forma en que se puede aprender: haciendo
tres casos completos de principio a fin, con sus dudas y sus vueltas atrás.

Es un capítulo sin herramientas nuevas. Eso es deliberado.

---

## 2. Antes de calcular

::: antes
Coge papel. Para la taza de café, y antes de leer nada:

1. Escribe cinco variables que podrían importar.
2. Táchalas hasta dejar dos.
3. Escribe la ecuación más simple que se te ocurra.
4. Predice cuánto tarda en pasar de 90 a 60 °C.

Guarda ese papel. Lo compararemos al final del capítulo.
:::

---

## 3. El ciclo, entero

![El ciclo completo. Lo que se ve: las quince etapas, agrupadas por color según sean de formulación (azul), de resolución (verde), de contraste (ocre) o de interpretación (rojo), con los dos bucles de realimentación. Lo que hay que concluir: las tres primeras etapas y las tres últimas son las que distinguen a un modelador; el centro es lo que enseña la carrera.](figuras/fig_ciclo.pdf)

Dos observaciones sobre el diagrama antes de usarlo.

**El bucle rojo es el importante.** Cuando el modelo falla, el reflejo es volver
a las ecuaciones —«habré resuelto mal»— o al método numérico. Casi nunca es
eso. La flecha va **a los supuestos**, que es donde está el error el 80 % de las
veces.

**El bucle ocre existe y casi nadie lo dibuja.** Cuando la simulación da un
número, hay que compararlo con la estimación de orden de magnitud que hiciste
al principio. Si no coinciden, uno de los dos está mal y hay que averiguar
cuál **antes** de seguir. Ese contraste es gratis y es el detector de errores
más eficaz que existe.

---

## 4. Caso guiado 1: la taza de café

### 4.1 Pregunta

«¿Cuánto tarda en enfriarse?» no es una pregunta: es un tema. La pregunta
tiene que ser cuantitativa y llevar una precisión:

> ¿Cuánto tarda un café de 92 °C en llegar a 60 °C, con un error menor de
> dos minutos?

Esa precisión declarada es lo que decide todo lo demás. Con un error admisible
de media hora, sirve el modelo más burdo. Con dos minutos, ya no.

### 4.2 Orden de magnitud

Capítulo 1. Masa 0,25 kg, $c=4186$ J/(kg·K), superficie total $\sim0{,}035$
m², $h\sim15$ W/(m²·K) en convección natural.

$$\tau=\frac{mc}{hA}=\frac{0{,}25\times4186}{15\times0{,}035}\approx2000\ \text{s}
\approx33\ \text{min}$$

Y de 92 a 60 °C, el exceso pasa de 71 a 39: $t=\tau\ln(71/39)\approx20$ min.

**Este número es el patrón contra el que se juzgará todo lo que venga después.**

### 4.3 Variables, y las que se descartan

Lo que importa: masa, calor específico, superficie, salto térmico, coeficiente
de transferencia.

Lo que se descarta, **con motivo escrito**:

| Descartada | Por qué |
|---|---|
| Forma exacta de la taza | entra sólo por $A$, y $A$ ya está |
| Material de la taza | su capacidad térmica es $\sim10\%$ de la del café |
| Color | afecta a la radiación, que estimamos en el 20 % |
| Presión atmosférica | irrelevante salvo a gran altitud |
| Agitación | **no descartada**: cambia $h$ por un factor 3 |

Esa última fila es la interesante. La lista de descartes no es un trámite: es
donde se decide el modelo, y donde aparecen las variables que hay que
**controlar en el experimento**.

### 4.4 Supuestos, numerados

1. Temperatura uniforme en el líquido. Válido si $Bi=hL/k\ll1$: con
   $L\sim0{,}03$ m y $k_{\text{agua}}=0{,}6$, $Bi\approx0{,}75$. **No es
   pequeño.** Sobrevive porque hay convección natural dentro de la taza, que
   mezcla; si el café estuviera gelificado, el modelo fallaría.
2. $h$ constante. Falso: en convección natural $h\propto\Delta T^{1/4}$.
3. Radiación despreciable frente a convección. A comprobar (sección 4.7).
4. Evaporación despreciable. A comprobar, y **esta es la que va a fallar**.
5. Temperatura ambiente constante.
6. Sin tapa, sin corrientes de aire.

### 4.5 Modelo mínimo y su solución

$$\frac{dT}{dt}=-\frac{T-T_{\text{amb}}}{\tau}
\quad\Longrightarrow\quad
T(t)=T_{\text{amb}}+(T_0-T_{\text{amb}})e^{-t/\tau}$$

### 4.6 Contraste con los datos, y el momento interesante

![La taza de café con datos. Arriba: ajuste del modelo de Newton y de un modelo con dos escalas. Abajo: sus residuos, con la banda gris del ruido de medida declarado (0,35 °C). Lo que hay que concluir: el modelo mínimo da un ajuste que parece bueno y deja residuos con forma; el segundo agota la información de los datos.](figuras/fig_cafe_progresivo.pdf)

El ajuste de Newton da $\tau=26{,}3$ min —cerca de los 33 estimados, dentro de
la incertidumbre de $h$— y un rms de residuos de **0,79 °C**, más del doble del
ruido de medida.

Y los residuos tienen **forma**. Eso, y no el valor del rms, es el diagnóstico
del capítulo 5: el modelo está sistemáticamente mal al principio y
sistemáticamente bien al final.

### 4.7 Diagnóstico: ¿qué falta?

La forma de los residuos dice que **el enfriamiento inicial es más rápido de lo
que predice Newton**. ¿Qué mecanismo se acelera con el salto térmico más
deprisa que linealmente?

* **Radiación:** $\propto T^4-T_{\text{amb}}^4$. Estimando con $\varepsilon=0{,}95$
  y $A=0{,}035$ m²: 19 W a 92 °C frente a 37 W de convección. **No es
  despreciable**, y crece más deprisa que linealmente.
* **Evaporación:** la presión de vapor crece exponencialmente con la
  temperatura (Clausius–Clapeyron), así que el flujo evaporativo crece mucho
  más deprisa que $\Delta T$. Del orden de 30 W a 92 °C y casi nada a 40 °C.

Los dos son candidatos y los dos van en la misma dirección. Y aquí llega la
pregunta honesta: **¿podemos distinguirlos con estos datos?**

La respuesta es que no, o no fácilmente: los dos producen un exceso de
enfriamiento inicial y ajustan igual de bien. Estamos en el valle plano del
capítulo 10. Para separarlos hace falta **un experimento distinto**, no un
ajuste mejor: pesar la taza (la evaporación quita masa, la radiación no) o
repetir con tapa.

Ese es exactamente el momento en que un modelador deja de teclear y va a
buscar una balanza.

### 4.8 Cuándo parar

El modelo de dos escalas deja residuos de 0,37 °C, indistinguibles del ruido de
medida de 0,35 °C. **Ha agotado la información de los datos.** Añadir un
tercer término mejoraría el rms un poco y no significaría nada: estaríamos
ajustando ruido, que es el capítulo 15.

El criterio operativo:

> Deja de añadir complejidad cuando los residuos sean del tamaño del ruido de
> medida **y** no tengan estructura.

Y el corolario incómodo: si tus datos son ruidosos, **no puedes distinguir
modelos**, por mucha física que sepas. Mejorar la medida es a menudo más
rentable que mejorar el modelo, y esa decisión es parte del modelado.

---

## 5. Caso guiado 2: la cola del supermercado

Un caso donde el «fenómeno» no es físico y el procedimiento es idéntico.

**Pregunta.** ¿Cuántas cajas hay que abrir un sábado a las 12:00 para que
nadie espere más de 5 minutos el 90 % de las veces?

**Orden de magnitud.** Llegan $\lambda\approx3$ clientes por minuto; cada uno
tarda $\sim2$ min en ser atendido. Se necesita capacidad
$\mu>\lambda$: al menos $3\times2=6$ cajas **sólo para no acumular cola
indefinidamente**. La respuesta es «más de 6», y ya sabemos el orden.

**Variables.** Tasa de llegada, tiempo de servicio, número de cajas. Se
descartan: qué compra cada cliente (entra vía el tiempo de servicio), la
disposición de la tienda, la fidelidad.

**Supuestos.** (1) Llegadas de Poisson —capítulo 4—; (2) tasa constante en la
ventana considerada, falso a lo largo del día pero razonable en una hora;
(3) servicio exponencial, discutible: el tiempo de caja tiene un mínimo y
**no** es exponencial; (4) una sola cola para todas las cajas.

**Modelo mínimo.** Una cola M/M/c. Y aquí aparece un resultado del capítulo 4
que no es evidente: **la utilización no puede acercarse a 1**. Con $\rho=0{,}9$
la espera media es diez veces la de $\rho=0{,}5$. La cola no crece
gradualmente al saturar: **explota**.

**Crítica.** El supuesto 3 es el peor, y sesga en la dirección peligrosa: un
servicio exponencial tiene mucha más variabilidad que uno real, así que el
modelo **sobreestima** la cola. Y el supuesto 4 es una decisión de diseño, no
del mundo: una cola única es medible y demostrablemente mejor que $c$ colas
independientes, y por eso los aeropuertos y los bancos las adoptaron.

El capítulo II.12 desarrolla esto.

---

## 6. Caso guiado 3: un rumor en una oficina

**Pregunta.** En una oficina de 200 personas, ¿a cuánta gente llega un rumor y
en cuánto tiempo?

**Modelo mínimo 1.** Todo el mundo que lo sabe se lo cuenta a todo el mundo:
$\dot y=\beta y$. Crecimiento exponencial. **Predice que llega a todos**, y
predice que la velocidad no baja nunca: falso por construcción, porque hay 200
personas.

**Modelo mínimo 2.** Sólo cuenta a quien no lo sabe: $\dot y=\beta y(N-y)/N$.
Logística. También predice que llega a todos, pero con la forma de S correcta.

**Modelo mínimo 3.** Los que ya lo han contado varias veces se aburren y dejan
de contarlo (Daley–Kendall). Ahora la fracción final es **menor que 1** y
depende de $\beta/\gamma$.

Los tres son razonables. ¿Cómo se elige?

**Con un dato observable y barato:** ¿el rumor llega a todo el mundo? Si en tu
oficina hay siempre gente que no se entera, los modelos 1 y 2 están
descartados sin necesidad de medir ninguna tasa.

Esa es la lección del caso: **el dato que discrimina entre modelos no suele ser
el más preciso, sino el que separa predicciones cualitativas**. Buscar ese dato
es más rentable que medir con más cifras.

---

## 7. ¿Qué estamos suponiendo? (sobre el propio método)

::: supuestos
1. **Que existe un modelo mínimo útil.** En sistemas fuertemente acoplados o
   con muchos mecanismos comparables, puede no haberlo.
2. **Que los datos discriminan entre modelos.** A menudo no lo hacen, y hay
   que reconocerlo en vez de fingir que sí.
3. **Que sabemos qué precisión hace falta.** Es una pregunta sobre la decisión
   que va a tomarse, no sobre el fenómeno.
4. **Que el fenómeno es estacionario** durante la observación.
5. **Que el ciclo termina.** En la práctica se abandona cuando el modelo es
   suficientemente bueno para la decisión, no cuando es «correcto».
:::

---

## 8. ¿Cuándo falla el método?

::: falla
**Falla si te saltas la estimación previa.** Sin ella no tienes patrón contra
el que juzgar el resultado, y aceptarás cualquier número que salga del
ordenador.

**Falla si los supuestos no están escritos.** Un supuesto tácito no se puede
revisar cuando el modelo falla, y el bucle rojo del diagrama se rompe.

**Falla si empiezas por el modelo complicado.** Es el error más frecuente entre
gente con formación técnica: se domina la herramienta y se aplica antes de
haber formulado la pregunta. Un modelo de 15 parámetros que ajusta bien no
enseña nada; uno de 2 que falla enseña dónde falla.

**Falla si no declaras la precisión necesaria.** Sin ella, no hay criterio de
parada y el modelo crece indefinidamente.

**Y falla si confundes ajustar con explicar.** Que un modelo reproduzca los
datos no significa que su mecanismo sea el real. Capítulo 15 entero.
:::

### Un anti-ejemplo: el modelo que se validó consigo mismo

Un equipo desarrolla un modelo de consumo energético de un edificio con 40
parámetros. Lo calibra con un año de datos y obtiene un error del 3 %. Lo
presenta como validado.

El problema: **calibración no es validación**. Los 40 parámetros se ajustaron
con esos mismos datos. Un error del 3 % sobre los datos de calibración no dice
nada; lo que habría que reportar es el error sobre un año **distinto**, que en
casos así suele estar entre el 15 % y el 30 %.

La distinción tiene vocabulario propio en ingeniería computacional, y conviene
usarlo: **verificación** es «¿resuelvo bien mis ecuaciones?»; **calibración** es
«¿qué parámetros hacen que se ajusten a estos datos?»; **validación** es
«¿predice datos que no he usado?». Son tres cosas distintas, y la tercera es la
única que autoriza a usar el modelo para decidir algo.

---

## 9. Historia

::: historia
**«Todos los modelos son falsos», y lo que Box dijo de verdad** ·
*Nivel de verificación: A.*

La frase se cita constantemente en una forma que Box no escribió exactamente
así de golpe. En *Science and Statistics* (JASA, 1976) escribió que todos los
modelos son falsos, y que la pregunta práctica es cuán falsos tienen que ser
para no ser útiles. La formulación popular —«all models are wrong, but some are
useful»— aparece en un trabajo de 1979.

Lo que se cita menos, y es más útil, es lo que decía a continuación: que el
científico debe buscar **la descripción económica** de los fenómenos naturales,
y que dado que todo modelo es falso, no hay que preocuparse por buscar la
falsedad —siempre está— sino por identificar **qué falsedad importa** para el
propósito concreto.

Y una segunda advertencia suya, en la misma línea: la sobreelaboración y la
sobreparametrización son a menudo la marca de la mediocridad. Es exactamente el
criterio de parada de la sección 4.8.

**Kepler, y el modelo que tardó ocho años en caer** ·
*Nivel de verificación: A.*

Johannes Kepler pasó unos ocho años intentando ajustar la órbita de Marte con
combinaciones de círculos, siguiendo la tradición de veinte siglos. Llegó a un
modelo que reproducía las observaciones de Tycho Brahe con un error de
**ocho minutos de arco**.

Ocho minutos de arco es una precisión extraordinaria: es una octava parte del
diámetro aparente de la Luna, y era mejor que casi cualquier observación
anterior a Tycho. Kepler podría haber publicado.

En su *Astronomia Nova* (1609) explica por qué no lo hizo: **porque sabía que
las observaciones de Tycho eran mejores que ocho minutos**. Esa discrepancia,
que cualquier otro habría atribuido a error de medida, la trató como
información. Y de ahí salieron las órbitas elípticas.

Es el mejor ejemplo histórico de la sección 4.8 al revés: Kepler tenía residuos
**por encima** del ruido de sus datos, con estructura, y se negó a aceptarlos.
Lo que hace falta para eso no es más matemática: es conocer la incertidumbre de
tus datos mejor que nadie.
:::

---

## 10. Problemas

En `problemas.md`; soluciones en `soluciones.md`.

---

## 11. Experimento computacional

::: experimento
**Recorre el ciclo entero con un fenómeno tuyo.**

*Pregunta:* elige algo que puedas medir esta semana. Cuánto tarda tu casa en
enfriarse, cuánta batería consume tu móvil, cuánto tardan en llegar los correos
de tu bandeja, cuánta gente hay en el gimnasio a cada hora.

*Diseño.* Recorre las quince etapas del diagrama, **por escrito**, en el
cuaderno del modelador. Especialmente:
las tres primeras (pregunta con precisión declarada, orden de magnitud,
variables descartadas con motivo) y las tres últimas (interpretación, límites,
nueva pregunta).

*Criterio de parada:* residuos del tamaño del ruido y sin estructura, **o** una
declaración explícita de por qué no puedes llegar ahí con los datos que tienes.

*Qué falsaría tu modelo:* escríbelo antes de medir. ¿Qué observación lo
mataría? Si no puedes contestar, tu modelo no es científico todavía, sólo
descriptivo.

*Lo importante del ejercicio no es el modelo.* Es descubrir en qué etapa te
atascas, porque en esa misma te atascarás siempre.
:::

---

## 12. Explícalo

::: explica
1. ¿Por qué la primera pregunta de un modelo es «¿con qué precisión?»?
2. ¿Qué información hay en un residuo con forma que no hay en su valor rms?
3. ¿Por qué cuando un modelo falla hay que volver a los supuestos y no a las
   ecuaciones?
4. Explica la diferencia entre calibrar y validar a alguien que no la conoce.
5. ¿Cuándo hay que dejar de mejorar un modelo?
6. ¿Por qué Kepler no publicó un modelo con un error de ocho minutos de arco?
:::

---

## 13. Lo esencial

::: esencial
* Una pregunta de modelado lleva **una precisión declarada**. Sin ella no hay
  criterio de parada.
* La estimación previa no es un adorno: es el patrón contra el que se juzga
  todo lo que salga del ordenador.
* La lista de variables descartadas, con su motivo, es donde se decide el
  modelo.
* Los supuestos se escriben y se numeran, con su condición de validez
  cuantitativa.
* Empieza por el modelo mínimo. Uno de dos parámetros que falla enseña más que
  uno de quince que ajusta.
* Los residuos con forma dicen que falta física; el rms solo, no.
* Para cuando los residuos sean del tamaño del ruido **y** no tengan
  estructura.
* Si dos mecanismos ajustan igual, no hace falta un ajuste mejor: hace falta
  **otro experimento**.
* Calibrar no es validar. Validar es predecir datos que no has usado.
:::

---

## 14. Preguntas que quedan abiertas

::: abierto
* ¿Existe algún criterio objetivo para decidir «lo más simple que podría
  funcionar», o es siempre juicio experto?
* Si dos modelos con mecanismos distintos ajustan igual de bien, ¿en qué
  sentido uno es «mejor»?
* ¿Cuándo es más rentable mejorar los datos que mejorar el modelo? ¿Se puede
  decidir antes de intentarlo?
* El ciclo tiene bucles. ¿Cómo se sabe que no estás dando vueltas
  indefinidamente?
* ¿Qué pasa con fenómenos donde no hay separación de escalas y todos los
  mecanismos son comparables? ¿Hay modelo mínimo?
:::
