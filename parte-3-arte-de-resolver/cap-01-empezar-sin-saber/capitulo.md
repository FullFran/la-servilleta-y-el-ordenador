# III.1 — Cómo empezar cuando no sabes qué hacer

> **Nota sobre la Parte III.** Estos capítulos son manual de campo: cortos,
> operativos y pensados para consultarse cuando estás atascado. No traen
> herramientas nuevas; traen protocolo. Los ejercicios van integrados al final
> de cada uno, y cada capítulo termina con una lista de comprobación de una
> página pensada para imprimirse.

---

## El problema

Tienes delante algo que no entiendes y ninguna idea de por dónde empezar. La
sensación es de bloqueo total, y es engañosa: **casi siempre hay algo que
hacer, y ese algo casi nunca es «pensar más fuerte»**.

Lo que sigue son ocho movimientos. Están ordenados por coste creciente, y casi
todos los problemas ceden con los tres primeros.

---

## Los ocho movimientos

### 1. Escribe la pregunta

Si no puedes escribirla en una frase con un signo de interrogación al final, no
tienes una pregunta: tienes un tema. Y no se puede empezar a resolver un tema.

Añade después dos cosas: **las unidades** de la respuesta que buscas y **la
precisión** que necesitas. Ambas cambian radicalmente el trabajo.

### 2. Estima el orden de magnitud

Capítulo 1. Aunque sea con cotas absurdas. Sirve para tres cosas: te obliga a
identificar de qué depende la respuesta, te da un patrón contra el que juzgar
lo que salga después, y a veces resuelve el problema.

### 3. Haz un dibujo

Un esquema con las cantidades, las flechas de lo que influye en qué, y los
números que ya conoces. Es sorprendente cuántos problemas se disuelven en el
momento de dibujarlos, y cuántos revelan al dibujarlos que estaban mal
planteados.

### 4. Resuelve un problema más fácil

La heurística central de Pólya. Cuatro variantes que funcionan casi siempre:

* **Quita una dimensión.** Hazlo en 1D antes que en 3D.
* **Quita la no linealidad.** Lineariza y mira qué pasa.
* **Toma un límite extremo.** ¿Qué ocurre si el parámetro es cero? ¿Y si es
  infinito? Los dos límites suelen ser fáciles y acotan la respuesta.
* **Coge un caso particular con números.** Sustituye lo general por un ejemplo
  concreto y calcula.

### 5. Pregunta qué se conserva

Capítulo 6. Energía, masa, carga, momento, número de individuos, dinero. Una
ley de conservación reduce la dimensión del problema y a veces lo cierra.

Pregunta hermana: **¿qué simetría hay?** Si el problema es invariante bajo algo,
la solución también debe serlo, y eso descarta familias enteras de respuestas.

### 6. Cuenta los grados de libertad

¿Cuántos números hacen falta para describir el estado? ¿Cuántos parámetros hay?
Con análisis dimensional (capítulo 2), ¿cuántos quedan?

Este movimiento es barato y sorprendentemente informativo: te dice si el
problema es de uno, de dos o de veinte parámetros, y eso decide qué técnicas
son viables.

### 7. Busca el mismo problema en otro campo

Es el movimiento con mayor rendimiento y el que menos se hace. La Parte II
entera existe para entrenarlo: si tu problema tiene la forma «algo crece
mientras haya recurso», ya está resuelto en ecología; si tiene la forma
«esperar por un recurso compartido», está resuelto en teoría de colas; si tiene
la forma «recuperar la causa a partir del efecto», está resuelto en problemas
inversos.

La pregunta operativa es: **¿qué estructura tiene esto?**, no «¿de qué campo
es?».

### 8. Habla con alguien

O con un pato de goma. El acto de explicar en voz alta obliga a linealizar el
razonamiento y expone los huecos. Es el capítulo III.10 aplicado hacia dentro,
y es también el motivo por el que la sección *Explícalo* aparece en todos los
capítulos de este libro.

---

## Lo que no funciona

**Leer más.** Es el bloqueo disfrazado de productividad. Leer sirve cuando
tienes una pregunta concreta; antes de eso, es procrastinación con buena
conciencia.

**Empezar a programar.** Escribir código antes de haber formulado el problema
produce un simulador de algo que no sabes qué es. Y como el código funciona,
resulta muy difícil admitir que no responde a nada.

**Buscar el método correcto.** El método sale del problema, no al revés. Si te
descubres pensando «esto seguro que se hace con X», comprueba primero que el
problema lo pide.

**Pedírselo a una IA antes de intentarlo.** Capítulo III.13. Obtendrás una
respuesta plausible y habrás perdido la oportunidad de construir el criterio que
te permitiría juzgarla.

---

## Lista de comprobación

```text
CUANDO NO SÉ POR DÓNDE EMPEZAR

□ ¿He escrito la pregunta en una frase, con unidades y precisión?
□ ¿He estimado el orden de magnitud, aunque sea con cotas absurdas?
□ ¿He hecho un dibujo con las cantidades y las flechas?
□ ¿He resuelto una versión más fácil?
    □ una dimensión menos
    □ sin la no linealidad
    □ en el límite extremo
    □ con números concretos
□ ¿Qué se conserva? ¿Qué simetría hay?
□ ¿Cuántos grados de libertad y cuántos parámetros quedan al adimensionalizar?
□ ¿Dónde he visto antes esta estructura?
□ ¿Se lo he explicado en voz alta a alguien?

Y si sigo atascado:
□ ¿Estoy respondiendo a la pregunta correcta?
□ ¿Qué haría falta saber para que esto fuera fácil?
□ ¿Qué es lo más simple que podría estar pasando?
```

---

## Ejercicios de campo

**A.** Coge un problema de tu trabajo que lleve tiempo atascado. Aplica los ocho
movimientos por escrito, en orden, sin saltarte ninguno. Anota en cuál se
desatasca.

**B.** Elige un fenómeno que no entiendas —por qué las nubes tienen la base
plana, por qué hay ondas en la arena de la playa, por qué el café forma anillos
al secarse— y aplica sólo los movimientos 1 a 4. Media hora, sin buscar nada.

**C.** Durante una semana, cada vez que te bloquees en algo, anota cuál de los
ocho movimientos te desatascó. Al final tendrás tu propio orden, que
probablemente no sea el de esta lista.

---

### Referencias

* **Pólya, George.** *How to Solve It.* Princeton UP, 1945. El origen de casi
  todo lo de este capítulo.
* **Mahajan, Sanjoy.** *The Art of Insight in Science and Engineering.* MIT
  Press, 2014. Los movimientos 2, 4 y 6, en versión desarrollada.
* **Hamming, Richard.** *The Art of Doing Science and Engineering.* 1997. Sobre
  todo el capítulo sobre cómo elegir problemas.
* **Schoenfeld, Alan.** *Mathematical Problem Solving.* Academic Press, 1985.
  El estudio empírico de qué hacen de verdad los que resuelven bien.
