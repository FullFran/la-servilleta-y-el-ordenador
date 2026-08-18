# II.2 — ¿Cuánto tarda algo en enfriarse?

> **El fenómeno:** el café de la mesa está tibio.
> **Herramientas que convoca:** cap. 1, cap. 2 (Biot), cap. 5 (ajuste),
> cap. 6 (EDO), cap. 14 (modelo mínimo).
> **Lo que hay que llevarse:** que «la ley de Newton del enfriamiento» es la
> suma disfrazada de tres mecanismos con tres dependencias distintas, y cómo se
> averigua cuál manda.

---

## 1. Una pregunta

::: pregunta
Sirves el café a 92 °C y lo dejas. Vuelves a los veinte minutos y está a 60.

**¿Cuál de los tres mecanismos —convección, radiación, evaporación— se ha
llevado más calor?**

Y una pregunta más incómoda: **¿cómo lo averiguarías sin buscarlo?**
:::

Esta es la quinta visita a la taza de café. En el capítulo 1 estimamos la
potencia; en el 5 ajustamos datos; en el 6 dedujimos la ecuación; en el 14
descubrimos que el modelo mínimo dejaba residuos con forma. Aquí desmontamos el
coeficiente $h$ y miramos qué hay dentro.

---

## 2. Antes de calcular

::: antes
1. Ordena los tres mecanismos por importancia a 90 °C. Apunta tus porcentajes.
2. ¿Cambia el orden a 30 °C?
3. Si soplas el café, ¿qué mecanismo estás modificando?
:::

---

## 3. Tres mecanismos, tres dependencias

Cada mecanismo tiene una firma funcional distinta, y ahí está la clave para
separarlos:

| Mecanismo | Ley | Dependencia con $\Delta T$ |
|---|---|---|
| Convección | $hA\,\Delta T$ | lineal (y $h\propto\Delta T^{1/4}$ en natural) |
| Radiación | $\varepsilon\sigma A(T^4-T_a^4)$ | ligeramente superlineal |
| Evaporación | $L\,k_m A\,\Delta\rho_v$ | **exponencial**, vía Clausius–Clapeyron |

![Los tres mecanismos. Izquierda: potencia perdida por cada uno frente a la temperatura. Derecha: la fracción que aporta cada uno. Lo que hay que concluir: los tres son del mismo orden, así que ninguno se puede despreciar, y sus proporciones cambian con la temperatura.](figuras/fig_mecanismos_cafe.pdf)

Con los parámetros del modelo —taza de 250 g, superficie libre 64 cm², pared
200 cm², $h_{\text{ef}}=6$ W/(m²·K), $\varepsilon=0{,}9$, $k_m=1{,}3$ mm/s— sale:

| $T$ | Convección | Radiación | Evaporación | Total |
|---|---|---|---|---|
| 90 °C | 34 % | 41 % | 25 % | 32 W |
| 70 °C | 39 % | 43 % | 19 % | 20 W |
| 50 °C | 43 % | 43 % | 14 % | 11 W |
| 30 °C | 45 % | 41 % | 13 % | 3,2 W |

::: aviso
**Estos porcentajes dependen de parámetros estimados, y hay que decirlo.**
El coeficiente de transferencia de masa $k_m$ es el peor conocido: variarlo un
factor 2 mueve la fracción de evaporación entre el 14 % y el 40 % a 90 °C.
Los valores publicados para tazas abiertas dan a la evaporación entre el 25 % y
el 60 % según la geometría y la humedad ambiente.

Es decir: **el modelo con parámetros de manual no resuelve la pregunta**. Hay
que medir. Y eso es exactamente lo interesante.
:::

---

## 4. Cómo se separan experimentalmente

Tres experimentos, cada uno diseñado para anular un mecanismo:

**Pesar la taza.** La evaporación quita masa; los otros dos no. Multiplicando
por el calor latente se obtiene directamente la energía perdida por
evaporación. Coste: una báscula de cocina de 0,1 g.

**Tapar la taza.** Elimina la evaporación casi por completo y apenas afecta a
la radiación (la tapa se calienta y radia parecido). La diferencia entre
$\tau$ con y sin tapa es una medida de la evaporación.

**Envolver en papel de aluminio brillante.** El aluminio pulido tiene
$\varepsilon\approx0{,}05$ frente al 0,9 de la cerámica. Reduce la radiación en
un factor 15 y no cambia la convección apreciablemente.

**El diseño completo es un factorial $2^2$**: con/sin tapa × con/sin aluminio,
cuatro experimentos. Con eso se estiman los tres mecanismos y su interacción, y
cuesta una tarde y cuatro euros.

Esa es la respuesta a la segunda pregunta del apartado 1, y es una lección
general: **cuando dos mecanismos ajustan igual, no se separan con más datos del
mismo tipo, sino con un experimento que anule uno de ellos**.

---

## 5. Y el modelo mínimo, ¿por qué funcionaba tan bien?

Aquí está la parte conceptualmente interesante. Si hay tres mecanismos con
dependencias distintas, ¿por qué una sola exponencial ajusta razonablemente?

Porque **en el rango de temperaturas de una taza, los tres son
aproximadamente lineales en $\Delta T$**:

* La convección lo es por definición.
* La radiación: $T^4-T_a^4\approx4T_a^3\Delta T$ con un error del 25 % para
  $\Delta T=70$ K, y menor después.
* La evaporación es la que peor se porta, pero su contribución baja
  precisamente cuando su no linealidad importaría más.

La suma de tres cosas casi lineales es casi lineal, con un $h$ efectivo que es
la suma de los tres. **La ley de Newton del enfriamiento no es una ley: es la
linealización conjunta de tres procesos distintos alrededor del régimen en el
que vivimos.**

Y de ahí sale una predicción falsable: si el modelo lineal es una linealización,
su $\tau$ ajustado debería **depender del rango de temperaturas ajustado**.
Ajustando sólo los primeros diez minutos sale un $\tau$ menor que ajustando la
hora completa. Eso es exactamente lo que se observa, y es la firma inconfundible
de un modelo linealizado usado fuera de su punto de expansión.

---

## 6. ¿Cuándo falla?

::: falla
**Falla con salto térmico grande.** Un lingote al rojo pierde calor
mayoritariamente por radiación, que va como $T^4$: la linealización es absurda
y $\tau$ no significa nada.

**Falla si el objeto no está a temperatura uniforme.** Criterio de Biot. Una
taza de café se mezcla por convección natural interna; una taza de sopa espesa,
no, y desarrolla gradientes de varios grados.

**Falla con corriente de aire.** La convección forzada multiplica $h$ por 3 o
más, y entonces sí domina claramente. Soplar el café ataca la convección **y**
la evaporación, al renovar el aire húmedo de la superficie.

**Falla al ignorar la masa térmica de la taza.** Una taza de cerámica gruesa
tiene una capacidad térmica del 15–25 % de la del café, y su temperatura va
retrasada: el sistema tiene **dos** masas térmicas y por tanto dos escalas de
tiempo, que es justamente lo que se observó en el capítulo 14.
:::

---

## 7. Historia

::: historia
**Dulong, Petit y la ley que sustituyó a la de Newton** ·
*Nivel de verificación: A.*

En 1817, Pierre Louis Dulong y Alexis Thérèse Petit publicaron un estudio
experimental sistemático del enfriamiento, hecho en el vacío y en aire a
distintas presiones. Encontraron que la ley de Newton fallaba claramente para
saltos térmicos grandes, y propusieron una ley empírica exponencial para la
parte radiativa.

Su trabajo es un modelo metodológico: separaron los mecanismos experimentalmente
—midiendo en vacío para eliminar la convección— en lugar de intentar
distinguirlos ajustando curvas.

Sesenta años después, Stefan (1879) dedujo empíricamente la ley $T^4$ a partir
de datos que incluían los de Dulong y Petit, y Boltzmann (1884) la dedujo
teóricamente a partir de la termodinámica de la presión de radiación.

**El recorrido completo —de la ley empírica de Newton a la linealización, a la
detección experimental de su fallo, a la ley correcta, a su deducción teórica—
tardó doscientos años** y es un buen recordatorio de cuánto trabajo hay detrás
de las fórmulas que damos por evidentes.
:::

---

## 8. Experimento computacional

::: experimento
**El experimento factorial completo.**

Mide el enfriamiento en las cuatro condiciones: taza desnuda, tapada,
envuelta en aluminio, y tapada + envuelta. Toma temperatura cada 2 minutos
durante una hora, y **pesa la taza al principio y al final en los cuatro
casos**.

*Análisis.* Ajusta un modelo con tres términos y estima los tres coeficientes
usando las cuatro condiciones simultáneamente. Compara la energía de
evaporación deducida del ajuste con la deducida del cambio de masa: **son dos
medidas independientes de la misma cantidad**.

*Qué falsaría el modelo:* si las dos estimaciones de la evaporación difieren en
más de un factor 2, hay un mecanismo sin contabilizar. El candidato más
probable es la conducción por la base hacia la mesa, que no hemos incluido.
:::

---

## 9. Lo esencial

::: esencial
* «La ley de Newton del enfriamiento» es la linealización conjunta de tres
  mecanismos distintos, no una ley.
* Los tres son del mismo orden en una taza: ninguno se desprecia sin medir.
* Cada mecanismo tiene una firma funcional propia, y ahí está la manera de
  separarlos.
* Cuando dos mecanismos ajustan igual, no se separan con más datos: se separan
  **anulando uno**. Un diseño factorial $2^2$ cuesta una tarde.
* Un modelo linealizado se delata porque su parámetro ajustado depende del
  rango ajustado.
* Pesar la taza es una medida independiente de la evaporación, y comparar dos
  medidas independientes de la misma cantidad es el mejor control que existe.
:::

---

## 10. Preguntas abiertas

::: abierto
* ¿Cuánto cambia el reparto entre mecanismos con la humedad ambiente? ¿Se puede
  usar una taza de café como higrómetro?
* ¿Por qué la leche fría añadida al principio hace que el café esté más caliente
  al final que si se añade después? (Es un problema clásico y la respuesta
  depende de qué mecanismo domine.)
* ¿Cómo se diseña una taza que mantenga el café a temperatura bebible el máximo
  tiempo? ¿Qué mecanismo hay que atacar primero?
* En medicina forense se estima la hora de la muerte por enfriamiento del
  cuerpo. ¿Qué mecanismos dominan ahí, y qué incertidumbre tiene el método?
:::

### Referencias

* **Dulong, P. L. y Petit, A. T.** *Recherches sur la mesure des températures et
  sur les lois de la communication de la chaleur.* Annales de Chimie et de
  Physique **7** (1817), 225–264, 337–367. **Nivel A (primaria).**
* **Incropera, F. et al.** *Fundamentals of Heat and Mass Transfer.* 7.ª ed.,
  Wiley, 2011, capítulos 1, 5 y 6. Coeficientes, número de Biot y transferencia
  simultánea de calor y masa.
* **Henssge, C. y Madea, B.** *Estimation of the time since death.* Forensic
  Science International **165** (2007), 182–184. El mismo problema aplicado a
  cuerpos humanos, con sus incertidumbres declaradas.
* **Rees, W. G. y Viney, C.** *On cooling tea and coffee.* American Journal of
  Physics **56** (1988), 434–437. El problema de la leche, hecho con cuidado.
