# Interludio 2 — Fourier contra la intuición matemática de su época

*Va después del capítulo 12.*

---

El 21 de diciembre de 1807, Joseph Fourier presentó ante la Académie des
Sciences de París una memoria sobre la propagación del calor en los cuerpos
sólidos. Contenía una afirmación que a los evaluadores les pareció, sin
matices, insostenible: que **cualquier** función —incluidas las que tienen
esquinas, saltos o comportamientos arbitrarios en trozos distintos— puede
escribirse como suma de senos y cosenos.

El comité lo formaban Lagrange, Laplace, Monge y Lacroix. Es decir, cuatro de
los cinco o seis mejores matemáticos vivos del planeta.

La memoria no se publicó.

---

## Quién era Fourier

Conviene situarlo, porque no era un aficionado y su biografía explica parte del
episodio.

Jean-Baptiste Joseph Fourier era huérfano, educado por benedictinos, y estuvo a
punto de ser guillotinado dos veces durante el Terror por razones políticas
contradictorias entre sí. Acompañó a Napoleón a Egipto como asesor científico,
donde se ocupó de administración y de arqueología. A la vuelta fue nombrado
prefecto de Isère, en Grenoble, cargo que desempeñó durante catorce años con
notable eficacia: drenó pantanos, construyó carreteras y coordinó la
*Description de l'Égypte*.

La memoria de 1807 la escribió en sus ratos libres de prefecto.

Y el problema del que partía era completamente concreto: **cómo se propaga el
calor**. Fourier no buscaba una teoría general de funciones; buscaba resolver
una ecuación que él mismo había deducido, y para resolverla necesitaba
descomponer una distribución inicial de temperatura arbitraria en piezas que
supiera propagar.

---

## La objeción de Lagrange

Lagrange se opuso, y su objeción no era un prejuicio de anciano.

Cuarenta años antes, en la disputa sobre la cuerda vibrante, él mismo había
discutido con d'Alembert y Euler exactamente esta cuestión. La postura de
Lagrange, defendible con el aparato matemático de la época, era que una suma
infinita de funciones analíticas —senos y cosenos son de lo más suave que
existe— no puede representar una función con una esquina, porque las
propiedades de suavidad deberían heredarse.

Y aquí está la clave del episodio: **Fourier no tenía cómo responder**. No
porque fuera peor matemático, sino porque la respuesta requiere conceptos que
en 1807 no existían. Hacía falta distinguir entre convergencia puntual,
uniforme y en media cuadrática; hacía falta una definición precisa de función,
de límite y de integral. Nada de eso estaba disponible. La palabra «función»
significaba cosas distintas para distintos autores, y a menudo cosas distintas
para el mismo autor en párrafos distintos.

Fourier tenía razón en el resultado y no tenía manera de demostrarlo. Lagrange
tenía razón en la objeción y no tenía manera de precisarla.

---

## Quince años

En 1811, la Académie convocó un premio sobre la propagación del calor. Fourier
presentó una versión ampliada. **Ganó**, y el dictamen del jurado —firmado, otra
vez, por Lagrange y Laplace— incluyó una nota explícita: la memoria dejaba algo
que desear en cuanto a rigor y generalidad.

Con esa reserva anotada, el trabajo no se publicó en las memorias de la
Académie.

En 1817 Fourier fue elegido miembro de la Académie. En 1822, ya secretario
perpetuo —cargo desde el cual controlaba las publicaciones—, publicó por fin la
*Théorie analytique de la chaleur*.

Quince años entre la idea y el libro. La versión de 1822 no responde
técnicamente a la objeción de Lagrange, que había muerto en 1813. Simplemente,
Fourier había dejado de necesitar su permiso.

---

## Y entonces la objeción resultó fértil

La parte que hace este episodio digno de contarse no es que Fourier tuviera
razón. Es lo que produjo el desacuerdo.

En 1829, siete años después del libro y uno antes de la muerte de Fourier,
Peter Gustav Lejeune Dirichlet publicó las primeras condiciones **suficientes**
para la convergencia de una serie de Fourier. Para poder enunciarlas tuvo que
precisar qué era una función —la definición moderna, «una regla que asigna un
valor a cada punto», es esencialmente suya— y qué significaba que una serie
convergiera en un punto.

De ahí en adelante, la cadena es continua: Riemann desarrolló su integral
(1854) en buena medida para tratar las funciones que aparecían en las series
trigonométricas; Cantor llegó a la teoría de conjuntos (1870s) estudiando los
conjuntos de puntos donde una serie de Fourier puede fallar; Lebesgue construyó
su integral (1902) para que la convergencia en media funcionara sin excepciones
molestas.

Es decir: **buena parte del análisis moderno se construyó para poder decir con
precisión si Fourier tenía razón**. La respuesta final, con el aparato completo,
es que la tenía casi siempre y que los casos en que no la tiene son
extraordinariamente sutiles —Kolmogórov construyó en 1926 una función integrable
cuya serie de Fourier diverge en todas partes, y Carleson demostró en 1966 que
para funciones de cuadrado integrable la serie converge en casi todo punto—.

Ciento cincuenta y nueve años entre la memoria y la demostración completa.

---

## Lo que se aprende de esto

Tres cosas, y ninguna es «los expertos se equivocan».

**Primera: una objeción técnica correcta puede retrasar una idea correcta.** Y
no por mala fe. El comité de 1807 estaba haciendo su trabajo: señalar que una
afirmación no estaba demostrada. Lo estaba, en efecto.

**Segunda: el desacuerdo era productivo porque ambas partes veían algo real.**
Fourier veía que el método funcionaba —lo había comprobado resolviendo
problemas de calor—. Lagrange veía que la justificación no existía. Un
desacuerdo así no se resuelve convenciendo a nadie, se resuelve construyendo lo
que falta.

**Tercera, y la más aplicable:** Fourier estaba seguro porque **su método
resolvía problemas concretos**. La confianza no le venía de la elegancia sino
del contraste con la realidad: la ecuación del calor resuelta por su método
predecía temperaturas medibles.

Esa es una lección transferible al trabajo cotidiano. Cuando tengas un método
que funciona y no puedas justificarlo del todo, no lo tires. Anota exactamente
qué es lo que no sabes justificar, sigue usándolo con esa reserva declarada, y
trata el hueco como un problema abierto y no como una vergüenza.

Con frecuencia, el hueco resulta ser más interesante que el método.

---

### Referencias

* **Fourier, Joseph.** *Théorie analytique de la chaleur.* Firmin Didot, 1822.
  **Nivel A (primaria).**
* **Grattan-Guinness, Ivor** (con J. R. Ravetz). *Joseph Fourier 1768–1830.*
  MIT Press, 1972. **Nivel A.** La fuente principal: reconstruye la memoria de
  1807, los dictámenes y la correspondencia.
* **Dirichlet, P. G. L.** *Sur la convergence des séries trigonométriques…*
  J. reine angew. Math. **4** (1829), 157–169. **Nivel A (primaria).**
* **Carleson, Lennart.** *On convergence and growth of partial sums of Fourier
  series.* Acta Mathematica **116** (1966), 135–157. **Nivel A (primaria).**
* **Körner, T. W.** *Fourier Analysis.* Cambridge UP, 1988. Los capítulos
  históricos son excelentes y matemáticamente serios.
* **Bressoud, David.** *A Radical Approach to Real Analysis.* MAA, 2007.
  Cuenta el desarrollo del análisis riguroso **como respuesta** a las series de
  Fourier. Muy recomendable.
