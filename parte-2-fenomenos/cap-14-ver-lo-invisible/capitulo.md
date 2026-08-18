# II.14 — ¿Cómo se ve lo que no se puede ver?

> **El fenómeno:** una imagen borrosa, un espectro con líneas solapadas, una
> radiografía a partir de proyecciones.
> **Herramientas:** cap. 5 (incertidumbre), cap. 10 (regularización), cap. 11
> (condicionamiento), cap. 12 (convolución), cap. 15 (mala especificación).
> **Lo que hay que llevarse:** que deshacer una medida no es dividir, que todo
> problema inverso exige información adicional, y que esa información hay que
> declararla.

---

## 1. Una pregunta

::: pregunta
Un instrumento emborrona lo que mide: en lugar de la señal $f$, registra
$m = f * h + \text{ruido}$, con $h$ conocido.

Por el teorema de convolución (capítulo 12), basta con dividir en frecuencia:
$\hat f = \hat m/\hat h$.

**¿Por qué eso no funciona?**
:::

---

## 2. Antes de calcular

::: antes
1. ¿Qué le pasa a $\hat m/\hat h$ en las frecuencias donde $\hat h$ es pequeño?
2. Si el ruido es un 0,1 % de la señal, ¿cuánto error esperas en el resultado?
3. ¿Se puede recuperar información que el instrumento ha borrado?
:::

---

## 3. Por qué explota la inversión ingenua

![Deconvolución. Arriba a la izquierda: la inversión ingenua, en su propio eje —fíjate en el $10^{14}$ de la esquina—. Abajo: la verdad, la medida borrosa con ruido y la solución regularizada. Derecha: la curva L, que localiza el compromiso. Lo que hay que concluir: la inversión ingenua da un error de $6\times10^{15}$ y la regularizada de 2,2. Quince órdenes de magnitud, por un solo parámetro. Que la ingenua necesite otro eje para caber **es** el resultado.](figuras/fig_deconvolucion.pdf)

El instrumento actúa como un **filtro paso bajo**: $\hat h(k)$ decae al crecer
$k$. En las frecuencias altas, $\hat h\approx0$, y ahí:

$$\hat f = \frac{\hat m}{\hat h} = \frac{\hat h\hat f_{\text{real}}+\hat n}
{\hat h} = \hat f_{\text{real}} + \frac{\hat n}{\hat h}$$

El segundo término **explota** justo donde $\hat h\to0$. Y esas son
precisamente las frecuencias que el instrumento ha borrado: dividir por casi
cero amplifica el ruido de manera ilimitada.

Es el condicionamiento del capítulo 11 en su forma más pura: el operador de
convolución tiene valores singulares que decaen a cero, así que su número de
condición es infinito.

---

## 4. Regularización: cambiar la pregunta

La solución no es un algoritmo mejor. Es **admitir que el problema, tal como
está planteado, no tiene solución única y estable**, y añadir información.

Tikhonov: en lugar de resolver $Kf=m$, minimiza

$$\|Kf-m\|^2+\lambda\|Lf\|^2$$

El primer término exige fidelidad a los datos; el segundo penaliza soluciones
«feas» según algún criterio $L$ —rugosidad, energía, variación total—.
$\lambda$ decide el equilibrio.

En Fourier, para $L=I$, el filtro resultante es

$$\hat f=\frac{\overline{\hat h}}{|\hat h|^2+\lambda}\,\hat m$$

que coincide con $1/\hat h$ donde $\hat h$ es grande y **se apaga suavemente**
donde $\hat h$ es pequeño. Es el filtro de Wiener, y su forma es exactamente la
de un compromiso sesgo-varianza.

**La elección de $\lambda$ es una decisión de modelado, no un detalle técnico.**
Con $\lambda$ pequeño, se recupera detalle y ruido; con $\lambda$ grande, una
solución suave y sesgada. Tres criterios habituales:

* **Curva L:** dibuja rugosidad frente a residuo en log-log; la esquina es un
  buen compromiso. Es lo que hace la figura, y da $\lambda=1{,}9\times10^{-6}$.
* **Principio de discrepancia de Morozov:** elige $\lambda$ para que el residuo
  iguale al nivel de ruido conocido. Requiere conocer el ruido.
* **Validación cruzada generalizada:** deja fuera datos y minimiza el error de
  predicción. No requiere conocer el ruido.

---

## 5. Qué información se añade, y por qué hay que declararla

Toda regularización es una **hipótesis sobre la solución**, y hay que decir
cuál:

| Penalización | Hipótesis implícita | Dónde se usa |
|---|---|---|
| $\|f\|^2$ | la solución es pequeña | genérica |
| $\|\nabla f\|^2$ | la solución es suave | señales continuas |
| Variación total | la solución es plana a trozos | imágenes con bordes |
| $\|f\|_1$ | la solución es dispersa | espectros, compressed sensing |
| $f\ge0$ | no hay valores negativos | conteos, concentraciones |

Esa última fila merece atención: **imponer positividad, que es gratis y
físicamente obvio en muchos problemas, es una de las regularizaciones más
potentes que existen**, y con frecuencia se olvida.

Y la advertencia del capítulo 15: la elección de penalización **determina qué
estructuras aparecerán en tu solución**. Si penalizas rugosidad, tu resultado
será suave, tenga o no bordes la realidad. Si penalizas $\ell_1$, tu resultado
tendrá picos. **Nunca se puede concluir que la solución tiene la estructura que
tu regularizador impone.**

---

## 6. El mismo problema en muchos disfraces

* **Tomografía.** Reconstruir un volumen a partir de proyecciones. La inversión
  de Radon es inestable de la misma manera, y por eso se usan filtros y métodos
  iterativos regularizados.
* **Espectroscopía.** Separar líneas más estrechas que la resolución
  instrumental.
* **Astronomía.** Deconvolucionar la PSF del telescopio. El caso más famoso:
  las imágenes del Hubble antes de la corrección óptica de 1993 se procesaron
  con deconvolución, y funcionó **porque la PSF se conocía con precisión**.
* **Geofísica.** Inferir la estructura del subsuelo a partir de tiempos de
  llegada sísmicos.
* **Imagen médica.** Todo: resonancia, PET, ecografía.

En todos: el operador directo es suave y estabilizante, así que **el inverso es
amplificador**. Es una propiedad estructural, no un defecto del instrumento.

---

## 7. ¿Cuándo falla?

::: falla
**Falla si $h$ no se conoce bien.** La deconvolución ciega —estimar $f$ y $h$ a
la vez— es mucho más difícil y admite soluciones múltiples: $f*h$ no cambia si
desplazas detalle de uno a otro.

**Falla si el modelo directo es incorrecto.** Si el instrumento no es lineal, o
si $h$ varía con la posición, deconvolucionar con un $h$ único introduce
artefactos que **parecen estructura real**.

**Falla el exceso de regularización sin declararlo.** Una imagen suave puede ser
una imagen de un objeto suave o una imagen sobrerregularizada. Sólo lo distingue
la validación.

**Y falla creer que se recupera información borrada.** Por encima de la
frecuencia de corte del instrumento, la señal no está en los datos. Lo que
aparece ahí viene de la penalización, no de la medida. Las técnicas de
superresolución funcionan porque añaden información previa —dispersión,
positividad, múltiples medidas desplazadas—, no porque deshagan la física.
:::

---

## 8. Historia

::: historia
**Tikhonov, 1963, y la idea de problema mal planteado** ·
*Nivel de verificación: A.*

Hadamard había definido en 1902 los problemas «bien planteados»: existencia,
unicidad y dependencia continua de los datos. Y sostuvo que los problemas mal
planteados eran artificiales y sin interés físico.

Resultó ser exactamente al revés: **casi todos los problemas inversos
interesantes están mal planteados**, y son los que aparecen cuando quieres
inferir causas a partir de efectos.

Andréi Tikhonov, trabajando en problemas geofísicos, formuló en 1943 y
desarrolló en los sesenta la teoría de la regularización, que convierte un
problema mal planteado en una familia de problemas bien planteados indexada por
$\lambda$. La solución no es la del problema original —ese no la tiene— sino la
del regularizado, y la elección de $\lambda$ es parte del modelo.

**El Hubble, 1990–1993** · *Nivel de verificación: A.*

El espejo principal del Hubble se pulió con una aberración esférica: 2,2
micras de error, causadas por un instrumento de prueba mal montado. Las
imágenes salían borrosas.

Durante tres años, hasta la misión de reparación de diciembre de 1993, la
comunidad usó deconvolución —principalmente Richardson–Lucy, un método
iterativo con positividad impuesta— para recuperar resolución. Funcionó
notablemente bien, **y funcionó por dos razones**: la PSF se podía medir con
mucha precisión sobre estrellas de campo, y la positividad es una restricción
física fuerte en imágenes astronómicas.

Y hubo un efecto colateral instructivo: la comunidad astronómica aprendió a
usar y a desconfiar de la deconvolución al mismo tiempo. Se documentaron
artefactos característicos —anillos alrededor de fuentes puntuales, estructura
espuria en objetos extensos— que siguen siendo el catálogo de referencia de lo
que la deconvolución puede inventar.
:::

---

## 9. Experimento computacional

::: experimento
**Descubre qué inventa tu regularizador.**

Toma una señal de prueba con tres estructuras distintas: dos picos estrechos y
juntos, un pico ancho, y un escalón.

Convoluciona con un núcleo conocido, añade ruido, y deconvoluciona con tres
penalizaciones: $\|f\|^2$, $\|\nabla f\|^2$ y variación total.

*Qué comparar:* cómo reconstruye cada regularizador **cada una de las tres
estructuras**.

*Qué esperar:* la penalización de suavidad redondea el escalón; la variación
total lo reconstruye pero convierte el pico ancho en escalones; ninguna separa
los dos picos si están por debajo de la resolución.

*La conclusión que hay que escribir:* qué estructuras de tu resultado vienen de
los datos y cuáles de tu elección. Esa frase debería aparecer en todo artículo
que use deconvolución, y casi nunca aparece.
:::

---

## 10. Lo esencial

::: esencial
* Deshacer una medida no es dividir: el operador directo suaviza, así que el
  inverso amplifica el ruido de forma ilimitada.
* Es condicionamiento (capítulo 11): los valores singulares del operador decaen
  a cero.
* Regularizar es **cambiar la pregunta**: se resuelve un problema bien
  planteado próximo, indexado por $\lambda$.
* $\lambda$ se elige con curva L, discrepancia de Morozov o validación cruzada.
  Es una decisión de modelado.
* Toda penalización es una hipótesis sobre la solución, y determina qué
  estructuras aparecerán. **Declárala.**
* La positividad es gratis, físicamente obvia y muy potente. Úsala.
* Por encima del corte del instrumento no hay información: lo que aparece
  viene de la previa.
:::

---

## 11. Preguntas abiertas

::: abierto
* ¿Cómo se valida una reconstrucción cuando no existe la verdad de referencia?
* En deconvolución ciega, ¿qué información adicional garantiza unicidad?
* Los métodos de reconstrucción con redes neuronales dan imágenes espectaculares.
  ¿Qué información previa están imponiendo, y cómo se audita?
* ¿Puede una reconstrucción regularizada producir una estructura falsa que pase
  todos los controles habituales?
:::

### Referencias

* **Tikhonov, A. N.** *Solution of incorrectly formulated problems and the
  regularization method.* Soviet Math. Doklady **4** (1963), 1035–1038.
  **Nivel A (primaria).**
* **Hansen, Per Christian.** *Discrete Inverse Problems: Insight and
  Algorithms.* SIAM, 2010. **La referencia del capítulo**, con la curva L y
  código.
* **Aster, R.; Borchers, B.; Thurber, C.** *Parameter Estimation and Inverse
  Problems.* 3.ª ed., Elsevier, 2018. Práctico y con ejemplos geofísicos.
* **Richardson, W. H.** JOSA **62** (1972), 55–59; **Lucy, L. B.**
  Astronomical Journal **79** (1974), 745–754. El algoritmo del Hubble.
* **Rudin, L.; Osher, S.; Fatemi, E.** *Nonlinear total variation based noise
  removal algorithms.* Physica D **60** (1992), 259–268. Variación total.
* **Candès, E.; Romberg, J.; Tao, T.** *Robust uncertainty principles.* IEEE
  Trans. Inf. Theory **52** (2006), 489–509. Compressed sensing: qué
  información previa hace posible lo aparentemente imposible.
