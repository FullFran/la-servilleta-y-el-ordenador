## Problemas del capítulo 8

**Marcas:** ○ directo · ◐ requiere pensar · ● difícil · ★ abierto.

---

### Calentamiento

**8.C1** ○ Un método de orden 3 da error $10^{-4}$ con $h=0{,}1$. ¿Qué error
esperas con $h=0{,}01$? ¿Y con $h=10^{-6}$?

**8.C2** ○ ¿Cuál es el paso máximo estable de Euler explícito para
$\dot y = -50y$? ¿Y para $\dot y = -50y + \sin t$?

**8.C3** ○ Reescribe de forma numéricamente estable: (a) $\sqrt{x+1}-\sqrt{x}$
para $x$ grande; (b) $\ln(1+x)$ para $x$ pequeño; (c) la raíz pequeña de
$ax^2+bx+c$ cuando $b^2\gg4ac$.

**8.C4** ○ En la ecuación del calor con $D=10^{-5}$ m²/s y $\Delta x=1$ mm,
¿cuál es el paso temporal máximo de un esquema explícito?

---

### Estimación

**8.E1** ◐ Estima cuántas operaciones de coma flotante hace tu ordenador en una
simulación de una hora. ¿Cuánto error de redondeo acumulado esperarías en el
peor caso, y cuánto en un caso realista?

**8.E2** ◐ Estima el coste de simular la atmósfera terrestre con una malla de
1 km durante un día. ¿Cuántos puntos? ¿Cuántos pasos temporales impone la CFL?

**8.E3** ● Estima cuánta memoria y cuánto tiempo costaría resolver la ecuación
del calor en 3D con $1000^3$ celdas, con esquema explícito y con esquema
implícito. ¿Cuál gana, y a partir de qué tamaño?

---

### Modelado

**8.M1** ◐ Tienes que integrar un sistema con constantes de tiempo de 1 μs y
1 hora. Explica por qué un método explícito es una mala idea y cuantifica
cuánto.

**8.M2** ◐ Un modelo tiene un término de fricción que cambia de signo cuando la
velocidad pasa por cero. ¿Qué le hace eso a un integrador adaptativo? ¿Cómo lo
tratarías?

**8.M3** ● Diseña la estrategia numérica completa para simular un sistema
planetario durante $10^9$ años: método, paso, precisión, comprobaciones.
Justifica cada decisión.

---

### Derivación

**8.D1** ◐ Deduce el error local de truncamiento de Euler explícito por
desarrollo de Taylor, y explica por qué el error global es un orden menor.

**8.D2** ◐ Deduce la región de estabilidad de Heun aplicándolo a
$\dot y=\lambda y$, y comprueba que contiene a la de Euler.

**8.D3** ● Haz el análisis de estabilidad de von Neumann del esquema explícito
para la ecuación del calor y deduce $r\le1/2$. Repítelo para el esquema
implícito y comprueba que es incondicionalmente estable.

**8.D4** ● Demuestra que el método de Euler simpléctico conserva exactamente el
área en el plano de fases para el oscilador armónico, calculando el
determinante de la matriz de un paso. Compara con Euler explícito.

---

### Computacional

**8.P1** ○ Implementa Euler, Heun y RK4 y mide sus órdenes. Después rompe RK4
cambiando un coeficiente y comprueba que el orden cae.

**8.P2** ◐ Reproduce la curva en V del error frente al paso para RK4.
Determina numéricamente el $h$ óptimo y compáralo con la predicción
$h^*\sim\epsilon^{1/(p+1)}$.

**8.P3** ◐ Integra el sistema rígido de dos compartimentos del capítulo 6 con
`RK45` y con `Radau`. Compara número de evaluaciones de $f$ y tiempo de pared.

---

### Experimento

**8.X1** ◐ Integra el oscilador armónico 10 000 periodos con los cuatro métodos
de la figura. Dibuja la deriva de energía frente al tiempo en log-log. ¿Qué
potencia sigue cada uno?

**8.X2** ● Implementa el método de soluciones manufacturadas para tu propio
solucionador de la ecuación del calor. Introduce a propósito un error de
orden 1 en la condición de contorno y comprueba que el test lo detecta.

---

### Detective

**8.T1** ◐ Un colega dice: «he bajado la tolerancia a $10^{-14}$ y el resultado
cambió, así que $10^{-12}$ no era suficiente; ahora con $10^{-14}$ ya es
correcto». ¿Qué falla en ese razonamiento?

**8.T2** ◐ Una simulación de dinámica molecular pierde un 0,1 % de energía cada
nanosegundo. El autor dice que es despreciable. ¿Lo es? ¿Qué pregunta harías?

**8.T3** ● Un código de EDP converge con orden 2 al refinar la malla y da un
resultado estable y reproducible. Pero el resultado es un 15 % distinto del
experimental. El autor concluye que el experimento está mal. Enumera, en
orden, las tres cosas que comprobarías antes de aceptar esa conclusión.

---

### Mundo real

**8.R1** ★ Coge un código de simulación de tu trabajo. ¿Alguien ha medido
alguna vez su orden de convergencia? Hazlo.

**8.R2** ★ Busca en tu campo un resultado publicado basado en simulación.
¿Aparece algún estudio de convergencia? ¿Qué fracción de los artículos que
consultas lo incluye?

---

### Feynman

**8.F1** ○ Explica a alguien que sabe cálculo qué hace exactamente un ordenador
cuando «resuelve» una ecuación diferencial.

**8.F2** ◐ Explica sin fórmulas por qué existe un paso de tiempo máximo, usando
la idea de que la información no puede viajar más rápido que la malla.

---

### Extensión

**8.Z1** ★ Lee el análisis de Lynch (1979 y 2006) sobre el fallo de Richardson.
¿Qué lección metodológica extraes sobre la relación entre datos iniciales y
esquemas numéricos?

**8.Z2** ★ Estudia el análisis hacia atrás (*backward error analysis*) de los
integradores simplécticos: la idea de que resuelven exactamente un problema
ligeramente distinto. ¿Qué otras técnicas numéricas admiten una interpretación
parecida?
