## Soluciones de II.14

**II.14.1** $\hat h(k)=e^{-\sigma^2k^2/2}$. Cae a $10^{-6}$ en
$k=\sqrt{2\ln10^6}/\sigma=5{,}26/\sigma$. Es decir: por encima de una
frecuencia del orden de $5/\sigma$, el instrumento no deja pasar nada, y ahí no
hay información que recuperar.

**II.14.2** Se puede deconvolucionar mientras $|\hat h|>$ ruido relativo, es
decir $e^{-\sigma^2k^2/2}>10^{-3}$, o sea $k<3{,}7/\sigma$. **Reducir el ruido
un factor 1000 sólo extiende la banda útil un factor 1,4**, porque la
dependencia es logarítmica —igual que el horizonte de predicción del capítulo
7—.

**II.14.3** Para $|\hat h|^2\gg\lambda$ el filtro tiende a
$\overline{\hat h}/|\hat h|^2=1/\hat h$. Para $|\hat h|^2\ll\lambda$ tiende a
$\overline{\hat h}/\lambda\to0$: se apaga suavemente en vez de explotar.

**II.14.4** La esquina se localiza por máxima curvatura de la curva en
coordenadas log-log, como en el código del capítulo.

**II.14.5** Suelen dar $\lambda$ dentro de un factor 2–5 entre sí, lo que
corresponde a diferencias visibles pero no dramáticas en la solución. Cuando
discrepan mucho, es señal de que el nivel de ruido supuesto o el modelo directo
están mal.

**II.14.6** El resultado esperado está en el enunciado del experimento. Lo
importante del ejercicio es **escribir la frase final**: qué estructuras vienen
de los datos y cuáles del regularizador.

**II.14.7** Richardson–Lucy impone positividad y conserva el flujo total, y es el
estimador de máxima verosimilitud para ruido de Poisson. Con conteos bajos bate
claramente a Tikhonov, que supone ruido gaussiano de varianza constante. **El
regularizador correcto depende del modelo de ruido**, y ese es el punto.

**II.14.8** **Artefacto casi seguro.** Los anillos alrededor de fuentes puntuales
son el artefacto característico de la deconvolución: aparecen cuando el
algoritmo intenta reconstruir frecuencias por encima del corte del instrumento
y el filtro produce oscilaciones —es Gibbs del capítulo 12, en dos dimensiones—.
La comprobación: deconvolucionar una imagen sintética con una fuente puntual
conocida y comprobar si aparecen los mismos anillos.

**II.14.9** ★ Con una fuente puntual real —una luz lejana, un reflejo especular—
se puede estimar la PSF directamente. El resultado suele mejorar visiblemente y
también suele mostrar artefactos de anillo, lo que hace el ejercicio doblemente
instructivo.
