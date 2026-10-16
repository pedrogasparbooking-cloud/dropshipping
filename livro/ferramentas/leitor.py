#!/usr/bin/env python3
"""Gera a página de leitura do livro (edicao/leitor.html) a partir dos capítulos.

Cada capítulo é convertido com o pandoc e embutido na página, que mostra um de
cada vez, com índice, navegação e o roteiro (com aviso de spoilers).

Uso:  python3 livro/ferramentas/leitor.py
"""
import html
import json
import pathlib
import re
import subprocess

LIVRO = pathlib.Path(__file__).resolve().parent.parent
FERR = LIVRO / "ferramentas"
CAP = LIVRO / "capitulos"
SAIDA = LIVRO / "edicao"


def md_para_html(texto):
    r = subprocess.run(["pandoc", "-f", "markdown", "-t", "html5", "--no-highlight"],
                       input=texto, capture_output=True, text=True, check=True)
    corpo = r.stdout
    # Realça os marcadores da interface do Claude Code dentro dos blocos de terminal.
    def terminal(m):
        bloco = m.group(0)
        bloco = re.sub(r"(●|✻)", r'<span class="t-dot">\1</span>', bloco)
        bloco = re.sub(r"(⎿)", r'<span class="t-dim">\1</span>', bloco)
        bloco = re.sub(r"^(&gt;.*)$", r'<span class="t-user">\1</span>', bloco, flags=re.M)
        bloco = re.sub(r"(usage limit reached[^\n<]*|Context left until auto-compact: \d+%|Compacting conversation…)",
                       r'<span class="t-warn">\1</span>', bloco)
        return bloco
    corpo = re.sub(r"<pre><code>.*?</code></pre>", terminal, corpo, flags=re.S)
    return corpo


def main():
    roteiro = json.loads((LIVRO / "bastidores" / "roteiro.json").read_text(encoding="utf-8"))
    caps = sorted(roteiro["capitulos"], key=lambda c: c["ordem"])

    entradas = []  # (id, rotulo, titulo, parte, html)
    for c in caps:
        f = CAP / c["ficheiro"]
        if not f.exists():
            continue
        texto = f.read_text(encoding="utf-8").strip()
        texto = re.sub(r"^# .*\n", "", texto, count=1)  # o título é desenhado pela página
        entradas.append((f"c{c['ordem']:02d}", c["rotulo"], c["titulo"], c.get("parte", ""), md_para_html(texto)))

    posf = LIVRO / "00-o-que-poderia-e-deveria-fazer.md"
    if posf.exists():
        texto = posf.read_text(encoding="utf-8").strip()
        m = re.match(r"^# (.*)\n", texto)
        titulo = m.group(1).strip() if m else "Se fosses tu"
        texto = texto[m.end():] if m else texto
        entradas.append(("posfacio", "Posfácio", titulo, "Posfácio", md_para_html(texto)))

    artigos, indice, parte_atual = [], [], None
    for i, (aid, rotulo, titulo, parte, corpo) in enumerate(entradas):
        grupo = parte if not rotulo.startswith(("Prólogo", "Epílogo", "Posfácio")) else ""
        if grupo and grupo != parte_atual:
            indice.append(f'<li class="toc-parte">{html.escape(grupo)}</li>')
            parte_atual = grupo
        indice.append(
            f'<li><a href="#{aid}" data-go="{aid}"><span class="toc-rot">{html.escape(rotulo)}</span>'
            f'<span class="toc-tit">{html.escape(titulo)}</span></a></li>')
        artigos.append(
            f'<article class="cap" id="{aid}" data-i="{i}" hidden>'
            f'<header class="cap-head"><p class="cap-parte">{html.escape(grupo or "")}</p>'
            f'<p class="cap-rot">{html.escape(rotulo)}</p><h2 class="cap-tit">{html.escape(titulo)}</h2></header>'
            f'<div class="prosa">{corpo}</div></article>')

    linhas_roteiro = "".join(
        f'<tr><td class="r-rot">{html.escape(c["rotulo"])}<br><span>{html.escape(c["titulo"])}</span></td>'
        f'<td class="r-data">{html.escape(c["data"])}<br><span>{html.escape(c["local"])}</span></td>'
        f'<td class="r-pov">{html.escape(c["pov"])}</td><td class="r-res">{html.escape(c["resumo"])}</td></tr>'
        for c in caps)

    modelo = (FERR / "leitor-modelo.html").read_text(encoding="utf-8")
    pagina = (modelo
              .replace("{{TITULO}}", html.escape(roteiro["titulo"]))
              .replace("{{LOGLINE}}", html.escape(roteiro["logline"]))
              .replace("{{INDICE}}", "\n".join(indice))
              .replace("{{CAPITULOS}}", "\n".join(artigos))
              .replace("{{ROTEIRO}}", linhas_roteiro)
              .replace("{{N}}", str(len(entradas))))
    SAIDA.mkdir(exist_ok=True)
    (SAIDA / "leitor.html").write_text(pagina, encoding="utf-8")
    print(f"leitor.html: {len(entradas)} secções, {len(pagina) // 1024} KB")


if __name__ == "__main__":
    main()
