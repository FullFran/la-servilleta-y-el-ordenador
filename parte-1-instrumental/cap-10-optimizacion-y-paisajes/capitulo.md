# Capítulo 10 — Optimización y paisajes

> **Qué sabrás hacer al terminar**
> · Reconocer que casi todo es una optimización disfrazada ·
> Diagnosticar un problema mirando su paisaje de coste ·
> Saber cuándo merece la pena la curvatura y cuándo el gradiente basta ·
> Usar la temperatura como herramienta de exploración ·
> Detectar en el paisaje que un parámetro no es identificable.
>
> **Herramientas que usa:** capítulos 3, 5, 6 y 9.
> **Disciplinas de los ejemplos:** física estadística, logística, ajuste de
> modelos, diseño de ingeniería, aprendizaje automático.
> **Deuda que paga:** el ajuste del capítulo 5, ahora visto como paisaje.
> **Deuda que abre:** el condicionamiento (capítulo 11) y la identificabilidad
> en serio (capítulo 15).

---

## 1. Una pregunta

::: pregunta
Un algoritmo de ajuste devuelve $\tau_1=1{,}03$ y $\tau_2=1{,}12$ con barras de
error del 2 %. Lo ejecutas otra vez cambiando el punto de partida y devuelve
$\tau_1=0{,}71$ y $\tau_2=1{,}54$, también con barras del 2 %.

**¿Cuál de los dos resultados es el bueno?**
:::

Ninguno. Y el problema no está en el algoritmo, que ha hecho su trabajo
correctamente en los dos casos. Está en la forma del paisaje que le has pedido
que recorra. Este capítulo trata de mirar ese paisaje **antes** de lanzar el
optimizador, porque la mayoría de los fracasos de optimización se diagnostican
en treinta segundos si sabes qué mirar.

---

## 2. Antes de calcular

::: antes
1. Si duplicas la dimensión de un problema de optimización, ¿cuánto más difícil
   se vuelve? ¿Depende de algo?
2. ¿Por qué un algoritmo que a veces acepta empeorar puede acabar encontrando
   soluciones mejores que uno que nunca lo hace?
3. ¿Qué diferencia hay entre «no encuentro el mínimo» y «no hay un mínimo que
   encontrar»?
:::

---

## 3. La intuición

### 3.1 Casi todo es una optimización disfrazada

| Lo que parece | Lo que es |
|---|---|
| Ajustar un modelo a datos | minimizar $\chi^2(\theta)$ |
| Un sistema mecánico en equilibrio | minimizar la energía potencial |
| Un rayo de luz refractándose | minimizar el tiempo de recorrido (Fermat) |
| Una trayectoria clásica | estacionarizar la acción |
| Un cristal formándose | minimizar la energía libre |
| Una ruta de reparto | minimizar la distancia total |
| Entrenar una red neuronal | minimizar una pérdida |
| Inferencia bayesiana | maximizar (o muestrear) la posterior |

Que tantas cosas distintas tengan la misma forma matemática es exactamente la
tesis de la Parte II del libro. Y significa que las herramientas de este
capítulo se transfieren íntegras entre disciplinas.

### 3.2 El paisaje como objeto de estudio

Un problema de optimización es una **función objetivo** $f:\mathbb{R}^n\to
\mathbb{R}$ y la pregunta «¿dónde está su mínimo?». Pero la pregunta útil, la
que decide si el problema es fácil o imposible, es otra: **¿qué forma tiene el
paisaje?**

![Tres paisajes y el mismo algoritmo. Izquierda: convexo y bien condicionado, converge desde cualquier sitio. Centro: convexo pero alargado, el gradiente zigzaguea. Derecha: rugoso, cada punto de partida acaba en un sitio distinto. Lo que hay que concluir: el algoritmo no es el problema; el paisaje sí.](figuras/fig_paisajes.pdf)

Tres propiedades del paisaje deciden casi todo:

**Convexidad.** Si el paisaje es convexo, hay un único mínimo y cualquier
método razonable lo encuentra. Si no lo es, no hay garantías de nada. La
frontera convexo/no convexo es **la** frontera entre fácil y difícil en
optimización, mucho más que la dimensión.

**Condicionamiento.** El cociente entre la curvatura máxima y la mínima,
$\kappa=\lambda_{\max}/\lambda_{\min}$ del hessiano. Con $\kappa$ grande el
paisaje es un cañón estrecho: el gradiente apunta hacia las paredes y no hacia
el fondo, y el descenso zigzaguea. En el panel central, $\kappa=50$ y ya se ve.

**Rugosidad.** Cuántos mínimos locales hay y cómo de profundas son las
barreras entre ellos. Aquí el gradiente es inútil por sí solo.

---

## 4. La matemática

### 4.1 Condiciones de optimalidad

En un mínimo interior, $\nabla f=0$ y el hessiano $H$ es semidefinido positivo.
Los autovalores de $H$ dicen qué clase de punto es:

* todos positivos → mínimo local;
* todos negativos → máximo local;
* mixtos → **punto de silla**;
* alguno nulo → dirección plana, y la segunda derivada no decide.

En dimensión alta, los puntos de silla son **muchísimo más abundantes** que los
mínimos locales. Si los signos de los $n$ autovalores fueran independientes, la
probabilidad de que todos sean positivos es $2^{-n}$. En dimensión 100, un
punto crítico al azar es un mínimo con probabilidad $10^{-30}$.

Esta observación cambió la intuición de la comunidad de optimización en la
última década: en problemas de dimensión alta, el enemigo no son los mínimos
locales sino **las mesetas alrededor de los puntos de silla**, donde el
gradiente es pequeño y el progreso se detiene sin que haya nada que impida
seguir bajando.

### 4.2 Gradiente, Newton y por qué la curvatura compensa

**Descenso por gradiente:** $x_{k+1}=x_k-\alpha\nabla f(x_k)$. Convergencia
lineal, con una tasa que depende del condicionamiento:

$$\frac{\|x_{k+1}-x^*\|}{\|x_k-x^*\|}\approx\frac{\kappa-1}{\kappa+1}$$

Con $\kappa=1$ converge en un paso; con $\kappa=1000$, la tasa es 0,998 y hacen
falta miles de iteraciones. **El condicionamiento no cambia el número de
operaciones por paso: cambia el número de pasos, y por eso duele tanto.**

**Newton:** $x_{k+1}=x_k-H^{-1}\nabla f$. Usa la curvatura para ir directamente
al mínimo del modelo cuadrático local. Convergencia **cuadrática**: el número
de cifras correctas se duplica en cada paso. Coste: calcular y resolver con $H$,
que es $\mathcal{O}(n^3)$.

**Cuasi-Newton (BFGS):** construye una aproximación de $H^{-1}$ a partir de los
gradientes que ya has calculado. Convergencia superlineal por el precio de un
gradiente.

![Los tres métodos sobre la función de Rosenbrock. Izquierda: las trayectorias en el valle. Derecha: la distancia al mínimo. Lo que hay que concluir: 20 000 pasos de gradiente, 32 de BFGS, 22 de Newton. La curvatura no es un lujo.](figuras/fig_gradiente_newton.pdf)

Los números son elocuentes: gradiente con paso fijo necesita 20 000
iteraciones para llegar a $6\times10^{-6}$; Newton con búsqueda de línea llega a
precisión de máquina en 22.

::: aviso
**¿Y entonces por qué el aprendizaje automático usa descenso por gradiente?**

Por tres razones que no se aplican a los problemas de este capítulo:

1. **$n$ es enorme.** Con $10^9$ parámetros, $H$ tiene $10^{18}$ elementos.
   No cabe.
2. **La función objetivo es una suma sobre datos** y se puede estimar el
   gradiente con un lote pequeño. Eso es descenso estocástico, y su coste por
   paso es minúsculo.
3. **El ruido del gradiente estocástico ayuda**: escapa de mesetas y sillas, y
   parece favorecer mínimos anchos, que generalizan mejor.

En un ajuste de 5 parámetros a 200 datos, usar SGD en lugar de Levenberg–
Marquardt es un error. **La elección del optimizador depende del régimen, no de
la moda.**
:::

### 4.3 Convexidad: la frontera real

Una función es convexa si su hessiano es semidefinido positivo en todo el
dominio, o equivalentemente si el segmento entre dos puntos del grafo queda por
encima de la función. Sus dos propiedades milagrosas:

* **Todo mínimo local es global.**
* **Existen algoritmos con garantías de convergencia en tiempo polinómico.**

Boyd y Vandenberghe lo resumen de forma provocadora: la línea divisoria en
optimización no es lineal/no lineal, es **convexo/no convexo**. Un problema
convexo con $10^5$ variables se resuelve; uno no convexo con 50 puede ser
intratable.

De ahí una estrategia que conviene tener siempre presente: **antes de atacar
un problema no convexo, pregúntate si hay una reformulación convexa**.
Sustituir una norma $\ell_0$ por una $\ell_1$, relajar restricciones enteras,
cambiar de parametrización. Media investigación en optimización aplicada
consiste exactamente en eso.

### 4.4 Recocido simulado: física convertida en algoritmo

Si el paisaje es rugoso, el gradiente se atasca en el primer hoyo. La idea de
Kirkpatrick, Gelatt y Vecchi (1983) es tomar prestado el mecanismo con el que
la naturaleza resuelve el mismo problema: un metal que se enfría despacio
alcanza un estado de energía mucho menor que uno templado de golpe.

El algoritmo es **Metropolis del capítulo 9 con la energía como función
objetivo y una temperatura que baja**:

$$P(\text{aceptar un empeoramiento }\Delta E)=e^{-\Delta E/T}$$

![Recocido simulado. Izquierda: el paisaje, con las soluciones encontradas por cada estrategia. Derecha: las trayectorias. Lo que hay que concluir: demasiado frío se queda donde empezó; demasiado caliente nunca se posa; sólo enfriar funciona.](figuras/fig_recocido.pdf)

Los tres resultados dicen exactamente lo que hay que entender:

| Estrategia | Mejor energía encontrada |
|---|---|
| $T=10^{-4}$ (casi cero) | **+0,70** — atrapado donde empezó |
| $T=6$ (muy caliente) | −2,97 — la encuentra, pero no se posa |
| Enfriamiento exponencial | **−2,97** — la encuentra y se queda |

La temperatura es una **escala de energía de exploración**: dice cuánto estás
dispuesto a empeorar para poder mirar más lejos. Alta, exploras y no explotas;
baja, explotas y no exploras. Todo el algoritmo consiste en pasar de lo primero
a lo segundo con la lentitud adecuada.

Hay un teorema, de Geman y Geman (1984), que garantiza convergencia al óptimo
global si $T(k)\ge c/\log(1+k)$. Es una garantía **inútil en la práctica**: ese
enfriamiento logarítmico es tan lento que exige más iteraciones que la búsqueda
exhaustiva. En la práctica se usa enfriamiento geométrico, que no garantiza
nada y funciona muy bien. Es un ejemplo instructivo de que un resultado teórico
correcto puede ser irrelevante operativamente.

### 4.5 La conexión con la física estadística

La expresión $e^{-\Delta E/T}$ no es una analogía decorativa. La distribución de
Boltzmann $p(x)\propto e^{-E(x)/T}$ tiene una propiedad exacta:

* Cuando $T\to\infty$, $p$ es uniforme: todos los estados igual de probables.
* Cuando $T\to0$, $p$ se concentra en el **mínimo global** de $E$.

Es decir: **muestrear la distribución de Boltzmann a temperatura cero es
resolver el problema de optimización**. Y muestrear a temperaturas
intermedias es explorar de forma controlada.

Y funciona en el otro sentido, que es igual de útil: dada cualquier función
objetivo $f$, puedes definir $p(x)\propto e^{-f(x)/T}$ y aplicarle todo el
arsenal del capítulo 9. Optimizar y muestrear son la misma cosa vista con dos
temperaturas distintas, y esa equivalencia conecta este capítulo con el 3
(máxima entropía), el 9 (MCMC) y el II.9 (Ising).

### 4.6 El paisaje del ajuste te dice si tu parámetro existe

Volvamos a la pregunta del principio.

![Dos paisajes de $\chi^2$. Izquierda: un ajuste de una exponencial; el mínimo es un pozo y los contornos de confianza son elipses cerradas. Derecha: un ajuste de dos exponenciales con constantes parecidas; el mínimo es un valle largo. Lo que hay que concluir: en el valle, todos los puntos ajustan igual de bien, y por tanto el «resultado» del optimizador es el punto donde le dio por pararse.](figuras/fig_identificabilidad.pdf)

En el panel derecho, cualquier par $(\tau_1,\tau_2)$ a lo largo del valle
produce prácticamente el mismo $\chi^2$. Los datos **no contienen información**
para separar las dos constantes de tiempo. El optimizador convergerá a un punto
distinto según el arranque, la tolerancia y la aritmética, y la matriz de
covarianza dará barras pequeñas porque mide la curvatura local en una dirección
y no la longitud del valle.

Diagnóstico práctico, por orden de coste:

1. **Ejecuta desde varios puntos de partida.** Si el resultado cambia, ya lo
   sabes. Cuesta un minuto.
2. **Mira la correlación de la matriz de covarianza.** $|\rho|>0{,}95$ es una
   bandera roja.
3. **Calcula los autovalores del hessiano.** Si $\kappa>10^6$, hay direcciones
   sin determinar.
4. **Dibuja el perfil de verosimilitud**: fija un parámetro, reoptimiza los
   demás, repite. Es lo correcto y es lo que casi nadie hace. Capítulo 15.

---

## 5. El ordenador entra en escena

::: antes
Vamos a ajustar la suma de dos exponenciales. Antes de ejecutar:

* ¿Convergerá el optimizador?
* ¿Dará barras de error grandes o pequeñas?
* ¿Coincidirán los resultados desde puntos de partida distintos?
:::

```python
from scipy.optimize import curve_fit
import numpy as np

def modelo(t, A1, tau1, A2, tau2):
    return A1*np.exp(-t/tau1) + A2*np.exp(-t/tau2)

for p0 in [[1, 0.8, 1, 1.4], [1.5, 0.6, 0.5, 2.0], [0.7, 1.3, 1.3, 0.9]]:
    popt, pcov = curve_fit(modelo, t, y, p0=p0, maxfev=20000)
    print(np.round(popt, 3), " chi2 =", round(chi2(popt), 2))
```

Los tres arranques convergen —sin quejarse— a parámetros muy distintos y a
$\chi^2$ prácticamente idénticos. **El optimizador ha hecho su trabajo
perfectamente; el problema no tiene solución única.**

::: juega
1. Separa las dos constantes de tiempo un factor 5 en lugar de un 15 %.
   ¿Desaparece el valle?
2. Reduce el ruido de los datos por 10. ¿Se vuelve identificable? ¿Cuánto
   habría que reducirlo?
3. Alarga el rango temporal al triple. ¿Ayuda más que reducir el ruido?
4. Reparametriza con $\tau_{\text{media}}$ y $\Delta\tau$. ¿Cuál de los dos
   nuevos parámetros está bien determinado?
:::

El punto 3 y el 4 contienen la lección práctica: cuando un parámetro no es
identificable, hay tres salidas y sólo dos funcionan. **Mejorar los datos** en
la dirección adecuada (el punto 3), **reparametrizar** para separar lo que se
mide de lo que no (el punto 4), o añadir información externa (una previa, una
restricción física). Lo que no funciona es cambiar de optimizador.

---

## 6. ¿Qué estamos suponiendo?

::: supuestos
1. **Que la función objetivo es la correcta.** Optimizar bien la función
   equivocada es el fallo más caro y el menos discutido.
2. **Que $f$ es suave.** Newton y BFGS suponen dos derivadas continuas. Con una
   $f$ ruidosa o discontinua, el gradiente numérico es basura.
3. **Que el mínimo es interior.** Con restricciones activas, las condiciones
   cambian (KKT en lugar de $\nabla f=0$).
4. **Que el gradiente es exacto.** Si lo calculas por diferencias finitas,
   arrastra el compromiso del capítulo 8 y limita la precisión alcanzable.
5. **Que el óptimo tiene sentido.** En un valle plano, «el óptimo» es un
   artefacto de la aritmética.
6. **Que un óptimo mejor es una solución mejor.** En ajuste de modelos,
   bajar el $\chi^2$ añadiendo parámetros es sobreajuste, no mejora.
:::

---

## 7. ¿Cuándo falla?

::: falla
**Falla el gradiente con mal condicionamiento.** Con $\kappa=10^4$, el descenso
necesita del orden de $10^4$ iteraciones. Remedios: precondicionar, cambiar de
variables (adimensionalizar, capítulo 2), o usar curvatura.

**Falla Newton lejos del mínimo.** Si $H$ no es definido positivo, el paso de
Newton puede ir **cuesta arriba**. Por eso todo Newton práctico lleva búsqueda
de línea o región de confianza, y por eso el código de la figura comprueba el
signo de $d\cdot g$.

**Falla la optimización sin gradiente en dimensión alta.** Nelder–Mead es
cómodo y funciona hasta unas 10 dimensiones; a partir de ahí degenera. Los
métodos evolutivos y CMA-ES aguantan más, pero pagan un coste enorme en número
de evaluaciones. Si puedes calcular gradientes —y con diferenciación automática
casi siempre puedes— úsalos.

**Falla el recocido con el programa equivocado.** Demasiado rápido y es un
descenso codicioso caro; demasiado lento y es una búsqueda exhaustiva cara. El
diagnóstico es la tasa de aceptación: debería empezar cerca de 0,8 y terminar
cerca de 0.

**Y falla, silenciosamente, cuando el problema no es identificable.** El
optimizador converge, no da errores y devuelve números con barras pequeñas. Es
el fallo más peligroso porque **no parece un fallo**.
:::

### Un anti-ejemplo: el óptimo que empeoró el sistema

Un equipo optimiza la ruta de reparto de una flota minimizando kilómetros
totales. El algoritmo funciona: los kilómetros bajan un 12 %. Seis meses
después, los costes han subido.

Lo que pasó: la solución óptima en kilómetros concentraba las entregas en
ventanas horarias que obligaban a pagar horas extra, aumentaba el tiempo de
carga en almacén y era tan ajustada que cualquier incidencia propagaba retrasos
por toda la ruta. El objetivo minimizado no era el objetivo real, y la solución
óptima era **frágil**.

Dos lecciones que se repetirán en el capítulo 15. Primera: **la función
objetivo es un modelo, y como todo modelo es falsa**; optimizar agresivamente
una función objetivo aproximada explota precisamente sus errores. Segunda:
casi siempre interesa un óptimo **robusto** —un mínimo ancho— antes que uno
profundo y estrecho, y eso hay que ponerlo en la función objetivo
explícitamente, porque el optimizador no lo va a adivinar.

---

## 8. Historia

::: historia
**Kirkpatrick, Černý y una idea que estaba en el aire** ·
*Nivel de verificación: A.*

En 1983, Scott Kirkpatrick, C. Daniel Gelatt y Mario Vecchi publicaron en
*Science* *Optimization by Simulated Annealing*. Trabajaban en IBM en diseño
de circuitos: colocar componentes en un chip minimizando la longitud de las
conexiones, un problema combinatorio brutal.

La conexión que hicieron es exacta y no metafórica: el problema de colocación
tiene la misma estructura matemática que un vidrio de espín, y el algoritmo de
Metropolis con temperatura decreciente es literalmente lo que hace un metal al
recocerse.

Václav Černý, en Bratislava, llegó a la misma idea de forma independiente. Su
preprint es de 1982 y su publicación de 1985 en el *Journal of Optimization
Theory and Applications*. Otro descubrimiento múltiple, y otro caso donde el
crédito se reparte de forma desigual por razones de visibilidad de la revista
más que de prioridad.

**El principio variacional, que es mucho más antiguo** ·
*Nivel de verificación: A.*

La idea de que la naturaleza optimiza tiene tres siglos y medio. Fermat
formuló en 1662 que la luz sigue el camino de tiempo estacionario, y de ahí
dedujo la ley de refracción de Snell. Maupertuis propuso en 1744 el principio
de mínima acción, con una justificación teológica que Euler y Lagrange
reemplazaron enseguida por una matemática.

Feynman, en el capítulo 19 del volumen II de las *Lectures*, cuenta que fue
esa idea la que le enseñó su profesor Bader en el instituto y la que le
persiguió hasta desembocar en la formulación de integrales de camino. Merece
la pena leer ese capítulo: es el mejor argumento existente de que un cambio de
punto de vista sobre el mismo contenido puede abrir una física entera.

**Y una advertencia sobre optimizar** · *Nivel de verificación: A.*

En 1975, Charles Goodhart formuló una observación sobre política monetaria que
Marilyn Strathern condensó después en la forma en que se cita hoy: cuando una
medida se convierte en objetivo, deja de ser una buena medida.

Es la formulación social exacta del anti-ejemplo de la sección 7, y todo el que
optimice algo automáticamente debería tenerla escrita en la pared. En cuanto un
sistema —humano o algorítmico— empieza a optimizar una métrica, explota la
diferencia entre la métrica y lo que la métrica pretendía medir.
:::

---

## 9. Problemas

En `problemas.md`; soluciones en `soluciones.md`.

---

## 10. Experimento computacional

::: experimento
**Mide el paisaje antes de optimizarlo.**

*Pregunta:* ¿cómo es de rugoso el paisaje de un problema tuyo?

*Diseño.* Toma una función objetivo de tu trabajo (un ajuste, una calibración,
un diseño). Lanza 200 optimizaciones locales desde puntos de partida aleatorios
y guarda los óptimos encontrados.

*Análisis.* Dibuja el histograma de valores finales. Si es un único pico, el
paisaje es esencialmente convexo. Si hay varios, cuenta las cuencas. Dibuja
también el valor final frente a la distancia entre el punto de partida y el
óptimo global: si hay correlación, el paisaje tiene forma de embudo y el
recocido funcionará bien; si no la hay, es un paisaje rugoso sin estructura y
harán falta métodos poblacionales.

*Qué falsaría la conclusión de que es convexo:* un solo arranque que caiga en
otro sitio. Con 200 arranques y ninguno discrepante, puedes acotar la
probabilidad de otra cuenca grande, pero **nunca** demostrar que no existe. Esa
asimetría es la de todo el capítulo 15.
:::

---

## 11. Explícalo

::: explica
1. ¿Por qué el descenso por gradiente zigzaguea en un valle estrecho? Explícalo
   con la imagen de una bola en una canaleta.
2. ¿Por qué aceptar empeoramientos puede llevar a soluciones mejores?
3. ¿Qué relación exacta hay entre la temperatura de un metal y un algoritmo de
   optimización?
4. ¿Cómo se ve en el paisaje que un parámetro no se puede determinar?
5. ¿Por qué en dimensión alta hay muchos más puntos de silla que mínimos?
6. ¿Qué le dirías a alguien que ha bajado su función objetivo un 20 % añadiendo
   cinco parámetros?
:::

---

## 12. Lo esencial

::: esencial
* Casi todo problema científico es una optimización disfrazada, y por eso estas
  herramientas se transfieren entre disciplinas.
* Mira el paisaje antes de elegir el algoritmo. Tres propiedades deciden:
  convexidad, condicionamiento y rugosidad.
* La frontera fácil/difícil es **convexo / no convexo**, no lineal / no lineal
  ni baja / alta dimensión.
* El condicionamiento no cambia el coste por paso: cambia el número de pasos.
  Adimensionalizar es precondicionar.
* La curvatura compensa: 20 000 pasos de gradiente frente a 22 de Newton.
* La temperatura es una escala de exploración. Muestrear a $T\to0$ **es**
  optimizar; optimizar y muestrear son la misma cosa a dos temperaturas.
* Si el paisaje tiene un valle plano, el «resultado» del optimizador es donde
  le dio por pararse. Diagnostica con arranques múltiples y perfiles de
  verosimilitud.
* Optimizar agresivamente una función objetivo aproximada explota sus errores.
  Ley de Goodhart.
:::

---

## 13. Preguntas que quedan abiertas

::: abierto
* ¿Se puede saber si un paisaje es convexo sin explorarlo entero?
* ¿Por qué el ruido del gradiente estocástico parece encontrar mínimos que
  generalizan mejor? ¿Es un efecto de regularización implícita o algo más?
* Si el enfriamiento que garantiza convergencia es inútil en la práctica,
  ¿qué garantías tiene lo que realmente usamos?
* ¿Cómo se formula «quiero un óptimo robusto» dentro de la propia función
  objetivo?
* ¿Existe una forma sistemática de detectar que estás optimizando la métrica
  equivocada, antes de que las consecuencias aparezcan?
:::
