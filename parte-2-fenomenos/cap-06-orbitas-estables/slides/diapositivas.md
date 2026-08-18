---
title: "¿Por qué algunas órbitas son estables?"
subtitle: "Parte II · Fenómeno 6"
author: "La servilleta y el ordenador"
---

# El fenómeno

Simulas una elipse durante 2500 periodos. El perihelio precesa y la órbita se
cierra.

\vspace{1em}
\Large
**¿Es física o es de tu integrador?**

# Orden no es fidelidad

\centering
![](../figuras/fig_orbitas.pdf){width=100%}

| Método | Deriva secular | Deriva total |
|---|---|---|
| RK4 (orden 4) | $7{,}4\times10^{-3}$/ut | **849×** |
| Verlet (orden 2) | $4{,}9\times10^{-11}$/ut | 0,09 |

# La diferencia es el **tipo** de error

**RK4**: error **secular**, siempre en la misma dirección. La órbita se va.

**Verlet**: error **acotado y oscilante** alrededor del valor correcto.

\vspace{1em}

Verlet conserva exactamente el volumen de fases: resuelve exactamente un
hamiltoniano próximo, y un hamiltoniano conserva su energía.

\vspace{0.8em}

\Large
**Un sistema hamiltoniano exige un integrador hamiltoniano.**

# Y por eso la precesión es peligrosa

La órbita cerrada es frágil: sólo el potencial exactamente $1/r$ conserva el
vector de Laplace–Runge–Lenz.

\vspace{0.8em}

Cualquier perturbación produce precesión $\Rightarrow$ **la precesión es
información**.

\vspace{0.5em}

Mercurio: 43 arcsec/siglo tras descontar todo lo newtoniano. Primera confirmación
cuantitativa de la relatividad general.

\vspace{0.8em}

\alert{Y un integrador que no conserva la estructura produce precesión espuria.}

# ¿Es estable el sistema solar?

**Laplace y Lagrange**: a primer orden, sí.

**Poincaré (1890)**: las series divergen, y hay órbitas de complejidad
extraordinaria.

**KAM**: la mayoría de trayectorias sobreviven… para perturbaciones mucho
menores que las reales.

**Laskar (desde 1989)**: es **caótico**, tiempo de Lyapunov ~5 Ma.

\vspace{0.5em}

En ~1 % de las integraciones Mercurio colisiona o es eyectado en 5000 Ma.

\alert{No es una predicción: es una probabilidad.}

# Poincaré y el error impreso

1889: gana el premio del rey Óscar II.

El editor plantea una duda. Poincaré revisa y encuentra un **error grave**:
había supuesto que ciertas variedades se cerraban.

\vspace{0.8em}

Paga de su bolsillo la retirada de la edición: 3585 coronas, más que el premio
de 2500.

\vspace{0.8em}

\alert{La versión corregida contiene el descubrimiento del caos determinista,
sesenta años antes que Lorenz. El error no fue un accidente: fue el camino.}

# Lo esencial

* A tiempos largos importa el tipo de error, no el orden
* Hamiltoniano $\Rightarrow$ simpléctico
* Comprueba siempre las conservaciones
* La precesión es información… si no es tuya
* El paso adaptativo rompe la simplecticidad
