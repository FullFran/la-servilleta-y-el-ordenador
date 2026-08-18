## Problemas del capítulo 1

**Marcas de dificultad:** ○ directo · ◐ requiere pensar · ● difícil ·
★ abierto, sin solución única.

> **Regla del capítulo.** En todos los problemas marcados como *Estimación*:
> primero estimas, después compruebas. Nada de buscador, nada de IA, nada de
> calculadora durante los primeros quince minutos. Apunta tu número y tu
> intervalo del 90 % **antes** de comprobar nada. El valor del ejercicio está
> en la distancia entre las dos cosas.

---

### Calentamiento

**1.C1** ○ Escribe estas cantidades como potencias de diez con una sola cifra
significativa, de memoria: (a) segundos en un siglo; (b) metros en un
año-luz; (c) átomos en 1 g de carbono; (d) julios en una caloría alimentaria;
(e) vatios de la radiación solar sobre un tejado de 100 m² a mediodía.

**1.C2** ○ ¿Cuántas décadas separan a un protón ($\sim10^{-15}$ m) de una
persona, y a una persona del diámetro de la Vía Láctea? ¿Cuál de los dos saltos
es mayor, y por cuánto?

**1.C3** ○ Un factor 3 son ≈0,48 décadas. ¿Cuántas décadas son un factor 2? ¿Y
un factor 7? ¿Y un factor 1000? Hazlo sin calculadora usando que
$\log_{10}2\approx0{,}30$ y $\log_{10}3\approx0{,}48$.

**1.C4** ○ Si tu estimación tiene una incertidumbre de 0,7 décadas, ¿entre qué
factores está tu respuesta con ~68 % de confianza? ¿Y con ~95 %?

---

### Estimación

**1.E1** ○ ¿Cuántas respiraciones has hecho en tu vida? Da mediana e intervalo
del 90 %.

**1.E2** ◐ ¿Cuánta potencia térmica emite el público de un estadio lleno?
¿Bastaría para calentar el recinto en invierno?

**1.E3** ◐ ¿Cuántos fotones entran por tu pupila cada segundo mirando una
pared blanca bien iluminada?

**1.E4** ◐ ¿Cuánta energía solar recibe tu ciudad en un día despejado de
junio? Compárala con su consumo eléctrico diario.

**1.E5** ◐ ¿Cuántas moléculas se evaporan cada segundo de una taza de café
caliente?

**1.E6** ◐ ¿Cuánto tarda una gota de lluvia en alcanzar su velocidad
terminal? (Sin resolver ninguna ecuación: sólo escalas.)

**1.E7** ◐ ¿Cuántos coches circulan simultáneamente en España a las 8:00 de un
martes? Hazlo por dos caminos independientes: (a) por parque móvil y fracción
de tiempo en marcha; (b) por kilómetros recorridos al año. ¿Coinciden?

**1.E8** ● ¿Cuántos datos genera al año el conjunto de cámaras de tráfico de
una ciudad de un millón de habitantes? ¿Y cuánto costaría almacenarlos todos
durante una década?

**1.E9** ● ¿Con qué frecuencia impacta en la Tierra un meteorito capaz de
destruir una ciudad? Estima el intervalo, no sólo el valor central, y di
explícitamente qué factor domina tu incertidumbre.

**1.E10** ● ¿Cuánta energía hay almacenada en el aire caliente de una
habitación a 22 °C respecto de una a 18 °C? Compárala con la energía que
cuesta calentarla. ¿Por qué no son la misma pregunta?

---

### Modelado

**1.M1** ◐ Un amigo afirma que dejar el portátil enchufado toda la noche
«gasta un dineral». Sin buscar datos, construye el modelo mínimo que decide la
cuestión y di qué cantidad hay que medir para zanjarla.

**1.M2** ◐ Quieres saber si merece la pena poner placas solares en el tejado
de tu edificio. Escribe la descomposición completa de la estimación: qué
factores, qué unidades, cuál conoces peor.

**1.M3** ● Estima la masa total de todas las hormigas del planeta. Después
busca las estimaciones publicadas —hay varias, y difieren— y explica de dónde
viene la discrepancia entre ellas. ¿Qué factor las separa?

---

### Derivación

**1.D1** ◐ Demuestra que si $Q=\prod x_i$ y los errores logarítmicos son
independientes con varianzas $\sigma_i^2$, entonces
$\sigma_{\log Q}^2=\sum\sigma_i^2$. ¿Dónde se usa exactamente la independencia?

**1.D2** ◐ En la estimación de la tormenta despreciamos la energía cinética
del viento y la energía potencial del aire ascendente. Estima ambas y
comprueba que son despreciables. ¿Cuántas décadas por debajo están?

**1.D3** ● Sea $Q=x_1x_2$ con $\log x_1$ y $\log x_2$ correlacionados con
coeficiente $\rho$. Deduce $\sigma_{\log Q}$ y evalúa el caso $\rho=1$ y el
caso $\rho=-1$. ¿En cuál de los dos casos la estimación es *mejor* que con
factores independientes, y qué significa eso en la práctica?

**1.D4** ● Demuestra que si conoces sólo dos cotas $x_{\min}$ y $x_{\max}$ y
supones $\log x$ uniforme entre ellas, el estimador que minimiza el error
cuadrático esperado **en escala logarítmica** es la media geométrica. ¿Cuál
minimizaría el error cuadrático en escala lineal?

---

### Computacional

**1.P1** ○ Reproduce `fig_cancelacion.py` y comprueba numéricamente que
$\sigma_{\log Q}=\sigma\sqrt n$ hasta $n=30$. ¿A partir de qué $n$ empieza a
notarse el error de muestreo con 10 000 realizaciones?

**1.P2** ◐ Escribe una función `estimar(factores, n=100_000)` que reciba una
lista de `(valor_central, factor_incertidumbre)` y devuelva mediana, P5, P95 y
la contribución de cada factor a la varianza. Úsala en tres problemas de la
sección *Estimación*.

**1.P3** ◐ Modifica la simulación de la tormenta para que $A$ y $h$ estén
correlacionados con $\rho=0{,}6$ (tormentas grandes descargan más). ¿Cuánto se
ensancha el intervalo del 90 %? Compáralo con la predicción analítica del
problema 1.D3.

---

### Experimento

**1.X1** ● **Reconstruye a Fermi.** Un trozo de papel que cae libremente es
arrastrado horizontalmente 2,5 m por el paso de una onda de choque. Con un
modelo mínimo del arrastre (la velocidad del papel se iguala rápidamente a la
del aire), estima la velocidad del viento detrás del frente y su duración.
Después, admitiendo la relación $\Delta p \sim \rho_0 u^2$ entre sobrepresión y
velocidad de partícula, y sabiendo que la onda llegó a 16 km en 40 s, estima la
energía de la explosión. ¿Te sale algo entre 5 y 50 kt? Documenta *todos* tus
supuestos: la gracia del problema son ellos, no el número.

**1.X2** ◐ Coge la simulación de la tormenta y barre el factor de
incertidumbre del área desde 1,1 hasta 10. Dibuja el ancho del intervalo del
90 % frente a ese factor. ¿La curva es la que esperabas? ¿Dónde deja de
importar el resto de factores?

---

### Detective

**1.T1** ◐ Un compañero estima la potencia disipada por el cuerpo humano así:
«Comemos unas 2000 kcal al día. Eso son $8{,}4\times10^6$ J. Dividido entre
86 400 s, salen 97 W. Pero como el rendimiento metabólico es del 25 %, la
potencia real es $97/0{,}25 = 388$ W». **Hay un error.** Encuéntralo y explica
por qué el razonamiento parecía sensato.

**1.T2** ◐ Otra estimación: «Un centro de datos con 10 000 servidores de 300 W
consume $3\times10^6$ W. Al año son $3\times10^6 \times 3\times10^7 =
9\times10^{13}$ J, o sea 25 GWh. Como el kWh cuesta 0,15 €, la factura son
3,75 M€ al año. Y como la refrigeración es otro 40 %, el total es 5,25 M€».
Todos los números son correctos y la conclusión final es demasiado baja.
¿Por qué?

**1.T3** ● Una estimación del número de estrellas de la Vía Láctea: «La Vía
Láctea tiene $10^{11}$ estrellas. La densidad cerca del Sol es de una estrella
por cada 10 pc³. El volumen del disco es $\pi(15\ \text{kpc})^2\times0{,}3\
\text{kpc}\approx2\times10^5\ \text{kpc}^3 = 2\times10^{14}\ \text{pc}^3$.
Luego hay $2\times10^{13}$ estrellas, doscientas veces más de lo que dicen los
libros». Localiza el problema. (Hay más de uno.)

---

### Mundo real

**1.R1** ★ Elige una noticia reciente que contenga una cifra grande. Estima esa
misma cifra por tu cuenta, sin mirar el artículo, y compara. Si no coincide en
orden de magnitud, averigua quién se equivoca.

**1.R2** ★ Tu empresa —o tu grupo— quiere saber si merece la pena migrar un
cálculo a GPU. Antes de mirar ningún benchmark, construye la estimación de
orden de magnitud del tiempo, del coste y del ahorro. ¿Qué factor domina la
incertidumbre? ¿Qué medida barata la reduciría más?

---

### Feynman

**1.F1** ○ Explica a alguien que sabe cálculo, sin escribir ni una ecuación,
por qué una estimación con seis factores puede ser mejor que una con dos.

**1.F2** ◐ Explica por qué una respuesta con un intervalo de un factor 40 puede
ser más útil que una respuesta con tres cifras significativas, y pon un ejemplo
donde sea al revés.

---

### Extensión

**1.Z1** ★ Lee el capítulo 1 de *Street-Fighting Mathematics* de Mahajan y
aplica su técnica de «agrupamiento» (*lumping*) a dos de los problemas de
estimación de arriba. ¿Qué añade respecto a lo que hemos hecho?

**1.Z2** ★ Busca la ecuación de Drake y analízala como lo que es: una
descomposición de Fermi. ¿Cuántos factores tiene? ¿Cuál domina la varianza?
Simula la distribución del resultado con incertidumbres logarítmicas honestas
y explica por qué el resultado abarca tantos órdenes de magnitud. Compara con
el análisis de Sandberg, Drexler y Ord (2018), y di si estás de acuerdo.
