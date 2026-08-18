--[[
  cajas.lua — pandoc filter that turns fenced divs into the book's pedagogical
  boxes.

  In markdown you write:

      ::: pregunta
      ¿Cuánta energía hay en una tormenta?
      :::

  and you get a styled box in LaTeX/PDF, and a semantic <div> in HTML.
  The class names are the 14 recurring sections of the chapter template.
--]]

local entornos = {
  pregunta    = "cajapregunta",
  antes       = "cajaantes",
  herramientas= "cajaherramientas",
  historia    = "cajahistoria",
  explica     = "cajaexplica",
  esencial    = "cajaesencial",
  abierto     = "cajaabierto",
  experimento = "cajaexperimento",
  aviso       = "cajaaviso",
  supuestos   = "cajasupuestos",
  falla       = "cajafalla",
  ia          = "cajaia",
  juega       = "cajajuega",
  numeros     = "cajanumero",
}

-- Títulos usados en la versión HTML (el LaTeX los lleva en el preámbulo).
local titulos = {
  pregunta    = "UNA PREGUNTA",
  antes       = "ANTES DE CALCULAR",
  herramientas= "CAJA DE HERRAMIENTAS MATEMÁTICA",
  historia    = "HISTORIA",
  explica     = "EXPLÍCALO SIN ESCONDERTE DETRÁS DE LAS ECUACIONES",
  esencial    = "LO ESENCIAL",
  abierto     = "PREGUNTAS QUE QUEDAN ABIERTAS",
  experimento = "EXPERIMENTO COMPUTACIONAL",
  aviso       = "TRAMPA",
  supuestos   = "¿QUÉ ESTAMOS SUPONIENDO?",
  falla       = "¿CUÁNDO FALLA?",
  ia          = "PROTOCOLO CON IA",
  juega       = "JUEGA CON EL MODELO",
  numeros     = "NÚMEROS QUE CONVIENE SABERSE",
}

function Div(el)
  for _, clase in ipairs(el.classes) do
    local env = entornos[clase]
    if env then
      if FORMAT:match("latex") or FORMAT:match("beamer") then
        local abre = pandoc.RawBlock("latex", "\\begin{" .. env .. "}")
        local cierra = pandoc.RawBlock("latex", "\\end{" .. env .. "}")
        local bloques = {abre}
        for _, b in ipairs(el.content) do table.insert(bloques, b) end
        table.insert(bloques, cierra)
        return bloques
      elseif FORMAT:match("html") then
        local cabecera = pandoc.Div(
          {pandoc.Plain({pandoc.Str(titulos[clase])})},
          pandoc.Attr("", {"caja-titulo"})
        )
        local contenido = {cabecera}
        for _, b in ipairs(el.content) do table.insert(contenido, b) end
        return pandoc.Div(contenido, pandoc.Attr("", {"caja", "caja-" .. clase}))
      end
    end
  end
  return el
end

--[[
  Saneado de matemáticas.

  `\%` dentro de modo matemático rompe la compilación con microtype
  («Incompatible glue units»), sobre todo precedido de un espacio fino.
  Envolverlo en \mathrm{} lo arregla y no cambia el aspecto. Se hace aquí, en
  el filtro, para que ningún capítulo futuro pueda reintroducir el fallo.
--]]
function Math(el)
  el.text = el.text:gsub("\\%%", "\\mathrm{\\%%}")
  return el
end
