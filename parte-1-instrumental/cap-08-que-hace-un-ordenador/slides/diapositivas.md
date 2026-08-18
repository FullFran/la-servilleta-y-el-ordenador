---
title: "Qué hace un ordenador"
subtitle: "Capítulo 8 · Cuando resuelve una ecuación"
author: "La servilleta y el ordenador"
date: "Parte I — El instrumental del modelador"
---

# La pregunta

`0.1 + 0.2 == 0.3` devuelve `False`.

\vspace{0.8em}

Y confiamos en simulaciones con $10^{12}$ operaciones seguidas.

\vspace{1em}
\Large
**¿Por qué funcionan, y cuándo dejan de funcionar?**

# La idea del capítulo, en una línea

\vspace{1em}
\Large

El ordenador **no resuelve tu ecuación**.

Resuelve otra parecida.

\vspace{1em}
\normalsize

Todo el cálculo numérico consiste en saber cuánto se parece, y en detectar
cuándo deja de parecerse.

# Tres errores, tres remedios

**Redondeo** — los reales no caben en 64 bits.
*Se cura reformulando el álgebra.*

**Truncamiento** — hemos discretizado.
*Se cura refinando o subiendo el orden.*

**Inestabilidad** — el método amplifica.
*No se cura: hay que cambiar de método o de paso.*

\vspace{0.8em}

\alert{Confundir el segundo con el tercero cuesta días.}

# La aritmética que llevas puesta

\centering
![](../figuras/fig_coma_flotante.pdf){width=100%}

\raggedright\small
$(1-\cos h)/h^2$ y $2[\sin(h/2)/h]^2$ son la misma matemática y aritméticas
distintas.

# El orden se mide, no se cree

```python
e1 = error(h)
e2 = error(h / 2)
print(f"orden medido: {np.log2(e1 / e2):.2f}")
```

\vspace{0.8em}

Si programas orden 4 y esto da 1, tienes un error de código.

\vspace{0.5em}

\alert{Es el test más barato del cálculo científico. La mitad de los errores
de implementación se manifiestan como pérdida de orden.}

# La pendiente en log-log **es** el orden

\centering
![](../figuras/fig_orden_convergencia.pdf){width=100%}

\raggedright\small
Y la comparación honesta no es a igual paso: es a igual **coste**.

# Estabilidad: el paso no lo decides tú

\centering
![](../figuras/fig_estabilidad.pdf){width=100%}

\raggedright\small
$h=0{,}0018$ funciona. $h=0{,}0022$ —un 20 % más— destruye el resultado. No hay
degradación gradual: hay un acantilado.

# Rigidez

Escalas muy distintas, y la rápida ya está muerta pero **sigue imponiendo el
paso**.

\vspace{1em}

Explícito: $h < 2/|\lambda_{\max}|$ durante toda la simulación.

Implícito: el paso lo fija la precisión, no la estabilidad.

\vspace{1em}

\alert{Si tu paso adaptativo se queda diminuto sin razón, tu problema es
rígido, no difícil.} `RK45` $\to$ `Radau` / `BDF`.

# Y ahora lo contraintuitivo

\centering
![](../figuras/fig_energia_integradores.pdf){width=100%}

\raggedright\small
Tras 2000 periodos: Euler $10^{43}$ · implícito 0,0000 · RK4 0,5000 ·
**simpléctico (orden 1) 0,5119 sin deriva**.

# La diferencia son dos líneas

```python
# Euler explícito              # Euler simpléctico
q += h * p                     p -= h * q
p -= h * q                     q += h * p    # ← p ya actualizado
```

\vspace{0.8em}

El simpléctico conserva **exactamente** el área en el espacio de fases.
Resuelve exactamente otro hamiltoniano muy próximo.

\vspace{0.8em}

\alert{Elige el método que respete la estructura, no el del número más alto.}

# De la EDO a la EDP

$$u_j^{n+1}=u_j^n+r(u_{j+1}^n-2u_j^n+u_{j-1}^n),
\qquad r=\frac{D\Delta t}{\Delta x^2}\le\frac12$$

\centering
![](../figuras/fig_cfl_calor.pdf){width=88%}

# Lo que significa la CFL

\Large

**La información no puede viajar más de una celda por paso.**

\normalsize
\vspace{1em}

Si tu esquema mira menos lejos de lo que la física mueve la señal, no puede
funcionar.

\vspace{1em}

Y duplicar la resolución espacial obliga a dividir el paso temporal por
cuatro: coste $\times 8$.

# Historia: Richardson, 1917

Primera predicción numérica del tiempo. Seis horas de pronóstico, seis semanas
de cálculo a mano, en los ratos libres de conducir ambulancias en el frente.

\vspace{0.5em}

Resultado: 145 hPa de cambio de presión. La realidad: unos pocos.

\vspace{0.8em}

Imaginó una «fábrica de predicción» con **64 000 computistas humanos**
coordinados con focos de colores. Arquitectura paralela, treinta años antes de
los ordenadores.

\vspace{0.8em}

\alert{En 1979 Lynch demostró que el método era correcto: el fallo estaba en
los datos iniciales.}

# Lo esencial

* El ordenador resuelve otra ecuación parecida
* Tres errores, tres remedios distintos
* El orden se mide: `log2(e(h)/e(h/2))`
* Compara a igual coste, no a igual paso
* La estabilidad impone un paso que no negocias
* Respeta la estructura: conservación, simplecticidad
* Convergencia $\neq$ corrección: soluciones manufacturadas

# Para llevarse a casa

\Large

Ante cualquier resultado numérico:

\vspace{0.5em}

**¿Qué operación está haciendo realmente el ordenador,
y he medido el orden?**

\vspace{1.2em}

\normalsize
Pregunta abierta: ¿qué significa «resolver» una ecuación caótica, si ninguna
trayectoria numérica es la verdadera?
