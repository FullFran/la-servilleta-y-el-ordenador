# II.9 — ¿Cómo puede surgir orden del azar?

> **El fenómeno:** un trozo de hierro se imana por debajo de 770 °C y deja de
> estarlo por encima, sin que nadie coordine nada.
> **Herramientas:** cap. 9 (Metropolis), cap. 10 (Boltzmann), cap. 16
> (experimento computacional).
> **Lo que hay que llevarse:** que una transición de fase es un cambio
> cualitativo colectivo producido por interacciones locales, y que su
> comportamiento cerca del punto crítico es **universal**.

---

## 1. Una pregunta

::: pregunta
Cada átomo de un imán sólo «sabe» de sus vecinos inmediatos, y a temperatura
finita cada uno cambia de orientación constantemente y al azar.

**¿Cómo consiguen millones de átomos ponerse de acuerdo?**
:::

---

## 2. Antes de calcular

::: antes
1. ¿Esperas que la magnetización caiga gradualmente al calentar, o de golpe?
2. ¿Habrá una temperatura crítica en un sistema unidimensional (una cadena de
   espines)?
3. ¿Depende la temperatura crítica de los detalles microscópicos?
:::

---

## 3. El modelo más simple posible

$$E=-J\sum_{\langle ij\rangle}s_is_j,\qquad s_i=\pm1$$

Cada espín interacciona sólo con sus cuatro vecinos. No hay campo externo, no
hay nada que imponga una dirección global.

![Modelo de Ising 2D con Metropolis. Izquierda: magnetización frente a temperatura, comparada con la solución exacta de Onsager. Arriba a la derecha: configuraciones a tres temperaturas. Abajo: el efecto del tamaño del sistema. Lo que hay que concluir: existe una temperatura crítica bien definida, la transición se afila al crecer el sistema, y la simulación reproduce el resultado exacto.](figuras/fig_ising.pdf)

Y sale una transición de fase en $T_c=2/\ln(1+\sqrt2)=2{,}269\ldots$, el valor
exacto de Onsager (1944).

---

## 4. La competencia que lo explica

La física es un balance entre dos términos de la energía libre
$F=E-TS$:

* **La energía** prefiere el orden: espines alineados bajan $E$.
* **La entropía** prefiere el desorden: hay muchísimas más configuraciones
  desordenadas que ordenadas.

A baja temperatura gana la energía; a alta, la entropía. **Y el paso entre
ambos regímenes no es gradual**: por debajo de $T_c$ hay magnetización
espontánea, por encima es exactamente cero.

La dimensión decide si existe la transición:

* **1D**: no hay transición a $T>0$. Ising lo demostró en 1925 y concluyó
  erróneamente que el modelo no describía el ferromagnetismo. Se equivocó al
  extrapolar de 1D a 3D.
* **2D**: hay transición, y Onsager la resolvió exactamente en 1944 —una de las
  proezas técnicas de la física del siglo XX—.
* **3D**: hay transición, y **no** hay solución exacta. Los exponentes se
  conocen con seis cifras gracias al *bootstrap conforme* (desde 2012).

---

## 5. Universalidad: lo que no depende de los detalles

Cerca del punto crítico, las cantidades siguen leyes de potencias:

$$m\sim(T_c-T)^{\beta},\qquad \chi\sim|T-T_c|^{-\gamma},\qquad
\xi\sim|T-T_c|^{-\nu}$$

Y aquí está el resultado profundo: **esos exponentes son idénticos para
sistemas completamente distintos**. El Ising 3D, la transición
líquido-vapor del agua en su punto crítico, la separación de fases de una
mezcla binaria y la transición de un sistema magnético uniaxial tienen los
**mismos** exponentes.

La razón es que cerca del punto crítico la longitud de correlación $\xi$
diverge, y el sistema deja de «ver» la escala atómica. Sólo importan la
dimensión del espacio y la simetría del parámetro de orden. Eso es la
**universalidad**, y es la misma idea que la constante de Feigenbaum del
capítulo 7.

Es también, dicho de otro modo, una justificación profunda del principio de
modelo mínimo: cerca de un punto crítico, **los detalles microscópicos son
literalmente irrelevantes**, y un modelo de juguete da los números correctos.

---

## 6. ¿Cuándo falla?

::: falla
**Falla el tamaño finito.** Un sistema finito no tiene transición estricta: la
magnetización nunca es exactamente cero. La transición se afila al crecer $L$,
como muestra el panel inferior de la figura, y los exponentes se extraen por
**escalado de tamaño finito**. El residuo por encima de $T_c$ lo dice con
números: la simulación da $|m|=0{,}250$ para $L=8$, $0{,}134$ para $L=16$,
$0{,}070$ para $L=32$ y $0{,}040$ para $L=48$. Cada vez que $L$ se duplica el
residuo se divide por dos: es $|m|\sim1/\sqrt{N}=1/L$, el mismo $1/\sqrt{N}$
del capítulo 3, aquí disfrazado de física.

**Falla Metropolis cerca de $T_c$.** El tiempo de autocorrelación diverge como
$\xi^z$ con $z\approx2$: la cadena se vuelve inutilizablemente lenta justo
donde interesa. Se llama *ralentización crítica* —y es pariente de la del
capítulo 7—. La solución son los algoritmos de cúmulos (Swendsen–Wang, 1987;
Wolff, 1989), que voltean regiones enteras y reducen $z$ a casi cero.

**Falla extrapolar de una dimensión a otra**, como le ocurrió a Ising.

**Y falla suponer que «orden espontáneo» requiere un organizador.** Es el
mensaje del capítulo: interacciones locales más un balance energía-entropía
bastan.
:::

---

## 7. La misma idea, fuera de la física

La estructura reaparece con notable frecuencia:

* **Percolación:** conectividad que aparece de golpe al superar una densidad
  crítica. Es el modelo mínimo de la propagación de incendios, de epidemias en
  redes y de la conductividad de mezclas.
* **Segregación de Schelling (1971):** agentes con una preferencia mínima por
  vecinos parecidos producen segregación total. Nadie quería segregarse tanto:
  es un efecto colectivo.
* **Sincronización de Kuramoto:** osciladores acoplados que se sincronizan de
  golpe al superar un acoplamiento crítico. Luciérnagas, aplausos, redes
  eléctricas.
* **Patrones de Turing (1952):** dos sustancias que difunden a velocidades
  distintas y reaccionan producen manchas y rayas espontáneas.

En todos: **reglas locales simples, umbral crítico, orden global emergente**.

---

## 8. Historia

::: historia
**Ising, 1925, y un error de extrapolación** · *Nivel de verificación: A.*

Ernst Ising resolvió el modelo unidimensional en su tesis doctoral, dirigida
por Wilhelm Lenz —que había propuesto el modelo—. Encontró que no hay
transición de fase a temperatura finita, y concluyó que el modelo no servía
para explicar el ferromagnetismo.

Fue un error de extrapolación: **1D es el caso excepcional**. Ising dejó la
investigación, trabajó como profesor de instituto, sufrió la persecución nazi y
emigró a Estados Unidos en 1947. Descubrió que su modelo se había vuelto famoso
leyendo la literatura muchos años después.

**Onsager, 1944** · *Nivel de verificación: A.*

Lars Onsager resolvió exactamente el modelo 2D sin campo externo, obteniendo
$T_c$ y la energía libre. La solución es célebre por su dificultad técnica, y
Onsager la presentó de una forma característicamente lacónica: anunció el
resultado de la magnetización espontánea, $m=(1-\sinh^{-4}(2/T))^{1/8}$,
escribiéndolo en la pizarra durante una conferencia en 1948 **sin publicar la
demostración**. La derivación completa la publicó C. N. Yang en 1952.

**Wilson, 1971** · *Nivel de verificación: A.*

Kenneth Wilson explicó **por qué** hay universalidad, con el grupo de
renormalización: al mirar el sistema a escalas cada vez mayores, los detalles
microscópicos fluyen hacia un punto fijo que sólo depende de la dimensión y de
la simetría. Nobel en 1982.

El grupo de renormalización es probablemente la mejor formalización que existe
de la pregunta central de este libro: **qué se puede ignorar y por qué**.
:::

---

## 9. Experimento computacional

::: experimento
**Mide un exponente crítico.**

Simula el Ising 2D para $L=8,16,32,64$ y mide la susceptibilidad
$\chi=L^2(\langle m^2\rangle-\langle|m|\rangle^2)/T$ cerca de $T_c$.

Usa escalado de tamaño finito: $\chi_{\max}(L)\propto L^{\gamma/\nu}$. Dibuja
$\ln\chi_{\max}$ frente a $\ln L$ y mide la pendiente.

*Valor exacto:* $\gamma/\nu=7/4=1{,}75$.

*Y después, lo importante:* repite con el algoritmo de Wolff y compara el
tiempo de cálculo necesario para la misma precisión cerca de $T_c$. La
diferencia es de órdenes de magnitud, y es un ejemplo perfecto de que **elegir
el algoritmo adecuado importa más que la potencia de la máquina**.
:::

---

## 10. Lo esencial

::: esencial
* Un orden global puede surgir de interacciones puramente locales, por el
  balance entre energía y entropía.
* La transición es un cambio **cualitativo**: hay una temperatura crítica bien
  definida.
* La dimensión decide: en 1D no hay transición, y extrapolar de 1D a 3D fue el
  error de Ising.
* Cerca del punto crítico, los exponentes son **universales**: sólo dependen de
  la dimensión y de la simetría.
* La universalidad justifica el modelo mínimo: los detalles microscópicos son
  literalmente irrelevantes ahí.
* Metropolis se ralentiza críticamente cerca de $T_c$; los algoritmos de
  cúmulos lo resuelven.
* La misma estructura aparece en percolación, segregación, sincronización y
  formación de patrones.
:::

---

## 11. Preguntas abiertas

::: abierto
* ¿Por qué exactamente la longitud de correlación diverge, y qué la hace
  divergir en sistemas tan distintos?
* ¿Hay universalidad en sistemas fuera del equilibrio? ¿Con qué clases?
* ¿Qué modelos sociales de segregación o de opinión tienen transiciones reales
  y cuáles son artefactos del modelo?
* Si un modelo de juguete da los exponentes correctos, ¿en qué sentido
  «explica» el fenómeno?
:::

### Referencias

* **Ising, Ernst.** *Beitrag zur Theorie des Ferromagnetismus.* Zeitschrift für
  Physik **31** (1925), 253–258. **Nivel A (primaria).**
* **Onsager, Lars.** *Crystal Statistics I.* Physical Review **65** (1944),
  117–149. **Nivel A (primaria).**
* **Wilson, Kenneth G.** *Problems in Physics with Many Scales of Length.*
  Scientific American, 1979, y su discurso Nobel de 1982.
* **Newman, M. E. J. y Barkema, G. T.** *Monte Carlo Methods in Statistical
  Physics.* Oxford UP, 1999. **La referencia práctica** del capítulo.
* **Wolff, Ulli.** *Collective Monte Carlo updating for spin systems.* PRL
  **62** (1989), 361. El algoritmo que resuelve la ralentización crítica.
* **Schelling, Thomas.** *Dynamic models of segregation.* J. Math. Sociol. **1**
  (1971), 143–186. La misma estructura en ciencias sociales.
* **Stauffer, D. y Aharony, A.** *Introduction to Percolation Theory.* 2.ª ed.,
  Taylor & Francis, 1994.
