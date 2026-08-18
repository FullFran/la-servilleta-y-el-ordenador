# II.12 — ¿Cuánto hay que esperar?

> **El fenómeno:** el supermercado tiene diez cajas y sólo cuatro abiertas.
> **Herramientas:** cap. 3 (exponencial), cap. 4 (Poisson y paradoja del
> autobús), cap. 9 (simulación).
> **Lo que hay que llevarse:** que la espera no crece proporcionalmente a la
> carga sino que diverge, y que la variabilidad hace tanto daño como la carga.

---

## 1. Una pregunta

::: pregunta
Un servidor procesa 100 peticiones por segundo y le llegan 90.

Está al 90 % de utilización, con un 10 % de margen.

**¿Cuánto tiempo espera una petición, comparado con un servidor al 50 %?**

La respuesta es **diez veces más**, no dos.
:::

---

## 2. Antes de calcular

::: antes
1. Tu respuesta a la pregunta anterior.
2. ¿Es mejor una cola única para 5 cajas o 5 colas independientes?
3. Si reduces a la mitad la variabilidad del tiempo de servicio sin cambiar la
   media, ¿cuánto mejora la espera?
:::

---

## 3. La divergencia

![Espera frente a utilización. Izquierda: la fórmula M/M/1 y la M/D/1, con los puntos de $\rho=0{,}5$, 0,8 y 0,95. Derecha: simulación por eventos discretos con tres variabilidades del servicio. Lo que hay que concluir: la espera diverge como $1/(1-\rho)$, y la variabilidad del servicio multiplica el resultado.](figuras/fig_colas.pdf)

Para la cola más simple —llegadas de Poisson, servicio exponencial, un
servidor— el tiempo medio en el sistema es

$$W=\frac{1/\mu}{1-\rho},\qquad \rho=\frac{\lambda}{\mu}$$

| $\rho$ | $W$ (en unidades de servicio) |
|---|---|
| 0,50 | 2 |
| 0,80 | 5 |
| 0,90 | **10** |
| 0,95 | **20** |
| 0,99 | **100** |

**No hay degradación gradual.** La última unidad de utilización cuesta
muchísimo más que la primera, y por eso ningún sistema con variabilidad se
puede operar cerca del 100 %.

La razón intuitiva: cerca de la saturación, cualquier ráfaga de llegadas crea
una cola que tarda muchísimo en drenar, porque el servidor apenas tiene
capacidad sobrante. La espera media está dominada por esos episodios raros y
largos, que es la cola pesada del capítulo II.3 asomando otra vez.

---

## 4. La variabilidad importa tanto como la carga

La fórmula de Pollaczek–Khinchine generaliza a servicios no exponenciales:

$$W_q=\frac{\rho}{1-\rho}\cdot\frac{1+c_v^2}{2}\cdot\frac{1}{\mu}$$

con $c_v$ el coeficiente de variación del tiempo de servicio.

Los números de la simulación, a $\rho=0{,}85$:

| Servicio | $c_v$ | Espera medida |
|---|---|---|
| Determinista | 0 | **3,7** |
| Exponencial | 1 | 6,9 |
| Muy variable | 2 | **13,7** |

**Reducir la variabilidad a cero casi divide la espera por dos**, sin tocar la
capacidad. Y duplicar la variabilidad la duplica.

De ahí una de las lecciones más transferibles de la teoría de colas:
**estandarizar los tiempos de servicio es tan eficaz como añadir capacidad, y
suele ser mucho más barato**. Es el principio detrás de la producción ajustada,
de los protocolos clínicos estandarizados y del diseño de sistemas informáticos
con latencias acotadas.

---

## 5. Una cola o varias

Con $c$ servidores hay dos diseños posibles: una cola única que alimenta a
todos, o $c$ colas independientes.

**La cola única es siempre mejor**, y por dos razones distintas:

* **Nunca hay un servidor ocioso con gente esperando**, cosa que en colas
  separadas ocurre constantemente.
* **La varianza de la espera es mucho menor**: nadie se queda atrapado detrás
  del cliente lento.

La diferencia en espera media, a $\rho=0{,}9$ con 5 servidores, es de un factor
de varias veces. Y la diferencia en **percentil 95** es todavía mayor, que es
lo que la gente percibe.

Es un resultado demostrable, medible y visible en cualquier aeropuerto, banco o
oficina de correos moderna. Y sin embargo los supermercados siguen usando colas
separadas, por una razón que también es real: la cola única **parece** más
larga, aunque avance más deprisa, y los clientes reaccionan a la longitud
visible.

---

## 6. La paradoja del autobús, otra vez

Del capítulo 4: quien llega en un instante al azar experimenta un tiempo de
servicio **sesgado hacia los largos**.

Consecuencia práctica en sistemas de colas: **el tiempo medio que reportan los
usuarios es peor que la media real**, porque hay más usuarios experimentando
los periodos malos. Un sistema que sirve el 99 % de las peticiones en 10 ms y
el 1 % en 10 s tiene una media de 110 ms, y prácticamente todos los usuarios
que se quejan están en ese 1 %.

Por eso en ingeniería de sistemas se reportan percentiles —p50, p95, p99, p999—
y no medias. Y por eso la métrica que importa suele ser la peor, no la típica.

---

## 7. ¿Cuándo falla?

::: falla
**Falla el supuesto de Poisson en las llegadas.** Con llegadas por lotes
—autobuses que descargan, procesos por tandas— la cola es mucho peor que la
predicha.

**Falla la tasa constante.** Un supermercado a las 12:00 y a las 17:00 son dos
sistemas distintos. Hay que trocear.

**Falla suponer clientes pacientes.** Con abandono, el sistema se estabiliza
solo aunque $\rho>1$: la cola no crece indefinidamente porque la gente se va.
Eso cambia radicalmente el análisis y es lo que ocurre en la realidad.

**Y falla el estado estacionario.** Las fórmulas describen el equilibrio a largo
plazo. Un pico de una hora en un sistema con $\rho>1$ durante ese rato nunca
alcanza el estacionario, y hay que simular el transitorio.
:::

---

## 8. Historia

::: historia
**Erlang, 1909, y la centralita de Copenhague** · *Nivel de verificación: A.*

Agner Krarup Erlang trabajaba para la compañía telefónica de Copenhague. El
problema era estrictamente comercial: ¿cuántas líneas hay que instalar para que
la proporción de llamadas bloqueadas sea aceptable?

Erlang modeló las llamadas como un proceso de Poisson y dedujo, en 1917, las
fórmulas B y C que siguen usándose exactamente igual hoy para dimensionar
centros de llamadas, redes de datos, camas de hospital y plantillas de personal.

Su método era característico: **medía**. Contaba llamadas con cronómetro y
comprobaba sus hipótesis con datos reales de la centralita antes de escribir
ninguna fórmula.

La unidad de tráfico se llama *erlang* en su honor. Es uno de los casos más
limpios de un problema de ingeniería que crea una rama de las matemáticas.

**Little, 1961** · *Nivel de verificación: A.*

John Little demostró un resultado de una generalidad asombrosa:

$$L=\lambda W$$

El número medio de clientes en un sistema es la tasa de llegada por el tiempo
medio de estancia. **Y no supone nada**: ni Poisson, ni exponencial, ni
independencia, ni una disciplina de servicio concreta. Sólo estacionariedad.

Es la clase de resultado que conviene tener en la cabeza, porque permite
estimar una de las tres cantidades cuando se conocen las otras dos, en
cualquier sistema con flujo: una fábrica, un hospital, una cola de mensajes, un
proceso de contratación.
:::

---

## 9. Experimento computacional

::: experimento
**Una cola frente a varias, medido.**

Simula por eventos discretos dos sistemas con la misma capacidad total: (a) una
cola y 5 servidores; (b) 5 colas independientes con asignación aleatoria al
llegar.

Barre $\rho$ de 0,5 a 0,95 y mide la espera media **y el percentil 95**.

*Qué esperar:* la diferencia en la media es notable; en el p95, mucho mayor.

*Después, la parte realista:* añade la posibilidad de cambiarse de cola al ver
que otra avanza más (*jockeying*). ¿Cuánto de la ventaja de la cola única
recupera? La respuesta —bastante, pero no toda— explica el comportamiento
observable en cualquier supermercado.
:::

---

## 10. Lo esencial

::: esencial
* La espera diverge como $1/(1-\rho)$. Del 50 % al 90 % de utilización, la
  espera se multiplica por cinco.
* Ningún sistema con variabilidad se opera cerca del 100 %.
* La variabilidad del servicio pesa tanto como la carga:
  $W_q\propto(1+c_v^2)/2$. Estandarizar es tan eficaz como añadir capacidad y
  más barato.
* Una cola única bate siempre a varias colas separadas, y sobre todo en el
  percentil alto.
* Los usuarios experimentan una media peor que la real: sesgo de longitud.
  Reporta percentiles.
* Ley de Little, $L=\lambda W$: no supone nada y sirve en cualquier sistema con
  flujo.
:::

---

## 11. Preguntas abiertas

::: abierto
* ¿Cómo se dimensiona un sistema cuyo pico dura menos que el tiempo de alcanzar
  el estacionario?
* ¿Qué disciplina de servicio minimiza el percentil 99, en lugar de la media?
* ¿Cómo cambia todo con clientes que abandonan, y cómo se estima esa tasa de
  abandono?
* Si la cola única es demostrablemente mejor, ¿por qué persisten las colas
  separadas? ¿Es un problema de percepción o hay otro coste?
:::

### Referencias

* **Erlang, A. K.** *The Theory of Probabilities and Telephone Conversations.*
  Nyt Tidsskrift for Matematik B **20** (1909), 33–39. **Nivel A (primaria).**
* **Little, John D. C.** *A Proof for the Queuing Formula $L=\lambda W$.*
  Operations Research **9** (1961), 383–387. **Nivel A (primaria).**
* **Kleinrock, Leonard.** *Queueing Systems*, vol. 1, Wiley, 1975. El tratado.
* **Gross, D.; Shortle, J.; Thompson, J.; Harris, C.** *Fundamentals of Queueing
  Theory.* 5.ª ed., Wiley, 2018. La referencia práctica.
* **Hopp, Wallace y Spearman, Mark.** *Factory Physics.* 3.ª ed., Waveland,
  2011. **Excelente** para entender el papel de la variabilidad en producción.
* **Dean, Jeffrey y Barroso, Luiz André.** *The Tail at Scale.* Communications
  of the ACM **56** (2013), 74–80. Por qué en sistemas grandes lo que importa
  es la cola de la distribución de latencias.
