## Soluciones del capítulo 14

> Las soluciones son razonadas: el número final es lo menos importante. En los
> problemas ● y ★ con solución cerrada hay **Pista 1** y **Pista 2** antes de
> ella; tápalas con la mano y úsalas de una en una.
>
> Los de **Mundo real** (R) no llevan solución a propósito: su procedimiento
> está en el apéndice D.

---

### Calentamiento

**14.C1** (a) «¿Cuántos kg de CO₂ equivalente emite un coche eléctrico por
100 km en España, con el mix eléctrico actual, con un error menor del 20 %?»
(b) «¿Cuál es el periodo de retorno de una instalación de 5 kWp en mi tejado,
con un error menor de 2 años?» (c) «¿Reduce el fármaco la mortalidad a 30 días
en más de un 10 % relativo, con una potencia estadística del 80 %?»
**Fíjate en que las tres versiones útiles incluyen un contexto, una unidad y
una precisión.**

**14.C2** rms 0,8 con ruido 0,3: el modelo está incompleto **si además los
residuos tienen estructura**; si no la tienen, has subestimado el ruido. Con
ruido 1,2, el modelo agota la información: seguir añadiendo términos sería
ajustar ruido.

**14.C3** (i) El tiempo característico no debe depender de la temperatura
inicial. (ii) Duplicar la masa con la misma superficie debe duplicar $\tau$.
(iii) Poner una tapa debe aumentar $\tau$ de forma medible. Cualquiera de las
tres, si falla, mata el modelo.

---

### Estimación

**14.E1** Taza abierta: ~25–35 min. Con tapa: ~45–60 min (se elimina la
evaporación, que es el 30–40 % del flujo). Termo: horas a días
($h$ efectivo cae dos órdenes de magnitud). Cadáver: la ley empírica de
Henssge da ~0,8–1 °C/h las primeras horas, es decir $\tau\sim20$–30 h; la
diferencia con la taza está en la masa (60 kg frente a 0,25) y en el
aislamiento de la ropa. Lingote de acero al aire: minutos a decenas de
minutos, y aquí **la radiación domina** desde el principio porque $T$ es alta.

**14.E2** $\lambda=3$/min, $1/\mu=2$ min, luego la carga ofrecida es
$a=\lambda/\mu=6$ erlangs. El mínimo teórico es $c=7$ (con 6 la cola es
inestable). Con $c=7$, $\rho=0{,}857$ y la espera media sale del orden de 1,5
min; con $c=8$, ~0,4 min. **La respuesta es 7 u 8, y el salto entre ambas es
enorme**: ese es el efecto no lineal de la utilización.

**14.E3** ● *Pista 1:* dos mecanismos que ajustan igual sólo se separan donde sus predicciones divergen. Dibuja $T^4$ y $e^{-L/RT}$ y busca dónde se despegan.
*Pista 2:* ahora compara esa diferencia con el ruido de tu termómetro. De ahí salen a la vez el rango de temperaturas y la precisión que necesitas.
*Solución:* Para separar dos mecanismos que ajustan igual hace falta que sus
predicciones difieran más que el ruido en alguna región. Radiación
$\propto T^4$ y evaporación $\propto e^{-L/RT}$ difieren sobre todo a
temperaturas **altas**. Con ruido de 0,35 °C, harían falta medidas por encima
de 90 °C, muy densas en los primeros minutos, y del orden de 0,05 °C de
precisión. Es decir: **es más barato pesar la taza**. Ese razonamiento —comparar
el coste de discriminar por ajuste con el de discriminar por otra medida— es
uno de los cálculos más rentables del oficio.

---

### Modelado

**14.M1** Etapas clave: precisión declarada («±10 minutos»); orden de magnitud
(60 kWh / 7 kW ≈ 8,5 h en casa; / 150 kW ≈ 25 min en rápida); variables
(capacidad, potencia disponible, estado de carga, temperatura, curva de carga);
descartes justificados (marca del cargador, hora del día si la potencia es
fija); supuestos (potencia constante — **falso**: por encima del 80 % la carga
se estrangula deliberadamente); modelo mínimo (carga a potencia constante hasta
el 80 %, exponencial después); crítica (la temperatura de la batería cambia
todo en invierno).

**14.M2** El fenómeno interesante no es la capacidad física sino el **umbral de
comportamiento**: la gente deja pasar el tren cuando la densidad supera un
valor que depende de la cultura y del tiempo hasta el siguiente tren. Es un
modelo de decisión, no de física, y el dato clave es la frecuencia de paso.
Modelo mínimo: umbral de densidad + tiempo de espera esperado. Predicción
falsable: en líneas de mayor frecuencia, la densidad tolerada debe ser menor.

**14.M3** ● No lleva solución, y no es un descuido: el fenómeno lo eliges tú.
Sigue el procedimiento del apéndice D para los problemas sobre trabajo
propio. La única parte que se puede corregir desde fuera es la lista de
**descartes**: si alguno no lleva un motivo cuantitativo al lado, no es un
descarte, es un olvido.

**14.M4** ● *Pista 1:* elige dos modelos con la misma fase inicial y distinto comportamiento asintótico; la epidemia da el ejemplo más limpio.
*Pista 2:* el experimento que los separa no es más datos de lo mismo. Es un dato de **otra escala**: otra región, otro momento, otra magnitud observable.
*Solución:* Ejemplo estándar: crecimiento exponencial con tasa decreciente
frente a ley de potencias, ajustados a la fase inicial de una epidemia. Ajustan
igual y predicen picos que difieren en un orden de magnitud. El experimento que
los separa no es más datos de la misma fase, sino **datos de otra escala**: por
ejemplo, la distribución de tamaños de brotes, o datos de una región que ya ha
pasado el pico.

---

### Derivación

**14.D1** Balance: $mc\,dT/dt=-hA(T-T_a)-\varepsilon\sigma A(T^4-T_a^4)$.
Linealizando la radiación alrededor de $T_a$:
$T^4-T_a^4\approx4T_a^3(T-T_a)$, luego se puede absorber en un $h$ efectivo
$h_{\text{ef}}=h+4\varepsilon\sigma T_a^3$. Válido mientras
$(T-T_a)/T_a\ll1$: con $T_a=294$ K y $\Delta T=71$ K, $\Delta T/T_a=0{,}24$, y
el error de la linealización es del orden del 25 %. **Justo en el límite de lo
aceptable**, y por eso la radiación contribuye al residuo estructurado.

**14.D2** En Daley–Kendall, la fracción final $x$ satisface
$x=1-e^{-(1+\theta)x}$ con $\theta$ la razón entre olvido y transmisión. Para
$\theta=0$ (nadie se aburre) sale $x\to1$; para $\theta=1$, $x\approx0{,}80$.
**Nunca llega a todos** salvo en el límite sin olvido.

**14.D3** ● *Pista 1:* no hace falta la fórmula exacta para ver el comportamiento: basta con saber que la espera diverge cuando la utilización tiende a 1.
*Pista 2:* pregúntate qué le pasa a una cola cuando llega una fluctuación y el sistema apenas tiene capacidad sobrante para drenarla.
*Solución:* La fórmula de Erlang C da
$W_q=\frac{C(c,a)}{c\mu-\lambda}$, que diverge como $1/(1-\rho)$ cuando
$\rho\to1$. La interpretación es la del capítulo 4: cerca de la saturación,
cualquier fluctuación produce una cola que tarda muchísimo en drenar, y la
espera media está dominada por esos episodios. **Ningún sistema con
variabilidad se puede operar cerca del 100 % de utilización**, y esa es una de
las lecciones más transferibles de la teoría de colas: vale para cajas de
supermercado, servidores, quirófanos y carreteras.

---

### Computacional

**14.P1** El tercer término mejora el rms de 0,369 a ~0,36: dentro del ruido.
El $\chi^2_\nu$ apenas cambia y el AIC empeora. **No aporta nada**, y ese es
justamente el criterio de parada.

**14.P2** La simulación por eventos con servicio **determinista** (más realista
que exponencial) da colas del orden de la mitad de las que predice M/M/c. La
discrepancia crece con la utilización. Moraleja: M/M/c es conservador, y
saberlo es útil para dimensionar.

**14.P3** La observación que los distingue es la **fracción final**, no la
velocidad. Medir la velocidad con precisión no ayuda; contar cuánta gente no se
enteró, sí.

---

### Experimento

**14.X1** Con tapa, $\tau$ sube típicamente un 40–70 % y los residuos del
modelo de Newton se reducen mucho: el término no lineal casi desaparece. Es la
confirmación experimental de que el mecanismo que faltaba era la evaporación y
no la radiación —que la tapa apenas modifica—.

**14.X2** ● *Pista 1:* pesa la taza. La masa que falta, por el calor latente, te da los julios que se han ido en evaporación.
*Pista 2:* compáralos con el calor total perdido, $mc\Delta T$. El cociente es la respuesta, y deberías reconocerlo: es justo el déficit que dejaba el modelo de Newton.
*Solución:* Una taza de 250 g que pierde 8 g en dos horas ha evaporado
$8\times10^{-3}\times2{,}4\times10^6=1{,}9\times10^4$ J. Comparado con el calor
total perdido, $0{,}25\times4186\times70=7{,}3\times10^4$ J: **la evaporación es
el 26 % del total**. Coincide en orden de magnitud con el déficit que dejaba el
modelo de Newton. Este es el experimento decisivo, cuesta cinco euros de
báscula y cierra el caso.

---

### Detective

**14.T1** Falta **validación**: el error sobre datos que no se usaron para
calibrar. Con 40 parámetros, un error del 3 % en calibración es esperable
aunque el modelo no tenga ninguna capacidad predictiva. Lo mínimo aceptable es
reservar un año completo y reportar el error sobre él.

**14.T2** No necesariamente. La discrepancia de 0,8 °C a las 3 horas puede
deberse a que $T_{\text{amb}}$ no era constante —la habitación se calentó—, o a
que el termómetro tiene un sesgo de 0,8 °C. **Antes de tocar el modelo, hay que
comprobar la medida**, y en concreto medir $T_{\text{amb}}$ con el mismo
termómetro. Es el bucle rojo del diagrama: revisa supuestos (el 5, en este
caso), no ecuaciones.

**14.T3** ● *Pista 1:* un $\chi^2_\nu$ tiene al menos dos lecturas posibles, y las barras de error entran en las dos. Escríbelas antes de decidir nada.
*Pista 2:* pide lo que un número resumen nunca contiene: los residuos, el error fuera de la muestra y si los 12 parámetros son identificables.
*Solución:* Ninguno de los dos números decide. $\chi^2_\nu=1{,}8$ puede ser
modelo incompleto o barras subestimadas; $\chi^2_\nu=0{,}6$ puede ser
sobreajuste o barras sobreestimadas. Lo que pediría: (i) **las gráficas de
residuos** de ambos; (ii) el error sobre datos de validación no usados; (iii)
AIC o BIC; (iv) si los 12 parámetros del segundo son **identificables** —perfil
de verosimilitud, capítulo 10—. Con esas cuatro cosas la decisión suele ser
evidente; sin ellas, comparar $\chi^2_\nu$ es comparar nada.

---

### Feynman

**14.F1** Guion: «Un modelo complicado que ajusta bien puede estar ajustando
por las razones equivocadas: tiene tantos botones que puede reproducir casi
cualquier cosa, incluido el ruido. Un modelo sencillo tiene pocos botones, así
que si ajusta es porque el mecanismo que has puesto está de verdad ahí. Y si no
ajusta, la forma en que falla te dice qué mecanismo te falta. El sencillo que
falla te enseña; el complicado que acierta, no.»

**14.F2** Guion: «Calibrar es como ajustar la báscula del baño hasta que marque
tu peso conocido. Validar es subirte con una maleta de peso conocido y ver si
acierta. Lo primero siempre sale bien, porque para eso lo has hecho. Lo segundo
es lo único que te dice si la báscula sirve.»

---

### Extensión

**14.Z1** ★ *Pista 1:* busca en *Astronomia Nova* qué dice Kepler sobre la precisión de las observaciones de Tycho, no sobre la órbita.
*Pista 2:* el argumento entero descansa en una comparación entre dos números. Uno es la discrepancia; el otro, la incertidumbre del dato.
*Solución:* Kepler argumenta que Tycho Brahe midió con una precisión de dos
minutos de arco, y que por tanto una discrepancia sistemática de ocho no puede
atribuirse a error de observación. Lo que necesitaba saber era **la
incertidumbre de sus datos, mejor que nadie**, y la conocía porque había
trabajado con ellos durante años. Esa es la condición previa de todo el
capítulo 5 y de este: **no puedes rechazar un modelo si no conoces la
incertidumbre de tus medidas**.

**14.Z2** ★ *Pista 1:* lee el artículo original y anota literalmente el dominio de validez que declara: rangos de temperatura, de concentración, de tamaño.
*Pista 2:* ahora sigue la cadena de citas hacia adelante y marca en qué eslabón desaparece cada condición. Casi siempre desaparecen todas.
*Solución:* Este ejercicio produce casi siempre el mismo hallazgo: el artículo
original declaraba con cuidado un dominio de validez —un rango de temperaturas,
de concentraciones, de tamaños— y las citas posteriores lo fueron perdiendo,
hasta que el modelo se usa rutinariamente fuera de él. Es la forma más común de
error en ciencia aplicada y no aparece en ninguna lista de errores estadísticos.
