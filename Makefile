.PHONY: todo figuras capitulos diapos libro html notebooks verificar glifos limpiar
todo:      ; @./construir.sh todo
figuras:   ; @./construir.sh figuras
capitulos: ; @./construir.sh capitulos
diapos:    ; @./construir.sh diapos
libro:     ; @./construir.sh libro
html:      ; @./construir.sh html
notebooks: ; @./construir.sh notebooks
verificar: ; @.venv/bin/python herramientas/verificar_numeros.py
glifos:    ; @.venv/bin/python herramientas/verificar_glifos.py
limpiar:   ; @rm -rf .tmp/* salida/*.pdf && echo limpio
