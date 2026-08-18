# III.13 — Cómo usar IA sin externalizar tu pensamiento

> Este capítulo cierra el libro, y no por casualidad. Todo lo anterior entrena
> una capacidad que hoy se puede delegar con un clic. La pregunta no es si
> delegarla —sería absurdo no usar la herramienta— sino **qué parte**.

---

## 1. El problema, planteado con precisión

No es que la IA se equivoque. Se equivoca menos que hace dos años y seguirá
mejorando.

El problema es más incómodo: **la IA es extraordinaria ejecutando y buena
formulando, y formular es exactamente la habilidad que este libro entrena**.

Y hay una asimetría que lo agrava. Cuando delegas la ejecución, sigues sabiendo
si el resultado es razonable, porque tienes el criterio. Cuando delegas la
formulación, **pierdes la capacidad de juzgar la respuesta**, y esa pérdida no
se nota: obtienes algo plausible, bien escrito y con la estructura correcta.

La palabra clave es *plausible*. Un modelo de lenguaje produce texto que se
parece al que produciría alguien que sabe. Distinguir eso de saber requiere,
precisamente, saber.

---

## 2. Lo que hace bien y lo que hace mal

Esto cambia deprisa, así que interesan las **categorías**, no la lista.

**Hace muy bien:**

* Implementar algo que ya has especificado.
* Traducir entre lenguajes, formatos y notaciones.
* Recordar sintaxis, API y fórmulas estándar.
* Generar alternativas para que elijas.
* Encontrar errores en código y en razonamientos que le presentas.
* Explicarte un concepto estándar a tu nivel.
* Buscar y resumir literatura, con verificación.

**Hace peor de lo que parece:**

* Decidir **qué** problema hay que resolver.
* Decidir qué precisión hace falta.
* Saber qué se puede despreciar en tu caso concreto.
* Estimar órdenes de magnitud sin datos (produce números plausibles y
  frecuentemente erróneos, sin señalar cuáles).
* Decirte cuándo su respuesta está fuera de su competencia.
* Distinguir lo que sabe de lo que interpola.

Esa última es la crítica: **no hay una señal fiable de incertidumbre**. Una
respuesta correcta y una inventada llegan con el mismo tono.

---

## 3. El protocolo de tres fases

Es la propuesta operativa del capítulo, y funciona.

### Fase 1 — Humano, y a solas

Antes de abrir ninguna herramienta, y durante al menos veinte minutos:

* **Formula el problema.** Una frase, con unidades y precisión.
* **Estima el orden de magnitud.** Con tus cotas, aunque sean malas.
* **Identifica las variables**, y escribe los descartes con su motivo.
* **Propón un modelo mínimo.**
* **Intenta una derivación**, aunque no la termines.
* **Anticipa el resultado.** Escribe qué número esperas y en qué dirección
  crees que fallará tu modelo.

Todo eso se escribe. En el cuaderno del modelador, con la plantilla del
apéndice G.

### Fase 2 — Con la herramienta

Ahora sí, y con instrucciones concretas:

* **Contrastar:** «he estimado X por este camino; ¿qué falla en mi
  razonamiento?»
* **Buscar errores:** dale tu derivación y pídele que la refute.
* **Generar alternativas:** «¿qué otros tres modelos podrían describir esto, y
  en qué se diferenciarían sus predicciones?»
* **Implementar:** lo que ya has especificado.
* **Encontrar referencias:** y después **verificarlas una a una**.
* **Ampliar:** «¿qué mecanismo he podido pasar por alto?»

Lo que **no** se le pide en esta fase: la respuesta.

### Fase 3 — Humano otra vez

Y esta fase es la que casi nadie hace:

* ¿Qué me creo de lo que ha dicho, y **por qué**?
* ¿Qué supuestos ha introducido sin decirlo?
* ¿Coincide con mi estimación de la fase 1? Si no, **¿quién está equivocado y
  cómo lo compruebo?**
* ¿Qué comprobación independiente puedo hacer?
* ¿Qué he aprendido que sea transferible al próximo problema?

Esa última pregunta es la que distingue usar la herramienta de depender de
ella.

---

## 4. Los cuatro modos de fallo

**Anclaje.** Una vez que has visto una respuesta, es muy difícil pensar en otra
dirección. Por eso la fase 1 tiene que ser previa y no simultánea: leer primero
y estimar después no es lo mismo, y produce estimaciones sesgadas hacia lo
leído.

**Plausibilidad sin verdad.** Una derivación con la estructura correcta y un
paso mal. Es especialmente difícil de detectar porque **todo lo demás está
bien**, y el ojo se relaja.

**Erosión del criterio.** No se pierde en un día. Se pierde por no haber hecho
las estimaciones durante meses, y se nota cuando llega un problema en el que la
herramienta no ayuda.

**Referencias fabricadas.** El modo de fallo más documentado y el más fácil de
evitar: **comprueba todas las citas**. Título, autores, año, revista, y que
diga lo que se afirma que dice. Este libro las ha verificado una a una, y ese
proceso encontró errores.

---

## 5. La regla de los veinte minutos

Si te quedas con una sola cosa de este capítulo:

> **Los primeros veinte minutos de cada problema son tuyos.** Sin buscador, sin
> IA, sin mirar la solución.

No es ascetismo. Es que en esos veinte minutos ocurren tres cosas que no
ocurren después:

1. **Construyes el criterio** que te permitirá juzgar cualquier respuesta que
   llegue luego.
2. **Descubres qué no sabes**, que es información valiosísima y que la respuesta
   correcta borra inmediatamente.
3. **Instalas el hábito.** La capacidad de formular no se mantiene sola: se
   atrofia si no se usa, y no hay manera de reactivarla en el momento en que la
   necesitas.

Veinte minutos al día son ochenta horas al año. Es suficiente.

---

## 6. Cuándo saltarse el protocolo

Sería una tontería no decirlo: hay situaciones donde el protocolo es
contraproducente.

* **Cuando el problema es puramente de ejecución.** Convertir un formato,
  recordar una sintaxis, escribir un script de una vez. Delegar entero.
* **Cuando estás explorando un campo nuevo** y necesitas orientarte antes de
  poder formular nada útil. Ahí la herramienta es un buen mapa, verificando.
* **Cuando hay una urgencia real.** Pero conviene notar cuántas urgencias lo son
  de verdad.

La distinción operativa: **¿es esto algo que quiero saber hacer, o algo que
quiero que esté hecho?** Delegar lo segundo es eficiencia. Delegar lo primero,
sistemáticamente, es renunciar.

---

## 7. Historia

::: historia
**El argumento tiene precedentes, y conviene conocerlos** ·
*Nivel de verificación: A y B.*

Platón, en el *Fedro*, hace decir a Sócrates que la escritura producirá olvido
en las almas de quienes la aprendan, porque confiarán en los caracteres
externos en lugar de recordar desde dentro. El argumento tiene 2400 años y es
literalmente el de este capítulo, aplicado a una tecnología que resultó ser
espectacularmente beneficiosa.

Se repitió con la imprenta, con la calculadora de bolsillo —hubo un debate real
y prolongado sobre si arruinaría el cálculo mental— y con los buscadores.

En todos los casos ocurrieron **dos** cosas: la capacidad delegada se atrofió
de verdad, y a cambio se liberó atención para otra cosa. Poca gente calcula hoy
raíces cuadradas a mano, y no parece haber sido una tragedia.

**Y por eso el argumento de este capítulo no es «no delegues».** Es más
específico: distingue entre delegar **ejecución** —que es lo que ocurrió con
la calculadora— y delegar **formulación**, que es cualitativamente distinto
porque es donde reside la capacidad de juzgar el resultado.

Un ejemplo empírico reciente y honesto: los estudios sobre asistentes de
programación muestran ganancias claras de productividad en tareas de ejecución
y resultados mixtos —a veces negativos— en tareas donde el programador tiene
que entender un sistema complejo. La distinción ejecución/comprensión aparece en
los datos.

**La cautela obligatoria:** este apartado se escribe en 2026 sobre una
tecnología que cambia cada pocos meses. Los datos empíricos son escasos y de
corto plazo. Lo que sí es sólido es el mecanismo psicológico del anclaje, que
está bien documentado desde Tversky y Kahneman (1974) y no depende de la
tecnología.
:::

---

## 8. Lista de comprobación

```text
USO DE IA

Antes (20 minutos, a solas):
□ ¿He escrito la pregunta con unidades y precisión?
□ ¿He estimado el orden de magnitud?
□ ¿He escrito variables y descartes?
□ ¿He propuesto un modelo mínimo?
□ ¿He anticipado el resultado por escrito?

Durante:
□ ¿Le estoy pidiendo contraste, no respuesta?
□ ¿Le he pedido que refute mi razonamiento?
□ ¿Le he pedido alternativas y sus predicciones distintas?

Después:
□ ¿Qué me creo y por qué?
□ ¿Qué supuestos ha introducido sin decirlo?
□ ¿Coincide con mi estimación previa? Si no, ¿quién falla y cómo lo compruebo?
□ ¿He verificado TODAS las referencias?
□ ¿Qué he aprendido que sea transferible?

Meta, una vez al mes:
□ ¿Cuántas estimaciones he hecho yo este mes, sin ayuda?
□ ¿Sigo pudiendo formular un problema desde cero?
```

---

## 9. Ejercicios de campo

**A.** Durante una semana, cronometra literalmente los veinte minutos antes de
consultar nada. Anota cuántas veces resolviste el problema dentro de ese plazo.

**B.** Coge un problema, estímalo tú y pídeselo también a la herramienta.
Compara. Cuando discrepéis, **averigua quién tiene razón**, y anota el resultado
de esa investigación: es donde está el aprendizaje.

**C.** Pídele una lista de diez referencias sobre un tema que conozcas.
Verifícalas una a una. Anota la tasa de error. Repite dentro de seis meses.

**D.** Escribe un problema que estés seguro de que la herramienta hará mal, y
compruébalo. Si aciertas, has identificado el límite; si fallas, has aprendido
algo sobre la herramienta. Las dos cosas valen.

---

## 10. Lo esencial

::: esencial
* La IA es extraordinaria ejecutando y buena formulando. Formular es la
  habilidad que este libro entrena.
* Delegar la ejecución conserva tu criterio. Delegar la formulación lo destruye,
  y la pérdida no se nota.
* No hay señal fiable de incertidumbre: lo correcto y lo inventado llegan con
  el mismo tono.
* Protocolo de tres fases: formula tú, contrasta con la herramienta, decide tú.
* Cuatro modos de fallo: anclaje, plausibilidad sin verdad, erosión del
  criterio, referencias fabricadas.
* La regla de los veinte minutos. Ochenta horas al año, y es suficiente.
* La pregunta operativa: **¿quiero saber hacer esto, o quiero que esté hecho?**
:::

---

## 11. Preguntas abiertas

::: abierto
* ¿Se puede medir la erosión del criterio, o sólo se detecta cuando ya ha
  ocurrido?
* ¿Cambia el argumento si las herramientas empiezan a señalar de forma fiable
  su propia incertidumbre?
* ¿Qué habilidades merece la pena mantener y cuáles conviene dejar ir? La
  respuesta con la calculadora resultó ser «déjalas ir». ¿Por qué sería distinta
  aquí?
* Si un sistema propone un modelo que funciona y nadie entiende por qué, ¿es
  conocimiento?
:::

---

### Referencias

* **Platón.** *Fedro*, 274c–275b. El argumento original.
* **Tversky, Amos y Kahneman, Daniel.** *Judgment under Uncertainty: Heuristics
  and Biases.* Science **185** (1974), 1124–1131. El anclaje, documentado.
* **Sparrow, B.; Liu, J.; Wegner, D.** *Google Effects on Memory.* Science
  **333** (2011), 776–778. Memoria transactiva y buscadores.
* **Peng, S. et al.** *The Impact of AI on Developer Productivity.*
  arXiv:2302.06590, 2023. Ganancias en tareas de ejecución.
* **Bainbridge, Lisanne.** *Ironies of Automation.* Automatica **19** (1983),
  775–779. **La referencia más importante de este capítulo**, y es de 1983:
  automatizar las partes fáciles deja al humano sólo las difíciles, y sin
  práctica para hacerlas.
* **Parasuraman, Raja y Riley, Victor.** *Humans and Automation: Use, Misuse,
  Disuse, Abuse.* Human Factors **39** (1997), 230–253. El marco clásico sobre
  cuándo la gente confía de más y de menos en un sistema automático.
* **Casner, Stephen M. et al.** *The Retention of Manual Flying Skills in the
  Automated Cockpit.* Human Factors **56** (2014), 1506–1516. Erosión de
  habilidad medida, no supuesta: los pilotos conservan el control motor y
  pierden la capacidad de saber qué hace el avión.
* **Tsai, T. L.; Fridsma, D. B.; Gatti, G.** *Computer decision support as a
  source of interpretation error: the case of electrocardiograms.* JAMIA **10**
  (2003), 478–483. Una sugerencia automática equivocada empeora el diagnóstico
  del médico respecto a no tener ninguna.
