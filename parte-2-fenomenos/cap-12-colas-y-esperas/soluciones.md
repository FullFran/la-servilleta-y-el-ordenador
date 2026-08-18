## Soluciones de II.12

**II.12.1** $\rho=0{,}95$: $W=(1/100)/0{,}05=0{,}2$ s, veinte veces el tiempo de
servicio. Con $\rho=0{,}99$: $W=1$ s, **cien veces**. Un 4 % más de carga
multiplica la espera por cinco.

**II.12.2** $L=\lambda W=30\times1{,}25=37{,}5$ comensales de media. Si el
restaurante tiene 40 plazas, está al límite.

**II.12.3** Carga ofrecida $a=\lambda/\mu=6$ erlangs. Con $c=7$, $\rho=0{,}857$ y
la espera en cola sale del orden de 1,5 min; con $c=8$, unos 0,4 min. Respuesta:
**8 cajas** para cumplir el objetivo con margen.

**II.12.4** El factor $(1+c_v^2)/2$ pasa de 1 a 0,625: **una reducción del 37,5 %
de la espera en cola**, sin tocar la capacidad ni la tasa de llegada.

**II.12.5** Con lotes de 5 a la misma tasa media, la espera crece
sustancialmente: los clientes del final de cada lote esperan a los 4 anteriores.
El efecto es equivalente a aumentar $c_v$.

**II.12.6** ● A $\rho=0{,}9$ con 5 servidores, la cola única mejora la media en un
factor ~2–3 y el p95 en un factor mayor. La razón del segundo es que en colas
separadas hay una probabilidad apreciable de quedar detrás de un cliente muy
lento, y esa situación desaparece con cola única.

**II.12.7** ● Con abandono, el sistema **siempre alcanza un estado estacionario**,
incluso con $\rho>1$: la tasa de abandono equilibra el exceso. La cola se
estabiliza en una longitud donde la paciencia media coincide con la espera. Es
lo que ocurre en cualquier centro de llamadas real, y explica por qué las
fórmulas sin abandono sobreestiman tanto las colas en saturación.

**II.12.8** El p95 y el p99. Con una media de 50 ms, es perfectamente posible que
el p99 sea de 3 s, y que los usuarios que se quejan sean exactamente esos. En
sistemas con muchos servicios encadenados, además, la probabilidad de que **al
menos uno** de ellos caiga en su cola lenta crece con el número de llamadas: es
el argumento de *The Tail at Scale*.

**II.12.9** ★ El resultado típico es que la espera observada supera la predicha
por M/M/1, y las dos causas habituales son las llegadas por lotes y la tasa no
constante. Trocear por franjas horarias suele reconciliar los números.
