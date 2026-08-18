## Soluciones del capítulo 5

> Las soluciones son razonadas: el número final es lo menos importante. En los
> problemas ● y ★ con solución cerrada hay **Pista 1** y **Pista 2** antes de
> ella; tápalas con la mano y úsalas de una en una.
>
> Los de **Mundo real** (R) no llevan solución a propósito: su procedimiento
> está en el apéndice D.

---

### Calentamiento

**5.C1** $g=4\pi^2(2{,}50)/(3{,}17)^2=9{,}82$ m/s².
$\sigma_g/g=\sqrt{(\sigma_L/L)^2+(2\sigma_T/T)^2}
=\sqrt{(0{,}008)^2+(0{,}0316)^2}=0{,}0326$, luego $g=(9{,}82\pm0{,}32)$ m/s².
**Domina $T$**, y no por poco: contribuye el 94 % de la varianza, porque entra
al cuadrado. Regla general: los exponentes multiplican la importancia de una
medida.

**5.C2** Con resolución $d$, la lectura está uniformemente distribuida en un
intervalo de anchura $d$; la desviación típica de una uniforme es
$d/\sqrt{12}$, luego $u=0{,}1/\sqrt{12}=0{,}029$ mm. Asignar $0{,}1$ mm
sobreestima por un factor 3,5. Está en el GUM, apartado 4.3.7.

**5.C3** $\nu=22$. $\chi^2=87$ da $\chi^2_\nu=3{,}95$: el modelo está mal o los
errores están subestimados. $\chi^2=6$ da $\chi^2_\nu=0{,}27$: errores
sobreestimados, o datos preprocesados, o el modelo tiene demasiados parámetros
libres. **Las dos situaciones son problemas, no una buena y otra mala.**

**5.C4** $\sigma_{a+b}=\sqrt{4+9+2(-0{,}8)(2)(3)}=\sqrt{3{,}4}=1{,}84$;
$\sigma_{a-b}=\sqrt{4+9+9{,}6}=4{,}75$. Con correlación negativa fuerte, **la
suma está mucho mejor determinada que cualquiera de los dos por separado**. Es
frecuente en ajustes: hay una combinación bien medida y otra pésimamente
medida, y sólo la elipse lo revela.

---

### Estimación

**5.E1** El tiempo de reacción humano tiene $\sigma\approx0{,}1$ s. Para una
caída de 1 s, el 0,1 % es 1 ms, lo que exige
$n=(\sigma/\text{objetivo})^2=(0{,}1/0{,}001)^2=10^4$ medidas… **si no hubiera
sesgo**. Pero el tiempo de reacción tiene un sesgo sistemático (se anticipa la
parada más que el arranque) de decenas de ms, que no se promedia. Conclusión:
**no es viable con cronómetro manual, a ninguna $n$**. Hace falta cambiar de
método, no de esfuerzo.

**5.E2** Tipo B: no procede de repeticiones estadísticas sino de juicio. Una
persona entrenada acierta la temperatura ambiente dentro de ±2 °C; sin
entrenamiento, ±4 °C. Declararlo como tipo B es perfectamente legítimo y es
justo lo que el GUM contempla.

**5.E3** ● *Pista 1:* $\alpha_{\text{acero}}\approx1{,}2\times10^{-5}$ K⁻¹.
*Pista 2:* el efecto es proporcional a la longitud y el error de lectura no. Iguálalos y sabrás a partir de qué distancia deja de ser despreciable.
*Solución:* $\Delta L/L=\alpha\Delta T=1{,}2\times10^{-5}\times15
=1{,}8\times10^{-4}$. En 10 m son 1,8 mm; en 1 m, 0,18 mm. Si tu error de
lectura es de 0,5 mm, el efecto térmico importa más a partir de unos 3 m. Por
eso las cintas de topografía llevan indicada su temperatura de calibración y
por eso las medidas de precisión se corrigen.

---

### Modelado

**5.M1** Cinco fuentes: (i) resistencia térmica de contacto en las interfaces;
(ii) pérdidas laterales no unidimensionales; (iii) calibración de los
termopares; (iv) no estacionariedad (aún no ha llegado al régimen permanente);
(v) espesor de la muestra mal medido. Detección **sin conocer la verdad**:
variar el espesor (si la conductividad aparente depende del espesor, hay
resistencia de contacto); variar el salto térmico (si depende, hay radiación o
convección); medir con dos pares de sensores; comprobar la deriva temporal.
**La estrategia general es hacer variar aquello de lo que el resultado no
debería depender.**

**5.M2** Protocolo ABBA: mide patrón, muestra, muestra, patrón. Con deriva
lineal, la media de las dos medidas del patrón corresponde al mismo instante
medio que la media de las dos de la muestra, y la deriva se cancela
exactamente. Es un clásico de la metrología y de la espectrometría de masas.

**5.M3** ● *Pista 1:* antes de combinar, comprueba compatibilidad.
*Pista 2:* calcula en cuántas sigmas difieren y qué $\chi^2$ da la combinación. Si el resultado es incompatible, combinar la media ponderada sin más esconde el problema en vez de resolverlo.
*Solución:* la diferencia es $0{,}9\pm0{,}36$, es decir 2,5 sigmas. Con dos
medidas, eso ocurre por azar un 1,2 % de las veces. **Combinar sin más sería
un error**: el $\chi^2$ de la combinación es 6,2 con 1 grado de libertad. Lo
correcto es (a) buscar el error sistemático no contabilizado en alguno de los
dos, y (b) si no se encuentra, aplicar el procedimiento del PDG: inflar la
incertidumbre combinada por $\sqrt{\chi^2_\nu}=2{,}5$. La media ponderada da
$10{,}82\pm0{,}17$; inflada, $10{,}82\pm0{,}42$. Lo que **no** vale es
publicar $\pm0{,}17$ como si nada hubiera pasado.

---

### Derivación

**5.D1** $y=f(x_0+\delta)=f(x_0)+f'\delta+\tfrac12 f''\delta^2+\dots$
Tomando varianzas y quedándose en el primer orden,
$\sigma_y^2=(f')^2\sigma_x^2$. Lo despreciado es
$\tfrac14 (f'')^2 \operatorname{Var}(\delta^2)+f'f''E[\delta^3]+\dots$, es
decir todo lo que involucra curvatura y momentos de orden superior. Con
$\delta$ gaussiana, el sesgo de la media es exactamente
$\tfrac12 f''\sigma_x^2$.

**5.D2** $-\ln\mathcal{L}=\tfrac12\chi^2+$const. Con errores correlacionados,
$\chi^2=(\mathbf{y}-\mathbf{f})^T V^{-1}(\mathbf{y}-\mathbf{f})$ con $V$ la
matriz de covarianza de los datos: la suma de cuadrados se convierte en una
forma cuadrática con la inversa de la covarianza en el medio. Ignorar la
correlación de los datos es equivalente a sustituir $V^{-1}$ por su diagonal, y
puede sesgar el resultado gravemente.

**5.D3** ● *Pista 1:* desarrolla $f(x_0+\delta)$ a segundo orden y toma el valor esperado. El término lineal se anula; el cuadrático no.
*Pista 2:* el sesgo sale $\tfrac12 f''\sigma^2$ en los tres casos, pero uno de ellos tiene un problema peor que el sesgo. Pregúntate qué pasa cuando $x$ se acerca a cero.
*Solución:* Sesgo $\approx\tfrac12 f''(x_0)\sigma^2$.
Para $x^2$: $f''=2$, sesgo $=\sigma^2$ (relativo $(\sigma/x_0)^2$).
Para $1/x$: $f''=2/x^3$, sesgo relativo $(\sigma/x_0)^2$ **con el mismo
tamaño**, pero además la distribución tiene cola infinita.
Para $\ln x$: $f''=-1/x^2$, sesgo $-\tfrac12(\sigma/x_0)^2$.
La peor es $1/x$: no porque el sesgo a segundo orden sea mayor, sino porque
**el desarrollo no converge**: la función no es analítica en 0 y $\sigma$ es
comparable a la distancia a la singularidad.

**5.D4** ● *Pista 1:* minimiza la varianza de $\sum w_ix_i$ con la restricción $\sum w_i=1$. Un multiplicador de Lagrange basta.
*Pista 2:* los pesos salen inversamente proporcionales a las varianzas. Evalúa qué peso le toca a una medida diez veces peor y saca la consecuencia práctica.
*Solución:* Minimiza $\operatorname{Var}(\sum w_i x_i)=\sum w_i^2\sigma_i^2$
sujeto a $\sum w_i=1$. Lagrange da $w_i\propto1/\sigma_i^2$, y la varianza
resultante es $1/\sum(1/\sigma_i^2)$. Consecuencia práctica: **una medida diez
veces peor que otra aporta el 1 % del peso**. Casi siempre no merece la pena
incluirla, y si la incluyes es por robustez, no por precisión.

---

### Computacional

**5.P1** Coinciden en la primera cifra: con incertidumbres relativas del 3 %
la linealización es excelente. La discrepancia aparece por debajo del 1 % del
valor de $\sigma_g$, y el sesgo por curvatura de $1/T^2$ es de orden
$(\sigma_T/T)^2=0{,}025\,\%$: despreciable.

**5.P2** Con un atípico a 5 sigmas, `curve_fit` desplaza los parámetros varias
sigmas; `soft_l1` apenas se mueve. El precio del ajuste robusto es que las
barras de error dejan de tener la interpretación estándar y hay que obtenerlas
por bootstrap.

**5.P3** La nube de 500 ajustes reproduce la elipse muy bien mientras el
modelo sea aproximadamente lineal en los parámetros cerca del mínimo. Con
$\tau$ mal determinado (pocos datos, rango corto), la nube se curva en forma de
plátano y **la elipse deja de ser una descripción válida**: ahí es donde hace
falta perfil de verosimilitud o MCMC (capítulos 9 y 15).

---

### Experimento

**5.X1** $\sigma_\tau$ cae rápidamente hasta $t_{\max}\approx2\tau$ y a partir
de $t_{\max}\approx3\tau$ apenas mejora, porque la señal restante es menor que
el ruido. **Regla práctica: mide dos o tres tiempos característicos y para.**
Medir diez es tirar el tiempo; medir medio deja $\tau$ y $T_{\text{amb}}$
degenerados.

**5.X2** *Pista 1:* la matriz de covarianza supone que el estimador es normal y el modelo casi lineal en los parámetros. Anota esas dos hipótesis antes de comparar nada.
*Pista 2:* busca deliberadamente los casos donde fallan: pocos datos, no linealidad fuerte, un atípico. Ahí es donde los dos intervalos se separan.
*Solución:* El bootstrap y la covarianza coinciden cuando hay muchos datos y el
modelo es casi lineal en los parámetros. Divergen cuando (i) hay pocos datos,
(ii) el modelo es fuertemente no lineal, o (iii) hay atípicos. En esos casos el
bootstrap es más honesto porque no supone normalidad de los estimadores.

---

### Detective

**5.T1** El resultado está a 114 sigmas del valor real: es un sesgo puro. El
número de medidas es irrelevante porque, como dice el apartado 3.2, promediar
sólo ataca la parte aleatoria. Y hay una segunda pista: declarar $10^{-4}$ de
incertidumbre en $g$ exige controlar la altura al micrómetro y el tiempo al
microsegundo; **la propia cifra declarada es inverosímil**. Es el mismo
diagnóstico que el problema 4.T2.

**5.T2** Con 8 puntos y 6 parámetros quedan 2 grados de libertad: el modelo
tiene casi tantos parámetros como datos y puede pasar por donde quiera.
$R^2=0{,}9999$ es exactamente lo que se espera del sobreajuste, y
$\chi^2_\nu=0{,}12$ confirma que está ajustando el ruido. La respuesta: pídele
una validación con datos que no haya usado, o que reduzca parámetros hasta que
$\chi^2_\nu\approx1$. Capítulo 15.

**5.T3** ● *Pista 1:* una convergencia suave y monótona hacia el valor previo no es lo que produce el azar. Es lo que produce un procedimiento.
*Pista 2:* pregúntate qué hace un experimentador cuando su resultado difiere del aceptado, y qué hace cuando coincide. La asimetría entre esas dos conductas lo explica todo.
*Solución:* Es el patrón de **sesgo de confirmación heredado** que Feynman
describió para la carga del electrón. Lo produce un procedimiento asimétrico:
cuando un resultado nuevo difiere del anterior, se busca el error hasta
encontrarlo; cuando coincide, no se busca. El resultado es una convergencia
suave hacia el valor previo, sea cual sea. El remedio moderno es el **análisis
ciego**: el investigador no ve el resultado hasta que todos los cortes y
correcciones están congelados.

---

### Feynman

**5.F1** Guion: «Si el termómetro marca siempre dos grados de más, cada medida
que tomas tiene esos dos grados dentro. Al promediar, promedias también los dos
grados: siguen ahí, intactos. Promediar sólo borra lo que unas veces sobra y
otras falta. Lo que siempre sobra, siempre sobra.»

**5.F2** Guion: «Las barras de error te dicen cuánto se puede mover cada
parámetro por separado. La elipse te dice cómo se mueven juntos. Si la elipse
está inclinada, significa que puedes subir uno si bajas el otro y seguir
explicando los datos, pero no puedes subir los dos a la vez. Guardar sólo las
barras es como describir un pasillo diciendo su anchura y su longitud sin decir
que está torcido.»

---

### Extensión

**5.Z1** ★ *Pista 1:* mira las series históricas de constantes fundamentales y cuenta cuántas veces el valor aceptado cayó fuera de la barra del 68 % previa.
*Pista 2:* debería ser un 32 % de las veces. Compara con lo que sale de verdad, y cuidado con convertir la discrepancia en una regla universal.
*Solución:* El estudio de Henrion y Fischhoff encuentra que, en las series
históricas de constantes fundamentales, el valor finalmente aceptado quedó
fuera del intervalo de confianza del 68 % mucho más a menudo del 32 % esperado;
en algunas series, más de la mitad de las veces. La lectura práctica que se
desprende de esos datos es que una barra publicada se comporta más como si
fuera un factor de 2 a 3 mayor, aunque ese factor es una regla de andar por
casa que ellos no proponen como número: lo que su artículo documenta es el
exceso de confianza, no una corrección universal. Es una conclusión incómoda y
bien documentada, y conviene tenerla presente al leer cualquier resultado.

**5.Z2** ★ *Pista 1:* simula datos con error en $x$ y ajusta por mínimos cuadrados ordinarios. La pendiente no sale insesgada: sale **atenuada** hacia cero.
*Pista 2:* el factor de atenuación es un cociente de varianzas. Cuando lo tengas, busca cómo se llama este efecto en epidemiología.
*Solución:* Con error en $x$, mínimos cuadrados ordinarios **atenúa** la
pendiente hacia cero por un factor
$\lambda=\sigma_x^{2,\text{verdadero}}/(\sigma_x^{2,\text{verdadero}}+\sigma_x^{2,\text{error}})$.
Con un 20 % de error relativo en $x$, la pendiente puede subestimarse un 4 %; con
un 50 %, un 20 %. La regresión de Deming lo corrige si conoces el cociente de
varianzas. En epidemiología este efecto tiene nombre propio —*regression
dilution*— y explica parte de las discrepancias entre estudios observacionales.
