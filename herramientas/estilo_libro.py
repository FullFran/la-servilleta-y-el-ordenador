"""Shared visual identity for every figure in the book.

Import this module from any figure script:

    import sys, pathlib
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "herramientas"))
    from estilo_libro import C, use_style, save

Design rules enforced here (see 00-preliminares/guia-de-estilo.md):
  * One figure answers one question.
  * No decorative chartjunk: no gridlines heavier than the data, no 3D, no shadows.
  * Colour is semantic and colour-blind safe (Okabe-Ito derived).
  * Every figure is saved as vector PDF for the book and PNG for the web/notebooks.
"""

from __future__ import annotations

import pathlib
from dataclasses import dataclass

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


# --------------------------------------------------------------------------
# Palette
# --------------------------------------------------------------------------
@dataclass(frozen=True)
class Palette:
    ink: str = "#1b2a41"      # axes, text, "the truth"
    blue: str = "#2f6fa8"     # primary series / model
    red: str = "#c1443c"      # secondary series / data / warning
    green: str = "#3f8f6b"    # third series / agreement
    ochre: str = "#d99a2b"    # fourth series / highlight
    purple: str = "#7d5ba6"   # fifth series
    teal: str = "#3a8fa0"     # sixth series
    grey: str = "#8a94a6"     # context, reference lines, "everything else"
    light: str = "#e8ecf2"    # fills, bands
    paper: str = "#fbfaf7"    # figure background (warm paper)

    @property
    def cycle(self) -> list[str]:
        return [self.blue, self.red, self.green, self.ochre, self.purple, self.teal]


C = Palette()

# Semantic aliases: use these instead of raw colours so meaning stays consistent.
COLOR_DATOS = C.red
COLOR_MODELO = C.blue
COLOR_EXACTO = C.ink
COLOR_APROX = C.ochre
COLOR_RUIDO = C.grey
COLOR_TEORIA = C.green


def use_style(figsize: tuple[float, float] = (6.4, 4.0)) -> None:
    """Apply the book's matplotlib style. Call once at the top of a script."""
    mpl.rcParams.update(
        {
            "figure.figsize": figsize,
            "figure.dpi": 120,
            "savefig.dpi": 200,
            "figure.facecolor": C.paper,
            "savefig.facecolor": C.paper,
            "axes.facecolor": C.paper,
            "axes.edgecolor": C.ink,
            "axes.labelcolor": C.ink,
            "axes.linewidth": 0.9,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.titlesize": 11,
            "axes.titleweight": "bold",
            "axes.titlelocation": "left",
            "axes.titlepad": 10,
            "axes.labelsize": 10,
            "axes.prop_cycle": mpl.cycler(color=C.cycle),
            "axes.grid": True,
            "grid.color": C.grey,
            "grid.alpha": 0.22,
            "grid.linewidth": 0.6,
            "xtick.color": C.ink,
            "ytick.color": C.ink,
            "xtick.labelsize": 9,
            "ytick.labelsize": 9,
            "xtick.direction": "out",
            "ytick.direction": "out",
            "legend.frameon": False,
            "legend.fontsize": 9,
            "lines.linewidth": 1.8,
            "lines.markersize": 5,
            "font.size": 10,
            "font.family": "sans-serif",
            "font.sans-serif": ["DejaVu Sans"],
            "mathtext.fontset": "dejavusans",
            "text.color": C.ink,
        }
    )


def save(fig, nombre: str, carpeta: str | pathlib.Path | None = None) -> pathlib.Path:
    """Save `fig` as PDF (for LaTeX) and PNG (for notebooks/HTML) in ../figuras/."""
    if carpeta is None:
        carpeta = pathlib.Path.cwd().parent / "figuras"
    carpeta = pathlib.Path(carpeta)
    carpeta.mkdir(parents=True, exist_ok=True)
    # tight_layout falla con ejes de aspecto fijo o sin marco; no es motivo
    # para perder la figura.
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            fig.tight_layout()
        except Exception:
            pass
    pdf = carpeta / f"{nombre}.pdf"
    fig.savefig(pdf, bbox_inches="tight")
    fig.savefig(carpeta / f"{nombre}.png", bbox_inches="tight")
    plt.close(fig)
    print(f"  -> {pdf.relative_to(pdf.parents[2]) if len(pdf.parents) > 2 else pdf}")
    return pdf


# --------------------------------------------------------------------------
# Annotation helpers: a figure should carry its own explanation
# --------------------------------------------------------------------------
def anota(ax, texto: str, xy, xytext, color: str | None = None, **kw):
    """Arrow annotation with the book's look."""
    color = color or C.ink
    ax.annotate(
        texto,
        xy=xy,
        xytext=xytext,
        color=color,
        fontsize=9,
        arrowprops=dict(arrowstyle="->", color=color, lw=1.0,
                        connectionstyle="arc3,rad=0.18"),
        **kw,
    )
    return ax


def nota(ax, texto: str, xy, color: str | None = None, **kw):
    """Plain text note in axes-fraction coordinates."""
    ax.text(*xy, texto, transform=ax.transAxes, fontsize=9,
            color=color or C.ink, va="top", **kw)
    return ax


def linea_referencia(ax, y: float, etiqueta: str = "", **kw):
    """Horizontal reference line ('the answer we expected')."""
    ax.axhline(y, color=C.grey, ls="--", lw=1.0, zorder=0, **kw)
    if etiqueta:
        ax.text(0.99, y, f" {etiqueta}", transform=ax.get_yaxis_transform(),
                ha="right", va="bottom", fontsize=8, color=C.grey)
    return ax


# --------------------------------------------------------------------------
# Diagram primitives: conceptual diagrams without external dependencies
# --------------------------------------------------------------------------
def lienzo(ancho: float = 8.0, alto: float = 4.5, xlim=(0, 10), ylim=(0, 6)):
    """Blank canvas for a conceptual diagram (no axes)."""
    fig, ax = plt.subplots(figsize=(ancho, alto))
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")
    ax.set_aspect("equal", adjustable="box")
    return fig, ax


def caja(ax, x, y, ancho, alto, texto, color=None, relleno=None,
         fontsize=9, redondeo=0.12, lw=1.4, zorder=3, **kw):
    """Rounded box with centred text. (x, y) is the centre."""
    from matplotlib.patches import FancyBboxPatch

    color = color or C.ink
    relleno = relleno if relleno is not None else "white"
    p = FancyBboxPatch(
        (x - ancho / 2, y - alto / 2), ancho, alto,
        boxstyle=f"round,pad=0.02,rounding_size={redondeo}",
        linewidth=lw, edgecolor=color, facecolor=relleno, zorder=zorder, **kw,
    )
    ax.add_patch(p)
    ax.text(x, y, texto, ha="center", va="center", fontsize=fontsize,
            color=C.ink, zorder=zorder + 1, linespacing=1.35)
    return p


def flecha(ax, p0, p1, color=None, texto: str = "", lw=1.4, rad=0.0,
           estilo="-|>", fontsize=8, desplaza=(0, 0.18), ls="-"):
    """Arrow between two points, with an optional label at the midpoint."""
    color = color or C.grey
    ax.annotate(
        "", xy=p1, xytext=p0,
        arrowprops=dict(arrowstyle=estilo, color=color, lw=lw, linestyle=ls,
                        connectionstyle=f"arc3,rad={rad}",
                        shrinkA=6, shrinkB=6),
    )
    if texto:
        mx, my = (p0[0] + p1[0]) / 2 + desplaza[0], (p0[1] + p1[1]) / 2 + desplaza[1]
        ax.text(mx, my, texto, ha="center", va="center", fontsize=fontsize, color=color)
    return ax


def banda(ax, x, y_lo, y_hi, color=None, alpha=0.18, **kw):
    """Uncertainty band."""
    color = color or C.blue
    return ax.fill_between(x, y_lo, y_hi, color=color, alpha=alpha, lw=0, **kw)


def escala_log_decadas(ax, lo: float, hi: float, eje: str = "x"):
    """Tidy decade ticks for order-of-magnitude plots."""
    decadas = np.arange(np.floor(np.log10(lo)), np.ceil(np.log10(hi)) + 1)
    ticks = 10.0**decadas
    etiquetas = [rf"$10^{{{int(d)}}}$" for d in decadas]
    if eje == "x":
        ax.set_xscale("log"), ax.set_xlim(lo, hi)
        ax.set_xticks(ticks), ax.set_xticklabels(etiquetas)
    else:
        ax.set_yscale("log"), ax.set_ylim(lo, hi)
        ax.set_yticks(ticks), ax.set_yticklabels(etiquetas)
    return ax


def rng(semilla: int = 42) -> np.random.Generator:
    """Every stochastic figure in the book is reproducible."""
    return np.random.default_rng(semilla)
