## Problemas del capítulo 11

**Marcas:** ○ directo · ◐ requiere pensar · ● difícil · ★ abierto.

---

### Calentamiento

**11.C1** ○ Calcula autovalores y autovectores de
$\begin{pmatrix}2&1\\1&2\end{pmatrix}$ e interprétalos como modos de dos masas
acopladas.

**11.C2** ○ ¿Cuál es el número de condición de $\operatorname{diag}(1,10^{-6})$?
¿Cuántas cifras pierdes al resolver con ella?

**11.C3** ○ Una matriz de datos tiene valores singulares
$100, 40, 12, 0{,}3, 0{,}2, 0{,}18$. ¿Cuál dirías que es su rango efectivo? ¿Qué
información necesitas para decidirlo bien?

**11.C4** ○ Demuestra que $\kappa(A^TA)=\kappa(A)^2$ para $A$ de rango
completo.

---

### Estimación

**11.E1** ◐ Estima la memoria y el tiempo de resolver un sistema denso de
$10^5$ incógnitas. ¿Y si es disperso con 7 no nulos por fila?

**11.E2** ◐ Estima el número de condición de la matriz de Vandermonde de grado
20 en $[0,1]$. ¿Se puede ajustar un polinomio de grado 20 en doble precisión?

**11.E3** ● Estima cuántas componentes principales hacen falta para representar
imágenes de caras de $100\times100$ píxeles con un error visualmente
imperceptible. Contrasta después con la literatura de *eigenfaces*.

---

### Modelado

**11.M1** ◐ Escribe la matriz de un sistema de tres compartimentos con flujos
lineales. ¿Qué te dicen sus autovalores? ¿Y el autovector de autovalor cero, si
lo hay?

**11.M2** ◐ Una cadena de Markov con 4 estados. Explica qué significan el
autovalor 1, su autovector, y el segundo autovalor en módulo.

**11.M3** ● Modela la difusión de una idea en una red social de 1000 nodos con
$\dot{\mathbf{u}}=-L\mathbf{u}$. ¿Qué predice el segundo autovalor del
laplaciano sobre la velocidad de propagación? Contrástalo simulando.

---

### Derivación

**11.D1** ◐ Demuestra que para una matriz simétrica los autovectores de
autovalores distintos son ortogonales.

**11.D2** ◐ Deduce la SVD a partir de la diagonalización de $A^TA$ y $AA^T$.
¿Por qué los valores singulares son las raíces de los autovalores?

**11.D3** ● Demuestra el teorema de Eckart–Young: la mejor aproximación de
rango $k$ en norma de Frobenius es truncar la SVD.

**11.D4** ● Para $A$ no normal, demuestra que
$\|e^{At}\|\le\kappa(V)\,e^{\lambda_{\max}t}$ con $V$ la matriz de
autovectores, y explica por qué esa cota es inútil cuando $\kappa(V)$ es
enorme.

---

### Computacional

**11.P1** ○ Reproduce la figura de modos normales con 10 masas en lugar de 3.
¿Reconoces la forma de los modos? ¿A qué se parecen?

**11.P2** ◐ Compara resolver mínimos cuadrados por ecuaciones normales, por QR
y por SVD, con matrices de condición creciente. Dibuja el error frente a
$\kappa$.

**11.P3** ◐ Aplica SVD a una imagen real y dibuja el error de reconstrucción
frente al rango. Encuentra el rango que da un error del 1 %.

---

### Experimento

**11.X1** ◐ Genera matrices aleatorias $n\times n$ y estudia la distribución de
sus valores singulares al crecer $n$. Compárala con la ley de Marchenko–Pastur.

**11.X2** ● Construye una familia de matrices con autovalores fijos y grado de
no normalidad creciente. Dibuja la amplificación transitoria máxima frente al
número de condición de los autovectores. ¿Qué relación encuentras?

---

### Detective

**11.T1** ◐ Un código resuelve $A^TA\mathbf{x}=A^T\mathbf{b}$ y obtiene
resultados que cambian mucho al reordenar las columnas de $A$. ¿Qué pasa?

**11.T2** ◐ Un análisis PCA de datos con presiones en Pa, temperaturas en K y
caudales en m³/s encuentra que la primera componente explica el 91 % de la
varianza. ¿Es un resultado o un artefacto?

**11.T3** ● Un modelo linealizado de un flujo predice estabilidad para todos los
parámetros ensayados, y el experimento muestra inestabilidad reproducible.
Antes de acusar al experimento, ¿qué propiedad de la matriz comprobarías, y
cómo?

---

### Mundo real

**11.R1** ★ Coge una matriz que aparezca en tu trabajo y calcula su número de
condición. ¿Sabías que era ese? ¿Cambia si adimensionalizas?

**11.R2** ★ Busca en tu campo un análisis PCA publicado. ¿Dice el artículo si
estandarizó las variables? ¿Cambia la conclusión si no lo hizo?

---

### Feynman

**11.F1** ○ Explica qué es un autovector a alguien que sabe cálculo, usando el
ejemplo de las masas y los muelles.

**11.F2** ◐ Explica el número de condición sin ecuaciones, con la imagen de dos
rectas casi paralelas.

---

### Extensión

**11.Z1** ★ Lee Trefethen et al. (1993). ¿Cómo se calcula un pseudoespectro y
qué información añade sobre el espectro? Calcula el de la matriz no normal del
capítulo.

**11.Z2** ★ Estudia la SVD aleatorizada (Halko et al. 2011). Impleméntala y
compárala con la SVD completa en tiempo y precisión para una matriz de
$5000\times5000$ de rango efectivo 50.
