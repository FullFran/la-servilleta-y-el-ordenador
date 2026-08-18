---
title: "Fourier"
subtitle: "Capítulo 12 · Ver el mundo en frecuencias"
author: "La servilleta y el ordenador"
date: "Parte I — El instrumental del modelador"
---

# La pregunta

Grabas el zumbido de un motor: 44 100 números por segundo. Una maraña.

\vspace{1em}
\Large
**¿Cómo se averigua a qué revoluciones gira y si le falta un diente a un
engranaje?**

# Por qué las sinusoides y no otra base

$$\frac{d}{dt}e^{i\omega t}=i\omega\,e^{i\omega t}$$

\vspace{0.8em}

$e^{i\omega t}$ es un **autovector del operador derivada**.

\vspace{0.8em}

Toda EDO lineal con coeficientes constantes está hecha de derivadas. En esa
base, derivar es multiplicar.

\vspace{0.5em}

\alert{Fourier es diagonalizar. Es el capítulo 11 en un espacio de funciones.}

# Gibbs: la esquina que no se deja hacer

\centering
![](../figuras/fig_series_fourier.pdf){width=100%}

\raggedright\small
6 armónicos: 1,1813 · 26: 1,1791 · 2501: 1,178956. Converge a
**1,178979**: 8,9 % de sobrepaso, para siempre.

# El teorema que lo hace útil

$$(f*g)(t)=\int f(\tau)g(t-\tau)d\tau
\qquad\Longleftrightarrow\qquad
\widehat{f*g}=\hat f\cdot\hat g$$

| $N$ | directo | vía FFT | factor |
|---|---|---|---|
| $10^3$ | $10^6$ | $10^4$ | 100 |
| $10^4$ | $10^8$ | $1{,}3\times10^5$ | 753 |
| $10^6$ | $10^{12}$ | $2\times10^7$ | **50 000** |

\vspace{0.5em}
\small
Tres páginas de Cooley y Tukey (1965) detrás de la tomografía, la resonancia
magnética, el radar y el MP3.

# Un filtro es una convolución

\centering
![](../figuras/fig_convolucion.pdf){width=95%}

# Aliasing: el error que no se puede deshacer

\centering
![](../figuras/fig_aliasing.pdf){width=100%}

\raggedright\small
8 Hz muestreados a 10 Hz aparecen como 2 Hz. **Indistinguibles de una señal
real de 2 Hz.**

# Y por eso el filtro va antes del conversor

La rueda de la diligencia en el cine. Las hélices en vídeo. Un proceso con
ciclo semanal muestreado a diario.

\vspace{1em}

\alert{La información perdida por aliasing no se recupera nunca. Filtrar
después, en el ordenador, no sirve de nada.}

\vspace{1em}

Cada vez que muestrees algo periódico: **¿cuál es mi frecuencia de Nyquist?**

# El periodograma no converge

\centering
![](../figuras/fig_psd.pdf){width=100%}

\raggedright\small
Dieciséis veces más datos, el mismo ruido. Cada punto se estima con **dos
grados de libertad**, independientemente de $N$.

# Welch, y el compromiso

Parte en $K$ segmentos, promedia: la varianza baja como $1/K$.

\vspace{0.8em}

Y la resolución empeora como $1/K$.

\vspace{1em}

```python
f, P = signal.welch(x, fs, nperseg=4096)     # sí
P = np.abs(np.fft.rfft(x))**2                # no
```

# Tiempo o frecuencia, no las dos

$$\Delta t\,\Delta\omega\ge\tfrac12$$

\vspace{0.8em}

Para separar dos tonos a $\Delta f$, hay que medir $1/\Delta f$.

\vspace{0.5em}

Dos tonos a 1 Hz de distancia: **un segundo de señal**, y no hay algoritmo que
lo evite.

\vspace{0.8em}

\small
Heisenberg es un caso particular: posición y momento están relacionados por una
transformada de Fourier.

# La ecuación del calor, en dos líneas

$$\partial_t u = D\,\partial_x^2 u
\quad\xrightarrow{\ \partial_x\to ik\ }\quad
\hat u(k,t)=\hat u(k,0)\,e^{-Dk^2 t}$$

\vspace{1em}

Cada modo evoluciona **solo**. La EDP se ha convertido en infinitas EDO
desacopladas.

\vspace{0.8em}

Y $e^{-Dk^2t}$ dice algo enorme: los detalles finos mueren primero, el tiempo
de difusión va como $L^2$, y **el problema inverso está mal condicionado por
construcción**.

# Fourier, 1807

Presenta a la Académie que cualquier función se representa con senos y cosenos.

Comité: Lagrange, Laplace, Monge, Lacroix. **Lagrange se opone.**

La memoria no se publica. Fourier publica el libro en **1822**.

\vspace{0.8em}

* **Fourier tenía razón en lo esencial**: la representación funciona
* **Lagrange tenía razón en el detalle**: faltaba una noción de convergencia

\vspace{0.5em}

Esa noción llegó con Dirichlet en 1829, y de la discusión salió medio análisis
moderno.

# Y un doble fondo

Cooley y Tukey, 1965. Contexto: detección sísmica de ensayos nucleares.

\vspace{1em}

1984: Heideman, Johnson y Burrus descubren que **Gauss tenía el algoritmo en
1805**, para interpolar las órbitas de Palas y Juno.

\vspace{0.5em}

En latín, notación oscura, sin publicar. Apareció póstumo en 1866.

\vspace{0.8em}

\alert{Siglo y medio de cálculo, escondido en un cuaderno.}

# Lo esencial

* Las sinusoides son los autovectores de la derivada
* Gibbs: 8,9 % que no desaparece nunca
* Convolución en el tiempo = producto en frecuencia
* Aliasing no se arregla después
* El periodograma no converge: usa Welch
* $\Delta t\,\Delta\omega\ge1/2$: no hay algoritmo que lo evite

# Para llevarse a casa

\Large

Ante cualquier señal muestreada:

\vspace{0.5em}

**¿Cuál es mi Nyquist, cuál mi resolución,
y cuántos grados de libertad tiene mi espectro?**

\vspace{1.2em}

\normalsize
Pregunta abierta: si Gauss tenía la FFT en 1805 y no la publicó, ¿cuántas ideas
equivalentes hay hoy en repositorios sin leer?
