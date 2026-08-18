## Problemas del capítulo 6

**Marcas:** ○ directo · ◐ requiere pensar · ● difícil · ★ abierto.

---

### Calentamiento

**6.C1** ○ Un café pasa de 90 a 60 °C en 15 min con la sala a 20 °C. ¿Cuánto
tarda en pasar de 60 a 40 °C? ¿Y de 40 a 30 °C?

**6.C2** ○ Para cada ecuación, encuentra los puntos fijos y clasifícalos sin
resolver: (a) $\dot x=x-x^3$; (b) $\dot x=\sin x$; (c) $\dot x=x^2$;
(d) $\dot x = 1-e^{-x}$.

**6.C3** ○ Una población crece al 3 % anual. Tiempo de duplicación, de memoria.
¿Y al 7 %? (Regla del 70.)

**6.C4** ○ Adimensionaliza $\dot v = g - kv^2$ e identifica la velocidad
terminal y el tiempo característico.

---

### Estimación

**6.E1** ◐ Estima el $\tau$ de enfriamiento de: una taza de café, una piscina,
un pollo en el horno, un edificio. Ordena por magnitud antes de calcular.

**6.E2** ◐ Estima la semivida de eliminación de la cafeína a partir de tu
propia experiencia. Compárala con el valor farmacológico (4–6 h).

**6.E3** ● Estima cuántos días tarda una epidemia con $R_0=3$ y periodo
infeccioso de 5 días en pasar de 100 a 100 000 casos, suponiendo crecimiento
exponencial puro. ¿Qué supuesto se rompe primero?

---

### Modelado

**6.M1** ◐ Un depósito recibe agua a caudal constante y pierde por un agujero
en el fondo. Escribe la EDO, encuentra el equilibrio y el tiempo
característico. ¿Es lineal?

**6.M2** ◐ Modela la concentración de un fármaco en sangre con dosis repetidas
cada 8 horas y eliminación de primer orden. ¿Cuándo se alcanza el estado
estacionario? ¿De qué depende la concentración media?

**6.M3** ● Un rumor se propaga en una oficina de 200 personas. Construye tres
modelos distintos (los que saben lo cuentan a todos; sólo a quienes no lo
saben; dejan de contarlo cuando se aburren) y di cómo distinguirías cuál
gobierna a partir de datos.

---

### Derivación

**6.D1** ◐ Resuelve $\dot x = a-bx$ por factor integrante y por separación de
variables. Comprueba que coinciden y verifica los dos límites $t\to0$ y
$t\to\infty$.

**6.D2** ◐ Deduce la solución explícita de la logística y comprueba que el
punto de inflexión está en $N=K/2$. ¿Qué significa físicamente ese punto?

**6.D3** ● Demuestra que $V=\delta P-\gamma\ln P+\beta D-\alpha\ln D$ se
conserva en Lotka–Volterra. Después demuestra que las medias temporales sobre
un ciclo son exactamente $\bar P=\gamma/\delta$ y $\bar D=\alpha/\beta$.
(Pista: integra $\frac{d}{dt}\ln P$ sobre un periodo.)

**6.D4** ● Considera $\dot x = -x(t-\tau_r)$, con retardo. Busca soluciones
$x=e^{\lambda t}$ y demuestra que existe un $\tau_r$ crítico por encima del cual
el origen se desestabiliza y aparecen oscilaciones. Un sistema de una variable
oscilando: ¿contradice el resultado de 4.4?

---

### Computacional

**6.P1** ○ Integra la logística para varias condiciones iniciales y comprueba
que todas colapsan sobre una única curva al adimensionalizar.

**6.P2** ◐ Integra Lotka–Volterra con `rtol` entre $10^{-3}$ y $10^{-12}$ y
dibuja la deriva de la cantidad conservada frente al tiempo. ¿Qué tolerancia
necesitas para 1000 unidades de tiempo?

**6.P3** ◐ Implementa el modelo de dos compartimentos térmicos de una vivienda
(aire y muros) y comprueba que la respuesta tiene dos exponenciales. Ajusta una
sola exponencial y mira los residuos.

---

### Experimento

**6.X1** ◐ Añade cosecha constante a la logística, $\dot u=u(1-u)-h$, y barre
$h$. Dibuja la posición de los puntos fijos frente a $h$. ¿Qué ocurre en
$h=1/4$? (Acabas de dibujar tu primer diagrama de bifurcación.)

**6.X2** ● Añade saturación en las presas a Lotka–Volterra y barre la capacidad
de carga $K$ desde muy grande hasta pequeña. ¿Cómo cambian las órbitas? ¿A
partir de qué $K$ desaparece la oscilación?

---

### Detective

**6.T1** ◐ Un modelo de una sola variable produce oscilaciones sostenidas en la
simulación. El autor concluye que ha descubierto un ciclo. ¿Qué tres cosas
comprobarías, en este orden?

**6.T2** ◐ Un ajuste de datos de enfriamiento da $\tau=18$ min con la taza
llena y $\tau=11$ min con la taza a la mitad. El autor concluye que $\tau$
depende de la temperatura. ¿Qué explicación más simple hay?

**6.T3** ● Un modelo SIR ajustado a los primeros 20 días de una epidemia
predice un pico de 3 millones de casos con un intervalo de confianza del 5 %.
Los datos ajustan magníficamente. ¿Por qué ese intervalo de confianza es
ficción?

---

### Mundo real

**6.R1** ★ Elige un proceso de tu trabajo que se comporte como una relajación
(un caché que se llena, una cola que se vacía, un despliegue que converge).
Identifica su $\tau$ midiendo, y después predícelo desde primeros principios.

**6.R2** ★ Busca un modelo publicado de tu campo con más de cinco parámetros.
Adimensionalízalo. ¿Cuántos quedan? ¿Los autores lo hicieron?

---

### Feynman

**6.F1** ○ Explica sin ecuaciones qué es un tiempo característico y por qué es
la magnitud más útil de un modelo dinámico.

**6.F2** ◐ Explica el principio de Volterra a un agricultor que quiere fumigar.

---

### Extensión

**6.Z1** ★ Lee el artículo de Volterra de 1926 (o un resumen fiable) y compara
sus supuestos con los de un modelo depredador–presa moderno. ¿Qué se ha
añadido en un siglo y por qué?

**6.Z2** ★ Estudia la aproximación de estado cuasi-estacionario en la cinética
de Michaelis–Menten. Deduce la condición de validez y compruébala
numéricamente. ¿Cuándo falla?
