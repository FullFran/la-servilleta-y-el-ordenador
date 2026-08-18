# Bibliografía comentada

*Fase 3 del encargo. Ninguna fuente aparece aquí sin haber sido comprobada: título, autores, año y que diga lo que se afirma que dice.*

> Para cada fuente: **qué aporta**, **qué capítulos apoya**, **nivel**,
> **fiabilidad** y si es **primaria** o **secundaria**.
>
> **Nivel:** ◆ divulgación seria · ◆◆ grado · ◆◆◆ posgrado · ◆◆◆◆ especialista.
> **Fiabilidad:** ★★★ referencia estándar, verificable · ★★ fiable con matices ·
> ★ útil pero hay que contrastar (memorias, divulgación, tradición oral).
>
> La clave BibTeX de cada entrada está en `refs.bib`.

---

## 1. Fuentes primarias: los protagonistas escribiendo

### 1.1 Estimación, física e intuición

**Fermi, Enrico — *My Observations During the Explosion at Trinity on July 16,
1945*** (informe manuscrito, 1945; Los Alamos, LA archives; reproducido en
recopilaciones de documentos del Proyecto Manhattan). `fermi1945trinity`
· **Aporta:** el texto donde Fermi describe, en primera persona, cómo dejó caer
trozos de papel y midió un desplazamiento de unos 2,5 m para estimar unos 10
kilotones. Es la fuente que convierte una anécdota en un dato.
· **Capítulos:** 1, Interludio 1. · **Nivel:** ◆ · **Fiabilidad:** ★★★
· **Primaria.**
· **Cautela:** el rendimiento real se estima hoy en torno a 21 kt. El interés no
es que Fermi acertara —falló por un factor 2— sino que acertara *el orden de
magnitud* en un minuto y sin instrumentos.

**Fermi, Enrico — *Thermodynamics*** (1937) y ***Notes on Quantum Mechanics***
(1961). `fermi1937thermo`
· **Aporta:** el estilo Fermi: mínimo formalismo, máximo contenido físico por
página. Modelo de cómo se escribe una derivación sin adornos.
· **Capítulos:** 6, 13. · **Nivel:** ◆◆ · **Fiabilidad:** ★★★ · **Primaria.**

**Feynman, Leighton, Sands — *The Feynman Lectures on Physics*** (1964; edición
en línea gratuita del Caltech). `feynman1964lectures`
· **Aporta:** la referencia de cómo construir intuición física antes que
formalismo. Especialmente: vol. I cap. 22 (álgebra), cap. 41 (movimiento
browniano), vol. II cap. 19 (principio de mínima acción).
· **Capítulos:** 3, 6, 9, 12, 13, III.10. · **Nivel:** ◆◆ · **Fiabilidad:** ★★★
· **Primaria.**

**Feynman, Richard — *The Character of Physical Law*** (1965). `feynman1965character`
· **Aporta:** siete conferencias sobre qué es una ley física, cómo se descubre y
por qué la misma matemática reaparece. El capítulo sobre «la misma ecuación una
y otra vez» es la tesis de la Parte II del libro, dicha veinte años antes.
· **Capítulos:** 6, 12, II.3, III.12. · **Nivel:** ◆ · **Fiabilidad:** ★★★
· **Primaria.**

**Feynman, Richard — *QED: The Strange Theory of Light and Matter*** (1985).
`feynman1985qed`
· **Aporta:** el ejemplo canónico de explicar algo profundo sin ecuaciones. Se
usa como modelo en el capítulo III.10.
· **Capítulos:** III.10. · **Nivel:** ◆ · **Fiabilidad:** ★★★ · **Primaria.**

**Feynman, Richard — *Surely You're Joking, Mr. Feynman!*** (1985).
`feynman1985joking`
· **Aporta:** episodios sobre cómo abordaba problemas nuevos; el ábaco, las
integrales, Los Álamos.
· **Capítulos:** 1, 13, 15. · **Nivel:** ◆ · **Fiabilidad:** ★
· **Primaria (memoria).**
· **Cautela importante:** es literatura oral transcrita por Ralph Leighton,
autopromocional y sin corroboración externa en casi ningún episodio. El libro la
usa **como memoria, nunca como registro**, y en el capítulo 15 se emplea
precisamente para hablar de cómo se construyen las leyendas científicas.

**Feynman, Richard — *Cargo Cult Science*** (discurso de graduación, Caltech,
1974; recogido en *Surely You're Joking*). `feynman1974cargo`
· **Aporta:** el análisis de la deriva histórica de la carga del electrón tras
Millikan: cómo un sesgo se hereda durante décadas porque nadie quiere ser el que
se aleja del valor aceptado. Es el mejor texto breve sobre honestidad
metodológica que existe.
· **Capítulos:** 15, III.7. · **Nivel:** ◆ · **Fiabilidad:** ★★★ · **Primaria.**

### 1.2 Monte Carlo y computación

**Ulam, Stanisław — *Adventures of a Mathematician*** (1976). `ulam1976adventures`
· **Aporta:** el relato en primera persona del origen del método de Monte Carlo
durante su convalecencia jugando al solitario de Canfield (1946), y una
descripción de primera mano del ambiente intelectual de Los Álamos.
· **Capítulos:** 9, 16, Interludio 3. · **Nivel:** ◆ · **Fiabilidad:** ★★
· **Primaria (memoria).**
· **Cautela:** memoria escrita treinta años después. Coherente con otras fuentes
en lo esencial (el solitario, la fecha, el papel de von Neumann).

**Metropolis, Nicholas — *The Beginning of the Monte Carlo Method***, Los Alamos
Science 15 (1987), 125–130. `metropolis1987beginning`
· **Aporta:** el origen del nombre «Monte Carlo» contado por quien lo propuso, y
la cronología del trabajo en el ENIAC.
· **Capítulos:** 9, Interludio 4. · **Nivel:** ◆ · **Fiabilidad:** ★★
· **Primaria (memoria).**

**Metropolis, Nicholas; Ulam, Stanisław — *The Monte Carlo Method***, Journal of
the American Statistical Association 44 (1949), 335–341. `metropolis1949mc`
· **Aporta:** la primera exposición pública del método en la literatura
estadística. Corto y perfectamente legible hoy.
· **Capítulos:** 9. · **Nivel:** ◆◆ · **Fiabilidad:** ★★★ · **Primaria.**

**Metropolis, Rosenbluth, Rosenbluth, Teller, Teller — *Equation of State
Calculations by Fast Computing Machines***, J. Chem. Phys. 21 (1953), 1087–1092.
`metropolis1953equation`
· **Aporta:** el algoritmo. Merece leerse entero: son seis páginas y el argumento
del balance detallado está ahí, explícito.
· **Capítulos:** 9, 10, II.9. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★
· **Primaria.**
· **Cautela sobre autoría:** véase Gubernatis (2005) más abajo.

**von Neumann, John — *Various Techniques Used in Connection with Random
Digits***, National Bureau of Standards Applied Mathematics Series 12 (1951),
36–38. `vonneumann1951random`
· **Aporta:** el método del cuadrado medio, el muestreo por rechazo y la frase
sobre el «estado de pecado» de quien genera aleatoriedad con aritmética.
· **Capítulos:** 9. · **Nivel:** ◆◆ · **Fiabilidad:** ★★★ · **Primaria.**

**Hastings, W. K. — *Monte Carlo sampling methods using Markov chains and their
applications***, Biometrika 57 (1970), 97–109. `hastings1970mc`
· **Aporta:** la generalización que convierte a Metropolis en una herramienta
estadística general. Es donde nace el MCMC moderno.
· **Capítulos:** 9. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Primaria.**

**Fermi, Pasta, Ulam — *Studies of Nonlinear Problems*, Los Alamos report
LA-1940** (1955). `fermi1955fpu`
· **Aporta:** el primer experimento numérico de la historia que produjo un
resultado inesperado que nadie sabía explicar. El origen de la ciencia
computacional como forma de descubrimiento, no de cálculo.
· **Capítulos:** 16, Interludio 8. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★
· **Primaria.**
· **Cautela de crédito:** el código lo escribió Mary Tsingou, mencionada en los
agradecimientos y no en la autoría. Véase Dauxois (2008).

### 1.3 Probabilidad, estadística e información

**Bayes, Thomas (comunicado por Richard Price) — *An Essay towards solving a
Problem in the Doctrine of Chances***, Phil. Trans. R. Soc. 53 (1763), 370–418.
`bayes1763essay`
· **Aporta:** el texto fundacional. Vale la pena leerlo para comprobar hasta qué
punto el «teorema de Bayes» tal como se enseña no está ahí en esa forma, y
cuánto puso Price.
· **Capítulos:** 3, 5. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Primaria.**

**Laplace, Pierre-Simon — *Théorie analytique des probabilités*** (1812) y
***Essai philosophique sur les probabilités*** (1814). `laplace1812theorie`
· **Aporta:** el *Essai* es el mejor ensayo divulgativo sobre probabilidad jamás
escrito, y contiene la formulación de la probabilidad como sentido común
cuantificado. La *Théorie* contiene el teorema central del límite en su forma
temprana.
· **Capítulos:** 3, 5. · **Nivel:** ◆◆ (Essai) / ◆◆◆◆ (Théorie)
· **Fiabilidad:** ★★★ · **Primaria.**

**Gauss, Carl Friedrich — *Theoria Motus Corporum Coelestium*** (1809).
`gauss1809theoria`
· **Aporta:** mínimos cuadrados justificados a partir de una hipótesis sobre la
distribución de errores, en el contexto real que los motivó: recuperar Ceres.
· **Capítulos:** 5, 11. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Primaria.**

**Legendre, Adrien-Marie — *Nouvelles méthodes pour la détermination des orbites
des comètes*** (1805). `legendre1805nouvelles`
· **Aporta:** la primera publicación del método de mínimos cuadrados. La disputa
de prioridad con Gauss es un caso de estudio sobre cómo se asigna el crédito.
· **Capítulos:** 5. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Primaria.**

**von Bortkiewicz, Ladislaus — *Das Gesetz der kleinen Zahlen*** (1898).
`bortkiewicz1898gesetz`
· **Aporta:** el ejemplo canónico de la distribución de Poisson con datos reales:
muertes por coz de caballo en el ejército prusiano. Datos aburridos, ley
profunda.
· **Capítulos:** 4. · **Nivel:** ◆◆ · **Fiabilidad:** ★★★ · **Primaria.**

**Rutherford, Geiger, Bateman — *The probability variations in the distribution
of α particles***, Phil. Mag. 20 (1910), 698–707. `rutherford1910probability`
· **Aporta:** el ajuste de Poisson a 2608 intervalos de conteo real. La tabla
sigue siendo el mejor ejercicio de introducción al conteo.
· **Capítulos:** 4, II.4. · **Nivel:** ◆◆ · **Fiabilidad:** ★★★ · **Primaria.**

**Kolmogórov, Andréi — *Grundbegriffe der Wahrscheinlichkeitsrechnung*** (1933;
trad. *Foundations of the Theory of Probability*, 1956). `kolmogorov1933grundbegriffe`
· **Aporta:** la axiomatización. Se cita para explicar **por qué hizo falta**,
no para demostrar nada: el libro no usa teoría de la medida.
· **Capítulos:** 3. · **Nivel:** ◆◆◆◆ · **Fiabilidad:** ★★★ · **Primaria.**

**Shannon, Claude — *A Mathematical Theory of Communication***, Bell System
Technical Journal 27 (1948), 379–423 y 623–656. `shannon1948mathematical`
· **Aporta:** entropía como medida de incertidumbre. Sorprendentemente legible.
Es también donde se acredita a J. W. Tukey la palabra «bit».
· **Capítulos:** 3, 12. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Primaria.**

**Erlang, Agner Krarup — *The Theory of Probabilities and Telephone
Conversations***, Nyt Tidsskrift for Matematik B 20 (1909), 33–39.
`erlang1909theory`
· **Aporta:** teoría de colas naciendo de un problema de ingeniería concreto: la
centralita de Copenhague. El ejemplo perfecto de que la ingeniería crea teoría.
· **Capítulos:** 4, II.12. · **Nivel:** ◆◆ · **Fiabilidad:** ★★★ · **Primaria.**

### 1.4 Dinámica, ondas y computación numérica

**Fourier, Joseph — *Théorie analytique de la chaleur*** (1822). `fourier1822theorie`
· **Aporta:** el libro donde se defiende que cualquier función puede
representarse mediante ondas, con la ecuación del calor como motivación física.
· **Capítulos:** 12, 6, Interludio 2. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★
· **Primaria.**

**Taylor, Geoffrey Ingram — *The Formation of a Blast Wave by a Very Intense
Explosion. I. Theoretical Discussion* y *II. The Atomic Explosion of 1945***,
Proc. R. Soc. A 201 (1950), 159–174 y 175–186. `taylor1950blast1`, `taylor1950blast2`
· **Aporta:** la deducción de $R \propto (Et^2/\rho)^{1/5}$ y su aplicación a las
fotografías desclasificadas de Trinity. La parte II es el análisis dimensional
más famoso de la historia.
· **Capítulos:** 2. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Primaria.**
· **Cautela:** la versión popular («Taylor dedujo un secreto militar de una
revista y el gobierno se enfadó») exagera. El trabajo teórico es de 1941, la
publicación de 1950, y Sedov y von Neumann llegaron a lo mismo de forma
independiente.

**Lorenz, Edward — *Deterministic Nonperiodic Flow***, J. Atmos. Sci. 20 (1963),
130–141. `lorenz1963deterministic`
· **Aporta:** el sistema de Lorenz y la primera descripción clara de la
sensibilidad a condiciones iniciales en un modelo determinista.
· **Capítulos:** 7, II.10. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Primaria.**

**Lorenz, Edward — *The Essence of Chaos*** (1993). `lorenz1993essence`
· **Aporta:** el relato del propio Lorenz sobre el episodio del redondeo
(0,506127 → 0,506) en el LGP-30, y sobre el origen de la metáfora de la mariposa,
que no es suya en la forma en que se cuenta.
· **Capítulos:** 7, 15, Interludio 6. · **Nivel:** ◆ · **Fiabilidad:** ★★
· **Primaria (memoria).**

**Runge, Carl — *Über die numerische Auflösung von Differentialgleichungen***,
Math. Ann. 46 (1895), 167–178; **Kutta, Wilhelm** — *Beitrag zur näherungsweisen
Integration totaler Differentialgleichungen*, Z. Math. Phys. 46 (1901), 435–453.
`runge1895ueber`, `kutta1901beitrag`
· **Aporta:** el origen de los métodos que todo el mundo usa sin saber de dónde
salen. Ambos nacen de necesidades de cálculo concretas.
· **Capítulos:** 8. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Primaria.**

**Richardson, Lewis Fry — *Weather Prediction by Numerical Process*** (1922).
`richardson1922weather`
· **Aporta:** el primer intento serio de predecir el tiempo resolviendo
ecuaciones a mano, y su «fábrica de predicción» de 64 000 computistas humanos. Un
fracaso instructivo: el método era correcto, faltaban la máquina y el filtrado de
las ondas rápidas.
· **Capítulos:** 8, II.10, 16. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★
· **Primaria.**

**Kirkpatrick, Gelatt, Vecchi — *Optimization by Simulated Annealing***, Science
220 (1983), 671–680. `kirkpatrick1983optimization`
· **Aporta:** la traducción explícita de la física estadística a un algoritmo de
optimización. La analogía temperatura–exploración está ahí, argumentada.
· **Capítulos:** 10. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Primaria.**
· **Nota:** Václav Černý llegó a la misma idea de forma independiente
(publicada en J. Optim. Theory Appl. 45, 1985; preprint de 1982).

**Turing, Alan — *The Chemical Basis of Morphogenesis***, Phil. Trans. R. Soc. B
237 (1952), 37–72. `turing1952chemical`
· **Aporta:** cómo un sistema que difunde y reacciona puede generar patrones
espontáneos. Un modelo mínimo que predijo fenómenos confirmados décadas después.
· **Capítulos:** II.9. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Primaria.**

**Cooley, James; Tukey, John — *An Algorithm for the Machine Calculation of
Complex Fourier Series***, Math. Comp. 19 (1965), 297–301. `cooley1965algorithm`
· **Aporta:** la FFT. Tres páginas que cambiaron la ciencia experimental.
· **Capítulos:** 12. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Primaria.**
· **Nota histórica:** Gauss tenía el algoritmo en 1805, en un manuscrito no
publicado. Véase Heideman, Johnson y Burrus (1984).

**Box, George — *Science and Statistics***, JASA 71 (1976), 791–799.
`box1976science`
· **Aporta:** la fuente real de «todos los modelos son falsos». La formulación
completa —«all models are wrong but some are useful»— aparece en Box (1979).
· **Capítulos:** 14, 15. · **Nivel:** ◆◆ · **Fiabilidad:** ★★★ · **Primaria.**

---

## 2. Referencias técnicas

### 2.1 Estimación y modelado

**Mahajan, Sanjoy — *Street-Fighting Mathematics*** (MIT Press, 2010, libre) y
***The Art of Insight in Science and Engineering*** (MIT Press, 2014, libre).
`mahajan2010street`, `mahajan2014art`
· **Aporta:** el mejor tratamiento sistemático de la estimación y la
aproximación que existe. Análisis dimensional, casos extremos, agrupamiento,
razonamiento pictórico.
· **Capítulos:** 1, 2, 13. · **Nivel:** ◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**
· **Es la referencia complementaria número uno del libro.**

**Weinstein, Lawrence; Adam, John — *Guesstimation*** (Princeton UP, 2008) y
**Weinstein — *Guesstimation 2.0*** (2012). `weinstein2008guesstimation`
· **Aporta:** un banco de problemas de Fermi con soluciones razonadas. Útil como
cantera de ejercicios.
· **Capítulos:** 1. · **Nivel:** ◆ · **Fiabilidad:** ★★ · **Secundaria.**

**Poundstone, William — *How Would You Move Mount Fuji?*** (2003).
`poundstone2003fuji`
· **Aporta:** contexto sobre problemas de estimación en entrevistas técnicas.
· **Capítulos:** 1 (mención breve). · **Nivel:** ◆ · **Fiabilidad:** ★
· **Secundaria.**
· **Cautela:** es periodismo, no historia. Se cita sólo donde es pertinente y sin
apoyar en él ninguna afirmación histórica.

**Barenblatt, Grigory — *Scaling, Self-Similarity, and Intermediate
Asymptotics*** (Cambridge UP, 1996) y ***Scaling*** (2003). `barenblatt1996scaling`
· **Aporta:** el tratamiento serio del análisis dimensional, incluida la
distinción entre autosemejanza de primera y segunda especie, que es donde el
teorema π deja de bastar.
· **Capítulos:** 2, 13. · **Nivel:** ◆◆◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**Bridgman, Percy — *Dimensional Analysis*** (Yale UP, 1922). `bridgman1922dimensional`
· **Aporta:** la exposición clásica, todavía la más clara sobre qué significa
realmente una dimensión.
· **Capítulos:** 2. · **Nivel:** ◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

### 2.2 Probabilidad y estadística

**Blitzstein, Joseph; Hwang, Jessica — *Introduction to Probability***
(2.ª ed., CRC, 2019). `blitzstein2019introduction`
· **Aporta:** la mejor construcción moderna de intuición probabilística; las
«historias» detrás de cada distribución encajan exactamente con el enfoque del
capítulo 3.
· **Capítulos:** 3, 4. · **Nivel:** ◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**MacKay, David — *Information Theory, Inference, and Learning Algorithms***
(Cambridge UP, 2003; libre en línea). `mackay2003information`
· **Aporta:** la unificación de inferencia, información y modelado. Los capítulos
de Monte Carlo (29–30) y de navaja de Occam bayesiana (28) son directamente
material de los capítulos 9 y 15.
· **Capítulos:** 3, 9, 15. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**Jaynes, Edwin T. — *Probability Theory: The Logic of Science*** (Cambridge UP,
2003). `jaynes2003probability`
· **Aporta:** la defensa más potente de la probabilidad como lógica extendida, y
el principio de máxima entropía.
· **Capítulos:** 3, 5. · **Nivel:** ◆◆◆◆ · **Fiabilidad:** ★★
· **Secundaria.**
· **Cautela obligatoria:** es un libro militante. Jaynes despacha posiciones
frecuentistas con desdén y presenta como resueltas cuestiones que siguen
discutiéndose. Se lee por la potencia de su argumento, no como árbitro neutral, y
el libro lo dice cada vez que lo cita.

**Gelman, Carlin, Stern, Dunson, Vehtari, Rubin — *Bayesian Data Analysis***
(3.ª ed., CRC, 2013). `gelman2013bayesian`
· **Aporta:** la práctica real de la inferencia bayesiana, incluyendo diagnóstico
de MCMC y comprobación predictiva posterior.
· **Capítulos:** 5, 9, 15. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**Stigler, Stephen — *The History of Statistics: The Measurement of Uncertainty
before 1900*** (Harvard UP, 1986). `stigler1986history`
· **Aporta:** la historia rigurosa de mínimos cuadrados, Gauss frente a Legendre,
y el nacimiento de la teoría de errores. Es la fuente que impide repetir mitos.
· **Capítulos:** 5, 3. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**Hacking, Ian — *The Emergence of Probability*** (Cambridge UP, 1975).
`hacking1975emergence`
· **Aporta:** por qué la probabilidad tardó tanto en aparecer, y la dualidad
azar/creencia desde el primer día.
· **Capítulos:** 3. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**Bevington, Philip; Robinson, D. Keith — *Data Reduction and Error Analysis for
the Physical Sciences*** (3.ª ed., McGraw-Hill, 2003). `bevington2003data`
· **Aporta:** el manual práctico de propagación, ajuste y χ².
· **Capítulos:** 5. · **Nivel:** ◆◆ · **Fiabilidad:** ★★ · **Secundaria.**
· **Cautela:** notación anticuada en algunos puntos; el vocabulario normativo
actual es el del GUM.

**JCGM 100:2008 — *Guide to the Expression of Uncertainty in Measurement (GUM)***
y **JCGM 101:2008 (Suplemento 1, método de Monte Carlo)**. `jcgm2008gum`
· **Aporta:** el vocabulario correcto: incertidumbre tipo A y tipo B,
incertidumbre expandida, factor de cobertura. Es el estándar en metrología e
industria.
· **Capítulos:** 5, 15. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★
· **Primaria (normativa).**

**Taylor, John R. — *An Introduction to Error Analysis*** (2.ª ed., 1997).
`taylorjr1997error`
· **Aporta:** la introducción más clara y la más usada en laboratorios de grado.
· **Capítulos:** 5. · **Nivel:** ◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**Cowan, Glen — *Statistical Data Analysis*** (Oxford, 1998). `cowan1998statistical`
· **Aporta:** el tratamiento de significancia, límites y conteo con fondo, con
rigor de física de partículas y sin retórica.
· **Capítulos:** 4, II.4. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

### 2.3 Dinámica y sistemas

**Strogatz, Steven — *Nonlinear Dynamics and Chaos*** (2.ª ed., Westview, 2015).
`strogatz2015nonlinear`
· **Aporta:** la mejor introducción existente a sistemas dinámicos. Retratos de
fase, bifurcaciones, caos, con ejemplos de biología, ingeniería y física.
· **Capítulos:** 6, 7, II.5, II.10, II.11. · **Nivel:** ◆◆
· **Fiabilidad:** ★★★ · **Secundaria.** **Referencia complementaria número dos.**

**Guckenheimer, John; Holmes, Philip — *Nonlinear Oscillations, Dynamical
Systems, and Bifurcations of Vector Fields*** (Springer, 1983).
`guckenheimer1983nonlinear`
· **Aporta:** el siguiente escalón, cuando Strogatz se queda corto.
· **Capítulos:** 7. · **Nivel:** ◆◆◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**Murray, James D. — *Mathematical Biology I & II*** (3.ª ed., Springer, 2002).
`murray2002mathematical`
· **Aporta:** el catálogo de modelos biológicos bien hechos: epidemias, patrones,
poblaciones. Antídoto contra el sesgo hacia la física.
· **Capítulos:** 6, 7, II.5, II.9, II.13. · **Nivel:** ◆◆◆
· **Fiabilidad:** ★★★ · **Secundaria.**

**Kermack, William; McKendrick, Anderson — *A Contribution to the Mathematical
Theory of Epidemics***, Proc. R. Soc. A 115 (1927), 700–721.
`kermack1927contribution`
· **Aporta:** el modelo SIR y el teorema del umbral, en el original.
· **Capítulos:** II.5. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Primaria.**

### 2.4 Métodos numéricos y computación

**Press, Teukolsky, Vetterling, Flannery — *Numerical Recipes*** (3.ª ed.,
Cambridge UP, 2007). `press2007numerical`
· **Aporta:** cobertura enciclopédica con explicaciones honestas de cuándo un
método falla. La prosa es excelente.
· **Capítulos:** 8, 9, 10, 11, 12. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★
· **Secundaria.**
· **Cautelas académicas necesarias:** algunas implementaciones han sido
criticadas por su calidad numérica frente a las bibliotecas estándar (LAPACK,
FFTW), y su licencia es restrictiva. Se recomienda **leerlo y no copiarlo**.

**Trefethen, Lloyd N.; Bau, David — *Numerical Linear Algebra*** (SIAM, 1997).
`trefethen1997numerical`
· **Aporta:** el mejor libro sobre condicionamiento, estabilidad y SVD. Cuarenta
clases, cada una de una idea.
· **Capítulos:** 11. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**Strang, Gilbert — *Introduction to Linear Algebra*** (5.ª ed., 2016) y
***Linear Algebra and Learning from Data*** (2019). `strang2016introduction`
· **Aporta:** la intuición geométrica de los cuatro subespacios y de la SVD.
· **Capítulos:** 11. · **Nivel:** ◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**Hairer, Nørsett, Wanner — *Solving Ordinary Differential Equations I y II***
(Springer, 1993/1996) y **Hairer, Lubich, Wanner — *Geometric Numerical
Integration*** (2006). `hairer1993solving`, `hairer2006geometric`
· **Aporta:** la referencia definitiva sobre integradores, rigidez e
integradores simplécticos.
· **Capítulos:** 8, II.6. · **Nivel:** ◆◆◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**LeVeque, Randall — *Finite Difference Methods for Ordinary and Partial
Differential Equations*** (SIAM, 2007). `leveque2007finite`
· **Aporta:** estabilidad, consistencia, convergencia y la condición CFL,
explicadas de verdad.
· **Capítulos:** 8, II.7. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**Goldberg, David — *What Every Computer Scientist Should Know About
Floating-Point Arithmetic***, ACM Computing Surveys 23 (1991), 5–48.
`goldberg1991floating`
· **Aporta:** la referencia sobre coma flotante y cancelación catastrófica.
· **Capítulos:** 8. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**Higham, Nicholas — *Accuracy and Stability of Numerical Algorithms***
(2.ª ed., SIAM, 2002). `higham2002accuracy`
· **Aporta:** el tratado sobre errores de redondeo. Se consulta, no se lee.
· **Capítulos:** 8, 11. · **Nivel:** ◆◆◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**Bender, Carl; Orszag, Steven — *Advanced Mathematical Methods for Scientists
and Engineers*** (McGraw-Hill, 1978). `bender1978advanced`
· **Aporta:** perturbaciones, balance dominante, capas límite, WKB. El capítulo
sobre balance dominante es exactamente lo que el capítulo 13 necesita.
· **Capítulos:** 13. · **Nivel:** ◆◆◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**Robert, Christian; Casella, George — *Monte Carlo Statistical Methods***
(2.ª ed., Springer, 2004). `robert2004monte`
· **Aporta:** el tratamiento riguroso de MCMC, convergencia y reducción de
varianza.
· **Capítulos:** 9. · **Nivel:** ◆◆◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**Newman, Mark; Barkema, Gerard — *Monte Carlo Methods in Statistical Physics***
(Oxford, 1999). `newman1999monte`
· **Aporta:** Ising, Metropolis, algoritmos de cúmulos, con física dentro.
· **Capítulos:** 9, II.9. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**Nocedal, Jorge; Wright, Stephen — *Numerical Optimization*** (2.ª ed.,
Springer, 2006). `nocedal2006numerical`
· **Aporta:** la referencia estándar de optimización continua.
· **Capítulos:** 10. · **Nivel:** ◆◆◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**Boyd, Stephen; Vandenberghe, Lieven — *Convex Optimization*** (Cambridge UP,
2004; libre). `boyd2004convex`
· **Aporta:** dónde está exactamente la frontera entre lo fácil y lo difícil.
· **Capítulos:** 10. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**Oppenheim, Alan; Schafer, Ronald — *Discrete-Time Signal Processing***
(3.ª ed., Pearson, 2009). `oppenheim2009discrete`
· **Aporta:** muestreo, aliasing, filtros y estimación espectral con rigor.
· **Capítulos:** 12, II.14. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**Bracewell, Ronald — *The Fourier Transform and Its Applications*** (3.ª ed.,
McGraw-Hill, 2000). `bracewell2000fourier`
· **Aporta:** el diccionario visual de transformadas y la mejor exposición de la
convolución.
· **Capítulos:** 12. · **Nivel:** ◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**Downey, Allen — *Think Stats*, *Think Bayes*, *Think DSP*, *Think
Complexity*** (O'Reilly, libres). `downey2014thinkstats`
· **Aporta:** el enfoque «aprender por simulación» en Python, muy alineado con el
espíritu del libro. Especialmente útil *Think DSP* para el capítulo 12.
· **Capítulos:** 3, 5, 12, 16. · **Nivel:** ◆ · **Fiabilidad:** ★★
· **Secundaria.**

**Wilson et al. — *Best Practices for Scientific Computing*** (PLoS Biology 12,
2014) y ***Good Enough Practices in Scientific Computing*** (PLoS Comp. Biol. 13,
2017). `wilson2014best`
· **Aporta:** higiene mínima de código y datos científicos, con evidencia.
· **Capítulos:** 16. · **Nivel:** ◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**Roache, Patrick — *Verification and Validation in Computational Science and
Engineering*** (Hermosa, 1998). `roache1998verification`
· **Aporta:** el vocabulario V&V y el método de las soluciones manufacturadas.
· **Capítulos:** 15, 16, III.7. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★
· **Secundaria.**

**Saltelli et al. — *Global Sensitivity Analysis: The Primer*** (Wiley, 2008).
`saltelli2008global`
· **Aporta:** índices de Sobol y por qué la sensibilidad local engaña en modelos
no lineales.
· **Capítulos:** 15. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

---

## 3. Historia de la ciencia

**Segrè, Gino; Hoerlin, Bettina — *The Pope of Physics: Enrico Fermi and the
Birth of the Atomic Age*** (Henry Holt, 2016). `segre2016pope`
· **Aporta:** la biografía moderna y documentada de Fermi.
· **Capítulos:** 1, 4, Interludio 1. · **Nivel:** ◆ · **Fiabilidad:** ★★★
· **Secundaria.**

**Fermi, Laura — *Atoms in the Family*** (1954). `fermilaura1954atoms`
· **Aporta:** la mirada doméstica sobre cómo trabajaba Fermi.
· **Capítulos:** 1. · **Nivel:** ◆ · **Fiabilidad:** ★★ · **Primaria (memoria).**

**Eckhardt, Roger — *Stan Ulam, John von Neumann, and the Monte Carlo Method***,
Los Alamos Science 15 (1987), 131–137. `eckhardt1987stan`
· **Aporta:** la reconstrucción documentada del origen del método, con las cartas
de von Neumann a Richtmyer de 1947.
· **Capítulos:** 9, Interludio 3. · **Nivel:** ◆◆ · **Fiabilidad:** ★★★
· **Secundaria.**

**Gubernatis, James — *Marshall Rosenbluth and the Metropolis algorithm***,
Physics of Plasmas 12 (2005), 057303. `gubernatis2005marshall`
· **Aporta:** la entrevista de 2003 en la que Marshall Rosenbluth explica quién
hizo qué en el paper de 1953: que el trabajo lo hicieron él y Arianna Rosenbluth,
que Teller aportó una sugerencia clave y que Metropolis aportó tiempo de máquina.
Es la fuente que impide repetir la versión cómoda.
· **Capítulos:** 9, Interludio 4. · **Nivel:** ◆◆ · **Fiabilidad:** ★★★
· **Secundaria (basada en testimonio primario).**

**Dauxois, Thierry — *Fermi, Pasta, Ulam, and a mysterious lady***, Physics Today
61 (2008), 55–57. `dauxois2008fermi`
· **Aporta:** la recuperación del papel de Mary Tsingou como programadora del
experimento FPU.
· **Capítulos:** 16, Interludio 8. · **Nivel:** ◆ · **Fiabilidad:** ★★★
· **Secundaria.**

**Aspray, William — *John von Neumann and the Origins of Modern Computing***
(MIT Press, 1990). `aspray1990john`
· **Aporta:** la historia rigurosa de la contribución de von Neumann a la
computación, sin las exageraciones habituales.
· **Capítulos:** 8, 9, Interludio 5. · **Nivel:** ◆◆ · **Fiabilidad:** ★★★
· **Secundaria.**

**Dyson, George — *Turing's Cathedral*** (Pantheon, 2012). `dyson2012turing`
· **Aporta:** el ambiente del IAS y la construcción de la máquina.
· **Capítulos:** Interludio 5. · **Nivel:** ◆ · **Fiabilidad:** ★★
· **Secundaria.** · **Cautela:** narrativo; algunas atribuciones técnicas se han
discutido.

**Grattan-Guinness, Ivor — *Joseph Fourier 1768–1830*** (MIT Press, 1972).
`grattanguinness1972joseph`
· **Aporta:** la historia documentada de la memoria de 1807, de las objeciones de
Lagrange y de por qué tardó quince años en publicarse.
· **Capítulos:** 12, Interludio 2. · **Nivel:** ◆◆◆ · **Fiabilidad:** ★★★
· **Secundaria.**

**Gleick, James — *Chaos: Making a New Science*** (1987) y ***Genius: The Life
and Science of Richard Feynman*** (1992). `gleick1987chaos`, `gleick1992genius`
· **Aporta:** narrativa excelente y una vía de entrada.
· **Capítulos:** 7, Interludio 6. · **Nivel:** ◆ · **Fiabilidad:** ★★
· **Secundaria.** · **Cautela:** *Chaos* comprime cronologías y dramatiza; se usa
para el ambiente, nunca para fechas ni atribuciones.

**Jones, Eric — *«Where is everybody?» An account of Fermi's question***, Los
Alamos report LA-10311-MS (1985). `jones1985where`
· **Aporta:** la reconstrucción, a partir de cartas de Konopinski, Teller y York,
de la conversación de 1950. El propio informe deja claro que la frase exacta es
una reconstrucción.
· **Capítulos:** 1. · **Nivel:** ◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**Badger, Lee — *Lazzarini's Lucky Approximation of π***, Mathematics Magazine 67
(1994), 83–91. `badger1994lazzarini`
· **Aporta:** el análisis que demuestra que el experimento de la aguja de
Lazzarini (1901), que dio π = 355/113, es estadísticamente inverosímil sin
detención selectiva. Caso perfecto para los capítulos 9 y 15.
· **Capítulos:** 9, 15. · **Nivel:** ◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**Brody, Rip, Vinten-Johansen, Paneth, Rachman — *Map-making and myth-making in
Broad Street: the London cholera epidemic, 1854***, The Lancet 356 (2000),
64–68. `brody2000map`
· **Aporta:** el desmontaje del mito del mapa de John Snow: el mapa ilustró una
conclusión ya alcanzada por otros medios.
· **Capítulos:** 15, III.10. · **Nivel:** ◆◆ · **Fiabilidad:** ★★★
· **Secundaria.**

**Burchfield, Joe — *Lord Kelvin and the Age of the Earth*** (1975).
`burchfield1975lord`
· **Aporta:** por qué Kelvin se equivocó y por qué su error no fue de cálculo
sino de física ausente.
· **Capítulos:** 15. · **Nivel:** ◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

**Klein, Martin; et al. — sobre el asunto de los rayos N**, y **Wood, Robert W. —
*The n-Rays*, Nature 70 (1904), 530–531**. `wood1904nrays`
· **Aporta:** la nota de una página con la que Wood desmontó un programa de
investigación entero. Ejemplo canónico del experimento decisivo.
· **Capítulos:** 15. · **Nivel:** ◆ · **Fiabilidad:** ★★★ · **Primaria.**

**Heideman, Johnson, Burrus — *Gauss and the history of the Fast Fourier
Transform***, IEEE ASSP Magazine 1 (1984), 14–21. `heideman1984gauss`
· **Aporta:** la prueba de que Gauss tenía la FFT en 1805.
· **Capítulos:** 12. · **Nivel:** ◆◆ · **Fiabilidad:** ★★★ · **Secundaria.**

---

## 4. Lecturas opcionales, por si el gusanillo pica

* **Polya, George — *How to Solve It*** (1945). El abuelo de toda la Parte III.
  `polya1945how`
* **Hamming, Richard — *The Art of Doing Science and Engineering*** (1997) y su
  charla *You and Your Research* (1986). Sobre cómo elegir en qué trabajar.
  `hamming1997art`
* **Wigner, Eugene — *The Unreasonable Effectiveness of Mathematics in the
  Natural Sciences***, Comm. Pure Appl. Math. 13 (1960). `wigner1960unreasonable`
* **Anderson, Philip — *More Is Different***, Science 177 (1972). Por qué cada
  escala necesita sus propias leyes. `anderson1972more`
* **Schelling, Thomas — *Micromotives and Macrobehavior*** (1978). Modelado en
  ciencias sociales hecho con honestidad. `schelling1978micromotives`
* **West, Geoffrey — *Scale*** (2017). Leyes de escala en biología y ciudades;
  entusiasta y discutido, léase con la crítica al lado. `west2017scale`
* **Tufte, Edward — *The Visual Display of Quantitative Information*** (2.ª ed.,
  2001). `tufte2001visual`
* **Kahneman, Daniel — *Thinking, Fast and Slow*** (2011), capítulos sobre
  anclaje y exceso de confianza, directamente aplicables a la estimación.
  `kahneman2011thinking`
* **Ziman, John — *Reliable Knowledge*** (1978). Qué hace fiable a un
  conocimiento. `ziman1978reliable`

---

## 5. Fuentes de datos para los ejercicios

Modelar sin datos es gimnasia sin peso. Fuentes abiertas usadas en el libro:

| Fuente | Qué tiene | Se usa en |
|---|---|---|
| NIST Fundamental Physical Constants (CODATA) | constantes con su incertidumbre | 1, 5 |
| NOAA / AEMET open data | series meteorológicas | 5, 7, II.10 |
| Our World in Data | series socioeconómicas y epidemiológicas | II.5, II.13 |
| NASA JPL Horizons | efemérides planetarias de precisión | II.6 |
| PhysioNet | señales biomédicas reales | 12, II.14 |
| UCI ML Repository | conjuntos tabulares clásicos | 5, 15 |
| Zenodo / Dryad | datos de papers publicados | III.11 |
| Datos.gob.es | tráfico, energía, demografía en España | II.11, II.12 |

Norma del libro: **cuando un ejercicio usa datos reales, se indica la fuente, la
fecha de descarga y las unidades.** Un dato sin procedencia no es un dato.
