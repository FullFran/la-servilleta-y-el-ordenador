---
title: "Cómo usar simulaciones sin engañarte"
subtitle: "Parte III · Manual de campo 8"
author: "La servilleta y el ordenador"
---

# La asimetría peligrosa

\Large
Una simulación siempre produce números.

**Nunca dice «no lo sé».**

# Cinco preguntas antes

1. ¿Qué espero que pase? *(escrito)*
2. ¿Qué resultado me haría sospechar? *(escrito)*
3. ¿Cuál es el caso trivial que sé resolver?
4. ¿Qué se conserva?
5. ¿Qué decisión va a cambiar este resultado?

# Cinco comprobaciones después

* ¿Cambia con la **semilla**?
* ¿Cambia al reducir el **paso** a la mitad?
* ¿Cambia con otro **método**?
* ¿Cambia al duplicar el **tamaño** del sistema?
* ¿Es robusto a perturbar los **parámetros** un 1 %?

# Los cinco autoengaños

* **El resultado bonito** — cuanto más te gusta, menos lo compruebas
* **La gráfica que convence** — mira los ejes
* **El barrido que no barre** — cien casos del parámetro irrelevante
* **El código que ya funcionaba** — errores latentes en regímenes nuevos
* **La conclusión que ya estaba** — parar de comprobar cuando aparece

# Qué constituye evidencia

\Large

Una simulación es evidencia de **las consecuencias de tus supuestos**.

\normalsize
\vspace{1em}

No del mundo, salvo en la medida en que los supuestos lo describan.

\vspace{0.8em}

Di qué modelo has simulado, no sólo qué ha salido. Y si la conclusión depende de
un supuesto sin verificar, dilo **en la conclusión**.
