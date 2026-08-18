# II.11 — ¿Por qué hay atascos donde no hay obstáculo?

> **El fenómeno:** conduces por autopista, te paras cinco minutos, y al arrancar
> no hay accidente, ni obra, ni nada.
> **Herramientas:** cap. 6 (EDO con retardo), cap. 7 (inestabilidad), cap. 13
> (ondas).
> **Lo que hay que llevarse:** que una inestabilidad de un sistema con retardo
> produce estructuras macroscópicas sin ninguna causa local, y que el flujo
> máximo no está en la densidad máxima.

---

## 1. Una pregunta

::: pregunta
Treinta coches circulando en una pista circular, todos idénticos, todos con el
mismo conductor ideal, sin obstáculos ni incorporaciones.

**¿Puede aparecer un atasco?**

Sí. Y aparece solo, en unos minutos.
:::

---

## 2. Antes de calcular

::: antes
1. ¿A qué densidad de vehículos crees que es máximo el flujo de una autopista?
2. ¿Hacia dónde se mueve un atasco: con el tráfico o contra él?
3. ¿Por qué un conductor que frena bruscamente afecta a coches que están
   kilómetros atrás?
:::

---

## 3. El mecanismo: retardo más no linealidad

![Modelo de seguimiento de vehículos en vía circular. Izquierda: las trayectorias en el plano espacio-tiempo; la onda de parada nace espontáneamente y viaja hacia atrás. Derecha: el diagrama fundamental, con capacidad máxima de 2388 veh/h a 52 veh/km. Lo que hay que concluir: el atasco es una inestabilidad, no una causa local.](figuras/fig_trafico.pdf)

Cada conductor ajusta su aceleración según la distancia y la velocidad
relativa al de delante. La reacción no es instantánea: hay un **tiempo de
respuesta** de entre 1 y 2 segundos.

Ese retardo es lo que desestabiliza. Si un conductor frena un poco, el de
detrás reacciona tarde y tiene que frenar **más**; el siguiente, más todavía.
La perturbación se amplifica al propagarse hacia atrás.

Es exactamente el problema 6.D4 del capítulo 6: **un retardo puede
desestabilizar un sistema estable**, y por encima de un retardo crítico aparecen
oscilaciones. Aquí, esas oscilaciones son ondas de parada.

Y hay un umbral: por debajo de cierta densidad, la perturbación se amortigua;
por encima, crece. Es una bifurcación, y por eso el atasco aparece de golpe.

---

## 4. El diagrama fundamental

El flujo es $q=\rho v$, con $\rho$ la densidad. A densidad baja, todos van a
velocidad libre y $q$ crece con $\rho$. A densidad alta, la velocidad cae y $q$
decrece.

Hay un máximo intermedio: **la capacidad**. En la simulación, 2388 veh/h a
52 veh/km, valores realistas para un carril de autopista.

De ahí salen tres consecuencias con implicaciones directas:

**Más coches pueden significar menos flujo.** Operar una autopista por encima
de la densidad crítica reduce su capacidad efectiva. Es contraintuitivo y es la
razón de ser del control de accesos por semáforo (*ramp metering*) que se ve en
las entradas de algunas autopistas: **frenar la entrada aumenta el flujo
total**.

**La histéresis.** Una vez formado el atasco, deshacerlo requiere bajar la
densidad **por debajo** del umbral de formación. El sistema no vuelve por el
mismo camino, y por eso los atascos duran mucho más de lo que su causa
justificaría. Es la silla-nodo del capítulo 7.

**La velocidad de la onda.** Las ondas de parada viajan hacia atrás a unos
15–20 km/h, un valor notablemente robusto entre países y tipos de vía. Es una
propiedad del diagrama fundamental, no de los conductores.

---

## 5. La misma estructura en otros sitios

* **Efecto látigo en cadenas de suministro.** Un pequeño cambio en la demanda
  final produce oscilaciones crecientes aguas arriba, por el retardo entre
  pedido y entrega. Es literalmente el mismo modelo.
* **Ducha de hotel.** El retardo entre girar el grifo y notar el cambio produce
  oscilaciones entre agua fría e hirviendo (problema 7.M1).
* **Osciladores de control.** Cualquier lazo de realimentación con retardo
  suficiente oscila.
* **Ondas de aplausos y de gente en multitudes**, con el mismo mecanismo de
  reacción retardada.

En todos: **realimentación negativa + retardo = oscilación**, y por encima de
un umbral, inestabilidad.

---

## 6. ¿Cuándo falla?

::: falla
**Falla suponer conductores idénticos.** La heterogeneidad —tiempos de reacción
distintos, camiones— cambia el umbral y puede estabilizar o desestabilizar
según el caso.

**Falla el modelo unidimensional con varios carriles.** El cambio de carril
introduce dinámica nueva y es donde los modelos simples se quedan cortos.

**Falla extrapolar a vehículos autónomos.** Con tiempo de reacción mucho menor
y comunicación entre vehículos, el umbral de inestabilidad sube muchísimo. Es
una de las mejoras potenciales más citadas, y también una de las menos
verificadas empíricamente a escala.

**Y falla el modelo circular.** Una pista circular tiene densidad conservada;
una autopista real tiene entradas y salidas, y ahí es donde nacen la mayoría de
los atascos reales.
:::

---

## 7. Historia

::: historia
**Sugiyama y el experimento del atasco fantasma** ·
*Nivel de verificación: A.*

En 2008, un equipo japonés dirigido por Yuki Sugiyama publicó un experimento
extraordinariamente directo: pusieron 22 coches en una pista circular de 230 m
y pidieron a los conductores que circularan a 30 km/h manteniendo una distancia
cómoda.

Al cabo de unos minutos apareció un atasco espontáneo, con coches parándose por
completo, y la onda de parada se propagó hacia atrás a unos 20 km/h.

No había obstáculos, ni señales, ni intersecciones. **La causa era la
inestabilidad, y quedó demostrada experimentalmente.** El vídeo del experimento
es probablemente la mejor pieza divulgativa que existe sobre este capítulo.

**Lighthill, Whitham y Richards, 1955–56** · *Nivel de verificación: A.*

El primer modelo continuo del tráfico trata el flujo como un fluido con una
relación velocidad-densidad. Predice ondas de choque —frentes de frenada— con
las mismas matemáticas que las ondas de choque en gases, es decir, las del
capítulo 2.

Es un ejemplo notable de transferencia: Lighthill y Whitham trabajaban en
dinámica de fluidos, y aplicaron su maquinaria a un problema de ingeniería de
carreteras publicándolo en las actas de la Royal Society.
:::

---

## 8. Experimento computacional

::: experimento
**Encuentra el umbral de inestabilidad.**

Con el modelo de seguimiento del capítulo, empieza con todos los coches
igualmente espaciados y a velocidad de equilibrio: es una solución exacta.

Perturba la posición de un coche en 1 cm. Barre la densidad y mide si la
perturbación crece o se amortigua.

*Qué esperar:* un umbral bien definido de densidad por encima del cual la
solución homogénea es inestable.

*Después:* varía el tiempo de reacción $T$ y dibuja el diagrama de estabilidad
en el plano (densidad, tiempo de reacción). ¿Cuánto habría que reducir $T$ para
eliminar la inestabilidad a densidades de hora punta? Esa cifra es el argumento
cuantitativo a favor de la conducción automatizada, y merece la pena
calcularlo en lugar de citarlo.
:::

---

## 9. Lo esencial

::: esencial
* Un atasco puede aparecer sin ninguna causa local: es una inestabilidad de un
  sistema con retardo.
* Realimentación negativa más retardo produce oscilación; por encima de un
  umbral, inestabilidad.
* El flujo máximo **no** está en la densidad máxima. Hay una capacidad
  intermedia.
* Por encima de la densidad crítica, más coches significan menos flujo. De ahí
  el control de accesos.
* Hay histéresis: deshacer un atasco exige bajar más de lo que costó formarlo.
* Las ondas de parada viajan hacia atrás a 15–20 km/h, y ese valor es robusto.
* La misma estructura: efecto látigo, duchas de hotel, lazos de control.
:::

---

## 10. Preguntas abiertas

::: abierto
* ¿Cuánta penetración de vehículos automatizados hace falta para estabilizar el
  tráfico? Hay estimaciones entre el 5 % y el 30 %, y dependen mucho del modelo.
* ¿Se puede detectar un atasco incipiente a partir de datos de tráfico y actuar
  antes de que se forme?
* ¿Qué modelos de cambio de carril reproducen la fenomenología observada sin
  añadir parámetros ad hoc?
* ¿Existe un diagrama fundamental universal, o depende de la cultura de
  conducción?
:::

### Referencias

* **Sugiyama, Y. et al.** *Traffic jams without bottlenecks—experimental
  evidence for the physical mechanism of the formation of a jam.* New Journal
  of Physics **10** (2008), 033001. **Nivel A (primaria).** Léase y véase el
  vídeo.
* **Lighthill, M. J. y Whitham, G. B.** *On kinematic waves II: a theory of
  traffic flow on long crowded roads.* Proc. R. Soc. A **229** (1955), 317–345.
  **Nivel A (primaria).**
* **Treiber, Martin y Kesting, Arne.** *Traffic Flow Dynamics.* Springer, 2013.
  **La referencia moderna**, con simulaciones interactivas en línea.
* **Helbing, Dirk.** *Traffic and related self-driven many-particle systems.*
  Reviews of Modern Physics **73** (2001), 1067–1141. Panorámica completa.
* **Sterman, John.** *Business Dynamics.* McGraw-Hill, 2000. El efecto látigo y
  los sistemas con retardo en gestión.
