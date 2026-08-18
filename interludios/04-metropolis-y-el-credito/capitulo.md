# Interludio 4 — Metropolis, y una idea que terminó apareciendo por todas partes

*Va después del capítulo 9.*

---

El artículo se titula *Equation of State Calculations by Fast Computing
Machines*. Se publicó en el *Journal of Chemical Physics* en junio de 1953,
ocupa seis páginas y firma cinco autores en orden alfabético: Nicholas
Metropolis, Arianna W. Rosenbluth, Marshall N. Rosenbluth, Augusta H. Teller y
Edward Teller.

Contiene el algoritmo que hoy se conoce universalmente como **algoritmo de
Metropolis**, que es probablemente el procedimiento numérico más usado de la
segunda mitad del siglo XX y que aparece hoy en física estadística, química
computacional, biología estructural, estadística bayesiana, aprendizaje
automático, econometría, criptografía y optimización combinatoria.

Es también un caso de estudio sobre cómo se reparte el crédito científico.

---

## El problema

En 1952, en Los Álamos, se quería calcular la ecuación de estado de un fluido
de esferas duras: cómo depende la presión de la densidad para un montón de
bolas que sólo interaccionan al chocar.

La magnitud a calcular es un promedio sobre todas las configuraciones posibles
del sistema, pesadas por el factor de Boltzmann. Con $N$ partículas en dos
dimensiones, eso es una integral en $2N$ dimensiones. Con $N=224$ —el número
que usaron— son 448 dimensiones.

Ninguna cuadratura sirve para eso (capítulo 9). Y el muestreo directo tampoco:
si sorteas configuraciones al azar, casi todas tendrán solapamientos entre
esferas y peso esencialmente nulo. Estarías gastando el 99,999 % del esfuerzo
en configuraciones que no contribuyen.

---

## La idea

En lugar de generar configuraciones independientes, **modifícalas poco a poco**.
Coge una partícula, muévela un poco al azar, y decide si aceptas el cambio
según cuánto haya cambiado la energía: si baja, acepta; si sube, acepta con
probabilidad $e^{-\Delta E/kT}$.

El resultado es una cadena de configuraciones que, a largo plazo, aparecen con
exactamente la frecuencia que dicta el factor de Boltzmann. **Y en ningún
momento hace falta la función de partición**, porque sólo aparecen cocientes de
probabilidades y la constante de normalización se cancela.

Ese es todo el algoritmo. Cabe en nueve líneas de Python, y en 1953 se ejecutó
en el MANIAC I, una máquina con 1024 palabras de memoria.

---

## Quién hizo qué

En 2003, poco antes de morir, Marshall Rosenbluth concedió una entrevista en la
que describió el reparto del trabajo. James Gubernatis la recogió y publicó en
*Physics of Plasmas* en 2005. Su versión:

* **Nicholas Metropolis** aportó tiempo de máquina y la infraestructura del
  MANIAC. No participó en el desarrollo del algoritmo.
* **Edward Teller** hizo una sugerencia importante en una conversación inicial:
  muestrear en el espacio de configuraciones en lugar de en el de momentos, ya
  que la parte cinética se integra analíticamente.
* **Augusta Teller** empezó parte del trabajo de programación.
* **Marshall y Arianna Rosenbluth** desarrollaron el algoritmo y escribieron el
  programa. Arianna Rosenbluth, doctora en física por Harvard, programó el
  MANIAC entero.

Marshall Rosenbluth lo resumía diciendo que Metropolis no había tenido nada que
ver con el desarrollo salvo por proporcionar tiempo de ordenador.

Los autores se ordenaron alfabéticamente, como era y sigue siendo costumbre en
algunas comunidades. Con la convención de citar por el primer autor, el
algoritmo quedó bautizado por quien menos había intervenido.

---

## Por qué contar esto

No es afán revisionista, ni interesa señalar culpables: nadie hizo trampa. La
combinación de dos convenciones razonables por separado —orden alfabético y
cita por el primer autor— produjo un resultado que no representa el trabajo.

Interesa por tres razones.

**Primera: entender cómo se produce el conocimiento incluye entender cómo se
reparte el crédito.** Un libro que enseña a modelar y que además cuenta
historias de científicos tiene la obligación de contarlas bien, porque la
versión cómoda —un nombre, una idea, un genio— es precisamente la que impide
entender que la ciencia es un trabajo colectivo.

**Segunda: el patrón se repite.** Mary Tsingou en FPU (interludio 8). Rosalind
Franklin en la estructura del ADN. Jocelyn Bell en los púlsares. Las
computistas de Harvard, del JPL y de Los Álamos, cuyo trabajo aparece
sistemáticamente en agradecimientos y no en autorías. No es una anécdota
aislada: es un sesgo estructural con una dirección clara.

**Tercera: Arianna Rosenbluth dejó la investigación** poco después, tras el
nacimiento de sus hijos, y no volvió. Su nombre está en uno de los artículos
más citados de la historia de la física computacional y casi nadie sabe quién
era. Murió en 2020.

---

## El artículo, además, se lee bien

Merece la pena leerlo entero. Son seis páginas, y el argumento del balance
detallado está ahí, explícito y sin florituras: explican por qué el
procedimiento genera la distribución correcta, discuten el tamaño del paso, la
tasa de aceptación y los efectos de tamaño finito, y presentan resultados
comparados con la aproximación de van der Waals.

También hay una frase que conviene recordar: reconocen que el método sólo da
promedios y no dice nada sobre la dinámica real del sistema. Es decir,
**declaran una limitación esencial en el propio artículo**, en 1953. Sesenta
años de literatura posterior lo han olvidado con cierta frecuencia.

---

### Referencias

* **Metropolis, N.; Rosenbluth, A. W.; Rosenbluth, M. N.; Teller, A. H.;
  Teller, E.** *Equation of State Calculations by Fast Computing Machines.*
  J. Chem. Phys. **21** (1953), 1087–1092. **Nivel A (primaria).**
* **Gubernatis, James E.** *Marshall Rosenbluth and the Metropolis algorithm.*
  Phys. Plasmas **12** (2005), 057303. **Nivel A.** La entrevista de 2003.
* **Rosenbluth, Marshall N.** *Genesis of the Monte Carlo algorithm for
  statistical mechanics.* AIP Conf. Proc. **690** (2003), 22–30.
  **Nivel A (primaria).** Su propio relato.
* **Hastings, W. K.** Biometrika **57** (1970), 97–109. La generalización.
* **Robert, Christian y Casella, George.** *A Short History of Markov Chain
  Monte Carlo.* Statistical Science **26** (2011), 102–115. **Nivel A.**
  Panorámica histórica cuidadosa, incluida la cuestión de la autoría.
