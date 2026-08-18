# Interludio 5 — Cuando von Neumann empezó a pensar en ordenadores

*Va después del capítulo 8.*

---

En el verano de 1944, John von Neumann esperaba un tren en el andén de la
estación de Aberdeen, Maryland. Un joven llamado Herman Goldstine, teniente y
matemático, lo reconoció y se acercó a hablar con él.

Goldstine cuenta en sus memorias que la conversación fue amable y trivial hasta
que mencionó que en Filadelfia se estaba construyendo una máquina electrónica
capaz de hacer más de trescientas multiplicaciones por segundo. A partir de ese
momento, dice, la conversación pasó de ser un intercambio de cortesías a
parecerse a un examen de doctorado.

Von Neumann llevaba meses atascado en un problema que no podía resolver.

---

## El problema

Ese problema era la hidrodinámica de las implosiones.

El diseño del arma de plutonio de Los Álamos requería comprimir una esfera de
material fisible mediante una onda de choque convergente producida por
explosivos. Para que funcionara, la onda tenía que ser esférica con una
precisión extraordinaria; cualquier asimetría arruinaba la compresión.

Las ecuaciones que describen eso —hidrodinámica compresible con ondas de choque
en geometría esférica— no se resuelven analíticamente. No es que sea difícil:
es que no hay solución cerrada.

En Los Álamos había un grupo de computistas humanos —en buena parte mujeres,
muchas de ellas esposas de los físicos— operando calculadoras electromecánicas
IBM. Podían hacer cálculos por diferencias finitas, pero un problema
bidimensional con resolución razonable requería meses.

Von Neumann no estaba buscando una máquina por curiosidad tecnológica.
**Necesitaba una para resolver un problema concreto que le estaba bloqueando.**

---

## Lo que aportó

Von Neumann no inventó el ordenador. El ENIAC lo estaban construyendo John
Mauchly y J. Presper Eckert en la Moore School de Filadelfia, y llevaban dos
años en ello cuando él apareció.

Lo que aportó fue una manera de pensar sobre la máquina.

El ENIAC se programaba **cableándolo**: cambiar de problema exigía días de
reconfiguración física de conexiones y conmutadores. Von Neumann, que venía de
la lógica matemática y conocía el trabajo de Turing de 1936 —Turing había sido
estudiante de doctorado en Princeton cuando von Neumann estaba allí—, planteó
la cuestión en términos distintos: si las instrucciones son información, ¿por
qué no guardarlas en la misma memoria que los datos?

El *First Draft of a Report on the EDVAC*, de junio de 1945, describe esa
arquitectura: unidad aritmética, unidad de control, memoria única para
instrucciones y datos, entrada y salida.

Firmaba una sola persona. Goldstine lo distribuyó ampliamente, y el resultado
fue doble: la arquitectura se difundió con enorme rapidez y quedó en el dominio
público —cosa que von Neumann consideraba deseable— y Eckert y Mauchly, que
habían contribuido sustancialmente a las ideas, perdieron la posibilidad de
patentarlas. La disputa envenenó las relaciones durante años, y el término
«arquitectura de von Neumann» sigue arrastrando esa injusticia parcial.

---

## Lo que hizo con ella

Aquí está la parte que interesa a este libro. Von Neumann no se dedicó a
construir máquinas: se dedicó a **descubrir qué se podía hacer con ellas**, y
el catálogo de lo que abordó en los diez años siguientes es asombroso.

Métodos de Monte Carlo, con Ulam (interludio 3). Análisis de estabilidad de
esquemas de diferencias finitas —el análisis de von Neumann del capítulo 8—.
Viscosidad artificial para tratar ondas de choque numéricamente. La primera
predicción meteorológica por ordenador, con Charney y Fjørtoft en el ENIAC en
1950. Generación de números pseudoaleatorios. Autómatas celulares y
autorreproducción. Y la teoría de juegos y la economía matemática, en paralelo.

El patrón es reconocible: **una herramienta nueva no se explota resolviendo más
deprisa los problemas antiguos, sino preguntando qué problemas se vuelven
abordables por primera vez**.

---

## La advertencia que dejó escrita

En 1949, en una conferencia, von Neumann formuló una objeción a su propio
programa que sigue vigente y que casi nadie cita.

Vino a decir que si uno permite dos parámetros libres puede ajustar un
elefante, y con tres puede hacerle mover la trompa. La versión que circula
—atribuida a él por Enrico Fermi en un relato de Freeman Dyson— es
probablemente una paráfrasis; la formulación exacta no está documentada en
fuente primaria, así que conviene citarla como lo que es.

Lo que sí está documentado, y es más interesante, es su preocupación explícita
por que la capacidad de calcular soluciones numéricas de ecuaciones muy
complicadas produjera una ilusión de comprensión. Advertía de que resolver no es
entender, y de que un cálculo con muchos parámetros ajustables puede reproducir
cualquier cosa sin contener ninguna física.

Es exactamente el capítulo 15 de este libro, escrito por quien más había hecho
por que los ordenadores existieran.

---

## Coda

Von Neumann murió en 1957, a los 53 años, de un cáncer probablemente relacionado
con su exposición a la radiación en las pruebas nucleares. Sus últimos meses los
pasó preparando las conferencias Silliman de Yale, que no llegó a dar. Se
publicaron póstumamente como *The Computer and the Brain*.

Es un libro corto, inacabado y sorprendentemente humilde. Su tesis central es
que el cerebro y el ordenador hacen cosas comparables con arquitecturas
radicalmente distintas, y que la diferencia más importante es que el cerebro
trabaja con precisión muy baja y una fiabilidad global muy alta, mientras que el
ordenador hace lo contrario.

Sesenta y cinco años después, esa observación sigue siendo el mejor punto de
partida para pensar en qué se parecen y en qué no.

---

### Referencias

* **von Neumann, John.** *First Draft of a Report on the EDVAC.* Moore School,
  1945. **Nivel A (primaria).**
* **von Neumann, John.** *The Computer and the Brain.* Yale UP, 1958.
  **Nivel A (primaria).**
* **Goldstine, Herman H.** *The Computer from Pascal to von Neumann.* Princeton
  UP, 1972. **Nivel A (memoria).** La fuente del encuentro en la estación de
  Aberdeen; téngase en cuenta que Goldstine es parte interesada en la disputa
  de crédito.
* **Aspray, William.** *John von Neumann and the Origins of Modern Computing.*
  MIT Press, 1990. **Nivel A.** La historia rigurosa, cuidadosa con las
  atribuciones.
* **Charney, J.; Fjørtoft, R.; von Neumann, J.** *Numerical Integration of the
  Barotropic Vorticity Equation.* Tellus **2** (1950), 237–254.
  **Nivel A (primaria).**
* **Dyson, George.** *Turing's Cathedral.* Pantheon, 2012. **Nivel B.**
  Narrativo y muy legible; algunas atribuciones técnicas se han discutido.
* **Mayer, Jürgen y otros.** *Drawing an elephant with four complex
  parameters.* American Journal of Physics **78** (2010), 648–649. La
  comprobación, hecha en serio, de la frase del elefante.
