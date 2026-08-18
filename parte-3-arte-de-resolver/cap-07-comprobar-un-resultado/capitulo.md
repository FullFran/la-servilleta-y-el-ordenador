# III.7 — Cómo comprobar un resultado

---

## El problema

Tienes un número. Antes de creértelo —y sobre todo antes de que otros se lo
crean— hay que someterlo a un interrogatorio. Este capítulo es el
interrogatorio.

Está ordenado por coste creciente. Los cinco primeros cuestan segundos.

---

## Los doce controles

### Coste: segundos

**1. Dimensiones.** ¿Las unidades son las correctas? Es el filtro más barato y
detecta una fracción sorprendente de errores.

**2. Signo.** ¿Es del signo esperado? Una temperatura que baja al calentar, una
concentración negativa, una probabilidad mayor que 1.

**3. Orden de magnitud.** ¿Coincide con la estimación que hiciste al principio?
Y si no la hiciste, hazla ahora. Capítulo 1.

**4. Casos límite.** ¿Qué pasa cuando un parámetro es cero? ¿E infinito? Los
límites suelen tener respuesta conocida.

**5. Casos conocidos.** ¿Reproduce el resultado un caso resuelto? Si tu código
de fluidos no da Poiseuille, no hace falta seguir.

### Coste: minutos

**6. Monotonía.** ¿Va en la dirección correcta cuando cambias un parámetro? Más
aislamiento debería enfriar más despacio, no más deprisa.

**7. Conservación.** ¿Se conserva lo que debe conservarse? Masa, energía,
probabilidad total, número de individuos.

**8. Invariancias.** Cambia unidades, gira los ejes, renumera los elementos,
invierte el tiempo. Lo que no debe cambiar, no debe cambiar.

**9. Convergencia.** Reduce el paso, refina la malla, sube la tolerancia. ¿Se
mueve el resultado? ¿Cuánto? Capítulo 8.

### Coste: horas

**10. Otro método.** Resuelve el mismo problema por un camino distinto:
analítico frente a numérico, Monte Carlo frente a determinista, otra
biblioteca. Es el control más potente que existe.

**11. Otra persona.** Que alguien reproduzca el resultado desde el enunciado,
sin ver tu código.

**12. El dato experimental.** Contrastar con la realidad, con las
incertidumbres de ambos lados declaradas.

---

## El orden importa

Un error de dimensiones detectado en el paso 1 ahorra los once restantes. Y sin
embargo la tentación es siempre saltar al 10 o al 12, que son los que se
publican.

Regla práctica: **nunca pases al siguiente control sin haber pasado todos los
anteriores.**

---

## La pregunta que hay que hacerse antes de todo

Antes incluso del control 1:

> ¿Estoy comprobando el resultado, o estoy comprobando que el resultado es el
> que esperaba?

Son cosas distintas y producen comportamientos opuestos. El sesgo de
confirmación en la comprobación es el mecanismo de Millikan del capítulo 15, y
la única defensa es **decidir los controles antes de ver el resultado**.

---

## Cuando el resultado es interesante

Regla dura, y la más útil de este capítulo:

> **Cuanto más interesante sea un resultado, más controles hay que pasarle.**

Un resultado aburrido y esperado puede pasar con los cinco primeros. Un
resultado que contradice lo establecido, que abre una línea nueva o que
conviene a tu hipótesis necesita los doce, y probablemente un análisis ciego.

La razón es aritmética: la probabilidad previa de que un resultado sorprendente
sea cierto es baja, así que hace falta un factor de Bayes mayor para moverla
(capítulo II.4). Y la probabilidad de que sea un error tuyo no es baja en
absoluto.

---

## Lista de comprobación

```text
COMPROBAR UN RESULTADO

Segundos:
□ Dimensiones correctas
□ Signo correcto
□ Orden de magnitud coincide con la estimación previa
□ Casos límite (parámetro 0, parámetro ∞)
□ Reproduce un caso conocido con solución

Minutos:
□ Monotonía en la dirección correcta
□ Conservaciones se conservan
□ Invariancias (unidades, rotación, orden, inversión temporal)
□ Convergencia al refinar

Horas:
□ Otro método independiente
□ Otra persona lo reproduce desde el enunciado
□ Contraste experimental con incertidumbres de ambos lados

Meta:
□ ¿Decidí los controles ANTES de ver el resultado?
□ ¿Es un resultado interesante? Entonces todos, y a ciegas.
```

---

## Ejercicios de campo

**A.** Coge tu último resultado y pásale los doce controles, en orden. Anota en
cuál falla, si falla.

**B.** Toma un resultado que ya diste por bueno hace meses. Pásale los cinco
primeros. (Este ejercicio sale mal más veces de las que uno espera.)

**C.** Escribe, antes de tu próximo cálculo, la lista de controles que le vas a
pasar y qué resultado te haría dudar. Guárdala.

---

### Referencias

* **Roache, P. J.** *Verification and Validation in Computational Science and
  Engineering.* Hermosa, 1998.
* **Oberkampf, W. y Roy, C.** *Verification and Validation in Scientific
  Computing.* Cambridge UP, 2010.
* **Feynman, R. P.** *Cargo Cult Science*, 1974. Sobre comprobar contra uno
  mismo.
* **Klein, J. R. y Roodman, A.** *Blind Analysis in Nuclear and Particle
  Physics.* Annu. Rev. Nucl. Part. Sci. **55** (2005).
