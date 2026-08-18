## Soluciones del capítulo 8

> Las soluciones son razonadas: el número final es lo menos importante. En los
> problemas ● y ★ con solución cerrada hay **Pista 1** y **Pista 2** antes de
> ella; tápalas con la mano y úsalas de una en una.
>
> Los de **Mundo real** (R) no llevan solución a propósito: su procedimiento
> está en el apéndice D.

---

### Calentamiento

**8.C1** Orden 3: $e\propto h^3$. Con $h/10$, el error baja $10^3$: $10^{-7}$.
Con $h=10^{-6}$ **la predicción falla**, porque estaríamos en $10^{-4}\times
10^{-15}=10^{-19}$, por debajo del suelo de redondeo. Ahí manda el redondeo y
el error vuelve a subir.

**8.C2** $h<2/50=0{,}04$ en ambos casos. El término forzante **no afecta a la
estabilidad**, que depende sólo de la parte homogénea, es decir, de los
autovalores del jacobiano. Es un punto que se confunde a menudo.

**8.C3** (a) $\frac{1}{\sqrt{x+1}+\sqrt{x}}$. (b) `np.log1p(x)`, que existe
precisamente para esto. (c) Calcula la raíz grande con la fórmula habitual y la
pequeña como $c/(a x_{\text{grande}})$, usando el producto de raíces.

**8.C4** $\Delta t \le \Delta x^2/(2D)=10^{-6}/(2\times10^{-5})=0{,}05$ s. Si
refinas a $\Delta x=0{,}1$ mm, baja a 0,5 ms: **cien veces menor** por refinar
diez veces.

---

### Estimación

**8.E1** Un procesador moderno hace $\sim10^{10}$–$10^{11}$ flops/s; en una
hora, $\sim10^{14}$. En el peor caso, los errores se suman:
$10^{14}\times10^{-16}=10^{-2}$, un 1 %: **inaceptable**. En un caso realista
los errores son aleatorios e independientes y crecen como $\sqrt N$:
$10^{7}\times10^{-16}=10^{-9}$. Es la misma raíz cuadrada del capítulo 1 y la
razón por la que el cálculo numérico funciona en la práctica. La diferencia
entre los dos escenarios es de siete órdenes de magnitud y depende de si los
errores están correlacionados, que es exactamente lo que hace peligrosa una
suma de muchos términos del mismo signo.

**8.E2** Superficie terrestre $5\times10^{14}$ m², con celdas de 1 km²:
$5\times10^{8}$ columnas, por ~100 niveles verticales: $5\times10^{10}$ celdas.
CFL con $c\approx300$ m/s (ondas de gravedad) y $\Delta x=1$ km:
$\Delta t\lesssim3$ s, luego $\sim3\times10^4$ pasos por día. Total
$\sim10^{15}$ actualizaciones de celda al día, con decenas de operaciones cada
una. Sale del orden de $10^{16}$–$10^{17}$ flops: horas en un
superordenador. Coincide con la realidad operativa.

**8.E3** ● *Pista 1:* la memoria sale de multiplicar celdas por bytes por número de campos; hazlo antes de pensar en el método.
*Pista 2:* para elegir método compara **el número total de pasos**, no el coste de un paso. El explícito paga $\Delta t\propto\Delta x^2$; el implícito paga resolver un sistema enorme.
*Solución:* $10^9$ celdas × 8 bytes = 8 GB por campo, y hacen falta varios:
del orden de 50–100 GB. Explícito: $\Delta t\propto\Delta x^2$, muchísimos
pasos, pero cada uno es $O(N)$ y trivialmente paralelizable. Implícito: pasos
grandes, pero hay que resolver un sistema de $10^9$ incógnitas por paso, que con
un método iterativo multigrid es $O(N)$ pero con constante alta. **El implícito
gana cuando el tiempo total simulado es mucho mayor que el tiempo de difusión
de una celda**, que es el caso habitual en problemas de conducción lenta.

---

### Modelado

**8.M1** El explícito necesita $h<2\times10^{-6}$ s por estabilidad, y hay que
simular $3600$ s: $1{,}8\times10^{9}$ pasos. Con un implícito, el paso lo fija
la precisión de la dinámica lenta, digamos 1 s: $3600$ pasos. **Un factor
$5\times10^5$**, aunque cada paso implícito cueste veinte veces más. Es la
diferencia entre un mes y un segundo.

**8.M2** El integrador adaptativo intenta reducir el paso indefinidamente cerca
del cambio de signo, y puede quedarse atascado o devolver basura. Tratamiento
correcto: **detección de eventos**. Se integra hasta el cruce por cero, se para,
se cambia la ecuación y se reinicia. En SciPy, `events=` con `terminal=True`.

**8.M3** ● *Pista 1:* la cantidad que no puede derivar en $10^9$ años es la energía, así que el método tiene que conservarla estructuralmente, no por casualidad.
*Pista 2:* cuidado con el paso adaptativo: rompe justo la propiedad que te interesa. Y cuidado con el acumulador de tiempo, que suma $10^{12}$ veces.
*Solución:* Método: integrador simpléctico de alto orden (Wisdom–Holman o
Yoshida) con paso fijo, porque el paso adaptativo **destruye la simplecticidad**.
Paso: una fracción pequeña (∼1/20) del periodo orbital más corto. Precisión:
doble no basta a $10^9$ años para todos los fines; se usa suma compensada de
Kahan para el acumulador de tiempo. Comprobaciones: deriva de energía y de
momento angular, reversibilidad temporal, y comparación con integraciones a
paso mitad. Y una advertencia: el sistema solar es caótico con un tiempo de
Lyapunov de ~5 millones de años, así que a $10^9$ años **las trayectorias
individuales no significan nada** y sólo son interpretables las estadísticas
sobre muchas condiciones iniciales.

---

### Derivación

**8.D1** $y(t+h)=y+hy'+\tfrac{h^2}{2}y''+\dots$, y Euler retiene sólo los dos
primeros: error local $\tfrac{h^2}{2}|y''|=O(h^2)$. En $T/h$ pasos, los errores
locales se acumulan: $O(h^2)\times O(1/h)=O(h)$. **El error global es siempre un
orden menor que el local.**

**8.D2** $y_{n+1}=(1+z+z^2/2)y_n$ con $z=h\lambda$. En el eje real negativo,
$|1+z+z^2/2|<1$ para $-2<z<0$: el mismo intervalo que Euler. Pero en el eje
imaginario, Heun sí contiene un trozo mientras que Euler no contiene ninguno,
que es la razón de que Euler explícito no sirva para problemas oscilatorios.

**8.D3** ● *Pista 1:* mete $u_j^n=\xi^n e^{ikj\Delta x}$ en el esquema y despeja el factor de amplificación $\xi$.
*Pista 2:* la condición de estabilidad es $|\xi|\le1$ **para todo $k$**, así que busca el caso peor: el modo que oscila celda a celda.
*Solución:* Con $u_j^n=\xi^n e^{ikj\Delta x}$:
$\xi=1+r(e^{ik\Delta x}-2+e^{-ik\Delta x})=1-4r\sin^2(k\Delta x/2)$. El caso
peor es $\sin^2=1$: $\xi=1-4r$, y $|\xi|\le1$ exige $r\le1/2$. Para el
implícito, $\xi=1/[1+4r\sin^2(\cdot)]$, que es $\le1$ **siempre**: estable sin
condiciones.

**8.D4** ● *Pista 1:* escribe un paso como una matriz $2\times2$ que actúa sobre $(q,p)$.
*Pista 2:* conservar el área en el espacio de fases es que esa matriz tenga determinante 1. Calcúlalo para los dos métodos y compara.
*Solución:* Un paso de Euler simpléctico es
$\begin{pmatrix}q'\\p'\end{pmatrix}
=\begin{pmatrix}1-h^2 & h\\ -h & 1\end{pmatrix}
\begin{pmatrix}q\\p\end{pmatrix}$, con determinante
$(1-h^2)\cdot1+h\cdot h=1$ **exactamente**, para cualquier $h$. Euler explícito
da $\begin{pmatrix}1&h\\-h&1\end{pmatrix}$ con determinante $1+h^2>1$: **infla
el área en cada paso**, y por eso la energía crece exponencialmente. La
diferencia entre conservar y no conservar es un $h^2$ en el determinante.

---

### Computacional

**8.P1** Cambiar un coeficiente de RK4 casi siempre reduce el orden a 2 sin
que el resultado parezca mal a ojo: la solución sigue siendo cualitativamente
correcta. Por eso el test de orden es imprescindible: **detecta errores que la
inspección visual no**.

**8.P2** El óptimo teórico es $h^*\sim(\epsilon/C)^{1/(p+1)}$; para RK4,
$\epsilon^{1/5}\approx10^{-3}$, y ahí el error mínimo es
$\sim\epsilon^{4/5}\approx10^{-13}$. Coincide bien con la simulación.

**8.P3** `RK45` gasta del orden de $10^4$–$10^5$ evaluaciones; `Radau`, unos
cientos. La diferencia crece proporcionalmente al cociente de constantes de
tiempo.

---

### Experimento

**8.X1** Euler explícito: energía $\propto e^{h t}$ (crece exponencialmente).
Euler implícito: $\propto e^{-ht}$ (decae). RK4: deriva **lineal** en $t$, con
pendiente $\propto h^4$. Simpléctico: **oscila acotada, sin deriva secular**.
Esa distinción —deriva secular frente a oscilación acotada— es lo único que
importa en integraciones largas y no aparece en el concepto de orden.

**8.X2** ● *Pista 1:* mide el orden con el refinamiento habitual, pero mide el error **del interior** y **del borde** por separado.
*Pista 2:* si el orden global sale un número raro entre 1 y 2, no es un error tuyo: es la mezcla de dos órdenes distintos ponderada por cuántas celdas hay de cada clase.
*Solución:* Con un error de orden 1 en el borde, el orden global observado cae
de 2 a aproximadamente 1,5 (el error del borde se propaga al interior
atenuado). Que el orden observado no sea ni 1 ni 2 sino algo intermedio es
característico y confunde a mucha gente; la solución es medir el error **por
separado en el interior y en la primera capa de celdas**.

---

### Detective

**8.T1** El razonamiento supone que la última tolerancia probada es la buena. La
comprobación correcta es al revés: se baja la tolerancia hasta que el resultado
**deja de cambiar** en las cifras que te interesan, y se comprueba con dos
niveles más. Que cambie al pasar de $10^{-12}$ a $10^{-14}$ significa que
$10^{-12}$ no bastaba, no que $10^{-14}$ baste. Y en un problema caótico puede
que ninguna tolerancia baste para la trayectoria.

**8.T2** No es despreciable si la simulación dura microsegundos: 0,1 % por ns
son mil pasos de 0,1 %, es decir un factor $e$ en energía. La pregunta correcta
es **¿cuánto dura la simulación en unidades de esa deriva?**, y la comprobación
es dibujar la energía frente al tiempo y ver si la deriva es secular o acotada.
En dinámica molecular, una deriva secular indica paso demasiado grande o un
termostato mal configurado.

**8.T3** ● *Pista 1:* separa dos preguntas que se confunden siempre: ¿resuelve el código las ecuaciones que dice? y ¿son esas las ecuaciones correctas?
*Pista 2:* antes de tocar el modelo, comprueba si un 15 % está dentro de la incertidumbre de las propiedades del material y del propio experimento.
*Solución:* En orden: (1) **verificación**: ¿resuelve el código las ecuaciones
que dice? Soluciones manufacturadas, orden en interior y bordes. (2)
**validación de entradas**: propiedades del material, geometría, condiciones de
contorno; un 15 % es exactamente el orden de la incertidumbre de muchas
propiedades tabuladas. (3) **incertidumbre experimental**: ¿tiene el
experimento un 15 % de incertidumbre sistemática? Sólo después de las tres, y
declarando la incertidumbre de ambos lados, se puede hablar de discrepancia. La
conclusión «el experimento está mal» es la última de la lista, no la primera.

---

### Feynman

**8.F1** Guion: «No la resuelve. Coge el estado de ahora, mira la regla que le
dice hacia dónde va, avanza un pasito en esa dirección, y vuelve a mirar. Como
la dirección cambia durante el paso, siempre se equivoca un poco. Todo el
oficio consiste en dar pasos tan pequeños que el error no importe, pero no tan
pequeños que los errores de redondear cada número acaben pesando más que el
error de la dirección.»

**8.F2** Guion: «En la realidad, una perturbación se mueve a cierta velocidad.
En tu malla, en un paso sólo puedes enterarte de lo que hacen las celdas
vecinas. Si en ese tiempo la señal real ha recorrido tres celdas, tu cálculo
está usando información que no le ha llegado, y lo que sale no es una versión
imprecisa de la realidad: es basura que además crece.»

---

### Extensión

**8.Z1** ★ *Pista 1:* el esquema de Richardson no estaba mal. Busca el problema en los **datos iniciales**, no en el método.
*Pista 2:* pregúntate qué modos rápidos contenían esos datos y qué les hace un esquema explícito con un paso de seis horas.
*Solución:* La lección es que **el esquema numérico y los datos iniciales no son
problemas independientes**. El método de Richardson era correcto, pero sus
datos contenían modos rápidos (ondas de gravedad) espurios que el esquema
amplificó. La solución moderna —inicialización por modos normales,
asimilación variacional de datos— consiste en proyectar los datos sobre el
subespacio de soluciones «lentas» antes de integrar. Generalizando: **si tu
sistema tiene modos rápidos que no te interesan, los datos iniciales tienen que
ser compatibles con esa separación o el modo rápido dominará la solución.**

**8.Z2** ★ *Pista 1:* el análisis hacia atrás no pregunta cuánto se equivoca el método, sino a qué problema le da la respuesta exacta.
*Pista 2:* aplícalo a un integrador simpléctico y saldrá un hamiltoniano modificado. Eso explica por qué la energía oscila en vez de derivar.
*Solución:* El análisis hacia atrás dice que un integrador simpléctico resuelve
exactamente un hamiltoniano modificado $H+h^2H_2+h^4H_4+\dots$, y por eso su
energía oscila en vez de derivar. Otras técnicas con interpretación análoga:
la eliminación gaussiana con pivoteo (resuelve exactamente un sistema con una
matriz ligeramente perturbada, Wilkinson 1961); los métodos de mínimos
cuadrados numéricamente estables; y los esquemas de viscosidad artificial en
fluidos, que resuelven exactamente unas ecuaciones con un término disipativo
añadido. Preguntar «¿qué problema resuelve exactamente mi algoritmo?» es una de
las preguntas más fértiles del análisis numérico.
