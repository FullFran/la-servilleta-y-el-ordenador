## Soluciones del capítulo 16

> Las soluciones son razonadas: el número final es lo menos importante. En los
> problemas ● y ★ con solución cerrada hay **Pista 1** y **Pista 2** antes de
> ella; tápalas con la mano y úsalas de una en una.
>
> Los de **Mundo real** (R) no llevan solución a propósito: su procedimiento
> está en el apéndice D.

---

### Calentamiento

**16.C1** $7-3=4$ grupos. De $8^7=2{,}1\times10^6$ a $8^4=4096$: **un factor
512**. Es la operación con mejor relación beneficio/esfuerzo de todo el libro.

**16.C2** Rejilla con 100 puntos: en 2D, 10 valores por eje; en 3D, 4 (redondeando
$100^{1/3}$); en 4D, 3. Hipercubo latino: **100 valores distintos en cualquier
dimensión**. La ventaja crece con $d$.

**16.C3** Semilla, versión del intérprete y de cada biblioteca, fichero de
configuración con todos los parámetros, script que regenera la figura, y los
datos de entrada con su procedencia y fecha.

**16.C4** (i) Comparar con $y=y_0e^{-t}$. (ii) Medir el orden de convergencia.
(iii) Comprobar que con $y_0=0$ la solución es idénticamente cero. Una cuarta,
mejor aún: comprobar que el resultado no cambia si expresas el tiempo en otra
unidad.

---

### Estimación

**16.E1** $10^6$ simulaciones × 1 min = $10^6$ min = **1,9 años de CPU**. En
nube a ~0,04 €/hora-núcleo son unos 700 €, y con 1000 núcleos en paralelo,
17 horas de pared. La cuenta importante no es el dinero: es que **con
adimensionalizar y muestrear bien, el mismo estudio cabe en una tarde**.

**16.E2** Los estimadores estándar de Sobol necesitan $N(k+2)$ evaluaciones con
$N\sim10^3$–$10^4$ para un 10 % de precisión. Con $k=5$: entre 7000 y 70 000
evaluaciones. Si cada una es cara, hay que construir un sustituto (proceso
gaussiano o polinomios de caos) con unas cientos y hacer el Sobol sobre él.

**16.E3** ● *Pista 1:* barre $N$ con $\alpha$ fija antes de tocar nada más, y ajusta una ley de potencias al tiempo de recurrencia.
*Pista 2:* al barrer $\alpha$ verás que hay umbral. Prueba a agrupar $\alpha$ con la densidad de energía en un solo parámetro y las curvas colapsarán.
*Solución:* El tiempo de recurrencia crece aproximadamente como $N^{2}$ a
$\alpha$ fija, y disminuye al aumentar $\alpha$. El resultado que hay que
encontrar es que existe un umbral: por debajo, recurrencia; por encima,
termalización en un tiempo que cae rápidamente. El parámetro relevante no es
$\alpha$ sola sino la densidad de energía combinada con ella.

---

### Modelado

**16.M1** En orden de coste: (1) cambiar la semilla; (2) reducir el paso a la
mitad; (3) comprobar conservaciones e invariancias; (4) cambiar de integrador;
(5) cambiar de código o de biblioteca; (6) reproducirlo otra persona desde el
enunciado. Las tres primeras cuestan minutos y descartan la mayoría de los
falsos hallazgos.

**16.M2** Estrategia estándar en tres fases: (i) **cribado** con el método de
Morris, ~100 evaluaciones, para descartar parámetros irrelevantes; (ii)
**exploración** con hipercubo latino sobre los 3–4 supervivientes, ~300
evaluaciones; (iii) **refinamiento** local alrededor de la región interesante,
~100. Total 500, y con mucha más información que 500 puntos de rejilla.

**16.M3** ● *Pista 1:* separa las comprobaciones que no necesitan la respuesta correcta (conservaciones, simetrías, convergencia) de las que sí.
*Pista 2:* la más potente es la que casi nadie hace: fabricar una solución, meterla en la ecuación y quedarte con el término fuente que sobra.
*Solución:* (a) Soluciones manufacturadas para verificar el orden en interior y
bordes. (b) Casos límite con solución analítica (lineal, estacionario,
simétrico). (c) Conservaciones globales (masa, energía). (d) Convergencia de
malla y de paso temporal por separado. (e) Comparación con otro código
independiente, si existe. (f) Invariancia bajo rotación y cambio de unidades.
**El orden importa: (a) primero, porque si falla lo demás sobra.**

---

### Derivación

**16.D1** $n-k$ grupos (capítulo 2). Con $m$ puntos por eje, el ahorro es
$m^{k}$. Con $m=8$ y $k=3$, factor 512.

**16.D2** Por construcción: se divide cada dimensión en $N$ intervalos
equiprobables, se toma una muestra de cada intervalo y se permutan
aleatoriamente los índices entre dimensiones. La proyección sobre cualquier eje
tiene exactamente un punto por intervalo, que es la propiedad que la rejilla no
tiene.

**16.D3** ● *Pista 1:* con $\alpha=0$ la cadena es un sistema lineal de muelles: diagonaliza y saca las frecuencias exactas.
*Pista 2:* mide en la simulación el periodo de oscilación de la energía de cada modo y compáralo. Esta comprobación va **antes** de encender la no linealidad, no después.
*Solución:* $\omega_k=2\sin\!\big(\tfrac{k\pi}{2(N+1)}\big)$ para la cadena de
muelles unitarios. La simulación las reproduce midiendo el periodo de
oscilación de la energía de cada modo en el caso lineal ($\alpha=0$), y esa
comprobación es la primera prueba que hay que pasar antes de encender la no
linealidad.

---

### Computacional

**16.P1** Con Euler explícito y el mismo paso, la energía crece
exponencialmente y la estructura de la recurrencia queda enterrada en unos
pocos miles de pasos. Es la demostración práctica del capítulo 8: **para este
experimento, el integrador no es un detalle de implementación, es parte del
diseño experimental**.

**16.P2** En $d=5$ con 200 puntos: la rejilla no llega ni a 3 puntos por eje y
su error es grande; el aleatorio da $\sim1/\sqrt{200}$; el hipercubo latino
mejora el aleatorio en un factor 2–4 para funciones con efectos principales
dominantes; Sobol es el mejor si la función es suave.

**16.P3** El orden en el interior debería salir 2 para un esquema centrado. Si
en el borde sale 1 y en el interior 2, el orden global observado queda entre
1,5 y 2 —resultado característico— y hay que arreglar el borde.

---

### Experimento

**16.X1** El umbral aparece cuando la densidad de energía por modo supera un
valor crítico; con $N=32$ y las convenciones del capítulo, ocurre en torno a
$\alpha\sim1$ para la amplitud usada. Por encima, la energía se reparte entre
todos los modos en un tiempo que decrece deprisa. Es el resultado de Izrailev y
Chirikov, y su interpretación moderna es que se ha cruzado el umbral de
solapamiento de resonancias.

**16.X2** ● *Pista 1:* con seis parámetros no hagas un barrido en rejilla: muestrea con hipercubo latino y calcula índices de Sobol.
*Pista 2:* casi siempre dos o tres parámetros se llevan toda la varianza. Fija los demás y gasta el presupuesto de cálculo donde sí importa.
*Solución:* El resultado típico —y el que hace útil el ejercicio— es que 2 o 3
de los parámetros explican casi toda la variación, y que los demás se pueden
fijar en su valor nominal sin cambiar ninguna conclusión. Eso reduce la
dimensión efectiva del problema y permite un barrido fino donde importa.

---

### Detective

**16.T1** Falta la barra de error de la media sobre realizaciones y, sobre
todo, la comprobación de que 5 realizaciones bastan. Con 5, el error de la
media es $\sigma/\sqrt5=0{,}45\sigma$: si el efecto buscado es menor que eso,
el resultado no significa nada. **Hay que estimar $\sigma$ primero y decidir
$N$ después**, no al revés.

**16.T2** Un cambio de versión que altera el resultado en un factor 7 indica
que el código depende de detalles no especificados: orden de operaciones,
comportamiento de un algoritmo por defecto que ha cambiado, o —lo más
probable— que el resultado estaba mal condicionado y el 2 % original era
casualidad. **El resultado original no era robusto**, y eso hay que
investigarlo antes que la actualización.

**16.T3** ● *Pista 1:* antes de creerte una anomalía, comprueba que no es del método: otra semilla, otra malla, otro paso.
*Pista 2:* después comprueba que no es del azar: con 50 000 simulaciones, ¿cuántas regiones raras esperarías encontrar aunque no hubiera nada?
*Solución:* (i) ¿Es reproducible con otra semilla? (ii) ¿Sobrevive al refinar
malla y paso? (iii) ¿Es una región del espacio de parámetros **físicamente
alcanzable**, o son valores absurdos? (iv) ¿Está en el borde del dominio
muestreado, donde el modelo puede estar extrapolando? (v) Con 50 000
simulaciones, ¿cuántas regiones anómalas se esperarían por puro azar dado el
ruido? Es look-elsewhere otra vez, y con 50 000 puntos es un efecto grande.

---

### Feynman

**16.F1** Guion: «Un experimento le pregunta a la naturaleza; una simulación le
pregunta a tu modelo. Si tu modelo es bueno, las respuestas se parecen y la
simulación te ahorra un laboratorio. Si tu modelo se ha dejado algo, la
simulación te dará una respuesta preciosa y equivocada, y con toda seguridad no
te avisará. Lo que sí puede hacer, y para eso es insustituible, es enseñarte
consecuencias de tus propias suposiciones que tú no habías previsto.»

**16.F2** Guion: «Si hubiera salido lo esperado, habrían escrito una nota y se
habrían ido a otra cosa: confirmar lo que ya crees no enseña nada. Como salió
otra cosa, tuvieron que preguntarse por qué, y esa pregunta estuvo abierta diez
años. Cuando se resolvió, había un objeto nuevo —el solitón— del que hoy
dependen las comunicaciones por fibra óptica. Lo caro no fue el cálculo: lo
valioso fue no barrer el resultado raro debajo de la alfombra.»

---

### Extensión

**16.Z1** ★ *Pista 1:* busca en LA-1940 lo que hicieron para descartar que la recurrencia fuera un fallo de la máquina. Está escrito, y es más de lo que se suele suponer.
*Pista 2:* ahora haz tu lista para hoy. La diferencia importante no es de técnica: es que ahora se puede publicar el código.
*Solución:* En LA-1940 describen que repitieron los cálculos con distintos
tamaños de paso y comprobaron la conservación de la energía, precisamente para
descartar que la recurrencia fuera un artefacto de la máquina. Hoy, además,
uno: usaría un integrador simpléctico, repetiría con precisión extendida,
compararía con una implementación independiente y publicaría el código y las
semillas. Lo notable es que **el razonamiento de fondo es idéntico**; lo que ha
cambiado es lo barato que resulta hacerlo.

**16.Z2** ★ *Pista 1:* toma el límite continuo de la cadena conservando el término no lineal y el dispersivo **al mismo orden**. Si tiras uno de los dos, pierdes el fenómeno.
*Pista 2:* la ecuación que sale tiene nombre. Y lo decisivo no fue la ecuación, sino dibujar la evolución y ver qué hacen dos pulsos al cruzarse.
*Solución:* Zabusky y Kruskal tomaron el límite continuo de la cadena
conservando el término no lineal y el de dispersión al mismo orden, lo que da
la ecuación de Korteweg–de Vries. La visualización fue decisiva: al dibujar la
evolución vieron pulsos que se cruzaban **sin deformarse**, un comportamiento
que no se buscaba y que no habrían detectado mirando números. Es un caso donde
la gráfica no comunicó un resultado: lo produjo.
