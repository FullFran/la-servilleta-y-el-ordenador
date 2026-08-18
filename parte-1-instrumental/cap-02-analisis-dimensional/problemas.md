## Problemas del capítulo 2

**Marcas:** ○ directo · ◐ requiere pensar · ● difícil · ★ abierto.

---

### Calentamiento

**2.C1** ○ Determina las dimensiones de: viscosidad dinámica $\mu$, viscosidad
cinemática $\nu$, conductividad térmica $k$, difusividad térmica $\alpha$,
tensión superficial $\gamma$, constante de Boltzmann $k_B$.

**2.C2** ○ ¿Cuántos grupos adimensionales tiene un problema con 7 variables en
el que aparecen masa, longitud, tiempo y temperatura? ¿Y si dos de las
variables resultan tener dimensiones proporcionales?

**2.C3** ○ Comprueba dimensionalmente estas expresiones y di cuáles son
imposibles: (a) $E=\tfrac12 mv^2$; (b) $T=2\pi\sqrt{L/g}$;
(c) $v=\sqrt{2gh}+\mu/\rho L$; (d) $\Delta p=\rho g h$; (e) $Re=\rho U L/\mu$.

**2.C4** ○ El número de Biot es $Bi=hL/k$. Sin buscar nada, di qué significa
$Bi\ll1$ y por qué eso justifica el modelo de «capacidad concentrada» que
usaremos en el capítulo 6 para la taza de café.

---

### Estimación

**2.E1** ◐ Estima el número de Reynolds de: tu mano al agitarla en el aire,
una cuchara removiendo café, la sangre en la aorta, el aire en tu tráquea al
correr. ¿Cuáles son turbulentos?

**2.E2** ◐ Estima el número de Mach de un aleteo de mosquito, de un latigazo y
de la punta de la pala de un aerogenerador. ¿Cuál explica un chasquido?

**2.E3** ● Un dron de 250 g vuela con hélices de 12 cm. Estima su número de
Reynolds y compáralo con el de un avión comercial. ¿Puedes usar los perfiles
alares de un avión, escalados, en el dron? Justifica con números.

---

### Modelado

**2.M1** ◐ Quieres predecir cuánto tarda en enfriarse una pieza metálica al
sacarla de un horno. Haz la lista de variables, construye los grupos π y di
cuál de ellos decide si el problema es de un parámetro o de dos.

**2.M2** ◐ La velocidad de una ola en aguas profundas depende de su longitud de
onda y de la gravedad; en aguas someras, de la profundidad. Deduce ambas leyes
por análisis dimensional y explica qué variable has quitado en cada caso.

**2.M3** ● Deduce la ley de escala del alcance máximo de un salto en función de
la masa del animal, suponiendo que la energía muscular disponible es
proporcional a la masa. ¿Predice que una pulga y un canguro saltan la misma
altura? Contrasta con datos reales y explica la discrepancia.

---

### Derivación

**2.D1** ◐ Deduce el periodo de un péndulo por análisis dimensional. Explica
por qué el método no puede darte la dependencia con la amplitud, y qué
información adicional haría falta.

**2.D2** ◐ Adimensionaliza la ecuación del oscilador amortiguado
$m\ddot x + c\dot x + kx = 0$. ¿Cuántos parámetros quedan? Identifica el que
sobrevive con su nombre habitual.

**2.D3** ● Deduce la ley de Taylor–Sedov–von Neumann incluyendo ahora la
presión ambiente $p_0$ en la lista de variables. ¿Cuántos grupos hay? ¿Cómo se
recupera el resultado del capítulo en el límite adecuado, y qué te dice eso
sobre cuándo deja de valer?

**2.D4** ● Demuestra que el número de grupos π es $n-k$ con $k$ el **rango** de
la matriz dimensional, y construye un ejemplo de tres variables donde el rango
sea menor que el número de dimensiones que aparecen.

---

### Computacional

**2.P1** ○ Escribe una función que reciba una lista de variables con sus
exponentes dimensionales y devuelva una base del núcleo de la matriz
dimensional, es decir, un conjunto de grupos π. Pruébala con la explosión y con
el arrastre de una esfera.

**2.P2** ◐ Reproduce el colapso del péndulo. Después añade rozamiento
proporcional a la velocidad y comprueba que el colapso **se rompe**. ¿Qué grupo
adimensional nuevo hay que introducir para recuperarlo?

**2.P3** ◐ Integra $d\hat v/d\hat t = 1-\hat v^2$ y comprueba analíticamente
que $\hat v(\hat t)=\tanh \hat t$. Después integra la ecuación con dimensiones
para tres gotas distintas y verifica que todas caen sobre la misma curva al
reescalar.

---

### Experimento

**2.X1** ◐ Barre el exponente del ajuste de Trinity entre 0,35 y 0,45 y dibuja
el error cuadrático. ¿Cómo de bien determinado está el 2/5 por los datos? ¿Qué
intervalo de exponentes es compatible?

**2.X2** ● Genera datos sintéticos de un problema con dos grupos π y comprueba
que un colapso con un solo grupo produce una banda en vez de una curva. Usa esa
banda para *descubrir* el segundo grupo sin conocerlo de antemano.

---

### Detective

**2.T1** ◐ Un informe afirma: «hemos deducido por análisis dimensional que la
potencia disipada por un agitador es $P=\rho N^3 D^5$, con $N$ las revoluciones
por segundo y $D$ el diámetro. Como la fórmula no contiene la viscosidad, el
resultado vale para cualquier fluido». Localiza el error de razonamiento.

**2.T2** ◐ Otro: «El periodo del péndulo es $T=2\pi\sqrt{L/g}$. Como no aparece
la masa, un péndulo de plomo y uno de corcho de la misma longitud oscilan
igual». ¿Es cierto? ¿Bajo qué condiciones deja de serlo, y qué variable falta
en la lista?

**2.T3** ● Un artículo de biomecánica presenta un colapso de datos «excelente»
de la velocidad máxima de carrera frente a la masa corporal, con un exponente
de 0,17 ± 0,02, y concluye que existe una ley universal. Mirando la figura, los
puntos de mamíferos grandes caen sistemáticamente por debajo de la recta.
¿Qué sospechas? ¿Qué comprobación pedirías?

---

### Mundo real

**2.R1** ★ Elige un sistema de tu trabajo que dependa de muchos parámetros.
Adimensionalízalo. ¿Cuántos parámetros quedan realmente? ¿Cuánto se reduce el
espacio de búsqueda si diseñas el barrido en las variables adimensionales?

**2.R2** ★ Busca un artículo reciente de tu campo que presente un barrido de
parámetros. ¿Están adimensionalizados? Si no, ¿cuántas simulaciones se podrían
haber ahorrado?

---

### Feynman

**2.F1** ○ Explica, sin ecuaciones, por qué una ley física no puede depender de
si mides en metros o en pies, y qué consecuencia tiene eso.

**2.F2** ◐ Explica a un biólogo por qué un insecto puede caminar por el techo y
un elefante no, usando sólo argumentos de escala.

---

### Extensión

**2.Z1** ★ Lee *Life at Low Reynolds Number* de Purcell (1977). Reproduce con
un dibujo el teorema de la vieira y explica por qué implica que un nadador
microscópico necesita un movimiento no recíproco.

**2.Z2** ★ Lee el capítulo 1 de Barenblatt (1996) sobre autosemejanza de
segunda especie y localiza un ejemplo físico donde el exponente **no** salga de
contar unidades. Explica cómo se detecta esa situación en los datos.
