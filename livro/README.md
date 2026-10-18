# Antrópico

*Em 2015, um explicador de Cacilhas que desistiu da Física torna-se a única pessoa do mundo com acesso a uma inteligência artificial de 2026, que não sabe o futuro e só guarda uma data sem ano.*

Thriller em português europeu: prólogo, 35 capítulos em quatro Partes, epílogo e posfácio, com cerca de 108 000 palavras.

## Ler

| Formato | Ficheiro |
|---|---|
| EPUB (leitores de livros, telemóvel) | [`edicao/antropico.epub`](edicao/antropico.epub) |
| PDF A5, 414 páginas | [`edicao/antropico.pdf`](edicao/antropico.pdf) |
| Manuscrito único em Markdown | [`edicao/manuscrito.md`](edicao/manuscrito.md) |
| Capítulos soltos | [`capitulos/`](capitulos/) |

O posfácio, «Se fosses tu» ([`00-o-que-poderia-e-deveria-fazer.md`](00-o-que-poderia-e-deveria-fazer.md)), é a resposta direta à pergunta que deu origem ao livro: o que poderia, e o que deveria, fazer quem fosse a única pessoa com acesso ao Claude Code em 2015.

## Bastidores

- [`bastidores/biblia.md`](bastidores/biblia.md): plot completo, regras da anomalia, personagens, cronologia e guia de estilo.
- [`bastidores/roteiro.md`](bastidores/roteiro.md) e [`bastidores/roteiro.json`](bastidores/roteiro.json): roteiro capítulo a capítulo.
- [`bastidores/propostas/`](bastidores/propostas/): as quatro propostas iniciais (caça ao homem, ascensão e queda, dinheiro e sombra, o enigma).
- [`bastidores/dossie-2015.md`](bastidores/dossie-2015.md): dossiê de época (Portugal e o mundo, 2015–2017).
- [`bastidores/registo-continuidade.md`](bastidores/registo-continuidade.md): o que cada capítulo realmente contém.

## Voltar a montar

```
python3 livro/ferramentas/montar.py     # manuscrito, EPUB, HTML e PDF em livro/edicao/
python3 livro/ferramentas/leitor.py     # página de leitura em livro/edicao/leitor.html
```

Precisa de `pandoc` e, para o PDF, do Playwright com o Chromium.
