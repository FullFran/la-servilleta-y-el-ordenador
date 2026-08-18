## Soluciones del capítulo 7

> Las soluciones son razonadas: el número final es lo menos importante. En los
> problemas ● y ★ con solución cerrada hay **Pista 1** y **Pista 2** antes de
> ella; tápalas con la mano y úsalas de una en una.
>
> Los de **Mundo real** (R) no llevan solución a propósito: su procedimiento
> está en el apéndice D.

---

### Calentamiento

**7.C1** (a) Triangular: $\lambda=-1,-3$, ambos reales negativos → **nodo
estable**. (b) $\lambda=\pm2i$ → **centro** (caso marginal: la linealización no
decide). (c) traza 0, determinante $-1+5=4$; $\lambda=\pm2i$ → también centro.

**7.C2** Periodo $=2\pi/3=2{,}09$. La amplitud va como $e^{-0{,}2t}$, luego se
reduce a la mitad en $\ln2/0{,}2=3{,}47$: **menos de dos oscilaciones**. Un
sistema así apenas «suena»; los dos números lo dicen sin resolver nada.

**7.C3** (a) horquilla (ruptura de simetría: la columna se dobla a un lado o al
otro); (b) transcrítica; (c) Hopf; (d) silla-nodo.

**7.C4** $t_h=\ln(1/10^{-4})/1{,}5=\ln(10^4)/1{,}5=6{,}1$ días.

---

### Estimación

**7.E1** $t_h=\lambda^{-1}\ln(1/\epsilon)$. Con $t_h=10$ días y
$\epsilon=10^{-2}$: $\lambda=\ln(100)/10=0{,}46$ día⁻¹, luego un tiempo de
duplicación $\ln2/\lambda=1{,}5$ días. Coincide bien con las estimaciones
operativas, que sitúan la duplicación del error entre 1 y 2 días.

**7.E2** Con $\lambda=0{,}9$, para $t=100$ hace falta
$\epsilon<\Delta e^{-\lambda t}=30\,e^{-90}\approx10^{-38}$. La doble precisión
llega a $10^{-16}$: **haría falta cuádruple precisión y aún más**, unos 38
dígitos decimales. Y ni siquiera bastaría, porque el propio modelo tendría que
ser exacto a ese nivel.

**7.E3** ● *Pista 1:* en cada colisión con un obstáculo convexo, dos rayos
paralelos separados $d$ salen separados angularmente $\sim d/R$.
*Pista 2:* el exponente que buscas no es por colisión sino por segundo. Te
falta una sola cosa: cuántas colisiones hay en un segundo.
*Solución:* la separación se amplifica por un factor $\sim\ell/R$ en cada
colisión, con $\ell$ el recorrido libre medio. Con $\ell\sim10$ cm y $R\sim3$
cm, factor $\sim3$ por colisión. Si hay una colisión cada $\ell/v$ con
$v\sim1$ m/s, es decir cada 0,1 s, entonces
$\lambda\sim\ln3/0{,}1\approx11$ s⁻¹. En un segundo, el error se amplifica
$e^{11}\approx6\times10^4$. Por eso el billar es imposible de calcular más allá
de unas pocas bandas, y es la base del argumento de Berry sobre la influencia
gravitatoria de un electrón en el borde de la galaxia.

---

### Modelado

**7.M1** $\dot T = -k(T - T_{\text{ref}}(t-\tau_r))$ o similar. Al aumentar
$\tau_r$ el sistema pasa de converger monótonamente a oscilar amortiguado, y
por encima de un $\tau_r$ crítico las oscilaciones se sostienen: **bifurcación
de Hopf**. Es la razón por la que las duchas de hotel oscilan entre agua fría y
agua hirviendo: el retardo entre el grifo y la salida convierte una
realimentación estabilizadora en un oscilador.

**7.M2** $\dot N = rN(N/A - 1)(1 - N/K)$. Tres puntos fijos: 0 (estable), $A$
(inestable, umbral de Allee) y $K$ (estable). Predicción sobre reintroducción:
**soltar pocos individuos no funciona**, por muchos recursos que haya, porque
por debajo de $A$ la población decae. Hay que superar el umbral de golpe. Es un
resultado con consecuencias directas en biología de la conservación.

**7.M3** ● *Pista 1:* pregúntate por qué un sistema lineal no puede tener un ciclo límite. La respuesta está en qué le pasa a una órbita cerrada si multiplicas la condición inicial por dos.
*Pista 2:* necesitas amortiguamiento que cambie de signo con la amplitud. La forma más simple de conseguirlo es un coeficiente que dependa de $x^2$.
*Solución:* Un ciclo límite exige no linealidad: en un sistema lineal, si hay
una órbita cerrada hay un continuo de ellas (un centro), no una aislada. El
modelo más simple es el oscilador de Van der Pol,
$\ddot x-\mu(1-x^2)\dot x+x=0$: amortiguamiento **negativo** para amplitudes
pequeñas (inyecta energía) y positivo para grandes (la disipa). El ciclo límite
es donde ambas se compensan en promedio. Cada término tiene su justificación:
uno hace crecer lo pequeño, otro frena lo grande.

---

### Derivación

**7.D1** Con $\tau=\operatorname{tr}J$ y $\Delta=\det J$,
$\lambda=\frac{\tau\pm\sqrt{\tau^2-4\Delta}}{2}$. Estable si $\tau<0$ y
$\Delta>0$; silla si $\Delta<0$; foco si $\tau^2<4\Delta$. El diagrama
traza–determinante resume toda la clasificación 2D en una figura, y merece la
pena dibujarlo a mano una vez.

**7.D2** Puntos fijos: origen, y $(\pm\sqrt{\beta(\rho-1)},
\pm\sqrt{\beta(\rho-1)},\rho-1)$, que existen sólo si $\rho>1$. Con
$\sigma=10$, $\beta=8/3$: $\rho_c=10(10+8/3+3)/(10-8/3-1)=470/19\approx24{,}74$.
Como el valor estándar es $\rho=28>\rho_c$, los tres puntos fijos son
inestables y la trayectoria no puede posarse en ninguno: por eso deambula para
siempre.

**7.D3** ● *Pista 1:* prueba el cambio $x_n=\sin^2(\pi\theta_n)$ y usa la identidad del ángulo doble.
*Pista 2:* la recurrencia que sale para $\theta$ es trivial. Escríbela en **binario** y verás qué hace el mapa con la información del dato inicial.
*Solución:* Con $x_n=\sin^2(\pi\theta_n)$:
$4x(1-x)=4\sin^2\cos^2=\sin^2(2\pi\theta)$, luego $\theta_{n+1}=2\theta_n$
módulo 1. En binario, eso es **desplazar un bit**: cada iteración descarta un
bit del dato inicial y saca a la superficie el siguiente. El exponente es
$\ln|d\theta_{n+1}/d\theta_n|=\ln2$.
Es la mejor definición operativa de caos que existe: **el sistema consume
información del dato inicial a un ritmo constante**, y cuando se acaba, deja de
haber predicción. Un bit por iteración, ni más ni menos.

**7.D4** ● *Pista 1:* no partas de un sistema concreto. Parte de $\dot x=f(x,r)$ genérica y desarrolla en serie alrededor del punto crítico.
*Pista 2:* en la bifurcación se anulan $f$ y $f_x$. El primer término que sobrevive en $x$ es el cuadrático, y el primero en $r$ es el lineal: ahí está la forma normal.
*Solución:* Sea $\dot x = f(x,r)$ con $f(x_0,r_0)=0$, $f_x(x_0,r_0)=0$ (punto
crítico) y $f_r\neq0$, $f_{xx}\neq0$ (condiciones de no degeneración).
Desarrollando: $\dot x\approx f_r\,\delta r+\tfrac12 f_{xx}\,\delta x^2$. Con
un reescalado de $x$ y $r$ queda $\dot X = R\pm X^2$. **La forma normal es
universal**: los detalles del sistema entran sólo en los factores de escala.
Es el mismo tipo de universalidad que la constante de Feigenbaum.

---

### Computacional

**7.P1** Duplicaciones en $r_1=3$, $r_2=3{,}4495$, $r_3=3{,}5441$,
$r_4=3{,}5644$. Cocientes: $(r_2-r_1)/(r_3-r_2)=4{,}75$,
$(r_3-r_2)/(r_4-r_3)=4{,}66$. Convergen a $4{,}669\ldots$ Con cuatro puntos ya
se obtienen tres cifras: es un resultado numérico sorprendentemente barato.

**7.P2** El exponente cruza cero exactamente en cada duplicación de periodo y
se vuelve negativo dentro de cada ventana periódica. Superponer las dos figuras
es la mejor manera de convencerse de que las ventanas blancas del diagrama son
orden, no falta de datos.

**7.P3** Sale la aplicación de tienda de campaña de Lorenz. Es un
descubrimiento notable: **un sistema continuo en 3D se reduce a un mapa 1D**,
y ese mapa es de la misma familia que el logístico. Ahí está la conexión entre
los dos ejemplos del capítulo, y es la razón de que la teoría de mapas
unidimensionales sea relevante para EDO.

---

### Experimento

**7.X1** El caos aparece en torno a $\rho\approx24{,}74$ (con histéresis: hay
un rango donde coexisten atractor caótico y puntos fijos estables). Y hay
ventanas periódicas anchas, por ejemplo alrededor de $\rho\approx100$ y
$\rho\approx160$, y comportamiento periódico para $\rho\gtrsim313$. Que el caos
**desaparezca** al aumentar el parámetro sorprende a casi todo el mundo y es un
recordatorio de que «más no lineal» no significa «más caótico».

**7.X2** ● *Pista 1:* cerca de la bifurcación un autovalor tiende a cero, así que el sistema tarda cada vez más en volver al equilibrio tras una perturbación.
*Pista 2:* eso se traduce en dos observables medibles en la serie temporal: la varianza y la autocorrelación a un paso. Mira cómo crecen al acercarte.
*Solución:* La varianza y la autocorrelación empiezan a crecer de forma
detectable cuando $h$ está a un 10–20 % de $h_c$, es decir, con antelación
suficiente para actuar. Con más ruido, la señal aparece antes (el sistema
explora más el paisaje) pero también hay más falsas alarmas. Es exactamente el
compromiso sensibilidad/especificidad del capítulo 4 aplicado a series
temporales.

---

### Detective

**7.T1** Lo primero: **contar las variables de estado**. Un sistema autónomo y
determinista de dimensión 2 no puede ser caótico (Poincaré–Bendixson). Si la
simulación parece caótica, hay una tercera variable escondida (un parámetro que
varía con el tiempo, un forzamiento externo, un retardo) o es un artefacto
numérico. Segunda comprobación: reducir el paso.

**7.T2** La objeción fundamental es el **tamaño de muestra**. Para estimar de
forma fiable una dimensión de correlación $D$ hacen falta del orden de
$10^{D}$–$10^{2D}$ puntos: para $D=3{,}4$, entre $10^{3}$ y $10^{7}$. Con 400
puntos, el algoritmo de Grassberger–Procaccia devuelve un número, pero ese
número lo devuelve también para ruido coloreado. La comprobación obligatoria es
la de **datos sustitutos** (*surrogate data*, Theiler et al. 1992): generar
series con el mismo espectro pero fases aleatorias y comprobar que dan una
dimensión distinta. Casi ninguno de los trabajos de los años ochenta lo hizo.

**7.T3** ● *Pista 1:* ordena las comprobaciones por coste, no por elegancia. La primera debería costar un minuto.
*Pista 2:* un atractor de verdad no depende del paso de integración. Un artefacto numérico, sí.
*Solución:* En orden de coste: (1) **reducir el paso a la mitad** y ver si el
«atractor» cambia —cuesta un minuto y resuelve el 90 % de los casos—;
(2) **cambiar de integrador** a uno implícito adecuado para problemas rígidos;
(3) comprobar si el paso está dentro de la región de estabilidad del método
calculando los autovalores del jacobiano (capítulo 8). Si el fenómeno sobrevive
a las tres, empieza a ser interesante.

---

### Feynman

**7.F1** Guion: «Las ecuaciones no tienen nada de azaroso: si conocieras el
estado exacto, podrías calcular el futuro exacto. El problema es que nunca lo
conoces exactamente, y la diferencia entre lo que crees y lo que hay se duplica
cada cierto tiempo. Al principio no se nota; después de veinte duplicaciones, un
error del tamaño de un átomo es del tamaño del sistema. No es que el futuro sea
aleatorio: es que tu ignorancia crece más deprisa de lo que puedes medir.»

**7.F2** Guion: «Predecir el tiempo es decir dónde estará exactamente la
trayectoria. Predecir el clima es decir por qué zonas pasa y cuánto tiempo pasa
en cada una. Lo primero se pierde deprisa; lo segundo es una propiedad del
conjunto, y esa es estable. Es como no saber a qué hora vendrá cada autobús y
saber perfectamente cuántos pasan al día.»

---

### Extensión

**7.Z1** ★ *Pista 1:* busca el relato en primera persona (*The Essence of Chaos*, capítulo 1) antes que cualquier divulgación.
*Pista 2:* fíjate en tres cosas concretas: cuántas ecuaciones tenía el modelo de 1961, qué pensó Lorenz al ver la discrepancia, y quién puso el título de la mariposa.
*Solución:* Tres detalles que la versión popular suele cambiar: (i) Lorenz
sospechó primero de una avería del hardware, no tuvo una revelación;
(ii) el modelo del episodio de 1961 tenía 12 ecuaciones, no las 3 famosas, que
llegaron después buscando el ejemplo mínimo; (iii) el título de la mariposa no
era suyo. La versión popular convierte un proceso de meses en un momento de
inspiración, que es la deformación narrativa habitual y contra la que este
libro insiste una y otra vez.

**7.Z2** ★ *Pista 1:* la demostración de Tucker no es analítica: usa aritmética de intervalos sobre una descomposición del espacio de fases.
*Pista 2:* haz la lista de todo lo que hay que creerse para aceptarla, del compilador para arriba. Esa lista es la respuesta.
*Solución:* Tucker demostró, con aritmética de intervalos y una descomposición
del espacio de fases en cajas verificadas por ordenador, que el atractor de
Lorenz es un atractor genuino y no un artefacto numérico. Aceptarla exige
creerse: el compilador, la aritmética de coma flotante del hardware, la
implementación de la aritmética de intervalos y la lógica del programa. La
comunidad matemática la acepta —resolvió el problema 14 de Smale— pero el
debate sobre qué es una demostración cuando nadie puede leerla entera sigue
abierto, y es un buen tema para el capítulo III.11.
