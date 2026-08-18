# Plan de entrenamiento

> Un libro que se lee se olvida. Un libro que se entrena, no. Lo que sigue es un
> programa, no una obligación: está diseñado para que puedas incumplirlo sin que
> se rompa.

---

## La sesión tipo

De 45 a 90 minutos, cinco o seis días por semana. Cinco bloques, siempre en este
orden:

```text
10 min   ESTIMACIÓN     un problema sin ayuda, sin buscador, sin IA
20–30    LECTURA        con lápiz; el libro se subraya y se discute
20–30    TRABAJO        un problema o una simulación
5–10     FEYNMAN        explicar en voz alta, sin ecuaciones
2        CUADERNO       una pregunta nueva
```

Por qué este orden y no otro:

* **La estimación va primero** porque es lo que peor se hace con la cabeza
  cansada, y porque establece el estado mental correcto para leer: llegas al
  texto con una pregunta propia, no como espectador.
* **La lectura va antes que el trabajo** para que el problema encuentre las
  herramientas frescas.
* **La explicación va al final** porque es la única prueba honesta de la sesión.
  Si no puedes explicar sin ecuaciones lo que acabas de hacer, no lo has
  entendido, y es mejor saberlo hoy que dentro de tres capítulos.
* **La pregunta nueva** existe para que la sesión siguiente ya tenga dónde
  agarrarse. Es el equivalente intelectual de dejar la caña preparada.

### Si sólo tienes 30 minutos

Estimación (10) + un problema (15) + explicación (5). La lectura se puede
aplazar; el entrenamiento no.

### Si tienes un día entero

No hagas cuatro sesiones seguidas. Haz una sesión y después un **proyecto**:
coge un fenómeno que te interese, recorre el ciclo entero y escribe el resultado
como si fueras a enseñárselo a alguien. Los proyectos son donde se consolida.

---

## La primera semana

El arranque es donde se abandona, así que la primera semana está cerrada: qué
leer, qué hacer y cuánto tarda. No hay decisiones que tomar.

### Día 1 — Escalas y Fermi

* **Estimación (10 min).** ¿Cuántas respiraciones has hecho en tu vida? Sin
  calculadora. Escribe también tu cota inferior y tu cota superior.
* **Lectura.** Capítulo 1, secciones 1.1 a 1.5.
* **Trabajo.** Problemas 1.E1 a 1.E4 (categoría Estimación). Después comprueba
  con datos reales y anota el factor de error de cada uno.
* **Feynman.** ¿Por qué multiplicar seis números malos puede dar un resultado
  bueno?
* **Cuaderno.** Una cantidad de tu trabajo o de tu vida diaria cuyo orden de
  magnitud no sepas.

### Día 2 — Probabilidad y conteo

* **Estimación.** ¿Cuántos rayos cósmicos atraviesan tu cuerpo cada segundo?
* **Lectura.** Capítulo 3, secciones 3.1 a 3.6; capítulo 4, secciones 4.1 a 4.3.
* **Trabajo.** Simula 10⁵ tiradas y comprueba a mano que σ crece como √N.
  Después el problema 4.C1.
* **Feynman.** ¿Por qué el ruido relativo baja cuando cuentas más, si el ruido
  absoluto sube?
* **Cuaderno.** ¿Dónde has visto tú una σ = √N sin darte cuenta?

### Día 3 — EDO y escalas temporales

* **Estimación.** ¿Cuánto tarda un café en pasar de 90 °C a 60 °C? Da un número
  antes de abrir el capítulo.
* **Lectura.** Capítulo 6, secciones 6.1 a 6.5.
* **Trabajo.** Resuelve la ley de Newton del enfriamiento a mano, identifica τ y
  compáralo con tu estimación. Si tienes un termómetro, mide de verdad.
* **Feynman.** ¿Qué significa físicamente que τ no dependa de la temperatura
  inicial?
* **Cuaderno.** Tres sistemas de tu entorno con tiempos característicos muy
  distintos.

### Día 4 — Cálculo numérico

* **Estimación.** Si un método tiene error $\mathcal{O}(h^2)$ y reduces el paso a
  la mitad, ¿cuánto baja el error? ¿Y si lo reduces por 10?
* **Lectura.** Capítulo 8, secciones 8.1 a 8.6.
* **Trabajo.** Implementa Euler a mano para el oscilador armónico. Dibuja la
  energía frente al tiempo. Explica lo que ves antes de leer la explicación.
* **Feynman.** ¿Por qué un método puede ser exacto en el límite y desastroso en
  la práctica?
* **Cuaderno.** ¿Cuándo fue la última vez que confiaste en un resultado numérico
  sin comprobar la convergencia?

### Día 5 — Monte Carlo

* **Estimación.** ¿Cuántas muestras hacen falta para estimar π con dos cifras
  decimales correctas?
* **Lectura.** Capítulo 9, secciones 9.1 a 9.5.
* **Trabajo.** Estima π por Monte Carlo. Dibuja el error frente a N en ejes
  logarítmicos y mide la pendiente. ¿Sale −1/2?
* **Feynman.** ¿Cómo puede un método aleatorio dar una respuesta determinista?
* **Cuaderno.** Un problema de tu trabajo que podría atacarse por muestreo.

### Día 6 — Problema libre

Elige un fenómeno real que te haya llamado la atención esta semana. Recorre el
ciclo entero, de fenómeno a nueva pregunta, y escríbelo en el cuaderno con la
plantilla completa. Dos horas. No busques nada durante la primera media hora.

### Día 7 — Recapitulación de memoria

Con el libro cerrado, responde por escrito:

* ¿Qué sé estimar ahora que no sabía el lunes?
* ¿Qué modelos puedo construir sin mirar nada?
* ¿Qué aproximaciones sé justificar, y con qué argumento?
* ¿Qué conceptos estaba usando mecánicamente?
* ¿Qué preguntas nuevas han aparecido?

Después, y sólo después, abre el libro y comprueba qué se te había olvidado.

---

## El ciclo largo: doce semanas

| Semanas | Contenido | Entregable propio |
|---|---|---|
| 1 | Caps. 1–2 (magnitud, dimensiones) | 20 estimaciones con su factor de error medido |
| 2 | Caps. 3–4 (probabilidad, conteo) | Un simulador de un proceso de conteo con su análisis |
| 3 | Caps. 5–6 (incertidumbre, EDO) | Ajuste de datos propios con incertidumbres honestas |
| 4 | Caps. 7–8 (dinámica, numérico) | Estudio de convergencia de un integrador escrito por ti |
| 5 | Caps. 9–10 (Monte Carlo, optimización) | Un MCMC propio, con diagnóstico |
| 6 | Caps. 11–13 (lineal, Fourier, escalas) | Un análisis espectral de una señal real tuya |
| 7 | Caps. 14–16 (modelar, dudar, laboratorio) | Un modelo propio, con su crítica escrita |
| 8–10 | Parte II, cinco capítulos a elegir | Un fenómeno modelado de principio a fin |
| 11 | Parte III completa | Las trece listas de comprobación, anotadas |
| 12 | Proyecto final | Un informe de 8–10 páginas y una charla de 20 minutos |

**El proyecto final** es el examen real: un fenómeno que nadie te ha explicado,
un modelo tuyo, una simulación tuya, una validación honesta y una lista escrita
de todo lo que tu modelo no puede hacer.

---

## Cómo saber si está funcionando

Indicadores observables, no sensaciones:

| Señal | Qué indica |
|---|---|
| Tus estimaciones caen dentro de un factor 3 más de la mitad de las veces | La descomposición funciona |
| Escribes los supuestos **antes** de las ecuaciones, sin acordarte de que había una regla | El hábito está instalado |
| Te molesta un resultado numérico sin prueba de convergencia | Has interiorizado la desconfianza |
| Puedes explicar tu último modelo a alguien de otra carrera en tres minutos | La capa de intuición existe |
| Al ver una noticia con un número, calculas si es plausible | El libro ha salido del libro |
| Empiezas a irritarte con los papers que no dan sus supuestos | Bienvenido |

## Cómo saber si NO está funcionando

* Lees los capítulos y saltas las cajas *Antes de calcular*. Es el fallo más
  común y el más fatal: sin la estimación previa, el capítulo es divulgación.
* Ejecutas el código y miras la gráfica sin haber escrito una predicción.
* Haces sólo los ejercicios ○ y ◐, y nunca los ● ni los ★.
* Consultas la solución antes de veinte minutos.
* Nunca has escrito nada en el cuaderno.

Si reconoces tres o más, no hace falta cambiar de libro: hace falta cambiar de
sesión. Vuelve al día 1 y haz sólo el bloque de estimación durante una semana.
