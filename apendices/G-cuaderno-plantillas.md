# Apéndice G — Plantillas del cuaderno del modelador

> Para imprimir. La explicación de cómo se usan está en
> `00-preliminares/06-cuaderno-del-modelador.md`.

---

## G.1 Entrada de problema

```text
────────────────────────────────────────────────────────────────
Fecha:                                       Problema nº:

PREGUNTA (una frase, cuantitativa, con unidades y precisión):


¿QUÉ CREO QUE OCURRIRÁ? (antes de calcular nada):


ORDEN DE MAGNITUD:   entre 10^___ y 10^___ ,  apuesto por __________

VARIABLES RELEVANTES:                 DESCARTADAS Y POR QUÉ:
 1.                                    1.                    (motivo)
 2.                                    2.
 3.                                    3.

SUPUESTOS:                            VÁLIDO MIENTRAS:
 1.                                    1.
 2.                                    2.
 3.                                    3.

MODELO MÍNIMO:


PREDICCIÓN DEL MODELO (antes de calcular bien):


CÁLCULO / SIMULACIÓN (método, parámetros, semilla):


RESULTADO:

¿TIENE SENTIDO?
 □ dimensiones  □ signo  □ orden de magnitud  □ límites extremos
 □ caso conocido  □ conservación  □ monotonía

¿QUÉ SALIÓ MAL?   Tipo:  □ dato  □ estructura  □ concepto  □ implementación


¿QUÉ CAMBIARÍA?


¿QUÉ HE APRENDIDO? (una frase TRANSFERIBLE a otro problema):


NUEVA PREGUNTA:

────────────────────────────────────────────────────────────────
```

---

## G.2 Hoja de estimación rápida

```text
────────────────────────────────────────────────────────
ESTIMACIÓN                                   Fecha:

Cantidad a estimar:                                  unidades:

DESCOMPOSICIÓN
 factor                valor          incertidumbre (×/÷)
 ______________     __________         __________
 ______________     __________         __________
 ______________     __________         __________
 ______________     __________         __________

PRODUCTO:  __________          σ(log) = √(Σσᵢ²) = __________

RESULTADO:  entre __________ y __________   (intervalo del 90 %)

¿QUÉ FACTOR DOMINA EL ERROR?  __________  (σᵢ² / Σσⱼ²  = ____ %)

COMPARADO CON QUÉ:


── comprobación posterior ──
Valor real:                Factor de error:
¿Estaba dentro de mi intervalo?  □ sí  □ no
¿Por qué falló?
────────────────────────────────────────────────────────
```

---

## G.3 Hoja de experimento computacional

```text
────────────────────────────────────────────────────────
EXPERIMENTO COMPUTACIONAL                    Fecha:

PREGUNTA:

PREDICCIÓN ESCRITA (antes de ejecutar):

¿QUÉ RESULTADO ME HARÍA SOSPECHAR DEL CÓDIGO?

DISEÑO
 parámetros barridos:
 rango:
 muestreo:  □ rejilla  □ aleatorio  □ hipercubo latino  □ Sobol
 nº de ejecuciones:            réplicas por punto:
 semilla base:                 versión del código:

CASO TRIVIAL EJECUTADO PRIMERO:   □ sí, resultado correcto  □ no

CRITERIO DE PARADA:

RESULTADO:

COMPROBACIONES
 □ cambia con la semilla        □ paso a la mitad
 □ otro método                  □ conservaciones
 □ invariancias                 □ tamaño del sistema

¿OCURRIÓ LO PREDICHO?  □ sí  □ no

SI NO: ¿POR QUÉ?

QUÉ HE APRENDIDO:
────────────────────────────────────────────────────────
```

---

## G.4 Hoja de calibración (una vez al mes)

```text
────────────────────────────────────────────────────────
CALIBRACIÓN                              Mes:

Veinte estimaciones con intervalo del 90 %, comprobadas después.

  #   cantidad          mi intervalo          real     ¿dentro?
  1                                                      □
  2                                                      □
 ...
 20                                                      □

ACIERTOS: ___ / 20        (esperado con intervalos honestos: 18)

□ Menos de 14: exceso de confianza. Ensancha por un factor 3.
□ 20 de 20: exceso de prudencia. Tus intervalos no informan.

ERRORES POR TIPO ESTE MES:
 dato ____  estructura ____  concepto ____  implementación ____

¿QUÉ ERROR SE REPITE?

¿QUÉ CAPÍTULO DEBERÍA RELEER?
────────────────────────────────────────────────────────
```
