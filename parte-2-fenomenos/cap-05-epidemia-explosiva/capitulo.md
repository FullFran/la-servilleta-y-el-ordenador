# II.5 — ¿Por qué una epidemia puede explotar?

> **El fenómeno:** unos cuantos casos se convierten en miles en semanas, y
> después la curva baja sola sin que nadie haya vacunado a nadie.
> **Herramientas:** cap. 2 (adimensionalizar), cap. 6 (EDO), cap. 7
> (bifurcación transcrítica), cap. 10 (ajuste), cap. 15 (extrapolación).
> **Lo que hay que llevarse:** que el umbral epidémico es una bifurcación, que
> una epidemia se pasa de frenada, y por qué los modelos de epidemias
> extrapolan tan mal.

---

## 1. Una pregunta

::: pregunta
Un patógeno con $R_0=3$ llega a una población totalmente susceptible.

**¿Qué fracción de la población acaba infectada?**

La respuesta intuitiva —«el 67 %, que es cuando se alcanza la inmunidad de
grupo $1-1/R_0$»— es falsa. La correcta es **94 %**.
:::

---

## 2. Antes de calcular

::: antes
1. Tu respuesta al tamaño final con $R_0=3$.
2. Si $R_0$ pasa de 0,95 a 1,05, ¿cambia poco o mucho el resultado?
3. ¿Por qué baja la curva de una epidemia?
:::

---

## 3. El modelo mínimo y su umbral

$$\dot S=-\beta SI,\qquad \dot I=\beta SI-\gamma I,\qquad \dot R=\gamma I$$

Adimensionalizando con $\tau=\gamma t$ y $R_0=\beta/\gamma$, quedan **dos**
parámetros: $R_0$ y la condición inicial. Los tres originales se han reducido a
uno relevante.

Al principio, con $S\approx1$:

$$\dot I=(\beta-\gamma)I=\gamma(R_0-1)I$$

Crecimiento exponencial si $R_0>1$, decaimiento si $R_0<1$. Ese es el umbral, y
es exactamente una **bifurcación transcrítica** del capítulo 7: el equilibrio
libre de enfermedad intercambia estabilidad con el endémico.

![El modelo SIR. Izquierda: curvas de infectados para varios $R_0$; el umbral en $R_0=1$ es abrupto. Derecha: tamaño final frente a $R_0$, comparado con el umbral de inmunidad de grupo. Lo que hay que concluir: la epidemia no se para al alcanzar la inmunidad de grupo; sigue por inercia y se pasa de frenada.](figuras/fig_sir.pdf)

---

## 4. El sobrepaso: por qué el 94 % y no el 67 %

La epidemia deja de crecer cuando $S=1/R_0$, es decir, cuando queda un $1/R_0$
de susceptibles. Ese es el umbral de inmunidad de grupo: $1-1/R_0=67\%$ ya
infectado.

Pero en ese instante **hay muchísima gente infecciosa todavía**, y sigue
contagiando. La epidemia decae, pero mientras decae sigue infectando. El
resultado final se obtiene de la ecuación de tamaño final:

$$1-x=e^{-R_0x}$$

que para $R_0=3$ da $x=0{,}94$.

| $R_0$ | Umbral de vacunación | Tamaño final sin intervención |
|---|---|---|
| 1,5 | 33 % | **58 %** |
| 2,5 | 60 % | **89 %** |
| 3,0 | 67 % | **94 %** |
| 5,0 | 80 % | **99 %** |

**Ese sobrepaso es la diferencia entre vacunar y dejar que pase.** Con
vacunación se llega al umbral y se para; sin ella, se llega al umbral con el
sistema en marcha y se atraviesa con mucho margen. Es dinámica, no
epidemiología: el mismo fenómeno ocurre en cualquier sistema con inercia que
cruza un umbral.

---

## 5. Por qué estos modelos extrapolan tan mal

Del capítulo 15. En la fase inicial, **todos los modelos son exponenciales**:
SIR, SEIR, modelos en red, modelos de agentes. Ajustan igual de bien y
predicen picos que difieren en órdenes de magnitud.

Y hay tres razones estructurales por las que el SIR simple sobreestima:

**Heterogeneidad de contactos.** Si unas personas tienen muchos más contactos
que otras, se infectan antes y sacan del juego a los nodos más conectados. El
tamaño final baja sustancialmente respecto a la mezcla homogénea, y el umbral
de inmunidad de grupo también.

**Sobredispersión.** Del capítulo 4: si el 10 % de los infectados causa el 80 %
de los contagios, muchos brotes se extinguen solos aunque $R_0>1$. La
probabilidad de extinción de un brote iniciado por un caso es la raíz de la
función generatriz, y con $k=0{,}1$ y $R_0=3$ supera el 80 %.

**Cambio de comportamiento.** $\beta$ no es constante: la gente reacciona. Un
modelo con $\beta$ fija es un modelo de una población que no se entera de que
hay una epidemia.

De ahí la regla operativa: **los modelos SIR sirven para entender mecanismos y
para comparar escenarios, no para predecir números concretos a dos meses vista**.
Y esa distinción hay que decirla en voz alta cada vez que se publique una cifra.

---

## 6. ¿Cuándo falla?

::: falla
**Falla la mezcla homogénea.** Es el supuesto dominante y el más falso: nadie
tiene la misma probabilidad de contactar con todos.

**Falla el continuo con pocos casos.** Al principio y al final de un brote hay
decenas de individuos, y ahí el modelo determinista no puede predecir la
extinción, que es un fenómeno estocástico.

**Falla suponer inmunidad permanente.** Con reinfección, el modelo correcto es
SIRS y admite oscilaciones sostenidas o endemicidad.

**Y falla, siempre, ajustar $R_0$ a la fase exponencial y extrapolar.** El
número que se obtiene es el de una población que todavía no ha cambiado de
comportamiento.
:::

---

## 7. Historia

::: historia
**Kermack y McKendrick, 1927** · *Nivel de verificación: A.*

William Kermack, químico, y Anderson McKendrick, médico militar en la India,
publicaron en 1927 el modelo y —lo importante— **el teorema del umbral**: una
epidemia sólo despega si la densidad de susceptibles supera un valor crítico.

Antes de eso, la explicación estándar del final de una epidemia era que el
patógeno perdía virulencia. Kermack y McKendrick demostraron que **no hace
falta ninguna hipótesis sobre el patógeno**: la epidemia se apaga sola porque
se queda sin susceptibles.

Es un ejemplo perfecto del principio del capítulo 14: un modelo mínimo elimina
la necesidad de un mecanismo que se había postulado sin evidencia.

**Y una nota sobre $R_0$** · *Nivel B.*

El símbolo $R_0$ y su interpretación provienen de la demografía —donde denota
la tasa neta de reproducción— y entraron en epidemiología a través de George
MacDonald en los años cincuenta, trabajando en malaria. La notación es
desafortunada: el subíndice cero sugiere una constante del patógeno, cuando en
realidad $R_0$ depende de la población, del comportamiento y del contexto tanto
como del microorganismo. Publicar «el $R_0$ del sarampión es 15» sin decir en
qué población es una afirmación incompleta.
:::

---

## 8. Experimento computacional

::: experimento
**Del continuo a la red.**

Implementa el SIR de tres maneras: (a) determinista, con las EDO; (b)
estocástico bien mezclado, con Gillespie; (c) sobre una red de contactos con
distribución de grado ancha.

Con el mismo $R_0$ en los tres, compara: probabilidad de extinción, tamaño
final y altura del pico.

*Qué esperar:* (b) da extinciones frecuentes que (a) no puede producir; (c) da
un tamaño final menor y un pico más bajo y ancho que (a).

*La pregunta que hay que contestar:* ¿cuánto de la diferencia entre (a) y (c) se
debe al valor medio del grado y cuánto a su varianza? (Pista: para redes
configuracionales, $R_0$ efectivo depende de $\langle k^2\rangle/\langle
k\rangle$.)
:::

---

## 9. Lo esencial

::: esencial
* El umbral $R_0=1$ es una bifurcación transcrítica: el cambio de
  comportamiento es cualitativo, no gradual.
* La epidemia **se pasa de frenada**: con $R_0=3$, el umbral de inmunidad es el
  67 % y el tamaño final el 94 %.
* Adimensionalizado, el SIR tiene un solo parámetro relevante.
* En la fase exponencial todos los modelos coinciden y predicen cosas
  radicalmente distintas después.
* Heterogeneidad, sobredispersión y cambio de comportamiento reducen el tamaño
  final respecto al SIR homogéneo.
* $R_0$ no es una constante del patógeno: depende de la población.
:::

---

## 10. Preguntas abiertas

::: abierto
* ¿Cuánta heterogeneidad hace falta para cambiar el umbral de inmunidad de
  grupo de forma apreciable?
* ¿Cómo se estima $R_0$ en tiempo real sin conocer el número de casos no
  detectados?
* ¿Se puede modelar el cambio de comportamiento endógenamente, sin meterlo a
  mano?
* ¿Qué modelo mínimo describe una epidemia con inmunidad decreciente y
  estacionalidad?
:::

### Referencias

* **Kermack, W. O. y McKendrick, A. G.** *A Contribution to the Mathematical
  Theory of Epidemics.* Proc. R. Soc. A **115** (1927), 700–721.
  **Nivel A (primaria).**
* **Anderson, Roy y May, Robert.** *Infectious Diseases of Humans.* Oxford UP,
  1991. El tratado clásico.
* **Keeling, Matt y Rohani, Pejman.** *Modeling Infectious Diseases in Humans
  and Animals.* Princeton UP, 2008. **La referencia moderna**, con código.
* **Lloyd-Smith, J. O. et al.** *Superspreading and the effect of individual
  variation on disease emergence.* Nature **438** (2005), 355–359.
* **Britton, T.; Ball, F.; Trapman, P.** *A mathematical model reveals the
  influence of population heterogeneity on herd immunity to SARS-CoV-2.*
  Science **369** (2020), 846–849. El efecto de la heterogeneidad, cuantificado.
