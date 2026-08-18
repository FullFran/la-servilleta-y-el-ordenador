# II.6 — ¿Por qué algunas órbitas son estables?

> **El fenómeno:** el sistema solar lleva 4600 millones de años funcionando.
> **Herramientas:** cap. 6 (conservación), cap. 8 (integradores), cap. 11
> (autovalores), cap. 13 (perturbaciones seculares).
> **Lo que hay que llevarse:** que la estabilidad de una simulación larga no
> depende del orden del método sino de si respeta la estructura, y que la
> precesión que ves puede ser tuya.

---

## 1. Una pregunta

::: pregunta
Simulas una órbita elíptica durante 2500 periodos y observas que el perihelio
precesa lentamente y que la órbita se va cerrando.

**¿Es física o es de tu integrador?**
:::

---

## 2. Antes de calcular

::: antes
1. Con un método de orden 4 y otro de orden 1, ¿cuál esperas que conserve mejor
   la energía tras 2500 periodos?
2. ¿Qué cantidad comprobarías primero para saber si tu integración es fiable?
3. ¿Es estable el sistema solar? ¿Qué significa exactamente esa pregunta?
:::

---

## 3. Orden no es lo mismo que fidelidad

![Órbita de excentricidad 0,8 integrada 2500 periodos. Izquierda: las últimas órbitas. Centro: la energía. Derecha: el error del momento angular. Lo que hay que concluir: RK4, de orden 4, destruye la órbita; Verlet, de orden 2 y mucho más barato, la conserva.](figuras/fig_orbitas.pdf)

Los números de esta simulación:

| Método | Deriva secular de $E$ | Anchura de la banda | Deriva total |
|---|---|---|---|
| Runge–Kutta 4 | $+7{,}4\times10^{-3}$/ut | $4{,}3\times10^{2}$ | **849×** |
| Verlet | $+4{,}9\times10^{-11}$/ut | $6{,}7\times10^{-2}$ | 0,09 |

La diferencia no está en la precisión por paso: RK4 es mucho más preciso a
corto plazo. Está en **el tipo de error**.

* RK4 comete un error que se acumula de forma **secular**: siempre en la misma
  dirección. Tras muchos periodos, la órbita se ha ido.
* Verlet comete un error **acotado y oscilante**: la energía sube y baja
  alrededor del valor correcto sin derivar.

La razón es la del capítulo 8: Verlet conserva exactamente el volumen en el
espacio de fases y, por el análisis hacia atrás, resuelve exactamente un
hamiltoniano $H+h^2H_2+\dots$ muy próximo al verdadero. Un hamiltoniano
conserva su energía, así que la energía del simpléctico oscila pero no deriva.

**Un sistema hamiltoniano exige un integrador hamiltoniano.** Y esto no es una
preferencia estética: es la diferencia entre una simulación utilizable a
$10^9$ años y una que no lo es.

---

## 4. Lo que sí conserva y lo que no

Para el problema de dos cuerpos hay tres cantidades conservadas: energía,
momento angular y el **vector de Laplace–Runge–Lenz**, que apunta al perihelio.
La conservación de este último es lo que hace que la órbita sea una elipse
cerrada y no precese.

Es una propiedad frágil: sólo se conserva para el potencial exactamente
$1/r$. Cualquier perturbación —el achatamiento del Sol, la relatividad general,
otros planetas— la rompe y produce **precesión del perihelio**.

Por eso la precesión es un observable tan valioso: es cero para el problema
kepleriano puro, así que cualquier precesión medida es información sobre la
física que falta. La de Mercurio, 43 segundos de arco por siglo tras descontar
todas las perturbaciones newtonianas, fue la primera confirmación cuantitativa
de la relatividad general.

Y por eso también es tan peligrosa numéricamente: **un integrador que no
conserva la estructura produce precesión espuria**, y confundirla con física es
un error fácil de cometer y difícil de detectar sin la comprobación de la
sección 3.

---

## 5. ¿Es estable el sistema solar?

La pregunta ocupó a Newton, Laplace, Poincaré y Kolmogórov, y la respuesta
moderna es interesante.

Laplace y Lagrange demostraron a finales del XVIII que, a primer orden en las
masas, los semiejes mayores no tienen términos seculares: el sistema parecía
estable. Poincaré demostró en 1890 que las series usadas para esas
demostraciones **divergen** en general, y que hay órbitas de comportamiento
extraordinariamente complicado.

La teoría KAM (Kolmogórov 1954, Arnold 1963, Moser 1962) demostró que, para
perturbaciones suficientemente pequeñas, **la mayoría** de las trayectorias
cuasi-periódicas sobreviven. Pero «suficientemente pequeñas» significa, en las
estimaciones originales, masas planetarias absurdamente menores que las reales.

La respuesta empírica llegó con la computación. Las integraciones de Laskar
(desde 1989) y otros muestran que el sistema solar es **caótico**, con un tiempo
de Lyapunov de unos 5 millones de años. La consecuencia práctica es exactamente
la del capítulo 7: una incertidumbre de 15 metros en la posición actual de la
Tierra se convierte en una incertidumbre del orden de la órbita al cabo de unos
100 millones de años.

Y lo que se puede afirmar es estadístico: en ~1 % de las integraciones,
Mercurio alcanza excentricidades que permiten colisiones o eyecciones en los
próximos 5000 millones de años. **No es una predicción; es una probabilidad.**

---

## 6. ¿Cuándo falla?

::: falla
**Falla el paso adaptativo con integradores simplécticos.** Cambiar el paso
rompe la simplecticidad y reintroduce deriva secular. Para órbitas excéntricas
hay que usar paso fijo con regularización, o esquemas simplécticos con cambio
de variable temporal.

**Falla la precisión de máquina a tiempos largos.** En $10^9$ años con paso de
días son $10^{11}$ pasos; el error de redondeo acumulado, aunque crezca sólo
como $\sqrt N$, llega a ser relevante. Se usa suma compensada de Kahan.

**Falla interpretar una trayectoria individual.** Con tiempo de Lyapunov de 5
Ma, ninguna trayectoria calculada a $10^8$ años es la real. Sólo son
interpretables las estadísticas sobre muchas condiciones iniciales.

**Y falla el modelo de dos cuerpos en cuanto hay un tercero.** El problema de
tres cuerpos no tiene solución cerrada, y eso no es una carencia técnica: es un
resultado (Bruns, Poincaré).
:::

---

## 7. Historia

::: historia
**Poincaré, el rey Óscar y el error impreso** · *Nivel de verificación: A.*

En 1885, el rey Óscar II de Suecia convocó un premio para quien resolviera el
problema de los $n$ cuerpos. Poincaré presentó una memoria que ganó en 1889.

Mientras se preparaba la publicación, el editor Lars Edvard Phragmén le planteó
dudas sobre un punto. Poincaré revisó y descubrió un **error grave**: había
supuesto que ciertas variedades invariantes se cerraban sobre sí mismas, y no
lo hacían. Al corregirlo apareció la estructura homoclínica: intersecciones
infinitas y una complejidad que él mismo describió como algo que ni siquiera
intentaría dibujar.

La memoria premiada ya estaba impresa y distribuida. Poincaré pagó de su
bolsillo la retirada y reimpresión: 3585 coronas, más que las 2500 del premio.

La versión corregida, publicada en *Acta Mathematica* en 1890, es la que
contiene el descubrimiento del caos determinista, sesenta años antes que
Lorenz.

**Lo que hay que llevarse:** el error no fue un accidente lamentable, fue el
camino. Corregirlo obligó a mirar la estructura que había supuesto sin
comprobar.
:::

---

## 8. Experimento computacional

::: experimento
**Mide la precesión espuria de tu integrador.**

Integra una órbita kepleriana con excentricidad 0,7 usando RK4, Verlet y
`solve_ivp` con `DOP853` y tolerancia $10^{-12}$.

Mide la precesión del perihelio de cada uno en función del paso y del número de
órbitas. La respuesta correcta es **cero**.

*Qué esperar:* la precesión espuria de RK4 escala como $h^4$ y crece
linealmente con el tiempo; la de Verlet es mucho menor y no crece secularmente.

*Después, la parte que importa:* añade un término $\propto1/r^3$ que simula la
corrección relativista, con la magnitud que produce los 43 segundos de arco por siglo de Mercurio.
¿Con qué paso puedes distinguir la precesión física de la numérica? Ese es
literalmente el problema que resuelven los códigos de efemérides.
:::

---

## 9. Lo esencial

::: esencial
* El orden de un método describe el error por paso; a tiempos largos importa
  el **tipo** de error: secular o acotado.
* Un sistema hamiltoniano exige un integrador simpléctico. RK4 de orden 4
  pierde frente a Verlet de orden 2 por un factor $10^4$ en deriva.
* Comprueba siempre las cantidades conservadas. Es el test más barato y el que
  detecta la clase de error que no se ve en la trayectoria.
* La órbita cerrada es una propiedad frágil del potencial $1/r$: cualquier
  perturbación produce precesión, y por eso la precesión es un observable
  valioso.
* El sistema solar es caótico con tiempo de Lyapunov de ~5 Ma. Lo que se puede
  afirmar a $10^8$ años es estadístico.
* El paso adaptativo rompe la simplecticidad.
:::

---

## 10. Preguntas abiertas

::: abierto
* ¿Se puede tener a la vez conservación exacta de la energía y del volumen de
  fases? (Hay un teorema que dice que no, salvo casos triviales. ¿Por qué?)
* ¿Cómo se hace paso adaptativo sin perder la simplecticidad?
* Si ninguna trayectoria a $10^8$ años es la real, ¿qué justifica exactamente
  las conclusiones estadísticas de esas integraciones?
* ¿Cuánto de la estabilidad observada del sistema solar es selección
  observacional: sólo vemos los sistemas que han sobrevivido?
:::

### Referencias

* **Poincaré, Henri.** *Sur le problème des trois corps et les équations de la
  dynamique.* Acta Mathematica **13** (1890). **Nivel A (primaria).**
* **Diacu, Florin y Holmes, Philip.** *Celestial Encounters.* Princeton UP,
  1996. La historia del premio y del error, documentada.
* **Hairer, E.; Lubich, C.; Wanner, G.** *Geometric Numerical Integration.*
  2.ª ed., Springer, 2006. **La referencia** sobre integradores que respetan la
  estructura.
* **Wisdom, Jack y Holman, Matthew.** *Symplectic maps for the n-body problem.*
  Astronomical Journal **102** (1991), 1528–1538. El integrador estándar en
  mecánica celeste.
* **Laskar, Jacques y Gastineau, Mickaël.** *Existence of collisional
  trajectories of Mercury, Mars and Venus with the Earth.* Nature **459**
  (2009), 817–819. El resultado estadístico sobre la estabilidad del sistema
  solar.
* **Murray, Carl y Dermott, Stanley.** *Solar System Dynamics.* Cambridge UP,
  1999. El manual.
