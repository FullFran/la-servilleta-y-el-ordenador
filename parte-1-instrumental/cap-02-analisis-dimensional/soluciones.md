## Soluciones del capítulo 2

> Las soluciones son razonadas: el número final es lo menos importante. En los
> problemas ● y ★ con solución cerrada hay **Pista 1** y **Pista 2** antes de
> ella; tápalas con la mano y úsalas de una en una.
>
> Los de **Mundo real** (R) no llevan solución a propósito: su procedimiento
> está en el apéndice D.

---

### Calentamiento

**2.C1** $[\mu]=\mathsf{M}\mathsf{L}^{-1}\mathsf{T}^{-1}$;
$[\nu]=\mathsf{L}^2\mathsf{T}^{-1}$;
$[k]=\mathsf{M}\mathsf{L}\mathsf{T}^{-3}\Theta^{-1}$;
$[\alpha]=\mathsf{L}^2\mathsf{T}^{-1}$;
$[\gamma]=\mathsf{M}\mathsf{T}^{-2}$;
$[k_B]=\mathsf{M}\mathsf{L}^2\mathsf{T}^{-2}\Theta^{-1}$.
Observación que conviene interiorizar: $\nu$ y $\alpha$ **tienen las mismas
dimensiones**. Por eso su cociente, el número de Prandtl, es adimensional y por
eso los problemas de transporte de cantidad de movimiento y de calor se parecen
tanto.

**2.C2** $7-4=3$ grupos. Si dos variables tienen dimensiones proporcionales, el
rango de la matriz baja y hay **más** grupos, no menos: la cuenta usa el rango,
no el número de dimensiones que aparecen escritas.

**2.C3** (a) correcta; (b) correcta; (c) **imposible**: suma una velocidad con
$\mu/\rho L$, que también es velocidad… en realidad es dimensionalmente
correcta, y ahí está la trampa del ejercicio: **la consistencia dimensional es
necesaria pero no suficiente**. La expresión es dimensionalmente válida y
físicamente absurda. (d) correcta; (e) correcta.

**2.C4** $Bi\ll1$ significa que la resistencia térmica interna del cuerpo es
mucho menor que la de su superficie: el interior se uniformiza mucho antes de
que la superficie logre evacuar el calor. Entonces basta con una sola
temperatura para todo el cuerpo y el problema pasa de EDP a EDO. Es
exactamente la licencia que nos permitirá escribir la ley de Newton del
enfriamiento en el capítulo 6.

---

### Estimación

**2.E1** Mano ($L\sim0{,}1$ m, $U\sim2$ m/s, $\nu_{aire}=1{,}5\times10^{-5}$):
$Re\sim10^{4}$, turbulento. Cuchara ($0{,}03$ m, $0{,}2$ m/s, agua):
$Re\sim6\times10^{3}$, turbulento a duras penas. Aorta ($0{,}02$ m, $0{,}3$
m/s, $\nu\approx4\times10^{-6}$): $Re\sim1500$, laminar con transición en
sístole —de hecho la aorta está justo en la frontera, lo cual no es casualidad
fisiológica—. Tráquea corriendo ($0{,}02$ m, $5$ m/s): $Re\sim7\times10^{3}$,
turbulento; por eso se oye.

**2.E2** Mosquito: punta del ala a $\sim3$ m/s, $Ma\sim0{,}01$, incompresible.
Latigazo: la punta supera los 340 m/s, $Ma>1$: **el chasquido es una onda de
choque**, y es el primer objeto fabricado por el hombre que rompió la barrera
del sonido. Aerogenerador: punta a $\sim80$ m/s, $Ma\sim0{,}24$; ese límite
existe por ruido y por erosión, no por compresibilidad.

**2.E3** ● *Pista 1:* usa la cuerda del perfil como longitud característica y la
velocidad relativa a tres cuartos del radio.
*Pista 2:* compara el $Re$ que salga con el de un avión comercial. Si difieren en órdenes de magnitud, la aerodinámica no es la misma, y ahí está la respuesta.
*Solución:* cuerda $\sim1$ cm, velocidad $\sim40$ m/s $\Rightarrow$
$Re\sim3\times10^{4}$. Un avión comercial vuela a $Re\sim10^{7}$. **Tres
órdenes de magnitud de diferencia**: a $Re\sim10^4$ la capa límite es laminar y
se desprende con facilidad, y los perfiles delgados y muy curvados funcionan
mejor que los perfiles gruesos de avión. No, no se pueden escalar. Es la misma
razón por la que un avión de papel y un Airbus no tienen la misma forma de ala.

---

### Modelado

**2.M1** Variables: $\Delta T$, tiempo $t$, tamaño $L$, difusividad $\alpha$,
coeficiente de convección $h$, conductividad $k$. Grupos:
$Fo=\alpha t/L^2$ (número de Fourier, «tiempo adimensional») y $Bi=hL/k$.
Si $Bi\ll1$ el problema colapsa a un parámetro y basta una exponencial; si
$Bi\gtrsim1$ hacen falta los dos y aparecen gradientes internos.

**2.M2** Aguas profundas: $c=f(\lambda,g)\Rightarrow c\propto\sqrt{g\lambda}$
(hemos quitado la profundidad, que ya no interviene). Aguas someras:
$c=f(h,g)\Rightarrow c\propto\sqrt{gh}$ (hemos quitado la longitud de onda).
Cada régimen se define por **qué variable se ha vuelto irrelevante**, y el
criterio de separación es $h/\lambda$, otro grupo adimensional.

**2.M3** ● *Pista 1:* si $E\propto M$ y $E=Mgh$, ¿de qué depende $h$?
*Pista 2:* el resultado es sorprendente y aproximadamente cierto. Para encontrar dónde falla, busca los dos extremos de tamaño y pregúntate qué término despreciado deja de ser pequeño en cada uno.
*Solución:* $h = E/(Mg) \propto M^0$: **la altura de salto no depende de la
masa**. Es la predicción clásica y es aproximadamente cierta en un rango
sorprendentemente amplio (saltamontes, ranas, humanos saltan del orden de
decenas de centímetros de elevación del centro de masas). Falla para animales
muy pequeños, donde el arrastre del aire deja de ser despreciable —la pulga
salta menos de lo que predice el modelo— y para los muy grandes, donde la
resistencia del hueso limita la fuerza aplicable. Dos correcciones distintas en
los dos extremos: un ejemplo perfecto de que un modelo puede fallar por arriba
y por abajo por razones sin ninguna relación.

---

### Derivación

**2.D1** Variables $T, L, g, m$ ($n=4$, $k=3$) $\Rightarrow$ un grupo:
$T\sqrt{g/L}$ = const. La masa desaparece sola, lo cual ya es un resultado. La
amplitud $\theta_0$ **no puede aparecer** en ese recuento porque es
adimensional: si la incluimos, $n=5$ pero $\theta_0$ ya es un π, así que hay dos
grupos y la relación es $T\sqrt{g/L}=\Phi(\theta_0)$ con $\Phi$ desconocida.
Para determinar $\Phi$ hace falta resolver la ecuación del movimiento (sale la
integral elíptica completa de primera especie) o medir.

**2.D2** Con $\hat t = t\sqrt{k/m}$ queda $\ddot{\hat x} + 2\zeta\dot{\hat x} +
\hat x = 0$, con $\zeta = c/(2\sqrt{km})$. **Un solo parámetro**: la razón de
amortiguamiento. Tres parámetros físicos se han reducido a uno, y todo el
comportamiento cualitativo (sobreamortiguado, crítico, subamortiguado) queda
determinado por si $\zeta$ es mayor, igual o menor que 1.

**2.D3** ● *Pista 1:* $p_0$ añade una variable y ninguna dimensión nueva.
*Pista 2:* con dos grupos adimensionales, la ley del capítulo es el límite en que el segundo tiende a cero. Escribe cuándo deja de serlo y tendrás el radio al que la ley muere.
*Solución:* $n=5$, $k=3$, luego **dos** grupos:
$\pi_1 = Et^2/(\rho R^5)$ y $\pi_2 = p_0 R^3/E$. La relación es
$\pi_1=\Phi(\pi_2)$. El resultado del capítulo corresponde al límite
$\pi_2\to0$, donde $\Phi$ tiende a una constante: la energía de la explosión
domina sobre el trabajo $p_0R^3$ contra la atmósfera. La ley deja de valer
cuando $p_0R^3\sim E$, es decir, cuando $R\sim(E/p_0)^{1/3}$. Con
$E=6{,}5\times10^{13}$ J y $p_0=10^5$ Pa sale $R\sim860$ m: a partir de ahí la
onda ya no es un frente fuerte, sino un pulso sonoro. Los datos de Taylor llegan
a 185 m, cómodamente dentro del régimen válido.

**2.D4** ● *Pista 1:* un grupo adimensional es un vector del núcleo.
*Pista 2:* el núcleo tiene dimensión $n-\operatorname{rango}$, no $n-k$. Busca un ejemplo con rango deficiente —longitud, área y volumen— y verás la diferencia.
*Solución:* la aplicación «producto de potencias» va de $\mathbb{R}^n$
(exponentes) a $\mathbb{R}^k$ (dimensiones resultantes) y es lineal; su matriz
es la matriz dimensional. Los grupos adimensionales son su núcleo, de dimensión
$n-\operatorname{rango}$. Ejemplo con rango deficiente: velocidad, aceleración y
tiempo. Aparecen $\mathsf{L}$ y $\mathsf{T}$ (dos dimensiones), pero la matriz
tiene rango 2 y $n=3$, luego un grupo, $at/v$. Ejemplo con rango realmente
deficiente: longitud, área y volumen: aparecen tres variables, sólo
$\mathsf{L}$, rango 1, dos grupos.

---

### Computacional

**2.P1** Con `scipy.linalg.null_space` sobre la matriz dimensional. La única
sutileza es que la base devuelta es ortonormal y con exponentes feos; conviene
racionalizarla multiplicando por el mínimo común denominador para obtener grupos
reconocibles.

**2.P2** Al añadir rozamiento aparece un tiempo característico nuevo,
$m/c$, y con él el grupo $\zeta$ del problema 2.D2. Los datos vuelven a
colapsar si se dibuja $T\sqrt{g/L}$ frente a $\theta_0$ **para cada $\zeta$
fijo**: es decir, el colapso pasa de una curva a una familia de curvas indexada
por el segundo grupo. Es exactamente lo que pasa al pasar de un π a dos.

**2.P3** Separando variables, $\int d\hat v/(1-\hat v^2)=\hat t$ da
$\operatorname{arctanh}\hat v=\hat t$, luego $\hat v=\tanh\hat t$. El 99 % de la
velocidad terminal se alcanza en $\hat t\approx2{,}6$, es decir en
$2{,}6\,v_t/g$. Para una gota con $v_t=8$ m/s, unos 2 s. Esa es la respuesta
cuantitativa a la estimación 1.E6.

---

### Experimento

**2.X1** El mínimo del error cuadrático es muy plano: con estos 16 puntos, los
exponentes entre 0,395 y 0,42 son prácticamente indistinguibles. Conclusión
honesta: **los datos son compatibles con 2/5, pero no lo demuestran**; lo que
hacen es no contradecirlo. Es una distinción que el capítulo 15 desarrollará.

**2.X2** *Pista 1:* genera los datos con dos grupos y dibuja el colapso usando sólo uno. Verás una banda, no una curva.
*Pista 2:* colorea los puntos de la banda por cada candidato a segundo grupo. El correcto la ordenará de forma monótona; los demás la dejarán revuelta.
*Solución:* Con dos grupos, un colapso en uno solo produce una banda cuya
**anchura** es una función del segundo grupo. Coloreando los puntos por
cualquier candidato a segundo grupo, el correcto ordena la banda de forma
monótona. Es una técnica real de descubrimiento y merece la pena practicarla.

---

### Detective

**2.T1** La fórmula $P=\rho N^3D^5$ (número de potencia constante) es correcta
**en el régimen turbulento**, donde la viscosidad efectivamente deja de
importar. Pero eso no lo dice el análisis dimensional: el análisis dimensional
con viscosidad da $Np = \Phi(Re)$, y sólo el **hecho experimental** de que
$\Phi$ se aplana a $Re$ alto justifica ignorarla. El error es presentar como
consecuencia del método lo que es una observación empírica. Con un fluido
viscoso a $Re$ bajo, la fórmula falla estrepitosamente.

**2.T2** Es cierto en el vacío. En aire, falta el arrastre, que introduce
$\rho_{aire}$ y por tanto el cociente de densidades. El péndulo de corcho se
amortigua mucho antes y su periodo se desplaza ligeramente por la masa añadida
del fluido. La variable que falta es la densidad del medio, y con ella entra el
grupo $\rho_{aire}/\rho_{cuerpo}$.

**2.T3** ● *Pista 1:* una desviación sistemática en un extremo nunca es ruido.
*Pista 2:* pregúntate si la relación es monótona. Ajustar una potencia única a algo que sube y luego baja produce un exponente sin significado y un residuo con forma.
*Solución:* la sospecha correcta es que **no hay una sola ley**, sino dos
regímenes: la velocidad máxima crece con la masa hasta unos 100 kg y luego
decrece (guepardo frente a elefante). Ajustar una única potencia a un
comportamiento no monótono produce un exponente promedio sin significado y un
residuo estructurado. La comprobación que hay que pedir es la **gráfica de
residuos frente a la masa**: si tienen forma, el modelo está mal especificado.
Este es exactamente el diagnóstico del capítulo 5 y el pecado del capítulo 15.
Y es un caso real: la relación velocidad–masa en mamíferos es no monótona
(Hirt et al., Nature Ecology & Evolution, 2017).

---

### Feynman

**2.F1** Guion: «Las leyes de la naturaleza existían antes que el metro. Si
escribo una fórmula que sólo funciona en metros, no he descrito la naturaleza:
he descrito mi cinta métrica. Eso obliga a que todo lo que aparezca en una ley
se combine de manera que las unidades se cancelen, y esa obligación es tan
fuerte que muchas veces sólo queda una combinación posible. Entonces la fórmula
está determinada salvo un número.»

**2.F2** Guion: «La fuerza con la que te agarras al techo depende de la
superficie de tus pies; el peso que tienes que sostener depende de tu volumen.
Al hacerte grande, el volumen crece más deprisa que la superficie. Un insecto
tiene superficie de sobra para su peso; un elefante, ni de lejos. No es que el
insecto sea más fuerte: es que es más pequeño.»

---

### Extensión

**2.Z1** ★ *Pista 1:* a $Re\ll1$ las ecuaciones no tienen término de inercia, y eso las hace reversibles en el tiempo. Piensa qué implica para un ciclo de movimiento.
*Pista 2:* si el ciclo es idéntico hacia delante y hacia atrás, el desplazamiento neto es cero. Para avanzar hay que romper esa simetría, y hay dos formas clásicas de hacerlo.
*Solución:* El teorema de la vieira: a $Re\ll1$ el flujo es reversible en el
tiempo, así que cualquier ciclo de movimiento que sea idéntico hacia delante y
hacia atrás produce desplazamiento neto nulo. Una vieira que abre y cierra dos
valvas no avanza. Hace falta romper esa simetría: un flagelo que gira, o dos
articulaciones desfasadas. La conclusión general —que la simetría del
movimiento determina si el movimiento es posible— reaparecerá en los capítulos
7 y II.9.

**2.Z2** ★ *Pista 1:* la autosemejanza de segunda especie aparece cuando el exponente no sale de contar dimensiones sino de resolver un problema de autovalores.
*Pista 2:* en los datos se reconoce por un colapso que «casi» funciona y que mejora al ajustar un exponente pequeño. Desconfía: puede ser eso o puede ser sobreajuste.
*Solución:* Un ejemplo estándar es la propagación de un frente de filtración en
medios porosos, donde el exponente del frente contiene una potencia anómala que
se obtiene resolviendo un problema de autovalores no lineal. La señal en los
datos es un colapso que «casi» funciona y que mejora al elevar uno de los ejes
a una potencia pequeña ajustada. Cuando veas a alguien ajustando un exponente
para que colapse, o estás ante autosemejanza de segunda especie, o ante un
ajuste sin contenido: las dos cosas se parecen mucho y sólo la teoría las
distingue.
