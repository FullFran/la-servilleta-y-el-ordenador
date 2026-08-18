# II.7 — ¿Cómo se propaga una sustancia?

> **El fenómeno:** echas una gota de tinta en agua quieta.
> **Herramientas:** cap. 3 (paseo aleatorio), cap. 8 (EDP), cap. 9 (Monte
> Carlo), cap. 12 (Fourier).
> **Lo que hay que llevarse:** que el mismo fenómeno admite tres
> descripciones equivalentes, y que la elección entre ellas es de conveniencia,
> no de verdad.

---

## 1. Una pregunta

::: pregunta
Una molécula de perfume difunde en aire quieto con $D\approx10^{-5}$ m²/s.

**¿Cuánto tarda en cruzar una habitación de 5 m?**

Y una segunda: si la respuesta es lo que sospechas, **¿por qué hueles el
perfume en segundos?**
:::

---

## 2. Antes de calcular

::: antes
1. Tu estimación del tiempo de difusión en 5 m.
2. Si duplicas la distancia, ¿se duplica el tiempo?
3. ¿Cuánto tarda una molécula en difundir 1 μm, el tamaño de una bacteria?
:::

---

## 3. Tres descripciones del mismo fenómeno

![Difusión, tres veces. Izquierda: paseos aleatorios individuales. Centro: el desplazamiento cuadrático medio, con exponente medido 1,0000. Derecha: el histograma de 20 000 partículas frente a la solución de la EDP. Lo que hay que concluir: las tres descripciones coinciden, y cada una es cómoda para preguntas distintas.](figuras/fig_difusion.pdf)

**Microscópica: paseo aleatorio.** Cada partícula da pasos independientes. Del
capítulo 3, $\langle x^2\rangle=n\ell^2$, y con $n=t/\Delta t$ sale
$\langle x^2\rangle=2Dt$ con $D=\ell^2/(2\Delta t)$.

**Macroscópica: la EDP.** $\partial_t c=D\partial_x^2c$, cuya solución para una
fuente puntual es una gaussiana que se ensancha como $\sqrt{2Dt}$.

**Estocástica: la ecuación de Langevin.** $dx=\sqrt{2D}\,dW$, que es la
descripción intermedia y la que se simula cuando hay además arrastre,
confinamiento o reacciones.

Las tres son **la misma física**. La primera es cómoda para entender el
mecanismo, la segunda para geometrías y contornos, la tercera para incluir
efectos adicionales.

---

## 4. La raíz del tiempo, y sus consecuencias

$$\langle x^2\rangle=2Dt \quad\Longrightarrow\quad t\sim\frac{L^2}{2D}$$

**El tiempo escala con el cuadrado de la distancia.** Ese único hecho tiene
consecuencias enormes:

| Distancia | Tiempo de difusión (aire, $D=10^{-5}$) |
|---|---|
| 1 μm | 0,05 ms |
| 1 mm | 50 s |
| 1 cm | 1,4 h |
| 1 m | **14 días** |
| 5 m | **1 año** |

Y ahí está la respuesta a la pregunta del principio: **hueles el perfume en
segundos porque el aire no está quieto**. La convección, aunque sea la de las
corrientes térmicas de tu propio cuerpo, transporta en segundos lo que la
difusión tardaría un año.

El número que compara ambos mecanismos es el Péclet del capítulo 2,
$Pe=UL/D$. Con $U=0{,}1$ m/s y $L=5$ m: $Pe=5\times10^4$. La difusión es
irrelevante para el transporte a esa escala.

Pero al revés, en el otro extremo: **para una bacteria de 1 μm, la difusión es
instantánea y la convección inútil**. Una bacteria no necesita un sistema
circulatorio, y no puede usar la natación para llevar nutrientes a su interior:
el Péclet a esa escala es $10^{-2}$. La misma física, invertida por el tamaño.

Ese cambio de régimen a escala celular es lo que explica la existencia de
sistemas circulatorios en organismos grandes: **el transporte por difusión es
inviable más allá de unos milímetros**, y todo organismo mayor necesita bombear.

---

## 5. Y cuando no es difusión

No todo lo que se propaga difunde. El diagnóstico está en el exponente del
desplazamiento cuadrático medio:

$$\langle x^2\rangle\propto t^{\alpha}$$

* $\alpha=1$: **difusión normal**.
* $\alpha<1$: **subdifusión**. Aparece en medios abarrotados —el citoplasma
  celular—, con trampas o con memoria.
* $\alpha>1$: **superdifusión**. Vuelos de Lévy, transporte turbulento,
  búsqueda animal.
* $\alpha=2$: transporte balístico, sin colisiones.

Medir ese exponente es una de las cosas más informativas que se pueden hacer con
una trayectoria experimental, y con datos de seguimiento de partículas
individuales se hace rutinariamente en biofísica.

---

## 6. ¿Cuándo falla?

::: falla
**Falla si hay convección**, que es casi siempre en fluidos a escala humana.

**Falla en medios heterogéneos.** Un $D$ efectivo único puede no existir si el
medio tiene estructura a todas las escalas.

**Falla la aproximación continua a tiempos cortos**, cuando la partícula ha
dado pocos pasos.

**Y falla el problema inverso.** Reconstruir la condición inicial a partir de
la concentración actual es el problema mal condicionado por excelencia: en
Fourier hay que dividir por $e^{-Dk^2t}$, y eso amplifica el ruido de forma
explosiva. Capítulo II.14.
:::

---

## 7. Historia

::: historia
**Brown, Einstein y Perrin** · *Nivel de verificación: A.*

En 1827, el botánico Robert Brown observó al microscopio que los granos de
polen en suspensión se movían erráticamente. Comprobó cuidadosamente que no era
un efecto vital, repitiendo con polvo de roca y con fragmentos de una esfinge
egipcia.

En 1905, Einstein publicó la explicación: el movimiento es el resultado de los
choques con las moléculas del fluido, y predijo $\langle x^2\rangle=2Dt$ con
$D=RT/(6\pi\eta aN_A)$. Lo notable es el objetivo: Einstein no buscaba explicar
el movimiento browniano, buscaba **una prueba de que los átomos existen**, en
una época en la que eso todavía se discutía.

Jean Perrin lo verificó experimentalmente entre 1908 y 1913, midiendo
desplazamientos de partículas y obteniendo el número de Avogadro. Recibió el
Nobel en 1926, y la comunidad científica dio por zanjada la discusión sobre la
realidad atómica.

**La cadena completa** —observación (1827), modelo (1905), verificación (1909),
consecuencia conceptual— tardó ochenta años y es un ejemplo de manual del ciclo
del capítulo 14.
:::

---

## 8. Experimento computacional

::: experimento
**Difusión con reacción: cómo aparece una escala de longitud.**

Simula partículas que difunden y además desaparecen con tasa $k$ (por ejemplo,
una molécula señalizadora que se degrada). La ecuación es
$\partial_tc=D\partial_x^2c-kc$.

*Predice antes:* ¿existe un estado estacionario? ¿Con qué perfil?

*Qué sale:* un perfil exponencial $c\propto e^{-x/\lambda}$ con
$\lambda=\sqrt{D/k}$. **La combinación de difusión y degradación genera una
longitud característica** que no estaba en ninguno de los dos ingredientes por
separado.

Ese es exactamente el mecanismo de los gradientes de morfógenos en el desarrollo
embrionario, y la razón por la que un embrión puede «medir» distancias.
:::

---

## 9. Lo esencial

::: esencial
* Tres descripciones equivalentes: paseo aleatorio, EDP y Langevin. Elegir
  entre ellas es conveniencia, no verdad.
* $\langle x^2\rangle=2Dt$: el tiempo va como el **cuadrado** de la distancia.
* Por eso la difusión gobierna a escala celular y es irrelevante a escala
  humana. El número que decide es el Péclet.
* Todo organismo mayor que unos milímetros necesita bombear: la difusión no
  llega.
* El exponente del MSD es un diagnóstico: $\alpha<1$ subdifusión, $\alpha>1$
  superdifusión.
* Difusión + degradación genera una longitud, $\sqrt{D/k}$, que no estaba en
  los ingredientes.
:::

---

## 10. Preguntas abiertas

::: abierto
* ¿Qué mecanismos producen subdifusión en el citoplasma, y se pueden distinguir
  midiendo?
* ¿Cómo se define un $D$ efectivo en un medio con estructura fractal?
* ¿Cuál es el límite de tamaño de un organismo sin sistema circulatorio, y qué
  organismos lo apuran?
* Si el problema inverso de la difusión está mal condicionado, ¿cómo funcionan
  las técnicas de imagen que lo resuelven?
:::

### Referencias

* **Einstein, Albert.** *Über die von der molekularkinetischen Theorie der Wärme
  geforderte Bewegung…* Annalen der Physik **17** (1905), 549–560.
  **Nivel A (primaria).**
* **Perrin, Jean.** *Les Atomes*, 1913. **Nivel A (primaria).**
* **Berg, Howard C.** *Random Walks in Biology.* Princeton UP, 1993. **La
  referencia del capítulo**: corto, claro y lleno de estimaciones biológicas.
* **Crank, John.** *The Mathematics of Diffusion.* 2.ª ed., Oxford UP, 1975.
* **Metzler, Ralf y Klafter, Joseph.** *The random walk's guide to anomalous
  diffusion.* Physics Reports **339** (2000), 1–77. Sub y superdifusión.
* **Wolpert, Lewis.** *Positional information and the spatial pattern of
  cellular differentiation.* J. Theor. Biol. **25** (1969), 1–47. Gradientes de
  morfógenos.
