# Plantilla de capítulo

*Documento de diseño (fase 5): el esqueleto que sigue cada capítulo de la Parte I.*

> Esqueleto reutilizable. Se copia tal cual al crear un capítulo nuevo y se
> rellena. Las secciones marcadas **(obligatoria)** no se pueden omitir; si un
> capítulo no admite alguna, hay que justificarlo en su cabecera.
>
> Copia ejecutable: `00-preliminares/plantilla/capitulo.md`

---

## Estructura canónica

```markdown
# Capítulo N — Título

> **Qué sabrás hacer al terminar**
> · capacidad 1 · capacidad 2 · capacidad 3
>
> **Herramientas que usa:** cap. X, cap. Y
> **Disciplinas de los ejemplos:** física, biología, ingeniería   ← cuota ≥3
> **Deuda que paga:** promesa abierta en el cap. Z
> **Deuda que abre:** se resolverá en el cap. W

## 1. Una pregunta                                    (obligatoria)

::: pregunta
Un fenómeno observable y una pregunta cuantitativa que el lector todavía no
sabe responder.
:::

Tres párrafos como máximo. Cero definiciones. Cero motivación genérica.

## 2. Antes de calcular                               (obligatoria)

::: antes
Apunta tu respuesta antes de seguir. No hace falta que sea buena: hace falta
que exista, porque el objetivo es medir la distancia entre tu intuición y el
resultado.
:::

## 3. La intuición

Modelo mental. Analogías. Límites extremos. Casos degenerados. Qué pasaría si
el parámetro fuese cero o infinito. Aquí todavía no hay álgebra seria.

## 4. La matemática

Derivación completa, sin saltos. Máximo tres ecuaciones numeradas seguidas sin
prosa. Cada ecuación importante se lee en voz alta y se comprueba
dimensionalmente.

::: herramientas
Repaso just-in-time de lo que haga falta (Taylor, autovalores, integración por
partes). Media página como mucho.
:::

## 5. El ordenador entra en escena

Predicción escrita **antes** de ejecutar. Después el código, de 15 a 40 líneas.
Después la figura. Después la comparación entre lo esperado y lo obtenido.

```python
# fig_nombre.py  —  qué pregunta responde
```

```markdown
![Pie en dos partes: qué se ve; qué hay que concluir.](figuras/fig_nombre.pdf)
```

## 6. Juega con el modelo

::: juega
Tres o cuatro manipulaciones concretas: duplica este parámetro, hazlo negativo,
llévalo al límite. Y para cada una, la pregunta: ¿qué esperas ver?
:::

## 7. ¿Qué estamos suponiendo?                        (obligatoria)

::: supuestos
Lista numerada de supuestos, cada uno con su condición de validez cuantitativa.
No vale «suponemos que el aire es ideal»: vale «suponemos gas ideal, válido
mientras p ≪ p_crítica, es decir por debajo de unas 30 atm».
:::

## 8. ¿Cuándo falla?                                  (obligatoria)

::: falla
Un régimen concreto donde el modelo da una respuesta incorrecta, con el número
que marca la frontera. Y el anti-ejemplo obligatorio del capítulo.
:::

## 9. Historia                                        (obligatoria)

::: historia
Episodio documentado. Nivel de verificación A/B/C declarado. Qué problema tenía
esa persona y qué hizo al atascarse. Entre el 8 % y el 15 % del capítulo.
:::

## 10. Problemas

Diez categorías. Marcadas ○ ◐ ● ★.
(Van en `problemas.md`; las soluciones en `soluciones.md`.)

## 11. Experimento computacional

::: experimento
Proyecto pequeño: pregunta, diseño, criterio de parada, qué gráfica lo
responde, y qué resultado falsaría la hipótesis.
:::

## 12. Explícalo                                      (obligatoria)

::: explica
De cuatro a siete preguntas Feynman. Sin ecuaciones en la respuesta.
:::

## 13. Lo esencial                                    (obligatoria)

::: esencial
De cinco a ocho viñetas. Conceptos, no fórmulas.
:::

## 14. Preguntas que quedan abiertas                  (obligatoria)

::: abierto
De tres a seis preguntas genuinas, sin respuesta en el libro.
:::

### Referencias                                       (obligatoria)

**Fuentes históricas** · **Referencias técnicas** · **Lecturas opcionales**
```

---

## Archivos de un capítulo

```text
cap-NN-nombre/
├── capitulo.md              texto principal (secciones 1–14)
├── problemas.md             enunciados por categoría
├── soluciones.md            soluciones razonadas con pistas graduadas
├── referencias.md           bibliografía comentada del capítulo
├── codigo/
│   ├── fig_*.py             un script por figura, ejecutable
│   └── exp_*.py             experimentos computacionales del capítulo
├── figuras/                 salida generada (PDF + PNG), no se edita a mano
├── slides/
│   ├── diapositivas.md      guion de la charla
│   └── cap-NN-…-diapositivas.pdf
├── notebook.ipynb           cuaderno interactivo generado
└── cap-NN-nombre.pdf        el capítulo compilado
```

---

## Plantilla de las diapositivas

Un capítulo, una charla de 20–25 minutos. **No es un resumen del capítulo:** es
el argumento del capítulo sin las derivaciones.

```markdown
# Título                          ← portada
# La pregunta                     ← el fenómeno, en una imagen
# Antes de calcular               ← que el público estime
# La intuición                    ← una figura, cero ecuaciones
# El modelo mínimo                ← 1–2 ecuaciones, no más
# Lo que predice                  ← la figura clave
# Lo que supone                   ← lista corta
# Cuándo falla                    ← el límite
# La historia                     ← el episodio
# Lo esencial                     ← 5 viñetas
# Para llevarse a casa            ← 1 frase + 1 pregunta abierta
```

Reglas: máximo seis líneas por diapositiva; una idea por diapositiva; toda
ecuación que aparezca se lee en voz alta; toda figura lleva su pregunta escrita.

---

## El capítulo piloto

El capítulo 1, *Órdenes de magnitud y estimaciones de Fermi*, se escribe
completo antes que ningún otro y sirve para calibrar tono, profundidad,
narrativa, matemáticas, ejercicios, historia y referencias. Todo lo que aprenda
el capítulo 1 se propaga a esta plantilla antes de escribir el capítulo 2.
