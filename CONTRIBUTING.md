# Cómo contribuir

Este libro está en revisión. Son 684 páginas y nadie las ha auditado enteras,
así que **encontrar un error es la contribución más valiosa que puedes hacer**.
Las tres primeras erratas de [ERRATA.md](ERRATA.md) las encontró un lector, no
el autor.

## Reportar una errata

Abre una issue con:

* **Dónde**: fichero y línea, o capítulo y sección.
* **Qué dice**: cítalo literal.
* **Por qué está mal**: el argumento, el cálculo o la fuente. No hace falta que
  sea largo; hace falta que sea comprobable.
* **Qué debería decir**, si lo tienes claro. Si no, con señalarlo basta.

No hace falta que estés seguro. Una sospecha bien argumentada vale; una
corrección equivocada se cierra en dos mensajes y no ha pasado nada.

## La regla que no es obvia

> **Corregir un número exige tocar el script, no solo el texto.**

Los números del libro son la salida real de los programas de `codigo/`. Cambiar
un número a mano en el markdown rompe la única garantía que el libro ofrece de
verdad. Si un resultado está mal, el arreglo es en el script; el texto se
actualiza después con lo que el script imprima.

Lo mismo con las figuras: no hay ninguna imagen de origen desconocido, y no
debería haberla.

## Contribuir problemas nuevos

Bienvenidos, sobre todo en las Partes II y III, que van cortas. Mira el
apéndice D para el esquema de numeración y las diez categorías.

Si el problema es ● o ★ **tiene que venir con Pista 1 y Pista 2**, no solo con
la solución. La primera nombra el marco correcto; la segunda quita el obstáculo
que queda; ninguna de las dos contiene la respuesta. Es una regla estricta
porque el libro promete esas pistas en cada capítulo, y hubo un momento en que
lo prometía sin cumplirlo.

## Cambios grandes

Reescribir un capítulo, cambiar la estructura o añadir uno nuevo: háblalo en
una issue antes. No por burocracia, sino porque el libro tiene un diseño
explícito —está en `00-preliminares/`— y conviene ver si el cambio encaja antes
de que escribas tres mil palabras.

## Levantar el entorno

```bash
python3 -m venv .venv && .venv/bin/pip install numpy scipy matplotlib pandas
# pandoc, tectonic y la fuente DejaVu Sans Mono desde tu gestor de paquetes

./construir.sh todo        # reconstruye figuras, capítulos, diapositivas y libro
make verificar             # ¿los números citados salen del código?
make glifos                # ¿se pierde algún carácter al compilar?
```

Las dos comprobaciones tienen que pasar antes de un PR. La segunda existe
porque XeTeX descartaba en silencio 1500 caracteres devolviendo código 0.

## Idioma

El libro es en español. Los identificadores del código, en inglés, como está
ahora. Los comentarios de código siguen la convención del fichero que tocas.

## Licencia de lo que aportes

El texto va con [CC BY-SA 4.0](LICENSE) y el código con [MIT](LICENSE-CODE).
Al contribuir aceptas que tu aportación se publique con la licencia que
corresponda a la parte que toques.
