# II.10 — ¿Cuándo deja de ser posible predecir?

> **El fenómeno:** la predicción del tiempo a 3 días acierta; a 15, no.
> **Herramientas:** cap. 7 (caos), cap. 8 (integración), cap. 15
> (incertidumbre estructural).
> **Lo que hay que llevarse:** que cuando la trayectoria deja de ser
> predecible, la distribución sigue siéndolo, y que eso cambia qué preguntas
> hay que hacer.

---

## 1. Una pregunta

::: pregunta
Tienes un modelo determinista perfecto y datos iniciales con un error de
$10^{-9}$.

**¿Cuánto tiempo puedes predecir?**

Y la pregunta que importa de verdad: **¿qué haces después de ese tiempo?**
:::

---

## 2. Antes de calcular

::: antes
1. Con $\lambda\approx0{,}9$ y error inicial $10^{-9}$, ¿cuál es el horizonte?
2. Si el error inicial baja a $10^{-12}$, ¿cuánto ganas?
3. ¿Qué se puede afirmar sobre el sistema a tiempos mucho mayores que el
   horizonte?
:::

---

## 3. Del cálculo único al conjunto

![Predicción por conjuntos en el sistema de Lorenz. Izquierda: 200 trayectorias con datos iniciales que difieren en 0,05. Derecha: la dispersión del conjunto, con crecimiento exponencial de exponente medido 0,939 y saturación en la dispersión climatológica. Lo que hay que concluir: pasado $t\approx5$, la media del conjunto deja de ser informativa y lo único que queda es la distribución.](figuras/fig_ensemble.pdf)

La idea es simple y cambió la meteorología operativa: en lugar de una
predicción, se hacen **muchas**, con condiciones iniciales perturbadas dentro de
la incertidumbre real de las observaciones.

Y el resultado del conjunto se lee de tres maneras distintas según el plazo:

| Plazo | Qué informa | Qué se publica |
|---|---|---|
| Corto ($t\ll t_h$) | la trayectoria | «mañana, 22 °C» |
| Intermedio ($t\sim t_h$) | la dispersión | «60 % de probabilidad de lluvia» |
| Largo ($t\gg t_h$) | la climatología | «en abril llueve 8 días de media» |

**La dispersión del conjunto es información**, y no un fracaso. Un día con
dispersión pequeña es un día predecible; con dispersión grande, no. Esa
variabilidad de la predecibilidad se puede predecir a su vez, y es la base de
los índices de confianza que acompañan a las predicciones modernas.

---

## 4. Los tres límites, en orden de importancia

El horizonte no lo pone sólo el caos. Hay tres barreras y conviene saber cuál
domina:

**1. Incertidumbre de las condiciones iniciales.** Crece como $e^{\lambda t}$.
Es la que estudiamos en el capítulo 7 y la que da $t_h=\lambda^{-1}\ln(\Delta/
\epsilon)$.

**2. Error del modelo.** Las ecuaciones no son las verdaderas: hay
parametrizaciones, resolución finita, procesos ausentes. Este error **no se
reduce con mejores observaciones**, y en meteorología domina a partir de unos
pocos días.

**3. Incertidumbre estructural.** Ni siquiera sabemos con seguridad qué
procesos hay que incluir. Es la del capítulo 15, y no hay técnica que la
cuantifique desde dentro.

La consecuencia práctica es incómoda: **invertir en más estaciones
meteorológicas tiene rendimientos decrecientes muy rápidos** si el error
dominante es el del modelo. Decidir cuál domina, y a qué plazo, es una pregunta
cuantitativa que se responde con experimentos de conjunto —perturbando datos
iniciales frente a perturbando el modelo— y que decide dónde va el presupuesto.

---

## 5. Predecir la predecibilidad

Hay una segunda capa, y es donde está la investigación actual.

El exponente de Lyapunov es un **promedio** sobre el atractor. Localmente, la
tasa de divergencia varía mucho: hay regiones del espacio de fases donde las
trayectorias divergen deprisa y otras donde son estables durante bastante
tiempo.

Eso significa que **hay días predecibles y días impredecibles**, y que se puede
saber de antemano cuáles. Operativamente se hace midiendo la dispersión inicial
del conjunto y su tasa de crecimiento en las primeras horas.

Es una idea general que se transfiere: en cualquier sistema caótico con
observación, la pregunta «¿cuánto puedo predecir?» tiene respuesta **variable**
y estimable, y usarla es mucho más útil que un horizonte fijo.

---

## 6. ¿Cuándo falla?

::: falla
**Falla el conjunto si las perturbaciones no representan la incertidumbre
real.** Un conjunto con perturbaciones demasiado pequeñas produce dispersión
insuficiente y **exceso de confianza**: es la curva de calibración del capítulo
1, ahora sobre predicciones meteorológicas. Se comprueba con diagramas de
fiabilidad.

**Falla si el modelo tiene sesgos.** Todo el conjunto se desvía en la misma
dirección y la dispersión no lo detecta. Por eso se usan conjuntos
**multimodelo**, con distintos centros meteorológicos.

**Falla extrapolar el horizonte a otros sistemas.** El de la atmósfera son ~2
semanas; el del océano, meses; el de las placas tectónicas, ninguno útil. Cada
sistema tiene su $\lambda$.

**Y falla confundir horizonte con inutilidad.** Que no se pueda predecir el
tiempo a 3 meses no impide predecir el clima a 50 años, porque son preguntas
distintas: una sobre la trayectoria, otra sobre las estadísticas.
:::

---

## 7. Historia

::: historia
**De Richardson a los conjuntos** · *Nivel de verificación: A.*

Richardson (1922) intentó la predicción numérica y falló por los datos
iniciales, no por el método (capítulo 8). Charney, Fjørtoft y von Neumann
(1950) hicieron la primera predicción con ordenador. Lorenz (1963) demostró
que había un límite intrínseco.

La respuesta operativa tardó tres décadas más. Epstein propuso en 1969 la
predicción estocástica; Leith mostró en 1974 que un conjunto pequeño ya
aproxima bien la media; y el ECMWF y el NCEP implementaron conjuntos
operativos en **1992**.

Es decir: **veintinueve años entre el descubrimiento del problema y su
tratamiento rutinario**. La solución no fue resolver el caos —no se puede— sino
cambiar la pregunta.

**Y una advertencia de Lorenz que suele omitirse** · *Nivel A.*

Lorenz insistió repetidamente en que la sensibilidad a las condiciones
iniciales no significa que las causas pequeñas produzcan efectos grandes de
forma controlable. Un aleteo puede provocar un tornado **o impedir uno que iba
a ocurrir**, y no hay manera de saber cuál. La metáfora popular se usa a menudo
para justificar una idea de causalidad que Lorenz negaba explícitamente.
:::

---

## 8. Experimento computacional

::: experimento
**Predice la predecibilidad.**

En el sistema de Lorenz, lanza conjuntos de 100 miembros desde muchos puntos
distintos del atractor, todos con la misma dispersión inicial.

Mide, para cada punto de partida, la dispersión al cabo de un tiempo fijo.

*Qué esperar:* una distribución ancha. Algunos puntos de partida son mucho más
predecibles que otros.

*La parte interesante:* ¿se puede predecir cuál será cuál **mirando sólo el
estado inicial**? Prueba con la posición en el atractor, la distancia al plano
de separación entre lóbulos, y el mayor valor singular de la matriz tangente.
Ese último es el que funciona, y es la base de los *vectores singulares* que
usa el ECMWF para generar sus perturbaciones.
:::

---

## 9. Lo esencial

::: esencial
* Cuando la trayectoria deja de ser predecible, la **distribución** sigue
  siéndolo. La solución no fue resolver el caos: fue cambiar la pregunta.
* La dispersión del conjunto es información, no fracaso.
* Tres límites: datos iniciales, error de modelo e incertidumbre estructural.
  Saber cuál domina decide dónde invertir.
* La predecibilidad **varía**: hay días predecibles y días que no, y se puede
  saber de antemano.
* Un conjunto mal calibrado produce exceso de confianza, y se detecta con
  diagramas de fiabilidad.
* Horizonte finito no significa inutilidad: tiempo y clima son preguntas
  distintas.
:::

---

## 10. Preguntas abiertas

::: abierto
* ¿Cómo se separa cuantitativamente el error de datos iniciales del error de
  modelo en un sistema real?
* ¿Cuál es el límite de predecibilidad de fenómenos sociales o económicos, y
  tiene sentido la pregunta?
* Si los conjuntos multimodelo funcionan mejor, ¿qué dice eso sobre lo que
  significa «el mejor modelo»?
* ¿Se puede predecir la predecibilidad en sistemas sin modelo, sólo con datos?
:::

### Referencias

* **Lorenz, E. N.** *The Essence of Chaos.* Univ. of Washington Press, 1993.
* **Palmer, Tim.** *The Primacy of Doubt.* Oxford UP, 2022. **La referencia del
  capítulo**, por un meteorólogo que ha construido estos sistemas.
* **Epstein, E. S.** *Stochastic dynamic prediction.* Tellus **21** (1969),
  739–759. **Nivel A (primaria).**
* **Leith, C. E.** *Theoretical skill of Monte Carlo forecasts.* Monthly Weather
  Review **102** (1974), 409–418. **Nivel A (primaria).**
* **Palmer, T. N. et al.** *Representing model uncertainty in weather and
  climate prediction.* Annu. Rev. Earth Planet. Sci. **33** (2005), 163–193.
* **Wilks, Daniel.** *Statistical Methods in the Atmospheric Sciences.* 4.ª ed.,
  Elsevier, 2019. Verificación y calibración de predicciones probabilísticas.
