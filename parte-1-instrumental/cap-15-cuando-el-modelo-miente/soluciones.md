## Soluciones del capítulo 15

> Las soluciones son razonadas: el número final es lo menos importante. En los
> problemas ● y ★ con solución cerrada hay **Pista 1** y **Pista 2** antes de
> ella; tápalas con la mano y úsalas de una en una.
>
> Los de **Mundo real** (R) no llevan solución a propósito: su procedimiento
> está en el apéndice D.

---

### Calentamiento

**15.C1** Con 3 parámetros, $\nu=17$ y $\chi^2\approx17\pm\sqrt{34}\approx
17\pm6$. Con 18 parámetros, $\nu=2$ y $\chi^2\approx2$: **casi cualquier
modelo con 18 parámetros ajustará 20 datos**, y el valor bajo de $\chi^2$ no
significa nada.

**15.C2** Por AIC, el de 3 (138 < 142). Por BIC, también, y con más margen
(145 < 158), porque BIC penaliza más los parámetros. Cuando ambos coinciden, la
decisión es cómoda; cuando discrepan, hay que ir a validación.

**15.C3** (a) confusor; (b) **colisionador** —es el sesgo de Berkson, y explica
por qué entre los profesionales de élite talento y suerte parecen
anticorrelacionados—; (c) confusor.

**15.C4** Un artefacto numérico. Y la comprobación costó un minuto.

---

### Estimación

**15.E1** Regla práctica: se necesitan al menos 10 datos por parámetro para que
el ajuste sea estable, y bastantes más para que la validación sea informativa.
Con 50 datos, más de 5 parámetros empieza a ser arriesgado y más de 10 es
temerario. La cuenta rigurosa depende del condicionamiento del problema, pero
el orden de magnitud es ese.

**15.E2** $\binom{20}{2}=190$ correlaciones. Al 5 %, se esperan
$190\times0{,}05\approx10$ «significativas» por puro azar. Con corrección de
Bonferroni, el umbral debería ser $0{,}05/190=2{,}6\times10^{-4}$. Es el
look-elsewhere del capítulo 4 con otro traje.

**15.E3** ● *Pista 1:* no razones con probabilidades: razona con 1000 hipótesis de carne y hueso y ve contándolas, como en el capítulo 3.
*Pista 2:* separa las verdaderas de las falsas, aplica la potencia a unas y $\alpha$ a las otras, y mira qué fracción de los positivos viene del grupo equivocado.
*Solución:* Con prevalencia previa de hipótesis verdaderas $\pi$, potencia
$1-\beta=0{,}4$ y $\alpha=0{,}05$: de 1000 hipótesis con $\pi=0{,}1$, hay 100
verdaderas de las que se detectan 40, y 900 falsas de las que 45 dan positivo.
**El 53 % de los positivos son falsos.** Es el argumento central de Ioannidis
(2005), y lo notable es que no requiere ninguna mala conducta: sólo potencia
baja y muchas hipótesis.

---

### Modelado

**15.M1** El punto (c) es el que casi nadie escribe y el que da valor al
ejercicio. Sin criterio de abandono preescrito, siempre habrá una explicación
*a posteriori* para cualquier discrepancia.

**15.M2** Lo habitual: aplicar un desplazamiento aleatorio desconocido al
resultado final, congelar todos los cortes, correcciones y criterios de
selección, y sólo entonces revelar. Lo que **no** se oculta son los datos de
control y calibración, que hay que poder mirar. La dificultad práctica es
social: exige comprometerse por escrito antes de ver nada.

**15.M3** ● *Pista 1:* para que la paradoja aparezca hace falta una tercera variable, y tiene que estar correlacionada con **dos** cosas a la vez.
*Pista 2:* ¿con cuáles? Con el tratamiento y con el pronóstico. Si la asignación fuera aleatoria, la primera correlación desaparecería, y con ella la paradoja.
*Solución:* El ingrediente necesario es una variable de estratificación
correlacionada tanto con el tratamiento como con el pronóstico. Cualquier
sistema donde la asignación no sea aleatoria lo produce, y es la razón de ser
de la aleatorización.

---

### Derivación

**15.D1** El AIC estima la divergencia KL esperada entre el modelo ajustado y
la verdad. El término $2k$ sale de corregir el sesgo optimista de usar los
mismos datos para ajustar y para evaluar: en promedio, la log-verosimilitud
máxima sobreestima la esperada en $k$ (a primer orden), y el factor 2 viene de
la convención $-2\ln\mathcal{L}$.

**15.D2** Sean $X,Y$ independientes $N(0,1)$ y $Z=X+Y$. Condicionado a $Z=z$,
$Y=z-X$: la correlación condicional es $-1$. Dos variables independientes se
vuelven perfectamente anticorrelacionadas al condicionar por su suma.
**Ese es todo el mecanismo del colisionador**, y en cuanto se ve así deja de
parecer paradójico.

**15.D3** ● *Pista 1:* descompón $f$ en la suma de un término constante, términos de una variable, de dos, y así sucesivamente, todos ortogonales entre sí.
*Pista 2:* la varianza se reparte igual que la función. Los índices de primer orden suman 1 sólo si sobra algo, y ese algo tiene nombre.
*Solución:* Con $Y=f(X_1,\dots,X_k)$ y $X_i$ independientes, la descomposición
ANOVA funcional da $f=f_0+\sum f_i+\sum f_{ij}+\dots$ con términos
ortogonales, luego $\operatorname{Var}(Y)=\sum V_i+\sum V_{ij}+\dots$. Los
índices de primer orden suman 1 **sólo si no hay interacciones**; el déficit
$1-\sum S_i$ es exactamente la fracción de varianza debida a interacciones, y
es la cantidad que el análisis local es incapaz de ver.

---

### Computacional

**15.P1** Con 100 datos el grado óptimo sube (a 5 o 6) y la caída del error de
validación es mucho más suave. **Más datos permiten más complejidad**, y la
relación es aproximadamente lineal en el número de parámetros admisibles.

**15.P2** Suelen coincidir en el orden de magnitud del grado óptimo pero no
siempre en el valor exacto. AIC tiende a elegir grados algo mayores que la
validación cruzada; BIC, menores. Cuando los tres discrepan mucho, es señal de
que el problema está mal condicionado y **ninguno** es de fiar.

**15.P3** La banda **entre modelos** en $t=40$ abarca cinco órdenes de
magnitud; la banda de covarianza de cada modelo individual es de un factor 2 o
3. La conclusión, que hay que decir en voz alta: **la barra de error que
publica la gente es la pequeña, y la relevante es la grande.**

---

### Experimento

**15.X1** Divergen cuando el modelo es fuertemente no lineal en los parámetros
o cuando el valle del $\chi^2$ es curvo. La elipse de covarianza supone un
valle cuadrático; el perfil sigue el valle real. En problemas con parámetros
casi no identificables, el perfil puede dar intervalos **infinitos** por un
lado, cosa que la covarianza nunca revela.

**15.X2** ● *Pista 1:* la sensibilidad local mira una derivada en un punto; Sobol mira toda la distribución de entradas. En un modelo lineal coinciden.
*Pista 2:* busca deliberadamente un parámetro cuya derivada se anule en el punto nominal pero que interactúe con otro. Ahí es donde las dos respuestas se separan.
*Solución:* En modelos no lineales con interacciones, es habitual que cambie el
orden de importancia de los parámetros, y no es raro que un parámetro con
sensibilidad local nula tenga índice de Sobol apreciable. La conclusión más
frecuente que cambia es «este parámetro no hace falta medirlo mejor».

---

### Detective

**15.T1** **No necesariamente.** Puede ser progreso o puede ser el mecanismo de
Millikan: convergencia hacia el valor previo por un procedimiento asimétrico de
búsqueda de errores. La forma de distinguirlos es mirar si las mediciones son
**metodológicamente independientes** —técnicas distintas, laboratorios
distintos, análisis ciegos— o si cada una conocía la anterior.

**15.T2** Falta separar calibración de validación. Si las parametrizaciones se
ajustaron con el mismo periodo, un error de 0,05 °C no dice nada sobre su
corrección. Lo que habría que reportar: la capacidad de reproducir un periodo
o un fenómeno **no usado** en el ajuste (por ejemplo, la respuesta a una
erupción volcánica, o el clima del Holoceno medio).

**15.T3** ● *Pista 1:* la pregunta no es la probabilidad de que **ese** subgrupo salga por azar, sino la de que salga **alguno** de los treinta.
*Pista 2:* calcula el complementario: la probabilidad de que ninguno salga. Verás que lo raro habría sido no encontrar nada.
*Solución:* Con 30 subgrupos y $\alpha=0{,}05$, la probabilidad de encontrar al
menos uno significativo por azar es $1-0{,}95^{30}=79\,\%$. Es decir: **es más
probable encontrar un subgrupo espurio que no encontrarlo**. Por eso los
análisis de subgrupos se preespecifican y se corrigen por multiplicidad, y por
eso los hallazgos de subgrupo no preespecificados se tratan como generadores de
hipótesis y no como resultados.

---

### Feynman

**15.F1** Guion: «Imagina que tienes que dibujar una línea que pase por diez
puntos que has medido con cierto error. Si la línea es recta, no puede pasar
exactamente por todos, y la parte que no encaja es el error de medida: eso está
bien. Si usas una curva con diez recovecos, puede pasar por todos exactamente,
pero entonces también ha copiado los errores, y esos errores no volverán a
repetirse. La curva complicada ha aprendido las equivocaciones de esa tarde
concreta, no la ley.»

**15.F2** Guion: «Si estudias sólo a la gente que entró en una universidad muy
selectiva, encontrarás que los que sacan mejores notas son peores deportistas.
No porque estudiar estropee el deporte, sino porque para entrar hacía falta
destacar en algo: si eres flojo en deporte, tuviste que ser buenísimo en notas.
Al mirar sólo a los que entraron has creado una relación que en la población
general no existe. A veces controlar por una variable no limpia el análisis: lo
ensucia.»

---

### Extensión

**15.Z1** ★ *Pista 1:* la fuga de datos no es un solo error: es una familia. Intenta clasificarlos por **en qué momento** la información del conjunto de prueba se cuela.
*Pista 2:* piensa en el preprocesado, en los duplicados, en las variables que no existirían en el momento de predecir y en el muestreo temporal.
*Solución:* Kapoor y Narayanan catalogan ocho tipos, entre ellos: falta de
separación limpia entre entrenamiento y prueba, preprocesado hecho sobre el
conjunto completo, uso de características no disponibles en el momento de la
predicción, duplicados entre conjuntos, y muestreo temporal incorrecto. Su
hallazgo más incómodo: encontraron fugas en 329 artículos de 17 campos
distintos, casi todos revisados por pares.

**15.Z2** ★ *Pista 1:* separa dos cosas: si la aritmética es correcta dadas las premisas, y si las premisas son razonables.
*Pista 2:* la premisa más discutible es la prevalencia previa $\pi$, que no es observable. La otra crítica es estructural: la ciencia no avanza por estudios aislados.
*Solución:* El argumento de Ioannidis es aritméticamente correcto dadas sus
premisas (potencia baja, muchas hipótesis, sesgo de publicación, flexibilidad
analítica). Las críticas más sólidas señalan que la prevalencia previa $\pi$ no
es observable y que sus valores supuestos son pesimistas, y que la ciencia no
funciona por estudios aislados sino por replicación acumulativa. La posición
razonable: la conclusión literal («la mayoría») no está establecida, pero la
**dirección** del argumento sí, y las reformas que motivó —preregistro,
potencias mayores, publicación de resultados nulos— son buenas
independientemente de si la cifra exacta era correcta.
