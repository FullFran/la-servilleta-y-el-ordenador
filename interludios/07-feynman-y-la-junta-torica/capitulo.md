# Interludio 7 — Feynman, el hielo y la junta tórica

*Va después del capítulo 15.*

---

El 28 de enero de 1986, el transbordador espacial *Challenger* se desintegró 73
segundos después del despegue. Murieron sus siete tripulantes. La temperatura
en la plataforma de lanzamiento aquella mañana era de −0,6 °C, la más baja de
cualquier lanzamiento del programa.

La Comisión Rogers, encargada de investigar, incluía astronautas, ingenieros,
militares, un antiguo secretario de Estado y un físico teórico de 67 años con
cáncer terminal al que habían convencido para participar: Richard Feynman.

---

## La sesión del 11 de febrero

Durante una sesión pública televisada, con el general Donald Kutyna presidiendo
el interrogatorio a los responsables de la NASA, Feynman pidió la palabra.

Había pedido antes un vaso de agua con hielo. Tenía delante un trozo de junta
tórica del cohete acelerador —el mismo material de las juntas que sellaban las
uniones entre segmentos— y unas tenazas de las que se compran en una ferretería.

Comprimió el material con las tenazas, lo sumergió en el agua helada, esperó, y
lo sacó. El trozo tardó unos segundos en recuperar su forma.

Su comentario, ante las cámaras, fue que había descubierto que ese material
pierde elasticidad a cero grados durante unos segundos.

Un compuesto que tarda segundos en recuperarse no puede sellar una junta que
debe cerrar en milisegundos ante un pico de presión.

---

## Lo que la escena no muestra

La versión que circula presenta el episodio como el momento en que un genio
solitario, con un vaso de agua, desmonta a la burocracia. Es una buena historia
y es incompleta en dos aspectos importantes.

**Primero: Feynman no lo descubrió solo.** El general Kutyna le había orientado
hacia la temperatura. Kutyna, piloto, contó que estaba trabajando en su coche
—un Opel GT— y se preguntó qué le pasaría a las juntas de su carburador a la
temperatura de aquella mañana. Se lo mencionó a Feynman como quien no quiere la
cosa. Kutyna reconoció años después que la información sobre la dependencia con
la temperatura le había llegado de ingenieros de la NASA que no podían hablar
abiertamente sin arriesgar su carrera.

**Segundo: los ingenieros de Morton Thiokol ya lo sabían.** Roger Boisjoly y
otros habían advertido del problema de las juntas a baja temperatura durante
meses, y la noche anterior al lanzamiento mantuvieron una teleconferencia
tensísima recomendando no lanzar. La dirección de Thiokol revirtió la
recomendación de sus propios ingenieros bajo presión.

La demostración de Feynman **no aportó información técnica nueva**. Lo que hizo
fue algo distinto y quizá más difícil: **hacerla incontestable en público**.

---

## Por qué el experimento es tan bueno

Y aquí está la razón de que esto sea un interludio de este libro y no una
anécdota más.

El experimento de las tenazas es, desde el punto de vista del diseño
experimental, casi perfecto:

**Es directo.** No mide un proxy: mide exactamente la propiedad relevante —la
capacidad de recuperación elástica del material— en exactamente la condición
relevante —la temperatura del lanzamiento—.

**Es binario.** No produce un número con barras de error que haya que discutir.
Produce un sí o un no visible: el material vuelve o no vuelve.

**Es barato.** Un vaso de agua, hielo y unas tenazas.

**Es reproducible por cualquiera.** Y esa es la propiedad decisiva en un
contexto público: nadie puede responder «nuestros modelos dicen otra cosa»,
porque cualquiera puede repetirlo.

**Y es imposible de refutar apelando a la autoridad.** Un análisis de elementos
finitos se puede discutir. Un trozo de goma que no recupera su forma, no.

Es exactamente lo que el capítulo 15 llama la prueba que mata un modelo: la
observación más simple que discrimina entre dos hipótesis, hecha en condiciones
donde el resultado no admite interpretación.

---

## El apéndice F

Feynman quiso incluir en el informe de la comisión sus propias conclusiones,
que iban bastante más allá de las juntas. Hubo negociaciones; finalmente se
publicaron como **apéndice F**, separado del cuerpo principal.

El texto merece leerse entero. Su hallazgo central es cuantitativo: la
dirección de la NASA estimaba la probabilidad de fallo catastrófico por
lanzamiento en 1 entre 100 000; los ingenieros que trabajaban en los
componentes la estimaban en torno a 1 entre 100.

**Tres órdenes de magnitud de discrepancia dentro de la misma organización.**

Feynman analiza de dónde sale esa diferencia, y su explicación es
estructuralmente interesante: la cifra de la dirección no procedía de ningún
cálculo, sino de un razonamiento circular sobre la necesidad de que el programa
fuese seguro. Y describe el mecanismo por el que cada vuelo con erosión parcial
de las juntas —que no estaba prevista en el diseño— se interpretaba como
evidencia de margen de seguridad en lugar de como señal de alarma.

El apéndice termina con una frase que se ha citado miles de veces y que resume
todo el capítulo 15 en once palabras: para una tecnología con éxito, la
realidad debe tener prioridad sobre las relaciones públicas, porque a la
naturaleza no se la puede engañar.

---

## Lo que se lleva un modelador

**El experimento decisivo suele ser barato.** Cuando hay un desacuerdo, la
pregunta que hay que hacerse no es «¿qué análisis lo resolvería?» sino «¿cuál es
la observación más simple que discrimina?». Muchas veces cabe en un vaso.

**La normalización de la desviación es un modo de fallo.** Cuando un sistema se
comporta fuera de su diseño y no pasa nada, la interpretación fácil es que había
margen. La correcta es que el modelo del sistema está mal y ya no sabes dónde
está el margen. Diane Vaughan lo estudió después en detalle y le puso nombre.

**Las estimaciones de probabilidad sin cálculo son propaganda.** Un 1 entre
100 000 que no procede de ningún modelo explícito no es una estimación: es una
expresión de deseo con formato numérico. La pregunta que hay que hacer siempre
—y Feynman la hizo— es «¿de qué cálculo sale ese número?».

---

### Referencias

* **Rogers Commission.** *Report of the Presidential Commission on the Space
  Shuttle Challenger Accident*, 1986, y en particular el **apéndice F**,
  *Personal Observations on the Reliability of the Shuttle*, de R. P. Feynman.
  **Nivel A (primaria).** Ambos son de dominio público.
* **Feynman, Richard P.** *What Do You Care What Other People Think?* W. W.
  Norton, 1988, segunda parte. **Nivel A (memoria).** Su relato de la comisión;
  téngase en cuenta que es parte interesada.
* **Vaughan, Diane.** *The Challenger Launch Decision.* University of Chicago
  Press, 1996. **Nivel A.** El estudio sociológico definitivo, y el origen del
  concepto de normalización de la desviación. Corrige la narrativa simple de
  «villanos contra héroes».
* **Boisjoly, Roger.** Testimonios ante la comisión y conferencias posteriores
  sobre ética en ingeniería. **Nivel A (primaria).**
* **Kutyna, Donald.** Entrevistas posteriores sobre su papel y el origen de la
  pista de la temperatura. **Nivel B.**
