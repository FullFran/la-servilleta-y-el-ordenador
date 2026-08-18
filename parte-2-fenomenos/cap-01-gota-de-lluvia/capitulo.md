# II.1 — ¿Por qué cae una gota de lluvia como cae?

> **El fenómeno:** llueve.
> **Herramientas que convoca:** cap. 1 (estimación), cap. 2 (dimensiones),
> cap. 6 (EDO), cap. 8 (integración), cap. 13 (regímenes).
> **Lo que hay que llevarse:** que un mismo objeto obedece dos físicas
> distintas según su tamaño, y que la frontera se calcula.

---

## 1. Una pregunta

::: pregunta
Una gota de llovizna de 0,2 mm cae a 0,7 m/s: la sientes como humedad. Una
gota de tormenta de 5 mm cae a 9 m/s: la sientes como un golpe.

El diámetro se ha multiplicado por 25. La velocidad, sólo por 13.

**¿Por qué no por 25? ¿Y por qué no por $25^2$?**
:::

---

## 2. Antes de calcular

::: antes
1. ¿Cuánto tarda una gota en alcanzar su velocidad terminal? ¿Y cuántos metros
   recorre mientras tanto?
2. Si duplicas el diámetro, ¿por cuánto se multiplica la velocidad terminal?
3. ¿Por qué las nubes no caen, si están hechas de agua?
:::

---

## 3. La estimación primero

Del capítulo 1: en velocidad terminal, el peso iguala al arrastre. Con arrastre
cuadrático,

$$\tfrac43\pi r^3\rho_w g=\tfrac12 C_D\,\pi r^2\rho_a v_t^2
\quad\Longrightarrow\quad
v_t=\sqrt{\frac{8}{3}\frac{r\rho_w g}{C_D\rho_a}}$$

Con $r=1$ mm, $C_D\approx0{,}5$: $v_t\approx6{,}6$ m/s. El dato experimental
para una gota de 2 mm de diámetro es 6,49 m/s.

**Un 2 % de error con una línea de álgebra.** Merece la pena detenerse en eso:
no hemos resuelto ninguna ecuación diferencial ni hemos consultado ninguna
tabla salvo $C_D$.

Y la respuesta a la pregunta del principio ya está: $v_t\propto\sqrt{d}$, así
que multiplicar el diámetro por 25 multiplica la velocidad por 5. Salen 13 y no
5 porque **la llovizna no está en ese régimen**.

---

## 4. Dos regímenes y una frontera

![Velocidad terminal frente al tamaño. Izquierda: las dos leyes teóricas y los datos clásicos de Gunn y Kinzer (1949). Derecha: la trayectoria adimensionalizada, idéntica para todas las gotas. Lo que hay que concluir: las gotas pequeñas viven en el régimen de Stokes ($v\propto d^2$) y las grandes en el cuadrático ($v\propto\sqrt d$); la frontera está en $Re\approx1$.](figuras/fig_gota.pdf)

El número que decide es el Reynolds del capítulo 2:

$$Re=\frac{\rho_a v d}{\mu}$$

* $Re\ll1$: manda la viscosidad. Arrastre de Stokes, $F=6\pi\mu r v$, y de ahí
  $v_t=\frac{2r^2\rho_w g}{9\mu}\propto d^2$.
* $Re\gg1$: manda la inercia. Arrastre cuadrático, $v_t\propto\sqrt d$.

La frontera está en $d\approx80$ μm, con $v\approx19$ cm/s. Y de ahí sale la
respuesta a la tercera pregunta del apartado 2: **las gotitas de una nube miden
entre 10 y 20 μm** y caen a menos de 1 cm/s, tan despacio que cualquier corriente
ascendente las mantiene arriba. La nube no cae porque sus gotas están en el
régimen de Stokes.

Para que llueva hace falta que las gotitas crezcan hasta unos 100 μm, y ese
crecimiento —por coalescencia o por el mecanismo de Bergeron con cristales de
hielo— es el problema central de la física de nubes.

---

## 5. La ecuación, y por qué no hace falta resolverla

$$m\frac{dv}{dt}=mg-\tfrac12\rho_a C_D A v^2$$

Adimensionalizando con $v_t$ y $\tau=v_t/g$ (capítulo 2):

$$\frac{d\hat v}{d\hat t}=1-\hat v^2
\quad\Longrightarrow\quad
\hat v=\tanh\hat t$$

**Ninguna gota es distinta de otra.** Todas siguen esa curva; lo único que
cambia son las dos escalas.

Y de ahí salen los números que importan:

| Diámetro | $v_t$ | $\tau=v_t/g$ | Distancia hasta el 99 % de $v_t$ |
|---|---|---|---|
| 0,2 mm | 0,72 m/s | 0,073 s | **0,10 m** |
| 2 mm | 6,49 m/s | 0,66 s | **8,4 m** |
| 5 mm | 9,09 m/s | 0,93 s | **16,5 m** |

Las nubes están a kilómetros. **Toda gota de lluvia llega al suelo a velocidad
terminal**, siempre, y por eso la altura de la nube no influye en la fuerza del
impacto. Es un resultado que sorprende a mucha gente y que sale de comparar dos
longitudes.

---

## 6. ¿Qué estamos suponiendo?

::: supuestos
1. **Gota esférica.** Falso por encima de 1 mm: la gota se aplana, y por encima
   de 5–6 mm se rompe. Ese límite explica por qué **no existen gotas de lluvia
   de 1 cm**.
2. **$C_D$ constante e igual a 0,5.** Depende de $Re$ y de la deformación; los
   datos de Gunn y Kinzer lo incluyen implícitamente.
3. **Aire en reposo.** Falso en una tormenta, donde hay corrientes verticales de
   varios m/s.
4. **Densidad del aire constante.** Varía un 30 % entre el suelo y 3 km.
5. **Sin evaporación durante la caída.** Falso para gotas pequeñas en aire
   seco: la *virga* es lluvia que se evapora antes de llegar.
6. **Sin interacción entre gotas.** Falso en lluvia intensa: hay colisiones y
   coalescencia.
:::

---

## 7. ¿Cuándo falla?

::: falla
**Falla por encima de 6 mm.** La tensión superficial no puede sostener la gota
frente a la presión dinámica. El criterio es el número de Weber,
$We=\rho_a v^2 d/\gamma\approx10$: por encima, la gota se rompe. Por eso la
velocidad terminal se satura en unos 9–10 m/s y no crece más.

**Falla en el régimen intermedio.** Entre $Re\sim1$ y $Re\sim1000$ ninguna de
las dos leyes vale, y hay que usar correlaciones empíricas. Es el problema
habitual del capítulo 13: en la zona de transición no hay parámetro pequeño.

**Falla al ignorar el aire en movimiento.** En una tormenta las corrientes
ascendentes pueden superar la velocidad terminal de gotas medianas, que suben en
lugar de caer. Ese reciclado es lo que permite que crezca el granizo, y de ahí
salen piedras de varios centímetros.
:::

---

## 8. Historia

::: historia
**Gunn y Kinzer, 1949** · *Nivel de verificación: A.*

Los datos de la figura proceden de un experimento hecho con una elegancia
notable. Ross Gunn y Gilbert Kinzer, del Bureau of Standards, dejaban caer
gotas de tamaño controlado por un tubo vertical y medían su velocidad haciendo
que atravesaran dos anillos conductores: la gota, cargada, inducía un pulso al
pasar por cada uno, y el intervalo daba la velocidad.

Su tabla, publicada en el *Journal of Meteorology*, sigue siendo la referencia
setenta y cinco años después. La razón es instructiva: midieron con cuidado en
todo el rango relevante, documentaron sus incertidumbres y publicaron los datos
crudos. **Un buen conjunto de datos sobrevive a muchas teorías.**

**Stokes, 1851** · *Nivel de verificación: A.*

George Gabriel Stokes dedujo la ley del arrastre viscoso resolviendo las
ecuaciones de Navier–Stokes en el límite de $Re\to0$, donde el término
inercial desaparece y el problema se vuelve lineal. Su motivación era, en
parte, entender el movimiento de los péndulos usados en gravimetría: el aire
frenaba el péndulo y había que corregirlo.

Ese mismo resultado se usó medio siglo después para algo que Stokes no pudo
prever: Millikan lo empleó en 1909 para medir la carga del electrón a partir de
la velocidad de caída de gotitas de aceite. Y como vimos en el capítulo 15, usó
un valor de la viscosidad del aire algo incorrecto, lo que sesgó su resultado y
el de toda una generación posterior.
:::

---

## 9. Experimento computacional

::: experimento
**Construye el diagrama de regímenes.**

Integra numéricamente la caída con un arrastre que interpole entre Stokes y
cuadrático mediante la correlación de Schiller–Naumann,
$C_D=\frac{24}{Re}(1+0{,}15Re^{0{,}687})$ para $Re<1000$.

Barre el diámetro entre 1 μm y 6 mm y dibuja $v_t$ frente a $d$. Compara con
las dos leyes asintóticas y con los datos de Gunn y Kinzer.

*Qué comprobar:* que la curva empalma correctamente los dos regímenes, y que
las asintóticas se separan de ella exactamente donde esperabas por el criterio
de $Re$.

*Y después:* añade evaporación durante la caída con aire al 50 % de humedad.
¿A partir de qué tamaño llega la gota al suelo? Acabas de modelar la virga.
:::

---

## 10. Explícalo

::: explica
1. ¿Por qué las nubes no se caen?
2. ¿Por qué no existen gotas de lluvia de un centímetro?
3. ¿Por qué la altura de la nube no influye en lo fuerte que te da la gota?
4. ¿Por qué una gota diez veces más grande no cae diez veces más deprisa?
5. ¿Qué le pasaría a la lluvia en Marte, con una atmósfera cien veces menos
   densa?
:::

---

## 11. Lo esencial

::: esencial
* Un mismo objeto obedece dos físicas distintas según su tamaño, y la frontera
  la marca un número adimensional: $Re\approx1$, es decir $d\approx80$ μm.
* Stokes: $v_t\propto d^2$. Cuadrático: $v_t\propto\sqrt d$. La llovizna está
  en el primero y la lluvia en el segundo.
* Las nubes flotan porque sus gotitas miden micras. Que llueva exige
  crecimiento previo.
* Adimensionalizada, la caída es $\hat v=\tanh\hat t$: una sola curva para todas
  las gotas del universo.
* Toda gota llega al suelo a velocidad terminal, porque la necesita metros y la
  nube está a kilómetros.
* El tamaño máximo lo fija la rotura, $We\approx10$: por eso $v_t$ se satura
  en 9–10 m/s.
:::

---

## 12. Preguntas abiertas

::: abierto
* ¿Cómo crecen exactamente las gotitas de nube hasta el tamaño de lluvia? Es
  un problema abierto en detalle, y afecta a las predicciones de precipitación
  de los modelos climáticos.
* ¿Cuál es la distribución de tamaños de gota en una lluvia real, y de qué
  depende? (Marshall y Palmer, 1948, dieron una ley exponencial empírica que
  sigue usándose.)
* ¿Por qué el radar meteorológico mide reflectividad $\propto d^6$, y qué
  problema causa eso al estimar la lluvia?
* ¿Cómo cambia todo esto en la atmósfera de Titán, con metano líquido y
  gravedad siete veces menor?
:::

### Referencias

* **Gunn, Ross y Kinzer, Gilbert D.** *The terminal velocity of fall for water
  droplets in stagnant air.* Journal of Meteorology **6** (1949), 243–248.
  **Nivel A (primaria).** Los datos.
* **Stokes, George G.** *On the effect of the internal friction of fluids on the
  motion of pendulums.* Trans. Camb. Phil. Soc. **9** (1851). **Nivel A.**
* **Pruppacher, Hans y Klett, James.** *Microphysics of Clouds and
  Precipitation.* 2.ª ed., Springer, 2010. El tratado.
* **Villermaux, Emmanuel y Bossa, Benjamin.** *Single-drop fragmentation
  determines size distribution of raindrops.* Nature Physics **5** (2009),
  697–702. Por qué la distribución de tamaños es la que es.
* **Marshall, J. S. y Palmer, W. M.** *The distribution of raindrops with size.*
  Journal of Meteorology **5** (1948), 165–166. Dos páginas, todavía en uso.
