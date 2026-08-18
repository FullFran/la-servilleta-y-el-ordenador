"""Comprueba que los números citados en el libro salen de verdad del código.

Para cada capítulo: ejecuta sus scripts de figura, captura lo que imprimen y
comprueba que cada número escrito dentro de un bloque ```text del capítulo
aparece en esa salida.

La cobertura es parcial y conviene saberlo: sólo mira los bloques ```text, no
los números escritos en la prosa. Pero es exactamente donde se citan salidas de
programa, que es donde el error se cuela sin que se note.

No todo lo que marca es un fallo: hay bloques que son listas de comprobación o
tablas hechas a mano, y hay redondeos legítimos (4,49e15 escrito como 4,5e15).
Lo que produce es una lista de cosas que mirar.

Ejecutar:  python herramientas/verificar_numeros.py
"""

from __future__ import annotations

import pathlib
import re
import subprocess
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
PY = RAIZ / ".venv/bin/python"
FENCE = re.compile(r"```text\n(.*?)```", re.S)
NUM = re.compile(r"\d+[.,]\d+|\d+e[+-]?\d+|\d{2,}")
PARTES = ("parte-1-instrumental", "parte-2-fenomenos", "parte-3-arte-de-resolver")


def normaliza(s: str) -> str:
    """Un número escrito con coma decimal y otro con punto son el mismo número."""
    return s.replace(",", ".").rstrip("0").rstrip(".")


def revisa(cap: pathlib.Path) -> None:
    scripts = sorted((cap / "codigo").glob("fig_*.py"))
    md = cap / "capitulo.md"
    if not scripts or not md.exists():
        return

    salida = []
    for s in scripts:
        try:
            r = subprocess.run([str(PY), s.name], cwd=s.parent,
                               capture_output=True, text=True, timeout=900)
            salida.append(r.stdout)
            if r.returncode != 0:
                print(f"!! {cap.name}/{s.name} falló:\n{r.stderr[-400:]}")
        except subprocess.TimeoutExpired:
            print(f"!! {cap.name}/{s.name} agotó el tiempo")

    blob = normaliza("\n".join(salida))
    citados = {n for b in FENCE.findall(md.read_text(encoding="utf-8"))
               for n in NUM.findall(b)}
    faltan = [n for n in sorted(citados) if normaliza(n) not in blob]

    marca = "OK " if not faltan else "REV"
    print(f"{marca} {cap.name}: {len(citados) - len(faltan)}/{len(citados)}"
          + (f"   revisar: {', '.join(faltan[:12])}" if faltan else ""))
    sys.stdout.flush()


def main() -> None:
    for parte in PARTES:
        for cap in sorted((RAIZ / parte).glob("cap-*")):
            revisa(cap)


if __name__ == "__main__":
    main()
