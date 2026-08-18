# Interludio 6 — El ordenador que cambió el tiempo de Lorenz

*Va después del capítulo 7.*

---

El invierno de 1961, en el MIT, Edward Lorenz tenía sobre la mesa una Royal
McBee LGP-30. Era una máquina de tubos de vacío del tamaño de un escritorio
grande, con una memoria de tambor magnético, capaz de unas sesenta
multiplicaciones por segundo. Costaba unos 47 000 dólares de la época y Lorenz
la había conseguido para su departamento con cierto esfuerzo.

En ella corría un modelo meteorológico simplificado de doce ecuaciones. Lorenz
estaba interesado en una cuestión muy concreta: si el comportamiento del tiempo
atmosférico es periódico —como sostenían quienes buscaban ciclos y análogos
históricos— o no lo es.

---

## Lo que hizo

Un día quiso examinar con más detalle un tramo de una simulación que ya había
ejecutado. En lugar de repetirla entera desde el principio, hizo lo razonable:
tomó los valores impresos correspondientes a un punto intermedio, los tecleó
como condiciones iniciales y dejó que la máquina siguiera.

Se fue a tomar un café.

Al volver, la nueva ejecución **no se parecía en nada** a la anterior. Al
principio coincidían; al cabo de unos dos meses simulados habían divergido por
completo.

La causa era simple, y Lorenz tardó en verla. La impresora sacaba tres
decimales; la máquina trabajaba internamente con seis. Donde el estado interno
era 0,506127, la impresora había escrito 0,506 y él había tecleado 0,506.

Una diferencia de una parte en cuatro mil.

---

## Lo que hizo con lo que hizo

Aquí está lo importante del episodio, y es lo que la versión popular suele
saltarse.

**La primera reacción de Lorenz fue sospechar de la máquina.** En 1961 eso no
era paranoia: la LGP-30 tenía tubos de vacío, la memoria era un tambor
magnético que giraba, y las averías eran frecuentes. La hipótesis por defecto
ante un resultado incoherente era que se había estropeado algo.

Lorenz lo comprobó. Verificó que las dos ejecuciones coincidían al principio y
divergían después, lo cual descartaba un fallo brusco. Comprobó el número de
decimales de la impresora frente a la precisión interna. Repitió el experimento
con perturbaciones deliberadas.

Sólo después de descartar la avería aceptó que **el comportamiento era real**.

Y sólo entonces vino la parte creativa: entender que si eso ocurría en su modelo
de doce ecuaciones, y si la atmósfera se comportaba de manera parecida,
**entonces la predicción del tiempo a largo plazo era imposible en principio, y
no por falta de ordenadores o de estaciones meteorológicas**.

---

## Las tres ecuaciones

El modelo de doce ecuaciones era demasiado complicado para estudiar el fenómeno
en sí mismo. Lorenz buscó el sistema más simple posible que lo mostrara, y en
1963 publicó *Deterministic Nonperiodic Flow*, con las tres ecuaciones que hoy
llevan su nombre.

Las obtuvo truncando salvajemente una expansión de Fourier de un problema de
convección de Rayleigh–Bénard estudiado por Barry Saltzman. Nunca pretendió que
describieran la convección real: son una **caricatura deliberada**, construida
para exhibir un fenómeno con el mínimo de ingredientes.

Esa decisión metodológica —buscar el ejemplo mínimo que muestre el fenómeno, en
lugar de el modelo más realista— es exactamente el principio del capítulo 14, y
es la razón de que el sistema de Lorenz siga siendo el ejemplo de referencia
sesenta años después.

---

## La mariposa no es suya

El artículo de 1963 se publicó en el *Journal of the Atmospheric Sciences* y
pasó una década prácticamente ignorado fuera de la meteorología. Hoy tiene
decenas de miles de citas; en sus primeros diez años acumuló unas pocas
decenas.

En diciembre de 1972, Lorenz iba a dar una charla en una reunión de la American
Association for the Advancement of Science. No envió título a tiempo, y el
organizador de la sesión, Philip Merilees, le puso uno: *«¿Provoca el aleteo de
una mariposa en Brasil un tornado en Texas?»*.

La metáfora más famosa de la ciencia del siglo XX es obra de un administrativo
con prisa.

Lorenz lo cuenta en *The Essence of Chaos* y añade un matiz que suele
perderse: en su charla explicó que la pregunta no tiene una respuesta simple,
porque un aleteo puede tanto provocar un tornado como **impedir** uno que iba a
ocurrir. La sensibilidad no significa que las causas pequeñas produzcan efectos
grandes de forma controlable; significa que **la relación entre unas y otros se
vuelve incalculable**.

---

## Lo que se aprende

**Primero: la sospecha correcta fue la del fallo técnico.** Ante un resultado
raro, la primera hipótesis debe ser que es tuyo. Lorenz la investigó y la
descartó, y sólo entonces el hallazgo fue un hallazgo. Ese orden es el que el
capítulo 15 recomienda, y es el que separa un descubrimiento de un artefacto.

**Segundo: el fenómeno estaba ahí desde Poincaré.** La sensibilidad a las
condiciones iniciales la había descrito Poincaré en 1890, y la había explicado
con notable claridad en 1908. Cartwright y Littlewood habían encontrado
dinámicas complicadísimas en los años cuarenta. Lo que faltaba no era la idea:
era **poder verla**. La computación no descubrió el caos; lo hizo visible, y por
tanto comunicable.

**Tercero: el problema no se resolvió, se reformuló.** Si no se puede predecir
la trayectoria, se predice la distribución. De ahí vienen las predicciones por
conjuntos que hoy producen los porcentajes de probabilidad de lluvia, y el
horizonte de dos semanas que la meteorología acepta como límite físico y no
como carencia tecnológica.

---

### Referencias

* **Lorenz, Edward N.** *Deterministic Nonperiodic Flow.* J. Atmos. Sci. **20**
  (1963), 130–141. **Nivel A (primaria).**
* **Lorenz, Edward N.** *The Essence of Chaos.* University of Washington Press,
  1993, capítulo 1 y apéndice 1. **Nivel A (memoria).** El relato del episodio
  y el origen del título de la mariposa.
* **Poincaré, Henri.** *Science et Méthode*, 1908, libro I, cap. IV.
  **Nivel A (primaria).**
* **Saltzman, Barry.** *Finite amplitude free convection as an initial value
  problem.* J. Atmos. Sci. **19** (1962), 329–341. **Nivel A (primaria).** El
  trabajo del que Lorenz truncó sus tres ecuaciones.
* **Palmer, Tim.** *The Primacy of Doubt.* Oxford UP, 2022. La predicción por
  conjuntos y el límite de predictibilidad, por un meteorólogo en activo.
* **Gleick, James.** *Chaos.* Viking, 1987. **Nivel B.** Buen ambiente, mala
  cronología: úsese para el clima intelectual, no para las fechas.
