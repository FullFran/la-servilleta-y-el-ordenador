# El cuaderno del modelador

Todo el que resuelve problemas bien lleva un cuaderno. No para acordarse de las
fórmulas —para eso está internet— sino para acordarse de **cómo pensó** y, sobre
todo, de **dónde se equivocó**.

El cuaderno tiene una función que el libro no puede cumplir: registra tus fallos
concretos. Al cabo de dos meses descubrirás que fallas siempre por las mismas
tres razones. Ese descubrimiento vale más que media Parte I.

## La plantilla

Una entrada por problema. Se rellena **en orden**, y las tres primeras casillas
se escriben antes de calcular nada.

```text
────────────────────────────────────────────────────────────
Fecha:

Pregunta:
    (una sola frase, cuantitativa, con unidades)

¿Qué creo que ocurrirá?
    (predicción cualitativa, antes de cualquier cuenta)

Orden de magnitud:
    (un número y un intervalo: entre 10^a y 10^b)

Variables relevantes:
    (y las que descarto, con el motivo)

Supuestos:
    1.                     válido mientras…
    2.                     válido mientras…
    3.                     válido mientras…

Modelo mínimo:
    (ecuaciones o reglas; lo más simple que podría funcionar)

Predicción del modelo:
    (qué número o qué comportamiento sale, antes de calcularlo bien)

Cálculo / simulación:
    (qué he hecho, con qué método, con qué parámetros, con qué semilla)

Resultado:

¿Tiene sentido?
    · dimensiones ·  límites extremos ·  orden de magnitud ·  signo ·
    · caso conocido ·  conservación

¿Qué salió mal?
    (y de qué tipo fue el error: dato, estructura, concepto, implementación)

¿Qué cambiaría?

¿Qué he aprendido?
    (una frase transferible a otro problema, no una conclusión sobre este)

Nueva pregunta:
────────────────────────────────────────────────────────────
```

## Cómo se usa de verdad

**Las tres primeras casillas son sagradas.** Si las rellenas después de calcular,
el cuaderno se convierte en un informe y pierde toda su utilidad. Estarás
registrando lo que resultó, no lo que pensabas, y lo interesante es la
diferencia.

**«¿Qué he aprendido?» debe ser transferible.** «El café se enfría con τ ≈ 20
minutos» no vale: es un dato. «Cuando el sistema tiene un solo tiempo
característico, la condición inicial se olvida en pocos τ y los detalles del
arranque dejan de importar» sí vale: eso lo usarás en otro problema.

**Clasifica tus errores.** Cuatro tipos, y conviene marcar cuál fue:

| Tipo | Ejemplo | Cómo se cura |
|---|---|---|
| **Dato** | usé 300 K donde eran 300 °C | comprobar unidades y órdenes al empezar |
| **Estructura** | olvidé un término que dominaba | análisis de escalas antes de resolver |
| **Concepto** | confundí correlación con causa | volver a la sección correspondiente |
| **Implementación** | índice mal, paso demasiado grande | pruebas de convergencia y casos límite |

Al cabo de veinte entradas, cuenta cuántas de cada tipo. La distribución te dirá
en qué parte del libro deberías estar trabajando.

## Revisión semanal

Diez minutos, el último día de la semana:

1. Lee las entradas de la semana.
2. ¿Qué error se repite?
3. ¿Qué pregunta abierta merece convertirse en el problema libre del día 6?
4. ¿Qué has aprendido que puedas escribir en una sola frase transferible?

## Ejemplo de entrada real

Se incluye completa, con sus fallos, porque una plantilla vacía no enseña nada.

```text
────────────────────────────────────────────────────────────
Fecha: 12 de marzo

Pregunta:
    ¿Cuánta potencia disipa mi portátil, en vatios, cuando compila?

¿Qué creo que ocurrirá?
    Que estará entre el consumo de una bombilla LED y el de una bombilla
    incandescente vieja. Y que casi toda la energía eléctrica acaba en calor.

Orden de magnitud:
    Entre 20 y 100 W. Apuesto por 45 W.

Variables relevantes:
    Consumo eléctrico, fracción convertida en calor (~1), área de disipación,
    salto térmico con el ambiente, caudal del ventilador.
    Descarto: la energía que sale como luz de la pantalla (es <1 W) y el trabajo
    útil (no hay: todo acaba en calor).

Supuestos:
    1. Todo el consumo acaba en calor       válido salvo carga de batería
    2. Régimen estacionario                 válido tras 2-3 minutos compilando
    3. El aire de salida se mezcla enseguida  válido en una habitación normal

Modelo mínimo:
    P = ṁ · c_p · ΔT, con ṁ = ρ · A · v el caudal másico del ventilador.

Predicción del modelo:
    Con A ≈ 4 cm², v ≈ 2 m/s, ρ ≈ 1,2 kg/m³, c_p ≈ 1000 J/(kg·K), ΔT ≈ 15 K:
    ṁ ≈ 1,2 · 4e-4 · 2 ≈ 1e-3 kg/s  →  P ≈ 1e-3 · 1000 · 15 ≈ 15 W.

Cálculo / simulación:
    A mano. Después medí con un enchufe medidor: 52 W en compilación sostenida.

Resultado:
    Modelo: 15 W. Medido: 52 W. Factor 3,5 de error.

¿Tiene sentido?
    Dimensiones bien. Signo bien. Orden de magnitud razonable pero bajo.
    Límite extremo: si el ventilador para, ΔT sube; coherente.

¿Qué salió mal?
    Error de ESTRUCTURA: supuse que toda la potencia sale por el ventilador.
    No es cierto: una fracción grande sale por conducción a través del chasis
    de aluminio, que está caliente al tacto. El modelo mínimo tenía sólo un
    camino de disipación y el sistema real tiene dos en paralelo.
    Además, subestimé v: los ventiladores a tope pasan de 2 m/s.

¿Qué cambiaría?
    Dos caminos en paralelo: P = P_ventilador + h·A_chasis·ΔT.
    Y medir v con un anemómetro de móvil en lugar de suponerla.

¿Qué he aprendido?
    Cuando un sistema tiene varios caminos en paralelo para el mismo flujo,
    modelar sólo el más visible subestima sistemáticamente. Los flujos en
    paralelo se suman; los que están en serie los domina el más lento.

Nueva pregunta:
    ¿Cuánto sube la temperatura de una habitación cerrada de 12 m² por tener
    dos personas y un portátil dentro durante tres horas?
────────────────────────────────────────────────────────────
```

Fíjate en lo que hace útil esta entrada: la estimación previa existía, el error
está clasificado, y la lección final —flujos en paralelo frente a flujos en
serie— sirve para problemas que no tienen nada que ver con un portátil. Eso es
lo que se busca.

::: esencial
* El cuaderno registra cómo pensaste, no qué resultó.
* Las tres primeras casillas se escriben antes de calcular. Siempre.
* Clasifica cada error: dato, estructura, concepto o implementación.
* La lección debe ser transferible o no es una lección.
* Diez minutos de revisión semanal valen más que dos horas de lectura.
:::
