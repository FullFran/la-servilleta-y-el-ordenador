---
title: "¿Cuánto tarda algo en enfriarse?"
subtitle: "Parte II · Fenómeno 2"
author: "La servilleta y el ordenador"
---

# El fenómeno

Café a 92 °C. Veinte minutos después, 60.

\vspace{1em}
\Large
**¿Cuál de los tres mecanismos se ha llevado más calor?**

\vspace{0.8em}
\normalsize
Y la pregunta incómoda: **¿cómo lo averiguarías sin buscarlo?**

# Tres mecanismos, tres firmas

| Mecanismo | Ley | Dependencia |
|---|---|---|
| Convección | $hA\Delta T$ | lineal |
| Radiación | $\varepsilon\sigma A(T^4-T_a^4)$ | superlineal |
| Evaporación | $Lk_mA\Delta\rho_v$ | **exponencial** |

\vspace{0.5em}

Cada uno depende de $\Delta T$ de forma distinta. **Ahí está la manera de
separarlos.**

# Los tres son del mismo orden

\centering
![](../figuras/fig_mecanismos_cafe.pdf){width=100%}

# Pero los parámetros son estimados

Variar $k_m$ un factor 2 mueve la evaporación entre el 14 % y el 40 %.

\vspace{1em}

\alert{El modelo con parámetros de manual **no resuelve la pregunta**.}

\vspace{1em}

Hay que medir. Y eso es lo interesante.

# Cómo se separan: anulando, no ajustando

**Pesar la taza** — la evaporación quita masa; los otros no

**Tapar** — elimina evaporación, apenas toca radiación

**Papel de aluminio** — $\varepsilon: 0{,}9\to0{,}05$, factor 18 en radiación

\vspace{1em}

Diseño factorial $2^2$: cuatro experimentos, una tarde, cuatro euros.

\vspace{0.5em}

\alert{Cuando dos mecanismos ajustan igual, no se separan con más datos del
mismo tipo.}

# ¿Y por qué funcionaba el modelo mínimo?

Porque en el rango de una taza **los tres son casi lineales**:

* convección, por definición
* radiación: $T^4-T_a^4\approx4T_a^3\Delta T$, 25 % de error
* evaporación: su no linealidad importa cuando ya aporta poco

\vspace{0.8em}

\Large
La «ley de Newton» no es una ley: es la **linealización conjunta** de tres
procesos.

# Y eso hace una predicción falsable

Si es una linealización, el $\tau$ ajustado debe **depender del rango
ajustado**.

\vspace{1em}

Primeros 10 min: $\tau$ menor. Hora completa: $\tau$ mayor.

\vspace{1em}

Es exactamente lo que se observa. Firma inconfundible de un modelo linealizado
usado fuera de su punto de expansión.

# Lo esencial

* La ley de Newton es tres mecanismos disfrazados de uno
* Cada uno tiene su firma funcional
* Se separan **anulando**, no ajustando
* Pesar la taza es una medida independiente
* Un modelo linealizado se delata solo
