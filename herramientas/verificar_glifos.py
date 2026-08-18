"""Comprueba que ningún carácter del libro se pierde al compilar.

XeTeX descarta en silencio los caracteres que la fuente no tiene: emite un
aviso, escribe el PDF y devuelve 0. Es la peor clase de fallo de este pipeline,
porque el resultado parece correcto.

Este script recorre todo el markdown, recoge los caracteres no ASCII que usa el
libro, construye un documento de prueba con todos ellos —en texto corrido y
dentro de un bloque literal, que se comportan distinto— y lo compila con el
preámbulo real. Si algo se pierde, lo dice.

Ejecutar:  python herramientas/verificar_glifos.py
"""

from __future__ import annotations

import collections
import pathlib
import re
import subprocess
import sys
import tempfile

RAIZ = pathlib.Path(__file__).resolve().parent.parent


def caracteres_del_libro() -> str:
    cnt: collections.Counter[str] = collections.Counter()
    for f in RAIZ.rglob("*.md"):
        if any(x in f.parts for x in (".tmp", "salida", ".venv", ".git")):
            continue
        for ch in f.read_text(encoding="utf-8"):
            if ord(ch) > 127:
                cnt[ch] += 1
    return "".join(sorted(cnt, key=lambda c: -cnt[c]))


def main() -> int:
    chars = caracteres_del_libro()
    print(f"{len(chars)} caracteres no ASCII distintos en el libro")

    muestra = (
        "En texto corrido:\n\n" + " ".join(chars)
        + "\n\nDentro de un bloque literal:\n\n```text\n" + " ".join(chars) + "\n```\n"
    )
    with tempfile.TemporaryDirectory() as tmp:
        d = pathlib.Path(tmp)
        (d / "muestra.md").write_text(muestra, encoding="utf-8")
        r = subprocess.run(
            ["pandoc", str(d / "muestra.md"),
             f"--metadata-file={RAIZ}/metadatos/capitulo.yaml",
             "-H", f"{RAIZ}/metadatos/estilo/preambulo.tex",
             "--pdf-engine=tectonic", "-o", str(d / "muestra.pdf")],
            capture_output=True, text=True, cwd=d,
        )
        err = r.stderr
        perdidos = sorted(set(re.findall(r'could not represent character "([^"]*)"', err)))
        errores = [l for l in err.splitlines() if l.startswith("error")]

    if errores:
        print("FALLO al compilar la muestra:")
        for l in errores[:5]:
            print("  ", l)
        return 2
    if perdidos:
        print(f"SE PIERDEN {len(perdidos)} caracteres: {' '.join(perdidos)}")
        print("Añade un \\newunicodechar en metadatos/estilo/preambulo.tex,")
        print("o cambia el texto si unicode-math reclama ese punto de código.")
        return 1
    print("Ningún carácter se pierde.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
