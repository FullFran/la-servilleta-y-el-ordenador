## Problemas del capítulo 12

**Marcas:** ○ directo · ◐ requiere pensar · ● difícil · ★ abierto.

---

### Calentamiento

**12.C1** ○ Muestreas a 1000 Hz una señal que contiene 100, 400, 600 y 1100 Hz.
¿Qué frecuencias verás en el espectro?

**12.C2** ○ Tienes 4 s de señal muestreada a 8 kHz. ¿Cuál es la resolución en
frecuencia? ¿Y la frecuencia máxima representable?

**12.C3** ○ Un filtro de media móvil de 10 muestras: ¿cuál es su respuesta en
frecuencia? ¿Dónde tiene ceros?

**12.C4** ○ ¿Cuánto tiempo hay que observar para distinguir dos tonos separados
0,1 Hz?

---

### Estimación

**12.E1** ◐ Estima la frecuencia fundamental de tu voz y cuántos armónicos
esperas ver. Compruébalo grabándote.

**12.E2** ◐ Estima cuántas operaciones ahorra la FFT en un escáner de
resonancia magnética típico ($256\times256\times128$ voxeles).

**12.E3** ● Estima la resolución espectral necesaria para separar las líneas de
sodio D1 y D2 (589,0 y 589,6 nm) y la longitud de camino óptico que exige un
interferómetro para conseguirla.

---

### Modelado

**12.M1** ◐ Quieres medir vibraciones de una máquina que gira a 3000 rpm.
Diseña la adquisición: frecuencia de muestreo, duración, filtro antialiasing,
ventana. Justifica cada elección.

**12.M2** ◐ Una señal biológica tiene componentes entre 0,5 y 40 Hz y un
artefacto de red a 50 Hz. Diseña la cadena de procesado y di qué pierdes con
cada paso.

**12.M3** ● Modela qué le hace a un espectro el hecho de que la frecuencia de
la señal derive lentamente durante la medida. ¿Cómo lo detectarías? ¿Cómo lo
corregirías?

---

### Derivación

**12.D1** ◐ Deduce los coeficientes de Fourier a partir de la ortogonalidad de
senos y cosenos. ¿Qué papel juega exactamente la ortogonalidad?

**12.D2** ◐ Demuestra el teorema de convolución para la transformada continua.

**12.D3** ● Deduce el valor del sobrepaso de Gibbs,
$\tfrac12+\tfrac1\pi\int_0^\pi\frac{\sin t}{t}dt$, y explica por qué no depende
del número de armónicos.

**12.D4** ● Deduce la relación $\Delta t\,\Delta\omega\ge1/2$ a partir de la
desigualdad de Cauchy–Schwarz, e identifica qué función alcanza la igualdad.

---

### Computacional

**12.P1** ○ Reproduce la construcción de la onda cuadrada y mide el sobrepaso
de Gibbs para 10, 100 y 1000 armónicos. ¿Converge al valor teórico?

**12.P2** ◐ Implementa una FFT recursiva de Cooley–Tukey para $N=2^k$ y
compárala en tiempo con `np.fft.fft` y con la DFT directa. Dibuja el tiempo
frente a $N$ en log-log.

**12.P3** ◐ Genera ruido $1/f$ y calcula su espectro con periodograma y con
Welch. Mide la varianza del logaritmo del espectro en ambos casos.

---

### Experimento

**12.X1** ◐ Toma una señal con dos tonos cercanos y barre el tamaño de la
ventana de Welch. Dibuja la varianza del espectro y la separación de los picos
frente al tamaño. Localiza el compromiso.

**12.X2** ● Implementa el test de datos sustitutos: genera series con el mismo
espectro y fases aleatorias, y calcula la distribución del máximo del
periodograma. Úsala para poner un nivel de significancia a un pico dudoso.

---

### Detective

**12.T1** ◐ Un espectro de vibración de una máquina que gira a 25 Hz muestra un
pico grande a 3 Hz que nadie sabe explicar. La adquisición es a 100 Hz sin
filtro antialiasing. ¿Qué sospechas?

**12.T2** ◐ Un análisis afirma haber detectado un ciclo de 60 años en una serie
climática de 150 años, con $p<0{,}01$. Enumera las tres objeciones
fundamentales.

**12.T3** ● Un espectro muestra picos a $f_0$, $2f_0$ y $3f_0$. El autor
concluye que la señal contiene tres componentes independientes. Da una
explicación alternativa y di cómo distinguirlas experimentalmente.

---

### Mundo real

**12.R1** ★ Graba diez segundos del ruido de fondo de tu casa y calcula su
densidad espectral. Identifica al menos tres fuentes.

**12.R2** ★ Busca en tu campo un artículo que use FFT. ¿Enventana? ¿Reporta
resolución? ¿Usa periodograma o un estimador consistente?

---

### Feynman

**12.F1** ○ Explica por qué una nota de piano y la misma nota de violín suenan
distintas, usando la palabra «espectro» y ninguna ecuación.

**12.F2** ◐ Explica el compromiso tiempo–frecuencia con un ejemplo cotidiano.

---

### Extensión

**12.Z1** ★ Lee la reconstrucción de Grattan-Guinness sobre la memoria de 1807.
¿Era la objeción de Lagrange razonable con el conocimiento de la época?
Escribe media página defendiendo su posición.

**12.Z2** ★ Estudia el muestreo comprimido (Candès, Romberg, Tao 2006).
¿En qué sentido «rompe» Nyquist y en qué sentido no lo rompe en absoluto?
