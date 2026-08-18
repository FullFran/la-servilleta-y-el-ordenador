# III.8 — Cómo usar simulaciones sin engañarte

---

## El problema

Una simulación siempre produce números. Nunca dice «no lo sé». Esa asimetría
—produce salida en cualquier caso, incluso cuando está mal— es lo que la hace
peligrosa.

---

## Las cinco preguntas antes de ejecutar

### 1. ¿Qué espero que pase?

Escríbelo. Una frase basta. Sin predicción previa, cualquier resultado parecerá
razonable *a posteriori*.

### 2. ¿Qué resultado me haría sospechar?

Igual de importante y aún menos frecuente. Si no puedes nombrar un resultado
que te haría revisar el código, no estás en condiciones de interpretar ninguno.

### 3. ¿Cuál es el caso trivial que sé resolver?

Ejecútalo primero. Siempre. Un parámetro a cero, una geometría simétrica, un
límite conocido. Si falla ahí, todo lo demás es ruido.

### 4. ¿Qué se conserva?

Y comprueba que se conserva. Capítulos 6 y 8.

### 5. ¿Cuánto voy a tardar y qué voy a hacer con el resultado?

Si no sabes qué decisión va a cambiar el resultado, probablemente no merezca la
pena ejecutarlo.

---

## Las cinco comprobaciones después

**1. ¿Cambia con la semilla?** Si es estocástico, ejecuta varias veces. Si el
efecto desaparece, era una realización.

**2. ¿Cambia con el paso o la malla?** Reduce a la mitad. Si el resultado se
mueve más que tu precisión objetivo, no has convergido.

**3. ¿Cambia con el método?** Otro integrador, otra biblioteca.

**4. ¿Cambia con la escala del sistema?** Si el efecto desaparece al duplicar el
tamaño, era un efecto de tamaño finito.

**5. ¿Es robusto a perturbar los parámetros?** Si un cambio del 1 % en un
parámetro cambia la conclusión, la conclusión no es del sistema: es del
parámetro.

---

## Los cinco autoengaños característicos

**El resultado bonito.** Cuanto más te gusta un resultado, menos lo compruebas.
Es el mecanismo del capítulo 15, y no se cura con voluntad: se cura decidiendo
los controles antes.

**La gráfica que convence.** Una figura con la forma esperada produce una
sensación de confirmación desproporcionada. Fíjate en los ejes: mira si están
en log, si el cero está incluido, si el rango se ha elegido después de ver los
datos.

**El barrido que no barre.** Ejecutar cien simulaciones variando un parámetro
irrelevante y ninguna variando el que importa. Se resuelve con el análisis de
sensibilidad del capítulo 15, hecho **antes** del barrido.

**El código que ya funcionaba.** Heredar un simulador y no verificarlo porque
«lleva años usándose». Los códigos científicos acumulan errores latentes que
sólo se manifiestan en regímenes nuevos.

**La conclusión que ya estaba.** Simular para confirmar algo que ya creías, y
parar de comprobar cuando aparece. La comprobación no debe depender del
resultado.

---

## Qué constituye evidencia

Una simulación es evidencia de algo muy concreto: **de las consecuencias de tus
supuestos**. No es evidencia sobre el mundo, salvo en la medida en que los
supuestos lo describan.

De ahí tres reglas al comunicar resultados de simulación:

* Di siempre **qué modelo** se ha simulado, no sólo qué se ha obtenido.
* Distingue explícitamente entre lo que sale del modelo y lo que se ha
  contrastado con datos.
* Si la conclusión depende de un supuesto no verificado, dilo **en la
  conclusión**, no en la sección de métodos.

---

## Lista de comprobación

```text
SIMULAR SIN ENGAÑARSE

Antes:
□ ¿Qué espero que pase? (escrito)
□ ¿Qué resultado me haría sospechar? (escrito)
□ ¿He ejecutado el caso trivial con solución conocida?
□ ¿Qué se conserva, y lo compruebo?
□ ¿Qué decisión va a cambiar este resultado?

Después:
□ ¿Cambia con la semilla?
□ ¿Cambia al reducir el paso o refinar la malla a la mitad?
□ ¿Cambia con otro método o biblioteca?
□ ¿Cambia al duplicar el tamaño del sistema?
□ ¿Es robusto a perturbar los parámetros un 1 %?

Meta:
□ ¿Decidí las comprobaciones antes de ver el resultado?
□ ¿Estoy comprobando más o menos porque el resultado me gusta?
□ ¿He dicho qué modelo he simulado, y no sólo qué ha salido?
```

---

## Ejercicios de campo

**A.** Coge tu última simulación y pásale las cinco comprobaciones posteriores.
Cronometra cuánto tardas: probablemente menos de una hora.

**B.** Ejecuta el caso trivial de un código que llevas tiempo usando. (Este
ejercicio descubre errores con una frecuencia incómoda.)

**C.** Escribe, antes de tu próxima simulación, las dos frases: qué esperas y
qué te haría sospechar. Guárdalas y compáralas después.

---

### Referencias

* **Wilson, G. et al.** *Good Enough Practices in Scientific Computing.* PLoS
  Comput. Biol. **13** (2017).
* **Winsberg, Eric.** *Science in the Age of Computer Simulation.* Chicago,
  2010. Qué tipo de evidencia es una simulación.
* **Oreskes, N.; Shrader-Frechette, K.; Belitz, K.** *Verification, Validation,
  and Confirmation of Numerical Models in the Earth Sciences.* Science **263**
  (1994), 641–646. Un artículo incómodo y muy citado sobre los límites de lo
  que una simulación puede establecer.
