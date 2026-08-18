# Auditoría del temario

*Documento de diseño (fase 2): qué faltaba en el temario de partida y cómo se corrigió.*

> Ejercicio deliberado de hostilidad contra el propio plan. Se hace **antes** de
> escribir, porque después uno defiende lo que ya ha escrito.
> Método: recorrer los trece dominios que el libro promete cubrir y preguntar,
> para cada uno, *¿qué haría falta saber para modelar bien y no está?*

Cada hueco lleva: **severidad** (crítica / seria / menor), **dónde se corrige** y
**cuánto cuesta**.

---

## 1. Modelado

| Hueco detectado | Severidad | Corrección |
|---|---|---|
| No hay nada sobre **de dónde salen los datos**: buscar, limpiar, dudar de una fuente, unidades mal documentadas | Seria | Nueva sección **14.7 «El dato antes del modelo»** y checklist en III.2. Ejemplo real: dos fuentes que dan la conductividad térmica del aire con un 8 % de diferencia |
| Falta la distinción **verificación / validación** (V&V), que es el vocabulario estándar en ingeniería | Crítica | Nueva sección **15.10** y checklist en III.7. *Verificar* = resuelvo bien las ecuaciones; *validar* = son las ecuaciones correctas |
| No aparecen los **modelos de compartimentos** como patrón general (farmacocinética, epidemias, ecología, calor) | Seria | Sección **6.7bis** presentándolos como patrón transversal, con tres ejemplos de tres disciplinas |
| No hay **modelos basados en agentes** ni simulación de eventos discretos | Seria | Sección **16.4bis** (agentes) y **II.12.6** (eventos discretos con una cola simulada evento a evento) |
| Falta hablar de **modelos sustitutos** (surrogates, emuladores) cuando la simulación es cara | Menor | Caja en 16.5 y mención en III.9 |

## 2. Probabilidad

| Hueco | Severidad | Corrección |
|---|---|---|
| **Colas pesadas y leyes de potencias** casi ausentes. Es un hueco grave: media y varianza pueden no existir, y el TCL no aplica | Crítica | Nueva sección **3.12 «Cuando la campana no aparece»** (Cauchy, Pareto, Lévy) y refuerzo de **II.3**, que pasa a titularse *¿Por qué hay campanas por todas partes… y dónde no las hay?* |
| **Teoría del valor extremo** ausente. Diseñar un dique, un margen de seguridad o un límite de detección es preguntar por el máximo, no por la media | Seria | Sección **II.3.7** con Gumbel/Fréchet/Weibull a nivel intuitivo y un ejemplo de crecidas |
| **Entropía e información** no aparecen como herramienta de modelado | Seria | Sección **3.13** (entropía como medida de ignorancia) y **10.9bis** (máxima entropía como criterio para elegir distribución) |
| Los **procesos estocásticos en tiempo continuo** (Wiener, Langevin, Ornstein–Uhlenbeck) sólo aparecen implícitos en difusión | Seria | Sección **II.7.6** con ruido blanco frente a ruido coloreado y una integración de Euler–Maruyama |
| **Cópulas / dependencia no lineal** | Menor | Sólo mención en 15.4, con referencia. Fuera de alcance |

## 3. Estadística

| Hueco | Severidad | Corrección |
|---|---|---|
| No hay **contraste de hipótesis** explícito: p-valor, potencia, error tipo I/II, comparaciones múltiples | Crítica | Nueva sección **5.10** y aplicación completa en **II.4**. Incluye por qué el p-valor no es la probabilidad de que la hipótesis sea falsa |
| **Frecuentista frente a bayesiano** no se plantea como decisión de modelado | Crítica | Sección **5.11** con el mismo problema resuelto de las dos formas, y sin militancia |
| **Selección de modelos** (AIC, BIC, navaja de Occam bayesiana, validación cruzada) ausente | Crítica | Sección **15.11**, con la advertencia de que ninguno sustituye a pensar |
| **Bootstrap y remuestreo** sólo mencionados | Seria | Sección **5.8bis** con implementación de 12 líneas |
| **Diseño experimental** (aleatorización, bloqueo, factorial, tamaño muestral) ausente | Seria | Sección **III.9.4** y caja en 16.4: un barrido de parámetros *es* un diseño experimental |
| **Regresión robusta** y qué hacer con outliers | Menor | Caja en 5.7 |

## 4. Métodos numéricos

| Hueco | Severidad | Corrección |
|---|---|---|
| **EDP no están cubiertas de verdad**: sólo aparece difusión vía Fourier. Faltan diferencias finitas en el espacio, condición CFL, tipos (parabólica/hiperbólica/elíptica) | Crítica | Nueva sección **8.10bis «De la EDO a la EDP»**: esquema explícito para el calor, criterio CFL, y por qué la advección explícita centrada es inestable |
| **Integradores simplécticos** ausentes, siendo el ejemplo perfecto de «el método que respeta la física» | Crítica | Sección **8.7bis** y capítulo **II.6** completo (Verlet frente a RK4 en órbitas) |
| **Sistemas rígidos** y métodos implícitos poco tratados | Seria | Sección **8.8** ampliada, con un ejemplo de cinética química |
| **Álgebra lineal numérica**: sparse, métodos iterativos, precondicionamiento | Seria | Sección **11.9** breve, orientada a «cuándo tu matriz ya no cabe» |
| **Cuadratura adaptativa** y por qué `quad` a veces miente | Menor | Caja en 8.10 |
| **Diferenciación automática** frente a diferencias finitas | Menor | Caja en 10.3, útil para el lector por su contexto profesional |

## 5. Álgebra lineal

| Hueco | Severidad | Corrección |
|---|---|---|
| **Matrices no normales** y crecimiento transitorio: un sistema con todos los autovalores estables puede amplificar enormemente antes de decaer | Seria | Sección **11.3bis**, con un ejemplo de dos modos casi paralelos. Explica fallos reales de análisis de estabilidad |
| **Grafos y matrices de adyacencia** ausentes | Seria | Sección **11.8bis**: laplaciano de grafo, conectividad y difusión en redes; enlaza con II.5 |
| **Perron–Frobenius** y por qué toda cadena de Markov razonable converge | Menor | Caja en 11.3, cierra el círculo con MCMC |

## 6. Sistemas dinámicos

| Hueco | Severidad | Corrección |
|---|---|---|
| Sólo hay dinámica continua; faltan **mapas iterados** como objeto propio | Seria | Ya previsto en 7.7, se amplía: los mapas son más fáciles de simular y enseñan lo mismo |
| **Sistemas con retardo** (DDE) ausentes, siendo omnipresentes en biología, control y economía | Seria | Sección **7.11** breve: un retardo puede desestabilizar un sistema estable |
| **Excitabilidad** (FitzHugh–Nagumo) y **osciladores acoplados / sincronización** (Kuramoto) | Seria | Sección **7.5bis**; la sincronización es de los fenómenos más visuales del libro |
| **Estructuras de Turing** y formación de patrones | Menor | Sección en **II.9**, conecta con Turing 1952 |

## 7. Optimización

| Hueco | Severidad | Corrección |
|---|---|---|
| **Restricciones** ausentes: multiplicadores de Lagrange, KKT | Seria | Sección **10.5bis**. Casi todo problema real tiene restricciones |
| **Optimización estocástica moderna** (SGD y por qué el ruido ayuda) | Menor | Caja en 10.7, sin convertir el capítulo en ML |
| **Problemas inversos y regularización** (Tikhonov, L-curve) | Crítica | Sección **10.10bis** y uso completo en **II.14**. Es el puente entre optimización, incertidumbre y señales |
| **Optimización multiobjetivo** y frentes de Pareto | Menor | Caja en 10.10, con un ejemplo de ingeniería |

## 8. Monte Carlo

| Hueco | Severidad | Corrección |
|---|---|---|
| **Calidad de los generadores** tratada de pasada; faltan pruebas prácticas y el peligro de correlaciones en simulaciones grandes | Seria | Sección **9.6** ampliada, con el caso histórico de RANDU y un test visual en 3D |
| **Cuasi-Monte Carlo** (Sobol, Halton) y su convergencia ~1/N | Seria | Sección **9.4bis**: rompe la idea de que 1/√N es una ley de la naturaleza |
| **Diagnóstico de MCMC** insuficiente: hace falta R̂, tamaño efectivo, y ver una cadena que *parece* convergida y no lo está | Crítica | Sección **9.11** ampliada con un contraejemplo bimodal |
| **Gibbs, HMC** al menos nombrados con la intuición geométrica | Menor | Caja en 9.10 |
| **Bootstrap paramétrico** como Monte Carlo aplicado a incertidumbre | Menor | Enlace desde 5.8bis |

## 9. Incertidumbre

| Hueco | Severidad | Corrección |
|---|---|---|
| **Vocabulario GUM** (tipo A / tipo B, incertidumbre expandida, factor de cobertura) ausente | Seria | Caja normativa en **5.1**. Es el idioma de cualquier laboratorio o industria |
| **Análisis de sensibilidad global** (Sobol, Morris) frente al local | Crítica | Sección **15.12**: la derivada parcial en un punto no dice nada si el modelo es no lineal |
| **Propagación de incertidumbre estructural** (¿y si el modelo es otro?) | Seria | Sección **15.13**: promediado de modelos, y por qué la mayor incertidumbre casi nunca está en los parámetros |
| **Calibración frente a validación** con datos separados | Seria | Integrado en 15.10 |

## 10. Señales

| Hueco | Severidad | Corrección |
|---|---|---|
| **Análisis tiempo–frecuencia** (espectrograma, wavelets) ausente | Seria | Sección **12.7bis**, con el compromiso de Heisenberg como idea central |
| **Densidad espectral de potencia** y estimación (Welch), frente al módulo de la FFT a secas | Crítica | Sección **12.4bis**. Es el error práctico más común al analizar ruido |
| **Ruido 1/f y ruidos coloreados** | Seria | Enlazado con II.7.6 y con 4.6 |
| **Filtros digitales** (FIR/IIR, fase) y por qué un filtro puede desplazar tu señal | Menor | Caja en 12.7 |
| **Deconvolución** como problema mal condicionado | Crítica | Núcleo de **II.14**, conecta con 10.10bis y 11.6 |

## 11. Cálculo científico

| Hueco | Severidad | Corrección |
|---|---|---|
| **Rendimiento**: vectorización, complejidad, memoria, cuándo compilar | Seria | Sección **16.8bis**, sin convertirlo en un libro de HPC |
| **Reproducibilidad**: semillas, entornos, versiones, datos | Crítica | Sección **16.3**, ya prevista, se amplía con una plantilla de proyecto |
| **Pruebas de código científico**: soluciones manufacturadas, casos límite, conservación | Crítica | Sección **16.5bis**. Un test que comprueba `assert resultado > 0` no es un test |
| **Unidades en el código** y errores por conversión (Mars Climate Orbiter) | Menor | Caja en 2.1 |

## 12. Interpretación

| Hueco | Severidad | Corrección |
|---|---|---|
| **Causalidad** tratada sólo como advertencia; falta la herramienta mínima (confusor, colisionador, DAG) | Seria | Sección **15.4** ampliada con tres diagramas y un ejemplo donde controlar una variable *empeora* la estimación |
| **Paradoja de Simpson** y agregación | Menor | Caja en 15.4 |
| **Comunicación de incertidumbre** a no expertos | Seria | Sección **III.10.5** |

## 13. Diseño experimental

| Hueco | Severidad | Corrección |
|---|---|---|
| Ausente casi por completo, tanto en el laboratorio como en el ordenador | Crítica | **III.9** se reestructura: pregunta → factores → niveles → aleatorización → réplicas → análisis. Un barrido de simulación mal diseñado desperdicia CPU y confunde |
| **Muestreo del espacio de parámetros** (rejilla, aleatorio, hipercubo latino) | Seria | Sección **III.9.5**, con la comparación visual entre rejilla y LHS en dimensión alta |
| **Cuándo parar de simular** (criterio de precisión objetivo) | Seria | Caja en 9.3 y en III.9 |

---

## Correcciones estructurales al plan

Más allá de los huecos temáticos, la auditoría detecta cuatro problemas de
arquitectura:

**C1. Falta un capítulo puente entre las herramientas y los fenómenos.**
El salto del capítulo 13 (perturbaciones) al 14 (modelar un fenómeno) es
demasiado grande si el capítulo 14 no cambia de naturaleza. *Corrección:* el
capítulo 14 se convierte explícitamente en un **capítulo-taller** con tres casos
guiados de principio a fin, y no en un capítulo teórico más.

**C2. El capítulo 3 corre el riesgo de ser un repaso de probabilidad.**
Un lector con formación en física ya ha visto Bernoulli y binomial. *Corrección:*
el capítulo se reorienta a **de dónde sale cada distribución**: el mecanismo
generador. La pregunta rectora deja de ser «¿cuál es la fórmula?» y pasa a ser
«¿qué proceso físico produce esta distribución y cuál la destruiría?».

**C3. Hay una asimetría entre construir y desconfiar.**
Quince capítulos enseñan a construir y uno a dudar. *Corrección:* cada capítulo
de la Parte I incorpora obligatoriamente sus dos secciones *¿Qué estamos
suponiendo?* y *¿Cuándo falla?*, y al menos un ejercicio de la categoría
*Detective*. La desconfianza deja de estar concentrada en el capítulo 15 y pasa a
estar distribuida.

**C4. Riesgo de sesgo disciplinar hacia la física.**
Es el riesgo más probable dado el autor y el lector. *Corrección:* cuota
verificable — cada capítulo de la Parte I debe citar ejemplos de **al menos tres
disciplinas distintas**, y al menos uno no debe ser de física. La comprobación
se anota en la cabecera de cada capítulo y se audita al cierre.

---

## Lo que se decide dejar fuera, y por qué

Un temario también se define por lo que rechaza:

* **Mecánica cuántica y relatividad como temas.** Aparecen como ejemplos si
  aportan, nunca como materia. El libro es sobre el método, no sobre la física.
* **Machine learning como disciplina.** El lector ya vive ahí. Entra sólo cuando
  es la mejor herramienta para una pregunta concreta (regularización, validación
  cruzada, descenso estocástico) y siempre subordinado al modelado.
* **Computación de altas prestaciones, GPU, paralelismo.** Otro libro.
* **Teoría de la medida.** Kolmogórov se cuenta, no se demuestra.
* **Elementos finitos.** Se nombra la idea, se remite a la literatura. Un
  tratamiento honesto exigiría 150 páginas.
* **Análisis funcional para EDP.** Fuera. Las EDP entran por el lado del
  esquema numérico y de Fourier.
* **Cálculo simbólico.** Se menciona SymPy en el apéndice B como herramienta
  auxiliar. No estructura ningún capítulo.

---

## Resumen de impacto

| | Antes de la auditoría | Después |
|---|---|---|
| Capítulos Parte I | 16 | 16 (con 23 secciones nuevas) |
| Capítulos Parte II | 10 propuestos | 14 |
| Capítulos Parte III | 13 | 13 (III.9 reestructurado) |
| Huecos críticos detectados | — | 13 |
| Huecos serios | — | 22 |
| Huecos menores | — | 11 |

Los trece huecos críticos —EDP, integradores simplécticos, contraste de
hipótesis, frecuentista/bayesiano, selección de modelos, colas pesadas,
problemas inversos, diagnóstico de MCMC, sensibilidad global, PSD,
deconvolución, reproducibilidad, pruebas de código y diseño experimental— son
condición de publicación: sin ellos el libro entrenaría a alguien capaz de
construir modelos y no de defenderlos.
