#!/usr/bin/env python3
"""Monta o livro a partir dos capítulos.

Lê a ordem e as Partes de bastidores/roteiro.json, junta os capítulos e o
posfácio num único manuscrito.md e gera o EPUB, o HTML e o PDF.

Uso:  python3 livro/ferramentas/montar.py [--sem-pdf]
"""
import json
import pathlib
import re
import subprocess
import sys

LIVRO = pathlib.Path(__file__).resolve().parent.parent
FERR = LIVRO / "ferramentas"
CAP = LIVRO / "capitulos"
SAIDA = LIVRO / "edicao"

FENCE = re.compile(r"^\s*(```|~~~)")


def descer_titulos(texto, niveis=1):
    """Acrescenta `niveis` cardinais aos títulos markdown fora dos blocos de código."""
    out, dentro = [], False
    for linha in texto.splitlines():
        if FENCE.match(linha):
            dentro = not dentro
        elif not dentro and re.match(r"^#{1,5} ", linha):
            linha = "#" * niveis + linha
        out.append(linha)
    return "\n".join(out)


def contar_palavras(texto):
    return len(re.findall(r"\w+(?:[-'’]\w+)*", texto))


def main():
    roteiro = json.loads((LIVRO / "bastidores" / "roteiro.json").read_text(encoding="utf-8"))
    titulo = roteiro["titulo"]
    subtitulo = roteiro.get("subtitulo", "")
    caps = sorted(roteiro["capitulos"], key=lambda c: c["ordem"])

    partes = [
        "---",
        f"title: {json.dumps(titulo, ensure_ascii=False)}",
        *([f"subtitle: {json.dumps(subtitulo, ensure_ascii=False)}"] if subtitulo else []),
        'author: "Claude Code"',
        "lang: pt-PT",
        "---",
        "",
    ]

    parte_atual, total, em_falta = None, 0, []
    for c in caps:
        f = CAP / c["ficheiro"]
        if not f.exists():
            em_falta.append(c["ficheiro"])
            continue
        texto = f.read_text(encoding="utf-8").strip()
        total += contar_palavras(texto)
        parte = (c.get("parte") or "").strip()
        rotulo = c.get("rotulo", "")
        epilogo_ou_prologo = rotulo.lower().startswith(("prólogo", "epílogo"))
        if parte and parte != parte_atual and not epilogo_ou_prologo:
            partes += [f"# {parte}", ""]
            parte_atual = parte
        if epilogo_ou_prologo:
            partes += [texto, ""]  # prólogo e epílogo ficam ao nível das Partes
            parte_atual = None if rotulo.lower().startswith("prólogo") else parte_atual
        else:
            partes += [descer_titulos(texto), ""]

    if em_falta:
        print("AVISO: capítulos em falta:", ", ".join(em_falta), file=sys.stderr)

    # O ensaio que responde à pergunta de partida fecha o livro, como posfácio.
    posfacio = LIVRO / "00-o-que-poderia-e-deveria-fazer.md"
    if posfacio.exists():
        corpo = posfacio.read_text(encoding="utf-8").strip()
        m = re.match(r"^# (.*)\n", corpo)
        titulo_posfacio = m.group(1).strip() if m else "Se fosses tu"
        corpo = corpo[m.end():] if m else corpo
        partes += [f"# Posfácio — {titulo_posfacio}", "", descer_titulos(corpo), ""]

    SAIDA.mkdir(exist_ok=True)
    manuscrito = SAIDA / "manuscrito.md"
    manuscrito.write_text("\n".join(partes) + "\n", encoding="utf-8")
    print(f"manuscrito.md: {total:,} palavras em {len(caps) - len(em_falta)} capítulos".replace(",", "."))

    slug = roteiro.get("slug") or re.sub(r"[^a-z0-9]+", "-", titulo.lower()).strip("-") or "livro"
    epub = SAIDA / f"{slug}.epub"
    capa = LIVRO / "ferramentas" / "capa.png"
    subprocess.run(
        ["pandoc", str(manuscrito), "-o", str(epub), "--toc", "--toc-depth=2", "--split-level=2",
         "--css", str(FERR / "epub.css"), "--metadata", "toc-title=Índice",
         *(["--epub-cover-image", str(capa)] if capa.exists() else [])],
        check=True,
    )
    print("EPUB:", epub.relative_to(LIVRO.parent))

    html = SAIDA / f"{slug}.html"
    subprocess.run(
        ["pandoc", str(manuscrito), "-s", "-o", str(html), "--toc", "--toc-depth=2",
         "--css", str(FERR / "impressao.css"), "--embed-resources", "--metadata", "toc-title=Índice"],
        check=True,
    )
    print("HTML:", html.relative_to(LIVRO.parent))

    if "--sem-pdf" not in sys.argv:
        pdf = SAIDA / f"{slug}.pdf"
        subprocess.run(["node", str(FERR / "pdf.mjs"), str(html), str(pdf)], check=True)
        print("PDF:", pdf.relative_to(LIVRO.parent))


if __name__ == "__main__":
    main()
