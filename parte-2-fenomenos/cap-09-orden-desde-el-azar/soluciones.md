## Soluciones de II.9

**II.9.1** Ordenada: $E=-2JL^2$ (cada espín tiene 4 vecinos, cada enlace contado
una vez). Aleatoria: $\langle E\rangle=0$.

**II.9.2** $2^{1024}\approx1{,}8\times10^{308}$. Es aproximadamente el mayor
número representable en doble precisión, y esa coincidencia da idea de la
escala.

**II.9.3** El argumento de Peierls acota la probabilidad de que exista un dominio
invertido de perímetro $\ell$: su coste energético es $2J\ell$ y su entropía es
$\sim\ell\ln3$. En 2D, el coste crece con el perímetro y para $T$ bajo domina
la energía: no hay dominios grandes y el orden sobrevive. **En 1D el «perímetro»
de un dominio son dos puntos**, coste $4J$ independiente del tamaño, mientras
que la entropía crece como $\ln L$: siempre gana la entropía y el orden se
destruye a cualquier $T>0$.

**II.9.4** La magnetización cae suavemente a cero al aumentar $L$ para cualquier
$T>0$.

**II.9.5** El cumulante de Binder $U=1-\langle m^4\rangle/(3\langle m^2\rangle^2)$
es adimensional y sus curvas para distintos $L$ **se cruzan en $T_c$**. Es el
método estándar y da $T_c$ con tres cifras usando tamaños modestos.

**II.9.6** Sale $\approx1{,}75$, coincidente con $7/4$ exacto, si se promedia
suficientemente cerca de $T_c$ y se usan al menos cuatro tamaños.

**II.9.7** El tiempo de autocorrelación de Metropolis crece como $L^{2,17}$ cerca
de $T_c$; el de Wolff, como $L^{0,25}$. Con $L=128$ la diferencia es de un
factor $\sim10^4$ en coste. **El algoritmo importa más que la máquina.**

**II.9.8** (i) **Tamaño finito**: la magnetización media de $|m|$ nunca es cero
en un sistema finito, y hay que usar $\langle|m|\rangle$ con corrección de
escalado o el cumulante de Binder. (ii) **Termalización insuficiente**: la
cadena arrancó ordenada y no ha tenido tiempo de desordenarse, que es la
ralentización crítica en acción.

**II.9.9** ★ El resultado clásico de Schelling: con una preferencia de que al
menos el 30 % de los vecinos sean del propio grupo —una preferencia muy débil,
compatible con querer vivir en minoría— aparece segregación casi total. **Nadie
deseaba ese resultado**, y es el ejemplo canónico de que un fenómeno colectivo
no refleja las preferencias individuales.
