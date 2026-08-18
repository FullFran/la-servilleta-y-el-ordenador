# III.5 — Cómo detectar qué término domina

---

## El problema

Tienes una ecuación con cinco términos. Casi seguro dos de ellos hacen el 95 %
del trabajo en el régimen que te interesa. Encontrarlos convierte un problema
intratable en uno resoluble a mano.

---

## El procedimiento, en cuatro pasos

### 1. Adimensionaliza

Sin esto no se puede comparar nada: los términos tienen unidades distintas y
«grande» no significa nada. Capítulo 2.

### 2. Estima el tamaño de cada término

Sustituye cada variable por su valor típico y evalúa. Un orden de magnitud
basta.

### 3. Ordena y quédate con los dos mayores

Si el tercero está una década por debajo, se desprecia. Si está al 50 %, no.

### 4. Comprueba

**Este paso es el método.** Resuelve el problema reducido y sustituye la
solución en los términos despreciados. Si siguen siendo pequeños, el balance
era correcto. Si no, elige otro par.

Esa comprobación distingue el balance dominante de adivinar, y es lo que casi
nadie hace.

---

## Cómo se ve en la práctica

| Situación | Términos que compiten | Número que decide |
|---|---|---|
| Fluido alrededor de un obstáculo | inercia y viscosidad | $Re$ |
| Transporte de un soluto | arrastre y difusión | $Pe$ |
| Enfriamiento de un objeto | conducción interna y convección externa | $Bi$ |
| Reacción en un reactor | reacción y mezcla | $Da$ |
| Partícula en un fluido | flotabilidad y agitación térmica | $\rho g V L/kT$ |
| Estructura bajo carga | rigidez y peso propio | número de Galileo |

Fíjate en el patrón: **cada número adimensional del capítulo 2 es exactamente
un balance dominante con nombre propio**. Cuando encuentres un balance nuevo,
merece la pena preguntarse si ya tiene nombre; casi siempre lo tiene.

---

## Las tres trampas

**El término pequeño con la derivada más alta.** Capítulo 13: si $\epsilon$
multiplica a $y''$, despreciarlo baja el orden de la ecuación y produce una
capa límite donde ese término manda. **El tamaño de un término no se juzga por
su coeficiente sino por su producto con la derivada, y la derivada puede ser
enorme en una región pequeña.**

**El término pequeño que se acumula.** Un efecto de $10^{-3}$ integrado durante
$10^4$ periodos no es un efecto de $10^{-3}$. El criterio no es $\epsilon\ll1$
sino $\epsilon t\ll1$.

**El régimen que cambia.** El balance dominante depende del punto de operación.
Un modelo validado en un régimen y usado en otro es el error del capítulo 15,
y la comprobación —recalcular los números adimensionales— cuesta minutos.

---

## Un truco práctico: la tabla de términos

Cuando el problema tiene más de tres términos, hazlo por escrito. Y lo primero
que se escribe **no** es la tabla: es el caso concreto, con números. Sin él la
tabla no significa nada, porque cada término cambia de tamaño con el punto de
operación.

```text
CASO: chorro de agua de una manguera
  rho = 1e3 kg/m^3    mu = 1e-3 Pa·s    gamma = 0,072 N/m
  U   = 10 m/s        L  = 0,02 m       g = 9,8 m/s^2

TÉRMINO              ORDEN DE MAGNITUD    FRACCIÓN DEL MAYOR
inercia              ρU²/L = 5,0e6        1
gravedad             ρg    = 9,8e3        2e-3
tensión superficial  γ/L²  = 1,8e2        4e-5
viscoso              μU/L² = 2,5e1        5e-6   ( = 1/Re, con Re = 2e5)
```

Media hoja de papel, y ahora sabes tres cosas. Que es un problema de inercia
pura. Que la viscosidad sólo importará en la capa límite, donde $L$ deja de ser
2 cm y pasa a ser el espesor de la capa —y ahí la fracción deja de ser $10^{-6}$.
Y que la tensión superficial, hoy irrelevante, será la que mande cuando el
chorro se rompa en gotas, porque entonces $L$ baja a un milímetro y $\gamma/L^2$
sube un factor 400 mientras la inercia sólo sube 20.

Fíjate en que **la fracción del viscoso frente al de inercia es exactamente
$1/\mathrm{Re}$**. No es casualidad: los números adimensionales que se aprenden
de memoria en un curso de fluidos son, uno por uno, cocientes de dos filas de
esta tabla. Hacer la tabla es reinventarlos cuando hacen falta, que es mucho
mejor que recordarlos.

---

## Lista de comprobación

```text
TÉRMINO DOMINANTE

□ ¿He adimensionalizado?
□ ¿He evaluado el orden de magnitud de cada término con valores típicos?
□ ¿He hecho la tabla y la he ordenado?
□ ¿Cuánto separa al segundo del tercero? ¿Una década, o un factor 2?
□ ¿He resuelto el problema reducido?
□ ¿He SUSTITUIDO la solución en los términos despreciados para comprobar?
□ ¿Alguno de los despreciados multiplica a la derivada de orden más alto?
□ ¿Alguno se acumula con el tiempo?
□ ¿Sigue valiendo el balance en el régimen en que voy a usar el modelo?
```

---

## Ejercicios de campo

**A.** Coge una ecuación de tu campo con cuatro o más términos y haz la tabla
completa para tu régimen de operación.

**B.** Encuentra el régimen donde el balance cambia: varía el parámetro
principal hasta que dos términos se crucen. Ese punto es una frontera de
régimen y suele tener nombre.

**C.** Busca un caso en tu campo donde alguien desprecie sistemáticamente un
término. Comprueba el número adimensional que lo justifica y si sigue siendo
válido hoy.

---

### Referencias

* **Bender, C. M. y Orszag, S. A.** *Advanced Mathematical Methods.* 1978,
  capítulo 3: el tratamiento canónico del balance dominante.
* **Barenblatt, G. I.** *Scaling.* Cambridge UP, 2003.
* **Acheson, D. J.** *Elementary Fluid Dynamics.* Oxford UP, 1990. Muchos
  balances dominantes trabajados en detalle.
