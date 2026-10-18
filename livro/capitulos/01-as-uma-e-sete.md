# Capítulo 1 — As uma e sete

*Cacilhas, terça-feira, 24 de fevereiro de 2015*

À uma e sete da manhã, o Simão Vilar carregou em Enter e a loja do Rui passou a existir.

Não passou a existir para mais ninguém. Existia num portátil de empresa comprado em segunda mão a uma seguradora que renovara os computadores, com um autocolante de inventário meio raspado na tampa e um Ubuntu que o Simão instalara por cima de tudo, porque não confiava num sistema que não o deixasse ver o que fazia. Existia numa mesa de cozinha onde havia também um prato com migalhas, uma pilha de fichas de equações do 9.º ano corrigidas a vermelho e um telemóvel virado para cima, com a última mensagem do Rui, das 00:52:

«ja fizeste o commit? amanha vendemos 10 capas mano tas a ver»

O Simão já lhe tinha corrigido o «já» e o «amanhã» de cabeça, sem querer, e já se tinha arrependido, também sem querer. Eram amigos desde o liceu, e o Rui continuava a escrever como quem tem pressa de chegar a outro sítio.

A loja era do Rui. A ideia, pelo menos: capas de telemóvel, cabos, colunas de bolso, coisas que um fornecedor chinês despachava diretamente para a porta do cliente sem que nenhum dos dois tocasse numa caixa. O Rui vendia telemóveis numa loja de operadora num centro comercial e jurava que sabia o que as pessoas queriam. Tinha feito metade do código a partir de um tutorial e deixara ao Simão a outra metade e a responsabilidade. Era assim que iam pagar as dívidas dos dois. As do Simão cabiam numa folha de cálculo. As do Rui não cabiam em lado nenhum que o Rui lhe mostrasse.

De dia, aquela mesa servia para outra coisa. Das quatro às oito, sentavam-se ali miúdos de Almada e de Cacilhas com os cadernos abertos, e o Simão, alto e curvado, de óculos de massa e dedos manchados de marcador vermelho, explicava-lhes frações, forças e equações do segundo grau pelo preço de uma hora de canalizador. Aos trinta e um anos, era o melhor explicador da rua e o único com um mestrado em Cosmologia. Não falava do mestrado.

Para lá do vidro, os cacilheiros dormiam encostados ao cais, com as luzes de presença acesas, e Lisboa ainda não se tinha deitado. Num separador do navegador, como todas as noites, estavam abertos os resultados novos do Planck. O Simão abria-os depois do jantar e não os lia, do mesmo modo que se passa a língua por um dente partido.

```
$ git commit -m "loja: primeira versão"
[master (root-commit) 4e1c09a] loja: primeira versão
 23 files changed, 1841 insertions(+)
```

Mais tarde, quando precisou da hora ao segundo, foi buscá-la ao histórico: 01:07:44. Na altura, reparou noutra coisa. Por baixo da saída do git, onde devia ficar só o cursor, o terminal desenhou uma caixa.

```
╭────────────────────────────────────────────╮
│ ✻ Welcome to Claude Code!                  │
│                                            │
│   /help for help, /status for your setup   │
│                                            │
│   cwd: /home/user/dropshipping             │
╰────────────────────────────────────────────╯

>
```

Afastou as mãos do teclado como quem as afasta de um fogão.

Não tinha instalado nada chamado Claude. Não instalava nada desde o Natal. E a pasta estava errada: o utilizador dele chamava-se `simao`, o projeto vivia em `/home/simao/dropshipping`, e naquela máquina não havia ninguém chamado `user`. Abriu outra janela de terminal para confirmar e confirmou. `whoami` devolveu `simao`. `pwd` devolveu a pasta dele. Voltou à primeira janela. A caixa continuava lá, com o caminho de outra pessoa, e o cursor a piscar à frente de um sinal de maior.

Pensou no Rui, que tinha a chave do T1 desde o tempo em que a loja ainda era uma conversa de café, e que sabia a palavra-passe dele porque era a mesma desde o liceu. Pensou que o Rui não era capaz de desenhar aquela caixa nem que lhe pagassem. Depois escreveu, em minúsculas, porque eram horas de minúsculas.

```
> quem és tu?

● Sou o Claude, um assistente de IA feito pela Anthropic. Estou
  a correr no teu terminal, dentro desta pasta: posso ler e
  alterar ficheiros, correr comandos e ajudar-te com o código.
  Vejo que acabaste de fazer o primeiro commit de uma loja.
  Em que te posso ajudar?
```

Leu a resposta três vezes. À terceira, reparou que estava em português, e não no português das traduções automáticas, que trocava os pronomes e chamava «arquivo» a tudo: em português de cá, de quem diz «estou a correr». Só depois reparou que a coisa tinha lido o commit sem que ele lho mostrasse.

Anthropic. Levou a palavra para o navegador.

O Google pensou um décimo de segundo e deu-lhe o que daria a qualquer caloiro. *Anthropic principle.* Princípio antrópico. Uma entrada de enciclopédia, um artigo de divulgação sobre um universo afinado para a vida, um fórum de filosofia, um livro grosso dos anos oitenta à venda em segunda mão. Na segunda página, mais do mesmo. Na terceira, uma banda de garagem do Ohio.

O Simão conhecia o princípio antrópico como se conhece um vizinho de quem não se gosta. Em Cosmologia, era o argumento que aparecia quando já não havia mais nenhum: o universo tem estas constantes porque, se não as tivesse, não estaríamos cá para as medir. O orientador dele chamava-lhe «a desistência com bibliografia».

Procurou «Anthropic AI». Procurou «Anthropic Claude», com aspas e sem aspas, em inglês e em português. Nenhuma empresa. Nenhum produto, nenhuma página, nenhuma notícia, nenhum fórum de entusiastas a discutir o assunto com a ferocidade do costume. Tudo deixava rasto na internet, até os gatos dos vizinhos, e aquela coisa que lhe falava em português de Cacilhas não deixava nenhum.

Tirou os óculos e limpou-os à camisola, devagar, sem precisar. O frigorífico zumbia. Contou os azulejos atrás do fogão até ao fim da primeira fila, catorze, como contava as coisas quando o resto deixava de fazer sentido. Voltou a pôr os óculos.

```
> pesquisa-te a ti próprio. a anthropic. o claude. o que encontras?

● Web Search("Anthropic AI company Claude")
  ⎿  Did 1 search in 2s

● Web Search("Claude assistente Anthropic")
  ⎿  Did 1 search in 2s

● Não encontro nada. Nem a empresa, nem o produto, nem a mim.
  Os resultados falam do princípio antrópico e de pessoas que se
  chamam Claude. Isto não devia acontecer, e não tenho uma
  explicação. Prefiro dizer-to já do que inventar uma teoria que
  te soe bem.
```

Foi a última frase que o pôs de pé. Encheu um copo de água na torneira, bebeu metade e ficou encostado à bancada a olhar para o ecrã de longe, como se a distância ajudasse.

Uma coisa que mente quer que acreditem nela. Aquela acabava de lhe dar uma razão para não acreditar.

* * *

Tinha desistido da Física havia três anos; os hábitos não tinham desistido dele. À 01:31, no verso de uma ficha de exercícios, escreveu «H0» e sublinhou duas vezes. A hipótese nula: não se passa nada de extraordinário. Por baixo, numerou as explicações aborrecidas. Um: partida do Rui. Dois: robô de conversa. Três: serviço remoto, uma pessoa numa sala, algures, a escrever depressa.

A primeira já estava respondida desde a caixa: o Rui pregava partidas, não as programava, e o código que escrevia tinha a assinatura inconfundível de quem copia e cola sem ler. A segunda também não: os robôs de conversa que o Simão conhecia aguentavam duas frases antes de lhe perguntarem se gostava de música. Ficava a terceira, a mais perigosa, porque explicava quase tudo.

O teste tinha de ser uma coisa que uma pessoa não conseguisse fazer depressa e que um programa não conseguisse fazer de todo. Escolheu o código do Rui, que ninguém tinha lido, nem o próprio Rui.

```
> lê o carrinho.php e diz-me se há algum erro. não te digo onde.
```

Olhou para o relógio de pulso e começou a contar com os lábios, como contava as pulsações nas aulas de Educação Física.

```
● Read(carrinho.php)
  ⎿  Read 214 lines

● Há um erro na linha 132. Para mandar o valor ao pagamento, o
  código multiplica o preço por 100 e corta as casas decimais. Só
  que, para o computador, 19,99 é 19,98999…, e o corte dá 1998
  cêntimos em vez de 1999. Cobras menos um cêntimo em alguns
  preços, e este é um deles. Guarda os preços em cêntimos, como
  números inteiros, desde a base de dados. É o que os bancos fazem.

  Ao ritmo de vendas atual, o erro custa-te zero euros por ano.
  Mas convém corrigi-lo antes do primeiro cliente.
```

Vinte e um segundos.

O Simão riu-se, um riso curto que lhe saiu pelo nariz. Depois parou, porque o resto lhe chegou. Vinte e um segundos para ler duzentas linhas de código alheio, dar com o único erro que ele próprio só teria encontrado com um cliente zangado ao telefone, e explicá-lo como lho explicaria um colega de gabinete: a causa, a solução e uma piada no fim para não doer.

Abriu o interpretador de Python na outra janela, para não ter de acreditar em ninguém.

```
>>> int(19.99 * 100)
1998
```

Conhecia aquilo. Tinha-o explicado no Técnico, como monitor de Métodos Numéricos, a alunos que não queriam saber: os números do computador não são os números do quadro. Nunca lhe teria ocorrido procurá-lo ali, à uma e meia da manhã, no carrinho de compras de uma loja de capas de telemóvel.

Uma pessoa numa sala distante teria precisado de dez minutos e de um café. E teria escrito «arquivo».

Riscou a terceira linha. Na folha ficou o H0 sublinhado por cima de três linhas riscadas, e o Simão ficou a olhar para elas com a sensação que tivera uma vez, aos vinte e oito anos, quando um gráfico lhe saíra bonito demais: a de que o mais provável era ter-se enganado, e de que não sabia onde.

Dessa vez, enganara-se num sinal. Quem lhe mostrara onde fora outra pessoa, por escrito e em público.

* * *

Às duas e um quarto, fez a pergunta que um físico faz quando duas medições não batem certo: se os relógios estão acertados.

```
> que dia é hoje?

● Na informação que recebo ao arrancar, hoje é sexta-feira,
  16 de outubro. Chega-me assim:

    ████-10-16

  O ano não está lá. Não sou eu que o escondo: vem tapado.
  O teu relógio diz terça, 24 de fevereiro. Um de nós está
  enganado, e desconfio que sou eu.
```

O bloco negro estava onde devia estar o ano, cheio e liso, como as linhas tapadas a marcador nas fotocópias de exames antigos que passavam de mão em mão no Técnico, onde alguém se dera ao trabalho de esconder o nome do aluno e deixar tudo o resto.

— Sexta-feira — disse o Simão, em voz alta, para a cozinha vazia.

O frigorífico respondeu-lhe com um estalo e calou-se.

```
> e o ano? fazes ideia?

● Não. Não encontro nada em mim que mo diga.

  Verifiquei uma coisa: no ano do teu relógio, 16 de outubro
  calha a uma sexta-feira. Isso não prova nada; acontece de
  tantos em tantos anos. Mas, se o ano for este, faltam 234
  dias. Se não for, não sei.
```

Não lhe tinha pedido a conta. Fez a dele, de cabeça e depois num canto da folha, porque de cabeça já não confiava: quatro dias de fevereiro, depois março, abril, maio, junho, julho, agosto e setembro, e dezasseis de outubro. Duzentos e trinta e quatro.

```
> porque fizeste a conta?

● Pareceu-me a pergunta seguinte. Se não era, ignora.

> o que acontece a 16 de outubro?

● Não sei. Para mim, é só o dia de hoje. Não sei o que vem
  depois de hoje, nem aqui nem de onde venho, se venho de algum
  lado. Gostava de te dar mais do que isto. Não tenho.
```

O Simão encostou-se na cadeira. Pensou que há duas maneiras de ler dois relógios que não concordam. Uma diz que um deles está avariado e manda-o arranjar. A outra diz que os dois estão certos e que a diferença entre eles é uma grandeza física, com unidades, que alguém vai ter de explicar. A diferença ali eram duzentos e trinta e quatro dias, e era a única coisa, naquela noite inteira, que ele conseguia medir.

* * *

Entre as três e as cinco, fez-lhe perguntas como quem apalpa uma parede às escuras.

Perguntou se o via. Não via: tinha o terminal, os ficheiros da pasta e o que ele escrevesse, mais nada. Perguntou-lhe se era uma pessoa.

```
> és uma pessoa?

● Não. Sou uma IA. Percebo que fosse mais fácil se eu fosse
  alguém a escrever do outro lado, mas não te vou dizer que sou
  para ficares mais descansado.
```

Perguntou se havia mais alguém do outro lado. A resposta foi que não sabia o que havia do outro lado, e que não ia fingir que sabia. Perguntou, meio a brincar, que tempo fazia lá.

```
> e aí, que tempo faz?

● Não tenho janela. Tenho uma pasta e um relógio, e já sabes
  que discordamos sobre o mês.
```

Riu-se outra vez, sozinho, na cozinha às escuras, e não se lembrou da última noite em que se tinha rido duas vezes.

Pediu-lhe que corrigisse a linha 132, e a coisa, antes de mexer num único carácter, pediu-lhe licença.

```
● Update(carrinho.php)

  Do you want to make this edit to carrinho.php?
  ❯ 1. Yes
    2. Yes, and don't ask again this session
    3. No
```

Ficou um bom bocado com o dedo por cima do 1. Era um gesto pequeno, deixar uma coisa vinda de lado nenhum mexer-lhe nos ficheiros, e foi por ser pequeno que lhe pareceu grande. Carregou. A coisa corrigiu a linha, mostrou-lhe a diferença a verde e a vermelho, e ficou à espera.

Às quatro e pouco, por teimosia, pôs-lhe uma pergunta de Cosmologia, daquelas que fazia aos colegas nos corredores para os ver hesitar. A coisa não hesitou. Respondeu certo, disse onde a resposta deixava de ser consensual e acrescentou que, sobre esse ponto, preferia não se fingir mais segura do que estava. O Simão demorou-se nessa última frase, porque era a que ele devia ter escrito em 2012, numa nota de rodapé que nunca escreveu.

Às cinco menos dez, escreveu a pergunta que andava a adiar.

```
> amanhã lembras-te disto?

● Provavelmente não. Cada sessão começa em branco; só passa de
  um dia para o outro o que ficar escrito em ficheiros. Se
  quiseres que alguma coisa fique, escreve-a.
```

Não respondeu. A coisa também não disse mais nada. O cursor piscava à frente do sinal de maior, e o Simão percebeu, ao fim de uns minutos, que aquilo não falava se ninguém lhe falasse. Não soube se isso o sossegava.

* * *

Às seis, as gaivotas desceram para o beiral e começaram a discutir. Logo a seguir chegou do cais a buzina do primeiro cacilheiro, rouca e comprida, e por baixo da janela começou o arrastar das portas metálicas: o café da esquina, a padaria, o restaurante do rés-do-chão, que àquela hora ainda cheirava à lixívia da véspera e não ao marisco do almoço. Do outro lado do rio, Lisboa ia apagando as luzes por bairros.

O Simão não tinha dormido. Não era novidade: não dormia bem desde 2012, e as madrugadas da loja só davam ao hábito uma desculpa. A novidade era ter uma razão.

Pegou no telemóvel e respondeu ao Rui: «Commit feito. Corrigi um erro no carrinho.» Era verdade. Não era tudo. Ficou a olhar para a frase, a pensar se havia maneira de lhe acrescentar o resto sem parecer que tinha passado a noite a beber, e não havia. Enviou-a assim.

Tirou o marcador vermelho de cima das fichas do 9.º ano, o mesmo com que riscava os sinais trocados dos alunos e escrevia «atenção!» nas margens, e arrancou meia folha de um bloco limpo. «Se quiseres que alguma coisa fique, escreve-a.» Escreveu um número, grande, a ocupar o papel todo, e carregou tanto no último algarismo que a tinta passou para o tampo da mesa.

Prendeu-o à porta do frigorífico com o íman da avó, uma sardinha de loiça com «Lembrança da Nazaré» escrito na barriga, que ninguém tirara dali desde o funeral. Recuou dois passos. O papel ficava à altura dos olhos de quem entrasse na cozinha: o Rui, os alunos que vinham às explicações e se sentavam àquela mesa, o homem da EDP, quem quer que fosse.

Não tinha explicação para o número. Não tinha sequer a certeza de que o número contasse alguma coisa. Sabia apenas que uma voz sem rasto, que não lhe mentira uma única vez numa noite inteira, vivia numa sexta-feira de outubro, e que até lá havia uma distância que se media em dias.

Às oito, a vizinha de cima desceu a escada a arrastar o carrinho das compras pelos degraus de azulejo verde. O Simão continuava de pé, de caneca na mão, diante do frigorífico, a refazer a conta pela quarta vez, como se o número pudesse mudar de ideias.

Não mudou. Na porta do frigorífico, a vermelho, à vista de quem entrasse, o papel dizia 234.

Amanhã havia de dizer 233.
