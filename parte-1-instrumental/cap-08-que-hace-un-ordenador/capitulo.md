# Capítulo 8 — Qué hace realmente un ordenador cuando resuelve una ecuación

> **Qué sabrás hacer al terminar**
> · Saber qué error llevas puesto antes de calcular nada ·
> Medir empíricamente el orden de un método en dos líneas ·
> Distinguir un problema de precisión de uno de estabilidad ·
> Elegir integrador por sus propiedades y no por costumbre ·
> Pasar de una EDO a una EDP y entender de dónde sale la condición CFL.
>
> **Herramientas que usa:** capítulos 5, 6 y 7.
> **Disciplinas de los ejemplos:** mecánica celeste, cinética química,
> transferencia de calor, finanzas computacionales, gráficos.
> **Deuda que paga:** «¿qué hace el ordenador?», pendiente desde el capítulo 6.
> **Deuda que abre:** integradores simplécticos en serio (capítulo II.6) y
> condicionamiento de matrices (capítulo 11).

---

## 1. Una pregunta

::: pregunta
Escribes `0.1 + 0.2 == 0.3` en Python y devuelve `False`.

Y sin embargo confías en simulaciones que hacen $10^{12}$ operaciones de coma
flotante seguidas.

**¿Por qué funcionan, y cuándo dejan de funcionar?**
:::

Este capítulo es una sola idea repetida en cinco contextos: **el ordenador no
resuelve tu ecuación, resuelve otra parecida**. Toda la disciplina del cálculo
numérico consiste en saber cuánto se parece, y en detectar el momento en que
deja de parecerse.

---

## 2. Antes de calcular

::: antes
1. Si un método tiene error $\mathcal{O}(h^2)$ y reduces $h$ a la mitad,
   ¿cuánto baja el error? ¿Y si lo divides por 10?
2. ¿Qué pasa si sigues reduciendo $h$ indefinidamente?
3. Integras una órbita planetaria durante un millón de años. ¿Prefieres un
   método de orden 4 o uno de orden 1?

La tercera tiene una respuesta que parece absurda hasta la sección 4.5.
:::

---

## 3. La intuición

### 3.1 Tres errores distintos, tres remedios distintos

Cuando un resultado numérico está mal, la causa es una de estas tres, y
confundirlas hace perder días:

**Error de redondeo.** Los números reales no caben en 64 bits. Cada operación
introduce un error relativo del orden de $\epsilon_{\text{maq}}=2{,}2\times
10^{-16}$. *Se reduce* reformulando la fórmula, no bajando el paso.

**Error de truncamiento (o de discretización).** Hemos sustituido una derivada
por un cociente, una integral por una suma, un continuo por una malla. *Se
reduce* refinando la malla o subiendo el orden.

**Inestabilidad.** El método amplifica los errores en lugar de amortiguarlos.
*No se reduce* con nada: hay que cambiar de método o de paso, y el paso
correcto puede no tener nada que ver con la precisión que buscas.

La confusión más cara es entre la segunda y la tercera. Alguien ve un resultado
malo, reduce el paso, mejora un poco, lo reduce más, y no entiende por qué a
partir de cierto punto empeora. Vamos por partes.

---

## 4. La matemática

### 4.1 La aritmética que llevas puesta

![Tres caras de la coma flotante. Izquierda: la distancia al siguiente número representable crece con el valor. Centro: dos expresiones matemáticamente idénticas, una de ellas inutilizable. Derecha: el compromiso entre truncamiento y redondeo en una derivada numérica. Lo que hay que concluir: el error de redondeo no es un detalle, es un suelo que determina cuánto puedes refinar.](figuras/fig_coma_flotante.pdf)

**El panel izquierdo** dice lo esencial: la resolución es *relativa*. Cerca de
1, los `double` están separados $2\times10^{-16}$; cerca de $10^8$, están
separados $10^{-8}$. Por eso `0.1 + 0.2 != 0.3`: ninguno de los tres es
representable exactamente en binario, y la suma de dos aproximaciones no es la
aproximación de la suma.

**El panel central** muestra la **cancelación catastrófica**. Calcular
$(1-\cos h)/h^2$ para $h$ pequeño resta dos números casi iguales: se pierden
todas las cifras significativas de golpe. La expresión equivalente
$2[\sin(h/2)/h]^2$ no resta nada y es perfectamente estable. **La misma
matemática, aritméticas distintas.**

Regla operativa: **desconfía de toda resta entre cantidades parecidas**. Cuando
la veas, busca una reformulación algebraica. La fórmula de la ecuación de
segundo grado, la varianza calculada como $E[x^2]-E[x]^2$ y las diferencias
finitas son los tres sospechosos habituales.

**El panel derecho** contiene el compromiso fundamental de todo el capítulo.
Para una derivada numérica centrada:

$$\text{error} \approx \underbrace{\frac{h^2}{6}|f'''|}_{\text{truncamiento}}
+\underbrace{\frac{\epsilon_{\text{maq}}}{h}|f|}_{\text{redondeo}}$$

El primero baja con $h$; el segundo sube. Hay un óptimo en
$h^*\sim\epsilon_{\text{maq}}^{1/3}\approx6\times10^{-6}$, con un error mínimo
de $\sim10^{-11}$. **No se puede hacer mejor**, y si necesitas más precisión,
la solución no es un $h$ más pequeño: es la diferenciación automática o la
derivada compleja.

### 4.2 Discretizar: de la derivada al cociente

Todo integrador de EDO sale de una idea de una línea. Si

$$\frac{dy}{dt}=f(t,y)$$

entonces, integrando entre $t_n$ y $t_{n+1}=t_n+h$:

$$y_{n+1}=y_n+\int_{t_n}^{t_{n+1}} f(t,y(t))\,dt$$

y todo lo que sigue es **cómo aproximas esa integral sin conocer $y(t)$**:

* con el valor en el extremo izquierdo → **Euler explícito**;
* con el del extremo derecho → **Euler implícito** (que exige resolver una
  ecuación, porque $y_{n+1}$ aparece en los dos lados);
* con la media de ambos, estimando el derecho → **Heun**, o Euler mejorado;
* con cuatro evaluaciones bien elegidas → **Runge–Kutta 4**.

Los coeficientes de RK4 no son magia: salen de imponer que el desarrollo de
Taylor de la solución numérica coincida con el de la exacta hasta orden $h^4$.
Son cuatro condiciones sobre ocho coeficientes, y por eso hay una familia de
métodos RK4, no uno solo.

### 4.3 Orden: la única propiedad que hay que medir

Un método tiene **orden $p$** si el error global escala como $h^p$. Esto no se
cree: se comprueba, y se comprueba en dos líneas.

![El orden de un método es la pendiente en log-log. Izquierda: error global frente al paso para tres métodos, con las pendientes teóricas punteadas y el suelo de redondeo abajo a la izquierda. Derecha: lo mismo frente al coste real, es decir, evaluaciones de $f$. Lo que hay que concluir: la comparación honesta no es «a igual paso» sino «a igual coste».](figuras/fig_orden_convergencia.pdf)

Los órdenes medidos salen 1,12, 2,00 y 3,93 frente a los 1, 2 y 4 teóricos. Que
Euler dé 1,12 en vez de 1,00 no es un fallo: es que los pasos más grandes están
fuera del régimen asintótico, donde los términos de orden superior todavía
cuentan. **Ajustar la pendiente en la zona equivocada es un error habitual** y
la propia figura enseña a evitarlo.

Fíjate en el suelo de la izquierda del panel: por debajo de $h\approx10^{-4}$,
RK4 deja de mejorar y empieza a empeorar. Es el redondeo acumulado de más
pasos. **Refinar indefinidamente no funciona nunca.**

::: herramientas
**Comprobar el orden de tu código en dos líneas**

```python
e1 = error(h)        # error con paso h
e2 = error(h / 2)    # error con paso h/2
print(f"orden medido: {np.log2(e1 / e2):.2f}")
```

Si programas un método de orden 4 y esto te da 1, tienes un error de código.
Es el test más barato y más informativo del cálculo científico, y **debería
ejecutarse siempre antes de confiar en un resultado nuevo**. La mitad de los
errores de implementación se manifiestan como una pérdida de orden.
:::

El panel derecho contiene la lección económica: a igualdad de **coste**, RK4 es
unos nueve órdenes de magnitud más preciso que Euler. Comparar métodos «con el
mismo $h$» es engañoso, porque RK4 hace cuatro evaluaciones por paso. La
métrica honesta es error frente a número de evaluaciones de $f$, que es donde
está el tiempo de cálculo.

### 4.4 Estabilidad: cuando el paso no lo decides tú

Aplica un método a la ecuación de prueba $\dot y=\lambda y$. Euler explícito da
$y_{n+1}=(1+h\lambda)y_n$, luego

$$y_n=(1+h\lambda)^n y_0$$

Para que no explote hace falta $|1+h\lambda|<1$. Con $\lambda$ real negativo,
eso significa $h<2/|\lambda|$. **Y esa condición no tiene nada que ver con la
precisión que quieras**: es un límite duro.

![Estabilidad. Izquierda: regiones del plano complejo donde cada método no amplifica; el implícito es estable en todo el semiplano izquierdo. Derecha: $\dot y=-1000y$ integrada con dos pasos que difieren un 20 %. Lo que hay que concluir: cruzar el límite de estabilidad no degrada el resultado, lo destruye.](figuras/fig_estabilidad.pdf)

En el panel derecho, $\lambda=-1000$ y el límite es $h<0{,}002$. Con
$h=0{,}0018$ el resultado es correcto; con $h=0{,}0022$ —un 20 % más— la
solución oscila y crece sin control. No hay degradación gradual: hay un
acantilado.

**Rigidez.** Un problema es *rígido* cuando tiene escalas temporales muy
distintas y la rápida está muerta pero sigue imponiendo el paso. En el ejemplo
de dos compartimentos del capítulo 6, $k_1=30$ y $k_2=0{,}5$: la especie rápida
desaparece en 0,1 s, pero un método explícito sigue obligado a dar pasos de
$h<2/30$ durante los 12 s completos de simulación. Se gastan miles de pasos
resolviendo con exquisito detalle algo que ya no existe.

La solución son los **métodos implícitos**, estables para cualquier $h$ en todo
el semiplano izquierdo. Cuestan más por paso —hay que resolver un sistema de
ecuaciones— pero pueden dar pasos miles de veces mayores. En SciPy, esto es la
diferencia entre `method='RK45'` y `method='Radau'` o `'BDF'`, y **elegir mal
puede significar horas frente a segundos**.

Regla de diagnóstico: si tu simulación va inexplicablemente lenta y el paso
adaptativo se queda diminuto, tienes un problema rígido, no un problema difícil.

### 4.5 Cuando el orden no es lo que importa

Aquí llega la respuesta a la tercera pregunta de la sección 2, y es
contraintuitiva.

![Cuatro métodos integrando un oscilador armónico durante 2000 periodos. Izquierda: la energía, que debería ser constante. Derecha: el plano de fases al final. Lo que hay que concluir: Euler explícito explota, Euler implícito amortigua hasta cero, RK4 se degrada lentamente y el simpléctico —de orden 1— conserva la energía indefinidamente.](figuras/fig_energia_integradores.pdf)

Los cuatro empiezan igual. Después de 2000 periodos:

| Método | Orden | Energía final (exacta: 0,5) |
|---|---|---|
| Euler explícito | 1 | $10^{43}$ |
| Euler implícito | 1 | 0,0000 |
| Runge–Kutta 4 | 4 | 0,5000 |
| **Euler simpléctico** | **1** | **0,5119, oscilando sin deriva** |

El método simpléctico es de orden 1 —el peor de la lista en precisión a corto
plazo— y es el único que se comporta bien a largo plazo. La diferencia con
Euler explícito es **el orden de dos líneas de código**: actualizar primero el
momento y después la posición usando el momento ya actualizado.

La razón es profunda: el método simpléctico conserva exactamente el área en el
espacio de fases, igual que el flujo hamiltoniano verdadero. No resuelve la
ecuación original, pero resuelve exactamente **otro hamiltoniano muy próximo**,
y por eso su energía oscila alrededor del valor correcto en vez de derivar.

La lección general, que vale mucho más allá de la mecánica: **elige el método
que respete la estructura del problema, no el que tenga el número más alto.**
Si hay una cantidad conservada, busca un método que la conserve. El capítulo
II.6 desarrolla esto con órbitas planetarias.

### 4.6 De la EDO a la EDP

La ecuación del calor $\partial_t u = D\,\partial_x^2 u$ se discretiza
sustituyendo la segunda derivada por su diferencia centrada:

$$u_j^{n+1}=u_j^n+r\,(u_{j+1}^n-2u_j^n+u_{j-1}^n),\qquad r=\frac{D\,\Delta t}{\Delta x^2}$$

Un análisis de von Neumann —introducir un modo $u_j^n=\xi^n e^{ikj\Delta x}$ y
exigir $|\xi|\le1$— da la condición

$$\boxed{\ r=\frac{D\,\Delta t}{\Delta x^{2}}\le\frac12\ }$$

![La condición CFL en acción. Izquierda: $r=0{,}49$, la solución difunde como debe. Derecha: $r=0{,}51$, un 4 % por encima, y la solución oscila y crece. Lo que hay que concluir: refinar la malla espacial obliga a reducir el paso temporal **al cuadrado**.](figuras/fig_cfl_calor.pdf)

La consecuencia práctica es brutal: si duplicas la resolución espacial para
tener más detalle, tienes que **dividir por cuatro** el paso temporal, y por
tanto el coste total se multiplica por ocho. Esa relación cuadrática es la que
hace caros los métodos explícitos para problemas parabólicos, y la razón de que
en la práctica se usen esquemas implícitos como Crank–Nicolson.

Para la ecuación de advección la condición es distinta —$c\Delta t/\Delta x\le
1$, la CFL clásica— y tiene una interpretación física preciosa: **la
información no puede viajar más de una celda por paso**. Si tu esquema numérico
mira menos lejos de lo que la física mueve la señal, no puede funcionar.

---

## 5. El ordenador entra en escena

::: antes
Vamos a escribir Euler y RK4 a mano y medir su orden. Antes:

* ¿Cuántas líneas crees que ocupa RK4?
* ¿Qué esperas que dé `np.log2(e(h)/e(h/2))` para cada uno?
* ¿A partir de qué $h$ dejará de mejorar RK4?
:::

```python
def rk4(f, y, t, h):
    k1 = f(t, y)
    k2 = f(t + h/2, y + h*k1/2)
    k3 = f(t + h/2, y + h*k2/2)
    k4 = f(t + h,   y + h*k3)
    return y + h*(k1 + 2*k2 + 2*k3 + k4)/6
```

Seis líneas. Y esas seis líneas son lo que hay debajo de una fracción enorme de
la simulación científica del mundo. Merece la pena escribirlas al menos una
vez, comprobar que dan orden 4, y sólo después usar `solve_ivp` sabiendo qué
hay dentro.

::: juega
1. Rompe RK4 a propósito: cambia el $2$ de $k_2$ por un $3$. ¿Sigue funcionando?
   ¿Qué orden mide? (Respuesta: sigue dando resultados razonables y el orden
   cae a 2. Por eso el test de orden detecta errores que la vista no.)
2. Integra $\dot y=-1000y+1000\cos t$ con `RK45` y con `Radau`. Compara el
   número de pasos y el tiempo.
3. Con el oscilador armónico, cambia el orden de las dos líneas del método
   simpléctico. ¿Sigue conservando la energía? ¿Por qué?
4. En la ecuación del calor, prueba $r=0{,}5$ exactamente. ¿Estable o
   inestable? ¿Qué te dice eso sobre trabajar en el límite?
:::

---

## 6. ¿Qué estamos suponiendo?

::: supuestos
1. **Que $f$ es suave.** Los órdenes de convergencia suponen derivadas
   continuas hasta orden $p+1$. Con una $f$ discontinua (un choque, un control
   tipo on/off, una tabla interpolada), el orden efectivo cae a 1 o menos, y
   ninguna tolerancia lo arregla.
2. **Que la solución no es rígida**, si usas un método explícito.
3. **Que el error de redondeo es despreciable frente al de truncamiento.**
   Falso para $h$ muy pequeño o simulaciones muy largas.
4. **Que la tolerancia local controla el error global.** No lo hace: los
   integradores adaptativos controlan el error **por paso**, y el global se
   acumula de forma que depende de la estabilidad del problema.
5. **Que el problema está bien condicionado.** Si la solución exacta es
   sensible a los datos, ningún método lo arregla: eso no es un problema
   numérico sino del problema.
6. **Que doble precisión basta.** Casi siempre sí; en integraciones de sistemas
   caóticos a largo plazo, no.
:::

---

## 7. ¿Cuándo falla?

::: falla
**Falla al refinar demasiado.** El error total tiene forma de V: baja con el
truncamiento y sube con el redondeo. Reducir $h$ por debajo del óptimo empeora
el resultado. Si alguien te dice «he usado un paso muy pequeño para asegurarme»,
desconfía.

**Falla cuando la tolerancia no controla lo que crees.** `rtol=1e-8` no
significa que tu respuesta tenga ocho cifras correctas. Significa que el error
estimado *por paso* está por debajo de eso. En un problema inestable, el error
global puede ser millones de veces mayor. La única comprobación válida es
**repetir con la tolerancia dividida por 100 y ver cuántas cifras se mueven**.

**Falla con eventos y discontinuidades.** Un integrador adaptativo que
atraviesa una discontinuidad sin detectarla produce basura silenciosa. Hay que
usar detección de eventos (`events` en `solve_ivp`) y parar la integración en
la discontinuidad.

**Falla la conservación con métodos no geométricos.** RK4 disipa energía
lentamente. En una simulación de un millón de años, eso significa que los
planetas caen en espiral hacia el Sol. No es física: es el integrador.

**Y falla el criterio «más orden es mejor».** Un método de orden 8 con paso
grande puede ser peor que uno de orden 4, y un simpléctico de orden 1 puede
batir a ambos si lo que te importa es la estructura y no la trayectoria.
:::

### Un anti-ejemplo: el resultado que convergía a lo que no era

Un grupo resuelve una EDP con diferencias finitas. Refinan la malla: los
resultados convergen limpiamente, con orden 2, a un valor bien definido.
Publican.

El problema: habían implementado mal la condición de contorno, con un orden 1
en el borde. El esquema converge —sí— pero converge a la solución de **otro
problema**, uno con una condición de contorno ligeramente distinta. La
convergencia es una comprobación de consistencia interna, **no de corrección**.

La comprobación que lo habría detectado es el **método de las soluciones
manufacturadas**: elige una función analítica cualquiera, calcula qué término
fuente haría que fuese solución exacta de tus ecuaciones, mételo en el código y
comprueba que recuperas la función con el orden esperado, **condiciones de
contorno incluidas**. Es la técnica estándar de verificación en ingeniería
computacional (Roache 1998) y se usa muchísimo menos de lo que debería.

---

## 8. Historia

::: historia
**Euler, y el método que todos usamos sin saberlo** ·
*Nivel de verificación: A.*

En *Institutionum calculi integralis* (1768), Euler describió el método de dar
pasos pequeños siguiendo la pendiente. Lo interesante es el contexto: no lo
planteó como una aproximación de segunda categoría, sino como **la definición
constructiva** de lo que significa que una ecuación diferencial tenga solución.
La existencia de soluciones se demuestra hoy, en el teorema de Peano, tomando
el límite de poligonales de Euler.

**Runge, Kutta y la necesidad práctica** · *Nivel de verificación: A.*

Carl Runge publicó su método en 1895 motivado por cálculos de trayectorias
balísticas y de física atmosférica; Martin Kutta lo generalizó en 1901 en su
tesis. Ninguno de los dos buscaba elegancia: buscaban precisión aceptable con
el mínimo número de evaluaciones, **porque las evaluaciones las hacía una
persona a mano**.

Merece la pena detenerse en esto. El criterio de diseño de RK4 —minimizar
evaluaciones de $f$ para un orden dado— nació de que cada evaluación costaba
minutos de trabajo humano. Ese mismo criterio sigue siendo el correcto hoy, por
una razón completamente distinta: hoy $f$ puede ser una simulación de fluidos
de una hora. Los buenos criterios de diseño sobreviven al cambio de la
tecnología que los motivó.

**Richardson y la fábrica de predicción** · *Nivel de verificación: A.*

Lewis Fry Richardson intentó en 1917, en los ratos libres de su trabajo como
conductor de ambulancias en el frente francés, la primera predicción numérica
del tiempo: seis horas de pronóstico, calculadas a mano durante seis semanas.
El resultado fue **catastróficamente erróneo**: predijo un cambio de presión de
145 hPa en seis horas, cuando la realidad fue de unos pocos hPa.

En su libro de 1922 imaginó una «fábrica de predicción»: un teatro esférico
gigantesco con 64 000 computistas humanos, cada uno responsable de una celda de
la malla, coordinados por un director con focos de colores. Es la primera
descripción de una arquitectura de cálculo paralelo, treinta años antes de que
existieran los ordenadores.

Y hay un epílogo instructivo. En 1979, Peter Lynch reanalizó los cálculos de
Richardson y demostró que **el método era correcto**: el fallo venía de que los
datos iniciales contenían ondas de gravedad espurias que el esquema amplificó.
Con un filtrado adecuado de los datos iniciales —una técnica que no existía en
1922— la predicción de Richardson es razonable. Tardó sesenta años en quedar
demostrado que no se había equivocado, sólo se había adelantado.

**Von Neumann y el análisis de estabilidad** · *Nivel de verificación: A.*

El criterio de estabilidad que usamos en la sección 4.6 lleva el nombre de John
von Neumann, que lo desarrolló en Los Álamos durante los años cuarenta
trabajando en cálculos de ondas de choque. La técnica —descomponer el error en
modos de Fourier y exigir que ninguno crezca— apareció en un artículo de
Crank y Nicolson (1947) y en el trabajo de Charney, Fjørtoft y von Neumann
(1950) sobre la primera predicción meteorológica hecha con ordenador, en el
ENIAC.

Aquella predicción del ENIAC de 1950 tardó unas 24 horas de cálculo en producir
un pronóstico de 24 horas: exactamente en el límite de la inutilidad. Pero
funcionó, y con ella empezó la meteorología moderna.
:::

---

## 9. Problemas

En `problemas.md`; soluciones en `soluciones.md`.

---

## 10. Experimento computacional

::: experimento
**Verifica tu propio integrador con soluciones manufacturadas.**

*Pregunta:* ¿tu código resuelve la ecuación que tú crees?

*Diseño.* Elige una solución arbitraria, por ejemplo
$u(x,t)=e^{-t}\sin(\pi x)+x^2$. Sustitúyela en tu EDP y calcula el término
fuente $S(x,t)$ que la haría solución exacta. Añade $S$ al código, impón las
condiciones de contorno que esa función exige, y resuelve.

*Análisis.* Mide el error frente a la solución conocida y refina la malla.
Comprueba que el orden observado coincide con el teórico **en el interior y en
los bordes por separado**.

*Qué falsaría la implementación:* un orden menor del esperado en el borde
delata una condición de contorno mal discretizada; en el interior, un error en
el esquema. Es la única prueba que distingue «converge» de «converge a lo
correcto», y detecta la clase de error del anti-ejemplo de la sección 7.
:::

---

## 11. Explícalo

::: explica
1. ¿Por qué `0.1 + 0.2 != 0.3`, y por qué eso no impide simular el clima?
2. Explica sin fórmulas por qué reducir el paso indefinidamente empeora el
   resultado.
3. ¿Qué diferencia hay entre que un método sea inestable y que sea impreciso?
4. ¿Por qué un método de orden 1 puede batir a uno de orden 4 en una
   integración larga?
5. Explica la condición CFL en términos de información que viaja.
6. ¿Qué le dirías a alguien que afirma que su resultado es correcto porque «he
   usado una tolerancia de $10^{-10}$»?
:::

---

## 12. Lo esencial

::: esencial
* El ordenador no resuelve tu ecuación: resuelve otra parecida. Todo consiste
  en saber cuánto.
* Tres errores distintos —redondeo, truncamiento, inestabilidad— con tres
  remedios distintos. Confundirlos cuesta días.
* La cancelación catastrófica se cura reformulando el álgebra, no bajando el
  paso.
* El orden se mide, no se cree: `log2(e(h)/e(h/2))`. Es el test más barato del
  cálculo científico.
* Compara métodos a igual **coste**, no a igual paso.
* La estabilidad impone un paso máximo que no tiene nada que ver con tu
  precisión. Cruzarlo no degrada: destruye.
* Si el paso adaptativo se hace diminuto sin razón, tu problema es rígido:
  cambia a implícito.
* Elige el método que respete la estructura (conservación, simplecticidad), no
  el del número más alto.
* Convergencia no es corrección: usa soluciones manufacturadas.
:::

---

## 13. Preguntas que quedan abiertas

::: abierto
* Si la tolerancia local no controla el error global, ¿cómo se acota el error
  global de verdad en un problema no lineal?
* ¿Existen métodos que conserven a la vez la energía y el volumen de fases?
  (Pista: hay un teorema que dice que no, salvo casos triviales.)
* ¿Qué significa «resolver» una ecuación cuya solución es caótica, si ninguna
  trayectoria numérica es la verdadera?
* ¿Cuánto de la incertidumbre de una simulación climática es numérica y cuánto
  es física? ¿Se puede separar?
* Si la diferenciación automática elimina el compromiso truncamiento/redondeo
  de las derivadas, ¿por qué seguimos usando diferencias finitas?
:::
