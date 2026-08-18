# Interludio 8 — La señora del MANIAC

*Va después del capítulo 16.*

---

En el informe LA-1940 de Los Álamos, fechado en mayo de 1955, se lee en la
sección de agradecimientos que los autores disfrutaron de la eficiente
cooperación de la señora Mary Tsingou.

El informe se titula *Studies of Nonlinear Problems* y firma Enrico Fermi, John
Pasta y Stanisław Ulam. Es el origen de lo que durante cincuenta años se llamó
el problema FPU y que hoy se llama, cada vez más, FPUT.

La señora Mary Tsingou escribió el programa.

---

## Qué significaba programar en 1954

Conviene detenerse aquí, porque la palabra «programar» ha cambiado tanto de
significado que la mención en los agradecimientos suena hoy a tarea auxiliar.

El MANIAC I era una máquina con memoria de tubos Williams, del orden de mil
palabras. No había lenguaje de alto nivel, ni compilador, ni sistema operativo,
ni siquiera ensamblador en el sentido moderno. Programar significaba:

Diseñar el flujo completo de operaciones en código máquina. Asignar a mano cada
posición de memoria. Gestionar la aritmética de punto fijo, decidiendo dónde
poner el punto decimal en cada variable para que nada desbordara ni perdiera
precisión. Escribir las rutinas de las funciones elementales, porque no había
biblioteca. Depurar sin depurador, mirando registros. Y decidir qué
comprobaciones hacer para distinguir un resultado real de un error de la
máquina, que en 1954 fallaba a menudo.

Es decir: **una parte sustancial del diseño del experimento**. La decisión de
qué integrador usar, con qué paso, con qué precisión y con qué controles no es
separable del resultado científico. En este caso, además, era crítica: la
recurrencia que descubrieron sólo es visible si la integración conserva la
energía razonablemente bien durante decenas de miles de periodos.

Mary Tsingou —Mary Tsingou Menzel tras su matrimonio— era licenciada en
matemáticas por la Universidad de Wisconsin, con un máster de la de Michigan.
Trabajó en Los Álamos desde 1952 hasta su jubilación en 1991.

---

## El resultado

El experimento y su resultado están en el capítulo 16. En resumen: una cadena de
64 osciladores unidos por muelles con una pequeña no linealidad, toda la energía
puesta en el modo más lento, y la expectativa universal de que se repartiera
entre todos los modos.

No se repartió. La energía visitó unos pocos modos y volvió casi entera al
inicial.

El informe lo describe con una franqueza que hoy resulta llamativa: los
resultados no mostraban la equipartición esperada, y los autores no tenían
explicación.

Fermi murió en noviembre de 1954, antes de que el informe circulara. Según
Ulam, lo consideraba uno de los trabajos más interesantes en los que había
participado, precisamente porque el resultado no era el esperado.

---

## Cincuenta y tres años

En 2008, Thierry Dauxois publicó en *Physics Today* un artículo corto titulado
*Fermi, Pasta, Ulam, and a mysterious lady*. Documentaba el papel de Tsingou,
reproducía sus cuadernos de trabajo, y proponía que el problema se llamara
FPUT.

Tsingou tenía entonces 80 años. En entrevistas posteriores describió el trabajo
con notable sobriedad: contaba que hacía la programación, que era lo que le
tocaba, y que en aquella época a los programadores no se les incluía como
autores.

Esa última frase es la clave del asunto, y explica por qué esto no es una
historia de villanos. **La convención de la época era esa.** Nadie infringió una
norma: la norma consideraba la programación un trabajo técnico de apoyo, como
operar un instrumento o preparar una muestra.

Lo que ha cambiado no es la ética de nadie: es la comprensión de que el diseño
computacional **es** parte del contenido científico. Y ese cambio ha llegado
tarde y de forma desigual.

---

## El patrón

Tsingou no es un caso aislado. La lista es larga y tiene una dirección clara.

Las computistas de Harvard que clasificaron cientos de miles de espectros
estelares a finales del siglo XIX —Williamina Fleming, Annie Jump Cannon,
Antonia Maury—, cuyo sistema de clasificación seguimos usando. Henrietta Swan
Leavitt, cuya relación periodo-luminosidad en las cefeidas hizo posible medir
distancias extragalácticas, y con ella la expansión del universo. Las
computistas humanas del JPL que calcularon trayectorias de misiones. Katherine
Johnson, Dorothy Vaughan y Mary Jackson en la NASA. Arianna Rosenbluth y el
algoritmo de Metropolis (interludio 4). Margaret Hamilton y el software del
Apolo.

En casi todos los casos el mecanismo es el mismo: el trabajo se clasificó como
técnico y no como científico, y esa clasificación determinó la autoría.

---

## Por qué está esto en un libro de modelado

Por tres razones concretas, no por corrección retrospectiva.

**Primera, y la más práctica: la implementación no es separable del
resultado.** El capítulo 8 lo mostró con integradores: elegir Verlet o Euler no
es un detalle de programación, es una decisión que determina si el fenómeno se
ve o se pierde bajo la deriva numérica. Quien toma esas decisiones está haciendo
ciencia, se llame como se llame su puesto.

**Segunda: si crees que la programación es la parte fácil, no has hecho
suficiente.** Es una advertencia dirigida a quien lea este libro. La parte
difícil de un experimento computacional no es la idea: es garantizar que el
código hace lo que crees, que el resultado no es un artefacto y que otra persona
puede reproducirlo. El capítulo 16 entero trata de eso.

**Y tercera: la historia limpia impide aprender.** Un relato en el que las ideas
surgen de mentes individuales y la ejecución es un trámite produce una imagen
falsa de cómo se hace la ciencia, y esa imagen falsa te perjudica cuando te toca
hacerla a ti. La ciencia computacional es un trabajo colectivo en el que la
frontera entre pensar y ejecutar es mucho más borrosa de lo que sugieren las
listas de autores.

---

## Coda

Mary Tsingou Menzel vive, a la fecha de escribir esto, en Los Álamos. En 2020
cumplió 92 años.

Su cadena de osciladores sigue siendo, sesenta y ocho años después, uno de los
sistemas más estudiados de la física no lineal.

---

### Referencias

* **Fermi, E.; Pasta, J.; Ulam, S.** *Studies of Nonlinear Problems.* Los Alamos
  report LA-1940, 1955. **Nivel A (primaria).** Léase la sección de
  agradecimientos.
* **Dauxois, Thierry.** *Fermi, Pasta, Ulam, and a mysterious lady.* Physics
  Today **61** (2008), 55–57. **Nivel A.** El artículo que recuperó su papel,
  con reproducción de los cuadernos.
* **Porter, M. A.; Zabusky, N. J.; Hu, B.; Campbell, D. K.** *Fermi, Pasta,
  Ulam and the Birth of Experimental Mathematics.* American Scientist **97**
  (2009), 214–221. **Nivel A.**
* **Metropolis, Nicholas.** *The Los Alamos Experience, 1943–1954*, en *A
  History of Scientific Computing*, ACM Press, 1990. **Nivel A (memoria).**
  Qué significaba programar aquellas máquinas.
* **Grier, David Alan.** *When Computers Were Human.* Princeton UP, 2005.
  **Nivel A.** La historia del cálculo humano y de quiénes lo hacían.
* **Shetterly, Margot Lee.** *Hidden Figures.* William Morrow, 2016.
  **Nivel A (secundaria).** El caso de la NASA, documentado.
