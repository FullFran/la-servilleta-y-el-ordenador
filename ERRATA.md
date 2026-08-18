# Erratas

Los errores encontrados en el libro, corregidos o no. **Las corregidas no se
borran: se marcan.** Un libro que dedica un capítulo entero a falsar modelos no
debería esconder lo que ha tenido que falsar de sí mismo.

Formato de cada entrada: dónde, qué decía, por qué estaba mal, qué dice ahora.

Si encuentras una, abre una issue. Instrucciones en [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Corregidas en v0.1

### E-001 · El experimento de la log-normal no demostraba el TCL

**Dónde:** capítulo 1, sección 4.2, y `codigo/fig_tormenta_mc.py`.

**Decía:** que la campana obtenida al propagar la incertidumbre por Monte Carlo
«es el teorema central del límite actuando sobre $\log E=\sum\log x_i$».

**Por qué estaba mal:** el código sorteaba cada $\log x_i$ de una **normal**.
Una suma de normales es normal exactamente, para cualquier $n$. La campana
estaba metida en los supuestos, no emergía de ellos: el experimento sólo podía
confirmar lo que se le había dado.

**Dice ahora:** los factores se sortean de una **Laplace** —picuda y de colas
pesadas, exceso de curtosis $+3$—, así que no hay normalidad escondida. Con los
cuatro factores del problema la suma **todavía no es normal**: su exceso de
curtosis medido vale $+1{,}54$. Un tercer panel enseña la emergencia con
$n=1,2,4,20$. Los resultados del capítulo apenas se mueven (mediana
$4{,}5\times10^{15}$ J, factor 42 entre P5 y P95, 72 Hiroshimas), pero ahora la
afirmación es cierta.

*Detectado por revisión externa; verificado contra el código antes de corregir.*

---

### E-002 · «Veinte órdenes de magnitud» de densidad de potencia

**Dónde:** capítulo 1, sección 3, y las diapositivas del capítulo.

**Decía:** que la potencia por unidad de volumen de la bomba y la tormenta
difieren en «unos veinte órdenes de magnitud».

**Por qué estaba mal:** con las escalas que da el propio párrafo —bomba en
microsegundos y cientos de metros, tormenta en media hora y cien kilómetros
cuadrados— el cociente sale entre $10^{10{,}3}$ y $10^{12{,}8}$. Para llegar a
20 haría falta un volumen de explosión de $\sim10^3$ m³, que contradice el
«cientos de metros» de la frase anterior. Error de ocho órdenes de magnitud en
el capítulo dedicado a los órdenes de magnitud.

**Dice ahora:** la comparación se **deriva** en el texto en vez de afirmarse, y
da unas **12 décadas**, con el rango 10–13 declarado explícitamente al variar
los supuestos.

*Detectado por revisión externa; el error resultó mayor de lo estimado.*

---

### E-003 · La promesa de apertura era más fuerte que el capítulo

**Dónde:** capítulo 1, primer párrafo, y las diapositivas.

**Decía:** «dentro de diez minutos vas a tener una respuesta que no se
equivocará por más de un factor 5».

**Por qué estaba mal:** el propio Monte Carlo del capítulo, 270 líneas después,
da un intervalo del 90 % de mediana $\times/\div 6{,}6$. El capítulo celebraba
ese resultado como «honesto» mientras la apertura prometía una cota que ese
mismo análisis no respalda. Justo el vicio contra el que está escrito el libro.

**Dice ahora:** «una respuesta que sitúa la energía en la década correcta», con
una frase que avisa de que prometer más sería deshonesto.

*Detectado por revisión externa.*

---

## Abiertas

Ninguna confirmada pendiente de corregir. Las revisiones sistemáticas que
todavía no se han hecho están en las issues de auditoría del repositorio:
matemática y física, bibliográfica e histórica, y computacional.
