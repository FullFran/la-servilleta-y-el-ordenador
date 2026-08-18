## Soluciones de II.7

**II.7.1** $t=L^2/(2D)$. Célula: $(10^{-5})^2/(2\times10^{-10})=0{,}5$ s.
Tejido: $(10^{-3})^2/(2\times10^{-10})=5000$ s $\approx1{,}4$ h. **Factor
$10^4$ por un factor 100 en distancia**, y por eso hay capilares cada ~50 μm.

**II.7.2** $Pe=10^{-3}\times10^{-5}/2\times10^{-9}=5$. Del mismo orden: en un
capilar **compiten**, que es precisamente el diseño óptimo. Ni desperdicia flujo
ni depende de la difusión a distancias largas.

**II.7.3** Con $D_{O_2}$ en tejido $\approx2\times10^{-9}$ m²/s y consumo
metabólico típico, el criterio de que el centro no quede anóxico da un radio
máximo del orden de **1 mm**. Los insectos superan ese límite con un sistema
traqueal que lleva **aire** (donde $D$ es $10^4$ veces mayor) hasta cerca de
cada célula. Y ese sistema es difusivo, lo que limita el tamaño de los insectos:
en el Carbonífero, con más oxígeno atmosférico, había libélulas de 70 cm.

**II.7.4** Paseo: $\langle x^2\rangle=n\ell^2$ con $n=t/\Delta t$. EDP: la
gaussiana tiene varianza $2Dt$. Identificando, $D=\ell^2/(2\Delta t)$.

**II.7.5** El sesgo aparece en la media y no cambia la varianza. Es la
descomposición de la ecuación de Langevin en arrastre más difusión.

**II.7.6** En estacionario, $D c''=kc$, luego $c=c_0e^{-x/\lambda}$ con
$\lambda=\sqrt{D/k}$. Con $D=10^{-10}$ m²/s y una vida media de 10 min:
$\lambda\approx90$ μm, del orden de diez diámetros celulares. **Esa es la
escala sobre la que un morfógeno puede informar de la posición.**

**II.7.7** En 1D gana claramente diferencias finitas. En 3D, con geometría
complicada o con dominio infinito, gana Monte Carlo, porque su coste no crece
con la dimensión (capítulo 9) y trata contornos irregulares sin mallado.

**II.7.8** El artefacto clásico es el **ruido de localización**: si la posición se
mide con error $\sigma$, el MSD medido es $2Dt+2\sigma^2$, y en escala log-log
eso aplana la curva a tiempos cortos produciendo un $\alpha$ aparente menor que
1. La comprobación: dibujar el MSD **restando** el offset ajustado, o medir a
tiempos largos donde el término constante es despreciable.

**II.7.9** ★ Con agar y colorante alimentario, el frente avanza como $\sqrt t$ y
se puede medir con fotos con marca temporal. Sale $D\sim10^{-9}$–$10^{-10}$
m²/s, coherente con moléculas orgánicas en agua.
