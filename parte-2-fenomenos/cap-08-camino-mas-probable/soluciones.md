## Soluciones de II.8

**II.8.1** $t(x)=\sqrt{x^2+a^2}/v_1+\sqrt{(d-x)^2+b^2}/v_2$. Derivando e
igualando a cero: $\frac{x}{v_1\sqrt{x^2+a^2}}=\frac{d-x}{v_2\sqrt{(d-x)^2+b^2}}$,
que es $\sin\theta_1/v_1=\sin\theta_2/v_2$. La simulación lo confirma con cuatro
cifras.

**II.8.2** $\binom{20}{10}=184\,756$ caminos monótonos, y muchísimos más si se
permite retroceder. Dijkstra visita cada nodo una vez: 100 nodos. **La
diferencia entre enumerar y explotar la estructura.**

**II.8.3** Si el camino óptimo de $A$ a $C$ pasa por $B$, su tramo $B\to C$ debe
ser óptimo: si hubiera uno mejor, se podría sustituir y mejorar el total. La
propiedad de Markov entra en que el coste del tramo $B\to C$ **no depende de
cómo se llegó a $B$**.

**II.8.4** Dijkstra da por definitivo el nodo de menor distancia provisional; con
pesos negativos, una arista posterior puede mejorar esa distancia y la
suposición se rompe.

**II.8.5** Variando $S=\int L(q,\dot q,t)dt$ e integrando por partes con extremos
fijos: $\frac{d}{dt}\frac{\partial L}{\partial\dot q}-\frac{\partial L}
{\partial q}=0$.

**II.8.6** Con $\epsilon$ grande, todos los caminos son casi equiprobables. Al
bajar, la fracción de muestras en el óptimo tiende a 1, y la anchura de la
distribución de costes escala como $\epsilon$ (no como $\sqrt\epsilon$: la
anchura en el **espacio de caminos** es $\sqrt\epsilon$, la de los **costes**,
$\epsilon$).

**II.8.7** Viterbi maximiza $\prod P$, que tomando logaritmos es minimizar
$\sum(-\log P)$: costes aditivos sobre un grafo dirigido acíclico de
(estado, tiempo). Es literalmente Dijkstra con la topología ya ordenada, y por
eso su coste es $\mathcal{O}(T\,S^2)$.

**II.8.8** Hay **empates** entre caminos de igual coste y el algoritmo los
desempata por orden de inserción. No es un error, pero conviene saberlo: si el
resultado se usa aguas abajo, hay que fijar un criterio de desempate
determinista o el sistema no será reproducible (capítulo 16).

**II.8.9** ★ Candidatos frecuentes: planificación de mantenimiento (secuencia de
intervenciones que minimiza coste total), alineamiento de series temporales
(*dynamic time warping*), segmentación de señales, y elección de la secuencia
de operaciones en un proceso productivo. Todos son programación dinámica y casi
nunca se formulan así.
