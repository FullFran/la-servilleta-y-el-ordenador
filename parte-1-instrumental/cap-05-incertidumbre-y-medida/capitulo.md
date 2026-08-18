# Capítulo 5 — Incertidumbre y medida

> **Qué sabrás hacer al terminar**
> · Distinguir error de incertidumbre, y sistemático de aleatorio ·
> Propagar incertidumbres y saber cuándo la fórmula lineal miente ·
> Ajustar un modelo a datos y leer la matriz de covarianza ·
> Diagnosticar un modelo mal especificado mirando los residuos ·
> Decir qué significa exactamente «compatible con los datos».
>
> **Herramientas que usa:** capítulos 1, 3 y 4.
> **Disciplinas de los ejemplos:** astronomía, metrología industrial, biología
> de laboratorio, ingeniería, cervecería.
> **Deuda que paga:** la propagación de errores del capítulo 1, ahora en serio.
> **Deuda que abre:** cómo se decide entre modelos (capítulo 15) y cómo se
> hace inferencia cuando la verosimilitud es intratable (capítulo 9).

---

## 1. Una pregunta

::: pregunta
Mides diez veces el mismo objeto y obtienes
$12{,}31$, $12{,}28$, $12{,}33$, $12{,}30$, $12{,}29$, $12{,}31$, $12{,}32$,
$12{,}30$, $12{,}29$, $12{,}31$ mm.

La desviación típica de la media sale $0{,}005$ mm.

**¿Puedes escribir $12{,}304\pm0{,}005$ mm?**
:::

Casi seguro que no. Y la razón no está en ninguno de esos diez números: está en
todo lo que no has escrito. ¿Estaba el calibre calibrado? ¿A qué temperatura?
¿Aprietas siempre igual? ¿El objeto es realmente cilíndrico?

Los diez números miden **la repetibilidad de tu procedimiento**. No miden la
distancia entre tu resultado y la verdad. Confundir esas dos cosas es el error
más caro de la metrología práctica, y este capítulo trata de por qué.

---

## 2. Antes de calcular

::: antes
1. Si promedias 100 medidas en vez de 10, ¿cuánto mejora tu resultado?
2. Mides $x=1{,}0\pm0{,}4$ y necesitas $1/x$. ¿Cuál es la incertidumbre de
   $1/x$?
3. Ajustas una recta y obtienes $R^2=0{,}98$. ¿Es un buen ajuste?

Las tres respuestas «obvias» son falsas, cada una por una razón distinta.
:::

---

## 3. La intuición

### 3.1 Error, incertidumbre y las palabras que importan

El vocabulario aquí no es pedantería: es lo que impide razonar mal.

* **Error** es la diferencia entre tu resultado y el valor verdadero. Es un
  número **desconocido y no cognoscible**: si lo conocieras, corregirías.
* **Incertidumbre** es la anchura del intervalo dentro del cual crees
  razonablemente que está el valor verdadero. Es un número **que tú calculas y
  declaras**.

El estándar internacional (el *GUM*, JCGM 100:2008) clasifica las
incertidumbres por **cómo las has evaluado**, no por su origen físico:

* **Tipo A**: evaluada por análisis estadístico de observaciones repetidas.
* **Tipo B**: evaluada por cualquier otro medio (certificado de calibración,
  especificación del fabricante, juicio experto, resolución del instrumento).

Es una clasificación que sorprende a mucha gente porque no coincide con
sistemático/aleatorio. Un efecto sistemático puede evaluarse por tipo A (si lo
has medido repitiendo en condiciones distintas) y uno aleatorio por tipo B (si
lo estimas del manual). El GUM insiste en esta distinción porque la pregunta
operativa no es «¿de dónde viene?» sino «¿cómo sé cuánto vale?».

### 3.2 El sesgo es un suelo

La distinción que sí es física es otra: **aleatorio frente a sistemático**.

![Cuatro combinaciones de sesgo y dispersión. Arriba: dianas. Abajo: el error de la media al promediar más medidas. Lo que hay que concluir: la dispersión baja como $1/\sqrt n$; el sesgo no baja nunca. Promediar es un remedio para la mitad de tus problemas.](figuras/fig_sesgo_dispersion.pdf)

El error total de la media de $n$ medidas es

$$\sigma_{\text{total}}=\sqrt{b^{2}+\frac{\sigma^{2}}{n}}$$

donde $b$ es el sesgo. Cuando $n$ crece, el segundo término se desvanece y
queda $b$. **A partir de $n\approx(\sigma/b)^2$, seguir midiendo no sirve de
nada.** Con $\sigma=0{,}5$ y $b=0{,}05$, ese número es 100: la medida 101 y la
medida 10 000 valen exactamente lo mismo.

Esa cuenta debería hacerse **antes** de empezar a medir, y casi nunca se hace.
Es la versión metrológica de la regla del capítulo 1: afina el factor peor
conocido, no el que sabes afinar.

---

## 4. La matemática

### 4.1 Propagación: la fórmula y su letra pequeña

Si $y=f(x_1,\dots,x_n)$ y las incertidumbres son pequeñas, un desarrollo de
Taylor a primer orden da

$$\sigma_y^{2}=\sum_i\left(\frac{\partial f}{\partial x_i}\right)^{2}\sigma_i^{2}
+2\sum_{i<j}\frac{\partial f}{\partial x_i}\frac{\partial f}{\partial x_j}\,
\sigma_{ij}$$

El segundo sumatorio es el que todo el mundo omite y a veces domina. Para
funciones producto o cociente, la fórmula se simplifica a la regla que
usábamos en el capítulo 1: **las incertidumbres relativas se suman en
cuadratura**.

La letra pequeña está en «a primer orden». Esa aproximación exige que $f$ sea
casi lineal **en el rango que abarca tu incertidumbre**. Cuando no lo es, la
fórmula puede fallar de dos maneras distintas.

![Cuándo miente la propagación lineal. Arriba: $f(x)=x^2$ con un 5 % de incertidumbre; la linealización es excelente, pero aparece un sesgo. Abajo: $f(x)=1/x$ con un 40 %; la distribución de salida no se parece en nada a una gaussiana. Lo que hay que concluir: la fórmula lineal da la anchura correcta sólo si la función es casi recta en el rango de tu error.](figuras/fig_propagacion.pdf)

**Fallo 1: aparece un sesgo.** Para $f(x)=x^2$, aunque la anchura sale
perfecta ($\sigma_{MC}/\sigma_{\text{lin}}=1{,}000$), la media de $f$ no es
$f$ de la media: $E[x^2]=x_0^2+\sigma^2$, un sesgo de $+0{,}25$ en nuestro
ejemplo. Toda función con curvatura introduce este sesgo, de magnitud
$\tfrac12 f''\sigma^2$. Con incertidumbres pequeñas es despreciable; con
incertidumbres grandes, no.

**Fallo 2: la distribución deja de tener sentido.** Para $f(x)=1/x$ con $x$
normal, la fórmula lineal da un número, la simulación da otro cien veces mayor,
y **ninguno de los dos significa nada**: si $x$ puede estar cerca de cero,
$1/x$ no tiene ni media ni varianza finitas. Es la log-normal del capítulo 1 y
la Cauchy del capítulo 3 reapareciendo. La lección práctica es dura y sencilla:

> Cuando la incertidumbre relativa de un denominador supera el 20 %, deja de
> propagar fórmulas y simula.

::: herramientas
**Propagación por Monte Carlo, en seis líneas**

```python
import numpy as np
rng = np.random.default_rng(0)
N = 200_000
x = rng.normal(x0, sigma_x, N)
y = rng.normal(y0, sigma_y, N)
resultado = f(x, y)                     # la función completa, sin linealizar
print(np.percentile(resultado, [16, 50, 84]))
```

Es el método recomendado por el propio GUM en su Suplemento 1 (JCGM 101:2008).
Ventajas: no linealiza, no supone normalidad de la salida, trata correlaciones
si generas con `multivariate_normal`, y funciona con funciones que no tienen
derivada analítica. Coste: cinco segundos de CPU. **No hay ninguna razón para
seguir propagando a mano salvo que quieras la fórmula simbólica.**
:::

### 4.2 Mínimos cuadrados, y de dónde salió

Ajustar es elegir los parámetros que hacen el modelo más compatible con los
datos. Si los errores son gaussianos, independientes y de varianzas conocidas
$\sigma_i$, la verosimilitud es

$$\mathcal{L}(\theta)=\prod_i \frac{1}{\sqrt{2\pi}\sigma_i}
\exp\!\left[-\frac{(y_i-f(x_i;\theta))^2}{2\sigma_i^2}\right]$$

y maximizarla equivale a minimizar

$$\chi^2(\theta)=\sum_i\frac{\big(y_i-f(x_i;\theta)\big)^2}{\sigma_i^2}$$

Este es el punto que conviene no olvidar: **mínimos cuadrados no es un método
neutro**. Es máxima verosimilitud bajo el supuesto de errores gaussianos
independientes. Si los errores no lo son —si hay valores atípicos, o
correlación, o varianzas mal estimadas— el estimador sigue funcionando, pero ya
no es óptimo y puede ser muy malo.

### 4.3 El diagnóstico que importa: los residuos

Existe una tentación universal: mirar $R^2$, ver 0,98 y darse por satisfecho.

![Un ajuste con $R^2=0{,}98$ que está mal. Arriba: ajuste lineal y cuadrático a los mismos datos. Abajo: los residuos. Lo que hay que concluir: los dos $R^2$ son casi iguales; los residuos no se parecen en nada. La estructura en los residuos es la firma de un modelo mal especificado.](figuras/fig_residuos.pdf)

El modelo lineal da $R^2=0{,}981$ y el cuadrático $0{,}991$. Con esa cifra sola
nadie rechazaría el lineal. Pero los residuos del ajuste lineal dibujan una
parábola perfecta: **el modelo está sistemáticamente mal en los extremos y
sistemáticamente bien en el centro**, que es lo que ocurre cuando ajustas una
recta a algo curvo.

Dos indicadores hacen el trabajo que $R^2$ no hace:

**El $\chi^2$ reducido.** $\chi^2_\nu=\chi^2/(N-k)$, con $N$ datos y $k$
parámetros. Si el modelo es correcto y las $\sigma_i$ son honestas,
$\chi^2_\nu\approx1$. En la figura vale 2,15 para el lineal y 1,04 para el
cuadrático. La diferencia es diagnóstica y $R^2$ no la ve.

**La gráfica de residuos.** Si tiene forma, el modelo está mal o las barras de
error lo están. Es la gráfica más barata y más ignorada de la ciencia
experimental.

::: aviso
**El $\chi^2_\nu$ corta por los dos lados.**

* $\chi^2_\nu\gg1$: o el modelo es incorrecto, o has subestimado tus errores.
* $\chi^2_\nu\ll1$: **has sobreestimado tus errores**, o —peor— los datos han
  sido ajustados, seleccionados o suavizados antes de llegarte.

Un $\chi^2_\nu$ de 0,3 no es «un ajuste buenísimo». Es una señal de alarma. En
el capítulo 15 veremos casos históricos donde ese olor delató datos demasiado
buenos para ser ciertos.
:::

### 4.4 La matriz de covarianza: lo que las barras de error no dicen

Al ajustar, no obtienes números independientes: obtienes una **distribución
conjunta** de parámetros. La curvatura del $\chi^2$ en el mínimo da la matriz
de covarianza,

$$V=2\left(\frac{\partial^2\chi^2}{\partial\theta_i\partial\theta_j}\right)^{-1}$$

y sus elementos fuera de la diagonal contienen información que se pierde en
cuanto escribes «$A=100{,}4\pm2{,}6$» y «$\tau=3{,}99\pm0{,}20$» y tiras el
resto.

![Lo que se pierde al tirar la covarianza. Izquierda: la elipse real de incertidumbre (azul) frente a lo que crees si sólo guardas las dos barras de error (rojo). Derecha: la banda de predicción resultante. Lo que hay que concluir: con $\rho=-0{,}71$, ignorar la correlación infla la predicción y la deforma.](figuras/fig_covarianza.pdf)

La correlación entre amplitud y tiempo característico es $-0{,}71$, y tiene
sentido físico: si el ajuste sube la amplitud, tiene que bajar $\tau$ para
seguir pasando por los datos. Las combinaciones $(A\uparrow,\tau\uparrow)$
están **excluidas por los datos**, y sin embargo aparecen si muestreas los dos
parámetros por separado.

La consecuencia práctica: **guarda siempre la matriz de covarianza, no sólo
las diagonales.** En cuanto vayas a propagar a una cantidad derivada, la
necesitarás; y si la has tirado, tu banda de predicción será falsa —y del lado
optimista o pesimista según el signo, así que ni siquiera puedes decir que
«pecas de prudente»—.

### 4.5 Qué significa «compatible con los datos»

Esta frase se usa constantemente y casi siempre significa una de estas cuatro
cosas distintas:

1. El $\chi^2_\nu$ es cercano a 1.
2. Los residuos no muestran estructura.
3. El valor del modelo cae dentro de las barras de error de los datos.
4. No se puede rechazar el modelo con los datos disponibles.

Sólo la cuarta es honesta, y su honestidad viene de admitir lo que **no** dice:
compatible no es correcto. Con datos pobres, todo es compatible. La pregunta
útil no es «¿es compatible mi modelo?» sino **«¿qué modelos serían
incompatibles?»**. Si la respuesta es «ninguno», tus datos no informan, y ese es
un resultado que también hay que publicar.

---

## 5. El ordenador entra en escena

::: antes
Vamos a ajustar la ley de Newton del enfriamiento a tres tazas que empiezan a
temperaturas distintas. Antes de mirar:

* ¿Saldrá el mismo $\tau$ para las tres?
* ¿Se determinará mejor $\tau$ con la taza que empieza más caliente?
* En escala logarítmica, ¿qué forma tendrán las curvas?
:::

```python
import numpy as np
from scipy.optimize import curve_fit

def modelo(t, T_amb, T0, tau):
    return T_amb + (T0 - T_amb) * np.exp(-t / tau)

popt, pcov = curve_fit(modelo, t, T, p0=[20, 80, 20])
```

```text
T0= 88.0  ->  T_amb=20.60  tau=24.18 min  (sigma_tau=0.30)
T0= 65.0  ->  T_amb=21.08  tau=23.91 min  (sigma_tau=0.45)
T0= 45.0  ->  T_amb=20.65  tau=25.16 min  (sigma_tau=1.08)

tau medio = 24.42 min, dispersion = 0.66 min  (valor verdadero 24.0)
```

![La ley de Newton del enfriamiento con tres condiciones iniciales. Izquierda: las tres curvas. Derecha: en escala logarítmica son tres rectas paralelas. Lo que hay que concluir: $\tau$ sale idéntico en los tres casos porque el sistema olvida su condición inicial; el tiempo característico es una propiedad de la taza y del aire, no del café.](figuras/fig_taza_cafe.pdf)

Los tres $\tau$ son compatibles entre sí —24,2, 23,9 y 25,2 minutos, frente a
los 24,0 con que se generaron los datos— y esto no es un detalle técnico: es la
propiedad definitoria de los sistemas lineales de primer orden. **El tiempo
característico no depende del punto de partida.**

Pero fíjate en la tercera columna, que es la que de verdad enseña algo. La
barra de error de $\tau$ crece de 0,30 a 1,08 minutos al bajar la temperatura
inicial. Las tres tazas miden lo mismo; **no lo miden igual de bien**. La que
empieza a 45 °C recorre menos de dos constantes de tiempo por encima del ruido
del termómetro, y el ajuste lo paga. La taza fría no es una medida peor por
ser fría: es peor porque el rango dinámico de la señal es menor comparado con
el ruido, que es la misma razón por la que se mide con la señal grande siempre
que se puede. Volveremos a esta
taza en el capítulo 6 para derivar la ecuación, en el 14 para criticarla y en
el II.2 para descubrir dónde falla.

::: juega
1. Reduce el rango temporal a los primeros 10 minutos. ¿Cuánto empeora la
   determinación de $\tau$? ¿Y la de $T_{\text{amb}}$? ¿Cuál se degrada antes?
2. Fija $T_{\text{amb}}$ a un valor medido con termómetro en vez de ajustarlo.
   Mira cómo cambian las barras de error de los otros dos parámetros. ¿Por qué
   mejora tanto?
3. Añade un valor atípico (una lectura mal anotada, 30 °C de más). ¿Cuánto se
   mueve el ajuste? Repite con un ajuste robusto (`loss='soft_l1'` en
   `least_squares`).
4. Mide $\rho$ entre $\tau$ y $T_{\text{amb}}$. ¿Por qué es tan grande, y qué
   diseño experimental lo reduciría?
:::

---

## 6. ¿Qué estamos suponiendo?

::: supuestos
1. **Que las $\sigma_i$ son conocidas y correctas.** Casi nunca lo son; se
   estiman, y esa estimación tiene su propia incertidumbre.
2. **Que los errores son independientes entre puntos.** Falso en casi cualquier
   serie temporal, donde la deriva del instrumento correlaciona medidas
   próximas.
3. **Que los errores son gaussianos.** Razonable por el TCL cuando el error
   total es suma de muchas causas; falso cuando domina una sola causa o cuando
   hay valores atípicos.
4. **Que no hay error en la variable independiente.** Mínimos cuadrados
   ordinarios lo supone. Si $x$ también tiene error, el ajuste está sesgado
   (*atenuación por error de medida*) y hay que usar regresión ortogonal.
5. **Que el modelo es correcto salvo por los parámetros.** Es el supuesto más
   fuerte y el que los residuos ponen a prueba.
6. **Que la aproximación lineal de la propagación vale** en el rango de tus
   incertidumbres.
:::

---

## 7. ¿Cuándo falla?

::: falla
**Falla cuando el sesgo domina.** Ninguna cantidad de repeticiones lo arregla.
Y el sesgo no se detecta repitiendo: se detecta **cambiando de método**. Medir
lo mismo con dos instrumentos distintos es el único diagnóstico fiable, y es la
razón de ser de las comparaciones interlaboratorio.

**Falla cuando los parámetros no son identificables.** Si dos parámetros
aparecen siempre en la misma combinación, el $\chi^2$ tiene un valle plano y el
ajuste devuelve números con barras de error enormes o, peor, números precisos
que dependen del punto de partida del optimizador. La señal es una correlación
$|\rho|>0{,}95$. Capítulo 15.

**Falla con datos preprocesados.** Si alguien ha suavizado, interpolado o
promediado los datos antes de dártelos, los errores están correlacionados y tu
$\chi^2_\nu$ saldrá artificialmente bajo. Pregunta siempre por el
preprocesado; es la fuente número uno de incertidumbres irrealmente pequeñas.

**Falla al extrapolar.** La banda de predicción de la figura de covarianza se
abre fuera del rango de los datos, y se abre **mucho más** de lo que sugiere la
intuición. Un ajuste válido en $[0,6]$ no dice nada útil en $t=20$, por muy
buenas que sean las barras de error de los parámetros.
:::

### Un anti-ejemplo: la precisión que creció sola

Un laboratorio mide una constante durante veinte años. Cada nueva publicación
tiene una incertidumbre menor que la anterior, y todos los valores son
compatibles entre sí. Parece la historia de un progreso instrumental ejemplar.

Y puede serlo, o puede ser esto: cada nuevo experimento compara su resultado
con el anterior, y cuando difiere, busca el error hasta encontrarlo —porque
siempre hay algún error que encontrar—; cuando coincide, no busca nada. El
procedimiento es asimétrico, y **produce convergencia hacia el valor anterior,
sea cual sea**.

Feynman describió exactamente este mecanismo en 1974 para la carga del
electrón tras Millikan, y no es historia antigua: la serie temporal de valores
recomendados de varias constantes fundamentales muestra el mismo patrón de
saltos correlacionados. La lección: **la compatibilidad entre medidas sucesivas
no es evidencia de corrección si el procedimiento de análisis conocía el
resultado previo.** De ahí vienen los análisis ciegos, hoy estándar en física
de partículas.

---

## 8. Historia

::: historia
**Gauss, Ceres y una disputa que sigue viva** · *Nivel de verificación: A.*

El 1 de enero de 1801, Giuseppe Piazzi descubrió Ceres desde Palermo. Lo siguió
41 días —unos 3 grados de arco— y después el objeto se perdió en el resplandor
del Sol. Para encontrarlo de nuevo en otoño había que predecir dónde estaría a
partir de un arco minúsculo de órbita, con datos ruidosos.

Carl Friedrich Gauss, con 24 años, desarrolló un método completo de
determinación orbital y publicó una predicción. En diciembre de 1801, Franz
Xaver von Zach encontró Ceres cerca de donde Gauss decía. El episodio hizo
famoso a Gauss de un día para otro.

En *Theoria Motus* (1809), Gauss expuso el método de mínimos cuadrados y afirmó
haberlo usado desde 1795. El problema es que Adrien-Marie Legendre lo había
**publicado en 1805**, y le sentó fatal. La disputa de prioridad se prolongó
durante años.

Stigler (1986) examinó la evidencia con cuidado y concluye que la afirmación de
Gauss es probablemente cierta pero no está documentada de forma independiente, y
que la publicación de Legendre fue anterior y perfectamente clara. La
convención moderna —«mínimos cuadrados de Gauss-Legendre»— es el compromiso
razonable. Lo que sí es de Gauss sin discusión es la **justificación
probabilística**: la conexión entre mínimos cuadrados, distribución normal de
errores y máxima verosimilitud, que es exactamente el apartado 4.2.

**Student, y por qué se llamaba Student** · *Nivel de verificación: A.*

En 1908, la revista *Biometrika* publicó *The Probable Error of a Mean*
firmado por «Student». El autor era William Sealy Gosset, químico y estadístico
de la cervecería Guinness en Dublín. Guinness prohibía a sus empleados publicar
para no revelar que usaba métodos estadísticos como ventaja competitiva, así
que Gosset publicó bajo seudónimo.

El problema de Gosset era estrictamente industrial: controlar la calidad de la
cebada y del lúpulo con **muestras pequeñas**, porque cada ensayo costaba
dinero y tiempo. Toda la teoría existente era asintótica y suponía muchas
medidas. La distribución $t$ nació de la necesidad de decir algo honesto con
cuatro datos.

Es uno de los mejores ejemplos de que las restricciones prácticas producen
teoría: si Gosset hubiera tenido muestras infinitas, no habría inventado nada.

**Y una nota sobre el vocabulario** · *Nivel de verificación: A.*

El GUM se publicó en 1993 (revisado en 2008) precisamente porque cada
disciplina usaba las palabras a su manera y los resultados no se podían
comparar entre laboratorios. Es un documento aburridísimo y sorprendentemente
útil: leer sus veinte primeras páginas ahorra una cantidad notable de
discusiones estériles.
:::

---

## 9. Problemas

En `problemas.md`; soluciones en `soluciones.md`.

---

## 10. Experimento computacional

::: experimento
**Mide algo de verdad y hazlo bien.**

*Pregunta:* ¿cuánto vale $g$ en tu casa, y con qué incertidumbre honesta?

*Diseño.* Con el móvil, graba en vídeo la caída de un objeto contra una regla,
o cronometra un péndulo largo durante muchas oscilaciones. Toma al menos 20
medidas y **anota además** todo lo que podría sesgarlas: la longitud del
péndulo con su incertidumbre, la resolución del cronómetro, tu tiempo de
reacción, el rozamiento del aire, la amplitud (¡capítulo 2!).

*Análisis.* Calcula la incertidumbre tipo A de tus repeticiones y las tipo B de
todo lo demás. Combínalas. Compara con $9{,}807$ m/s².

*Qué falsaría tu resultado:* si tu intervalo no contiene el valor real, tienes
un sesgo sin identificar. **Búscalo, no ensanches la barra.** Ese es el
ejercicio de verdad: la mayoría de la gente, al fallar, amplía la
incertidumbre en vez de encontrar la causa, y eso es exactamente lo contrario
de lo que hay que hacer.
:::

---

## 11. Explícalo

::: explica
1. ¿Por qué promediar mil medidas no mejora un resultado sesgado?
2. Explica sin ecuaciones qué es una matriz de covarianza de un ajuste, usando
   la imagen de la elipse.
3. ¿Por qué un $\chi^2$ reducido de 0,2 debería preocuparte?
4. ¿Qué le dirías a alguien que presenta un ajuste con $R^2=0{,}999$ y ningún
   gráfico de residuos?
5. ¿Cómo detectarías un error sistemático que no sabes que tienes?
6. ¿Qué significa exactamente que un modelo sea «compatible con los datos», y
   qué no significa?
:::

---

## 12. Lo esencial

::: esencial
* Error es lo que no sabes; incertidumbre es lo que declaras. El GUM clasifica
  por cómo la has evaluado (tipo A/B), no por su origen.
* El sesgo es un suelo: a partir de $n\approx(\sigma/b)^2$, medir más no sirve.
  Calcula ese número antes de empezar.
* La propagación lineal falla de dos maneras: introduce sesgo si hay curvatura,
  y deja de significar nada si la función es muy no lineal. Con más de un 20 %
  de incertidumbre relativa en un denominador, simula.
* Mínimos cuadrados **es** máxima verosimilitud con errores gaussianos
  independientes. No es neutro.
* $R^2$ no diagnostica nada. El $\chi^2_\nu$ y la gráfica de residuos, sí.
* $\chi^2_\nu\ll1$ es tan sospechoso como $\chi^2_\nu\gg1$.
* Guarda la matriz de covarianza completa. Las barras de error solas mienten en
  cuanto propagues.
* El sesgo no se detecta repitiendo, se detecta cambiando de método.
:::

---

## 13. Preguntas que quedan abiertas

::: abierto
* Si las $\sigma_i$ se estiman de los propios datos, ¿cómo se propaga la
  incertidumbre de la incertidumbre?
* ¿Cuándo merece la pena un análisis ciego, y cuánto cuesta en tiempo y en
  frustración?
* La covarianza captura la dependencia lineal entre parámetros. ¿Qué se pierde
  cuando el valle del $\chi^2$ es curvo?
* ¿Se puede decidir, sólo con los datos, si un residuo estructurado se debe a
  un modelo incorrecto o a barras de error mal estimadas?
* Si todo modelo es falso, ¿qué es exactamente lo que estamos midiendo cuando
  ajustamos un parámetro? (Capítulos 14 y 15.)
:::
