# Interludio 3 — Ulam jugando al solitario

*Va después del capítulo 9.*

---

En enero de 1946, Stanisław Ulam estaba convaleciente en Los Ángeles de una
encefalitis aguda que había estado a punto de matarlo. Le habían practicado una
craneotomía de urgencia. Durante la recuperación no podía trabajar en nada
serio, y para pasar el rato jugaba al solitario Canfield.

El Canfield es un solitario con muy mala tasa de éxito. Ulam, aburrido, se
preguntó cuál era exactamente la probabilidad de completarlo.

Lo cuenta él mismo en *Adventures of a Mathematician*: después de intentar
estimarla con combinatoria pura y ver que era un problema enorme, se le ocurrió
que sería mucho más práctico jugar cien manos y contar los éxitos.

Y a continuación —esta es la parte que importa— pensó inmediatamente en los
problemas de difusión de neutrones en los que había estado trabajando.

---

## Por qué el salto no es obvio

Visto desde hoy parece trivial: si no sabes calcular una probabilidad, simula
muchas veces y cuenta. La idea de muestrear para estimar tiene siglos, y Buffon
ya la había usado en 1733.

Lo que hace especial el momento de Ulam es la **dirección** del razonamiento.

En el solitario, la probabilidad es la magnitud que interesa y el juego es el
proceso natural: simular es lo obvio. En la difusión de neutrones, la magnitud
que interesa es determinista —el factor de multiplicación de una masa de
material fisible, un número fijo— y lo que hay es una ecuación integrodiferencial
en un espacio de fases de seis dimensiones que nadie sabía resolver para
geometrías realistas.

El salto consiste en **darse cuenta de que esa ecuación describe el
comportamiento promedio de un proceso aleatorio subyacente**, y que por tanto
se puede estimar siguiendo trayectorias individuales de neutrones sorteadas al
azar: dónde choca, qué le pasa al chocar, hacia dónde sale, cuántos neutrones
nuevos produce.

Es decir: en lugar de resolver la ecuación que describe el promedio, **generar
el promedio**.

---

## Von Neumann y la carta

Ulam se lo contó a John von Neumann, con quien mantenía una relación de trabajo
estrecha. La reacción fue inmediata.

En marzo de 1947, von Neumann escribió a Robert Richtmyer, jefe de la división
teórica de Los Álamos, una carta de once páginas que se conserva y está
reproducida en la recopilación de Los Alamos Science de 1987. No es una carta
de ideas: es un **plan de cálculo completo** para el ENIAC. Contiene la
descripción del problema físico, el esquema de muestreo de las trayectorias, el
tratamiento de las secciones eficaces, la generación de números aleatorios, la
estructura de datos y un diagrama de flujo.

Leerla hoy produce una sensación curiosa. La parte perecedera —cómo se
programaba una máquina que se configuraba con cables— resulta arqueológica. La
parte que trata del **diseño del estimador** —qué se muestrea, cómo se pesan las
trayectorias, cómo se estima la varianza— es reconocible sin esfuerzo por
cualquiera que haya escrito un Monte Carlo esta semana.

El primer cálculo se ejecutó en el ENIAC en 1948.

---

## El nombre

El proyecto necesitaba un nombre en clave. Lo propuso Nicholas Metropolis, y lo
explicó él mismo en 1987: Ulam tenía un tío que pedía dinero prestado a la
familia porque «tenía que ir a Monte Carlo». El nombre quedó.

Es una etimología de una banalidad refrescante, y conviene contarla porque
contrarresta la tendencia a atribuir profundidad retrospectiva a todo lo que
acaba siendo importante.

---

## Lo que hay que llevarse

**Primero: el problema aburrido produjo el método.** Ulam no estaba buscando un
método general de integración numérica. Estaba aburrido en una cama de hospital
preguntándose por un juego de cartas. La conexión con la difusión de neutrones
la hizo porque llevaba meses con ese problema en la cabeza.

Ese patrón —una pregunta trivial en un dominio ilumina un problema serio en
otro— es el que este libro intenta entrenar, y es la razón por la que los
capítulos de la Parte II están organizados por fenómenos y no por disciplinas.
La transferencia no ocurre entre campos: ocurre entre **estructuras**.

**Segundo: la frustración fue informativa.** Ulam intentó primero el cálculo
combinatorio. Que fuera intratable no fue un fracaso: fue el dato que le hizo
buscar otra cosa. Un problema que no cede a la vía obvia está pidiendo un
cambio de representación, y merece la pena preguntarse explícitamente cuál.

**Tercero: hizo falta la máquina.** Muestrear trayectorias a mano es
impensable; con papel y lápiz no se llega a las decenas de miles de historias
que hacen falta. La idea de Ulam estaba disponible desde Buffon, pero **no era
utilizable**. Que un método sea buena idea y que sea aplicable son cosas
distintas, y a veces las separan doscientos años y una tecnología.

**Y cuarto, sobre la propia historia.** La fuente principal es la memoria de
Ulam, escrita treinta años después de los hechos. Es coherente con las cartas de
von Neumann y con el relato independiente de Metropolis, así que la cronología
es sólida. Pero conviene recordar que las memorias son reconstrucciones: la
frase exacta que se le ocurrió a Ulam mirando las cartas no la sabe nadie, ni
siquiera él treinta años después.

---

### Referencias

* **Ulam, Stanisław M.** *Adventures of a Mathematician.* Scribner's, 1976,
  capítulo 7. **Nivel A (memoria).**
* **Eckhardt, Roger.** *Stan Ulam, John von Neumann, and the Monte Carlo
  Method.* Los Alamos Science **15** (1987), 131–137. **Nivel A.** Incluye la
  carta de von Neumann a Richtmyer.
* **Metropolis, Nicholas.** *The Beginning of the Monte Carlo Method.* Los
  Alamos Science **15** (1987), 125–130. **Nivel A (memoria).**
* **Metropolis, N. y Ulam, S.** *The Monte Carlo Method.* JASA **44** (1949),
  335–341. **Nivel A (primaria).**
* **Haigh, Thomas; Priestley, Mark; Rope, Crispin.** *Los Alamos Bets on ENIAC:
  Nuclear Monte Carlo Simulations, 1947–1948.* IEEE Annals of the History of
  Computing **36** (2014), 42–63. **Nivel A.** La reconstrucción técnica más
  detallada de los primeros cálculos.
