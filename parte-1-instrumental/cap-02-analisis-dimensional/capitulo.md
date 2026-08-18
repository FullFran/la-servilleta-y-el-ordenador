# Capítulo 2 — Análisis dimensional y similitud

> **Qué sabrás hacer al terminar**
> · Deducir la forma de una ley física sin resolver ninguna ecuación ·
> Construir los grupos π de un problema y saber cuántos hay ·
> Adimensionalizar una ecuación y quedarte con los parámetros que de verdad
> mandan · Leer un número adimensional como una pregunta ·
> Saber cuándo el método miente.
>
> **Herramientas que usa:** capítulo 1 (órdenes de magnitud).
> **Disciplinas de los ejemplos:** física de fluidos, biología, ingeniería
> naval, meteorología, química.
> **Deuda que paga:** la ley $R\propto(Et^2/\rho)^{1/5}$ que quedó pendiente en
> el capítulo 1.
> **Deuda que abre:** por qué la adimensionalización simplifica tanto una EDO
> (capítulo 6) y qué hacer cuando un grupo π es pequeño pero no cero
> (capítulo 13).

---

## 1. Una pregunta

::: pregunta
Tienes una fotografía de una explosión con una regla al lado y el instante en
que se tomó. Nada más: ni la composición del explosivo, ni la presión, ni la
temperatura. **¿Cuánta energía se liberó?**
:::

La pregunta parece imposible por una razón distinta a la del capítulo 1. Allí
faltaban datos y los inventábamos. Aquí falta **física**: no tenemos las
ecuaciones de la hidrodinámica de una onda de choque, y aunque las tuviéramos
no sabríamos resolverlas en una servilleta.

Y sin embargo, en 1950 Geoffrey Ingram Taylor publicó la energía de la primera
explosión nuclear de la historia a partir de fotografías publicadas. Su
herramienta cabe en una línea:

$$R = C\left(\frac{E\,t^{2}}{\rho}\right)^{1/5}$$

Esa línea no sale de resolver nada. Sale de contar unidades.

---

## 2. Antes de calcular

::: antes
Antes de seguir, contesta de memoria:

1. Si la energía de una explosión se multiplica por 1000, ¿por cuánto se
   multiplica el radio de la bola de fuego en un instante dado?
2. Un péndulo de 1 m tiene un periodo de 2 s. ¿Cuál es el periodo de uno de
   4 m? ¿Y el de uno de 1 m en la Luna?
3. Una maqueta de barco a escala 1:100 se ensaya en un canal. ¿A qué velocidad
   hay que remolcarla para que «se parezca» al barco real?

La tercera tiene trampa, y esa trampa es media asignatura de ingeniería naval.
:::

---

## 3. La intuición

### 3.1 Una ecuación no puede ser dimensionalmente falsa

La regla es de una obviedad desconcertante: no puedes sumar metros con
segundos. De esa obviedad sale casi todo lo que hace este capítulo, porque
impone una restricción brutal sobre las formas que puede tener una ley física.

Piénsalo así: si una cantidad $y$ depende de $x_1,\dots,x_n$, la relación
$y=f(x_1,\dots,x_n)$ tiene que seguir siendo cierta si mañana decidimos medirlo
todo en pulgadas y en horas. Una ley de la naturaleza no puede depender de qué
sistema de unidades usó el que la escribió. Esa invariancia es una simetría, y
como toda simetría, **elimina grados de libertad**.

Cuántos elimina exactamente es el contenido del teorema π.

### 3.2 Dimensiones no son unidades

Conviene separar dos cosas que se confunden todo el rato.

Una **unidad** es un convenio: el metro, el pie, el año-luz. Una **dimensión**
es una clase de magnitud: longitud, masa, tiempo. El metro y el pie son
unidades distintas de la misma dimensión.

Escribiremos $[x]$ para «las dimensiones de $x$». En mecánica bastan tres:
longitud $\mathsf{L}$, masa $\mathsf{M}$ y tiempo $\mathsf{T}$. Así,
$[v]=\mathsf{L}\mathsf{T}^{-1}$, $[F]=\mathsf{M}\mathsf{L}\mathsf{T}^{-2}$,
$[E]=\mathsf{M}\mathsf{L}^{2}\mathsf{T}^{-2}$. Cuando hay calor se añade la
temperatura $\Theta$; cuando hay electricidad, la corriente $\mathsf{I}$.

::: aviso
El ángulo es adimensional, y por eso el análisis dimensional **no puede decir
nada sobre cómo depende algo de un ángulo**. Esto no es una tecnicidad: es la
razón por la que el método falla en el ejemplo más famoso de todos, el péndulo,
como veremos en la sección 8.
:::

### 3.3 Contar unidades como quien cuenta grados de libertad

Volvamos a la explosión. ¿De qué puede depender el radio $R$ del frente?

* del tiempo transcurrido $t$,
* de la energía liberada $E$,
* de la densidad del aire que hay que empujar, $\rho$.

¿Y de la presión ambiente? Al principio no: la presión detrás del frente es
miles de veces mayor que la atmosférica, así que el aire de delante ofrece
resistencia por su **inercia**, no por su presión. Ese razonamiento —decidir
qué entra en la lista— es el paso donde se gana o se pierde el problema, y
volveremos sobre él en la sección 8.

Tenemos cuatro cantidades y tres dimensiones. La cuenta que hace el teorema π
es exactamente esta: **cuatro menos tres es uno**. Sólo existe una combinación
adimensional posible, y por tanto la física entera del problema se reduce a
decir que esa combinación vale una constante.

---

## 4. La matemática

### 4.1 El teorema π de Buckingham

**Enunciado.** Si una relación física involucra $n$ magnitudes dimensionales y
en ellas aparecen $k$ dimensiones independientes, entonces la relación se puede
escribir en función de $n-k$ grupos adimensionales:

$$f(x_1,\dots,x_n)=0 \quad\Longleftrightarrow\quad
\Phi(\pi_1,\dots,\pi_{n-k})=0$$

**Por qué es cierto, sin formalismo.** Construye la *matriz dimensional*: una
matriz $k\times n$ cuya columna $j$ contiene los exponentes de las dimensiones
en $x_j$. Buscar un grupo adimensional $\prod x_j^{a_j}$ es buscar un vector
$\mathbf{a}$ en el **núcleo** de esa matriz. Si el rango de la matriz es $k$,
la dimensión del núcleo es $n-k$ por el teorema del rango. Eso es todo: el
teorema π es álgebra lineal disfrazada, y $k$ es un rango, no «el número de
dimensiones que se me ocurren».

::: herramientas
**La matriz dimensional, en tres pasos**

Para la explosión, con $x=(R,t,E,\rho)$:

| | $R$ | $t$ | $E$ | $\rho$ |
|---|---|---|---|---|
| $\mathsf{M}$ | 0 | 0 | 1 | 1 |
| $\mathsf{L}$ | 1 | 0 | 2 | −3 |
| $\mathsf{T}$ | 0 | 1 | −2 | 0 |

1. **Rango.** Las tres filas son independientes: $k=3$.
2. **Cuántos grupos.** $n-k=4-3=1$.
3. **Cuál.** Busca $R^{a}t^{b}E^{c}\rho^{d}$ adimensional:
   $\mathsf{M}: c+d=0$; $\mathsf{L}: a+2c-3d=0$; $\mathsf{T}: b-2c=0$.
   Tomando $c=1$: $d=-1$, $b=2$, $a=-5$. Luego

   $$\pi_1=\frac{E\,t^{2}}{\rho\,R^{5}}$$
:::

Como sólo hay un grupo, la relación $\Phi(\pi_1)=0$ obliga a que $\pi_1$ sea
**una constante**. Despejando:

$$\boxed{\ R = C\left(\frac{E t^{2}}{\rho}\right)^{1/5}\ }$$

Leído en voz alta: *el frente avanza como la potencia dos quintos del tiempo,
y el radio crece con la energía elevada a un quinto*. La segunda mitad es
notable: para duplicar el radio de la bola de fuego a un tiempo dado hacen
falta **32 veces más energía**. Las bombas son mucho menos impresionantes de lo
que su energía sugiere, y la culpa la tiene ese $1/5$.

### 4.2 La receta práctica

Cuando hay más de un grupo, conviene un método sistemático.

1. **Lista las variables.** Este paso es el problema entero. Si sobra una,
   aparecen grupos espurios; si falta una, el resultado es sencillamente falso.
2. **Escribe la matriz dimensional y calcula su rango** $k$. (En Python:
   `np.linalg.matrix_rank`.)
3. **Elige $k$ variables repetidas.** Criterios, por orden de importancia:
   * entre las $k$ deben aparecer todas las dimensiones;
   * no deben formar un grupo adimensional entre ellas;
   * **no incluyas la variable que quieres despejar**, o aparecerá en varios
     grupos y no podrás aislarla;
   * si puedes elegir, coge las que controlas experimentalmente.
4. **Forma un grupo por cada variable restante**, combinándola con las
   repetidas.
5. **Recombina para que los grupos signifiquen algo.** $\pi_1\pi_2$,
   $\pi_1/\pi_2$ y $\pi_1^{-1}$ son grupos igual de válidos: elige los que
   tengan interpretación física. Un grupo con nombre —Reynolds, Péclet— vale
   diez veces más que un grupo correcto y anónimo.

### 4.3 Adimensionalizar una ecuación: el paso que más problemas salva

El teorema π actúa sobre listas de variables. Hay una versión más potente que
actúa sobre la ecuación entera, y es probablemente la técnica más rentable de
todo este libro.

Tomemos la caída de una gota con arrastre cuadrático:

$$m\frac{dv}{dt}=mg-\tfrac12\rho_{a}C_{D}A\,v^{2}$$

Cuatro parámetros ($m,g,\rho_a C_D A$) y dos variables. Definamos escalas
naturales: la velocidad terminal $v_{t}$, que sale de igualar los dos términos
del segundo miembro, y el tiempo que se tarda en alcanzarla,
$\tau = v_t/g$:

$$v_{t}=\sqrt{\frac{2mg}{\rho_{a}C_{D}A}},\qquad \tau=\frac{v_{t}}{g}$$

Con $\hat v = v/v_t$ y $\hat t = t/\tau$, la ecuación se convierte en

$$\frac{d\hat v}{d\hat t}=1-\hat v^{2}$$

**Han desaparecido todos los parámetros.** No hay ninguna gota «distinta» de
otra: todas las gotas del universo, en cualquier planeta, con cualquier
coeficiente de arrastre, siguen esta única curva. Lo que cambia entre ellas es
la escala con la que se mide, no la forma.

Esto no es un truco estético. Es una reducción de la dimensionalidad del
espacio de parámetros: un barrido que habría requerido explorar cuatro
parámetros se convierte en **una sola integración**. En el capítulo 16
insistiremos: adimensionalizar antes de barrer es la diferencia entre un
experimento computacional y un desperdicio de CPU.

### 4.4 El colapso de datos: la prueba experimental de que has entendido

Cuando has encontrado los grupos correctos, ocurre algo visualmente
espectacular: nubes de datos que parecían no tener nada que ver caen sobre una
sola curva.

![Colapso de datos en el péndulo no lineal. Izquierda: el periodo frente a la amplitud para cuatro longitudes y cuatro gravedades. Derecha: exactamente los mismos puntos, con el periodo medido en unidades de $2\pi\sqrt{L/g}$. Lo que hay que concluir: el problema no tenía tres parámetros, tenía uno.](figuras/fig_colapso_pendulo.pdf)

El colapso es la señal de que la lista de variables era correcta y los grupos,
los adecuados. Cuando los datos **no** colapsan, has olvidado una variable. Es
el diagnóstico más barato y más honesto que existe: no requiere teoría, sólo
elegir bien los ejes.

### 4.5 Números adimensionales como preguntas

Un grupo adimensional no es un número: es un cociente entre dos efectos, y por
tanto **una pregunta con respuesta cuantitativa**.

| Grupo | Cociente | La pregunta que hace |
|---|---|---|
| Reynolds $\;Re=UL/\nu$ | inercia / viscosidad | ¿puedo despreciar la viscosidad? |
| Péclet $\;Pe=UL/D$ | arrastre / difusión | ¿transporta más el flujo o la difusión? |
| Mach $\;Ma=U/c$ | velocidad / sonido | ¿es compresible el fluido? |
| Froude $\;Fr=U/\sqrt{gL}$ | inercia / gravedad | ¿importan las olas de superficie? |
| Biot $\;Bi=hL/k$ | resistencia interna / externa | ¿está el cuerpo a temperatura uniforme? |
| Knudsen $\;Kn=\lambda/L$ | camino libre / tamaño | ¿es el gas un medio continuo? |
| Damköhler $\;Da=k\tau$ | reacción / transporte | ¿manda la química o la mezcla? |
| Rayleigh $\;Ra$ | flotabilidad / difusión | ¿arranca la convección? |

![Quince décadas de Reynolds. Lo que se ve: dónde vive cada nadador y cada volador. Lo que hay que concluir: una bacteria y un atún no viven en «el mismo fluido con otra escala», viven en dos físicas distintas separadas por siete décadas de $Re$.](figuras/fig_mapa_reynolds.pdf)

Ese mapa explica cosas que de otro modo parecen anecdóticas. Una bacteria a
$Re\sim10^{-5}$ vive en un mundo donde la inercia no existe: si deja de
moverse, se para en una distancia menor que su propio tamaño, y por eso no
puede nadar agitando algo hacia delante y hacia atrás —el famoso *teorema de la
vieira* de Purcell—. Necesita un flagelo helicoidal, que rompe la reversibilidad
temporal. La forma del bicho está dictada por un número adimensional.

---

## 5. El ordenador entra en escena

::: antes
Vamos a ajustar la ley $R\propto t^{2/5}$ a los radios de la bola de fuego de
Trinity que Taylor publicó en 1950. Antes de mirar:

* ¿Crees que una única ley de potencias aguantará tres décadas de tiempo, desde
  0,1 ms hasta 62 ms?
* Si cada punto da una estimación independiente de $E$, ¿se parecerán entre sí?
* ¿La energía que salga estará por encima o por debajo de los 21 kt aceptados?
:::

```python
import numpy as np

# Radios del frente (m) frente al tiempo (ms), tabla publicada por Taylor (1950)
t = np.array([0.10, 0.24, 0.38, 0.52, 0.66, 0.94, 1.25, 1.50, 1.93,
              3.53, 4.61, 15.0, 25.0, 34.0, 53.0, 62.0]) * 1e-3
R = np.array([11.1, 19.9, 25.4, 28.8, 31.9, 36.3, 41.0, 44.4, 46.9,
              59.0, 65.6, 106.5, 130.0, 145.0, 175.0, 185.0])

m, a = np.polyfit(np.log10(t), np.log10(R), 1)      # pendiente empírica
E = np.median(1.25 * R**5 / (1.03**5 * t**2))        # rho=1.25, C=1.03
print(f"pendiente {m:.3f} (teoría 0.400)   E = {E/4.184e12:.1f} kt")
```

```text
pendiente 0.408 (teoría 0.400)   E = 15.5 kt
```

![La ley de la onda de choque contra los datos de Trinity. Izquierda: tres décadas de tiempo sobre una sola recta de pendiente 0,408 frente a los 0,400 predichos. Derecha: la energía deducida de cada fotografía por separado. Lo que hay que concluir: el análisis dimensional acierta la *forma* con precisión de laboratorio, y la constante con un factor 1,4.](figuras/fig_taylor_trinity.pdf)

Tres cosas merecen comentario.

**La pendiente sale bordada.** 0,408 frente a 0,400 en tres décadas de tiempo.
El exponente es la parte que predice el análisis dimensional, y la predice sin
resolver una sola ecuación diferencial.

**La constante no sale de aquí.** El valor $C\approx1{,}03$ requiere resolver
la ecuación de la onda de choque autosemejante —eso sí lo hizo Taylor, y
también Sedov y von Neumann—. El análisis dimensional te da la forma
funcional; la constante te la da la física o el experimento. Es un reparto de
trabajo que conviene tener claro para no vender el método más caro de lo que
vale.

**Sale 15,5 kt y el valor aceptado es 21 kt.** Un factor 1,35. Para un método
que ignora la composición del artefacto, la geometría del dispositivo y toda la
termodinámica, no está nada mal; y como aprendimos en el capítulo 1, un factor
1,35 está dentro de la barra de error de una estimación con cuatro supuestos.

::: juega
1. Ajusta sólo los cinco primeros puntos y sólo los cinco últimos. ¿Cambia la
   pendiente? ¿En qué dirección, y por qué? (Pista: ¿en qué momento deja de ser
   despreciable la presión ambiente?)
2. Cambia $\rho$ de 1,25 a 1,0 kg/m³. ¿Cuánto cambia $E$? ¿Es una fuente de
   error importante comparada con las demás?
3. Repite el ajuste dejando libre el exponente y estimando $E$ con él. ¿Mejora o
   empeora? ¿Qué te dice eso sobre ajustar más parámetros de los que la física
   permite? (Volveremos a esto en el capítulo 15.)
:::

---

## 6. Semejanza: por qué las maquetas mienten

Dos sistemas son **dinámicamente semejantes** si todos sus grupos π coinciden.
Entonces, y sólo entonces, la solución adimensional es la misma y basta con
reescalar.

Aquí aparece el problema que hace interesante la ingeniería naval. Para que una
maqueta de barco represente al barco real hacen falta dos cosas a la vez:

$$Re=\frac{UL}{\nu}\ \text{igual}
\qquad\text{y}\qquad
Fr=\frac{U}{\sqrt{gL}}\ \text{igual}$$

Con una escala $L_m = L/100$, igualar Froude exige $U_m = U/10$, e igualar
Reynolds exige $U_m = 100\,U$. **Son incompatibles por un factor 1000.** No
existe ninguna velocidad de ensayo que satisfaga las dos.

La salida real es tan interesante como el problema: se ensaya a Froude igual —
porque la resistencia por formación de olas es la que peor se sabe calcular— y
la parte viscosa de la resistencia se corrige aparte con una fórmula empírica.
Es decir, **se rompe deliberadamente la semejanza en el grupo que sí se sabe
modelar**. Esa decisión, tomada por William Froude en la década de 1870, sigue
siendo la base del ensayo de carenas.

La moraleja general vale para todo el libro: cuando no puedes cumplir todas las
condiciones, incumple aquella cuyo efecto sabes calcular por otro camino.

### 6.1 Escalas en biología: por qué no hay mamíferos del tamaño de un edificio

Si escalas un animal geométricamente por un factor $\lambda$, su masa crece
como $\lambda^{3}$ pero la sección de sus huesos sólo como $\lambda^{2}$. La
tensión en el hueso crece por tanto como $\lambda$, o como $M^{1/3}$.

![Isometría contra resistencia. Izquierda: la sección de hueso que exige la geometría frente a la que exige mantener la tensión constante. Derecha: la tensión relativa que soportaría un animal escalado sin cambiar de forma. Lo que hay que concluir: un ratón agrandado hasta el tamaño de un elefante se rompería las patas al levantarse.](figuras/fig_escala_huesos.pdf)

La consecuencia es que los animales grandes **no** son animales pequeños
agrandados: tienen huesos proporcionalmente más gruesos, posturas más rectas y
un margen de seguridad menor. Es lo que Galileo ya observó en 1638 en los
*Discorsi*, con un dibujo de dos huesos que sigue reproduciéndose. Y explica
también por qué el animal más grande de la historia vive en el agua, donde la
flotabilidad elimina el problema.

Este argumento se llevará más lejos en el capítulo II.13, donde discutiremos
la ley de Kleiber y por qué el exponente 3/4 lleva noventa años dando
problemas.

---

## 7. ¿Qué estamos suponiendo?

::: supuestos
1. **Que la lista de variables es completa y sin sobras.** Es el supuesto
   fuerte, el único que importa de verdad y el único que el método no puede
   verificar por sí mismo.
2. **Que la relación es física, es decir, invariante bajo cambio de unidades.**
   Falla para correlaciones empíricas ajustadas en unidades concretas, que
   abundan en ingeniería y que dejan de valer si cambias de sistema.
3. **Que las dimensiones elegidas son las correctas.** Tratar la temperatura
   como dimensión independiente o reducirla vía $k_B$ cambia el recuento de
   grupos, y ambas opciones son legítimas: hay que declarar cuál se usa.
4. **Que la explosión de Trinity era esférica y en aire homogéneo.** Ni lo uno
   ni lo otro exactamente; el suelo estaba a 30 m de la torre.
5. **Que la presión ambiente es despreciable frente a la del frente.** Válido
   mientras $\Delta p \gg p_0$, es decir en los primeros milisegundos. La ley
   deja de valer justo cuando la onda se convierte en sonido.
6. **Que existe un régimen autosemejante.** Lo hay en este problema; no siempre
   lo hay, como veremos ahora.
:::

---

## 8. ¿Cuándo falla?

::: falla
**Falla si olvidas una variable.** Y falla en silencio, dando una fórmula de
aspecto respetable. Es el modo de fallo dominante.

**Falla con los grupos que ya eran adimensionales.** El teorema π no puede
decir nada sobre cómo depende un resultado de un ángulo, de un cociente de
longitudes o de $\gamma=c_p/c_v$, porque esas cantidades ya son números puros y
pueden entrar en $\Phi$ de cualquier manera. El péndulo es el ejemplo clásico:
dimensionalmente, $T=\sqrt{L/g}\,\Phi(\theta_0)$, y $\Phi$ puede ser cualquier
cosa. La figura de la sección 4.4 muestra que $\Phi$ crece un 18 % a 2 radianes
y se dispara cerca de $\pi$. Ninguna cuenta de unidades habría predicho eso.

**Falla cuando la constante importa.** El método da la forma; si necesitas el
número, necesitas física o experimento. Presentar un resultado dimensional como
si fuera cuantitativo es la exageración habitual del método.

**Falla en la autosemejanza de segunda especie.** Hay problemas donde un grupo
π tiende a cero pero el resultado **no** tiende a un límite finito: la
dependencia sobrevive con un exponente que no sale de contar unidades, sino de
resolver un problema de autovalores. Barenblatt (1996) lo trata en detalle. La
señal de alarma es que tus datos casi colapsan pero con una deriva sistemática.

**Y falla catastróficamente si mezclas unidades.** El 23 de septiembre de 1999,
la Mars Climate Orbiter se perdió porque un fichero de software de tierra
entregaba impulsos en libra-fuerza·segundo mientras el receptor los esperaba en
newton·segundo, un factor 4,45 (informe de la Mars Climate Orbiter Mishap
Investigation Board, 1999). Ciento veinticinco millones de dólares por una
dimensión mal declarada. La lección práctica: **lleva las unidades dentro del
código**, no en un comentario.
:::

### Un anti-ejemplo: la lista de variables que parecía completa

Estimemos con análisis dimensional el caudal $Q$ que sale por un agujero en el
fondo de un depósito. Variables: altura de líquido $h$, área del agujero $A$,
gravedad $g$, densidad $\rho$. Cuatro variables, tres dimensiones, un grupo:
sale $Q = C A\sqrt{gh}$, que es Torricelli y es correcto.

Ahora hazlo con miel en vez de agua. La fórmula sigue diciendo lo mismo, y es
completamente falsa: para la miel el caudal depende de la viscosidad, que no
está en la lista. El método no ha fallado; ha respondido exactamente lo que le
preguntamos. **El análisis dimensional es un amplificador de tu criterio
físico, no un sustituto.**

---

## 9. Historia

::: historia
**La onda de choque: tres personas, tres países, la misma solución** ·
*Nivel de verificación: A.*

La ley $R\propto(Et^2/\rho)^{1/5}$ se descubrió al menos tres veces de forma
independiente, y la historia habitual sólo cuenta una.

**Geoffrey Ingram Taylor** la obtuvo en 1941, en un informe para el Ministry of
Home Security británico, estudiando qué pasaría con una explosión que liberase
mucha energía en muy poco volumen. Publicó el trabajo en 1950 en dos partes:
la primera con la teoría, la segunda aplicándola a las fotografías de la
explosión de Trinity tomadas por Julian Mack, que se habían hecho públicas.
Taylor obtuvo unos 16,8 kt (Taylor 1950, parte II).

**John von Neumann** trabajó en el mismo problema en Los Álamos entre 1941 y
1943; su solución circuló como informe interno y se publicó mucho después.
**Leonid Sedov**, en la Unión Soviética, publicó la solución general en 1946.
Por eso la literatura habla del problema *Taylor–Sedov–von Neumann*, y por eso
conviene desconfiar de las historias en las que un genio solitario ve algo que
nadie más ve: cuando un problema está maduro, suele resolverse en varios sitios
a la vez.

Sobre la parte más contada —que Taylor dedujo un secreto militar de unas fotos
publicadas y que eso incomodó a las autoridades estadounidenses— la
documentación es más fina de lo que la anécdota sugiere. Lo sólido es la
cronología: teoría en 1941, fotografías desclasificadas en 1947, publicación en
1950. Lo que se cuenta sobre reacciones oficiales pertenece al nivel B, y
conviene contarlo como lo que es.

**Y una nota sobre el nombre del teorema.** El «teorema π» lleva el nombre de
Edgar Buckingham, que lo formalizó en 1914 en *Physical Review*, pero la idea
circulaba desde antes: Rayleigh había estado usando el método durante décadas,
Bertrand y Vaschy publicaron versiones anteriores. Es otro caso de la ley de
Stigler, según la cual ningún descubrimiento científico lleva el nombre de su
descubridor —una ley que, con la ironía apropiada, Stigler atribuyó a Merton.
:::

---

## 10. Problemas

En `problemas.md`; soluciones razonadas en `soluciones.md`.

---

## 11. Experimento computacional

::: experimento
**Encuentra la ley de escala escondida.**

*Pregunta:* ¿cómo depende el tiempo de vaciado de un depósito de su geometría?

*Diseño.* Simula (o resuelve numéricamente) el vaciado de depósitos cilíndricos
por un agujero en el fondo, usando Torricelli con un coeficiente de descarga.
Barre el radio del depósito entre 0,1 y 2 m, el radio del agujero entre 1 y
50 mm y la altura inicial entre 0,1 y 3 m. Guarda el tiempo de vaciado.

*Criterio de parada:* 200 simulaciones. No más.

*Análisis.* Primero dibuja $t_{\text{vaciado}}$ frente a cada parámetro por
separado: verás una nube. Después construye el grupo adimensional que creas
correcto y dibuja el colapso. Si no colapsa, tu lista de variables está
incompleta.

*Qué falsaría tu hipótesis:* una deriva sistemática residual en el colapso. Si
la ves, pregúntate qué variable con dimensiones has dejado fuera (pista:
¿qué pasa si el agujero no es pequeño comparado con el depósito?).
:::

---

## 12. Explícalo

::: explica
1. ¿Por qué el hecho de que una ley no dependa del sistema de unidades limita
   la forma que puede tener? Explícalo sin escribir la matriz dimensional.
2. ¿Qué significa físicamente que sólo haya *un* grupo adimensional en un
   problema?
3. ¿Por qué duplicar el radio de una bola de fuego exige 32 veces más energía?
4. Explica a un ingeniero naval por qué no puede ensayar su maqueta «a la
   velocidad correcta», y qué hace en la práctica.
5. ¿Por qué un colapso de datos es una prueba y no una coincidencia?
6. ¿Qué le dirías a alguien que afirma haber deducido una ley física «sólo con
   análisis dimensional»?
:::

---

## 13. Lo esencial

::: esencial
* Una ley física no puede depender del sistema de unidades. Esa invariancia es
  una simetría, y elimina grados de libertad.
* Teorema π: $n$ variables con $k$ dimensiones independientes dan $n-k$ grupos
  adimensionales. $k$ es el **rango** de la matriz dimensional.
* Con un solo grupo, la física se reduce a una constante y el resto es una ley
  de potencias exacta.
* Adimensionalizar una ecuación elimina parámetros: la familia entera de
  soluciones se convierte en una sola curva.
* Un grupo adimensional es una pregunta: ¿importa la viscosidad? ¿es
  compresible? ¿está el cuerpo a temperatura uniforme?
* El colapso de datos es el diagnóstico: si no colapsan, falta una variable.
* El método da la **forma**, no la constante, y no dice nada sobre variables ya
  adimensionales, como los ángulos.
* Cuando no puedes cumplir todos los grupos a la vez, incumple el que sepas
  corregir por otro camino.
:::

---

## 14. Preguntas que quedan abiertas

::: abierto
* ¿Cómo se decide, sin hacer trampa, qué variables entran en la lista? ¿Existe
  algún criterio que no sea «saber física»?
* ¿Qué ocurre cuando un grupo π es pequeño pero no nulo? ¿Se puede desarrollar
  en serie en él? (Capítulo 13.)
* La constante $C\approx1{,}03$ salió de resolver la ecuación de onda
  autosemejante. ¿Cuándo existe una solución autosemejante y cuándo no?
* Si un modelo de aprendizaje automático se entrena con variables
  dimensionales, ¿aprende la invariancia de unidades, o hay que imponérsela?
* ¿Por qué tantos exponentes biológicos son múltiplos de 1/4 en vez de 1/3?
  (Capítulo II.13.)
:::
