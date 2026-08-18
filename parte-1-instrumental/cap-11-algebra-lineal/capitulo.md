# Capítulo 11 — Álgebra lineal como lenguaje de modelos

> **Qué sabrás hacer al terminar**
> · Leer un autovector como un modo natural del sistema ·
> Usar la SVD para saber cuánta información hay realmente en unos datos ·
> Diagnosticar un sistema mal condicionado antes de resolverlo ·
> Saber por qué los autovalores no bastan para juzgar la estabilidad práctica.
>
> **Herramientas que usa:** capítulos 5, 6, 7 y 8.
> **Disciplinas de los ejemplos:** mecánica, redes, química, tratamiento de
> imagen, hidrodinámica, análisis de datos.
> **Deuda que paga:** los autovalores prometidos en el capítulo 7.
> **Deuda que abre:** la deconvolución como problema mal condicionado
> (capítulo II.14).

---

## 1. Una pregunta

::: pregunta
Tienes un sistema de dos ecuaciones con dos incógnitas. Los datos de entrada
los conoces con un 1 % de error, cosa normal en un laboratorio.

**¿Con qué error conocerás la solución?**
:::

La respuesta correcta —«depende de la matriz, y puede ser un 1000 %»— es la
razón por la que existe el análisis numérico como disciplina. Y el número que
lo decide, el **número de condición**, es probablemente la cantidad más útil de
todo este capítulo.

---

## 2. Antes de calcular

::: antes
1. ¿Qué información contiene un autovector que no contenga el autovalor?
2. Si todos los autovalores de una matriz tienen parte real negativa, ¿es el
   sistema estable? ¿Siempre?
3. Una matriz de datos de $10^4\times10^3$. ¿Cuántos números independientes
   contiene realmente?
:::

---

## 3. La intuición

### 3.1 Un vector es un estado; una matriz es una regla

Este capítulo no es un curso de álgebra lineal. Es una selección brutal: sólo
lo que hace falta para modelar, y contado desde el uso.

La traducción que hay que instalar:

| Objeto | Lo que es en un modelo |
|---|---|
| Vector $\mathbf{x}$ | el **estado** del sistema |
| Matriz $A$ | una **regla** que transforma estados |
| $A\mathbf{x}=\mathbf{b}$ | «¿qué estado produce esta observación?» |
| Autovector | una dirección que la regla **no mezcla** |
| Autovalor | cuánto estira o encoge esa dirección |
| Cambio de base | elegir el punto de vista |

La idea central del capítulo cabe en una frase: **casi todos los problemas
lineales se vuelven triviales en la base correcta, y toda la técnica consiste
en encontrarla**.

### 3.2 Autovectores: los modos naturales

Un autovector no es una curiosidad algebraica. Es una configuración del sistema
que, al evolucionar, **conserva su forma y sólo cambia de tamaño**.

![Tres masas y tres muelles. Arriba: los tres modos normales, con sus frecuencias. Abajo: un movimiento arbitrario, la misma cosa vista en la base de modos, y el peso de cada modo. Lo que hay que concluir: en la base correcta, un problema acoplado se convierte en tres problemas independientes.](figuras/fig_modos_normales.pdf)

El panel inferior izquierdo es un lío: tres masas moviéndose de forma
aparentemente errática. El panel central son **tres cosenos**. Es exactamente
el mismo movimiento. La única diferencia es el sistema de coordenadas.

Esta idea reaparece en todo el libro:

* En un sistema dinámico lineal, los autovalores del jacobiano son las tasas y
  frecuencias (capítulo 7).
* En una cadena de Markov, el autovector dominante es la distribución
  estacionaria y el segundo autovalor da la velocidad de convergencia
  (capítulo 9).
* En una molécula, los autovectores son los modos de vibración y los
  autovalores, las frecuencias del espectro infrarrojo.
* En una red, los autovectores del laplaciano revelan sus comunidades.
* En Fourier, las exponenciales complejas son los autovectores de la derivada,
  y por eso Fourier funciona (capítulo 12).

**Fourier es un caso particular de diagonalización.** Esa frase es todo el
puente entre este capítulo y el siguiente.

---

## 4. La matemática

### 4.1 Cuando sí y cuando no se puede diagonalizar

Para una matriz **simétrica** (o hermítica), el teorema espectral garantiza:
autovalores reales, autovectores ortogonales, diagonalización siempre posible.
Es el caso cómodo, y aparece siempre que hay una energía o una covarianza
detrás.

Para una matriz general, no hay garantías: puede no ser diagonalizable, y sus
autovectores pueden ser casi paralelos. Esa última posibilidad es la fuente de
uno de los errores más sutiles del modelado, y le dedicamos la sección 4.5.

Para sistemas lineales $\dot{\mathbf{x}}=A\mathbf{x}$, la solución es

$$\mathbf{x}(t)=e^{At}\mathbf{x}_0=\sum_k c_k e^{\lambda_k t}\mathbf{v}_k$$

es decir: **descompón el estado inicial en modos, deja evolucionar cada modo
por separado, vuelve a sumar**. Tres pasos, y el segundo es trivial.

### 4.2 La SVD: la descomposición que lo explica todo

Toda matriz —cuadrada o no, simétrica o no— admite

$$A=U\Sigma V^{T}$$

con $U$ y $V$ ortogonales y $\Sigma$ diagonal con entradas $\sigma_1\ge
\sigma_2\ge\dots\ge0$. Geométricamente: **toda transformación lineal es una
rotación, un estiramiento a lo largo de ejes perpendiculares, y otra
rotación**. No hay más.

![La SVD de una imagen. Izquierda: el espectro de valores singulares. Centro: reconstrucciones con rango 1, 5, 20 y completo. Derecha: energía acumulada. Lo que hay que concluir: el 99 % de la información está en 38 de las 200 componentes, y el resto es sobre todo ruido.](figuras/fig_svd.pdf)

De la SVD salen, sin esfuerzo adicional:

* **El rango efectivo.** Cuántos $\sigma_k$ están por encima del nivel de
  ruido. Es «cuántos números independientes hay realmente aquí».
* **La mejor aproximación de rango $k$** (teorema de Eckart–Young): quedarse
  con los $k$ mayores es óptimo en norma de Frobenius y en norma 2. Es
  compresión, y es también eliminación de ruido.
* **El PCA**, que es la SVD de los datos centrados. Los vectores de $V$ son las
  componentes principales.
* **Los mínimos cuadrados** vía la pseudoinversa
  $A^+=V\Sigma^{+}U^{T}$, que es la forma numéricamente estable de resolverlos
  —y no las ecuaciones normales, que elevan al cuadrado el número de
  condición—.
* **El número de condición**: $\kappa=\sigma_{\max}/\sigma_{\min}$.

Cinco cosas que en los cursos se enseñan por separado y son la misma.

### 4.3 Condicionamiento: cuánto amplifica tus errores

Si resuelves $A\mathbf{x}=\mathbf{b}$ y perturbas $\mathbf{b}$, el error
relativo de la solución se amplifica:

$$\frac{\|\delta \mathbf{x}\|}{\|\mathbf{x}\|}\le\kappa(A)\,
\frac{\|\delta \mathbf{b}\|}{\|\mathbf{b}\|},\qquad
\kappa(A)=\frac{\sigma_{\max}}{\sigma_{\min}}$$

![Dos sistemas $2\times2$ con la misma solución. Izquierda: $\kappa=1{,}5$. Derecha: $\kappa=1999$, las dos rectas casi paralelas. En ambos, 300 perturbaciones del 1 % en el término independiente. Lo que hay que concluir: la misma perturbación produce una dispersión 1300 veces mayor.](figuras/fig_condicionamiento.pdf)

La imagen geométrica es la que hay que recordar: **mal condicionado significa
que las rectas se cortan con un ángulo muy pequeño**. Un desplazamiento
minúsculo de una de ellas mueve el punto de corte muchísimo. En dimensión alta,
lo mismo con hiperplanos.

::: herramientas
**Regla de las cifras perdidas**

$$\text{cifras significativas perdidas}\approx\log_{10}\kappa(A)$$

Con doble precisión tienes unas 16 cifras. Con $\kappa=10^{12}$ te quedan 4.
Con $\kappa=10^{16}$, ninguna: el resultado que devuelve el ordenador es ruido
con formato de número.

**Comprueba siempre `np.linalg.cond(A)` antes de resolver.** Es una línea y
te dice si el resultado significa algo. Y si sale grande, la solución no es
buscar un algoritmo mejor —ninguno arregla un problema mal planteado— sino
replantear: reescalar las variables, añadir información (regularización) o
aceptar que ciertas combinaciones no se pueden determinar.
:::

Y una advertencia importante: **el mal condicionamiento suele ser culpa tuya, no
de la matriz**. Si mides longitudes en metros y tiempos en nanosegundos, tu
matriz tendrá entradas con nueve órdenes de magnitud de diferencia y un
$\kappa$ enorme por razones puramente de unidades. Adimensionalizar —capítulo 2
otra vez— es la primera medida de precondicionamiento.

### 4.4 Sistemas grandes: cuando la matriz ya no cabe

Con $n=10^6$, una matriz densa ocupa 8 TB. No hay ninguna posibilidad de
almacenarla, y menos de invertirla.

La salida es que casi todas las matrices grandes que aparecen en modelado son
**dispersas**: cada ecuación involucra unos pocos vecinos. Una discretización
por diferencias finitas produce una matriz con 3, 5 o 7 elementos no nulos por
fila.

Para esas, los métodos iterativos (gradiente conjugado, GMRES) sólo necesitan
saber **multiplicar por $A$**, nunca almacenarla. Y su velocidad de convergencia
depende de... el número de condición, otra vez: el gradiente conjugado converge
en $\mathcal{O}(\sqrt{\kappa})$ iteraciones. De ahí que precondicionar —buscar
$M\approx A^{-1}$ barato y resolver $M A\mathbf{x}=M\mathbf{b}$— sea, en la
práctica, más importante que elegir el iterador.

### 4.5 Matrices no normales: el fallo que los autovalores no ven

Este apartado corrige un error muy extendido.

Una matriz es **normal** si $A^TA=AA^T$; entonces sus autovectores son
ortogonales y todo es intuitivo. Si no lo es, sus autovectores pueden ser casi
paralelos, y entonces ocurre algo que la teoría de autovalores no anticipa.

![Una matriz con autovalores $-1$ y $-2$: ambos estables. Izquierda: la amplificación real frente a lo que predicen los autovalores. Derecha: trayectorias que salen del círculo unidad antes de volver. Lo que hay que concluir: el sistema es asintóticamente estable y aun así amplifica una perturbación por un factor 50 antes de decaer.](figuras/fig_no_normal.pdf)

El sistema **es** estable: a tiempo largo todo decae. Pero antes crece por un
factor 50, y si hay cualquier no linealidad en el sistema real, esa
amplificación transitoria puede llevarlo a un régimen del que no vuelva.

Esto no es una patología de laboratorio: es la explicación aceptada de la
**transición a la turbulencia** en flujo de Poiseuille y de Couette, donde el
análisis lineal clásico predice estabilidad para todos los números de Reynolds
y el experimento muestra turbulencia a partir de $Re\approx2000$. El operador
linealizado de Navier–Stokes es fuertemente no normal, y las perturbaciones
crecen transitoriamente por factores de $10^3$ antes de que las no linealidades
tomen el control (Trefethen et al., *Science* 1993).

La lección práctica es directa: **si tu matriz no es normal, los autovalores te
dicen qué pasa a tiempo infinito y no te dicen nada sobre qué pasa antes**. Lo
que hay que mirar entonces son los valores singulares de $e^{At}$, o los
pseudoespectros.

### 4.6 Grafos: cuando el modelo es una red

Una red se describe por su matriz de adyacencia $A$, y su **laplaciano**
$L=D-A$ contiene su estructura. Tres hechos que se usan constantemente:

* $L$ es semidefinida positiva y $\lambda_1=0$ siempre.
* La **multiplicidad de $\lambda=0$ es el número de componentes conexas**.
* El segundo autovalor $\lambda_2$ (conectividad algebraica de Fiedler) mide
  cuán difícil es partir la red en dos, y su autovector da **la partición**.

Y hay una conexión que cierra varios capítulos: la ecuación
$\dot{\mathbf{u}}=-L\mathbf{u}$ es **difusión sobre el grafo**. Es la misma
ecuación del calor del capítulo 8, con el laplaciano discreto sustituido por el
del grafo. Difusión de calor, propagación de una epidemia por una red de
contactos, sincronización de osciladores acoplados y consenso en sistemas
distribuidos son, matemáticamente, el mismo problema.

---

## 5. El ordenador entra en escena

::: antes
Vamos a resolver un sistema mal condicionado de dos maneras. Antes:

* ¿Dará el mismo resultado `np.linalg.solve` que la pseudoinversa?
* ¿Cuántas cifras correctas esperas con $\kappa=10^{10}$?
* ¿Ayudaría trabajar en precisión cuádruple?
:::

```python
import numpy as np

n = 12
A = np.vander(np.linspace(0, 1, n), n)      # matriz de Vandermonde: infame
x_real = np.ones(n)
b = A @ x_real

print(f"kappa = {np.linalg.cond(A):.2e}")
x1 = np.linalg.solve(A, b)
x2 = np.linalg.pinv(A, rcond=1e-10) @ b
print(f"error solve  : {np.linalg.norm(x1 - x_real):.2e}")
print(f"error pinv   : {np.linalg.norm(x2 - x_real):.2e}")
```

Con $\kappa\sim10^{10}$, `solve` pierde unas diez cifras y devuelve algo
reconocible pero malo. La pseudoinversa con truncamiento devuelve una solución
distinta: **la de norma mínima compatible con los datos dentro del ruido**. No
es «más correcta»: es una respuesta a una pregunta ligeramente distinta, y esa
es exactamente la idea de la regularización que usaremos en II.14.

::: juega
1. Sube $n$ de 6 a 20 y dibuja $\kappa$ frente a $n$. ¿Crece exponencialmente?
2. Cambia la base de monomios a polinomios de Chebyshev. ¿Cuánto baja $\kappa$?
   (La respuesta es espectacular y es la razón de que existan.)
3. Resuelve mediante ecuaciones normales $A^TA\mathbf{x}=A^T\mathbf{b}$.
   Comprueba que el condicionamiento se eleva al cuadrado.
4. Añade ruido de $10^{-8}$ a $b$ y mira cuánto se mueve la solución. Compáralo
   con la cota $\kappa\cdot\|\delta b\|/\|b\|$.
:::

---

## 6. ¿Qué estamos suponiendo?

::: supuestos
1. **Que el problema es lineal**, o que lo hemos linealizado y estamos dentro
   del radio de validez (capítulo 13).
2. **Que la matriz es diagonalizable**, cada vez que escribimos una
   descomposición modal. Las matrices defectivas existen.
3. **Que los autovectores son una base razonable.** Si son casi paralelos, la
   descomposición es numéricamente inestable aunque exista.
4. **Que las unidades están bien escaladas.** Buena parte del mal
   condicionamiento observado es artificial.
5. **Que los valores singulares pequeños son ruido.** Puede que sean señal
   débil: truncar es una decisión de modelado, no una operación neutra.
6. **Que la matriz cabe en memoria**, cosa que deja de ser cierta antes de lo
   que uno espera.
:::

---

## 7. ¿Cuándo falla?

::: falla
**Falla resolver por ecuaciones normales.** $\kappa(A^TA)=\kappa(A)^2$: si $A$
tenía $\kappa=10^8$, ya has perdido todas las cifras. Usa QR o SVD. Es el error
numérico más frecuente en código de ajuste escrito a mano.

**Falla invertir explícitamente.** `np.linalg.inv(A) @ b` es más lento y menos
preciso que `np.linalg.solve(A, b)`. La inversa explícita casi nunca hace
falta; si aparece en tu código, casi seguro que hay una forma mejor.

**Falla el análisis modal con matrices no normales.** Los autovalores describen
el comportamiento asintótico y sólo eso.

**Falla la interpretación del PCA como «causas».** Las componentes principales
son direcciones de máxima varianza, no mecanismos. Que la primera componente
explique el 60 % no significa que exista un factor físico que haga eso; es una
propiedad de la covarianza, y depende de cómo hayas escalado las variables.

**Y falla el truncamiento sin criterio.** Elegir el rango mirando el «codo» del
espectro es razonable cuando hay codo, y arbitrario cuando no. El criterio
honesto lo da el nivel de ruido: descarta $\sigma_k$ por debajo del ruido de tus
datos, y declara ese umbral.
:::

### Un anti-ejemplo: la componente principal que no existía

Un equipo aplica PCA a un conjunto de medidas de un proceso industrial: diez
variables, mil observaciones. La primera componente explica el 78 % de la
varianza y tiene pesos grandes en tres sensores. Se interpreta como un «modo de
operación» del proceso y se construye un indicador con ella.

El problema: tres de las diez variables estaban en unidades con valores
numéricos mucho mayores que las demás (presiones en pascales frente a caudales
en m³/s). El PCA sin estandarizar maximiza varianza **en las unidades en que
esté escrito**, así que la primera componente era esencialmente «las tres
variables con números grandes». Al estandarizar, la estructura desaparecía.

La lección: **el PCA no es invariante bajo cambio de unidades**. Estandarizar
o no es una decisión de modelado que hay que justificar, y sobre la que casi
nunca se dice nada en los artículos.

---

## 8. Historia

::: historia
**La SVD, descubierta cuatro veces** · *Nivel de verificación: A.*

Eugenio Beltrami la publicó en 1873 para formas bilineales; Camille Jordan la
obtuvo independientemente en 1874; James Joseph Sylvester la redescubrió en
1889; Erhard Schmidt la extendió a operadores integrales en 1907, y en ese
contexto demostró lo que hoy llamamos teorema de Eckart–Young —que Carl Eckart
y Gale Young redescubrieron para matrices en 1936—.

Stewart (1993) reconstruyó la historia completa. Es un caso de manual de la ley
de Stigler, y también de algo más interesante: la SVD tardó un siglo en
volverse central, y lo hizo cuando Golub y Kahan publicaron en 1965 un
**algoritmo estable para calcularla**. La utilidad de un concepto matemático
depende con frecuencia de que exista una forma fiable de computarlo.

**Gauss, otra vez, y la eliminación** · *Nivel de verificación: A.*

La eliminación gaussiana aparece en el *Jiuzhang Suanshu* chino, unos dos mil
años antes de Gauss. Lo que sí es de Gauss, y es lo que importa, es haberla
usado sistemáticamente para resolver los sistemas normales de los ajustes por
mínimos cuadrados de sus cálculos astronómicos.

Y hay un epílogo del siglo XX. En los años cuarenta y cincuenta se temía que la
eliminación gaussiana fuera numéricamente inestable: con $n$ ecuaciones hay
$\mathcal{O}(n^3)$ operaciones, y si los errores se acumularan, con $n=100$ el
método sería inservible. Hotelling llegó a publicar una cota pesimista.

James Wilkinson resolvió el asunto en 1961 con el **análisis hacia atrás**: en
lugar de acotar el error de la solución, demostró que la solución calculada es
la solución **exacta** de un sistema ligeramente perturbado. La eliminación con
pivoteo parcial es estable en ese sentido, y eso explica por qué funciona en la
práctica desde siempre.

Es la misma idea que reaparecía en el capítulo 8 con los integradores
simplécticos, y merece la pena tenerla como pregunta general: **¿qué problema
resuelve exactamente mi algoritmo?**

**Trefethen y la turbulencia que no debía existir** · *Nivel de verificación: A.*

En 1993, Lloyd Trefethen, Anne Trefethen, Satish Reddy y Tobin Driscoll
publicaron en *Science* *Hydrodynamic Stability Without Eigenvalues*. El
problema llevaba un siglo abierto: el análisis de estabilidad lineal del flujo
de Poiseuille predice estabilidad hasta $Re\approx5772$, y experimentalmente la
turbulencia aparece hacia $Re\approx2000$.

Su respuesta: el operador es fuertemente **no normal**. Perturbaciones que
según los autovalores deberían decaer crecen antes por factores de $10^3$, y a
esa amplitud las no linealidades ya mandan. El análisis correcto no son los
autovalores sino los pseudoespectros.

Es uno de los mejores ejemplos modernos de que **una herramienta estándar puede
estar respondiendo a la pregunta equivocada durante cien años**, y de que la
corrección no vino de más potencia de cálculo sino de mirar otra cantidad.
:::

---

## 9. Problemas

En `problemas.md`; soluciones en `soluciones.md`.

---

## 10. Experimento computacional

::: experimento
**Encuentra el rango efectivo de tus datos.**

*Pregunta:* ¿cuántos números independientes hay realmente en una tabla de datos
tuya?

*Diseño.* Coge una matriz de datos de tu trabajo (observaciones × variables).
Estandariza las columnas. Calcula la SVD y dibuja el espectro en escala
logarítmica.

*Análisis.* Compara el espectro con el de una matriz de ruido puro del mismo
tamaño (hay un resultado clásico, la ley de Marchenko–Pastur, que da la
distribución esperada). Los valores singulares que sobresalen por encima de ese
fondo son señal; el resto, ruido.

*Qué falsaría la conclusión:* baraja aleatoriamente cada columna por separado.
Eso destruye toda la correlación entre variables pero conserva las
distribuciones marginales. Si el espectro apenas cambia, **tu «estructura» no
era estructura**. Es una prueba de datos sustitutos, la misma idea que en el
capítulo 7.
:::

---

## 11. Explícalo

::: explica
1. ¿Qué es un autovector, físicamente, sin usar la palabra «autovalor»?
2. Explica el número de condición con la imagen de dos rectas que se cortan.
3. ¿Por qué la SVD explica a la vez compresión, ajuste y PCA?
4. ¿Cómo puede un sistema con todos los autovalores estables amplificar una
   perturbación por un factor 1000?
5. ¿Por qué es peor resolver por ecuaciones normales que por QR?
6. ¿Qué le dirías a alguien que interpreta la primera componente principal como
   una causa física?
:::

---

## 12. Lo esencial

::: esencial
* Un vector es un estado; una matriz, una regla. Casi todo problema lineal es
  trivial en la base correcta.
* Un autovector es una dirección que el sistema no mezcla; el autovalor, cuánto
  la estira. En dinámica: tasa y frecuencia.
* Toda transformación lineal es rotar, estirar y rotar. Eso es la SVD.
* De la SVD salen el rango efectivo, la mejor aproximación de rango $k$, el
  PCA, los mínimos cuadrados estables y el número de condición.
* $\kappa$ dice cuántas cifras vas a perder: $\log_{10}\kappa$. Compruébalo
  antes de resolver.
* Buena parte del mal condicionamiento es culpa de las unidades.
  Adimensionalizar es precondicionar.
* Con matrices no normales, los autovalores describen el infinito y nada más.
  Mira los valores singulares de $e^{At}$.
* No resuelvas por ecuaciones normales. No inviertas explícitamente.
:::

---

## 13. Preguntas que quedan abiertas

::: abierto
* ¿Cómo se decide dónde truncar un espectro de valores singulares, si no hay
  codo?
* La no normalidad explica la transición a la turbulencia. ¿Dónde más estamos
  usando autovalores donde deberíamos usar pseudoespectros?
* Si el PCA no es invariante bajo escalado, ¿qué significa exactamente una
  «componente principal» de datos heterogéneos?
* ¿Cuándo merece la pena precondicionar, y cómo se elige el precondicionador
  sin resolver antes el problema?
* Los métodos aleatorizados calculan SVD aproximadas muchísimo más rápido.
  ¿Qué se pierde exactamente al aleatorizar?
:::
