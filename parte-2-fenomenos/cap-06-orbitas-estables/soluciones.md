## Soluciones de II.6

**II.6.1** $\dot E=\mathbf{p}\cdot\dot{\mathbf p}/m+\nabla V\cdot\dot{\mathbf q}
=\mathbf{v}\cdot(-\nabla V)+\nabla V\cdot\mathbf{v}=0$.
$\dot{\mathbf L}=\mathbf{q}\times\mathbf{F}=0$ porque la fuerza es central.

**II.6.2** $T=2\pi a^{3/2}=2\pi$ (tercera ley de Kepler en esas unidades).

**II.6.3** El vector LRL es $\mathbf{A}=\mathbf{p}\times\mathbf{L}-mk\hat r$. Al
derivar aparece un término proporcional a $\partial_r(r^2 F(r))$ que se anula
sólo si $F\propto1/r^2$. Cualquier otra ley de fuerza central da $\dot{\mathbf
A}\neq0$ y por tanto precesión.

**II.6.4** El determinante de la matriz de un paso de Euler explícito es
$1+h^2\omega^2>1$: el área en el plano de fases crece cada paso, y con ella la
energía. La órbita se abre exponencialmente.

**II.6.5** Sale 2. Verlet es de orden 2 en la posición, y su virtud no es el
orden sino la simplecticidad.

**II.6.6** Yoshida de orden 4 usa tres pasos de Verlet con coeficientes
$w_1=w_3=1/(2-2^{1/3})$, $w_2=-2^{1/3}/(2-2^{1/3})$. **Nótese el coeficiente
negativo**: hay un paso hacia atrás en el tiempo, y eso es inevitable para
órdenes altos en métodos simplécticos explícitos. A igualdad de coste, mejora la
deriva en varios órdenes de magnitud.

**II.6.7** La precesión por órbita es lineal en el coeficiente a primer orden. Es
un buen test: si tu medida no es lineal en el coeficiente, hay contaminación
numérica.

**II.6.8** ● (i) **Reduce el paso a la mitad**: si la migración cambia, es
numérica. (ii) **Cambia a un integrador simpléctico** si no lo era. (iii)
Comprueba la conservación de la energía y del momento angular total: una
migración física conserva el momento angular total del sistema, redistribuido
entre cuerpos; una migración numérica no lo conserva. La tercera es la
diagnóstica.

**II.6.9** ★ Con Verlet y paso de un día, mil años de sistema solar interior dan
errores de posición del orden de $10^{-6}$ UA para los planetas interiores, si
se incluyen todas las perturbaciones mutuas. Las discrepancias con las
efemérides reales delatan lo que falta: la Luna tratada como cuerpo separado, la
relatividad general, el achatamiento solar, y los asteroides masivos.
