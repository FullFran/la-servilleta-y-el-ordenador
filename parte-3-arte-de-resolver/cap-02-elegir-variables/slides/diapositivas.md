---
title: "Cómo elegir variables"
subtitle: "Parte III · Manual de campo 2"
author: "La servilleta y el ordenador"
---

# La decisión que nadie declara

Qué se pone y qué se deja fuera.

\vspace{0.8em}

Determina todo lo demás, y es la que más veces arruina un trabajo.

# Cuatro preguntas, en orden

1. **¿Qué quiero predecir?** — con unidades y precisión
2. **¿De qué depende?** — lista larga primero, sin filtrar
3. **¿Cuáles son independientes?** — redundancia y dependencias ocultas
4. **¿Cuántas quedan al adimensionalizar?**

\vspace{0.8em}

\alert{El mismo sistema exige modelos distintos para preguntas distintas.}

# El filtro

Para cada candidata:

\vspace{0.5em}
\Large
**Si esta variable cambiara un factor 2, ¿cambiaría la salida?**

\normalsize
\vspace{0.8em}

No $\to$ fuera. «No lo sé» $\to$ dentro, hasta que lo sepas.

# Los descartes se escriben

```text
DESCARTADA: rugosidad de la superficie
MOTIVO: afecta a h en menos de un 5 % para Re < 10^4
VÁLIDO MIENTRAS: Re < 10^4 y sin incrustaciones
```

\vspace{0.8em}

Sirve para: revisarlo cuando el modelo falle, contestar a quien pregunte, y
**recomprobar cuando cambie el régimen**.

\vspace{0.5em}

Eso último casi nunca se hace, y es la causa más común de que un modelo fiable
deje de serlo.

# Cuatro criterios

* **Físicas** antes que ajustables
* **Medibles** antes que fundamentales
* **Combinaciones** antes que variables sueltas
* **Pocas** antes que muchas

\vspace{1em}

Con 50 datos, cinco parámetros ya es mucho.
