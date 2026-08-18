# Arquitectura del libro

*Documento de diseño. Corresponde a la fase 1 del encargo: decidir la estructura antes de escribir una línea.*

> Documento de diseño. No forma parte del texto que leerá un lector final:
> es el plano del edificio. Se conserva en el repositorio porque un libro que
> enseña a construir modelos debería enseñar también su propio modelo.

---

## 1. Título provisional

**La servilleta y el ordenador**

*Un entrenamiento en estimación, modelado y experimentación computacional*

El título nombra los dos polos entre los que oscila todo el libro. La
servilleta es Fermi dejando caer papelitos en el desierto de Jornada del
Muerto para estimar la energía de Trinity con dos cifras y un metro de
desplazamiento. El ordenador es von Neumann y Ulam convirtiendo el azar en un
método de cálculo. Casi todo el oficio de modelar vive en la tensión entre
esas dos herramientas: **la que cabe en un bolsillo y la que ejecuta 10¹²
operaciones por segundo**. Quien sólo domina una de las dos es peligroso de
maneras distintas.

Alternativas consideradas y por qué se descartaron:

| Título | Por qué se descartó |
|---|---|
| *Pensar con modelos* | Correcto pero anodino; suena a manual de gestión. |
| *Antes de calcular* | Buen lema, mal título: sólo cubre la mitad del ciclo. |
| *El laboratorio de papel* | Bonito, pero deja fuera la computación, que es media obra. |
| *Estimar, modelar, simular, dudar* | Es la tesis, no el título. Se usa como subtítulo interno de la Parte III. |
| *Cómo pensaban Fermi, Feynman, von Neumann y Ulam* | Prohibido por diseño: convertiría el libro en hagiografía. |

**Título corto para cabeceras y diapositivas:** *La servilleta y el ordenador*.

---

## 2. Tesis del libro

> La capacidad de resolver problemas científicos difíciles no es un almacén de
> técnicas, sino **un ciclo entrenable**: estimar antes de calcular, modelar
> antes de simular y dudar antes de creer. Las técnicas son el vocabulario; el
> ciclo es la gramática. Este libro entrena la gramática.

Tres corolarios que se defienden a lo largo de todo el texto:

1. **Una respuesta aproximadamente correcta a la pregunta correcta vale más que
   una respuesta exacta a la pregunta equivocada.** Casi todo el fracaso
   técnico real es de la segunda clase.
2. **El ordenador no simula la realidad.** Ejecuta un modelo discretizado que
   hemos construido nosotros, con nuestros supuestos y nuestros errores dentro.
   Confundir ambas cosas es la fuente principal de resultados convincentes y
   falsos.
3. **Las mismas cinco o seis estructuras matemáticas reaparecen en todas las
   disciplinas.** Un físico que lo sabe puede entrar en epidemiología, en
   logística o en biología de poblaciones en semanas, no en años. Esa
   transferencia es el activo que el libro intenta construir.

---

## 3. Objetivos pedagógicos

Redactados como capacidades observables, no como temario. Al terminar el libro
el lector debe ser capaz de:

**Estimación**

* O1. Producir en menos de diez minutos, sin buscar datos, una estimación de
  orden de magnitud de una cantidad física, biológica, económica o de
  ingeniería, con un intervalo de confianza declarado.
* O2. Descomponer un problema aparentemente imposible en factores estimables e
  identificar cuál de ellos domina el error.
* O3. Diagnosticar por qué una estimación falló, distinguiendo error de dato,
  error de estructura y error conceptual.

**Modelado**

* O4. Pasar de un fenómeno descrito en lenguaje natural a un modelo mínimo con
  variables, supuestos y ecuaciones explícitos.
* O5. Adimensionalizar un modelo, identificar sus grupos π y predecir su
  comportamiento en los límites de esos grupos antes de resolverlo.
* O6. Justificar cada término que conserva y cada término que desprecia, con un
  argumento cuantitativo de escalas.

**Computación**

* O7. Elegir un método numérico por sus propiedades (orden, estabilidad, coste,
  conservación) y no por costumbre, y demostrar empíricamente su orden de
  convergencia.
* O8. Diseñar una simulación Monte Carlo con estimador, varianza y barra de
  error, y saber cuándo el muestreo directo no basta.
* O9. Distinguir un resultado físico de un artefacto numérico mediante pruebas
  de convergencia, conservación e invariancia.

**Inferencia y crítica**

* O10. Propagar incertidumbre a través de un modelo y comunicar el resultado sin
  falsa precisión.
* O11. Detectar sobreajuste, parámetros no identificables y extrapolación
  ilegítima en un modelo propio o ajeno.
* O12. Diseñar la prueba que **falsaría** su propio modelo, y ejecutarla.

**Explicación**

* O13. Explicar cualquier resultado del libro sin escribir ecuaciones, a alguien
  que sabe cálculo pero desconoce el fenómeno.
* O14. Leer un paper de un campo desconocido y extraer en una hora su modelo,
  sus supuestos y su punto débil.

**Meta**

* O15. Usar herramientas de IA aumentando su capacidad de ejecución sin ceder la
  formulación del problema, y saber decir en qué punto exacto del ciclo la ha
  usado.

---

## 4. Perfil del lector

Se escribe para una persona concreta:

* Graduada en Física. Ha visto cálculo, álgebra lineal, EDO, mecánica,
  electromagnetismo, termodinámica, física estadística, cuántica, métodos
  numéricos, estadística y programación.
* **Las herramientas están oxidadas, no ausentes.** Esto cambia todo el diseño:
  no hace falta enseñar qué es una derivada, hace falta devolverle el
  significado físico a la derivada.
* Programa en Python con soltura. Trabaja profesionalmente con software, IA y
  ML. Tiene experiencia previa con simulación y Monte Carlo.
* Aprende experimentando: cambiando parámetros y mirando qué pasa.
* Quiere recuperar deliberadamente la capacidad de formular problemas sin
  delegarla de inmediato en un modelo de lenguaje.

Consecuencias de diseño, explícitas:

1. **No se define nada elemental.** Se recuerda con una *Caja de herramientas
   matemática* de media página cuando el problema lo exige, y se sigue.
2. **La densidad matemática puede ser alta**, pero cada paso se deriva. Nada de
   «se puede demostrar que».
3. **El código nunca es el protagonista.** Aparece cuando responde una pregunta
   que no se puede responder a mano, y es corto y legible.
4. **No se usa IA/ML como ejemplo por defecto**, precisamente porque es el
   terreno cómodo del lector. Aparece cuando es la mejor herramienta y no antes.
5. **El tono asume un adulto.** Se puede decir «esto es feo», «esto es un
   truco», «aquí la literatura miente un poco».

---

## 5. Filosofía pedagógica

### 5.1 El orden canónico

Se prohíbe el patrón *definición → teorema → fórmula → ejercicios*. Se sustituye
por:

```text
fenómeno → pregunta → estimación → variables → supuestos → modelo mínimo
   → matemáticas → análisis de escalas → solución aproximada → computación
   → validación → incertidumbre → interpretación → límites → nueva pregunta
```

Este diagrama aparece impreso en el interior de la cubierta y se repite, con la
etapa activa resaltada, al principio de cada capítulo de la Parte II. La
repetición es intencionada: se trata de instalar un hábito, no de informar.

### 5.2 Las cuatro capas

Todo concepto importante se presenta en cuatro capas. **Si falta una, el
concepto está incompleto** y el capítulo no se da por terminado:

| Capa | Pregunta | Forma típica en el texto |
|---|---|---|
| Intuición | ¿Qué significa? | Analogía física, límite extremo, caso degenerado |
| Matemática | ¿Cómo se expresa? | Derivación completa, sin saltos |
| Computación | ¿Cómo se calcula? | 15–40 líneas de Python ejecutables |
| Realidad | ¿Dónde aparece? | Dos o tres ejemplos de disciplinas distintas |

### 5.3 Matemáticas *just-in-time*

No hay un bloque inicial de fundamentos. Las matemáticas entran cuando un
problema las reclama, en cajas breves:

* Taylor entra en el capítulo 13, cuando hay que justificar una linealización
  concreta.
* Los autovalores entran en el capítulo 7, cuando hay que decidir si un punto
  fijo es estable, y se completan en el 11.
* La transformada de Fourier entra en el 12, después de que el capítulo 6 haya
  dejado una ecuación del calor sin resolver a propósito.

Esto crea deuda técnica deliberada: **el libro promete cosas y luego las paga.**
La lista de promesas y pagos está en `metadatos/dependencias.md`.

### 5.4 Contra el «ejecutar y mirar la gráfica»

Toda simulación importante va precedida de una predicción escrita y seguida de
una explicación. El patrón es:

```text
¿qué esperamos? → simular → ¿ocurrió? → ¿por qué? → ¿qué predice ahora el modelo?
```

Los ejercicios de la categoría *Detective* existen exactamente para castigar la
lectura pasiva de gráficas: se entregan resultados numéricos plausibles y
falsos, y hay que localizar el error.

### 5.5 Criterio de calidad de una sección

Una sección se conserva si produce **al menos una** de estas cinco cosas:

1. una intuición nueva;
2. una herramienta reutilizable;
3. una conexión sorprendente entre campos;
4. una habilidad practicable;
5. una pregunta genuina.

Si sólo transmite información consultable en Wikipedia, se reescribe o se
elimina. Este criterio se aplica en la revisión de cada capítulo y queda
registrado en su cabecera.

---

## 6. Estructura completa

```text
PRELIMINARES
  Cómo usar este libro · El ciclo · El cuaderno del modelador · Plan de entrenamiento

PARTE I — EL INSTRUMENTAL DEL MODELADOR            16 capítulos
  Las herramientas, cada una nacida de un problema que la necesitaba.

PARTE II — PROBLEMAS QUE CONECTAN LAS HERRAMIENTAS 14 capítulos
  Fenómenos, no disciplinas. Cada capítulo usa media Parte I a la vez.

PARTE III — EL ARTE DE RESOLVER PROBLEMAS          13 capítulos
  Metodología explícita. El manual de campo.

INTERLUDIOS                                         8, intercalados
APÉNDICES                                           7
```

### PARTE I — EL INSTRUMENTAL DEL MODELADOR

**Capítulo 1 — Órdenes de magnitud y estimaciones de Fermi**
1.1 Un problema que no se puede resolver · 1.2 Potencias de diez como sistema
nervioso · 1.3 La anatomía de una estimación: descomponer, acotar, multiplicar ·
1.4 Por qué los errores se cancelan (y cuándo no) · 1.5 Cotas superior e
inferior: la técnica del sándwich · 1.6 Incertidumbre logarítmica y la regla del
√n · 1.7 Análisis de sensibilidad de servilleta: ¿qué factor domina el error? ·
1.8 Trinity: la estimación de Fermi, documentada · 1.9 Cuándo una estimación es
mejor que un cálculo exacto · 1.10 Diez estimaciones progresivas
*Herramientas nuevas:* logaritmos como cambio de unidad mental, propagación
multiplicativa de errores, cotas.

**Capítulo 2 — Análisis dimensional y similitud**
2.1 Una ecuación no puede ser dimensionalmente falsa · 2.2 Dimensiones frente a
unidades · 2.3 El teorema π de Buckingham, con demostración informal ·
2.4 Recetario: cómo elegir las variables repetidas · 2.5 Adimensionalizar una
ecuación: el paso que más veces salva un problema · 2.6 Números adimensionales
como preguntas (Re, Pe, Fr, Bi, Ma, Da) · 2.7 Leyes de escala y semejanza:
maquetas, animales, edificios · 2.8 La onda de choque: Taylor, Sedov y von
Neumann, quién hizo qué · 2.9 Los límites del método: cuándo π no basta
*Herramientas nuevas:* matriz dimensional, grupos π, escalas características.

**Capítulo 3 — Probabilidad como modelo del desconocimiento y del azar**
3.1 Dos cosas distintas llamadas «probabilidad» · 3.2 Espacio muestral: el
modelo antes de la fórmula · 3.3 Variables aleatorias como funciones ·
3.4 Esperanza y varianza como primeros momentos de la ignorancia ·
3.5 Independencia: el supuesto que más se viola en silencio ·
3.6 Condicionar es actualizar: Bayes como contabilidad de la evidencia ·
3.7 El zoo mínimo: Bernoulli, binomial, Poisson, exponencial, normal, uniforme,
potencial · 3.8 De dónde sale cada distribución (mecanismo, no fórmula) ·
3.9 Ley de los grandes números: qué promete y qué no · 3.10 Teorema central del
límite: por qué es cierto y dónde falla (Cauchy, colas pesadas) ·
3.11 Kolmogórov y por qué hizo falta axiomatizar
*Herramientas nuevas:* simulación como definición operativa, funciones
generadoras (ligero).

**Capítulo 4 — Contar cosas: Poisson, ruido y fluctuaciones**
4.1 Contar es medir · 4.2 El proceso de Poisson desde tres derivaciones
distintas · 4.3 σ = √N y por qué gobierna medio mundo experimental ·
4.4 Señal, fondo y significancia · 4.5 Tiempos entre sucesos y la paradoja del
autobús · 4.6 Sobredispersión: cuando la varianza excede la media, y qué
significa · 4.7 Estimar una tasa con pocos sucesos · 4.8 Bortkiewicz, los
caballos prusianos y Rutherford–Geiger · 4.9 Aplicaciones: fotones, llamadas,
mutaciones, accidentes, colas, servidores
*Herramientas nuevas:* verosimilitud de Poisson, intervalos con pocos sucesos.

**Capítulo 5 — Incertidumbre y medida**
5.1 Error no es incertidumbre · 5.2 Sistemático frente a aleatorio: el sesgo no
se reduce promediando · 5.3 Propagación: fórmula lineal, Monte Carlo y cuándo la
primera miente · 5.4 Mínimos cuadrados como respuesta a un problema real de
astronomía · 5.5 Gauss, Legendre, Ceres y una disputa de prioridad ·
5.6 Ajuste: χ², matriz de covarianza, correlación entre parámetros ·
5.7 Residuos: la gráfica que más veces salva un ajuste · 5.8 Qué significa
«compatible con los datos» · 5.9 Cifras significativas y la falsa precisión
*Herramientas nuevas:* covarianza, χ², bootstrap.

**Capítulo 6 — Ecuaciones diferenciales como lenguaje del cambio**
6.1 dx/dt = f(x,t) leído en voz alta · 6.2 Estado: qué hay que saber hoy para
predecir mañana · 6.3 Los cuatro modelos que explican medio mundo: relajación,
crecimiento, oscilación, saturación · 6.4 Escalas temporales y el tiempo
característico · 6.5 Adimensionalizar una EDO (pago de la deuda del cap. 2) ·
6.6 Equilibrio y estabilidad, versión unidimensional · 6.7 Sistemas acoplados:
depredador–presa, dos cuerpos, dos compartimentos · 6.8 Conservación como
primera integral · 6.9 Euler resolviendo problemas físicos con ecuaciones
*Herramientas nuevas:* separación de variables, factor integrante, retrato de
fases 1D.

**Capítulo 7 — Sistemas dinámicos**
7.1 Espacio de fases: pensar con geometría en vez de con fórmulas ·
7.2 Puntos fijos y su clasificación · 7.3 Linealización y jacobiano ·
7.4 Autovalores como tasas y frecuencias (deuda con el cap. 11) ·
7.5 Ciclos límite y oscilaciones autosostenidas · 7.6 Bifurcaciones: silla-nodo,
transcrítica, horquilla, Hopf · 7.7 El mapa logístico y la cascada de duplicación
de periodo · 7.8 Caos: sensibilidad, exponente de Lyapunov, horizonte de
predicción · 7.9 Lorenz, 1961: qué ocurrió realmente con aquella simulación ·
7.10 El sistema de Lorenz como laboratorio
*Herramientas nuevas:* jacobiano, diagrama de bifurcación, exponente de Lyapunov.

**Capítulo 8 — Qué hace realmente un ordenador cuando resuelve una ecuación**
8.1 El ordenador no resuelve: aproxima · 8.2 Coma flotante: el error que llevas
puesto · 8.3 Cancelación catastrófica y un ejemplo que aterra ·
8.4 Discretización: de la derivada al cociente incremental · 8.5 Euler explícito
y su error global · 8.6 Orden de un método y cómo medirlo empíricamente ·
8.7 Runge–Kutta: de dónde salen los coeficientes · 8.8 Estabilidad, rigidez y
por qué un paso «pequeño» a veces explota · 8.9 Implícito frente a explícito ·
8.10 Integración, raíces, interpolación y diferencias finitas · 8.11 Coste:
cuándo el algoritmo importa más que el ordenador
*Herramientas nuevas:* análisis de orden, región de estabilidad, condicionamiento.

**Capítulo 9 — Monte Carlo: calcular mediante azar**
9.1 ¿Cómo puede el azar calcular algo determinista? · 9.2 La aguja de Buffon y
la primera integral estocástica de la historia · 9.3 El estimador Monte Carlo y
su varianza · 9.4 ε ∝ 1/√N: la buena y la mala noticia · 9.5 La maldición y la
bendición de la dimensionalidad · 9.6 Números pseudoaleatorios: von Neumann, el
estado de pecado y los generadores modernos · 9.7 Muestreo por transformada
inversa y por rechazo · 9.8 Reducción de varianza: importancia, antitéticas,
variables de control · 9.9 Cuando no se puede muestrear directamente: cadenas de
Markov · 9.10 Metropolis y Metropolis–Hastings, derivados desde el balance
detallado · 9.11 Diagnóstico de MCMC: burn-in, autocorrelación, tamaño efectivo ·
9.12 Los Álamos, el MANIAC y quién hizo qué, con fuentes
*Herramientas nuevas:* estimadores insesgados, cadenas de Markov, balance
detallado.

**Capítulo 10 — Optimización y paisajes**
10.1 Casi todo es una optimización disfrazada · 10.2 El paisaje como objeto
geométrico · 10.3 Gradiente: la dirección de máxima pendiente y sus problemas ·
10.4 Newton y cuasi-Newton: usar la curvatura · 10.5 Convexidad: la frontera
entre fácil y difícil · 10.6 Mínimos locales y estrategias de escape ·
10.7 Recocido simulado: física estadística convertida en algoritmo ·
10.8 Temperatura, energía y la conexión Boltzmann–probabilidad ·
10.9 Optimización sin gradiente: Nelder–Mead, evolutivos, y cuándo merecen la
pena · 10.10 Ajuste de modelos como optimización, y por qué el paisaje del
ajuste dice si el parámetro es identificable
*Herramientas nuevas:* condiciones de optimalidad, hessiano, recocido.

**Capítulo 11 — Álgebra lineal como lenguaje de modelos**
11.1 Un vector es un estado, una matriz es una regla · 11.2 Cambio de base:
elegir el punto de vista correcto · 11.3 Autovalores como modos naturales del
sistema · 11.4 Exponencial de una matriz y solución de sistemas lineales ·
11.5 Sistemas lineales: cuándo la solución existe y cuándo es una fantasía ·
11.6 Condicionamiento: la matriz que amplifica tus errores · 11.7 SVD: la
descomposición que explica el ajuste, el PCA y la compresión a la vez ·
11.8 Aplicaciones: estabilidad, difusión discreta, redes, cadenas de Markov,
mínimos cuadrados
*Herramientas nuevas:* SVD, número de condición, exp(At).

**Capítulo 12 — Fourier: ver el mundo en frecuencias**
12.1 Una señal es una suma de cosas que sabemos resolver · 12.2 La idea de
Fourier y por qué escandalizó a Lagrange · 12.3 Series, transformada y el paso
al continuo · 12.4 El espectro como respuesta a una pregunta física ·
12.5 Convolución y el teorema que la hace útil · 12.6 Muestreo, Nyquist y
aliasing: el error que se ve · 12.7 Filtrado, resolución y el compromiso
tiempo–frecuencia · 12.8 Resolver la ecuación del calor en dos líneas (pago de
la deuda del cap. 6) · 12.9 FFT: por qué N log N cambió la ciencia experimental ·
12.10 Aplicaciones: sonido, imagen, espectroscopía, cristalografía, señales
*Herramientas nuevas:* DFT/FFT, convolución, ventanas.

**Capítulo 13 — Escalas, aproximaciones y perturbaciones**
13.1 La habilidad central: decidir qué se puede ignorar · 13.2 Taylor como
herramienta de decisión, no como fórmula · 13.3 Parámetros pequeños y en qué
unidades son pequeños · 13.4 Linealización y su radio de validez ·
13.5 Perturbaciones regulares · 13.6 Perturbaciones singulares y capas límite:
cuando el término pequeño manda · 13.7 Notación asintótica y el arte de escribir
«≈» honestamente · 13.8 Límites extremos como test de un modelo
*Herramientas nuevas:* desarrollo asintótico, balance dominante.

**Capítulo 14 — De un fenómeno a un modelo**
14.1 El protocolo completo, paso a paso · 14.2 Caso guiado: una taza de café se
enfría (observación → modelo → experimento real → ajuste → crítica) ·
14.3 Caso guiado: la cola del supermercado · 14.4 Caso guiado: un rumor se
propaga · 14.5 Qué hacer cuando el modelo mínimo falla · 14.6 Cuándo añadir
complejidad y cuándo negarse
*Herramientas nuevas:* ninguna. Es un capítulo de integración deliberada.

**Capítulo 15 — Cuando el modelo miente**
15.1 Sobreajuste: el modelo que aprende el ruido · 15.2 Parámetros no
identificables y modelos equivalentes · 15.3 Mala especificación: el ajuste
bueno del modelo falso · 15.4 Correlación, causalidad y confusores ·
15.5 Extrapolación: el pecado favorito · 15.6 Artefactos numéricos disfrazados
de física · 15.7 Sesgo del experimentador: Millikan, los rayos N, la deriva de
las constantes · 15.8 Casos: cold fusion, OPERA y el cable suelto, Lazzarini y
su aguja demasiado buena, Kelvin y la edad de la Tierra · 15.9 Cómo diseñar la
prueba que mataría tu modelo
*Herramientas nuevas:* validación cruzada, análisis de identifiabilidad,
perfiles de verosimilitud.

**Capítulo 16 — Computación como laboratorio**
16.1 El ordenador como instrumento, no como calculadora · 16.2 Anatomía de un
experimento computacional · 16.3 Reproducibilidad: semillas, versiones,
cuadernos · 16.4 Barridos de parámetros y adimensionalización previa ·
16.5 Convergencia, invariancias y otras pruebas de cordura · 16.6 Visualizar
para descubrir frente a visualizar para comunicar · 16.7 Fermi, Pasta, Ulam y
Tsingou: el primer experimento numérico que sorprendió a todos ·
16.8 Higiene mínima de código científico
*Herramientas nuevas:* diseño de barridos, pruebas de convergencia, cuaderno
reproducible.

### PARTE II — PROBLEMAS QUE CONECTAN LAS HERRAMIENTAS

Cada capítulo abre con un fenómeno observable y declara, en una tabla de
cabecera, **qué herramientas de la Parte I va a usar**. El lector debería sentir
que las herramientas no eran temas: eran piezas.

| # | Fenómeno | Herramientas que convoca |
|---|---|---|
| II.1 | ¿Por qué cae una gota de lluvia como cae? | 1, 2, 6, 8, 13 |
| II.2 | ¿Cuánto tarda algo en enfriarse? | 1, 5, 6, 14 |
| II.3 | ¿Por qué hay campanas de Gauss por todas partes? | 3, 9, 13 |
| II.4 | ¿Cuánto podemos fiarnos de una detección? | 4, 5, 15 |
| II.5 | ¿Por qué una epidemia puede explotar? | 2, 6, 7, 10 |
| II.6 | ¿Por qué algunas órbitas son estables? | 6, 8, 11, 13 |
| II.7 | ¿Cómo se propaga una sustancia? | 3, 8, 9, 12 |
| II.8 | ¿Cómo encontramos el camino más probable? | 3, 9, 10 |
| II.9 | ¿Cómo puede surgir orden del azar? | 9, 10, 16 |
| II.10 | ¿Cuándo deja de ser posible predecir? | 7, 8, 15 |
| II.11 | ¿Por qué hay atascos donde no hay obstáculo? | 6, 7, 13 |
| II.12 | ¿Cuánto hay que esperar en una cola? | 3, 4, 9 |
| II.13 | ¿Por qué no hay mamíferos del tamaño de un edificio? | 1, 2, 13 |
| II.14 | ¿Cómo se ve lo que no se puede ver? | 5, 11, 12, 15 |

### PARTE III — EL ARTE DE RESOLVER PROBLEMAS

Capítulos cortos, densos y operativos. Son el manual de campo que se consulta
cuando uno está atascado de verdad. Cada uno termina con una **lista de
comprobación de una página**, pensada para imprimirse.

III.1 Cómo empezar cuando no sabes qué hacer · III.2 Cómo elegir variables ·
III.3 Cómo construir un modelo mínimo · III.4 Cómo encontrar la escala correcta ·
III.5 Cómo detectar qué término domina · III.6 Cómo decidir qué aproximación
usar · III.7 Cómo comprobar un resultado · III.8 Cómo usar simulaciones sin
engañarte · III.9 Cómo diseñar experimentos computacionales · III.10 Cómo
comunicar una explicación científica · III.11 Cómo leer un paper con mentalidad
de modelador · III.12 Cómo entrar en un campo científico nuevo · III.13 Cómo
usar IA sin externalizar tu pensamiento.

### INTERLUDIOS

Entre 2 y 5 páginas. Narrativos, documentados, sin ejercicios. Cada uno se
coloca inmediatamente después del capítulo cuya herramienta ilumina.

| # | Título | Va después de | Idea que ilumina |
|---|---|---|---|
| 1 | Fermi y los papelitos | Cap. 1 | Medir con lo que hay en el bolsillo |
| 2 | Fourier contra la intuición matemática de su época | Cap. 12 | Una idea correcta puede ser rechazada por los mejores |
| 3 | Ulam jugando al solitario | Cap. 9 | El fracaso de la combinatoria como origen de un método |
| 4 | Metropolis, y una idea que terminó apareciendo por todas partes | Cap. 9 | Autoría colectiva y crédito mal repartido |
| 5 | Cuando von Neumann empezó a pensar en ordenadores | Cap. 8 | La computación nace de un problema físico concreto |
| 6 | El ordenador que cambió el tiempo de Lorenz | Cap. 7 | Un error de redondeo como descubrimiento |
| 7 | Feynman, el hielo y la junta tórica | Cap. 15 | El experimento mínimo decisivo |
| 8 | La señora del MANIAC | Cap. 16 | Quién programaba realmente los descubrimientos |

### APÉNDICES

A. Caja de herramientas matemática (todas las cajas del libro, recopiladas) ·
B. Recetario de Python científico para modeladores · C. Números que conviene
saberse de memoria · D. Soluciones razonadas con pistas graduadas ·
E. Bibliografía comentada · F. Plan de entrenamiento de 12 semanas ·
G. Plantillas del cuaderno del modelador.

---

## 7. Herramientas matemáticas: mapa de dependencias

```text
Órdenes de magnitud ─┬─> Análisis dimensional ─┬─> Escalas y perturbaciones
                     │                          └─> Leyes de escala (II.13)
                     └─> Estimación de errores ──> Incertidumbre
Probabilidad ─┬─> Poisson y conteo ──> Inferencia de tasas (II.4)
              ├─> Ley de grandes números ──> Monte Carlo
              ├─> TCL ──> Gaussianas por todas partes (II.3)
              └─> Cadenas de Markov ──> MCMC ──> Orden desde el azar (II.9)
Cálculo ─┬─> EDO ─┬─> Sistemas dinámicos ──> Caos (II.10)
         │        └─> Métodos numéricos ──> Integradores simplécticos (II.6)
         ├─> Taylor ──> Perturbaciones ──> Balance dominante
         └─> Fourier ──> Convolución ──> Señales e imágenes (II.14)
Álgebra lineal ─┬─> Autovalores ──> Estabilidad
                ├─> SVD ──> PCA, ajuste, condicionamiento
                └─> Sistemas lineales ──> Diferencias finitas
Optimización ─┬─> Gradiente, Newton
              └─> Recocido ── (Boltzmann) ── Física estadística
```

La regla de oro: **ninguna herramienta se introduce más de un capítulo antes de
su primer uso real.**

---

## 8. Herramientas computacionales

Pila deliberadamente pequeña:

| Herramienta | Uso | Se evita |
|---|---|---|
| Python ≥3.11 | todo | azúcar sintáctico exótico |
| NumPy | vectorización, álgebra lineal | bucles cuando el vector es obvio |
| SciPy | `integrate`, `optimize`, `stats`, `signal`, `linalg` | reimplementar lo estándar... salvo cuando reimplementarlo *es* la lección |
| Matplotlib | todas las figuras | seaborn, plotly, estilos por defecto |
| pandas | sólo cuando hay datos tabulares reales | usarlo para arrays numéricos |
| Jupyter | cuadernos por capítulo | notebooks como código de producción |

Reglas de código, que se aplican sin excepción:

1. Cada script es **autocontenido y ejecutable**: `python fig_algo.py` funciona.
2. Menos de 60 líneas salvo justificación.
3. Cero clases salvo que el estado lo exija de verdad.
4. Semilla fija y explícita en todo lo estocástico.
5. `typing` sólo cuando aclara la firma, nunca por ritual.
6. **Se implementa a mano el método que se está aprendiendo** (Euler, RK4,
   Metropolis) y sólo después se compara con SciPy. La comparación es la
   lección.

---

## 9. Personajes históricos: quién aparece, dónde y para qué

Nadie aparece por prestigio. Cada figura entra porque ilustra **una manera de
pensar** que el lector debe adquirir.

| Persona | Capítulos | Qué modela intelectualmente |
|---|---|---|
| Enrico Fermi | 1, 4, 16, Int. 1 | Reducir lo imposible a lo estimable; medir con lo que hay |
| Richard Feynman | 1, 6, 13, 15, Int. 7 | Entender desde primeros principios; explicar; el experimento mínimo |
| John von Neumann | 2, 8, 9, Int. 5 | Formalizar y computar; cruzar disciplinas |
| Stanisław Ulam | 9, 16, Int. 3 | Jugar con el cálculo hasta que aparezca el patrón |
| Nicholas Metropolis | 9, 10, Int. 4 | El algoritmo como trabajo colectivo |
| Marshall y Arianna Rosenbluth | 9, Int. 4 | Quién hizo el trabajo y quién se llevó el nombre |
| Mary Tsingou | 16, Int. 8 | La programación como parte del descubrimiento |
| Edward Lorenz | 7, 15, Int. 6 | Tomarse en serio un resultado raro |
| Geoffrey I. Taylor | 2 | Sacar física de una fotografía y un cronómetro |
| Leonhard Euler | 6, 8 | Convertir un fenómeno en una ecuación resoluble |
| Isaac Newton | 6, 11 | Inventar las matemáticas que hacen falta |
| Joseph Fourier | 12, Int. 2 | Defender una idea correcta contra la autoridad |
| Carl F. Gauss | 5, 11 | Domar el error de medida |
| Adrien-Marie Legendre | 5 | Prioridad, disputa y trabajo simultáneo |
| Pierre-Simon Laplace | 3, 5 | La probabilidad como sentido común cuantificado |
| Thomas Bayes / Richard Price | 3 | Actualizar creencias con evidencia |
| Siméon Denis Poisson | 4 | Contar sucesos raros |
| Ladislaus Bortkiewicz | 4 | Datos aburridos, ley profunda |
| Andréi Kolmogórov | 3 | Por qué hace falta axiomatizar |
| Claude Shannon | 3, 12 | Cuantificar la información |
| Agner Krarup Erlang | 4, II.12 | Ingeniería que crea teoría |
| Carl Runge, Martin Kutta | 8 | Mejorar un método por necesidad práctica |
| George Box | 14, 15 | «Todos los modelos son falsos» |
| John Tukey | 5, 16, III.10 | Mirar los datos antes de modelarlos |
| Alan Turing | 8, II.9 | Qué puede y no puede calcularse; morfogénesis |
| James C. Maxwell | 2, 3 | Modelos mecánicos como andamio |
| Ludwig Boltzmann | 9, 10 | Del azar microscópico a la ley macroscópica |
| Lewis Fry Richardson | 8, II.10 | Predecir el tiempo antes de tener con qué |
| Florence Nightingale | III.10 | Un gráfico que cambió una política |
| John Snow | 15, III.10 | El mapa que se cuenta mal |
| Georges-Louis Leclerc, conde de Buffon | 9 | La primera integral por azar |
| Robert Millikan | 15 | Cómo un sesgo se hereda durante décadas |
| Robert W. Wood | 15 | Cómo se desmonta un resultado falso |
| Scott Kirkpatrick / Václav Černý | 10 | La misma idea, dos veces, en dos sitios |

Regla anti-culto explícita: **cada personaje recurrente aparece al menos una vez
equivocándose.** Fermi con la sobrestimación de la sección eficaz; Feynman con
sus propias trampas retóricas en las memorias; von Neumann con el middle-square;
Kelvin con la edad de la Tierra; Lorenz creyendo al principio que era un fallo
de la máquina.

---

## 10. Historias candidatas, con estado de verificación

Se clasifican en tres niveles. **El libro nunca presenta como hecho algo del
nivel C.**

**A — Documentado en fuente primaria**

| Historia | Fuente primaria | Cap. |
|---|---|---|
| Fermi estima Trinity con papelitos (≈10 kt frente a ≈21 kt reales) | Informe manuscrito de Fermi, *My Observations During the Explosion at Trinity on July 16, 1945* (LA archives; reproducido en varias recopilaciones) | 1, Int. 1 |
| Ulam concibe Monte Carlo jugando al solitario durante una convalecencia (1946) | Ulam, *Adventures of a Mathematician* (1976), cap. 7 | 9, Int. 3 |
| Metropolis explica el origen del nombre «Monte Carlo» | Metropolis, *The Beginning of the Monte Carlo Method*, Los Alamos Science 15 (1987) | 9, Int. 4 |
| von Neumann: «quien considera métodos aritméticos para producir dígitos aleatorios está, por supuesto, en estado de pecado» | von Neumann, *Various Techniques Used in Connection with Random Digits*, NBS AMS 12 (1951) | 9 |
| Lorenz reintroduce 0.506 en lugar de 0.506127 y obtiene otro tiempo | Lorenz, *The Essence of Chaos* (1993), cap. 1; Lorenz, *Deterministic Nonperiodic Flow*, J. Atmos. Sci. 20 (1963) | 7, Int. 6 |
| Feynman sumerge una junta tórica en agua helada ante la Comisión Rogers | Actas de la Rogers Commission, 11-feb-1986; apéndice F del informe | 15, Int. 7 |
| Taylor deduce la energía de la bomba a partir de la ley R ∝ (Et²/ρ)^{1/5} | Taylor, *The Formation of a Blast Wave by a Very Intense Explosion*, Proc. R. Soc. A 201 (1950), partes I y II | 2 |
| Bortkiewicz y las muertes por coz de caballo | von Bortkiewicz, *Das Gesetz der kleinen Zahlen* (1898) | 4 |
| Rutherford, Geiger y Bateman cuentan partículas α | Phil. Mag. 20 (1910) | 4 |
| El experimento FPU (con Tsingou como programadora) | Fermi, Pasta, Ulam, LA-1940 (1955); Dauxois, *Fermi, Pasta, Ulam and a mysterious lady*, Physics Today 61 (2008) | 16, Int. 8 |
| Gauss recupera Ceres; Legendre publica mínimos cuadrados antes | Gauss, *Theoria Motus* (1809); Legendre, *Nouvelles méthodes* (1805); Stigler, *The History of Statistics* (1986) | 5 |
| Fourier es criticado por Lagrange y su memoria de 1807 no se publica | Grattan-Guinness, *Joseph Fourier 1768–1830* (1972); Fourier, *Théorie analytique de la chaleur* (1822) | 12, Int. 2 |
| Feynman denuncia el sesgo heredado en la medida de la carga del electrón | Feynman, *Cargo Cult Science*, discurso en Caltech (1974) | 15 |
| Erlang modela la centralita de Copenhague | Erlang, *The Theory of Probabilities and Telephone Conversations* (1909) | 4, II.12 |
| Marshall Rosenbluth describe quién hizo qué en el paper de 1953 | Gubernatis, *Marshall Rosenbluth and the Metropolis algorithm*, Phys. Plasmas 12 (2005) | 9, Int. 4 |

**B — Bien documentado en fuentes secundarias fiables, con matices**

| Historia | Matiz que el libro debe declarar | Cap. |
|---|---|---|
| El «paradoja de Fermi» y la frase «¿dónde está todo el mundo?» | Reconstruida en 1985 por Eric Jones (LA-10311-MS) a partir de cartas de Konopinski, Teller y York; la frase exacta no está registrada en 1950 | 1 |
| Blondlot y los rayos N, desmontados por R. W. Wood | Bien documentado; la versión popular exagera el gesto teatral | 15 |
| El mapa de cólera de John Snow | El mapa ilustró una conclusión ya alcanzada, no la generó; véase Brody et al., Lancet 356 (2000) | 15, III.10 |
| Kelvin y la edad de la Tierra | Su error no fue de cálculo sino de física ausente (radiactividad y convección); Burchfield (1975) | 15 |
| Lazzarini y su aguja que da 355/113 | Casi con certeza detención selectiva; Badger, Math. Mag. 67 (1994) | 9, 15 |

**C — Folclore. Se cuenta *como* folclore o no se cuenta**

| Historia | Problema |
|---|---|
| «¿Cuántos afinadores de pianos hay en Chicago?» atribuido a Fermi | No hay fuente primaria de Fermi planteándolo. Está documentado que usaba problemas de estimación en clase; el enunciado concreto es atribución posterior. El libro lo usa **declarando** que la atribución es dudosa |
| Erdős rechazando Monty Hall hasta ver una simulación | Anecdótico, vía Hoffman (1998). Se cuenta como anécdota de segunda mano |
| Von Neumann resolviendo el problema de la mosca y los trenes «sumando la serie» | Circula en múltiples versiones incompatibles. Se usa sólo como chiste declarado |
| Feynman abriendo cajas fuertes en Los Álamos | Autobiográfico y sin corroboración externa; el libro lo usa para hablar de **cómo se cuentan las historias**, no como hecho |

---

## 11. Problemas transversales: la columna vertebral

Cinco problemas recorren el libro entero y se reencuentran con herramientas
nuevas. Es el recurso pedagógico más importante del diseño: demuestra que **una
misma realidad admite muchos niveles de descripción**, y que subir de nivel es
una decisión, no un progreso automático.

| Problema | 1ª vez | 2ª | 3ª | 4ª | 5ª |
|---|---|---|---|---|---|
| **La taza de café** | Cap. 1: estimar la potencia perdida | Cap. 5: ajustar datos reales con incertidumbre | Cap. 6: EDO de Newton y tiempo característico | Cap. 14: modelo mínimo y su crítica | II.2: convección, radiación y qué modelo basta |
| **La gota de lluvia** | Cap. 1: estimar velocidad terminal | Cap. 2: análisis dimensional del arrastre | Cap. 8: integrar la EDO no lineal | Cap. 13: régimen de Stokes frente a cuadrático | II.1: el capítulo completo |
| **El decaimiento radiactivo** | Cap. 3: distribución exponencial | Cap. 4: conteo de Poisson y √N | Cap. 6: EDO determinista y su relación con lo anterior | Cap. 9: simulación estocástica del mismo proceso | II.4: inferir la tasa con pocos sucesos |
| **La difusión** | Cap. 3: paseo aleatorio y ⟨x²⟩ = 2Dt | Cap. 8: diferencias finitas y estabilidad | Cap. 9: Monte Carlo de partículas | Cap. 12: solución por Fourier | II.7: el capítulo completo |
| **La epidemia** | Cap. 1: estimar contactos diarios | Cap. 6: modelo SIR | Cap. 7: umbral y bifurcación transcrítica | Cap. 10: ajustar R₀ a datos | II.5: el capítulo completo |

Cada reencuentro abre con una caja: *«Ya hemos estado aquí. Lo que entonces no
podíamos hacer era…»*.

---

## 12. Referencias fundamentales

Listado troncal; la bibliografía comentada completa está en
`bibliografia/bibliografia-comentada.md` (FASE 3).

**Primarias / de los propios protagonistas**

* Feynman, Leighton, Sands — *The Feynman Lectures on Physics* (1964).
* Feynman — *The Character of Physical Law* (1965); *QED* (1985);
  *Surely You're Joking, Mr. Feynman!* (1985), con las cautelas del §10.
* Ulam — *Adventures of a Mathematician* (1976).
* von Neumann — *Various Techniques Used in Connection with Random Digits*
  (1951); *The Computer and the Brain* (1958).
* Metropolis, Rosenbluth, Rosenbluth, Teller, Teller — *Equation of State
  Calculations by Fast Computing Machines*, J. Chem. Phys. 21 (1953).
* Metropolis, Ulam — *The Monte Carlo Method*, JASA 44 (1949).
* Lorenz — *Deterministic Nonperiodic Flow* (1963); *The Essence of Chaos* (1993).
* Taylor — *The Formation of a Blast Wave by a Very Intense Explosion* I y II
  (1950).
* Fourier — *Théorie analytique de la chaleur* (1822).
* Gauss — *Theoria Motus Corporum Coelestium* (1809).
* Shannon — *A Mathematical Theory of Communication* (1948).
* Kolmogórov — *Grundbegriffe der Wahrscheinlichkeitsrechnung* (1933).
* Kirkpatrick, Gelatt, Vecchi — *Optimization by Simulated Annealing* (1983).

**Técnicas de referencia**

* Strogatz — *Nonlinear Dynamics and Chaos* (2.ª ed., 2015).
* Blitzstein, Hwang — *Introduction to Probability* (2.ª ed., 2019).
* MacKay — *Information Theory, Inference, and Learning Algorithms* (2003).
* Jaynes — *Probability Theory: The Logic of Science* (2003), leído como lo que
  es: brillante y militante.
* Strang — *Introduction to Linear Algebra* / *Linear Algebra and Learning from
  Data* (2019).
* Trefethen, Bau — *Numerical Linear Algebra* (1997).
* Press et al. — *Numerical Recipes* (3.ª ed., 2007), con las cautelas de rigor.
* Barenblatt — *Scaling, Self-Similarity, and Intermediate Asymptotics* (1996).
* Bender, Orszag — *Advanced Mathematical Methods for Scientists and Engineers*
  (1978).
* Robert, Casella — *Monte Carlo Statistical Methods* (2004).
* Newman, Barkema — *Monte Carlo Methods in Statistical Physics* (1999).
* Gelman et al. — *Bayesian Data Analysis* (3.ª ed., 2013).
* Mahajan — *Street-Fighting Mathematics* (2010) y *The Art of Insight in
  Science and Engineering* (2014).
* Weinstein, Adam — *Guesstimation* (2008).
* Bevington, Robinson — *Data Reduction and Error Analysis* (2003);
  JCGM 100:2008 (*GUM*) para el vocabulario correcto de incertidumbre.

**Historia de la ciencia**

* Stigler — *The History of Statistics* (1986).
* Hacking — *The Emergence of Probability* (1975).
* Segrè, Hoerlin — *The Pope of Physics: Enrico Fermi* (2016).
* Gleick — *Genius* (1992) y *Chaos* (1987), con distancia crítica.
* Aspray — *John von Neumann and the Origins of Modern Computing* (1990).
* Eckhardt — *Stan Ulam, John von Neumann and the Monte Carlo Method*,
  Los Alamos Science 15 (1987).
* Grattan-Guinness — *Joseph Fourier 1768–1830* (1972).
* Dyson — *Turing's Cathedral* (2012), con cautelas.

---

## 13. Progresión de dificultad

Cuatro ejes que crecen de forma **desacoplada**, para que el lector nunca suba
por los cuatro a la vez:

| Eje | Parte I | Parte II | Parte III |
|---|---|---|---|
| Matemática | media→alta, siempre derivada | alta, pero reutilizando | baja: es metodología |
| Computacional | corto y guiado (20–40 líneas) | proyectos de 60–150 líneas | plantillas y protocolos |
| Autonomía | el problema viene formulado | el fenómeno viene, el modelo no | ni fenómeno ni modelo: sólo un contexto |
| Ambigüedad | ninguna | moderada (hay que elegir supuestos) | alta (hay que elegir la pregunta) |

Dentro de cada capítulo, los ejercicios siguen la escala:

```text
Calentamiento → Estimación → Modelado → Derivación → Computacional
    → Experimento → Detective → Mundo real → Feynman → Extensión
```

**Regla de progresión:** un capítulo de la Parte II sólo puede exigir
herramientas de capítulos de la Parte I ya publicados, y lo declara en su tabla
de cabecera. Los cruces están verificados en `metadatos/dependencias.md`.

---

## 14. Plan de entrenamiento (resumen)

Detalle completo en `00-preliminares/plan-de-entrenamiento.md` y apéndice F.

Sesión tipo, 45–90 min, 5–6 días por semana:

```text
10 min  estimación o problema, sin ayuda y sin buscar nada
20–30   lectura activa (con lápiz; el libro se subraya)
20–30   un problema o una simulación
5–10    explicación Feynman en voz alta o por escrito
        1 pregunta nueva al cuaderno
```

Ciclo largo: 12 semanas. Semanas 1–6, Parte I completa. Semanas 7–10, Parte II.
Semanas 11–12, Parte III y un proyecto propio de principio a fin.

La primera semana tiene un itinerario cerrado (día a día) porque el arranque es
donde se abandona.

---

## 15. Decisiones de diseño y por qué

**1. Tres partes y no dos.** El brief pedía herramientas y problemas. Falta el
puente: la metodología explícita. Sin la Parte III, el lector sabe usar
herramientas y ha visto problemas resueltos, pero no tiene un protocolo para el
problema número 43, que es nuevo. La Parte III es corta a propósito: es un
manual de campo, no un tratado.

**2. Los interludios no llevan ejercicios.** Un interludio con deberes deja de
ser un descanso y se convierte en capítulo. Su función es cambiar el ritmo
respiratorio del libro.

**3. Cada historia lleva nivel de verificación.** Es la decisión más importante
del diseño histórico. Un libro que enseña a dudar de los modelos no puede repetir
folclore como si fuera dato. Cuando una historia es dudosa, decirlo **es** la
lección.

**4. Los problemas transversales antes que la exhaustividad.** Es preferible ver
la taza de café cinco veces con cinco herramientas que ver cincuenta fenómenos
una vez. La transferencia se entrena volviendo, no acumulando.

**5. Un capítulo entero contra uno mismo (cap. 15).** La mayoría de los libros de
modelado enseñan a construir y no a desconfiar. La asimetría produce
modeladores peligrosos. El capítulo 15 y la Parte III existen para corregirla.

**6. La IA se trata en un capítulo, no en una nota al pie.** El lector la usa a
diario. Un libro de 2020 podía ignorarlo; uno de hoy que lo ignore es un libro
que finge. La postura es explícita: la IA es extraordinaria ejecutando y
peligrosa formulando, porque formular **es** la habilidad que entrenamos.

**7. Las figuras se generan con código versionado.** Cada figura del libro tiene
su script en `codigo/fig_*.py`. Nada de imágenes de origen desconocido. Es
coherente con lo que el libro predica sobre reproducibilidad.

**8. Español de España, tono adulto.** Se permite la ironía y se prohíbe el
entusiasmo decorativo. La frase «la ciencia es maravillosa» está vetada; el
asombro se produce enseñando algo que lo provoque.

---

## 16. Riesgos del proyecto y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Que se convierta en enciclopedia | Criterio de calidad del §5.5, aplicado sección a sección |
| Que la historia se vuelva decorativa | Toda historia debe responder «¿qué problema tenía esta persona?» |
| Que el código sustituya al pensamiento | Predicción escrita obligatoria antes de cada simulación |
| Que la Parte I se haga larga y el lector abandone | Interludios, problemas transversales y un itinerario cerrado de primera semana |
| Que las anécdotas sean falsas | Sistema A/B/C de verificación del §10 |
| Sesgo hacia la física | Cuota explícita: cada capítulo de la Parte I necesita ejemplos de ≥3 disciplinas |
| Que los ejercicios sean escolares | Diez categorías obligatorias, incluidas *Detective* y *Mundo real* |
