#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# construir.sh — compilación del libro
#
#   ./construir.sh figuras     genera todas las figuras (Python -> PDF/PNG)
#   ./construir.sh capitulos   un PDF por capítulo, dentro de su propia carpeta
#   ./construir.sh diapos      un PDF de diapositivas por capítulo, en slides/
#   ./construir.sh libro       el libro completo -> salida/libro-completo.pdf
#   ./construir.sh html        versión HTML navegable -> salida/libro.html
#   ./construir.sh notebooks   un notebook Jupyter por capítulo
#   ./construir.sh todo        todo lo anterior, en orden
# ---------------------------------------------------------------------------
set -uo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$RAIZ"

PY="$RAIZ/.venv/bin/python"
[[ -x "$PY" ]] || PY="python3"

META_CAP="$RAIZ/metadatos/capitulo.yaml"
META_LIBRO="$RAIZ/metadatos/libro.yaml"
META_DIAPOS="$RAIZ/metadatos/diapositivas.yaml"
PREAMBULO="$RAIZ/metadatos/estilo/preambulo.tex"
PRE_BEAMER="$RAIZ/metadatos/estilo/beamer.tex"
FILTRO="$RAIZ/herramientas/cajas.lua"
ORDEN="$RAIZ/metadatos/orden-libro.txt"

verde() { printf '\033[32m%s\033[0m\n' "$*"; }
rojo()  { printf '\033[31m%s\033[0m\n' "$*"; }
gris()  { printf '\033[90m%s\033[0m\n' "$*"; }

FALLOS=0

# --- capítulos (carpetas que contienen capitulo.md) ------------------------
capitulos() { find parte-* interludios -name capitulo.md 2>/dev/null | sort; }

# ---------------------------------------------------------------------------
figuras() {
  verde "== Generando figuras =="
  local n=0
  while IFS= read -r script; do
    local dir; dir="$(dirname "$script")"
    gris "  $script"
    ( cd "$dir" && "$PY" "$(basename "$script")" >/dev/null 2>"$RAIZ/.tmp/fig.err" ) \
      || { rojo "  FALLO: $script"; sed -n '1,12p' "$RAIZ/.tmp/fig.err"; FALLOS=$((FALLOS+1)); }
    n=$((n+1))
  done < <(find parte-* interludios apendices 00-preliminares -name 'fig_*.py' 2>/dev/null | sort)
  verde "   $n scripts ejecutados"
}

# ---------------------------------------------------------------------------
# Une capitulo.md + problemas.md + soluciones.md + referencias.md
unir_capitulo() {
  local dir="$1" salida="$2"
  : > "$salida"
  for f in capitulo.md problemas.md soluciones.md referencias.md; do
    [[ -f "$dir/$f" ]] || continue
    cat "$dir/$f" >> "$salida"
    printf '\n\n' >> "$salida"
  done
}

# Un carácter sin glifo no rompe la compilación: desaparece del PDF sin más.
# Es la peor clase de fallo silencioso, así que se vigila explícitamente.
avisa_glifos() {
  local err="$1" quien="$2"
  local n
  n=$(grep -c 'could not represent character' "$err" 2>/dev/null || true)
  [[ "${n:-0}" -gt 0 ]] && {
    rojo "  AVISO: $quien pierde $n caracteres sin glifo en la fuente"
    grep -o 'could not represent character "[^"]*"' "$err" | sort -u | head -5
  }
  return 0
}

capitulos_pdf() {
  verde "== Compilando capítulos =="
  while IFS= read -r md; do
    local dir; dir="$(dirname "$md")"
    local nombre; nombre="$(basename "$dir")"
    local tmp="$RAIZ/.tmp/${nombre}.md"
    unir_capitulo "$dir" "$tmp"
    gris "  $nombre"
    local abs; abs="$RAIZ/$dir"
    ( cd "$abs" && pandoc "$tmp" \
        --metadata-file="$META_CAP" \
        --resource-path=".:figuras" \
        -H "$PREAMBULO" --lua-filter="$FILTRO" \
        --pdf-engine=tectonic \
        -o "$abs/${nombre}.pdf" ) 2>"$RAIZ/.tmp/cap.err" \
      || { rojo "  FALLO: $nombre"; grep -E '^(error|! )' "$RAIZ/.tmp/cap.err" | head -6; FALLOS=$((FALLOS+1)); }
    avisa_glifos "$RAIZ/.tmp/cap.err" "$nombre"
  done < <(capitulos)
}

# ---------------------------------------------------------------------------
diapos() {
  verde "== Compilando diapositivas =="
  while IFS= read -r md; do
    local dir; dir="$(dirname "$md")"          # .../slides
    local cap; cap="$(basename "$(dirname "$dir")")"
    gris "  $cap"
    ( cd "$dir" && pandoc "$(basename "$md")" -t beamer \
        --metadata-file="$META_DIAPOS" \
        --resource-path=".:../figuras" \
        -H "$PRE_BEAMER" --lua-filter="$FILTRO" \
        --pdf-engine=tectonic \
        -o "${cap}-diapositivas.pdf" ) 2>"$RAIZ/.tmp/dia.err" \
      || { rojo "  FALLO diapos: $cap"; grep -E '^(error|! )' "$RAIZ/.tmp/dia.err" | head -6; FALLOS=$((FALLOS+1)); }
  done < <(find parte-* -path '*/slides/diapositivas.md' 2>/dev/null | sort)
}

# ---------------------------------------------------------------------------
libro() {
  verde "== Compilando el libro completo =="
  local tmp="$RAIZ/.tmp/libro.md"
  : > "$tmp"
  while IFS= read -r linea; do
    [[ -z "$linea" || "$linea" == \#* ]] && continue
    if [[ -d "$linea" ]]; then
      unir_capitulo "$linea" "$RAIZ/.tmp/_x.md"
      # rutas de figuras relativas a la raíz
      sed "s|](figuras/|](${linea}/figuras/|g" "$RAIZ/.tmp/_x.md" >> "$tmp"
    elif [[ -f "$linea" ]]; then
      local d; d="$(dirname "$linea")"
      sed "s|](figuras/|](${d}/figuras/|g" "$linea" >> "$tmp"
    else
      rojo "  no existe: $linea"; continue
    fi
    printf '\n\n' >> "$tmp"
  done < "$ORDEN"
  gris "  $(wc -w < "$tmp") palabras"
  pandoc "$tmp" \
    --metadata-file="$META_LIBRO" \
    --resource-path="$RAIZ" \
    -H "$PREAMBULO" --lua-filter="$FILTRO" \
    --pdf-engine=tectonic \
    -o "$RAIZ/salida/libro-completo.pdf" 2>"$RAIZ/.tmp/libro.err" \
    || { rojo "  FALLO libro"; grep -E '^(error|! )' "$RAIZ/.tmp/libro.err" | head -10; FALLOS=$((FALLOS+1)); }
  [[ -f "$RAIZ/salida/libro-completo.pdf" ]] && verde "   salida/libro-completo.pdf"
}

html() {
  verde "== Versión HTML =="
  # El navegador no muestra un PDF dentro de <img>: pandoc lo convertiría en un
  # <embed> con un visor por figura. Cada figura tiene su PNG al lado.
  sed 's|\(figuras/fig_[a-z0-9_]*\)\.pdf)|\1.png)|g' \
      "$RAIZ/.tmp/libro.md" > "$RAIZ/.tmp/libro-web.md"
  pandoc "$RAIZ/.tmp/libro-web.md" \
    --metadata-file="$META_LIBRO" --metadata title="La servilleta y el ordenador" \
    --resource-path="$RAIZ" \
    --lua-filter="$FILTRO" --standalone --toc --toc-depth=2 --mathml \
    --css="estilo-web.css" --embed-resources \
    -o "$RAIZ/salida/libro.html" 2>/dev/null \
    && verde "   salida/libro.html"
}

notebooks() {
  verde "== Notebooks =="
  "$PY" "$RAIZ/herramientas/generar_notebooks.py"
}

case "${1:-todo}" in
  figuras)   figuras ;;
  capitulos) capitulos_pdf ;;
  diapos)    diapos ;;
  libro)     libro ;;
  html)      libro >/dev/null; html ;;
  notebooks) notebooks ;;
  todo)      figuras; capitulos_pdf; diapos; libro; notebooks ;;
  *) echo "uso: $0 {figuras|capitulos|diapos|libro|html|notebooks|todo}"; exit 1 ;;
esac

if [[ $FALLOS -gt 0 ]]; then rojo "== $FALLOS fallos =="; exit 1; fi
verde "== OK =="
