## Soluciones del capítulo 12

> Las soluciones son razonadas: el número final es lo menos importante. En los
> problemas ● y ★ con solución cerrada hay **Pista 1** y **Pista 2** antes de
> ella; tápalas con la mano y úsalas de una en una.
>
> Los de **Mundo real** (R) no llevan solución a propósito: su procedimiento
> está en el apéndice D.

---

### Calentamiento

**12.C1** Nyquist = 500 Hz. Verás 100 Hz (bien), 400 Hz (bien), 600 Hz
**aparecerá en 400 Hz** y 1100 Hz **aparecerá en 100 Hz**. Es decir, dos picos:
uno en 100 (mezcla de la señal real y del alias de 1100) y otro en 400 (mezcla
de 400 y del alias de 600). **Y son indistinguibles.**

**12.C2** Resolución $\Delta f=1/T=0{,}25$ Hz. Máxima frecuencia
$f_s/2=4$ kHz.

**12.C3** $H(f)=\frac{\sin(\pi f N/f_s)}{N\sin(\pi f/f_s)}$, con $N=10$: un
núcleo de Dirichlet. Ceros en múltiplos de $f_s/10$. Nota importante: la media
móvil tiene **lóbulos laterales grandes**, así que atenúa mal fuera de banda; es
cómoda y es un filtro mediocre.

**12.C4** $T\ge1/0{,}1=10$ s. Y no hay algoritmo que lo evite: es una
propiedad de la transformada, no del método.

---

### Estimación

**12.E1** Voz masculina: 85–155 Hz; femenina: 165–255 Hz. Al ser una señal casi
periódica y muy no sinusoidal, aparecen decenas de armónicos, con la envolvente
(los **formantes**) determinada por la geometría del tracto vocal. Esa
distinción —fundamental frente a formantes— es exactamente lo que permite
distinguir vocales cantadas a la misma nota.

**12.E2** $N=256\times256\times128=8{,}4\times10^6$ voxeles. DFT directa:
$N^2=7\times10^{13}$ operaciones. FFT: $N\log_2N=1{,}9\times10^8$. **Factor
$3{,}6\times10^5$**: la diferencia entre segundos y meses. La resonancia
magnética como técnica clínica existe gracias a la FFT.

**12.E3** ● *Pista 1:* traduce «separar dos líneas» a un número adimensional: $R=\lambda/\Delta\lambda$. Sale del orden de mil.
*Pista 2:* en un interferómetro la resolución la fija la diferencia de camino, $R=2L/\lambda$. Despeja $L$ y mira si es un requisito serio o modesto.
*Solución:* Resolución necesaria: $\lambda/\Delta\lambda=589/0{,}6\approx1000$.
En un interferómetro, $R=2L/\lambda$ con $L$ la diferencia de camino, luego
$L=R\lambda/2\approx0{,}3$ mm. Es un requisito modesto, y por eso la
separación de las líneas D del sodio es un experimento clásico de laboratorio
de grado. El compromiso $\Delta t\,\Delta\omega$ del apartado 4.6 aplicado al
dominio espacial es literalmente el mismo.

---

### Modelado

**12.M1** 3000 rpm = 50 Hz de giro. Interesan armónicos hasta el 20.º, es decir
1 kHz. Muestreo a **4 kHz** (factor 4 sobre Nyquist para dar margen al filtro),
filtro antialiasing analógico con corte en 1,5 kHz, duración ≥ 2 s para
resolución de 0,5 Hz, ventana de Hann (los picos son fuertes y hace falta
controlar la fuga), y Welch con solapamiento del 50 %.

**12.M2** Filtro paso alto a 0,5 Hz (elimina deriva de línea base), filtro
elimina-banda estrecho en 50 Hz (y en 100 y 150, sus armónicos), paso bajo a
40 Hz antes de diezmar. Lo que se pierde: el paso alto distorsiona las
componentes lentas reales; el elimina-banda borra cualquier señal genuina a
50 Hz; y todo filtro con fase no lineal **desplaza en el tiempo** unas
frecuencias respecto a otras, lo que puede alterar la forma de los eventos.
Por eso en biomedicina se usan filtros de fase cero (aplicados hacia delante y
hacia atrás).

**12.M3** ● *Pista 1:* si la frecuencia deriva, el espectro de todo el registro no es la suma de nada: es un promedio que ensancha el pico.
*Pista 2:* trocea el registro y compara la posición del pico entre trozos. Si se mueve, ya sabes qué pasa y cómo corregirlo.
*Solución:* Una frecuencia que deriva convierte un pico estrecho en uno ancho
—o en varios— y reduce la altura. Detección: dividir el registro en segmentos y
comparar la posición del pico entre ellos, es decir, mirar el espectrograma. Si
el pico se mueve, hay deriva. Corrección: seguimiento de fase, o remuestreo en
un «tiempo angular» sincronizado con el giro (*order tracking*), técnica
estándar en diagnóstico de máquinas rotativas.

---

### Derivación

**12.D1** Multiplicando la serie por $\cos mx$ e integrando, todos los términos
se anulan salvo el $m$-ésimo por ortogonalidad. **La ortogonalidad es lo que
convierte un sistema de infinitas ecuaciones acopladas en infinitas ecuaciones
independientes**, exactamente como los autovectores del capítulo 11.

**12.D2** $\widehat{f*g}(\omega)=\int\!\!\int f(\tau)g(t-\tau)e^{-i\omega t}
d\tau\,dt$. Cambiando $u=t-\tau$ y separando,
$=\int f(\tau)e^{-i\omega\tau}d\tau\int g(u)e^{-i\omega u}du
=\hat f\hat g$. La clave es que $e^{-i\omega t}=e^{-i\omega\tau}e^{-i\omega u}$:
**la exponencial convierte una suma de argumentos en un producto**, y ahí está
todo el teorema.

**12.D3** ● *Pista 1:* escribe la suma parcial como una convolución con el núcleo de Dirichlet y busca dónde está su primer máximo.
*Pista 2:* al aumentar $N$ ese máximo se acerca a la discontinuidad exactamente igual de rápido que se estrecha. Por eso la altura del sobrepaso no depende de $N$.
*Solución:* La suma parcial cerca de la discontinuidad tiende a
$\frac{2}{\pi}\int_0^{\pi}\frac{\sin t}{t}dt$ evaluada en el máximo del seno
integral, lo que da $1{,}178979\ldots$. No depende de $N$ porque al aumentar los
armónicos **el máximo se acerca a la discontinuidad a la misma velocidad a la
que se estrecha**: la forma del sobrepaso es invariante bajo reescalado, y sólo
cambia su anchura.

**12.D4** ● *Pista 1:* define $\Delta t$ y $\Delta\omega$ como desviaciones típicas de $|f|^2$ y de $|\hat f|^2$, normalizadas.
*Pista 2:* aplica Cauchy–Schwarz a $tf$ y $f'$, e integra por partes. La igualdad exige que $f'\propto tf$: resuelve esa ecuación y verás qué función es.
*Solución:* Con $\Delta t^2=\int t^2|f|^2/\int|f|^2$ y análogo en $\omega$, la
desigualdad sale de Cauchy–Schwarz aplicada a $tf$ y $f'$, más una integración
por partes. La igualdad se alcanza para la **gaussiana**, y sólo para ella. Es
la razón de que la gaussiana sea la ventana óptima en el compromiso
tiempo–frecuencia y el núcleo de la transformada de Gabor.

---

### Computacional

**12.P1** Converge a 1,178979 desde arriba, con un error que decae como $1/N$.
Con 10 armónicos ya se obtienen tres cifras correctas: el fenómeno se
establece muy deprisa, que es justamente lo que lo hace tan visible.

**12.P2** La DFT directa cruza a la FFT en torno a $N\approx32$–64 en Python
puro. `np.fft.fft` bate a cualquier implementación propia por uno o dos órdenes
de magnitud, porque está en C, usa FFTW o Pocketfft y está optimizada para
caché. **Escribir tu propia FFT es un ejercicio excelente y una mala idea en
producción.**

**12.P3** La desviación típica de $\log_{10}P$ es ~0,7 para el periodograma
—independientemente de $N$— y baja como $1/\sqrt K$ con $K$ segmentos en Welch.
Con 64 segmentos, ~0,09.

---

### Experimento

**12.X1** El producto (resolución × varianza) es aproximadamente constante:
al duplicar la ventana, la resolución mejora al doble y la varianza empeora al
doble, porque hay la mitad de segmentos. **No hay ventana óptima universal:
depende de si te importa más separar picos o medir un fondo suave.**

**12.X2** ● *Pista 1:* no compares el pico con el nivel medio del espectro: compáralo con lo que produce **ruido sin señal** del mismo color.
*Pista 2:* genera muchos sustitutos $1/f$, guarda el máximo del periodograma de cada uno y construye su distribución. El percentil 95 es tu umbral.
*Solución:* Con datos sustitutos, el nivel de significancia del 95 % para el
máximo del periodograma sobre ruido $1/f$ está típicamente **entre 5 y 10 veces
por encima** del nivel medio del espectro a esa frecuencia. Los picos de
«factor 3 sobre el fondo» que se publican habitualmente no llegan ni de lejos.
Es una comprobación que cuesta veinte líneas y desmonta muchos resultados.

---

### Detective

**12.T1** Aliasing. Con $f_s=100$ Hz, Nyquist es 50 Hz, y cualquier componente
por encima se repliega. Un armónico a 197 Hz aparecería en
$|197-2\times100|=3$ Hz. La comprobación: **remuestrear a 500 Hz**. Si el pico
de 3 Hz desaparece o se mueve, era alias. Si se queda donde está, es real.

**12.T2** (i) Sólo caben 2,5 ciclos: la resolución en frecuencia no permite
distinguir 60 de 40 o de 100 años. (ii) En ruido $1/f$ los picos espurios a
frecuencias bajas son la norma. (iii) El $p<0{,}01$ casi seguro se ha calculado
contra ruido **blanco**, que es un modelo nulo inadecuado; contra ruido
coloreado, el mismo pico no sería significativo. Es exactamente el
anti-ejemplo del capítulo.

**12.T3** ● *Pista 1:* tres picos en $f_0$, $2f_0$ y $3f_0$ tienen una explicación mucho más aburrida que tres componentes independientes.
*Pista 2:* diseña el experimento que las separa: barre la amplitud de excitación y mira cómo escala cada pico.
*Solución:* Explicación alternativa: hay **una sola** componente a $f_0$ y el
sistema es no lineal, lo que genera armónicos. Cómo distinguirlas: cambiar la
amplitud de excitación. Si son tres componentes independientes, todas escalan
linealmente con la excitación. Si son armónicos de una no linealidad, el
segundo escala como el cuadrado y el tercero como el cubo. **Un barrido de
amplitud lo resuelve en una tarde**, y es el diagnóstico estándar en
caracterización de sistemas.

---

### Feynman

**12.F1** Guion: «Las dos tocan la misma nota, o sea que el ritmo básico al que
vibra el aire es el mismo. Lo que cambia es la receta: además del ritmo básico,
cada instrumento añade el doble de rápido, el triple, el cuádruple… en
proporciones distintas. Esa receta de proporciones es lo que el oído reconoce
como timbre, y es lo que el espectro dibuja.»

**12.F2** Guion: «Para saber muy bien a qué ritmo pasa algo tienes que mirarlo
durante mucho tiempo, porque si sólo lo miras un instante no puedes saber si
iba a repetirse. Y si lo miras mucho tiempo, ya no sabes decir en qué momento
exacto ocurrió. Es como distinguir dos notas casi iguales: necesitas oírlas
largo rato, y entonces no puedes decir cuándo empezaron.»

---

### Extensión

**12.Z1** ★ *Pista 1:* no juzgues la objeción con las matemáticas de hoy. Pregúntate qué conceptos **no existían** en 1807.
*Pista 2:* haz la lista: definición de convergencia de series de funciones, de integral, distinción entre convergencia puntual y uniforme. Ninguno estaba disponible.
*Solución:* La objeción de Lagrange era razonable y en parte correcta. En 1807
no existía una definición precisa de convergencia de series de funciones, ni de
integral, ni la distinción entre convergencia puntual, uniforme y en media
cuadrática. Afirmar que una suma infinita de funciones analíticas representa
una función con esquinas era, con el aparato disponible, una afirmación sin
contenido preciso. Lo que Lagrange no podía prever es que **la propia necesidad
de responderle** produciría ese aparato. El episodio se entiende mejor como una
disputa productiva que como un error del comité.

**12.Z2** ★ *Pista 1:* escribe las hipótesis de Nyquist y las del muestreo comprimido, una debajo de otra. No son las mismas.
*Pista 2:* la hipótesis extra es dispersión en alguna base conocida. Cuenta grados de libertad y verás de dónde sale el $K\log(N/K)$.
*Solución:* El muestreo comprimido no rompe Nyquist: **cambia la hipótesis**.
Nyquist supone únicamente que la señal está limitada en banda. El muestreo
comprimido supone además que es **dispersa en alguna base conocida**, es decir,
que tiene muchos menos grados de libertad que muestras. Con esa hipótesis
adicional, bastan del orden de $K\log(N/K)$ medidas incoherentes para una señal
de $K$ componentes. Es información previa convertida en muestras ahorradas, y
por eso funciona en resonancia magnética (las imágenes son dispersas en
ondículas) y no en ruido blanco (que no es disperso en ninguna base).
