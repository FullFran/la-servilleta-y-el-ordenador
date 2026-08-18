# Interludio 1 — Fermi y los papelitos

*Va después del capítulo 1.*

---

A las 5:29:45 de la mañana del 16 de julio de 1945, en un tramo de desierto de
Nuevo México que los españoles habían llamado Jornada del Muerto, un
dispositivo de plutonio del tamaño de un balón grande liberó, en unos
microsegundos, la energía de veinte mil toneladas de trinitrotolueno.

A dieciséis kilómetros del punto cero, en el puesto de observación de la Base
Camp, Enrico Fermi estaba tumbado boca abajo con la cara hacia el suelo, como
se les había ordenado a todos. Llevaba en la mano un puñado de trocitos de
papel.

Cuarenta segundos después de la detonación, cuando llegó la onda de choque,
Fermi se levantó y los dejó caer.

---

## Lo que escribió

El informe que redactó poco después se conserva. La parte pertinente dice, en
traducción:

> «Unos 40 segundos después de la explosión me alcanzó la onda de choque.
> Intenté estimar su intensidad dejando caer desde una altura de unos seis pies
> pequeños trozos de papel antes, durante y después del paso de la onda. Como
> en aquel momento no había viento, pude observar con claridad y medir de hecho
> el desplazamiento de los trozos de papel que estaban cayendo mientras pasaba
> la onda. El desplazamiento fue de unos dos metros y medio, que en ese momento
> estimé que correspondía a la onda que produciría una explosión de diez mil
> toneladas de TNT.»

Diez kilotones. El valor que se acepta hoy, tras décadas de análisis de las
mediciones instrumentales y de los datos radioquímicos, ronda los 21.

Fermi se equivocó por un factor 2.

---

## Por qué esto no es una historia sobre cálculo mental

Es tentador contar el episodio como una proeza de virtuosismo aritmético: el
genio que hace de cabeza lo que a otros les cuesta semanas de instrumentación.
Esa versión circula, y es la menos interesante de las posibles.

Lo primero que hay que decir es que **Fermi no era el único midiendo**. En
Trinity había docenas de instrumentos: medidores de presión, cámaras de alta
velocidad, detectores de radiación, sismógrafos. Había un programa de medida
completo, con presupuesto y con personal. La estimación de Fermi no llenaba
ningún hueco: iba a haber una cifra oficial en cuestión de días.

Lo segundo, y más incómodo para la leyenda: **el cálculo detallado de Fermi no
se conserva**. Lo que aparece en los libros son reconstrucciones plausibles a
partir de las relaciones estándar de ondas de choque, hechas después por otros.
Sabemos lo que midió y lo que concluyó. No sabemos exactamente cómo pasó de una
cosa a la otra.

Entonces, ¿por qué lo hizo?

---

## Un número sin otro número al lado es un acto de fe

La respuesta está en la estructura de la decisión, no en la aritmética.

Fermi sabía que en las horas siguientes habría una cifra producida por
instrumentación cara y compleja. Sabía también que esa instrumentación era
nueva, que se había construido para un experimento que sólo iba a hacerse una
vez, y que nadie había podido calibrarla contra una explosión nuclear previa
por la sencilla razón de que no las había.

Un instrumento sin verificación independiente puede estar equivocado por un
factor 10 y nadie lo sabría. Lo único que permite detectarlo es **otra medida,
obtenida por un camino completamente distinto**, aunque sea mucho peor.

Eso es lo que hacen los papelitos. No compiten con los sensores de presión: los
**vigilan**. Si el análisis instrumental hubiera dado 200 kilotones o 500
toneladas, la estimación de Fermi habría sido la señal de que algo estaba mal
en la cadena de análisis.

Es el mismo principio que en el capítulo 1 llamamos estimar por dos caminos
independientes, y que en metrología se llama comparación interlaboratorio. Lo
notable es que Fermi lo aplicara **tumbado en la arena, cuarenta segundos
después de la primera explosión nuclear de la historia**, con lo que llevaba en
el bolsillo.

---

## Lo que hace falta para poder hacerlo

Y aquí está la parte que sí se puede aprender, que es la razón de contar esto.

Para dejar caer papelitos y sacar una energía hay que haber decidido, **antes**,
varias cosas:

Que el desplazamiento de un objeto ligero mide el impulso del aire, no la
presión estática. Que un papel alcanza la velocidad del aire en un tiempo
despreciable frente a la duración del pulso. Que el desplazamiento acumulado es
esencialmente la integral de la velocidad del aire durante la fase positiva.
Que la sobrepresión se relaciona con esa velocidad. Y que la energía de la
explosión se relaciona con la sobrepresión a una distancia dada mediante una
ley de escala.

Ninguna de esas cinco cosas se improvisa en cuarenta segundos. Lo que se
improvisa es el instrumento —papel— y el momento. **La física estaba pensada de
antes.**

Ese es el patrón, y es el que este libro persigue: la capacidad de estimar en
el momento no consiste en calcular deprisa. Consiste en tener ya construida, y
disponible, la cadena de razonamiento que conecta lo observable con lo que
quieres saber. Cuando llega el instante, sólo hay que rellenar un número.

---

## El error como parte del método

Fermi falló por un factor 2 y anotó el número sin dramatismo, con la
observación de que era una estimación hecha en ese momento.

Merece la pena hacer la cuenta que hicimos en el capítulo 1. Su reconstrucción
requiere al menos cuatro supuestos, cada uno con una incertidumbre razonable de
un factor 2 —la duración del pulso, la relación entre desplazamiento y
velocidad, la relación entre velocidad y sobrepresión, la ley de escala—. Con
errores independientes de $\sigma\approx0{,}3$ décadas cada uno, la
incertidumbre total es $\sqrt4\times0{,}3=0{,}6$ décadas: **un factor 4**.

Fermi acabó a un factor 2 del valor real. Es decir: **dentro de su propia barra
de error**, y en la mitad buena.

Eso es lo que convierte la anécdota en ciencia y no en magia. No acertó por
suerte ni por genialidad inescrutable: hizo una estimación cuya incertidumbre
él sabía acotar, y el resultado cayó donde tenía que caer.

---

## Coda: el resto de la historia

Fermi hizo muchas más estimaciones aquella semana, algunas menos afortunadas.
En el trayecto al emplazamiento, según varios testimonios, ofreció apuestas a
sus colegas sobre si la atmósfera se incendiaría, y si lo haría sólo en Nuevo
México o en todo el planeta. Los oficiales presentes no encontraron la broma
divertida. La cuestión de la ignición atmosférica se había estudiado en serio
en 1942 —el informe LA-602, de Konopinski, Marvin y Teller— y se había
descartado con margen amplio; la apuesta era una manera muy suya de aliviar la
tensión de la espera.

Diez años después, en 1955, Fermi moría de cáncer de estómago a los 53 años.
Entre sus últimos trabajos estaba una simulación numérica en la máquina de Los
Álamos que no dio el resultado esperado y que abrió, sin que él llegara a
saberlo, medio campo de la física no lineal. De eso trata el interludio 8.

---

### Referencias

* **Fermi, Enrico.** *My Observations During the Explosion at Trinity on July
  16, 1945.* Informe manuscrito, 1945. Archivos de Los Alamos.
  **Nivel A (primaria).** Es la fuente de la cita.
* **Rhodes, Richard.** *The Making of the Atomic Bomb.* Simon & Schuster, 1986,
  capítulo 18. **Nivel A (secundaria).** La reconstrucción documentada del día,
  con las fuentes citadas una a una.
* **Segrè, Gino y Hoerlin, Bettina.** *The Pope of Physics.* Henry Holt, 2016.
  **Nivel A.** El contexto biográfico.
* **Konopinski, E. J.; Marvin, C.; Teller, E.** *Ignition of the Atmosphere with
  Nuclear Bombs.* LA-602, 1946 (trabajo de 1942). **Nivel A (primaria).** El
  estudio que descartó la ignición atmosférica.
* **Taylor, Geoffrey I.** Proc. R. Soc. A **201** (1950), partes I y II. Para la
  ley de escala que permite reconstruir el cálculo (capítulo 2).
