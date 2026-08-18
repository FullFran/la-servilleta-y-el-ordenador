---
title: "Cómo detectar qué término domina"
subtitle: "Parte III · Manual de campo 5"
author: "La servilleta y el ordenador"
---

# Cuatro pasos

1. **Adimensionaliza** — sin esto no se puede comparar nada
2. **Estima cada término** con valores típicos
3. **Ordena y quédate con los dos mayores**
4. **Comprueba**: sustituye la solución en los despreciados

\vspace{1em}

\alert{El paso 4 es el método. Sin él, es adivinar.}

# La tabla de términos

```text
TÉRMINO         ORDEN         ¿DOMINA?
inercia         1,2e3         sí
viscoso         1,5e-1        no (1e-4)
gravedad        1,2e1         no (1e-2)
tensión sup.    7,2e0         no (1e-2)
```

\vspace{0.8em}

Media hoja de papel. Y ahora sabes que es inercia pura y que la viscosidad sólo
importará en la capa límite.

# Cada número adimensional es un balance con nombre

| Compiten | Número |
|---|---|
| inercia / viscosidad | $Re$ |
| arrastre / difusión | $Pe$ |
| conducción / convección | $Bi$ |
| reacción / mezcla | $Da$ |

\vspace{0.5em}

Cuando encuentres un balance nuevo, pregunta si ya tiene nombre. Casi siempre lo
tiene.

# Las tres trampas

**El término pequeño con la derivada más alta** — capa límite

**El término pequeño que se acumula** — el criterio pasa a $\epsilon t\ll1$

**El régimen que cambia** — recalcular los números cuesta minutos
