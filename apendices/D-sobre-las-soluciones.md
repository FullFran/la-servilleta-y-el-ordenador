# Apéndice D — Sobre las soluciones

Las soluciones no están reunidas en este apéndice, sino **en la carpeta de cada
capítulo**, en el fichero `soluciones.md`, y aparecen al final del PDF de cada
capítulo.

La razón es práctica: separarlas del enunciado por trescientas páginas obliga a
un ir y venir que nadie hace, y agruparlas todas al final del libro invita a
mirarlas antes de tiempo. Estando en el mismo fichero pero después de los
enunciados, cuesta exactamente el esfuerzo adecuado: hay que buscarlas
deliberadamente.

## Cómo se numeran

Cada parte tiene su propio esquema, y por eso un identificador dice siempre de
dónde viene:

| Parte | Formato | Ejemplo | Se lee |
|---|---|---|---|
| I | `capítulo.CATEGORÍAnúmero` | `7.D3` | capítulo 7, tercer problema de Derivación |
| II | `II.capítulo.número` | `II.11.4` | Parte II, capítulo 11, problema 4 |
| III | letra, dentro del capítulo | `C` | tercer ejercicio de campo de ese capítulo |

Las diez categorías de la Parte I son: **C** calentamiento · **E** estimación ·
**D** derivación · **M** modelado · **P** programación · **X** experimento
computacional · **T** detective · **F** Feynman · **R** mundo real ·
**Z** extensión.

La dificultad va marcada aparte: sin marca (directo), **○** (requiere pensar),
**●** (cuesta una tarde), **★** (abierto, sin solución cerrada).

## Cómo están escritas

**Razonadas, no numéricas.** El número final es lo menos importante. Lo que se
explica es el camino, y sobre todo **por qué ese camino y no otro**.

**Con pistas graduadas** en todos los problemas ● y ★ que tienen solución
cerrada —los 127 de la Parte I—:

```text
● Pista 1: la idea que desbloquea
  Pista 2: el paso técnico que cuesta
  Solución: el desarrollo completo
```

Tápalas con la mano y úsalas de una en una. Si lees la solución directamente,
el problema no ha servido para nada: los problemas ● están calibrados para que
cuesten una tarde.

Los de **Mundo real** (categoría R) son la excepción, y a propósito: no tienen
solución en el libro porque la respuesta depende de tu trabajo, no del mío. Su
guía no es una pista, es el procedimiento de la última sección de este apéndice.
Lo mismo vale para el puñado de problemas de otras categorías que también piden
aplicar algo a un caso propio.

**Con el error esperado declarado.** En los problemas de estimación se indica
qué margen es aceptable. Si tu número difiere en un factor 2 o 3, **no está
mal**. Si difiere en un factor 100, hay una estructura que revisar, no un dato.

## Los problemas ★

No tienen solución cerrada, y su «solución» es un comentario sobre por dónde
atacarlos y qué se aprende. Están ahí porque los problemas reales son así, y
porque acostumbrarse a que todo problema tenga respuesta es una mala
preparación.

## Cómo usar los ejercicios

* **Estimación:** primero estima, después comprueba. Sin excepciones. Y anota
  tu intervalo del 90 % antes.
* **Detective:** contienen errores a propósito. Son los más útiles y los que
  más se saltan.
* **Feynman:** se hacen **en voz alta**. Escribirlos no es lo mismo: el habla
  no permite volver atrás y delata los huecos.
* **Mundo real:** no tienen respuesta única. Su valor está en el proceso, y
  conviene escribirlos en el cuaderno con la plantilla del apéndice G.

## Cómo se ataca un problema de Mundo real

Todos tienen la misma forma —«coge algo de tu trabajo y aplícale esto»— y por
eso comparten procedimiento. Estos cinco pasos sustituyen a las pistas:

1. **Elige el caso más pequeño que siga siendo real.** No el proyecto entero:
   un módulo, un experimento, una métrica. Si tardas más de una tarde en
   entender el objeto, es demasiado grande.
2. **Escribe la pregunta con unidades antes de mirar ningún dato.** La mitad de
   estos problemas se atascan aquí, y ese atasco ya es un hallazgo.
3. **Predice el resultado por escrito.** Un número y un intervalo. Sin esto no
   podrás distinguir «lo sabía» de «ahora me lo parece».
4. **Hazlo, y anota dónde te desviaste de tu predicción y por qué.** Ese es el
   dato que el problema quería generar.
5. **Escribe una frase transferible.** No sobre este caso: sobre lo que harás
   distinto la próxima vez.

Si al terminar no tienes esa frase, el problema no ha terminado.

Y una advertencia: estos problemas suelen encontrar cosas incómodas sobre
trabajo propio o ajeno. Es su función. Lo que se hace con el hallazgo es otra
cuestión, y suele requerir más tacto que técnica.
