# III.2 — Cómo elegir variables

---

## El problema

Un modelo empieza con una decisión que casi nadie declara: **qué se pone y qué
se deja fuera**. Esa decisión determina todo lo demás, y es la que más veces
arruina un trabajo.

---

## Cuatro preguntas, en orden

### 1. ¿Qué quiero predecir?

La variable de salida define el problema. «Modelar el sistema» no es un
objetivo; «predecir la temperatura del centro a los 10 minutos con ±1 °C» sí.

Y hay una consecuencia inmediata: **el mismo sistema exige modelos distintos
para preguntas distintas**. Un modelo de un motor para predecir consumo, para
predecir vibración y para predecir vida útil no comparten variables.

### 2. ¿De qué depende esa salida?

Haz la lista larga primero, sin filtrar. Incluye lo que te parezca absurdo: es
más fácil tachar después que recordar más tarde.

Después, para cada candidata, la pregunta operativa: **si esta variable
cambiara un factor 2, ¿cambiaría la salida de forma apreciable?** Si la
respuesta es no, fuera. Si es «no lo sé», queda dentro hasta que lo sepas.

### 3. ¿Cuáles son realmente independientes?

Dos errores frecuentes y opuestos:

* **Redundancia.** Incluir masa, volumen y densidad cuando sólo dos son libres.
  Produce parámetros no identificables (capítulo 10).
* **Ocultar una dependencia.** Tratar como constantes cosas que dependen de la
  variable de salida. Un $h$ «constante» que en realidad depende de $\Delta T$
  es el ejemplo del capítulo II.2.

### 4. ¿Cuántas quedan al adimensionalizar?

Capítulo 2. Este paso es obligatorio y casi nadie lo hace. Reduce el número de
parámetros a $n-k$, y con frecuencia revela que dos variables que parecían
independientes sólo aparecen en una combinación.

---

## Los descartes se escriben

La lista de lo que has dejado fuera, **con el motivo cuantitativo de cada
descarte**, es tan parte del modelo como las ecuaciones. Sirve para tres cosas:

* Cuando el modelo falla, es la primera lista que se revisa.
* Cuando alguien pregunta «¿y no habría que incluir…?», la respuesta ya está
  escrita.
* Cuando cambia el régimen de operación, se revisa si los descartes siguen
  valiendo. Casi nunca se hace, y es la causa más común de que un modelo
  fiable deje de serlo.

Formato recomendado:

```text
DESCARTADA: rugosidad de la superficie
MOTIVO: afecta a h en menos de un 5 % para Re < 10^4
VÁLIDO MIENTRAS: Re < 10^4 y no haya incrustaciones
```

---

## Elegir bien las variables: cuatro criterios

**Físicas antes que ajustables.** Una variable con significado físico se puede
medir, acotar y contrastar. Un parámetro de ajuste, no. Si tu modelo tiene un
«factor de corrección», pregúntate qué representa.

**Medibles antes que fundamentales.** De poco sirve un modelo cuyo parámetro
clave nadie sabe medir. A veces conviene reparametrizar en términos de algo
observable, aunque sea menos elegante.

**Combinaciones antes que variables sueltas.** Si el análisis dimensional dice
que sólo aparece $\rho v^2/E$, usa esa combinación como variable. Los ajustes
serán mejor condicionados (capítulo 11).

**Poques antes que muchas.** Cada variable adicional multiplica el espacio de
parámetros y divide la información por dato. Con 50 datos, cinco parámetros ya
es mucho.

---

## Lista de comprobación

```text
ELECCIÓN DE VARIABLES

□ ¿Cuál es exactamente la salida, con unidades y precisión?
□ ¿He hecho la lista larga sin filtrar?
□ Para cada candidata: si cambia un factor 2, ¿cambia la salida?
□ ¿Hay redundancias (tres variables donde hay dos grados de libertad)?
□ ¿Hay alguna «constante» que dependa de la salida?
□ ¿He adimensionalizado? ¿Cuántos parámetros quedan?
□ ¿He escrito los descartes con su motivo cuantitativo y su rango de validez?
□ ¿Son mis variables medibles? ¿Físicas o de ajuste?
□ ¿Cuántos datos tengo por parámetro?
```

---

## Ejercicios de campo

**A.** Coge un modelo que uses y escribe, por primera vez, su lista de
descartes con motivos cuantitativos. Cuenta cuántos puedes justificar de verdad.

**B.** Toma un modelo publicado de tu campo y adimensionalízalo. ¿Cuántos
parámetros quedan? ¿Lo hicieron los autores?

**C.** Elige un fenómeno cotidiano y haz dos modelos con salidas distintas
—por ejemplo, de una lavadora: consumo de agua y duración del ciclo—. Comprueba
que las listas de variables apenas se solapan.

---

### Referencias

* **Lin, C. C. y Segel, L. A.** *Mathematics Applied to Deterministic Problems
  in the Natural Sciences.* SIAM, 1988, parte I.
* **Barenblatt, G. I.** *Scaling.* Cambridge UP, 2003, capítulos 1–2.
* **Transtrum, M. et al.** *Perspective: Sloppiness and emergent theories.*
  J. Chem. Phys. **143** (2015). Por qué pocos parámetros bien elegidos baten a
  muchos.
