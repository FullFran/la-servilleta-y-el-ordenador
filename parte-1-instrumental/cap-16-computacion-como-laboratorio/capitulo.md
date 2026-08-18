# Capítulo 16 — Computación como laboratorio

> **Qué sabrás hacer al terminar**
> · Diseñar un experimento computacional en lugar de «probar cosas» ·
> Barrer un espacio de parámetros sin desperdiciar CPU ·
> Hacer que un resultado tuyo sea reproducible por otra persona ·
> Escribir pruebas para código científico que sirvan de algo.
>
> **Herramientas que usa:** todas.
> **Disciplinas de los ejemplos:** física de sólidos, ingeniería, biología
> computacional, meteorología.
> **Deuda que paga:** la adimensionalización antes de barrer, prometida en los
> capítulos 2 y 6.

---

## 1. Una pregunta

::: pregunta
En 1953, en Los Álamos, tres físicos y una programadora simularon una cadena de
osciladores unidos por muelles ligeramente no lineales. Esperaban ver el
resultado más seguro de toda la física estadística: que la energía, puesta al
principio en un solo modo, acabara repartiéndose por igual entre todos.

No ocurrió. La energía volvió casi entera al modo inicial.

**¿Qué haces cuando el ordenador contradice algo de lo que estabas seguro?**
:::

Este capítulo trata del ordenador como **instrumento de descubrimiento** y no
como calculadora. La diferencia práctica es que un instrumento se calibra, se
somete a controles y se usa con un protocolo; una calculadora, no.

---

## 2. Antes de calcular

::: antes
1. Quieres explorar un modelo con 5 parámetros. ¿Cuántas simulaciones necesitas
   con una rejilla de 10 puntos por eje? ¿Y con un muestreo mejor?
2. Ejecutas dos veces el mismo código y sale distinto. ¿Cuántas causas
   posibles se te ocurren?
3. ¿Qué comprobación haría que confiaras en un código que no has escrito tú?
:::

---

## 3. La intuición

### 3.1 Simular no es experimentar, y tampoco es demostrar

Una simulación ocupa un lugar propio entre la teoría y el experimento, y
conviene ser preciso sobre cuál:

* **No es un experimento**, porque no interroga a la naturaleza sino a tu
  modelo. Si el modelo está mal, la simulación reproducirá fielmente su error.
* **No es una demostración**, porque explora casos particulares. Mil
  simulaciones no demuestran un teorema.
* **Sí es un instrumento de descubrimiento**: permite ver el comportamiento de
  sistemas que no se saben resolver, generar hipótesis y, sobre todo,
  **falsar intuiciones**.

Ese último punto es el que hace interesante la historia de FPU y el que da
título al capítulo.

### 3.2 El patrón del experimento computacional

```text
hipótesis → predicción escrita → simulación → observación
    → explicación → nueva hipótesis
```

La diferencia entre esto y «ejecutar código y mirar la gráfica» está en dos
puntos: la **predicción escrita** antes de ejecutar, y la exigencia de
**explicar** antes de pasar a lo siguiente.

Sin predicción previa, cualquier resultado parece razonable *a posteriori* —el
cerebro humano es extraordinariamente bueno racionalizando—. Sin explicación,
se acumulan gráficas y no conocimiento.

---

## 4. La matemática (y la práctica)

### 4.1 El experimento FPU, reproducido

![La cadena de Fermi, Pasta, Ulam y Tsingou. Izquierda: la energía de los cinco primeros modos, empezando con toda la energía en el modo 1. Derecha: la distribución final frente a la equipartición esperada. Lo que hay que concluir: la energía no se reparte; vuelve casi entera al modo inicial, y el 80 % sigue en los tres primeros modos.](figuras/fig_fpu.pdf)

Los números de esta reproducción: el 93,7 % de la energía vuelve al modo 1 en
$t\approx20\,300$, y al final del cálculo el 80 % sigue estando en los tres
primeros modos, frente al 9 % que predice la equipartición.

Lo importante no es el resultado sino **lo que se hizo con él**. Fermi, Pasta,
Ulam y Tsingou no publicaron un artículo triunfal: escribieron un informe
interno (LA-1940) describiendo el resultado como sorprendente y sin
explicación, y anotando explícitamente que el experimento no había hecho lo que
esperaban.

Ese resultado abrió tres líneas de investigación: los solitones (Zabusky y
Kruskal, 1965, que explicaron la recurrencia y de paso fundaron un campo), la
teoría KAM sobre la persistencia de trayectorias cuasi-periódicas, y el estudio
del caos en sistemas hamiltonianos.

**Un experimento numérico que falló abrió más ciencia que mil que confirman.**

::: aviso
**Y la comprobación obligatoria.** Antes de creerse una recurrencia como esta,
hay que descartar que sea numérica. En esta simulación la deriva de energía
total es $2\times10^{-3}$ en $8\times10^4$ unidades de tiempo, con Verlet de
velocidades (capítulo 8). Si se usa Euler explícito, la «recurrencia»
desaparece bajo la deriva. Los autores originales, con el MANIAC y aritmética
limitada, tuvieron que hacer exactamente esta comprobación.
:::

### 4.2 Adimensionalizar antes de barrer

Del capítulo 2, ahora como norma operativa. Un modelo con 6 parámetros
dimensionales que se reduce a 2 grupos π supone la diferencia entre $10^6$ y
$10^2$ simulaciones para una rejilla de 10 puntos por eje. **Cuatro órdenes de
magnitud, por hacer álgebra veinte minutos.**

Y hay una segunda ventaja, menos obvia: barrer en variables adimensionales
garantiza que **no repites el mismo caso físico** con distintas etiquetas. En
un barrido dimensional, la mitad de los puntos suelen ser el mismo problema.

### 4.3 Cómo se muestrea un espacio de parámetros

![Tres formas de elegir 25 puntos. Arriba: la distribución en el plano. Abajo: la proyección sobre el primer parámetro. Lo que hay que concluir: la rejilla explora sólo 5 valores distintos de cada parámetro con 25 simulaciones; el hipercubo latino explora 25.](figuras/fig_muestreo_parametros.pdf)

Esa es la razón por la que la rejilla es mala, y no es la que suele darse.
El problema no es sólo que $n^d$ crezca deprisa: es que **cada simulación
aporta poquísima información marginal**. Con 25 simulaciones en rejilla sólo
pruebas 5 valores distintos de cada parámetro; con hipercubo latino, 25.

Cuando el modelo depende fuertemente de un parámetro y poco de otro —que es lo
habitual—, la diferencia es enorme: la rejilla desperdicia el 80 % del
presupuesto repitiendo valores del parámetro importante.

**Recomendación práctica, por orden:** hipercubo latino para exploración
inicial; secuencias de Sobol si vas a calcular índices de sensibilidad;
rejilla sólo con 1 o 2 parámetros y cuando quieras dibujar un mapa.

### 4.4 Reproducibilidad: el mínimo aceptable

Un resultado que no se puede reproducir no es un resultado. Lo mínimo, por
orden de coste creciente:

1. **Semilla fija y explícita** en todo lo estocástico. Una línea.
2. **Versiones registradas** de Python y de cada biblioteca. Un fichero.
3. **Parámetros en un fichero de configuración**, no dispersos por el código.
4. **Un script que reproduzca cada figura** desde cero, sin pasos manuales.
5. **Datos intermedios guardados** con la configuración que los generó.
6. **Control de versiones**, incluidos los scripts de análisis.

Este libro sigue esa norma: cada figura tiene su script, con su semilla, y se
regenera con una orden. No es un adorno de estilo. Es que **un resultado que
sólo existe en la carpeta de descargas de alguien es un rumor**.

### 4.5 Probar código científico

`assert resultado > 0` no es una prueba. Las que sirven, en orden de valor:

**Soluciones analíticas conocidas.** Casos límite con respuesta cerrada. Si tu
código de fluidos no reproduce Poiseuille, no hace falta seguir.

**Órdenes de convergencia.** Del capítulo 8: `log2(e(h)/e(h/2))`. Detecta la
mitad de los errores de implementación.

**Soluciones manufacturadas.** Elige una solución, calcula qué término fuente
la haría exacta, comprueba que la recuperas. Verifica **también** los bordes.

**Invariancias y conservaciones.** Cambia unidades, gira los ejes, permuta el
orden de las partículas, invierte el tiempo. La física no debe cambiar.

**Casos degenerados.** Un solo elemento, tiempo cero, parámetro nulo, dominio
simétrico. Suelen romper el código y son baratísimos de probar.

**Pruebas de regresión.** Guarda la salida de un caso pequeño y compárala en
cada cambio. Detecta las roturas accidentales, que son la mayoría.

### 4.6 Visualizar para descubrir y visualizar para comunicar

Son dos actividades distintas y se hacen con criterios opuestos.

**Para descubrir:** rápido, feo, mucho de todo. Dibuja todo lo que se te ocurra,
en escalas logarítmicas, con residuos, con diferencias. El objetivo es que algo
te llame la atención.

**Para comunicar:** una figura, una pregunta. Con unidades, con anotación, con
línea de referencia. El objetivo es que el lector llegue a **una** conclusión.

El error habitual es publicar la primera. Una figura de descubrimiento tiene
seis paneles porque el autor no sabía qué buscaba; el lector no tiene por qué
pasar por esa búsqueda.

---

## 5. El ordenador entra en escena

::: antes
Vamos a comprobar si la recurrencia FPU es real o numérica. Antes:

* ¿Qué esperas que pase con Euler explícito?
* ¿Cómo distinguirías una recurrencia física de una periodicidad del
  integrador?
* Si duplicas la no linealidad $\alpha$, ¿la recurrencia se mantiene?
:::

```python
# Verlet de velocidades: conserva el volumen de fases (capítulo 8)
for paso in range(pasos):
    v += 0.5 * dt * a
    x += dt * v
    a = fuerzas(x)
    v += 0.5 * dt * a
```

::: juega
1. Sustituye Verlet por Euler explícito con el mismo paso. ¿Sobrevive la
   recurrencia?
2. Sube $\alpha$ de 0,25 a 1,5. ¿Se mantiene? (Hay un umbral por encima del
   cual el sistema **sí** termaliza: es el resultado de Izrailev y Chirikov,
   1966.)
3. Empieza con la energía en el modo 10 en vez de en el 1. ¿Cambia el tiempo de
   recurrencia?
4. Aumenta $N$ de 32 a 128 manteniendo la densidad de energía. ¿Qué le pasa al
   tiempo de recurrencia?
:::

---

## 6. ¿Qué estamos suponiendo?

::: supuestos
1. **Que el código hace lo que creemos.** Es el supuesto menos verificado de
   toda la ciencia computacional.
2. **Que el resultado no es un artefacto numérico.** Requiere las
   comprobaciones del capítulo 15.
3. **Que la simulación es representativa.** Un caso no es un teorema, y el
   espacio de parámetros explorado casi nunca es el relevante.
4. **Que el generador aleatorio es adecuado** y que las semillas son
   independientes entre realizaciones.
5. **Que la precisión numérica basta** para el fenómeno observado.
:::

---

## 7. ¿Cuándo falla?

::: falla
**Falla mirar sin predecir.** El resultado más frecuente de «probemos a ver qué
sale» es una carpeta con doscientas gráficas y ninguna conclusión.

**Falla barrer sin adimensionalizar.** Se gastan meses de CPU explorando
familias de casos que son el mismo caso.

**Falla el código sin pruebas.** Y falla en silencio: produce números.

**Falla la simulación como sustituto del experimento.** Si tu modelo no
incluye un mecanismo, ninguna cantidad de simulación lo descubrirá. Las
simulaciones sólo pueden revelar consecuencias inesperadas de lo que ya has
puesto dentro —que, como muestra FPU, no es poco—.

**Falla la irreproducibilidad.** Un resultado que sólo funciona en la máquina
de su autor, con su versión de las bibliotecas, no es utilizable ni criticable.
:::

### Un anti-ejemplo: el barrido de 200 000 simulaciones

Un equipo explora un modelo de 6 parámetros con una rejilla de 8 puntos por
eje: 262 144 simulaciones, tres semanas de clúster. El resultado es una tabla
enorme y ninguna conclusión clara.

Dos errores, ambos evitables en una tarde de trabajo previo. Primero: el modelo
se reducía a **tres** grupos adimensionales, así que la mitad de los casos eran
físicamente idénticos a otros. Segundo: con 8 puntos por eje sólo se prueban 8
valores distintos de cada parámetro; un hipercubo latino de 2000 puntos habría
dado 2000 valores de cada uno, con 130 veces menos coste.

Y hay un tercer error, más grave: no se hizo ningún análisis de sensibilidad
previo. Con 200 evaluaciones baratas se habría visto que dos de los seis
parámetros explicaban el 90 % de la varianza, y el barrido se podría haber
concentrado en ellos.

**Veinte minutos de análisis dimensional y doscientas simulaciones
exploratorias habrían ahorrado tres semanas.**

---

## 8. Historia

::: historia
**Fermi, Pasta, Ulam, Tsingou y el informe que nadie publicó** ·
*Nivel de verificación: A.*

En 1953–1954, en Los Álamos, se planteó una pregunta que parecía tener
respuesta segura. Una cadena de osciladores acoplados **linealmente** no
termaliza: cada modo normal conserva su energía para siempre (capítulo 11). Se
creía que bastaba una no linealidad pequeña para que la energía se repartiera
por igual entre todos los modos, que es lo que exige la mecánica estadística
para justificar la termodinámica.

El MANIAC I permitía por primera vez comprobarlo. **Mary Tsingou programó el
cálculo.** El resultado fue el de la figura: la energía visitaba unos pocos
modos y volvía casi entera al inicial.

El informe LA-1940 (1955) lo describe sin adornos: el resultado era inesperado
y no tenían explicación. Fermi murió en noviembre de 1954, antes de que el
informe se distribuyera; según Ulam, lo consideraba uno de los trabajos más
interesantes en los que había participado.

**Sobre la autoría.** El informe se firma Fermi, Pasta y Ulam. En los
agradecimientos aparece «hemos disfrutado de la eficiente cooperación de la
señora Mary Tsingou» en la programación. Durante cincuenta años el problema se
llamó FPU. En 2008, Thierry Dauxois publicó en *Physics Today* un artículo
recuperando su papel, y desde entonces se usa cada vez más **FPUT**.

Merece detenerse en lo que significaba «programar» en 1954: no era teclear una
fórmula, era diseñar el flujo de operaciones de una máquina sin lenguaje de
alto nivel, gestionar la aritmética de precisión limitada y decidir cómo
comprobar que el resultado no era un error de la máquina. Es decir: **parte
sustancial del diseño del experimento**.

**Lo que salió de ahí.** En 1965, Norman Zabusky y Martin Kruskal estudiaron el
límite continuo del problema, encontraron la ecuación de Korteweg–de Vries y
descubrieron que sus soluciones —a las que llamaron **solitones**— atraviesan
otras sin deformarse. Eso explicaba la recurrencia y abrió un campo entero, del
que salen las fibras ópticas de comunicaciones actuales.

Y en 1966, Izrailev y Chirikov demostraron que **por encima de cierta
no linealidad el sistema sí termaliza**. La paradoja FPU no era una excepción a
la mecánica estadística: era un régimen distinto, y encontrar la frontera entre
ambos ocupó décadas.

Todo eso salió de un experimento numérico que no confirmó lo esperado, y de que
sus autores lo publicaran diciendo justamente eso.
:::

---

## 9. Problemas

En `problemas.md`; soluciones en `soluciones.md`.

---

## 10. Experimento computacional

::: experimento
**Haz reproducible un resultado tuyo.**

*Pregunta:* ¿podría otra persona regenerar tu último resultado sin hablar
contigo?

*Diseño.* Coge un resultado tuyo de los últimos meses. Crea una carpeta limpia
y reconstrúyelo desde cero: datos, código, configuración, figura.

*Análisis.* Cronometra cuánto tardas y anota cada vez que tienes que recordar
algo que no estaba escrito (un parámetro, un paso de limpieza, una versión, un
fichero que se generó a mano).

*Criterio:* debería costar una orden y menos de diez minutos.

*Qué falsaría tu confianza:* si tú, que lo hiciste, no puedes reproducirlo en
una hora, nadie más podrá nunca. Y si al reproducirlo sale **distinto**, ya
tienes un problema mucho más urgente que la reproducibilidad.
:::

---

## 11. Explícalo

::: explica
1. ¿En qué se parece y en qué se diferencia una simulación de un experimento?
2. ¿Por qué escribir la predicción antes de ejecutar cambia lo que aprendes?
3. ¿Por qué una rejilla es mala forma de explorar un espacio de parámetros?
4. ¿Qué prueba escribirías para un código que resuelve una ecuación cuya
   solución no conoces?
5. ¿Por qué el resultado de FPU abrió más ciencia que uno que hubiera
   confirmado la equipartición?
6. ¿Qué significa que un resultado sea reproducible, exactamente?
:::

---

## 12. Lo esencial

::: esencial
* Una simulación no es un experimento ni una demostración: es un instrumento
  para falsar intuiciones.
* Predicción escrita antes de ejecutar; explicación antes de seguir. Sin eso,
  se acumulan gráficas y no conocimiento.
* Adimensionaliza antes de barrer. Cuatro órdenes de magnitud por veinte
  minutos de álgebra.
* La rejilla no sólo escala mal: desperdicia el presupuesto repitiendo valores.
  Usa hipercubo latino o Sobol.
* Semilla, versiones, configuración, un script por figura. Un resultado no
  reproducible es un rumor.
* Prueba con soluciones conocidas, órdenes de convergencia, soluciones
  manufacturadas, invariancias y casos degenerados.
* Visualizar para descubrir y para comunicar son actividades opuestas.
* El resultado que no esperabas es el valioso, **si lo publicas diciendo que
  no lo esperabas**.
:::

---

## 13. Preguntas que quedan abiertas

::: abierto
* ¿Cuándo una simulación constituye evidencia, y de qué exactamente?
* Si el código es demasiado complejo para ser leído por una persona, ¿qué
  significa «verificarlo»?
* ¿Cuántas simulaciones hacen falta para afirmar que un fenómeno es genérico y
  no una casualidad de los parámetros elegidos?
* La reproducibilidad exacta bit a bit es imposible con paralelismo y coma
  flotante. ¿Qué nivel de reproducibilidad es el correcto?
* Si un modelo de aprendizaje automático descubre un patrón que no sabemos
  explicar, ¿es un descubrimiento?
:::
