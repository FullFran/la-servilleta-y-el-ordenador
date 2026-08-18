# Apéndice F — Plan de entrenamiento de doce semanas

> Versión detallada del plan de `00-preliminares/05-plan-de-entrenamiento.md`.
> Sesión de 45–90 minutos, cinco o seis días por semana.

---

## Estructura de la sesión

```text
10 min   ESTIMACIÓN   sin ayuda, sin buscador, sin IA
20–30    LECTURA      con lápiz
20–30    TRABAJO      un problema o una simulación
5–10     FEYNMAN      explicar en voz alta, sin ecuaciones
2        CUADERNO     una pregunta nueva
```

---

## Semanas 1–7: la Parte I

| Semana | Capítulos | Entregable propio |
|---|---|---|
| **1** | 1, 2 + Interludio 1 | 20 estimaciones con su factor de error medido |
| **2** | 3, 4 | Un simulador de un proceso de conteo, con su análisis de dispersión |
| **3** | 5, 6 | Ajuste de datos medidos por ti, con incertidumbres honestas |
| **4** | 7, 8 + Int. 5, 6 | Estudio de convergencia de un integrador escrito por ti |
| **5** | 9, 10 + Int. 3, 4 | Un MCMC propio, con $\hat R$ y $N_{\text{ef}}$ |
| **6** | 11, 12, 13 + Int. 2 | Análisis espectral de una señal real tuya, con Welch |
| **7** | 14, 15, 16 + Int. 7, 8 | Un modelo propio de principio a fin, con su crítica escrita |

**Al final de la semana 7** deberías poder: estimar cualquier cosa en diez
minutos con intervalo, adimensionalizar un modelo, medir el orden de un método
numérico, diagnosticar un MCMC y escribir la lista de supuestos de un modelo
con sus condiciones de validez.

---

## Semanas 8–10: la Parte II

Elige **cinco** capítulos de fenómenos. Recomendación de itinerarios:

**Itinerario físico:** II.1 (gota), II.2 (café), II.6 (órbitas), II.7
(difusión), II.10 (predicción).

**Itinerario de sistemas:** II.5 (epidemia), II.9 (orden), II.11 (tráfico),
II.12 (colas), II.10 (predicción).

**Itinerario de datos:** II.3 (gaussianas), II.4 (detección), II.7 (difusión),
II.13 (escalas), II.14 (invertir).

Para cada uno: el capítulo, su experimento computacional y **una variante
propia** del fenómeno.

*Entregable de la fase:* un fenómeno modelado de principio a fin, con datos
medidos por ti si es posible.

---

## Semana 11: la Parte III

Los trece capítulos, que son cortos. Y el trabajo real: **aplicar cada lista de
comprobación a un trabajo tuyo en curso**, e imprimirlas.

*Entregable:* las trece listas anotadas con lo que has encontrado al
aplicarlas.

---

## Semana 12: el proyecto final

Es el examen de verdad. Un fenómeno que nadie te ha explicado, recorrido entero:

1. Pregunta cuantitativa con precisión declarada.
2. Estimación de orden de magnitud, previa.
3. Variables y descartes con motivo.
4. Supuestos numerados con condición de validez.
5. Modelo mínimo y su solución.
6. Simulación con predicción escrita previa.
7. Datos, medidos o recogidos, con incertidumbre.
8. Validación **con datos no usados en el ajuste**.
9. Análisis de sensibilidad.
10. Lista explícita de lo que tu modelo **no** puede hacer.
11. Preguntas abiertas.

*Entregables:* un informe de 8–10 páginas y una charla de 20 minutos con
diapositivas propias.

---

## Cómo saber si funciona

| Señal observable | Qué indica |
|---|---|
| Tus estimaciones caen dentro de un factor 3 más de la mitad de las veces | la descomposición funciona |
| Escribes los supuestos antes de las ecuaciones sin acordarte de la regla | el hábito está instalado |
| Te molesta un resultado numérico sin prueba de convergencia | la desconfianza está interiorizada |
| Puedes explicar tu último modelo en tres minutos a alguien de otra carrera | la capa de intuición existe |
| Al ver un número en una noticia, calculas si es plausible | el libro ha salido del libro |

---

## Si te descuelgas

Ocurrirá. Tres reglas:

* **No reinicies.** Sigue desde donde estés.
* **Prioriza el bloque de estimación.** Si sólo puedes hacer diez minutos, que
  sean esos.
* **El cuaderno importa más que la lectura.** Una entrada por semana es
  suficiente para que el método se instale; cero entradas es equivalente a no
  haber leído nada.
