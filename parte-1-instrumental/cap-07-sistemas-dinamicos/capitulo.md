# Capítulo 7 — Sistemas dinámicos

> **Qué sabrás hacer al terminar**
> · Leer un retrato de fases y clasificar puntos fijos con el jacobiano ·
> Reconocer las cuatro bifurcaciones locales y qué significan físicamente ·
> Distinguir caos de ruido, y medir un exponente de Lyapunov ·
> Calcular el horizonte de predicción de un sistema y saber por qué mejorar
> los datos apenas lo alarga.
>
> **Herramientas que usa:** capítulos 2, 5 y 6.
> **Disciplinas de los ejemplos:** meteorología, ecología, ingeniería de
> control, neurociencia, láseres, economía pesquera.
> **Deuda que abre:** los autovalores en serio (capítulo 11) y qué hace el
> ordenador al integrar esto (capítulo 8).

---

## 1. Una pregunta

::: pregunta
La predicción meteorológica a tres días es buena. A siete días es regular. A
quince días es inútil, y lo seguirá siendo por mucho que mejoren los
ordenadores y los satélites.

**¿Por qué existe ese muro, y dónde está exactamente?**
:::

La respuesta no es «el tiempo es complicado». Los modelos meteorológicos son
deterministas: las mismas ecuaciones con los mismos datos dan siempre el mismo
resultado. El muro no viene de la complejidad ni del azar. Viene de una
propiedad geométrica de las ecuaciones que se puede medir con un número, y ese
número dice exactamente cuántos días de predicción se ganan por cada mejora de
los datos iniciales.

Spoiler incómodo: **muy pocos**.

---

## 2. Antes de calcular

::: antes
1. Si mejoras la precisión de tus datos iniciales por un factor 1000, ¿cuánto
   alargas tu predicción? ¿Se triplica el plazo? ¿Se multiplica por mil?
2. Una población de peces se explota cada vez más. ¿Colapsará gradualmente o de
   golpe? Y si colapsa, ¿basta con dejar de pescar para recuperarla?
3. ¿Qué diferencia hay entre un sistema aleatorio y uno caótico, si sus series
   temporales parecen iguales?
:::

---

## 3. La intuición

### 3.1 Geometría en lugar de fórmulas

El capítulo 6 dejó una idea sin explotar: un sistema dinámico define un **campo
de vectores** en el espacio de estados. En cada punto, una flecha. Las
soluciones son curvas que siguen las flechas.

Ese cambio de perspectiva —de resolver a mirar— es el corazón de este
capítulo. La mayoría de los sistemas interesantes no tienen solución analítica,
y sin embargo se puede saber casi todo sobre su comportamiento cualitativo:
dónde acaban las trayectorias, cuántos estados de equilibrio hay, si oscilan,
si el sistema es robusto ante perturbaciones. Todo eso es **geometría del campo
de vectores**, y no requiere integrar nada.

### 3.2 Lo que puede pasar, según la dimensión

Hay un teorema con consecuencias enormes. En dimensión 2, el teorema de
Poincaré–Bendixson dice que una trayectoria acotada que no llega a un punto
fijo tiene que acabar en un **ciclo límite**. Es decir:

* **1D**: sólo puntos fijos. No hay oscilación.
* **2D**: puntos fijos y ciclos límite. No hay caos.
* **3D o más**: ya cabe todo, incluido el caos.

La razón es topológica: en el plano, una curva cerrada separa el interior del
exterior, y una trayectoria no puede cruzarse a sí misma. Eso la encierra. En
tres dimensiones, la trayectoria puede pasar «por encima» de sí misma y
estirarse y plegarse indefinidamente sin repetirse jamás.

**El caos necesita tres dimensiones y no linealidad.** Ninguna de las dos cosas
por separado basta.

---

## 4. La matemática

### 4.1 Puntos fijos y jacobiano

Para $\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x})$, un punto fijo cumple
$\mathbf{f}(\mathbf{x}^*)=0$. Linealizando con $\mathbf{x}=\mathbf{x}^*+\boldsymbol{\eta}$:

$$\dot{\boldsymbol{\eta}}=J\boldsymbol{\eta},\qquad
J_{ij}=\left.\frac{\partial f_i}{\partial x_j}\right|_{\mathbf{x}^*}$$

Las soluciones son combinaciones de $e^{\lambda_k t}\mathbf{v}_k$ con
$\lambda_k$ los autovalores de $J$. De ahí toda la clasificación:

| Autovalores | Tipo | Comportamiento |
|---|---|---|
| Ambos reales $<0$ | nodo estable | vuelve directamente |
| Ambos reales $>0$ | nodo inestable | se va |
| Reales de signo opuesto | **punto de silla** | vuelve por una dirección y se va por otra |
| Complejos, $\operatorname{Re}<0$ | foco estable | vuelve dando vueltas |
| Complejos, $\operatorname{Re}>0$ | foco inestable | se va dando vueltas |
| Imaginarios puros | centro | órbitas cerradas (**caso frágil**) |

Dos observaciones que valen más que la tabla.

**La parte real es la tasa; la imaginaria es la frecuencia.** Si
$\lambda=-0{,}1\pm2i$, el sistema oscila con periodo $2\pi/2\approx3{,}1$ y esa
oscilación se amortigua con $\tau=1/0{,}1=10$. Dos números, todo el
comportamiento.

**El centro es frágil.** Cuando $\operatorname{Re}\lambda=0$ exactamente, la
linealización **no decide**: los términos no lineales, que hemos despreciado,
son los que mandan. Es exactamente lo que ocurría con Lotka–Volterra en el
capítulo 6, y explica por qué sus órbitas cerradas se destruyen con cualquier
modificación del modelo.

### 4.2 Bifurcaciones: cuando el comportamiento cambia de golpe

Un sistema depende de parámetros. Al variarlos suavemente, casi siempre el
comportamiento cambia también suavemente. Pero en ciertos valores críticos, la
**estructura cualitativa** cambia: aparecen o desaparecen puntos fijos, cambian
de estabilidad, nace una oscilación. Eso es una bifurcación.

![Las cuatro bifurcaciones locales básicas. Lo que se ve: los puntos fijos en función del parámetro; línea continua estable, discontinua inestable. Lo que hay que concluir: cada una corresponde a un fenómeno físico distinto, y sólo la primera es irreversible.](figuras/fig_bifurcaciones.pdf)

**Silla-nodo.** Dos puntos fijos, uno estable y otro inestable, se acercan,
chocan y desaparecen. Es el mecanismo de los **puntos de no retorno**: el
sistema se queda sin equilibrio y salta a otro sitio. Cuando el parámetro
vuelve atrás, el equilibrio reaparece pero el sistema **ya no está allí**. De
aquí sale la histéresis y el colapso irreversible: pesquerías, ecosistemas,
mercados, la resistencia de un material.

**Transcrítica.** Dos puntos fijos se cruzan e intercambian estabilidad, pero
ninguno desaparece. Es el umbral epidémico: por debajo de $R_0=1$ el equilibrio
sin enfermedad es estable; por encima, se desestabiliza y el endémico toma el
relevo. Reversible.

**Horquilla.** Un equilibrio simétrico se desestabiliza y nacen dos simétricos.
Es la **ruptura espontánea de simetría**: el pandeo de una columna, la
magnetización de un ferromagneto, la elección entre dos estados equivalentes.
El sistema tiene que elegir, y lo que elige lo decide el ruido.

**Hopf.** Un foco estable se convierte en inestable y nace un ciclo límite a su
alrededor. Es el nacimiento de una **oscilación sostenida**: el latido de una
célula marcapasos, la vibración de un ala (*flutter*), el chirrido de una
tiza, el arranque de un láser, un oscilador electrónico.

::: aviso
**Detectar una bifurcación antes de que ocurra.** Cerca de una bifurcación, el
autovalor dominante tiende a cero, y por tanto el tiempo característico de
recuperación **tiende a infinito**. El sistema tarda cada vez más en volver
tras una perturbación pequeña.

Ese fenómeno —*ralentización crítica*— es medible y se ha propuesto como señal
de alarma temprana en lagos que van a eutrofizarse, en el clima, en poblaciones
al borde del colapso y en pacientes que van a sufrir una crisis epiléptica. Las
señales: aumento de la autocorrelación a un paso, aumento de la varianza y
recuperación cada vez más lenta.

No es infalible —hay bifurcaciones sin aviso y falsas alarmas— pero es una de
las ideas más útiles que salen de este capítulo (Scheffer et al., Nature 2009).
:::

### 4.3 El camino al caos, en una línea de código

El mapa logístico $x_{n+1}=rx_n(1-x_n)$ es una parábola. No hay nada más
simple. Y contiene toda la ruta al caos.

![Cascada de duplicación de periodo. Izquierda: los valores visitados a largo plazo en función de $r$. Derecha: telarañas que muestran el mecanismo para $r=2{,}8$ y $r=3{,}9$. Lo que hay que concluir: el caos no aparece de golpe, llega por una cascada infinita de duplicaciones que se acumulan en un punto finito.](figuras/fig_mapa_logistico.pdf)

Al aumentar $r$: un punto fijo estable, luego un ciclo de periodo 2 ($r=3$),
luego 4 ($r\approx3{,}449$), luego 8 ($3{,}544$), 16, 32... Los intervalos se
acortan geométricamente y se acumulan en $r_\infty\approx3{,}5699$, donde
empieza el caos.

El cociente entre intervalos sucesivos tiende a

$$\delta=4{,}669\,201\,6\ldots$$

la **constante de Feigenbaum**. Y aquí está lo que convirtió esto en un
resultado profundo y no en una curiosidad: ese número **es el mismo para
cualquier mapa unimodal suave con máximo cuadrático**. No depende de la
parábola. Es universal en el sentido preciso de la física estadística, y de
hecho Feigenbaum lo descubrió en 1975 en una calculadora HP-65 notando que los
números se repetían al cambiar de función.

Dentro del caos hay **ventanas** de comportamiento periódico, y la más ancha es
la de periodo 3 en $r\approx3{,}83$. No es una anécdota: el teorema de
Li y Yorke (1975) demuestra que **periodo 3 implica caos** —si un mapa continuo
tiene una órbita de periodo 3, tiene órbitas de todos los periodos—.

### 4.4 Lorenz: tres ecuaciones y un muro

$$\dot x=\sigma(y-x),\qquad \dot y=x(\rho-z)-y,\qquad \dot z=xy-\beta z$$

con $\sigma=10$, $\rho=28$, $\beta=8/3$. Es una caricatura brutal de la
convección atmosférica: tres modos de una expansión de Fourier truncada
salvajemente. Lorenz nunca pretendió que fuera realista.

![El sistema de Lorenz. Izquierda: el atractor. Arriba a la derecha: dos trayectorias que empiezan separadas $10^{-9}$. Abajo: su separación en escala logarítmica. Lo que hay que concluir: la separación crece exponencialmente con exponente $0{,}905$, y cuando alcanza el tamaño del atractor la predicción ha muerto.](figuras/fig_lorenz.pdf)

La medida de la separación da $\lambda=0{,}905$, frente al valor aceptado
$0{,}906$. Ese número, el **exponente de Lyapunov**, es la magnitud central:

$$d(t)\approx d_0\,e^{\lambda t}$$

::: herramientas
**Medir un exponente de Lyapunov sin equivocarse**

1. **Deja que la trayectoria caiga sobre el atractor primero.** Si empiezas
   fuera, el transitorio *contrae* y mides un exponente demasiado pequeño. (En
   el código de este capítulo, el ajuste sin este paso da 0,28 en lugar de
   0,90: un error del 70 % causado por tres líneas que faltaban.)
2. Perturba en una dirección arbitraria y mide $\ln d(t)$.
3. **Ajusta sólo en la zona de crecimiento exponencial**, antes de que $d$
   alcance el tamaño del atractor y sature.
4. Promedia sobre varias condiciones iniciales: el exponente local varía mucho
   a lo largo del atractor.
:::

### 4.5 El horizonte de predicción, y por qué es tan caro moverlo

Si tu error inicial es $\epsilon$ y toleras un error $\Delta$ en la predicción:

$$t_h=\frac{1}{\lambda}\ln\frac{\Delta}{\epsilon}$$

![El precio del caos. Lo que se ve: el horizonte de predicción en función de la precisión inicial, en un sistema caótico y en uno que no lo es. Lo que hay que concluir: en un sistema caótico el horizonte crece como el **logaritmo** de la precisión.](figuras/fig_horizonte.pdf)

Esa es la respuesta a la pregunta del principio. En Lorenz, con
$\lambda\approx0{,}9$, mejorar los datos iniciales por un factor **mil** alarga
el horizonte en $\ln(1000)/0{,}9\approx7{,}7$ unidades de tiempo. Un factor un
millón lo alarga en 15. En la atmósfera real, con un tiempo de duplicación de
error de entre uno y dos días, mejorar la red de observación por un factor 100
compra **una semana** de predicción, y ese es aproximadamente el techo teórico
que se estima en torno a las dos semanas.

No es una limitación tecnológica. **Es una propiedad de las ecuaciones.** Y
tiene una consecuencia metodológica que ha cambiado la meteorología: si no se
puede predecir la trayectoria, se predice la **distribución**. De ahí vienen
las predicciones por conjuntos (*ensembles*) y los porcentajes de probabilidad
de lluvia.

---

## 5. El ordenador entra en escena

::: antes
Vamos a integrar Lorenz con dos tolerancias distintas, $10^{-6}$ y $10^{-12}$,
desde exactamente la misma condición inicial. Antes de ejecutar:

* ¿Se parecerán las dos trayectorias a $t=5$? ¿Y a $t=40$?
* ¿Cuál de las dos es «la correcta»?
* ¿Tiene sentido preguntar cuál es la correcta?
:::

```python
import numpy as np
from scipy.integrate import solve_ivp

def lorenz(t, y):
    x, yy, z = y
    return [10*(yy - x), x*(28 - z) - yy, x*yy - (8/3)*z]

a = solve_ivp(lorenz, (0, 40), [1, 1, 1], rtol=1e-6,  dense_output=True)
b = solve_ivp(lorenz, (0, 40), [1, 1, 1], rtol=1e-12, dense_output=True)
```

Las dos trayectorias son indistinguibles hasta $t\approx20$ y completamente
distintas después. **Ninguna es correcta**: el error de redondeo actúa como una
perturbación inicial de tamaño $10^{-16}$, y esa perturbación crece igual que
cualquier otra. Al cabo de $\ln(10^{16})/0{,}9\approx41$ unidades de tiempo,
cualquier cálculo en doble precisión ha perdido toda relación con la
trayectoria «verdadera».

Y aquí viene el resultado que salva la situación: lo que **sí** se conserva son
las propiedades estadísticas. La media, la varianza, la forma del atractor, la
fracción de tiempo en cada lóbulo. Existe un teorema de sombreado (*shadowing*)
que garantiza, para ciertos sistemas, que la trayectoria numérica errónea es la
trayectoria exacta de una condición inicial ligeramente distinta. En términos
prácticos: **el clima se puede calcular aunque el tiempo no se pueda
predecir**.

::: juega
1. Integra Lorenz con $\rho=0{,}5$, $\rho=10$, $\rho=24$ y $\rho=28$. ¿Qué
   ocurre en cada caso? Localiza el valor de $\rho$ donde aparece el caos.
2. Con $\rho=350$, el sistema vuelve a ser periódico. Compruébalo. ¿Te lo
   esperabas?
3. Mide la fracción de tiempo que la trayectoria pasa en cada lóbulo, con
   `rtol=1e-6` y con `1e-12`. ¿Coinciden aunque las trayectorias no lo hagan?
4. Dibuja la sección de Poincaré (los máximos sucesivos de $z$) y comprueba
   que caen sobre una curva casi unidimensional. Acabas de reducir un sistema
   continuo 3D a un mapa 1D como el logístico.
:::

---

## 6. ¿Qué estamos suponiendo?

::: supuestos
1. **Que el sistema es autónomo y determinista.** Sin ruido externo. Un sistema
   con ruido puede parecer caótico sin serlo, y viceversa.
2. **Que el estado es de dimensión finita y conocida.** En un sistema real
   nunca lo sabemos: se estima con métodos de reconstrucción de espacio de
   fases (Takens).
3. **Que la linealización decide la estabilidad.** Falso cuando algún
   $\operatorname{Re}\lambda=0$: los casos marginales exigen ir a orden
   superior.
4. **Que el exponente de Lyapunov es una constante.** Es un promedio: el
   exponente local varía mucho a lo largo del atractor, y por eso hay días
   meteorológicos más predecibles que otros.
5. **Que las bifurcaciones son locales.** Existen bifurcaciones globales
   (colisiones con órbitas homoclínicas) que no se ven linealizando.
6. **Que el modelo de Lorenz describe la convección.** No lo hace: es una
   truncación de tres modos, y Lorenz lo sabía perfectamente.
:::

---

## 7. ¿Cuándo falla?

::: falla
**Falla el análisis lineal en el caso marginal.** Cuando el autovalor dominante
tiene parte real nula, todo depende de los términos no lineales despreciados.
Es exactamente lo que ocurre **en** la bifurcación, es decir, en el punto más
interesante.

**Falla confundir caos con ruido.** Una serie temporal caótica tiene espectro
ancho y autocorrelación que decae, igual que el ruido. Distinguirlos exige
mirar la estructura en el espacio de fases reconstruido, y con series cortas y
ruidosas —es decir, con datos reales— la distinción es genuinamente difícil.
La literatura de los años ochenta y noventa está llena de «caos de baja
dimensión» detectado en series económicas y fisiológicas que después no se
sostuvo.

**Falla la determinación de la dimensión con pocos datos.** El algoritmo de
Grassberger–Procaccia necesita un número de puntos que crece exponencialmente
con la dimensión. Aplicarlo a 500 datos y anunciar dimensión 5 es
metodológicamente insostenible.

**Falla el horizonte si la incertidumbre no es sólo inicial.** En meteorología
real, la incertidumbre del **modelo** —parametrizaciones, resolución— domina
sobre la de los datos iniciales a partir de cierto plazo. Mejorar los datos no
sirve si el modelo no reproduce la física.
:::

### Un anti-ejemplo: el atractor extraño que era un artefacto

Un grupo integra un sistema rígido con un método explícito y paso demasiado
grande. La solución numérica oscila de forma irregular y acotada, la sección de
Poincaré tiene estructura, el exponente de Lyapunov calculado sale positivo. Se
anuncia caos.

No hay caos: hay **inestabilidad numérica**. Un método explícito fuera de su
región de estabilidad produce oscilaciones crecientes que, combinadas con la no
linealidad del sistema, quedan acotadas y parecen un atractor. La comprobación
que lo delata es la del capítulo 8: **reduce el paso a la mitad**. Si el
«atractor» cambia de forma, es numérico. Si no cambia, puede que sea física.

Esa comprobación cuesta un minuto y no se hace casi nunca.

---

## 8. Historia

::: historia
**Lorenz, 1961: qué ocurrió realmente** · *Nivel de verificación: A.*

Edward Lorenz trabajaba en el MIT con un modelo meteorológico de 12 ecuaciones
en una Royal McBee LGP-30, una máquina de tubos de vacío que hacía unas 60
multiplicaciones por segundo. Quiso repetir una simulación y, para ahorrar
tiempo, la reinició por la mitad tecleando los valores que la impresora había
sacado.

La impresora imprimía tres decimales; la máquina trabajaba con seis. Lorenz
tecleó 0,506 donde el estado interno era 0,506127. Esperaba una diferencia
inapreciable. Al cabo de unos meses simulados, la nueva predicción no se
parecía en nada a la anterior.

Lo importante del episodio es lo que Lorenz hizo con él. La reacción normal
—y la suya, al principio— es sospechar de un fallo del hardware, que en una
máquina de tubos era de lo más plausible. Sólo después de descartar el fallo
aceptó que **el comportamiento era real**, y a partir de ahí construyó el
sistema de tres ecuaciones de 1963 buscando el ejemplo más simple posible.

El propio Lorenz lo cuenta en *The Essence of Chaos* (1993). Y aporta un matiz
que suele omitirse: el título de la charla de 1972, *«¿Provoca el aleteo de una
mariposa en Brasil un tornado en Texas?»*, **no era suyo**: se lo puso el
organizador de la sesión, Philip Merilees, porque Lorenz no había enviado
título a tiempo. La mariposa más famosa de la ciencia es obra de un
administrativo con prisa.

**Poincaré, cuarenta años antes** · *Nivel de verificación: A.*

La sensibilidad a las condiciones iniciales no la descubrió Lorenz. Henri
Poincaré la encontró en 1890, trabajando en el problema de los tres cuerpos
para un premio del rey Óscar II de Suecia. Y hay un detalle memorable: la
versión premiada de su memoria contenía un **error**; Poincaré lo descubrió
cuando ya estaba impresa, pagó de su bolsillo la retirada y reimpresión —más
de lo que había ganado con el premio— y la versión corregida es la que contiene
el descubrimiento de la dinámica homoclínica.

En *Science et Méthode* (1908) lo escribió con una claridad que no se ha
mejorado: una causa pequeñísima que se nos escapa determina un efecto
considerable que no podemos dejar de ver, y entonces decimos que ese efecto se
debe al azar.

**Por qué tardó setenta años en calar** · *Nivel B.*

La explicación habitual es que hacía falta el ordenador para *ver* el fenómeno,
y tiene mucho de cierto: nadie iba a iterar a mano miles de veces un mapa.
También hubo trabajo intermedio poco conocido —Cartwright y Littlewood en los
años cuarenta, estudiando la ecuación de van der Pol forzada por encargo del
gobierno británico durante la guerra, encontraron dinámicas extraordinariamente
complicadas—. La historia de «Lorenz descubrió el caos» es cómoda y falsa; la
más honesta es que el fenómeno se encontró varias veces y sólo se volvió
comunicable cuando se pudo dibujar.
:::

---

## 9. Problemas

En `problemas.md`; soluciones en `soluciones.md`.

---

## 10. Experimento computacional

::: experimento
**Caza la ralentización crítica.**

*Pregunta:* ¿se puede predecir un colapso antes de que ocurra, mirando sólo
las fluctuaciones?

*Diseño.* Toma el modelo de pesca del capítulo 6,
$\dot u = u(1-u)-h$, y añádele ruido: $du = [u(1-u)-h]dt + \sigma\,dW$.
Aumenta $h$ muy lentamente desde 0 hasta pasar de $h_c=1/4$.

*Análisis.* En ventanas deslizantes, calcula (a) la varianza de $u$ y (b) su
autocorrelación a un paso. Dibújalas frente a $h$.

*Qué esperar:* ambas deberían crecer al acercarse a $h_c$, porque el autovalor
dominante tiende a cero y el sistema se recupera cada vez más despacio.

*Qué falsaría la hipótesis:* si las señales sólo aparecen cuando el colapso ya
ha empezado, no sirven como alarma temprana. Mídelo: ¿con cuánta antelación
detectas la subida, en unidades de $h$? Compara con un caso de control donde
$h$ sube pero se detiene por debajo de $h_c$: ¿das falsas alarmas?
:::

---

## 11. Explícalo

::: explica
1. ¿Por qué un sistema de una sola variable no puede oscilar y uno de dos no
   puede ser caótico? Explícalo con la imagen de una curva que no puede
   cortarse a sí misma.
2. ¿Qué diferencia hay entre caos y azar, si las dos series parecen iguales?
3. Explica por qué mejorar mil veces la medida inicial sólo alarga la
   predicción un poquito.
4. ¿Qué significa que un colapso sea «irreversible», en términos de puntos
   fijos?
5. ¿Por qué el clima se puede calcular aunque el tiempo no se pueda predecir?
6. ¿Qué le dirías a alguien que ha encontrado un atractor extraño en su
   simulación?
:::

---

## 12. Lo esencial

::: esencial
* Un sistema dinámico es un campo de vectores. Casi todo el comportamiento
  cualitativo es geometría, no integración.
* La dimensión limita lo posible: 1D no oscila, 2D no es caótico, 3D ya
  permite todo.
* Los autovalores del jacobiano lo dicen todo cerca de un punto fijo: parte
  real = tasa, parte imaginaria = frecuencia. El caso marginal no lo decide la
  linealización.
* Cuatro bifurcaciones básicas, cuatro fenómenos: colapso irreversible
  (silla-nodo), umbral (transcrítica), ruptura de simetría (horquilla) y
  nacimiento de una oscilación (Hopf).
* Cerca de una bifurcación el sistema se recupera cada vez más despacio, y eso
  es medible: ralentización crítica como alarma temprana.
* El caos es determinista. Lo que impide predecir no es el azar, es la
  amplificación exponencial de la ignorancia inicial.
* $t_h=\lambda^{-1}\ln(\Delta/\epsilon)$: el horizonte crece como el
  **logaritmo** de la precisión. Es el resultado más caro del capítulo.
* Las trayectorias no se pueden calcular a largo plazo; las estadísticas, sí.
:::

---

## 13. Preguntas que quedan abiertas

::: abierto
* ¿Cómo se distingue caos de ruido con series cortas y ruidosas, es decir, con
  datos reales?
* Si el exponente de Lyapunov varía por el atractor, ¿se puede predecir *qué
  días* serán más predecibles? (La meteorología operativa lo intenta.)
* ¿Por qué la constante de Feigenbaum es universal? ¿Qué tiene que ver esto con
  los exponentes críticos de la física estadística?
* ¿Existen señales de alarma temprana fiables para bifurcaciones no locales, o
  sólo para las locales?
* Si toda trayectoria numérica de un sistema caótico es falsa, ¿en qué sentido
  exactamente confiamos en las simulaciones climáticas? (Capítulos 15 y II.10.)
:::
