## Problemas del capítulo 7

**Marcas:** ○ directo · ◐ requiere pensar · ● difícil · ★ abierto.

---

### Calentamiento

**7.C1** ○ Clasifica el punto fijo del origen para
$J=\begin{pmatrix}-1&2\\0&-3\end{pmatrix}$,
$J=\begin{pmatrix}0&1\\-4&0\end{pmatrix}$ y
$J=\begin{pmatrix}1&-5\\1&-1\end{pmatrix}$.

**7.C2** ○ Un foco estable tiene $\lambda=-0{,}2\pm3i$. ¿Cuál es el periodo de
la oscilación y cuánto tarda la amplitud en reducirse a la mitad?

**7.C3** ○ ¿Qué tipo de bifurcación describe cada situación? (a) una columna
que pandea; (b) el umbral $R_0=1$ de una epidemia; (c) el chirrido de una
tiza; (d) el colapso de una pesquería.

**7.C4** ○ Con $\lambda=1{,}5$ día⁻¹ y error inicial relativo $10^{-4}$,
¿cuántos días de predicción tienes si toleras un error del 100 %?

---

### Estimación

**7.E1** ◐ Estima el tiempo de duplicación del error en la atmósfera a partir
del hecho de que la predicción útil llega a unos 10 días y los datos iniciales
tienen un error relativo del orden del 1 %.

**7.E2** ◐ Estima cuántos dígitos de precisión necesitarías para predecir el
sistema de Lorenz durante 100 unidades de tiempo. ¿Cabe en doble precisión?

**7.E3** ● Estima el exponente de Lyapunov de una mesa de billar con
obstáculos circulares, a partir de la geometría (dispersión angular por
colisión y recorrido libre medio).

---

### Modelado

**7.M1** ◐ Un termostato con retardo: el calefactor reacciona con un retraso
$\tau_r$ a la temperatura. Escribe el modelo y predice cualitativamente qué
pasa al aumentar $\tau_r$. ¿Qué bifurcación esperas?

**7.M2** ◐ Modela una población con efecto Allee (reproducción pobre a
densidad baja). ¿Cuántos puntos fijos hay? ¿Qué predice sobre la
reintroducción de una especie?

**7.M3** ● Construye el modelo más simple que produzca un ciclo límite y
justifica cada término. ¿Puedes hacerlo con dos ecuaciones lineales?
¿Por qué no?

---

### Derivación

**7.D1** ◐ Deduce las condiciones de estabilidad en 2D en términos de la traza
y el determinante del jacobiano, y dibuja el diagrama traza–determinante.

**7.D2** ◐ Encuentra los puntos fijos del sistema de Lorenz y demuestra que los
dos no triviales existen sólo para $\rho>1$ y se desestabilizan en
$\rho_c=\sigma(\sigma+\beta+3)/(\sigma-\beta-1)$. Calcula $\rho_c$ para los
valores estándar.

**7.D3** ● Demuestra que el mapa logístico con $r=4$ es conjugado a
$\theta\mapsto2\theta$ mediante $x=\sin^2(\pi\theta)$, y deduce de ahí que su
exponente de Lyapunov vale exactamente $\ln 2$.

**7.D4** ● Deduce la forma normal de la bifurcación silla-nodo y demuestra que
cualquier sistema unidimensional que la sufra se comporta, cerca del punto
crítico, como $\dot x = r \pm x^2$.

---

### Computacional

**7.P1** ○ Reproduce el diagrama de bifurcación del mapa logístico y localiza
numéricamente los tres primeros puntos de duplicación. Estima la constante de
Feigenbaum.

**7.P2** ◐ Calcula el exponente de Lyapunov del mapa logístico en función de
$r$ y superpónlo al diagrama de bifurcación. ¿Coinciden los cruces por cero con
las ventanas periódicas?

**7.P3** ◐ Dibuja la sección de Poincaré de Lorenz tomando los máximos
sucesivos de $z$. Comprueba que $z_{n+1}$ frente a $z_n$ cae sobre una curva
casi unidimensional con forma de tienda de campaña.

---

### Experimento

**7.X1** ◐ Barre $\rho$ en Lorenz de 1 a 400 y clasifica el comportamiento
(punto fijo, periódico, caótico) midiendo el exponente de Lyapunov. Dibuja el
mapa de regímenes. ¿Hay ventanas periódicas dentro del caos?

**7.X2** ● Implementa el experimento de ralentización crítica descrito en la
sección 10 y determina con cuánta antelación se detecta el colapso. Repite con
distintos niveles de ruido: ¿ayuda o estorba el ruido?

---

### Detective

**7.T1** ◐ Un modelo de dos ecuaciones produce en la simulación una trayectoria
que parece caótica. ¿Qué le dirías al autor, y qué comprobación es la primera?

**7.T2** ◐ Un artículo mide la «dimensión de correlación» de una serie
económica de 400 puntos mensuales y obtiene 3,4, concluyendo caos determinista
de baja dimensión. ¿Qué objeción es la fundamental?

**7.T3** ● Una simulación de un sistema rígido con Euler explícito produce
oscilaciones irregulares acotadas con exponente de Lyapunov positivo. Se
anuncia un atractor extraño. Diseña las tres comprobaciones que lo desmontan,
en orden de coste creciente.

---

### Mundo real

**7.R1** ★ Busca en tu campo un sistema con un umbral crítico conocido. ¿Qué
tipo de bifurcación es? ¿Existen señales de alarma temprana documentadas?

**7.R2** ★ Estima el horizonte de predicción útil de algún modelo que uses en
tu trabajo. ¿Está limitado por los datos iniciales, por el modelo, o por otra
cosa?

---

### Feynman

**7.F1** ○ Explica sin ecuaciones por qué el caos es determinista y aun así
impredecible.

**7.F2** ◐ Explica por qué se puede simular el clima dentro de cien años sin
poder predecir el tiempo dentro de un mes.

---

### Extensión

**7.Z1** ★ Lee el capítulo 1 de *The Essence of Chaos* de Lorenz y compáralo
con la versión que aparece en libros de divulgación. Enumera tres detalles que
la versión popular cambia o elimina.

**7.Z2** ★ Estudia la demostración asistida por ordenador de Tucker (2002) de
que el atractor de Lorenz existe. ¿Qué significa exactamente que una
demostración sea «asistida por ordenador», y qué habría que creerse para
aceptarla?
