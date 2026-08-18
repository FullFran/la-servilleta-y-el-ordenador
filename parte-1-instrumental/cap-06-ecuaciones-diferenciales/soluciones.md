## Soluciones del capítulo 6

> Las soluciones son razonadas: el número final es lo menos importante. En los
> problemas ● y ★ con solución cerrada hay **Pista 1** y **Pista 2** antes de
> ella; tápalas con la mano y úsalas de una en una.
>
> Los de **Mundo real** (R) no llevan solución a propósito: su procedimiento
> está en el apéndice D.

---

### Calentamiento

**6.C1** El exceso pasa de 70 a 40: factor $40/70=0{,}571$ en 15 min, luego
$\tau=15/\ln(70/40)=26{,}8$ min. De 60 a 40 °C el exceso pasa de 40 a 20:
$t=\tau\ln2=18{,}6$ min. De 40 a 30: exceso de 20 a 10, **otros 18,6 min**.
Cada vez que el exceso se reduce a la mitad tarda lo mismo: esa es la semivida,
y es la firma inconfundible de un proceso exponencial.

**6.C2** (a) $x^*=0$ inestable ($f'=1$), $x^*=\pm1$ estables ($f'=-2$).
(b) $x^*=n\pi$; estables los pares, inestables los impares (alternan).
(c) $x^*=0$ **semiestable**: atrae por la izquierda y repele por la derecha;
$f'(0)=0$ y la linealización no decide. (d) $x^*=0$ estable ($f'=-1$).

**6.C3** Regla del 70: $t_2\approx70/3=23$ años; al 7 %, 10 años. Viene de
$\ln2=0{,}693$.

**6.C4** $v_t=\sqrt{g/k}$, $\tau=v_t/g=1/\sqrt{gk}$. Con $\hat v=v/v_t$ y
$\hat t=t/\tau$ queda $d\hat v/d\hat t=1-\hat v^2$, la ecuación del capítulo 2
sin ningún parámetro.

---

### Estimación

**6.E1** Orden esperado: taza (minutos-decenas de minutos), pollo (una hora),
edificio (horas-días), piscina (días-semanas). El mecanismo:
$\tau=mc/(hA)\propto V/A\propto L$, así que **$\tau$ crece linealmente con el
tamaño** si la forma se mantiene. Una piscina es mil veces más grande que una
taza en volumen y cien en superficie: factor 10 en $\tau$ por esa vía, más el
factor de $h$ (agua quieta frente a aire) y del calor específico.

**6.E2** Si una taza a las 17:00 te quita el sueño a medianoche pero una a las
9:00 no se nota a las 17:00, tu semivida está entre 4 y 7 h. Coincide con la
farmacología. Nota: la semivida de la cafeína varía por un factor 3 entre
individuos (genética del CYP1A2, embarazo, tabaco); es un buen ejemplo de
parámetro con enorme variabilidad poblacional.

**6.E3** ● *Pista 1:* la tasa de crecimiento de una epidemia en fase exponencial no es $R_0$: es $(R_0-1)$ dividido por el tiempo que uno pasa infeccioso.
*Pista 2:* para saber qué supuesto se rompe primero, pregúntate cuál de ellos depende del **número acumulado** de casos y no del tiempo.
*Solución:* $r=(R_0-1)/T_{\text{inf}}=(3-1)/5=0{,}4$ día⁻¹.
$t=\ln(1000)/0{,}4=17$ días. El supuesto que se rompe primero es el de
población susceptible infinita: con 100 000 casos y contactos limitados, $S/N$
empieza a bajar. También se rompen antes, en la práctica, la homogeneidad de
mezcla y la constancia del comportamiento social.

---

### Modelado

**6.M1** $A\dot h = Q - C_d a\sqrt{2gh}$. **No es lineal** por la raíz.
Equilibrio: $h^*=\frac{1}{2g}(Q/(C_d a))^2$. Linealizando cerca de $h^*$:
$\tau=\frac{2Ah^*}{Q}$, es decir, dos veces el tiempo de llenado del volumen de
equilibrio. Nota bonita: aunque la ecuación no es lineal, cerca del equilibrio
se comporta como una relajación, que es la tesis del capítulo 13.

**6.M2** $\dot C=-kC$ entre dosis, con saltos $+D/V$ cada $T$. El estado
estacionario se alcanza tras unas 4–5 semividas, **independientemente de la
dosis**. La concentración media en estado estacionario es
$\bar C = \frac{D}{V k T}$: depende de la dosis **total por unidad de tiempo**,
no de cómo la repartas. Por eso, para la media, dar 100 mg cada 8 h equivale a
300 mg cada 24 h; lo que cambia es la **oscilación**, que sí importa cuando hay
una ventana terapéutica estrecha.

**6.M3** ● *Pista 1:* un rumor y una epidemia comparten la ecuación, así que empieza por escribir la logística y pregúntate qué le falta.
*Pista 2:* piensa en quién deja de contarlo. Ese mecanismo cambia la **fracción final**, que es lo único que los datos pueden distinguir.
*Solución:* Tres modelos: (a) $\dot y = \beta y$ (exponencial puro, ignora
saturación); (b) $\dot y=\beta y(N-y)/N$ (logística: sólo cuenta contar a
quien no lo sabe); (c) $\dot y=\beta y(N-y)/N-\gamma y$ con «aburridos» que
dejan de contarlo (modelo de Daley–Kendall, que **no** alcanza a toda la
población). Cómo distinguirlos con datos: la fracción final. (a) predice todos;
(b) predice todos; (c) predice una fracción $<1$ que depende de $\beta/\gamma$.
Si en tu oficina el rumor nunca llega a todos, el modelo es (c), y eso es un
dato observable sin necesidad de medir tasas.

---

### Derivación

**6.D1** Factor integrante $e^{bt}$: $(xe^{bt})'=ae^{bt}$, luego
$x=a/b+(x_0-a/b)e^{-bt}$. Límite $t\to0$: $x\to x_0$ ✓. Límite
$t\to\infty$: $x\to a/b$ ✓. Y la pendiente inicial es $a-bx_0$, que es
justamente lo que dice la ecuación.

**6.D2** $N(t)=\frac{K}{1+(K/N_0-1)e^{-rt}}$. Derivando dos veces,
$\ddot N=0$ cuando $N=K/2$. Significado físico: **es el momento de máxima
velocidad de crecimiento**. Antes hay pocos individuos; después, poco sitio. En
epidemiología es el pico de incidencia y es lo que se intenta aplanar.

**6.D3** ● *Pista 1:* no intentes resolver el sistema. Divide $\dot P$ entre $P$ e integra sobre un periodo completo.
*Pista 2:* la órbita es cerrada, así que $\ln P$ vuelve a su valor inicial. ¿Qué obliga eso a valer al promedio?
*Solución:* De $\dot P/P=\alpha-\beta D$, integrando sobre un periodo $T$:
$\frac1T\int_0^T\frac{\dot P}{P}dt=\frac{\ln P(T)-\ln P(0)}{T}=0$ porque la
órbita es cerrada. Luego $\alpha-\beta\bar D=0$, o sea $\bar D=\alpha/\beta$.
Igual con la otra ecuación para $\bar P=\gamma/\delta$.
**Este es el principio de Volterra en tres líneas**, y es un resultado exacto,
no una aproximación: no depende de la amplitud de la oscilación.

**6.D4** ● *Pista 1:* prueba $x=e^{\lambda t}$ y verás que el retardo convierte una ecuación algebraica en una trascendente.
*Pista 2:* en el umbral de estabilidad $\lambda$ es imaginario puro. Separa parte real e imaginaria y tendrás dos ecuaciones para dos incógnitas.
*Solución:* Sustituyendo $x=e^{\lambda t}$: $\lambda=-e^{-\lambda\tau_r}$. En el
umbral, $\lambda=i\omega$, y separando partes real e imaginaria sale
$\omega=1$ y $\tau_r=\pi/2$. Para $\tau_r>\pi/2$ el origen es inestable y
aparecen oscilaciones.
**No contradice 4.4**, porque un sistema con retardo no es de dimensión finita:
su estado no es un número, es la *función* $x$ en todo el intervalo
$[t-\tau_r,t]$, que es un espacio de dimensión infinita. Es un buen recordatorio
de que «cuántas variables tiene el sistema» significa «cuánta información hace
falta para predecir», y no «cuántos símbolos he escrito».

---

### Computacional

**6.P1** El colapso es exacto porque la reducción a $du/ds=u(1-u)$ es exacta,
no aproximada. Si algún caso no colapsa, hay un error de código, no de física:
es un test de tu implementación.

**6.P2** Con `rtol=1e-3` la deriva de $V$ es visible en pocas decenas de
periodos; con `1e-10` aguanta miles. Regla práctica: **para $t$ largos, la
cantidad conservada es el mejor indicador de si tu tolerancia es suficiente**,
mucho mejor que comparar dos tolerancias entre sí. El capítulo II.6 mostrará que
para problemas hamiltonianos hay algo mejor que apretar la tolerancia: cambiar
de integrador.

**6.P3** Los dos autovalores son muy distintos ($\tau_{\text{aire}}\sim1$ h,
$\tau_{\text{muros}}\sim20$ h). Ajustar una sola exponencial da residuos con
forma de S clarísima, y el $\tau$ obtenido es un promedio sin significado
físico que depende de la ventana temporal ajustada. Es el diagnóstico del
capítulo 5 aplicado a un modelo dinámico.

---

### Experimento

**6.X1** Los puntos fijos son $u^*=\frac{1\pm\sqrt{1-4h}}{2}$. Existen para
$h<1/4$, se juntan en $h=1/4$ y desaparecen. Es una **bifurcación silla-nodo**,
y su significado es dramático: si cosechas por encima de $h_c=1/4$ la población
se extingue, y no gradualmente sino de golpe. Más aún: al bajar $h$ por debajo
de $h_c$ la población **no se recupera**, porque ya está en cero. Es el modelo
mínimo del colapso pesquero, y el capítulo 7 lo desarrolla.

**6.X2** ● *Pista 1:* añade la capacidad de carga y recalcula el jacobiano en el punto de coexistencia. Fíjate en la **traza**.
*Pista 2:* un centro tiene traza cero. Cualquier cosa que la haga negativa convierte las órbitas cerradas en espirales.
*Solución:* Con saturación, el punto fijo de coexistencia pasa de centro a foco
estable: las órbitas cerradas se convierten en espirales que convergen. La
oscilación deja de ser permanente y se vuelve transitoria. Si $K$ baja lo
suficiente para que $K<\gamma/\delta$, el depredador no puede sostenerse y se
extingue. **La estructura de órbitas cerradas era un artefacto de un modelo
demasiado limpio.**

---

### Detective

**6.T1** En este orden: (1) ¿es realmente autónomo el sistema, o $f$ depende de
$t$? (2) ¿hay un retardo escondido en la implementación —por ejemplo, usar el
valor del paso anterior en algún término—? (3) ¿es una oscilación numérica del
integrador por paso demasiado grande? Las tres producen «oscilaciones» en
sistemas 1D, y **ninguna es un descubrimiento**. El teorema de 4.4 es un test
de sanidad, no una curiosidad.

**6.T2** $\tau=mc/(hA)$. Media taza tiene la mitad de masa pero **no la mitad de
superficie** (la superficie libre superior es la misma y el área lateral mojada
baja menos que la mitad). Con $m$ dividido por 2 y $A$ reducido en menos de la
mitad, $\tau$ baja: exactamente lo observado. No hace falta ninguna dependencia
con la temperatura. Es la explicación más simple y es geométrica.

**6.T3** ● *Pista 1:* un intervalo de confianza responde a una pregunta muy concreta. Escríbela exactamente, con el «dado que…» incluido.
*Pista 2:* mira la figura de extrapolación del capítulo 15 y pregúntate qué discriminan los datos en la fase exponencial.
*Solución:* Porque el intervalo de confianza es sólo la **incertidumbre de los
parámetros dentro de un modelo dado**, y la incertidumbre dominante es la del
modelo mismo: mezcla homogénea, $\beta$ constante, sin estructura de edad, sin
cambio de comportamiento. En los primeros 20 días todos los modelos coinciden
—están en su fase exponencial— así que los datos no discriminan entre ellos, y
las predicciones a 60 días difieren en órdenes de magnitud. Un intervalo del
5 % en esa situación es una afirmación sobre el ajuste, no sobre el mundo.
Capítulo 15, sección 15.13.

---

### Feynman

**6.F1** Guion: «El tiempo característico es lo que tarda un sistema en olvidar
de dónde venía. Antes de ese tiempo, todavía se acuerda de su punto de partida;
después, sólo depende de dónde está y de lo que le rodea. Es útil porque te
dice cuánto tienes que esperar para que las cosas dejen de importar, y cuánto
tienes que mirar para ver algo cambiar.»

**6.F2** Guion: «Si fumigas, matas plaga y también matas a los bichos que se
comen la plaga. La plaga se recupera deprisa porque se reproduce deprisa; sus
depredadores, no. Así que al cabo de unas semanas tienes menos enemigos de la
plaga que antes, y la plaga vuelve con más fuerza. No es que el insecticida no
funcione: es que funciona con los dos, y a ti sólo te interesaba uno.»

---

### Extensión

**6.Z1** ★ *Pista 1:* haz la lista de supuestos de Volterra antes de buscar nada; salen cuatro, y todos están en la forma de las dos ecuaciones.
*Pista 2:* la pregunta interesante no es cuáles se han corregido, sino **cuál de sus conclusiones sobrevive** a las correcciones.
*Solución:* Volterra suponía: mezcla homogénea, crecimiento exponencial de las
presas sin límite, respuesta funcional lineal (un depredador come
proporcionalmente a la densidad de presas), sin estructura de edad ni espacio.
Un modelo moderno añade al menos: capacidad de carga, respuesta funcional
saturante (tipo Holling II o III), estructura espacial y ruido demográfico. Lo
notable es que **el principio de Volterra sobrevive cualitativamente** a la
mayoría de esas modificaciones, aunque la conservación exacta no.

**6.Z2** ★ *Pista 1:* la aproximación de estado estacionario dice que un intermediario cambia despacio comparado con algo. ¿Comparado con qué, exactamente?
*Pista 2:* compara las escalas de tiempo del complejo y del sustrato. El cociente que salga es el parámetro pequeño, y la condición es que sea pequeño.
*Solución:* La condición estándar es $e_0\ll s_0+K_M$: enzima mucho menos
abundante que sustrato. Numéricamente se comprueba integrando el sistema
completo y comparando con la aproximación; el error relativo escala con
$e_0/(s_0+K_M)$. Falla en el régimen de enzima abundante, frecuente **dentro de
la célula**, donde muchas enzimas están en concentraciones comparables a sus
sustratos. Es un caso donde una aproximación de libro de texto se usa fuera de
su dominio de validez de forma rutinaria.
