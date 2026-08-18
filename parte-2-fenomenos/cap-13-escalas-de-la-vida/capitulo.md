# II.13 — ¿Por qué no hay mamíferos del tamaño de un edificio?

> **El fenómeno:** un ratón come el equivalente a la mitad de su peso al día;
> un elefante, el 4 %.
> **Herramientas:** cap. 1 (estimación), cap. 2 (leyes de escala), cap. 13
> (regímenes), cap. II.3 (ajuste de exponentes).
> **Lo que hay que llevarse:** que las leyes de escala imponen límites duros al
> diseño de los seres vivos, y que un exponente medido es una pregunta abierta,
> no una respuesta.

---

## 1. Una pregunta

::: pregunta
La tasa metabólica de un mamífero escala como su masa elevada a algún
exponente.

El argumento geométrico dice 2/3: el calor se pierde por la superficie, que va
como $M^{2/3}$.

**Los datos dicen 3/4.**

¿De dónde sale ese cuarto de más?
:::

---

## 2. Antes de calcular

::: antes
1. ¿Cuántas veces más come un elefante que un ratón, por kilo de peso?
2. ¿Vive más un animal grande porque su corazón late más despacio, o late más
   despacio porque vive más?
3. ¿Cuál es el mamífero terrestre más grande posible, y qué lo limita?
:::

---

## 3. Los datos

![Ley de Kleiber. Izquierda: tasa metabólica basal frente a masa corporal en cinco décadas, con el ajuste y las dos leyes candidatas. Derecha: las consecuencias del exponente para la potencia específica y los tiempos biológicos. Lo que hay que concluir: el exponente ajustado es 0,747 ± 0,003, mucho más cerca de 3/4 que de 2/3.](figuras/fig_kleiber.pdf)

Con trece especies que cubren cinco órdenes de magnitud de masa, el ajuste da
$0{,}747\pm0{,}003$. La diferencia con 2/3 = 0,667 es de más de veinte
desviaciones típicas.

Y las consecuencias son inmediatas:

$$\frac{P}{M}\propto M^{-1/4},\qquad
t_{\text{biológico}}\propto M^{1/4}$$

* **Potencia por kilo:** un ratón consume unas 30 veces más energía por gramo
  que un elefante. Por eso come constantemente y por eso no puede permitirse
  ayunar.
* **Tiempos biológicos:** frecuencia cardiaca, respiratoria, tiempo de
  gestación y esperanza de vida escalan como $M^{1/4}$. La consecuencia
  llamativa: **el número total de latidos por vida es aproximadamente constante**
  —del orden de $10^9$— para mamíferos que van del ratón a la ballena.

---

## 4. De dónde podría salir el 3/4

Tres explicaciones han competido, y merece la pena verlas porque ilustran tres
maneras distintas de construir un argumento de escala.

**Superficie (2/3).** El calor se pierde por la piel. Es el argumento más
simple y **no reproduce los datos**.

**Redes de distribución (WBE, 1997).** West, Brown y Enquist propusieron que la
tasa metabólica la limita el sistema de distribución de nutrientes, y
derivaron 3/4 suponiendo: red fractal que llena el espacio, capilares
terminales invariantes en tamaño, y minimización de la energía de bombeo. El
argumento es elegante y produce el exponente correcto.

**Restricciones múltiples.** Otros autores sostienen que no hay un único
mecanismo, y que el 3/4 emerge de la combinación de varias limitaciones
—transporte, disipación de calor, resistencia estructural— cada una dominante en
un rango.

::: aviso
**Y aquí conviene ser honesto sobre el estado de la cuestión.**

El modelo WBE ha sido criticado con solidez. Kozłowski y Konarzewski (2004)
señalaron inconsistencias internas en la derivación; White y Seymour (2003)
argumentaron que, controlando por temperatura corporal y estado digestivo, el
exponente en mamíferos está más cerca de 2/3; y varios reanálisis muestran que
el exponente **no es universal**: difiere entre grupos taxonómicos y depende de
si se incluyen aves, reptiles o plantas.

Es decir: **el exponente existe, es reproducible dentro de cada grupo, y su
explicación mecanicista sigue en disputa después de noventa años**.

Contarlo así no es una debilidad del capítulo: es la lección. Un exponente
ajustado con precisión no es una explicación, y confundir la regularidad con su
mecanismo es exactamente el error del capítulo 15.
:::

---

## 5. Los límites duros del tamaño

Independientemente del exponente metabólico, hay tres restricciones geométricas
que sí son inequívocas:

**Estructural.** Del capítulo 2: la tensión en los huesos crece como $M^{1/3}$
si la forma se conserva. Los animales grandes compensan con huesos
proporcionalmente más gruesos y posturas más rectas, pero el margen de
seguridad decrece. El límite terrestre está en torno a las 100 toneladas, y los
saurópodos más grandes lo apuraban.

**Térmica.** La producción de calor va como $M^{3/4}$ y la disipación como
$M^{2/3}$. El cociente crece como $M^{1/12}$: **los animales grandes tienen
problemas para deshacerse del calor**, no para conservarlo. De ahí las orejas
del elefante, que son radiadores con una superficie enorme y muy vascularizados.

**Respiratoria.** El intercambio de gases ocurre por difusión a través de una
superficie. El capítulo II.7 dio el límite: sin sistema circulatorio, unos
milímetros. Con sistema traqueal difusivo, como los insectos, unos centímetros
—y por eso las libélulas gigantes del Carbonífero necesitaban una atmósfera con
más oxígeno—.

**Y por eso el animal más grande de la historia vive en el agua.** La
flotabilidad elimina la restricción estructural, y el agua disipa calor mucho
mejor que el aire. La ballena azul, con 150 toneladas, no podría existir en
tierra.

---

## 6. ¿Cuándo falla?

::: falla
**Falla ajustar exponentes por mínimos cuadrados en log-log.** Del capítulo
II.3: el ajuste está sesgado y las barras de error son optimistas. Con datos
filogenéticos, además, las especies **no son independientes** —comparten
ancestros— y hay que usar métodos comparativos filogenéticos.

**Falla extrapolar fuera del rango.** La ley de Kleiber se ajusta con mamíferos
de 20 g a 4 toneladas. Aplicarla a bacterias o a ballenas azules es
extrapolación, y hay evidencia de que el exponente cambia.

**Falla suponer que el exponente es universal.** Difiere entre grupos, y dentro
de un grupo depende de las condiciones de medida.

**Y falla confundir correlación con mecanismo.** Que los tiempos biológicos
escalen como $M^{1/4}$ no demuestra que exista una red fractal detrás.
:::

---

## 7. Historia

::: historia
**Rubner, Kleiber y noventa años de discusión** · *Nivel de verificación: A.*

Max Rubner propuso en 1883 la ley de superficie: $P\propto M^{2/3}$, con datos
de perros de distintos tamaños. Era el argumento geométrico y encajaba
razonablemente con sus datos.

Max Kleiber, en 1932, con datos de mamíferos que cubrían mucho más rango,
encontró 0,74. Samuel Brody lo confirmó en 1945 con una recopilación mayor. La
comunidad adoptó el 3/4, y se estableció como «ley de Kleiber».

Durante sesenta años se aceptó sin mecanismo. En 1997, West, Brown y Enquist
publicaron en *Science* la derivación fractal, y el asunto se reabrió en lugar
de cerrarse: la derivación fue criticada, la universalidad del exponente fue
cuestionada, y hoy hay al menos tres posiciones defendidas por grupos activos.

**Lo instructivo del episodio** es que una regularidad empírica sólida puede
convivir noventa años con una explicación en disputa, y que la aparición de una
teoría elegante **no zanja** la cuestión: la abre.

**Galileo, 1638** · *Nivel de verificación: A.*

El argumento estructural es mucho más antiguo. En los *Discorsi*, Galileo
razona que un animal el doble de alto necesitaría huesos desproporcionadamente
más gruesos, e incluye un dibujo comparando el hueso de un animal pequeño con
el que necesitaría uno tres veces mayor. Es probablemente el primer argumento
de ley de escala de la historia de la ciencia, y sigue siendo correcto.
:::

---

## 8. Experimento computacional

::: experimento
**Ajusta un exponente honestamente.**

Descarga un conjunto de datos alométricos público (hay varios en Dryad y en
suplementos de artículos). Ajusta el exponente de tres maneras: mínimos
cuadrados en log-log, regresión de eje mayor reducido, y máxima verosimilitud
con error en ambas variables.

*Qué esperar:* los tres dan exponentes distintos, y la diferencia puede ser
comparable a la que separa 2/3 de 3/4.

*Después, lo importante:* calcula el intervalo de confianza de cada uno y
comprueba si tus datos distinguen realmente 0,667 de 0,750. Con pocas especies
y rango limitado, **casi nunca lo hacen**.

Es exactamente el ejercicio del capítulo 15 aplicado a uno de los debates más
longevos de la biología cuantitativa.
:::

---

## 9. Lo esencial

::: esencial
* La tasa metabólica escala como $M^{0,75}$, y el ajuste es sólido: 0,747 ±
  0,003 en cinco décadas.
* De ahí: potencia por kilo $\propto M^{-1/4}$ y tiempos biológicos $\propto
  M^{1/4}$. Los latidos por vida son aproximadamente constantes.
* El mecanismo del 3/4 sigue en disputa noventa años después. Un exponente
  medido con precisión **no es una explicación**.
* Tres límites duros e inequívocos: estructural ($M^{1/3}$ en la tensión ósea),
  térmico ($M^{1/12}$ en el exceso de calor) y respiratorio (difusión).
* El animal más grande vive en el agua porque la flotabilidad elimina el límite
  estructural y el agua disipa mejor.
* Ajustar exponentes en log-log por mínimos cuadrados está sesgado, y las
  especies no son datos independientes.
:::

---

## 10. Preguntas abiertas

::: abierto
* ¿Es 3/4 universal, o hay exponentes distintos por grupo taxonómico?
* ¿Cuál es el mecanismo, si es que hay uno solo?
* ¿Por qué los latidos por vida son aproximadamente constantes, y qué especies
  se salen de la regla —y por qué—?
* ¿Se aplican estas leyes a las ciudades y a las empresas, como se ha
  propuesto, o es una analogía forzada?
:::

### Referencias

* **Kleiber, Max.** *Body size and metabolism.* Hilgardia **6** (1932), 315–353.
  **Nivel A (primaria).**
* **West, G. B.; Brown, J. H.; Enquist, B. J.** *A general model for the origin
  of allometric scaling laws in biology.* Science **276** (1997), 122–126.
  **Nivel A (primaria).**
* **Kozłowski, J. y Konarzewski, M.** *Is West, Brown and Enquist's model of
  allometric scaling mathematically correct and biologically relevant?*
  Functional Ecology **18** (2004), 283–289. **La crítica principal.**
* **White, C. R. y Seymour, R. S.** *Mammalian basal metabolic rate is
  proportional to body mass 2/3.* PNAS **100** (2003), 4046–4049. La posición
  contraria, con datos.
* **Schmidt-Nielsen, Knut.** *Scaling: Why is Animal Size so Important?*
  Cambridge UP, 1984. **La referencia del capítulo**, honesta con las
  discrepancias.
* **Galilei, Galileo.** *Discorsi*, 1638, Jornada Primera. El argumento
  estructural, con dibujo.
* **West, Geoffrey.** *Scale.* Penguin, 2017. Entusiasta y discutido; léase con
  las críticas al lado.
