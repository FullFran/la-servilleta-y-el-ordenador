# Cómo usar este libro

Este libro no está escrito para ser leído. Está escrito para ser **usado**, que
es una cosa distinta y bastante más incómoda.

La diferencia es fácil de comprobar. Si lees el capítulo 1 en el sofá, en una
hora, sin lápiz, habrás pasado un rato agradable y no habrás aprendido nada
transferible. Si lo trabajas —estimando antes de leer la estimación, fallando,
mirando por qué fallaste— tardarás tres sesiones y saldrás con una capacidad que
antes no tenías. El libro está diseñado para el segundo caso y no funciona en el
primero.

## Qué pretende cambiar

No pretende que recuerdes más fórmulas. Pretende cambiar tu reacción ante algo
que no entiendes.

Queremos pasar de:

> «No sé cómo se resuelve esto.»

a:

> «Vale. ¿Qué escala tiene? ¿Qué variables importan? ¿Cuál es el modelo más
> simple que podría explicar esto? ¿Qué puedo estimar antes de calcular nada?»

Y de ahí a:

> «Vamos a construirlo y a comprobarlo.»

Ese cambio de comportamiento es el producto del libro. Todo lo demás
—las derivaciones, el código, las historias— es andamio.

## El ciclo

Todo el libro repite el mismo ciclo. Aparece por primera vez aquí, y volverás a
verlo, con una etapa resaltada, al principio de cada capítulo de la Parte II.

```text
fenómeno
  ↓
pregunta
  ↓
orden de magnitud
  ↓
variables relevantes
  ↓
supuestos
  ↓
modelo mínimo
  ↓
ecuaciones
  ↓
análisis de escalas
  ↓
solución aproximada
  ↓
simulación
  ↓
validación
  ↓
incertidumbre
  ↓
interpretación
  ↓
límites del modelo
  ↓
siguiente pregunta
```

No es un procedimiento burocrático. Es la secuencia que sigue, con más o menos
desorden, cualquiera que resuelva bien problemas nuevos. La diferencia entre
quien lo hace bien y quien no suele estar en las tres primeras etapas y en las
tres últimas, casi nunca en el medio. El medio es lo que enseña la carrera.

## Las tres partes

**Parte I — El instrumental del modelador.** Dieciséis herramientas, cada una
introducida por un problema que la necesita. Si algo te suena, no lo saltes:
está contado desde un ángulo distinto al de la carrera, y los ejercicios no son
los de la carrera.

**Parte II — Problemas que conectan las herramientas.** Catorce fenómenos. Aquí
no hay temas: hay una gota de lluvia, una epidemia, un atasco, una imagen
borrosa. Cada capítulo usa media Parte I a la vez, que es como funcionan los
problemas de verdad.

**Parte III — El arte de resolver problemas.** Trece capítulos cortos de
metodología explícita. Es el manual de campo: se consulta cuando estás atascado.
Se puede leer antes que todo lo demás, pero no se entiende bien hasta haberse
atascado unas cuantas veces.

**Interludios.** Ocho, intercalados, sin ejercicios. Sirven para cambiar el
ritmo y para ver a gente real resolviendo problemas reales, con sus errores
dentro.

## Las cinco reglas de uso

**1. Estima antes de leer.** Cuando aparezca una caja *Antes de calcular*, para.
Apunta un número. No importa que sea malo; importa que exista, porque el
aprendizaje está en la distancia entre tu número y el resultado, y esa distancia
no existe si no apuntaste nada.

**2. Predice antes de ejecutar.** Antes de correr cualquier simulación, escribe
qué esperas ver. Una frase basta. Ejecutar código y mirar la gráfica es
entretenimiento; predecir y contrastar es ciencia.

**3. Explica en voz alta.** Al final de cada sesión, explícale a alguien —o a la
pared, o al cuaderno— lo que has hecho, sin usar ecuaciones. Es la prueba más
barata y más despiadada de si has entendido algo.

**4. Escribe en el cuaderno.** Una entrada por problema, con la plantilla del
apéndice G. En tres meses, ese cuaderno vale más que el libro.

**5. Tus primeros veinte minutos son tuyos.** Sin buscador, sin IA, sin mirar la
solución. Después, todo vale. El capítulo III.13 explica en detalle por qué esta
regla es la más importante del libro y cómo aplicarla sin volverse un asceta
inútil.

## Cómo están marcados los ejercicios

| Marca | Significado |
|---|---|
| ○ | Directo. Si no sale en cinco minutos, revisa la sección |
| ◐ | Requiere pensar. Quince o veinte minutos |
| ● | Difícil. Puede llevar una tarde. Lleva pistas graduadas |
| ★ | Abierto. No tiene solución única, y por eso está aquí |

Los ejercicios de la categoría **Detective** contienen errores a propósito: se te
da un resultado plausible y falso, y tienes que encontrar dónde está el fallo.
Son los más útiles del libro y los que más se saltan.

## Qué necesitas

* Python 3.11 o superior, con NumPy, SciPy y Matplotlib. Nada más.
* Lápiz y papel de verdad. La estimación de servilleta se hace en servilleta.
* Un cuaderno, físico o digital, con la plantilla del apéndice G.
* De 45 a 90 minutos, cinco o seis días por semana, durante unas doce semanas.

El repositorio del libro incluye, para cada capítulo, el código de todas sus
figuras y un cuaderno interactivo. Nada de lo que ves en estas páginas viene de
una imagen encontrada por ahí: si una figura está en el libro, su script está en
el repositorio y lo puedes ejecutar y modificar.

## Una advertencia sobre la IA

Usas modelos de lenguaje a diario y no vamos a fingir que no existen. El libro
tampoco va a pedirte que renuncies a ellos: sería una tontería y no lo harías.

La postura es más concreta. La IA es extraordinaria ejecutando y peligrosa
formulando, y **formular es exactamente la habilidad que estamos entrenando**.
El protocolo de tres fases —humano, IA, humano— está en el capítulo III.13, y
aparecerá recordado en cajas a lo largo del libro cuando la tentación sea
especialmente fuerte. Si sigues una sola regla, que sea la de los veinte
minutos.

::: esencial
* El libro se usa, no se lee.
* Estima antes de leer; predice antes de ejecutar; explica al terminar.
* Los primeros veinte minutos de cada problema son tuyos y de nadie más.
* El objetivo no es saber más cosas: es reaccionar de otra manera ante lo que
  no entiendes.
:::
