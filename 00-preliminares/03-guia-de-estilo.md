# Guía de estilo

*Documento de diseño (fase 4): las reglas de voz, densidad y formato que este libro se impone, escritas para poder comprobarlas.*

> Reglas concretas y verificables. Una guía de estilo que dice «sé claro» no
> sirve para nada. Todo lo que hay aquí se puede comprobar leyendo un párrafo.

---

## 1. Voz

**Persona.** Primera del plural cuando pensamos juntos («vamos a estimar»,
«supongamos»). Segunda del singular cuando se pide acción («antes de seguir,
apunta tu número»). Primera del singular sólo para opiniones asumidas («creo que
este modelo se usa más de lo que se justifica»). Nunca la pasiva refleja
impersonal como muletilla: *«se puede observar que»* → *«fíjate en que»*.

**Español de España.** Vosotros no aparece porque el interlocutor es una sola
persona. Sí se usan giros peninsulares naturales («no da la talla», «a ojo»,
«sale a cuenta»). Nada de neutro latinoamericano, nada de calcos del inglés
(*asumir* por *suponer*, *eventualmente* por *finalmente*, *consistente* por
*coherente*).

**Registro.** Adulto, técnico, coloquial cuando conviene. Se permite una
irreverencia cada dos o tres páginas, nunca dos seguidas. La ironía se dirige a
las ideas y a los métodos, jamás al lector.

### Prohibiciones explícitas

| Prohibido | Motivo | Sustituto |
|---|---|---|
| «La ciencia es maravillosa / fascinante» | Afirma lo que debería demostrar | Enseña el resultado que produce esa sensación |
| «Como todos sabemos» | Excluye o condesciende | Se elimina, o «puede que recuerdes» |
| «Simplemente», «basta con», «trivialmente» | Casi siempre mentira | Se elimina o se explica |
| «Se puede demostrar que» sin referencia | Es una deuda impagada | Se demuestra o se da la fuente exacta |
| «Dejamos como ejercicio al lector» sin pista | Pereza disfrazada | Se convierte en ejercicio con pista graduada |
| «En el mundo real…» | Sugiere que el resto es de mentira | Se nombra el contexto concreto |
| Emojis, exclamaciones múltiples, mayúsculas de énfasis | Ruido | Cursiva, y con moderación |
| Motivación genérica de arranque | Se salta siempre | Empezar por el fenómeno |

### Frases de transición canónicas

Sirven para marcar en qué punto del ciclo estamos y deben aparecer literalmente:

* «Antes de calcular nada: ¿qué orden de magnitud esperas?»
* «Vamos a escribir lo que estamos suponiendo.»
* «¿Qué término domina aquí?»
* «Aquí es donde el ordenador empieza a servir para algo.»
* «Predicción antes de ejecutar: apunta qué esperas ver.»
* «¿Ocurrió? ¿Por qué?»
* «¿En qué límite deja esto de tener sentido?»
* «Volvemos a la taza de café, ahora con una herramienta que antes no
  teníamos.»

---

## 2. Densidad matemática

**Regla de oro:** tanta matemática como permita pensar mejor, no tanta como sea
posible escribir.

* **Todo paso no evidente se muestra.** Si hay que saltar, se dice qué se salta y
  dónde está: *«el paso intermedio es una integración por partes; si no te sale,
  está en el apéndice A.4»*.
* **Máximo tres ecuaciones numeradas seguidas** sin texto en medio. Si hacen
  falta más, el desarrollo va a una caja de herramientas.
* **Toda ecuación importante se lee en voz alta** inmediatamente después, en
  lenguaje natural: *«la tasa de cambio de la temperatura es proporcional a lo
  lejos que estás del ambiente»*.
* **Toda ecuación importante se comprueba dimensionalmente** al menos una vez.
* **Notación estable en todo el libro:**

| Símbolo | Significado fijo |
|---|---|
| $x, \mathbf{x}$ | estado del sistema |
| $t$ | tiempo; $\tau$ tiempo característico |
| $\theta$ | vector de parámetros a estimar |
| $\varepsilon$ | parámetro pequeño (perturbaciones) |
| $\sigma$ | desviación típica; $\sigma_N=\sqrt N$ en conteos |
| $N$ | número de muestras/sucesos; $n$ tamaño de una malla |
| $\hat{\cdot}$ | estimador |
| $\sim$ | «del orden de»; $\approx$ «aproximadamente igual»; $\propto$ «proporcional a» |
| $\mathcal{O}(\cdot)$ | orden asintótico (nunca «complejidad» sin decirlo) |

* **Se distingue siempre** entre $\sim$ (mismo orden de magnitud) y $\approx$
  (mismo valor con un error pequeño). Confundirlos es el error de honestidad más
  frecuente en la literatura de estimación.

---

## 3. Longitud y ritmo

| Unidad | Objetivo | Máximo duro |
|---|---|---|
| Párrafo | 3–6 líneas | 8 líneas |
| Sección (`##`) | 400–900 palabras | 1400 |
| Subsección (`###`) | 150–400 palabras | 700 |
| Capítulo Parte I | 4000–6000 palabras | 8000 |
| Capítulo Parte II | 2500–4000 palabras | 5500 |
| Capítulo Parte III | 1500–2500 palabras | 3500 |
| Interludio | 800–1800 palabras | 2200 |
| Bloque de código | 15–40 líneas | 60 |

**Regla del respiro:** no más de dos páginas seguidas de prosa continua sin una
ecuación destacada, una figura, una caja o una lista. Y a la inversa: no más de
dos elementos gráficos seguidos sin prosa que los explique.

**Regla de apertura:** los tres primeros párrafos de un capítulo contienen (a) un
fenómeno concreto y observable, (b) una pregunta cuantitativa que el lector no
sabe responder todavía y (c) la promesa explícita de lo que sabrá hacer al
terminar. Nada más. Ninguna definición en la primera página.

---

## 4. Uso de la historia

**Función.** Toda historia responde a la pregunta *«¿qué problema tenía esta
persona y qué hizo cuando se atascó?»*. Si sólo aporta color, se corta.

**Reglas duras:**

1. **Nivel de verificación explícito.** A (fuente primaria), B (secundaria
   fiable, con matiz), C (folclore). El nivel C se presenta *como* folclore:
   «se cuenta que…», «la atribución es dudosa».
2. **Nunca se inventan diálogos.** Si no hay transcripción, se parafrasea y se
   dice que se parafrasea.
3. **Nunca se atribuye una frase sin fuente.** Y si la fuente es dudosa, se dice.
4. **Se muestran versiones discrepantes** cuando existen: «la versión que circula
   dice X; los documentos de la época dicen Y».
5. **Se nombra a quien hizo el trabajo**, no sólo a quien firmó. Arianna
   Rosenbluth, Mary Tsingou, los computistas humanos.
6. **Se muestra el error.** Cada personaje recurrente aparece al menos una vez
   equivocándose.
7. **Extensión:** dentro de un capítulo, la sección histórica ocupa entre el 8 %
   y el 15 % del texto. Si crece, se convierte en interludio.

**Cómo se cita en el texto.** Nota corta entre paréntesis con autor y año, y la
ficha completa en la sección *Referencias* del capítulo, que separa
**fuentes históricas**, **referencias técnicas** y **lecturas opcionales**.

---

## 5. Ejemplos

**Cuota de variedad.** Cada capítulo de la Parte I usa ejemplos de al menos tres
disciplinas, y al menos uno no es de física. Se anota en la cabecera del
capítulo y se audita al cierre.

**Jerarquía del ejemplo:** primero cotidiano y observable (una taza, una cola,
una gota), después profesional (un detector, un servidor, un reactor), después
histórico (la medida que hizo alguien). Nunca al revés.

**Números reales.** Todo ejemplo numérico usa magnitudes plausibles y citadas.
Nada de «supongamos que el coeficiente vale 3».

**Anti-ejemplos.** Al menos uno por capítulo: un caso donde la herramienta
recién aprendida da una respuesta incorrecta o engañosa.

---

## 6. Ejercicios

Diez categorías obligatorias por capítulo de la Parte I (al menos una de cada,
en este orden):

| Categoría | Qué entrena | Cuántos |
|---|---|---|
| **Calentamiento** | Aplicación directa, confianza | 2–4 |
| **Estimación** | Fermi, sin calculadora ni buscador | 2–4 |
| **Modelado** | No se da la ecuación | 2–3 |
| **Derivación** | Construir la matemática | 1–3 |
| **Computacional** | Implementar | 2–3 |
| **Experimento** | Barrer parámetros y observar | 1–2 |
| **Detective** | Encontrar el error en un resultado dado | 1–2 |
| **Mundo real** | Abierto, sin respuesta única | 1–2 |
| **Feynman** | Explicar sin ecuaciones | 1–2 |
| **Extensión** | Investigar más allá | 1–2 |

**Marcado de dificultad:** ○ directo · ◐ requiere pensar · ● difícil ·
★ abierto, sin solución cerrada.

**Reglas:** cada enunciado es autocontenido. Los problemas de estimación llevan
la instrucción explícita *«primero estima, después comprueba»*, y cuando procede,
*«no consultes nada durante los primeros 15 minutos»*. Los de la categoría
*Detective* incluyen datos o gráficas verosímiles y falsos.

**Soluciones.** Razonadas, nunca sólo el número. Los problemas ● y ★ llevan
**Pista 1 → Pista 2 → Solución**, separadas visualmente para que se puedan tapar.

---

## 7. Código

**Estética.** Python moderno, plano, legible en papel.

```python
# Cabecera obligatoria de todo script:
"""Qué pregunta responde esta figura o simulación.

Ejecutar:  python fig_velocidad_terminal.py
"""
```

**Reglas duras:**

1. Autocontenido: `python archivo.py` funciona sin argumentos.
2. Menos de 60 líneas salvo justificación escrita.
3. Sin clases salvo que haya estado real que mantener.
4. Semilla explícita en todo lo estocástico: `rng = np.random.default_rng(42)`.
5. Nombres en español para las variables del dominio (`temperatura`,
   `masa`, `paso`), en inglés para lo que es API (`np.linspace`, `axis=0`).
6. `typing` sólo cuando aclara una firma no obvia.
7. Constantes físicas con unidades en el comentario de la misma línea.
8. **Primero a mano, después con la biblioteca.** Se implementa RK4 y luego se
   compara con `solve_ivp`. La comparación es la lección, no un trámite.
9. Cada bloque de código del libro va seguido de **qué esperamos que imprima o
   dibuje**, antes de mostrarlo.

**Lo que no se hace:** `if __name__ == "__main__":` decorativo en scripts de 20
líneas; barras de progreso; logging; argparse salvo que el script sea una
herramienta de verdad; abstracciones «por si acaso».

---

## 8. Figuras

**Regla de oro: una figura responde una pregunta.** Si no se puede escribir esa
pregunta en el pie, la figura sobra.

**Anatomía obligatoria:**

* Título del eje **con unidades**, siempre.
* Pie de figura en dos partes: **qué se ve** y **qué hay que concluir**.
* Anotación dentro de los ejes señalando el punto que importa (una flecha con
  cuatro palabras vale más que un párrafo).
* Línea de referencia cuando exista un valor esperado (la predicción teórica, la
  ley de escala, el valor real).

**Prohibido:** 3D salvo que la tercera dimensión sea información; dos ejes y
gráficas distintas peleando por el mismo panel; leyendas de más de cuatro
entradas; mapas de color tipo arcoíris; gráficos de sectores; decoración.

**Paleta semántica fija** (definida en `herramientas/estilo_libro.py` y en el
preámbulo LaTeX, para que figura y texto coincidan):

| Color | Significado invariable |
|---|---|
| azul `#2F6FA8` | el modelo, la predicción |
| rojo `#C1443C` | los datos, la medida, el aviso |
| verde `#3F8F6B` | la teoría exacta, la coincidencia |
| ocre `#D99A2B` | la aproximación, el resaltado |
| gris `#8A94A6` | el contexto, la referencia, el ruido |
| tinta `#1B2A41` | ejes, texto, la verdad de referencia |

**Reproducibilidad:** toda figura tiene su script en `codigo/fig_*.py`, con el
mismo nombre que el archivo de salida. No hay ninguna imagen en el libro cuyo
origen no esté versionado.

**Tipos de figura que el libro prefiere:** convergencia frente a N en ejes log,
retratos de fase, residuos, diagramas de bifurcación, comprobaciones de leyes de
escala, bandas de incertidumbre, sensibilidad a parámetros, comparación
analítico/numérico, y diagramas conceptuales de flujo del modelo.

---

## 9. Cajas

Catálogo cerrado. No se inventan cajas nuevas sin añadirlas aquí y al preámbulo.

| Caja | Cuándo | Longitud |
|---|---|---|
| **Una pregunta** | Abre el capítulo | 2–5 líneas |
| **Antes de calcular** | Antes de cualquier resultado | 3–8 líneas |
| **Caja de herramientas matemática** | Repaso just-in-time | ½ página |
| **Historia** | Episodio documentado | ½–1 página |
| **Juega con el modelo** | Después de una simulación | 5–10 líneas |
| **¿Qué estamos suponiendo?** | Obligatoria en todo capítulo | lista de 4–8 puntos |
| **¿Cuándo falla?** | Obligatoria en todo capítulo | 5–12 líneas |
| **Trampa** | Error frecuente | 3–8 líneas |
| **Experimento computacional** | Proyecto pequeño de cierre | ½ página |
| **Explícalo sin esconderte…** | Preguntas Feynman | 4–7 preguntas |
| **Protocolo con IA** | Cuando procede | 5–10 líneas |
| **Números que conviene saberse** | Datos memorizables | tabla corta |
| **Lo esencial** | Cierre conceptual | 5–8 viñetas |
| **Preguntas abiertas** | Cierre del capítulo | 3–6 preguntas |

Sintaxis en markdown:

```markdown
::: pregunta
¿Cuánta energía libera una tormenta comparada con una bomba nuclear?
:::
```

---

## 10. Lista de comprobación antes de dar un capítulo por terminado

1. ¿Abre con un fenómeno observable y una pregunta cuantitativa?
2. ¿Se pide una estimación **antes** del primer cálculo?
3. ¿Cada concepto importante tiene sus cuatro capas (intuición, matemática,
   computación, realidad)?
4. ¿Hay ejemplos de al menos tres disciplinas, y al menos uno no es de física?
5. ¿Está la sección *¿Qué estamos suponiendo?* con supuestos numerados?
6. ¿Está la sección *¿Cuándo falla?* con un límite concreto?
7. ¿Hay al menos un anti-ejemplo donde la herramienta engaña?
8. ¿Toda historia lleva nivel A/B/C y referencia?
9. ¿Cada figura responde una pregunta escribible en su pie?
10. ¿Todo script se ejecuta limpio desde cero?
11. ¿Hay al menos una de cada categoría de ejercicio?
12. ¿Las soluciones de los problemas ● y ★ tienen pistas graduadas?
13. ¿Las referencias están separadas en históricas / técnicas / opcionales?
14. ¿Se ha eliminado todo lo que sólo transmite información consultable?
15. ¿El capítulo termina dejando una pregunta abierta genuina?
