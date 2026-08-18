"""Genera un cuaderno Jupyter por capítulo a partir de sus scripts de figuras.

La idea es que el lector pueda ejecutar y modificar cada figura del libro sin
salir del navegador: cambiar un parámetro, volver a ejecutar y ver qué pasa.
Es el «juega con el modelo» de cada capítulo, hecho operativo.

Ejecutar:  python herramientas/generar_notebooks.py
"""

from __future__ import annotations

import json
import pathlib
import re

RAIZ = pathlib.Path(__file__).resolve().parent.parent
PARTES = ["parte-1-instrumental", "parte-2-fenomenos", "parte-3-arte-de-resolver"]


def celda_md(texto: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": texto.splitlines(True)}


def celda_codigo(texto: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": texto.splitlines(True),
    }


def titulo_capitulo(carpeta: pathlib.Path) -> str:
    md = carpeta / "capitulo.md"
    if md.exists():
        for linea in md.read_text(encoding="utf-8").splitlines():
            if linea.startswith("# "):
                return linea[2:].strip()
    return carpeta.name


def docstring(codigo: str) -> tuple[str, str]:
    """Separa el docstring del script del resto del código."""
    m = re.match(r'\s*"""(.*?)"""\s*\n(.*)', codigo, re.S)
    if not m:
        return "", codigo
    return m.group(1).strip(), m.group(2)


def limpia_preambulo(codigo: str) -> str:
    """Quita el ajuste de sys.path y la llamada a save(), que en un cuaderno
    sobran: allí las figuras se muestran en línea."""
    lineas = []
    for linea in codigo.splitlines():
        if "sys.path.insert" in linea:
            continue
        if linea.startswith("save(fig"):
            lineas.append("plt.show()")
            continue
        lineas.append(linea)
    return "\n".join(lineas)


def construye(carpeta: pathlib.Path) -> pathlib.Path | None:
    scripts = sorted((carpeta / "codigo").glob("fig_*.py"))
    if not scripts:
        return None

    titulo = titulo_capitulo(carpeta)
    celdas = [
        celda_md(
            f"# {titulo}\n\n"
            "**Cuaderno interactivo de *La servilleta y el ordenador*.**\n\n"
            "Cada sección reproduce una figura del capítulo. La gracia no es "
            "ejecutarlas: es **cambiar los parámetros y comprobar si ocurre lo "
            "que esperabas**.\n\n"
            "> Antes de ejecutar cada celda, escribe en una línea qué esperas "
            "ver. Después mira si ocurrió. Y después, por qué.\n"
        ),
        celda_codigo(
            "import sys, pathlib\n"
            f"sys.path.insert(0, str(pathlib.Path.cwd() / '{'/'.join(['..'] * 0)}'))\n"
            "sys.path.insert(0, '../../../herramientas')\n"
            "sys.path.insert(0, str(pathlib.Path.cwd().parents[1] / 'herramientas'))\n"
            "\n"
            "import numpy as np\n"
            "import matplotlib.pyplot as plt\n"
            "from estilo_libro import C, use_style, rng, save\n"
            "\n"
            "use_style()\n"
            "%matplotlib inline"
        ),
    ]

    for script in scripts:
        doc, cuerpo = docstring(script.read_text(encoding="utf-8"))
        pregunta = doc.splitlines()[0] if doc else script.stem
        resto = "\n".join(doc.splitlines()[1:]).strip()
        celdas.append(
            celda_md(
                f"---\n\n## {pregunta}\n\n{resto}\n\n"
                f"*(script original: `codigo/{script.name}`)*\n\n"
                "**Antes de ejecutar, escribe aquí qué esperas ver:**\n\n> \n"
            )
        )
        celdas.append(celda_codigo(limpia_preambulo(cuerpo).strip()))
        celdas.append(
            celda_md(
                "**¿Ocurrió lo que esperabas? ¿Por qué?**\n\n> \n\n"
                "**Juega:** cambia un parámetro de la celda anterior, vuelve a "
                "ejecutarla y anota el efecto.\n\n> \n"
            )
        )

    nb = {
        "cells": celdas,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    destino = carpeta / "notebook.ipynb"
    destino.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
    return destino


def main() -> None:
    n = 0
    for parte in PARTES:
        for carpeta in sorted((RAIZ / parte).glob("cap-*")):
            if construye(carpeta):
                print(f"  -> {carpeta.name}/notebook.ipynb")
                n += 1
    print(f"   {n} cuadernos generados")


if __name__ == "__main__":
    main()
