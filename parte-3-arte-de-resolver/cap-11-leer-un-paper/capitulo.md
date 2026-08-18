# III.11 — Cómo leer un paper con mentalidad de modelador

---

## El problema

Leer un artículo de principio a fin es lento e ineficaz. Y leerlo como si fuera
una fuente de información —«¿qué dice?»— desaprovecha lo único que realmente
transfiere: **cómo pensó ese equipo**.

---

## El protocolo de tres pasadas

### Primera pasada: 10 minutos

Título, resumen, figuras, conclusiones. Objetivo: contestar cuatro preguntas.

1. ¿Qué pregunta se hacen?
2. ¿Qué afirman haber conseguido?
3. ¿Qué figura contiene el resultado principal?
4. ¿Me interesa seguir?

Con esto se descarta el 80 % de lo que llega.

### Segunda pasada: 45 minutos

Ahora sí, pero en un orden concreto y **no** el del artículo:

1. **La figura principal.** Entiéndela entera: ejes, unidades, barras de error,
   qué se compara con qué.
2. **El modelo.** ¿Cuáles son las variables? ¿Los supuestos? ¿Cuántos
   parámetros libres?
3. **De dónde salen los datos.** ¿Cuántos? ¿Medidos o simulados? ¿Con qué
   incertidumbre?
4. **La conexión entre modelo y datos.** ¿Ajuste? ¿Predicción? ¿Calibración o
   validación?
5. **Sólo entonces**, el texto.

### Tercera pasada: horas

Sólo para artículos que importan de verdad. Reproducir: rehacer las cuentas,
recalcular los órdenes de magnitud, implementar el método en un caso simple.

---

## Las doce preguntas del modelador

Estas son las que este libro entrena, y son las que casi nunca se hacen:

1. **¿Cuál es el modelo mínimo?** ¿Cuánto de lo que hay es esencial?
2. **¿Cuántos parámetros libres, y cuántos datos?** Si hay más parámetros que
   una décima parte de los datos, alerta.
3. **¿Está adimensionalizado?** Si no, ¿cuántos parámetros habría realmente?
4. **¿Cuáles son los números adimensionales?** ¿Están en el régimen que dicen?
5. **¿Dónde están las barras de error, y de qué son?** ¿Estadísticas,
   sistemáticas, o «las que salieron del ajuste»?
6. **¿Calibraron y validaron con los mismos datos?**
7. **¿Hay gráfica de residuos?** Si no, ¿por qué no?
8. **¿Extrapolan?** ¿Cuánto más allá del rango medido?
9. **¿Qué resultado habría falsado su hipótesis?** ¿Lo dicen?
10. **¿Cuántas cosas probaron antes de esta?** (Look-elsewhere.)
11. **¿Convergen?** Si hay simulación, ¿hay estudio de malla o de paso?
12. **¿Podría reproducirlo?** ¿Están el código y los datos?

---

## Las señales de alarma

* Ninguna barra de error, o barras sin especificar de qué.
* $R^2$ como única medida de bondad.
* Gráficas sin residuos en un artículo de ajuste.
* Ejes elegidos para que algo parezca lineal.
* Un exponente de ley de potencias ajustado en un histograma log-log
  (capítulo II.3).
* «Nuestro modelo reproduce los datos» sin decir cuántos parámetros tiene.
* Simulación sin estudio de convergencia.
* Un resultado justo por encima del umbral de significancia convencional.
* Conclusiones más fuertes en el resumen que en el cuerpo.

Ninguna de ellas invalida por sí sola un artículo. Todas justifican mirar más de
cerca.

---

## Lo que sí hay que llevarse de un buen artículo

Y esto es lo que distingue leer de recopilar:

**La estructura del problema.** ¿A qué se parece esto que ya conoces? Si el
modelo tiene la forma de un balance, de una competencia entre dos términos, de
una difusión con reacción o de una cola, ya sabes mucho.

**Los órdenes de magnitud.** Anótalos. Un número típico de un campo nuevo vale
más que diez páginas de contexto.

**El truco.** Casi todo buen artículo tiene una idea que hace tratable lo
intratable: un cambio de variable, una aproximación inesperada, una manera de
medir algo indirectamente. **Ese truco es transferible; el resultado, a menudo,
no.**

**Lo que no funcionó.** Si lo cuentan, es oro. Y si no lo cuentan, la sección
de métodos suele delatarlo.

---

## Lista de comprobación

```text
LEER UN PAPER

Primera pasada (10 min):
□ ¿Qué pregunta? ¿Qué afirman? ¿Qué figura? ¿Sigo?

Segunda pasada (45 min), en este orden:
□ Figura principal entera: ejes, unidades, barras
□ Modelo: variables, supuestos, parámetros libres
□ Datos: cuántos, de dónde, con qué incertidumbre
□ Conexión: ¿ajuste, calibración o validación?
□ Ahora el texto

Las doce preguntas:
□ modelo mínimo · parámetros/datos · adimensionalizado · números adimensionales
□ barras de error · calibración vs validación · residuos · extrapolación
□ falsabilidad · look-elsewhere · convergencia · reproducibilidad

Y me llevo:
□ la estructura del problema
□ tres órdenes de magnitud
□ el truco
□ lo que no funcionó
```

---

## Ejercicios de campo

**A.** Coge el último artículo que leíste y aplícale las doce preguntas.
Cuántas puedes contestar dice mucho del artículo, y también de cómo lo leíste.

**B.** Lee un artículo de un campo que no sea el tuyo aplicando el protocolo.
Anota la estructura del problema y los órdenes de magnitud, e ignora todo el
vocabulario que no entiendas.

**C.** Coge un artículo muy citado de tu campo e intenta reproducir su figura
principal con los datos que dan. Si no puedes, anota exactamente qué falta.

---

### Referencias

* **Keshav, S.** *How to Read a Paper.* ACM SIGCOMM CCR **37** (2007), 83–84.
  El protocolo de tres pasadas, en dos páginas.
* **Ioannidis, John.** *Why Most Published Research Findings Are False.* PLoS
  Med. **2** (2005). Léase junto con sus críticas.
* **Gelman, A. y Loken, E.** *The Garden of Forking Paths.* 2013.
* **Nosek, B. et al.** *The preregistration revolution.* PNAS **115** (2018),
  2600–2606. Qué cambia cuando la hipótesis se registra antes.
