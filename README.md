# La servilleta y el ordenador

**Un entrenamiento en estimación, modelado y experimentación computacional.**

> **Trabajo en curso — v0.1.** El libro está completo y compila, pero **no está
> auditado entero**: son 684 páginas y la revisión ha sido parcial. Sirve como
> material de entrenamiento y como referencia de trabajo; todavía no para
> citarlo como fuente autoritativa. Las erratas encontradas están en
> [ERRATA.md](ERRATA.md) y lo que falta por revisar, en las issues.
>
> Se escribió con ayuda de IA. Decirlo no es un descargo: es coherente con el
> capítulo III.13, que va exactamente de eso. Lo que sí está verificado a mano
> se detalla más abajo, y lo que no, también.
>
> **Encontrar un error es la contribución más valiosa.** Las tres primeras
> erratas las encontró un lector. Ver [CONTRIBUTING.md](CONTRIBUTING.md).

Un libro para alguien con formación en física que quiere recuperar y
sistematizar su capacidad de enfrentarse a un fenómeno nuevo: entender qué
importa, construir un modelo útil, aproximarlo, simularlo, cuantificar su
incertidumbre e interpretar el resultado.

No enseña más fórmulas. Entrena un ciclo:

```text
fenómeno → pregunta → orden de magnitud → variables → supuestos → modelo mínimo
   → ecuaciones → escalas → solución aproximada → simulación → validación
   → incertidumbre → interpretación → límites → nueva pregunta
```

---

## Qué hay aquí

| | |
|---|---|
| **43 capítulos** | 16 de herramientas, 14 de fenómenos, 13 de metodología |
| **8 interludios** históricos | narrativos, documentados, sin ejercicios |
| **7 apéndices** | caja de herramientas, recetario Python, números, plantillas |
| **~163 000 palabras** | 612 páginas en el PDF completo |
| **76 figuras** | todas generadas por código versionado |
| **43 juegos de diapositivas** | un PDF por capítulo, en su propia carpeta |
| **30 cuadernos Jupyter** | uno por capítulo con figuras, para jugar |
| **101 referencias BibTeX** | con nivel de verificación y cautelas editoriales |
| **453 problemas** (Parte I) | en 10 categorías, de calentamiento a extensión |
| **127 con pistas graduadas** | Pista 1 → Pista 2 → Solución, en todo ● y ★ con solución cerrada |

---

## Estructura

```text
00-preliminares/        cómo usar el libro, arquitectura, guía de estilo,
                        plan de entrenamiento, cuaderno del modelador
parte-1-instrumental/   16 capítulos: las herramientas
parte-2-fenomenos/      14 capítulos: los fenómenos
parte-3-arte-de-resolver/ 13 capítulos: el manual de campo
interludios/            8 episodios históricos
apendices/              A–G
bibliografia/           bibliografía comentada + refs.bib
                        primarias/, secundarias/, papers-historicos/
                        (con su README: qué va en cada una y cómo nombrarlo)
herramientas/           estilo de figuras, filtro pandoc, generador de notebooks,
                        verificador de números citados
metadatos/              configuración de compilación y orden del libro
salida/                 libro-completo.pdf, libro.html
```

Cada capítulo es una carpeta autocontenida:

```text
cap-07-sistemas-dinamicos/
├── capitulo.md                       texto principal
├── problemas.md                      enunciados por categoría
├── soluciones.md                     razonadas, con pistas graduadas
├── referencias.md                    históricas / técnicas / opcionales
├── codigo/fig_*.py                   un script por figura, ejecutable
├── figuras/                          PDF + PNG generados
├── slides/diapositivas.md            guion de la charla
├── slides/cap-07-…-diapositivas.pdf  las diapositivas compiladas
├── notebook.ipynb                    cuaderno interactivo
└── cap-07-sistemas-dinamicos.pdf     el capítulo compilado
```

---

## Compilar

Requisitos: `pandoc`, `tectonic`, Python 3.11+ con NumPy, SciPy y Matplotlib,
y la fuente **DejaVu Sans Mono** (para los diagramas ASCII y las casillas de las
listas de comprobación; sin ella el libro compila igual, pero esos caracteres
desaparecen y `construir.sh` lo avisa).

```bash
python3 -m venv .venv && .venv/bin/pip install numpy scipy matplotlib pandas
brew install pandoc tectonic          # o el gestor de paquetes que uses

./construir.sh figuras     # regenera las 76 figuras desde su código
./construir.sh capitulos   # un PDF por capítulo, en su propia carpeta
./construir.sh diapos      # un PDF de diapositivas por capítulo
./construir.sh libro       # salida/libro-completo.pdf
./construir.sh html        # salida/libro.html
./construir.sh notebooks   # un notebook por capítulo
./construir.sh todo        # todo lo anterior

python herramientas/verificar_numeros.py   # ¿los números citados salen del código?
python herramientas/verificar_glifos.py    # ¿se pierde algún carácter al compilar?
```

También hay `Makefile` con los mismos objetivos.

---

## Decisiones de diseño

**Toda figura tiene su código.** No hay ninguna imagen de origen desconocido.
Cada una se regenera con una orden, con semilla fija. Es coherente con lo que
el libro predica sobre reproducibilidad (capítulo 16).

**Toda afirmación histórica lleva nivel de verificación.**

* **A** — fuente primaria.
* **B** — secundaria documentada, con el matiz declarado.
* **C** — folclore, presentado explícitamente como folclore.

Ejemplos de nivel C que aparecen: el problema de los afinadores de pianos
atribuido a Fermi (sin fuente primaria), la anécdota de Erdős y Monty Hall, la
frase del elefante atribuida a von Neumann. Se cuentan porque son útiles, y en
cada caso se dice que la atribución es dudosa. **Esa distinción es una de las
lecciones del libro.**

**Los números salen de cálculos, no de memoria.** Los resultados citados en el
texto —el exponente de Lyapunov de Lorenz (0,905 medido frente a 0,906
aceptado), la energía de Trinity a partir de los datos de Taylor (15,5 kt), el
exponente de Kleiber (0,747 ± 0,003), la recurrencia de FPU (93,7 %), la
magnetización del Ising a $T=1{,}4$ (0,991 medido frente a 0,991 de Onsager)—
son la salida real de los scripts del repositorio.

`herramientas/verificar_numeros.py` lo comprueba automáticamente: ejecuta cada
script, captura lo que imprime y contrasta los números citados en los bloques
de salida del capítulo. Encontró dos citas inventadas en la primera pasada.

**Cada capítulo declara sus deudas.** Qué herramientas usa de capítulos
anteriores y qué promesa deja abierta para capítulos posteriores.

**Cuota de disciplinas.** Cada capítulo de la Parte I usa ejemplos de al menos
tres campos, y al menos uno no es de física.

**La compilación avisa de lo que pierde.** XeTeX descarta en silencio los
caracteres que la fuente no tiene: el PDF sale bien, el código de salida es 0 y
el contenido ha desaparecido. Pasó de verdad con los marcadores de dificultad
(○ ◐ ● ★), con el nivel bibliográfico (◆), con las casillas □ de las listas de
comprobación y con los caracteres de dibujo de cajas de todos los diagramas
ASCII: más de 1800 líneas los usaban y ninguno llegaba al PDF.
`construir.sh` cuenta ahora esos avisos y los muestra en rojo, y
`herramientas/verificar_glifos.py` compila una muestra con los 91 caracteres
no ASCII que usa el libro —en texto y dentro de bloques literales, que se
comportan distinto— y falla si alguno desaparece.

---

## Documentos de diseño

El proceso de diseño está en el repositorio, porque un libro que enseña a
construir modelos debería enseñar también su propio modelo:

* `00-preliminares/01-arquitectura.md` — tesis, objetivos, estructura completa,
  personajes, historias candidatas con su nivel de verificación, riesgos.
* `00-preliminares/02-auditoria-del-temario.md` — qué faltaba y cómo se
  corrigió: 13 huecos críticos, 22 serios, 11 menores.
* `00-preliminares/03-guia-de-estilo.md` — reglas concretas y verificables de
  voz, densidad matemática, uso de la historia, código y figuras.
* `00-preliminares/04-plantilla-de-capitulo.md` — el esqueleto reutilizable.
* `bibliografia/bibliografia-comentada.md` — cada fuente con qué aporta, qué
  capítulos apoya, nivel, fiabilidad y cautelas. Va incluida al final del libro.

---

## Estado

**v0.1.** Todo el texto está escrito, todas las figuras generadas y todos los
PDF compilan. Lo que eso significa y lo que no:

**Verificado**

* Cada figura la genera un script versionado; ninguna imagen tiene origen
  desconocido.
* Los números citados en los bloques de salida se contrastan automáticamente
  contra lo que imprimen los scripts (`make verificar`).
* Ningún carácter se pierde al compilar (`make glifos`), tras un fallo que
  borraba 1500 símbolos en silencio.
* Las tres erratas de [ERRATA.md](ERRATA.md), verificadas y corregidas.

**No verificado todavía**

* Las derivaciones y los órdenes de magnitud, capítulo a capítulo.
* Que cada una de las 101 referencias exista y diga lo que se le atribuye.
* Los números citados en la prosa, fuera de los bloques de salida.

Las tres auditorías pendientes están abiertas como issues. Que estén a la vista
es información útil para el lector: dice exactamente cuánto fiarse de qué.

Lo que queda está en las **issues** del repositorio, con el contexto suficiente
para retomarlo dentro de unos meses: referencias cruzadas, problemas de las
Partes II y III, pistas graduadas fuera de la Parte I, revisión histórica fuente
por fuente, datos medidos de verdad y la licencia.

Los PDF y la edición web no se versionan —salen de `./construir.sh todo`—; van
adjuntos a cada release.

---

## Licencia

El repositorio mezcla dos cosas con necesidades distintas, así que lleva dos
licencias:

| Qué | Licencia | Qué puedes hacer |
|---|---|---|
| **El texto del libro** — capítulos, problemas, soluciones, figuras, bibliografía | [CC BY-SA 4.0](LICENSE) | Copiarlo, repartirlo en clase, traducirlo, adaptarlo y hasta venderlo, **citando la fuente** y publicando lo que derives con esta misma licencia |
| **El código** — scripts de figura, herramientas, cadena de compilación | [MIT](LICENSE-CODE) | Lo que quieras, incluido uso comercial, conservando el aviso de copyright |

### Por qué esta combinación

**Para que se pueda usar en clase sin dudas.** Un profesor —de instituto, de
universidad pública o privada, de una academia— puede repartir un capítulo,
proyectarlo o adaptarlo sin preguntar nada a nadie. Una licencia «no comercial»
habría dejado ese caso en el aire, y ese caso es justo el que importa.

**Para que nadie pueda apropiárselo.** La cláusula de atribución obliga a
decir de dónde sale, y la de *share-alike* obliga a que cualquier versión
derivada salga también libre. Se puede vender una copia, sí; lo que no se puede
es encerrarla, firmarla como propia ni impedir que otro la reparta gratis. Ese
es el mecanismo que de verdad protege un libro abierto, no la prohibición de
cobrar.

**El código va en MIT** porque las licencias Creative Commons no están
pensadas para software —lo dice la propia Creative Commons— y porque los
scripts que dibujan una figura de matplotlib son más útiles sueltos que atados.

### Cómo citarlo

> BlakIA, F. (2026). *La servilleta y el ordenador: un entrenamiento en
> estimación, modelado y experimentación computacional* (v0.1).
> https://github.com/FullFran/la-servilleta-y-el-ordenador

Hay un `CITATION.cff` en la raíz por si tu gestor bibliográfico lo lee solo.
