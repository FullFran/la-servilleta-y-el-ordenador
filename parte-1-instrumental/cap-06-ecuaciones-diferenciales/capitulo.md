# Capítulo 6 — Ecuaciones diferenciales como lenguaje del cambio

> **Qué sabrás hacer al terminar**
> · Traducir una descripción verbal de un fenómeno a $\dot x=f(x,t)$ ·
> Leer una ecuación diferencial sin resolverla, usando la línea de fases ·
> Identificar el tiempo característico y usarlo para decidir qué ignorar ·
> Adimensionalizar una EDO y reducir su número de parámetros ·
> Reconocer los cuatro modelos que explican medio mundo.
>
> **Herramientas que usa:** capítulos 1, 2 y 5.
> **Disciplinas de los ejemplos:** física térmica, electricidad, ecología,
> farmacología, química, epidemiología.
> **Deuda que paga:** la adimensionalización prometida en el capítulo 2; la
> taza de café ajustada en el capítulo 5, ahora derivada.
> **Deuda que abre:** cómo se resuelve esto en un ordenador (capítulo 8); qué
> pasa en dimensión tres (capítulo 7).

---

## 1. Una pregunta

::: pregunta
Tres situaciones sin nada en común:

* una taza de café enfriándose sobre la mesa;
* un condensador descargándose a través de una resistencia;
* una muestra radiactiva perdiendo actividad.

**¿Por qué las tres tienen exactamente la misma gráfica?**
:::

No es una coincidencia bonita, y tampoco es que «la naturaleza sea elegante».
Es que las tres frases —«el café pierde calor tanto más deprisa cuanto más
caliente está», «el condensador se descarga tanto más deprisa cuanta más carga
tiene», «cuantos más núcleos quedan, más se desintegran por segundo»— dicen
literalmente lo mismo:

$$\frac{dx}{dt}=-\frac{x}{\tau}$$

Este capítulo va de aprender a oír esa frase debajo de las palabras.

---

## 2. Antes de calcular

::: antes
1. Un café pasa de 90 °C a 60 °C en 15 minutos, con la habitación a 20 °C.
   ¿Cuánto tarda en pasar de 60 °C a 40 °C? ¿Más o menos de 15 minutos?
2. Una población crece un 3 % al año. ¿En cuántos años se duplica? Sin
   calculadora.
3. ¿Qué información necesitas hoy para predecir el estado de un sistema
   mañana? Escribe una lista.

La tercera pregunta define lo que en este capítulo llamaremos *estado*, y es
más sutil de lo que parece.
:::

---

## 3. La intuición

### 3.1 Leer la ecuación en voz alta

$$\frac{dx}{dt}=f(x,t)$$

Traducción literal: **«dime dónde estás y te digo hacia dónde vas y a qué
velocidad»**. Nada más. Una ecuación diferencial es una regla local; no
contiene la trayectoria, la genera.

Este cambio de punto de vista es el que hay que instalar. Una fórmula
$x(t)=x_0e^{-t/\tau}$ te dice dónde está el sistema en cada instante. La
ecuación $\dot x=-x/\tau$ te dice **por qué**, y sigue siendo útil cuando la
fórmula no existe, que es casi siempre.

### 3.2 Estado: lo que hay que saber hoy para predecir mañana

El **estado** es la información mínima que determina el futuro. Para un café,
su temperatura. Para un péndulo, su ángulo *y* su velocidad angular: sólo el
ángulo no basta, porque el péndulo puede estar en el mismo sitio subiendo o
bajando.

Elegir el estado es una decisión de modelado, no un dato del problema, y tiene
consecuencias inmediatas:

* Si el estado es un número, el sistema es unidimensional y **no puede
  oscilar** (lo demostraremos en 4.4).
* Si necesitas dos números, ya puedes tener oscilaciones.
* Si necesitas tres, puede haber caos (capítulo 7).

Fíjate en lo que acabamos de hacer: hemos deducido restricciones fuertes sobre
el comportamiento posible **antes de escribir ninguna ecuación concreta**, sólo
contando cuántos números hacen falta. Es el mismo tipo de razonamiento que el
teorema π.

### 3.3 Los cuatro modelos que explican medio mundo

![Los cuatro modelos básicos. Arriba: la línea de fases, es decir, $\dot x$ frente a $x$, con los puntos fijos y el sentido del flujo. Abajo: las soluciones. Lo que hay que concluir: la línea de fases se dibuja sin resolver nada y ya contiene todo el comportamiento cualitativo.](figuras/fig_cuatro_modelos.pdf)

**Relajación**, $\dot x=-x/\tau$. Todo lo que decae hacia un equilibrio:
temperatura, carga, concentración de un fármaco, deformación de un material
viscoelástico. Un solo punto fijo, estable, y una única escala de tiempo.

**Crecimiento**, $\dot x=rx$. Todo lo que se realimenta positivamente:
poblaciones sin límite, interés compuesto, reacciones en cadena, epidemias en
su fase inicial. El punto fijo en el origen es inestable, y por eso el sistema
se va.

**Saturación**, $\dot x=rx(1-x/K)$. Crecimiento con un recurso limitado. Dos
puntos fijos: el origen, inestable, y $K$, estable. Es el modelo mínimo de
«algo crece hasta que se queda sin sitio».

**Oscilación**, $\ddot x=-\omega^2x$. Necesita dos números de estado. Aquí no
hay línea de fases sino plano de fases, y las trayectorias son curvas cerradas
porque hay una cantidad conservada.

Con estos cuatro y sus combinaciones se modela una fracción sorprendentemente
grande de la realidad. No porque el mundo sea simple, sino porque **cerca de un
equilibrio casi todo se comporta igual**, y eso lo justificaremos en el
capítulo 13.

---

## 4. La matemática

### 4.1 De un enunciado verbal a una ecuación

Hagamos el café en serio. Enunciado: *un cuerpo pierde calor hacia el ambiente
a un ritmo proporcional a su exceso de temperatura*.

Balance de energía: la energía que sale por unidad de tiempo es la que pierde
el cuerpo.

$$mc\frac{dT}{dt}=-hA\,(T-T_{\text{amb}})$$

con $m$ la masa, $c$ el calor específico, $h$ el coeficiente de transferencia y
$A$ la superficie. Reagrupando y definiendo $\theta=T-T_{\text{amb}}$:

$$\frac{d\theta}{dt}=-\frac{\theta}{\tau},\qquad \tau=\frac{mc}{hA}$$

Comprobación dimensional: $[mc]=$ J/K, $[hA]=$ W/K, luego $[\tau]=$ s. Bien.

Y aquí está lo importante, que no es la solución: **el tiempo característico
tiene significado físico y se puede estimar antes de medir nada**. $\tau$ es
grande si hay mucha masa que enfriar y pequeño si hay mucha superficie por la
que perder. Por eso una taza grande se enfría más despacio que una pequeña, por
eso los animales pequeños tienen problemas para mantener la temperatura, y por
eso los radiadores tienen aletas.

::: herramientas
**Resolver $\dot x = a - bx$ de memoria**

Casi todo modelo lineal de primer orden tiene esta forma: un aporte constante y
una pérdida proporcional. La solución se escribe sin calcular nada si
identificas dos cosas:

* el **equilibrio**, $x_\infty = a/b$ (donde $\dot x=0$);
* el **tiempo característico**, $\tau = 1/b$.

Entonces
$$x(t)=x_\infty+(x_0-x_\infty)e^{-t/\tau}$$

Léelo: *el sistema va del sitio donde está al sitio donde acabará, y tarda unos
pocos $\tau$*. Con $t=\tau$ ha recorrido el 63 % del camino; con $3\tau$, el
95 %; con $5\tau$, el 99,3 %.
:::

### 4.2 El tiempo característico como herramienta de decisión

$\tau$ no es un parámetro más: es la unidad natural del problema, y sirve para
decidir qué se puede ignorar.

* Si observas el sistema durante $t\ll\tau$, apenas cambia: puedes tratarlo
  como constante.
* Si lo observas durante $t\gg\tau$, ya ha llegado al equilibrio: puedes
  ignorar el transitorio.
* Sólo cuando $t\sim\tau$ hay que resolver de verdad.

Y cuando hay **varios** tiempos característicos, la comparación entre ellos
decide el modelo.

![Un sistema con dos relojes muy distintos. Izquierda: en la escala rápida, A desaparece y B se acumula; C ni se entera. Derecha: en la escala lenta, A ya no existe y el sistema es efectivamente B → C. Lo que hay que concluir: la variable rápida se puede eliminar del modelo, y eso reduce su dimensión.](figuras/fig_escalas_temporales.pdf)

En el ejemplo, $k_1=30$ s⁻¹ y $k_2=0{,}5$ s⁻¹: sesenta veces distintos. Después
de unas décimas de segundo, la especie A ha desaparecido y el sistema completo
se comporta como si sólo existieran B y C. **Se puede tachar una variable del
modelo.**

Este es el origen de la *aproximación de estado cuasi-estacionario* de la
cinética química, de la eliminación adiabática en física, de los modelos
reducidos en control, y en general de una de las técnicas más rentables del
modelado: cuando hay separación de escalas, la variable rápida se convierte en
una función algebraica de las lentas. El capítulo 13 lo formaliza.

### 4.3 Adimensionalizar: pagando la deuda del capítulo 2

Tomemos la ecuación logística completa:

$$\frac{dN}{dt}=rN\left(1-\frac{N}{K}\right),\qquad N(0)=N_0$$

Tres parámetros ($r$, $K$, $N_0$). Definamos $u=N/K$ y $s=rt$:

$$\frac{du}{ds}=u(1-u),\qquad u(0)=N_0/K$$

**Han desaparecido dos parámetros.** Sólo queda la condición inicial
adimensional. Cualquier población logística del universo —bacterias, conejos,
usuarios de una red social— sigue esta misma curva; lo único que cambia es cómo
se estira en los dos ejes.

Consecuencia práctica inmediata: si vas a hacer un barrido de parámetros para
estudiar el comportamiento, **hacerlo en $r$ y $K$ es tirar el tiempo**. Todos
esos casos son el mismo caso. Volveremos a insistir en el capítulo 16.

### 4.4 Equilibrio, estabilidad y por qué un sistema 1D no oscila

Un **punto fijo** $x^*$ cumple $f(x^*)=0$. Para saber si es estable,
linealizamos: sea $x=x^*+\eta$ con $\eta$ pequeño. Entonces

$$\dot\eta=f(x^*+\eta)\approx f(x^*)+f'(x^*)\eta=f'(x^*)\,\eta$$

luego $\eta(t)=\eta_0e^{f'(x^*)t}$ y el criterio es inmediato:

$$f'(x^*)<0 \Rightarrow \textbf{estable};\qquad f'(x^*)>0 \Rightarrow \textbf{inestable}$$

La magnitud $|f'(x^*)|$ es el inverso del tiempo característico local: dice no
sólo si vuelve, sino **cuánto tarda en volver**.

Y ahora el resultado que anunciamos en 3.2. En una dimensión, $x(t)$ se mueve a
lo largo de una recta y su velocidad está determinada por su posición. Para
oscilar, tendría que volver a un punto por el que ya pasó, y al llegar allí su
velocidad sería la misma que la primera vez, con el mismo signo: seguiría de
largo. **Un sistema autónomo unidimensional no puede oscilar.** Nunca. Si tu
modelo de una variable produce oscilaciones, o no es autónomo (depende
explícitamente del tiempo), o tiene un retardo, o hay un error.

Es un teorema barato y potentísimo: descarta modelos enteros antes de
resolverlos.

### 4.5 Sistemas acoplados: cuando dos cosas se hablan

Casi nada está solo. El patrón general es

$$\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x}),\qquad \mathbf{x}\in\mathbb{R}^n$$

y el ejemplo canónico es el de depredador y presa.

![Lotka–Volterra. Izquierda: las poblaciones oscilan con las presas por delante. Derecha: el retrato de fases, con el campo de direcciones y órbitas cerradas alrededor del punto fijo. Lo que hay que concluir: las órbitas son cerradas porque existe una cantidad conservada; el modelo no tiene amortiguamiento y eso es a la vez su gracia y su defecto.](figuras/fig_lotka_volterra.pdf)

$$\dot P=\alpha P-\beta PD,\qquad \dot D=\delta PD-\gamma D$$

Lo interesante no es la solución sino lo que se lee **sin** resolver:

* El punto fijo de coexistencia está en $P^*=\gamma/\delta$, $D^*=\alpha/\beta$.
  Fíjate: **la población de presas en equilibrio no depende de los parámetros
  de las presas**, sino de los del depredador, y viceversa. Es contraintuitivo
  y es una predicción falsable.
* De ahí sale el **principio de Volterra**: si matas indiscriminadamente a
  ambas especies (aumentando $\gamma$ y reduciendo $\alpha$), el nivel medio de
  presas **baja** y el de depredadores también, pero si sólo reduces la
  mortalidad general, el promedio de presas **sube**. Es la explicación del
  fenómeno que motivó el modelo, y lo contamos en la sección 7.

::: aviso
**El patrón de compartimentos.** Una enorme familia de modelos —farmacocinética,
epidemias, ecología, transferencia de calor, contabilidad de carbono— tiene la
misma forma: cajas con contenido, flechas con flujos entre ellas.

$$\frac{dx_i}{dt}=\sum_{j}\big(\text{entra de } j\big)-\sum_j\big(\text{sale hacia } j\big)$$

Si los flujos son proporcionales al contenido de la caja de origen, el sistema
es **lineal** y se resuelve con autovalores (capítulo 11). Si dependen del
producto de dos contenidos —como $\beta SI$ en epidemias o $\beta PD$ aquí— es
**no lineal** y hay que trabajar. Reconocer a qué familia pertenece tu problema
ahorra semanas.
:::

### 4.6 Conservación: la primera integral

En Lotka–Volterra, dividiendo las dos ecuaciones y separando variables se
obtiene

$$V(P,D)=\delta P-\gamma\ln P+\beta D-\alpha\ln D=\text{const}$$

Esa cantidad se conserva a lo largo de cada trayectoria, y **por eso las
órbitas son cerradas**. Una cantidad conservada en un sistema de dos variables
reduce la dinámica a una curva de nivel: has bajado la dimensión efectiva de 2
a 1.

Buscar cantidades conservadas antes de integrar numéricamente es un hábito
excelente por dos razones. Primero, porque a veces resuelve el problema.
Segundo, porque **te da un test de tu código**: si tu integrador no conserva lo
que debería conservar, tienes un error numérico y no un descubrimiento. El
capítulo 8 explota esto sin piedad.

---

## 5. El ordenador entra en escena

::: antes
Vamos a integrar la ecuación logística y Lotka–Volterra. Antes de ejecutar:

* En la logística con $u_0=0{,}02$, ¿cuánto tarda en llegar a la mitad de la
  capacidad? ¿Depende de $u_0$ igual que $\tau$ dependía de $T_0$ en el café?
* En Lotka–Volterra, ¿qué pasa si empiezas exactamente en el punto fijo?
* Si aumentas $\alpha$ (las presas se reproducen más), ¿sube la población media
  de presas?
:::

```python
import numpy as np
from scipy.integrate import solve_ivp

alfa, beta, gamma, delta = 1.1, 0.4, 0.4, 0.1

def lotka_volterra(t, y):
    presa, depredador = y
    return [alfa * presa - beta * presa * depredador,
            delta * presa * depredador - gamma * depredador]

sol = solve_ivp(lotka_volterra, (0, 60), [10, 5], dense_output=True, rtol=1e-10)
```

La respuesta a la tercera pregunta es **no**: aumentar $\alpha$ sube la
población media de *depredadores* ($D^*=\alpha/\beta$) y deja la de presas
intacta. Es exactamente el tipo de resultado que un modelo mínimo aporta y que
la intuición no da.

::: juega
1. Empieza exactamente en el punto fijo. ¿Qué pasa? ¿Y si te desvías un 1 %?
2. Añade saturación a las presas: $\alpha P(1-P/K)$. ¿Siguen siendo cerradas las
   órbitas? ¿Qué ha cambiado cualitativamente?
3. Integra durante 10 000 unidades de tiempo con `rtol=1e-3`. Dibuja $V(P,D)$
   frente al tiempo. ¿Se conserva? ¿Qué acabas de descubrir sobre tu
   integrador?
4. Sustituye la logística por $\dot u = u(1-u)-h$, una cosecha constante.
   ¿Cuántos puntos fijos hay? ¿Qué pasa cuando $h$ pasa de 1/4?
:::

---

## 6. ¿Qué estamos suponiendo?

::: supuestos
1. **Que el estado es completo.** Que esas variables bastan para predecir el
   futuro. Si falta una (una temperatura interna, una clase de edad, una
   memoria del sistema), el modelo falla de formas difíciles de diagnosticar.
2. **Que el sistema es autónomo.** Que $f$ no depende explícitamente del
   tiempo. Falso en cuanto hay ciclo día-noche, estacionalidad o
   envejecimiento.
3. **Que no hay retardos.** La respuesta es instantánea. Falso en biología, en
   control y en economía, y el capítulo 7 muestra que un retardo puede
   desestabilizar un sistema perfectamente estable.
4. **Que las variables son continuas.** Con 3 individuos, hablar de $dN/dt$ es
   una ficción; hace falta un modelo estocástico (capítulos 4 y 9).
5. **Que los parámetros son constantes.** $h$ en el café depende de la
   temperatura y del movimiento del aire; $\tau$ constante ya es una
   aproximación.
6. **Que el sistema está bien mezclado.** No hay gradientes espaciales. Si los
   hay, esto deja de ser una EDO y se convierte en una EDP (capítulos 8 y 12).
:::

---

## 7. ¿Cuándo falla?

::: falla
**Falla la ley de Newton del enfriamiento cuando el salto térmico es grande.**
La radiación va como $T^4$, no como $T$. Con $\Delta T\lesssim30$ K la
linealización es buena; con una pieza al rojo, no. Además $h$ depende de si la
convección es natural o forzada, y en convección natural $h\propto\Delta
T^{1/4}$, con lo que la ecuación deja de ser lineal. El capítulo II.2 lo mide.

**Falla el modelo unidimensional cuando el objeto no está a temperatura
uniforme.** El criterio es el número de Biot del capítulo 2: si $Bi\gtrsim0{,}1$
hay gradientes internos y una sola temperatura no describe la taza.

**Falla Lotka–Volterra de manera espectacular.** Las órbitas cerradas son
**estructuralmente inestables**: cualquier perturbación del modelo —saturación,
un tercer depredador, ruido— destruye la conservación y convierte las órbitas
en espirales que entran o salen. Un modelo cuyo comportamiento cualitativo se
destruye con la más mínima modificación es un modelo del que hay que
desconfiar, por bonito que sea.

**Falla el continuo cuando quedan pocos individuos.** La logística predice que
una población nunca se extingue, sólo se acerca a cero asintóticamente. En un
modelo estocástico con 3 individuos, la extinción ocurre y es frecuente.
:::

### Un anti-ejemplo: el ajuste exponencial que no significaba nada

En la fase inicial de una epidemia, los casos acumulados se ajustan
estupendamente a una exponencial y el ajuste da una tasa $r$ con barras de
error pequeñísimas. La tentación es extrapolar.

El problema no es el ajuste, que es correcto. Es que **el mismo dato es
compatible con muchísimos modelos** que divergen justo después: exponencial
pura, logística en su fase inicial, ley de potencias con exponente alto,
exponencial con $r$ decreciente. Los cuatro coinciden en los datos disponibles
y predicen cosas radicalmente distintas dos semanas después.

La conclusión no es «no ajustes exponenciales». Es que **en la zona donde todos
los modelos coinciden, los datos no seleccionan modelo**, y por tanto la
extrapolación depende íntegramente de la física que hayas puesto tú. Capítulo
15.

---

## 8. Historia

::: historia
**Newton, el enfriamiento y una ley que no es del todo suya** ·
*Nivel de verificación: A, con matiz.*

En 1701, Isaac Newton publicó de forma anónima en las *Philosophical
Transactions* un artículo titulado *Scala graduum caloris* («escala de los
grados de calor»), donde describía cómo construir una escala de temperaturas
usando el enfriamiento de un hierro caliente.

El matiz: lo que hoy llamamos «ley de Newton del enfriamiento» aparece allí
como una observación empírica sobre un montaje concreto, no como la ley general
que enseñamos. Y estrictamente **no es una ley**: es la aproximación lineal de
un fenómeno de transporte que incluye conducción, convección y radiación, cada
una con su propia dependencia con $\Delta T$. Que funcione tan bien en la
práctica se debe a que casi siempre trabajamos con saltos térmicos pequeños,
donde toda función suave es lineal.

Es un buen ejemplo de algo que se repetirá: **muchas «leyes» son la
linealización de algo más complicado alrededor del régimen en el que solemos
vivir.**

**Euler convirtiendo fenómenos en ecuaciones** · *Nivel de verificación: A.*

En *Institutionum calculi integralis* (1768–1770), Leonhard Euler expuso el
método que hoy lleva su nombre para integrar ecuaciones diferenciales paso a
paso. Pero su contribución mayor fue anterior y más profunda: fue quien
sistemáticamente **tradujo problemas físicos a ecuaciones diferenciales**
—vigas, fluidos, cuerdas vibrantes, mecánica de sólidos— y estableció que ese
era el lenguaje en el que se escribe la física.

Antes de Euler, la mecánica se hacía con geometría a la manera de Newton.
Después de Euler, se hace con ecuaciones. El cambio de lenguaje fue más
importante que cualquier resultado concreto.

**Volterra, su yerno y los peces del Adriático** ·
*Nivel de verificación: A.*

En 1926, el biólogo Umberto D'Ancona presentó a su suegro, el matemático Vito
Volterra, un dato desconcertante. Durante la Primera Guerra Mundial la pesca en
el Adriático se había reducido drásticamente, y sin embargo la **proporción de
peces depredadores** en las capturas había *aumentado*. Al reanudarse la pesca
intensiva, volvió a bajar.

Menos pesca debería beneficiar a todos por igual, así que ¿por qué la pesca
favorecía relativamente a las presas?

Volterra construyó el modelo de dos ecuaciones y demostró que la población
media de presas en un ciclo es $\gamma/\delta$ y la de depredadores
$\alpha/\beta$. Una pesca uniforme reduce $\alpha$ y aumenta $\gamma$, lo que
**sube la media de presas y baja la de depredadores**. El dato de D'Ancona no
era una anomalía: era una predicción del modelo.

Alfred Lotka había publicado ecuaciones equivalentes en 1920 en un contexto de
cinética química autocatalítica, sin conexión con la ecología. Es otro
descubrimiento múltiple, y otro caso de la misma estructura matemática
apareciendo en dos dominios sin relación.

El principio de Volterra tiene consecuencias prácticas incómodas y bien
documentadas: aplicar un insecticida de amplio espectro puede **aumentar** la
población de la plaga a medio plazo, porque mata también a sus depredadores. Es
un modelo de dos ecuaciones prediciendo un fracaso agronómico real.
:::

---

## 9. Problemas

En `problemas.md`; soluciones en `soluciones.md`.

---

## 10. Experimento computacional

::: experimento
**Mide el $\tau$ de tu casa.**

*Pregunta:* ¿cuál es el tiempo característico de enfriamiento de tu vivienda?

*Diseño.* Apaga la calefacción con la casa a 22 °C y una noche fría fuera.
Registra la temperatura interior cada 15 minutos durante cuatro o cinco horas
(el móvil o un termómetro barato bastan). Anota también la temperatura
exterior, que **no será constante**: eso ya es una violación del supuesto 2.

*Análisis.* Ajusta $\dot\theta=-\theta/\tau$ y obtén $\tau$. Después estima
$\tau$ *a priori* con $\tau=mc/(hA)$: masa de aire más masa térmica de paredes
y muebles, superficie de la envolvente, y un $h$ efectivo del orden de
1 W/(m²·K) para una vivienda razonablemente aislada.

*Qué falsaría el modelo:* si los residuos tienen estructura, el modelo de una
sola temperatura está mal. Y lo estará: una casa tiene al menos dos masas
térmicas con constantes muy distintas (el aire, rápido; los muros, lentos),
así que verás **dos exponenciales**. Detectarlas es el verdadero objetivo del
ejercicio, y es el mismo fenómeno de la figura de escalas temporales.
:::

---

## 11. Explícalo

::: explica
1. ¿Qué significa físicamente $\dot x = f(x)$, en una frase, sin usar la
   palabra «derivada»?
2. ¿Por qué el tiempo característico del café no depende de lo caliente que
   estuviera al principio?
3. Explica por qué un sistema de una sola variable no puede oscilar, usando
   sólo la línea de fases.
4. ¿Qué significa que una variable sea «rápida» y por qué eso permite tacharla
   del modelo?
5. Explica el principio de Volterra a alguien que quiere fumigar su huerto.
6. ¿Por qué un modelo cuyas órbitas cerradas se destruyen con cualquier
   perturbación es sospechoso?
:::

---

## 12. Lo esencial

::: esencial
* $\dot x=f(x,t)$ significa «dime dónde estás y te digo hacia dónde vas». Es
  una regla local que genera la trayectoria; no la contiene.
* El estado es la información mínima que determina el futuro, y elegirlo es una
  decisión de modelado. Su dimensión limita el comportamiento posible: 1 no
  oscila, 2 puede oscilar, 3 puede ser caótico.
* Cuatro modelos —relajación, crecimiento, saturación, oscilación— cubren una
  fracción enorme de la realidad.
* La línea de fases se dibuja sin resolver nada y contiene todo el
  comportamiento cualitativo. Dibújala siempre primero.
* $\tau$ es la unidad natural del problema y sirve para decidir qué ignorar. Con
  varios $\tau$ muy distintos, la variable rápida se elimina.
* Adimensionalizar reduce parámetros: la logística tiene tres y en realidad
  uno.
* Estabilidad en 1D: el signo de $f'(x^*)$, y su magnitud es $1/\tau$ local.
* Busca cantidades conservadas antes de integrar: a veces resuelven el
  problema y siempre sirven para comprobar el código.
:::

---

## 13. Preguntas que quedan abiertas

::: abierto
* ¿Cómo se sabe si el estado que has elegido es completo, sin conocer la
  respuesta correcta?
* Si un sistema con retardo puede oscilar aunque tenga una sola variable, ¿en
  qué sentido «es» unidimensional?
* Las órbitas de Lotka–Volterra son estructuralmente inestables. ¿Qué modelos
  ecológicos sí son robustos, y qué los hace robustos?
* ¿Cuándo es legítimo eliminar una variable rápida, y qué error se comete al
  hacerlo? (Capítulo 13.)
* Si casi todo lo que observamos está cerca de un equilibrio, ¿estamos viendo
  el mundo o estamos viendo su linealización?
:::
