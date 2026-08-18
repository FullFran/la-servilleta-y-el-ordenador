# Capítulo 13 — Escalas, aproximaciones y perturbaciones

> **Qué sabrás hacer al terminar**
> · Decidir con un número hasta dónde vale una aproximación ·
> Identificar el término dominante y justificar por escrito lo que desprecias ·
> Distinguir una perturbación regular de una singular, y saber qué hacer ·
> Usar una serie divergente sin equivocarte.
>
> **Herramientas que usa:** capítulos 1, 2, 6, 8 y 11.
> **Disciplinas de los ejemplos:** mecánica, fluidos, cinética química,
> óptica, ingeniería de control.
> **Deuda que paga:** el «¿qué podemos ignorar?» que ha aparecido en todos los
> capítulos anteriores.

---

## 1. Una pregunta

::: pregunta
En el capítulo 2 escribimos, sin pestañear, «para ángulos pequeños,
$\sin\theta\approx\theta$».

**¿Cuánto de pequeño es pequeño? ¿Diez grados? ¿Treinta? ¿Y si necesito un
1 % de precisión?**
:::

La habilidad que este capítulo entrena no es aproximar: eso lo hace todo el
mundo. Es **saber cuándo la aproximación deja de valer y por cuánto**, es decir,
convertir «pequeño» en un número.

Y hay algo más incómodo. A veces el término pequeño **es el que manda**, y
despreciarlo no introduce un error pequeño: destruye la solución. Reconocer esa
situación es probablemente lo más valioso del capítulo.

---

## 2. Antes de calcular

::: antes
1. ¿Hasta qué ángulo vale $\sin\theta\approx\theta$ con un error del 1 %?
   Apunta un número.
2. Si una serie diverge, ¿puede servir para calcular algo con precisión?
3. La ecuación $\epsilon x^2+x-1=0$ tiene dos raíces. Al hacer $\epsilon=0$
   queda $x=1$. ¿Dónde ha ido la otra?
:::

---

## 3. La intuición

### 3.1 Aproximar es una decisión, y hay que justificarla

Todo modelo es una aproximación, y en cada capítulo anterior hemos despreciado
cosas: la radiación frente a la convección, la energía cinética frente al calor
latente, la viscosidad a Reynolds alto. En cada caso hicimos la misma cuenta
informal: **comparar dos términos y quedarnos con el grande**.

Este capítulo formaliza esa cuenta y le añade lo que faltaba: una estimación
del error cometido y un criterio para saber cuándo el procedimiento falla.

La regla de oro es la que ya conocemos del capítulo 2: **compara términos
adimensionalizados**. Decir «este término es pequeño» sin decir *comparado con
cuál* no significa nada, porque depende de las unidades.

### 3.2 Parámetro pequeño frente a término pequeño

Hay una distinción que decide todo el capítulo.

**Perturbación regular:** al hacer $\epsilon\to0$, el problema se convierte
suavemente en un problema más simple cuya solución se parece a la del original.
Se puede desarrollar $x=x_0+\epsilon x_1+\epsilon^2x_2+\dots$ y todo funciona.

**Perturbación singular:** al hacer $\epsilon\to0$, el problema **cambia de
naturaleza**. Baja el grado de una ecuación, se pierde una raíz, desaparece una
condición de contorno, cambia el orden de una ecuación diferencial. El
desarrollo ingenuo da una respuesta incompleta o directamente falsa.

Las señales de alarma de una perturbación singular son reconocibles:

* $\epsilon$ multiplica **la derivada de orden más alto**;
* $\epsilon$ multiplica el término de mayor grado de un polinomio;
* al poner $\epsilon=0$, quedan **menos condiciones de contorno de las que hay**;
* la solución tiene una región estrecha donde varía muy deprisa.

---

## 4. La matemática

### 4.1 Taylor como herramienta de decisión

$$f(x_0+h)=f(x_0)+f'(x_0)h+\frac{f''(x_0)}{2}h^2+\dots$$

El desarrollo no es lo interesante; lo interesante es el **resto**. Truncar en
el orden $n$ deja un error acotado por
$\frac{|f^{(n+1)}|_{\max}}{(n+1)!}|h|^{n+1}$, y de ahí sale el número que
buscábamos.

![Hasta dónde valen las aproximaciones. Izquierda: error relativo de tres truncamientos de $\sin x$, con el punto donde cruzan el 1 %. Derecha: la serie de $1/(1+x)$, que diverge más allá de su radio de convergencia. Lo que hay que concluir: cada aproximación tiene un dominio de validez cuantificable, y añadir términos no siempre ayuda.](figuras/fig_taylor_validez.pdf)

Los números responden a la pregunta del principio:

| Aproximación | Error < 1 % hasta |
|---|---|
| $\sin\theta\approx\theta$ | 0,248 rad = **14°** |
| $\sin\theta\approx\theta-\theta^3/6$ | 1,010 rad = **58°** |
| Un término más | 1,757 rad = **101°** |

Catorce grados es bastante menos de lo que la mayoría supone. Y hay un matiz
importante: para el **periodo del péndulo**, que depende de $\sin\theta$ de una
manera integrada, la aproximación de ángulo pequeño aguanta bastante más
—recuerda la figura del capítulo 2, donde a 1 rad el error del periodo era sólo
del 7 %—. **El dominio de validez depende de qué cantidad te importa**, no sólo
de la función.

El panel derecho añade una advertencia distinta: la serie de $1/(1+x)$ tiene
radio de convergencia 1, y más allá **diverge**. Sumar más términos empeora el
resultado sin límite. Una serie de Taylor no es siempre una aproximación mejor
cuanto más larga.

### 4.2 Balance dominante: la técnica más útil

El procedimiento, que se aplica a ecuaciones algebraicas y diferenciales por
igual:

1. Escribe todos los términos.
2. **Supón** que dos de ellos dominan y el resto son despreciables.
3. Resuelve el balance de esos dos.
4. **Comprueba** que los despreciados son efectivamente pequeños con esa
   solución.
5. Si la comprobación falla, prueba otro par.

El paso 4 no es opcional: es lo que distingue el método de adivinar.

![Perturbación regular frente a singular. Izquierda: la raíz que el desarrollo ingenuo encuentra bien. Derecha: la que pierde, y que se recupera reescalando. Lo que hay que concluir: al hacer $\epsilon=0$ la ecuación baja de grado, y una raíz se escapa al infinito.](figuras/fig_balance_dominante.pdf)

Tomemos $\epsilon x^2+x-1=0$ con $\epsilon$ pequeño.

**Balance 1: $x\sim1$.** Entonces $\epsilon x^2\sim\epsilon\ll1$: el término
pequeño es despreciable y queda $x\approx1$. Refinando,
$x=1-\epsilon+2\epsilon^2+\dots$ Con $\epsilon=10^{-2}$ da 0,990200 frente a
la raíz exacta 0,990195. Excelente.

**Balance 2: ¿y si $x$ es grande?** Supongamos $x\sim\epsilon^{-a}$. Los tres
términos escalan como $\epsilon^{1-2a}$, $\epsilon^{-a}$ y $1$. Para que dos se
equilibren hace falta $1-2a=-a$, es decir $a=1$: $x\sim1/\epsilon$. Con
$x=X/\epsilon$, la ecuación se convierte en $X^2+X-\epsilon=0$, cuya raíz es
$X\approx-1$, luego $x\approx-1/\epsilon-1$. Con $\epsilon=10^{-2}$ da $-101{,}0$
frente a la raíz exacta $-100{,}990$.

**La segunda raíz existía siempre**; lo que pasaba es que se va al infinito
cuando $\epsilon\to0$, y por eso el desarrollo alrededor de $\epsilon=0$ no la
ve. El reescalado la trae de vuelta a una escala visible.

::: herramientas
**Cómo se encuentra el reescalado correcto**

Pon $x=\epsilon^{-a}X$ con $a$ desconocido y $X=\mathcal{O}(1)$. Escribe cómo
escala cada término con $\epsilon$. Busca los valores de $a$ que hacen que **al
menos dos términos tengan el mismo orden** y que ese orden sea el mayor de
todos.

Cada valor válido de $a$ corresponde a una escala distinta del problema, y por
tanto a una parte distinta de la solución. Esto se llama *análisis de balance
dominante* y es la técnica central del libro de Bender y Orszag.
:::

### 4.3 Capas límite: cuando el término pequeño manda

El mismo fenómeno en ecuaciones diferenciales:

$$\epsilon y''+y'+y=0,\qquad y(0)=0,\ y(1)=1$$

Si haces $\epsilon=0$ queda $y'+y=0$, que es de primer orden y **sólo admite
una condición de contorno**. Tienes dos. Algo tiene que ceder.

![Capas límite. Izquierda: la solución exacta para tres valores de $\epsilon$ y la solución exterior, que no cumple $y(0)=0$. Derecha: el empalme entre la solución exterior, la interior y la compuesta. Lo que hay que concluir: la solución tiene dos escalas espaciales, $1$ y $\epsilon$, y la aproximación ingenua sólo ve una.](figuras/fig_capa_limite.pdf)

Lo que ocurre es que la solución tiene **dos escalas espaciales**:

* Lejos del borde, $y\approx e^{1-x}$: la solución **exterior**, que satisface
  $y(1)=1$.
* Cerca de $x=0$, en una región de anchura $\epsilon$, la solución varía muy
  deprisa para bajar de $e$ hasta 0. Es la **capa límite**.

Reescalando $x=\epsilon\xi$, el término $\epsilon y''$ deja de ser pequeño:
pasa a ser $y''/\epsilon$, del mismo orden que $y'/\epsilon$. Ahí es donde
manda. La solución interior es $y\approx e(1-e^{-\xi})$, y la **compuesta** —la
suma de ambas menos su parte común— aproxima la solución en todo el intervalo
con un error del 4 % para $\epsilon=0{,}02$.

Esto no es un ejercicio académico. Es exactamente lo que ocurre en:

* la **capa límite viscosa** de Prandtl (1904): a Reynolds alto, la viscosidad
  es despreciable *salvo* en una capa fina junto a la pared, donde manda. Toda
  la aerodinámica moderna nace de esa observación;
* la **cinética enzimática**, donde la aproximación de estado cuasi-estacionario
  es una capa límite en el tiempo;
* los **circuitos con condensadores parásitos**, donde una capacidad diminuta
  domina el transitorio rápido;
* los **sistemas rígidos** del capítulo 8: el modo rápido es una capa límite
  temporal, y por eso los métodos explícitos sufren tanto.

### 4.4 Series asintóticas: divergentes y utilísimas

Aquí viene el resultado que más sorprende del capítulo.

Considera $f(x)=e^x E_1(x)=\int_0^\infty \frac{e^{-t}}{1+t/x}dt$ para $x$
grande. Desarrollando el denominador e integrando término a término:

$$f(x)\sim\frac{1}{x}-\frac{1}{x^2}+\frac{2}{x^3}-\frac{6}{x^4}+\dots
=\sum_{n=0}^{\infty}\frac{(-1)^n n!}{x^{n+1}}$$

Esa serie **diverge para todo $x$**: $n!$ crece más deprisa que $x^n$.

![Una serie divergente que funciona. Izquierda: el error frente al número de términos sumados; baja, alcanza un mínimo y después explota. Derecha: la precisión óptima alcanzable en función de $x$. Lo que hay que concluir: hay que sumar hasta el término más pequeño y parar ahí.](figuras/fig_serie_asintotica.pdf)

Los números:

| $x$ | Mejor con $N$ términos | Error mínimo | Error con 25 términos |
|---|---|---|---|
| 3 | 2 | $3{,}4\times10^{-2}$ | $5\times10^{12}$ |
| 5 | 4 | $3{,}7\times10^{-3}$ | $9\times10^{6}$ |
| 10 | 9 | $1{,}8\times10^{-5}$ | $0{,}11$ |

La regla práctica —**suma hasta el término más pequeño y para**— se llama
truncamiento óptimo, y el error alcanzable decae como $e^{-x}$.

La lección conceptual es importante y contradice lo que se enseña en primero:
**convergencia y utilidad son propiedades distintas**. Una serie convergente
puede necesitar $10^6$ términos para dar tres cifras; una divergente puede dar
cinco cifras con cuatro términos. Las series asintóticas son la herramienta
estándar en mecánica cuántica (teoría de perturbaciones), mecánica estadística,
óptica y mecánica celeste, y en casi todos esos casos **son divergentes**.

Y hay un corolario incómodo: si tu serie asintótica te da un error mínimo de
$10^{-5}$, no hay manera de mejorarlo dentro de ese esquema. Hacen falta
métodos distintos —resumación de Borel, aproximantes de Padé, análisis
exponencialmente asintótico— o aceptar el límite.

---

## 5. El ordenador entra en escena

::: antes
Vamos a resolver numéricamente $\epsilon y''+y'+y=0$ con $\epsilon=10^{-3}$.
Antes de ejecutar:

* ¿Cuántos puntos de malla necesitas para resolver la capa límite?
* ¿Qué pasa si usas una malla uniforme de 100 puntos?
* ¿Cuál es la relación entre esto y la rigidez del capítulo 8?
:::

```python
import numpy as np
from scipy.integrate import solve_bvp

eps = 1e-3
def sistema(x, y):
    return np.vstack([y[1], (-y[1] - y[0]) / eps])

def contorno(ya, yb):
    return np.array([ya[0], yb[0] - 1.0])

x = np.linspace(0, 1, 100)                    # malla uniforme: mala idea
sol = solve_bvp(sistema, contorno, x, np.zeros((2, x.size)), max_nodes=100000)
print(sol.status, len(sol.x))
```

Con malla uniforme de 100 puntos, la capa de anchura $10^{-3}$ cae entre los dos
primeros nodos: **el solucionador no la ve**, o la resuelve con oscilaciones
espurias. El solucionador adaptativo acaba metiendo miles de nodos concentrados
cerca de cero.

La lección práctica: **el análisis asintótico te dice dónde poner los puntos de
malla antes de calcular nada**. Saber que hay una capa de anchura $\epsilon$ es
lo que permite construir una malla graduada y resolver el problema con 200
nodos en lugar de 200 000. En problemas grandes, esa diferencia es la que
decide si el cálculo es viable.

::: juega
1. Baja $\epsilon$ a $10^{-5}$ con malla uniforme. ¿Qué pasa?
2. Usa una malla graduada con más puntos cerca de 0. ¿Cuántos necesitas?
3. Compara la solución numérica con la compuesta asintótica. ¿Cuál es más
   precisa para $\epsilon=10^{-4}$? (La respuesta sorprende.)
4. Cambia el signo del término $y'$. ¿Dónde aparece ahora la capa? ¿Por qué?
:::

---

## 6. ¿Qué estamos suponiendo?

::: supuestos
1. **Que el parámetro es realmente pequeño en el sentido adimensional
   correcto.** «$\epsilon=0{,}01$» no significa nada sin saber comparado con
   qué.
2. **Que la función es suficientemente suave** para el orden de Taylor que
   usamos.
3. **Que estamos dentro del radio de convergencia**, si la serie converge.
4. **Que la perturbación es regular**, cada vez que hacemos un desarrollo
   ingenuo. Comprobar las señales de alarma es obligatorio.
5. **Que hay separación de escalas**, es decir, que $\epsilon$ es realmente
   pequeño frente a 1. Cuando $\epsilon\approx0{,}3$, ni la aproximación
   asintótica ni el desarrollo regular sirven, y hay que calcular.
6. **Que el término despreciado no acumula efecto con el tiempo.** Un término
   pequeño integrado durante mucho tiempo puede dominar: es el problema
   secular.
:::

---

## 7. ¿Cuándo falla?

::: falla
**Falla ignorar el término de mayor derivada.** Es la firma de la perturbación
singular. Si $\epsilon$ multiplica a $y''$ y lo tiras, has bajado el orden de la
ecuación y has perdido una condición de contorno.

**Falla el desarrollo regular con términos seculares.** En el problema de dos
cuerpos perturbado, o en un oscilador con frecuencia ligeramente distinta, el
desarrollo ingenuo produce términos como $\epsilon t\sin t$, que crecen sin
límite y estropean la aproximación para $t\gtrsim1/\epsilon$. La solución es el
método de escalas múltiples o el de Poincaré–Lindstedt: **reconocer que la
frecuencia también se corrige**.

**Falla sumar demasiados términos de una serie asintótica.** Y falla
espectacularmente: en el ejemplo, pasar de 9 a 25 términos degrada el error de
$10^{-5}$ a $10^{-1}$.

**Falla la aproximación cuando el parámetro no es tan pequeño.** Con
$\epsilon=0{,}2$ el error de la solución compuesta ya es del 20 %. El régimen
intermedio —donde nada es pequeño— es el más difícil y es donde hay que
calcular numéricamente.

**Y falla despreciar por costumbre.** El caso más caro es despreciar algo
porque «siempre se desprecia», sin recomprobar que el número sigue siendo
pequeño en el régimen nuevo.
:::

### Un anti-ejemplo: la corrección que se acumuló

Un cálculo de órbita desprecia el achatamiento terrestre porque el término
correspondiente es $10^{-3}$ del principal. Para una órbita, error del 0,1 %:
irrelevante. Para predecir la posición al cabo de un mes —unas 500 órbitas— el
término no produce un error del 0,1 %: produce una **precesión acumulativa**
que desplaza el plano orbital varios grados.

La diferencia entre un error pequeño y un error pequeño **acumulativo** es la
distinción entre términos periódicos y seculares, y es la razón de que la
mecánica celeste desarrollara técnicas específicas durante dos siglos.

La pregunta que hay que hacerse siempre: **¿este término pequeño se promedia a
cero o se acumula?** Si se acumula, el criterio no es «$\epsilon\ll1$» sino
«$\epsilon t\ll1$», que es una condición sobre cuánto tiempo puedes usar tu
modelo.

---

## 8. Historia

::: historia
**Prandtl, 1904: ocho páginas y una disciplina entera** ·
*Nivel de verificación: A.*

Durante todo el siglo XIX hubo una contradicción incómoda. Las ecuaciones de un
fluido ideal (sin viscosidad) predicen que un cuerpo en movimiento uniforme no
experimenta resistencia: es la **paradoja de d'Alembert**, y contradice la
experiencia de cualquiera que haya sacado la mano por la ventanilla. Las
ecuaciones con viscosidad —Navier–Stokes— eran intratables.

En agosto de 1904, en el Congreso Internacional de Matemáticos de Heidelberg,
Ludwig Prandtl presentó una comunicación de ocho páginas: *Über
Flüssigkeitsbewegung bei sehr kleiner Reibung*. Su idea: a Reynolds alto la
viscosidad es despreciable **salvo en una capa muy fina junto a la superficie**,
donde los gradientes son enormes y el término viscoso, que va con la segunda
derivada, deja de ser pequeño.

Es exactamente el análisis de la sección 4.3, y la anchura de la capa escala
como $1/\sqrt{Re}$.

La comunicación pasó casi desapercibida en el congreso. Hoy es el fundamento de
la aerodinámica: permite calcular la resistencia, predecir el desprendimiento
de la capa límite —y por tanto la entrada en pérdida de un ala— y diseñar
perfiles.

Y merece señalarse el método: Prandtl no resolvió Navier–Stokes. **Identificó
las dos regiones donde dominaban términos distintos, resolvió cada una y las
empalmó.**

**Poincaré y las series que no convergen** · *Nivel de verificación: A.*

Los astrónomos del siglo XIX usaban series divergentes con enorme éxito
práctico y con muy mala conciencia matemática. Abel escribió en 1828 que las
series divergentes eran «una invención del diablo» y que basar cualquier
demostración en ellas era vergonzoso.

En 1886, Poincaré dio la definición precisa de **serie asintótica** y demostró
que esas series, aunque divergentes, proporcionan aproximaciones controladas
si se truncan adecuadamente. Reconcilió la práctica astronómica con el rigor.

Hay una anécdota que circula en varias versiones, y por eso la contamos como
nivel B: se dice que Poincaré observó que para los astrónomos una serie converge
si los primeros términos decrecen deprisa, y para los matemáticos diverge; y
que ambos tienen razón desde su punto de vista. La formulación exacta y la
fuente primaria son inciertas, pero el contenido es real y está en el espíritu
de su trabajo de 1886.

**Y una advertencia sobre el orden de magnitud** · *Nivel de verificación: A.*

En 1948, Freeman Dyson señaló que la serie de perturbaciones de la
electrodinámica cuántica —la teoría más precisamente verificada de la física—
**tiene que ser divergente**, mediante un argumento de una elegancia notable:
si convergiera para una constante de acoplamiento $\alpha$, convergería también
para $-\alpha$, y un universo con cargas del mismo signo atrayéndose sería
inestable.

Y sin embargo, truncada en los primeros términos, la QED predice el momento
magnético anómalo del electrón con doce cifras significativas de acuerdo con el
experimento. **Es la serie divergente más exitosa de la historia de la
ciencia.**
:::

---

## 9. Problemas

En `problemas.md`; soluciones en `soluciones.md`.

---

## 10. Experimento computacional

::: experimento
**Descubre el exponente de una capa límite midiendo.**

*Pregunta:* ¿cómo escala la anchura de una capa límite con el parámetro
pequeño, si no lo sabes de antemano?

*Diseño.* Resuelve numéricamente $\epsilon y''+y'+y=0$ con condiciones de
contorno fijas, para $\epsilon$ entre $10^{-1}$ y $10^{-5}$, con malla adaptativa.

*Análisis.* Define la anchura de la capa como la distancia en la que $y$ pasa
del 10 % al 90 % de su valor exterior. Dibuja anchura frente a $\epsilon$ en
log-log y mide la pendiente.

*Qué esperar:* pendiente 1, es decir anchura $\propto\epsilon$.

*Después, la parte interesante:* repite con $\epsilon y''+xy'+y=0$, donde el
coeficiente se anula en el interior. La anchura escala ahora como
$\sqrt\epsilon$, y la capa aparece **en el interior**, no en el borde. Es una
*capa interior* o de transición, y descubrirla midiendo es mucho más
instructivo que leerla.
:::

---

## 11. Explícalo

::: explica
1. ¿Qué significa exactamente «pequeño» en una aproximación?
2. ¿Cómo puede una serie divergente dar resultados precisos?
3. Explica una capa límite a alguien que ha sacado la mano por la ventanilla
   del coche.
4. ¿Por qué despreciar el término con la derivada más alta es distinto de
   despreciar cualquier otro?
5. ¿Qué diferencia hay entre un error pequeño y un error pequeño acumulativo?
6. ¿Por qué el dominio de validez de $\sin\theta\approx\theta$ depende de qué
   quieras calcular?
:::

---

## 12. Lo esencial

::: esencial
* «Pequeño» sin decir comparado con qué no significa nada.
  Adimensionaliza primero.
* Taylor sirve para decidir, no para desarrollar: lo que importa es el resto.
  $\sin\theta\approx\theta$ vale hasta 14° al 1 %, no hasta donde te apetezca.
* Balance dominante: supón qué manda, resuelve, **comprueba**. El cuarto paso
  es el método.
* Perturbación singular: $\epsilon$ multiplica la derivada más alta, o el
  término de mayor grado, o te quedas sin condiciones de contorno. Entonces hay
  que reescalar.
* Una capa límite es una región donde el término pequeño deja de serlo porque
  las derivadas se disparan. Prandtl, y toda la aerodinámica.
* El análisis asintótico te dice dónde poner los puntos de malla **antes** de
  calcular.
* Las series asintóticas divergen y funcionan: suma hasta el término más
  pequeño y para.
* Un término pequeño que se acumula no es pequeño. El criterio pasa de
  $\epsilon\ll1$ a $\epsilon t\ll1$.
:::

---

## 13. Preguntas que quedan abiertas

::: abierto
* ¿Cómo se sabe, ante un problema nuevo, si la perturbación es regular sin
  resolverlo?
* Si el error mínimo de una serie asintótica es $e^{-1/\epsilon}$, ¿qué
  información contiene esa parte exponencialmente pequeña, y se puede recuperar?
* ¿Qué hacer en el régimen intermedio, donde ningún parámetro es pequeño y el
  cálculo numérico es caro?
* Los métodos de escalas múltiples eliminan términos seculares. ¿Hay un
  criterio general para saber cuántas escalas hacen falta?
* Si la serie de la QED diverge, ¿en qué sentido exactamente «tenemos» esa
  teoría?
:::
