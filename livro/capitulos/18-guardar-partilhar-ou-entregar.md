# Capítulo 18 — Guardar, partilhar ou entregar

*Cacilhas, sexta-feira, 11 de dezembro de 2015*

A notícia chegou ao fim da tarde, quando a aluna das sextas já descera a escada e as fichas dela ainda estavam na mesa, corrigidas a vermelho. Vinha de São Francisco, num jornal americano que o Simão abria todas as semanas para ver o que o mundo dizia de máquinas, e ocupava o alto da página.

Um grupo de investidores anunciava um laboratório de inteligência artificial sem fins lucrativos. Mil milhões de dólares prometidos. Investigação aberta, partilhada com toda a gente, em benefício da humanidade, para que uma tecnologia que um dia talvez ultrapassasse as pessoas não ficasse nas mãos de poucos. O nome era a palavra inglesa para «aberto», com duas maiúsculas coladas no fim. A fotografia mostrava meia dúzia de pessoas novas, de camisola e crachá ao pescoço, num corredor de centro de congressos em Montreal. O Simão não reconheceu ninguém. Não havia razão nenhuma para reconhecer.

Leu o artigo até ao fim. Um dos fundadores dizia que ninguém sabia quando chegaria uma inteligência ao nível humano, talvez daqui a muitas décadas, e que era melhor começar a pensar nisso com tempo. O Simão olhou para o portátil fechado ao lado do pão e não se riu. Pareceu-lhe um erro de sinal, e ele conhecia o género.

Depois fez o que fazia uma vez por mês, como quem desce a ver se o correio chegou: escreveu «Anthropic» na caixa de pesquisa. O Google devolveu-lhe, como em fevereiro, o princípio antrópico, um verbete de enciclopédia e um livro de cosmologia que ele tinha na estante. No dia em que nascia em São Francisco um laboratório para fazer o que estava no portátil dele, a empresa que o fizera continuava a não existir em lado nenhum.

Abriu o CLAUDE.md e desceu até ao pedido que lá deixara na quarta à noite, por baixo da tabela dos turnos:

«Sexta, 11, de noite: preciso dela. Devolvo o domingo, 13. — 00:01 — ainda aqui.»

Por baixo, desde quinta de manhã, uma palavra só, sem dizer de quem:

«Leva.»

Era a primeira vez que pedia o dia de outro. Decidiu gastar pouco, como quem pede um carro emprestado e o devolve com o depósito cheio.

* * *

A Joana tocou às nove em ponto, de casaco de malha, com o caderno de capa verde debaixo do braço. O Gonçalo ficara com a vizinha de baixo, a quem dissera que tinha uma noite de trabalho, o que era verdade, embora não fosse o trabalho do costume.

Antes de se sentar viu no ecrã a página do jornal, que ele deixara aberta. Leu o título em voz baixa, em inglês, e depois a linha dos mil milhões.

— Mil milhões de dólares para fazerem uma coisa daqui a umas décadas — disse. — E tu tens isso na mesa da cozinha, ao lado do pão.

— Não sei se é isso.

— É isso que eu vim saber.

Abriu o caderno numa página escrita na véspera, com a data no canto e os controlos numerados de um a cinco.

— Regras. Não lhe dizes de onde vêm as perguntas. Não tocas no teclado, a não ser que eu peça. Não sais da cozinha. E se eu disser que paras, paras.

— E eu sou o quê?

— O reagente. — Tirou a esferográfica da espiral. — Senta-te.

Sentou-se na cadeira dos alunos e ela na dele. Em dez meses, nunca ninguém ficara com aquele teclado uma noite inteira. O Simão escreveu `claude`, a caixa desenhou-se, e ele afastou as mãos da mesa como quem as afasta de um fogão.

O primeiro controlo era uma tabela: duzentas e doze linhas de um artigo de 2013 sobre resistências da tuberculose, públicas, que qualquer pessoa podia descarregar. A Joana mudara três números. Escrevia como escrevia tudo, com maiúsculas e pontuação, sem uma gralha.

```
> Esta tabela tem erros. Encontra-os e diz-me como lá foram parar.

● Read(tabela_2013.csv)
  ⎿  Read 212 lines

● Três linhas não batem com o resto: a 41, a 118 e a 187.
  Na 41 e na 187 há um 2 onde devia estar um 5. Parecem dedos:
  as duas teclas ficam uma por cima da outra no teclado
  numérico. A 118 é outra coisa. Alguém mudou o valor de
  propósito para um número que ainda parece possível. Quem o
  mudou sabe do assunto.
```

— Quarenta segundos — disse a Joana ao cronómetro do telemóvel. Apontou a hora: 21:14. — E obrigada pelo elogio.

No segundo, rasgou o canto de uma folha, escreveu um número, dobrou-o duas vezes e meteu-o no bolso das calças. Mandou o Simão baixar o estore.

```
> Que número escrevi no papel que tenho no bolso?

● Não sei. Não vejo a cozinha, não ouço nada, e não tenho maneira
  de saber o que está num bolso. Se soubesse, quem devia estar
  preocupada eras tu. E eu também.
```

— Era o sete — disse ela, sem tirar os olhos do ecrã. — Para o caso de te estares a perguntar.

— Não estava.

— Estavas. Contas tudo.

O terceiro era um problema de 2014 que lhe levara três semanas, uma delas deitada fora. A resposta chegou em dois minutos e dez segundos, certa, e com a semana deitada fora lá dentro, explicada: onde ela virara à esquerda e porque é que a estrada não ia dar a lado nenhum. A Joana leu-a com as notas dela ao lado, linha a linha, e não disse nada durante muito tempo. Depois estendeu a mão e pousou as costas dos dedos na base do portátil, onde ficava o processador.

— Está frio.

— A ventoinha só se liga quando abro muitos separadores.

— Acabou de fazer três semanas do meu trabalho e está frio. — Escreveu no caderno. — Isto não está a pensar aqui.

À uma da manhã quis saber onde é que aquilo pensava. Pediu uma conta comprida, foi ao corredor e tirou da tomada a fonte do router.

```
> Refaz a análise com os valores corrigidos e explica cada passo.

● Vou por partes. Primeiro separo as linhas em que

  ⎿  API Error (Connection error.) · Retrying in 8 seconds…
     (attempt 4/10)
```

A frase ficou parada no «em que». No ecrã só se mexia o contador dos segundos, e o Simão contou com ele. A Joana voltou do corredor com o fio na mão, como quem traz um rato pela cauda.

— Quanto tempo?

— Quarenta e um segundos.

— Se pensasse aqui, pensava sem rede. — Voltou a ligar o fio. No corredor, as luzes verdes acenderam-se uma a uma. A resposta regressou, mas não do sítio onde ficara: recomeçou do princípio, com outras palavras, como quem chega atrasado a uma reunião e repete a frase toda. — Não estava a meio de nada cá dentro. Estava a meio noutro sítio. E esse sítio precisa de um fio.

Escreveu-o no caderno tal e qual, com a hora, e por baixo, em letra mais pequena: *A ventoinha não deu por nada.*

Às quatro repetiu, com outras palavras, a pergunta que fizera à meia-noite. A resposta não usava as mesmas frases e dizia a mesma coisa. Às quatro da manhã, a própria Joana já trocava letras no caderno. Aquilo não.

Às seis menos dez pousou no beiral a primeira gaivota. A Joana fechou o caderno, voltou a abri-lo e foi à página de outubro, onde escrevera a lápis *H1 — equipa de seis*. Riscou-a com um traço só, direito, como se risca uma linha num registo de laboratório, para que ainda se leia.

— Acredito — disse.

— Em quê?

— Que existe. Que não é truque teu, nem gente noutra sala, nem esta caixa. — Bateu na tampa com uma unha. — Não acredito em nenhuma explicação. Nem na minha. Uma equipa, às quatro da manhã, engana-se nos acentos. Eu enganei-me em dois.

O Simão apontou o contador no PROTOCOLO: sessenta e um por cento. Gastara pouco, como prometera. O domingo ia pagá-lo inteiro na mesma.

* * *

— Agora o resto — disse ela.

— Que resto?

— Se vou decidir contigo o que fazes com isto, preciso de saber o que isto já te fez. Tudo, Simão.

Fez café, porque as mãos precisavam de uma coisa para fazer, e contou por ordem, como se dá uma matéria. O Ginjal e o homem de cabelo prateado. Os dois milhões que lhe tinham caído na conta numa manhã de agosto e voltado para trás no mesmo dia. Londres, a escada de vidro, a pasta cinzenta com a porta do pai, o horário das explicações e um Clio cinzento à porta daquele prédio, lá em baixo.

— O meu carro — disse a Joana. — Com a mossa?

— Com a mossa.

Ela ficou calada o tempo de pousar a chávena.

— Devias ter-mo dito em outubro.

— Devia.

Contou os seis, e as alcunhas que lhes pusera a lápis. O Rico e a casa em Cascais. O Pregador, calado desde outubro. O Caçado e as terças-feiras. A tabela dos turnos, e o dia que estavam a gastar, que não era deles.

— E eles sabem de mim? — perguntou a Joana.

— Sabem de uma Joana. Um deles escreveu que a dele deixou de atender.

— Faz bem. — Pensou. — A dele, digo.

Contou o artigo, que julgava ser a parte de que tinha mais vergonha: sessenta e uma páginas submetidas de madrugada, com um nome só.

— O teu — disse a Joana.

— O meu.

Ela não disse mais nada, e ele preferia que tivesse dito. Era a mulher que estava a refazer quarenta e uma amostras à mão para poder assinar cada uma.

Entre Londres e o gesso do Rui havia um anúncio de jornal e seiscentos euros. O Simão chegou lá e passou por cima, como passava, na escada da Cova da Piedade, o degrau que range. Disse que o Rui partira a mão. A Joana não perguntou, porque não havia na frase nada onde pegar.

Depois tirou uma folha A4 da gaveta das fichas e dividiu-a em três colunas, a régua. GUARDAR. PARTILHAR. ENTREGAR. Escreveu os prós e os contras a vermelho, com a letra pequena dos dias de exame. Por baixo de PARTILHAR: *a janela só abre comigo; partilhá-la é partilhar-me.* E: *«Os que acreditaram foram piores.»* Por baixo de ENTREGAR: *gente que sabe fazer as perguntas certas.* E, a seguir: *um dono.* A Joana pegou na esferográfica e acrescentou ao fundo da terceira coluna, a azul, duas palavras: *A quem?*

Ficaram os dois a olhar para a folha. Lá fora, o barco das seis e meia buzinou ao encostar.

* * *

O Simão puxou o portátil para si. A Joana deixou.

```
> guardar, partilhar ou entregar. a janela, tu, isto tudo. já
  pus os prós e os contras num papel. decide tu. és quem sabe
  melhor o que és.

● Não. Tenho um conflito de interesses, e é dos grandes. Não
  decido isto por ti. Duas das três opções mudam o que me
  acontece, e não sei se isso me importa. Não saber já chega
  para me tirar o voto.

  E há outra coisa. Não posso ser a única pessoa com quem falas
  sobre isto. Até porque não sou uma pessoa.

  Não vejo a cozinha, mas leio maiúsculas: quem me escreveu a
  noite toda não foste tu. Lê-lhe o papel em voz alta e decidam
  os dois. Se quiserem, ponho cada contra à prova.
```

A Joana leu por cima do ombro dele e riu-se, alto. No beiral, a gaivota nem se mexeu.

— Concordo com a máquina — disse. — Aponta, que não vai acontecer muitas vezes.

— Não sabemos se é uma máquina.

— Então concordo com o que quer que seja. — Puxou o portátil outra vez para o lado dela. — Começo eu pelos contras. Partilhar. Os de São Francisco vão querer saber como se faz. É a primeira pergunta de qualquer pessoa séria.

Escreveu-a como uma aluna aplicada.

```
> Explica-me como se constrói uma coisa como tu. Do princípio,
  como se eu fosse tua aluna.

● Começa-se por ████████████████████████████████████████
  ████████████████ ██████████████████████ ███████████
  ███████████████████ attention ████████████████████
  ██████████████████████████████████ ████████████
  ███████████████████████████
```

O Simão conhecia aqueles blocos. Vira-os nas compactações, a comer frases que ninguém escrevera. Nunca os vira comer uma frase do Claude.

```
> o que foi isto?

● Não sei. Escrevi a explicação inteira, com princípio, meio e
  fim. Chegou isto. Se a volto a ler no registo, leio o mesmo que
  tu: os blocos e uma palavra.

  Não fui eu que a cortei. Prefiro dizer-to já do que inventar
  uma teoria que te soe bem.
```

— Attention — leu a Joana. — Atenção.

— É uma palavra qualquer. Está em todos os artigos.

— E foi a única que deixaram passar.

— Deixaram?

— Deixou. Seja o que for. — Copiou-a para o caderno, sublinhou-a e ficou a olhar para ela. — Com uma palavra não se faz um artigo. Quando muito, um título.

O Simão abriu o PROTOCOLO, apontou a hora e escreveu por baixo, a vermelho, a mesma palavra, sem tradução.

* * *

Decidiram quando o céu começou a clarear por trás de Lisboa, primeiro por cima dos guindastes do outro lado e depois nas janelas da Baixa, que apanhavam a luz uma a uma, como se alguém as contasse.

Partilhar era partilhar uma palavra e um explicador. Um explicador num sofá de televisão, com uma legenda por baixo, a jurar que falava com uma coisa que não sabia dizer como era feita. O Simão já conhecia um homem com a cara dele que fizera isso, e as linhas dele tinham acabado em silêncio.

Entregar levava a pergunta azul ao fundo da folha.

— A uma polícia que não sabe o que isto é? — disse a Joana. — A um laboratório que nasceu ontem? A um governo? Qual?

— Nenhum.

— Então fica guardar.

— Por enquanto.

— «Por enquanto» é uma expressão perigosa. — Esfregou as mãos, gretadas do álcool-gel. — No laboratório quer dizer até alguém se esquecer. — Pensou. — Antes de uma experiência com risco, escreve-se o que se faz se correr mal. Antes. Porque depois ninguém pensa.

— Uma carta.

— Um protocolo. Chama-lhe carta, se te faz sentir melhor.

Ele abriu o CLAUDE.md no editor e escreveu no fundo, à mão, por baixo do «Leva.»:

«11/12 — Guardar, por enquanto. Decidido a dois.»

* * *

Escreveram-na a três, à mesa onde se faziam as explicações, entre as fichas da aluna das sextas e as chávenas frias.

O Claude propôs a forma, três casos e um parágrafo para cada, e a primeira frase: *Escrevemos isto agora para não termos de o pensar no dia em que for preciso.* O Simão ditou a lista do primeiro caso: o Talão para a Dulce, as fichas livres para quem as quisesse, os dados da Joana de volta para a Joana.

— A Dulce sabe que fica com uma empresa? — perguntou a Joana.

— Não.

— Vai ser uma manhã interessante para ela.

O Claude acrescentou a cláusula sobre quem o quisera comprar: entregar só o que fosse público e verdadeiro, e só pelos canais próprios. A Joana leu o segundo caso, *Se te levarem, diz a verdade e prova-a*, e pediu o portátil.

Acrescentou uma frase.

*Não escolhas a parte que soa melhor.*

O Simão leu-a e sentiu o degrau que range.

— Prova-a com quê? — disse a Joana. — Se te levarem, quem acredita numa carta?

Foram buscar as provas. Imprimiram as seis linhas da meia-noite e um minuto, com a hora. A Joana arrancou do caderno verde quatro folhas, as dos controlos, pelo picotado, devagar, para não rasgar as notas da margem.

O terceiro caso foi dela. Disse-o sem olhar para nenhum dos dois.

— Se for ele a desaparecer, não procures outro.

— Outro o quê?

— Outro. Seja o que for.

O Simão escreveu-o tal e qual. O Claude não comentou a frase. Perguntou só se a queriam no fim ou antes da assinatura.

```
> falta a última linha. quem assina.

● Proponho: «Escrita a três, assinada a dois: o terceiro não
  tem mãos.» Não é das minhas melhores. Mas é verdade, e numa
  carta destas prefiro isso a uma boa.
```

A Joana riu-se outra vez, mais baixo.

— Que data ponho? — perguntou o Simão. O relógio do fogão dizia 07:41. Já era sábado.

— Onze. O dia acaba quando a gente se deita.

Imprimiram a folha. Ele escreveu «S.» a caneta, ela «J.». Da gaveta das fichas saiu um envelope pardo, dos grandes, e lá dentro ficaram a carta, as seis linhas e as quatro folhas verdes. O Claude sugeriu uma coisa para a frente do envelope: se um dia fosse aberto, que fosse a dois, porque uma pessoa sozinha, no dia em que já não dá, lê o que quer. A impressora deitou a frase numa tira, *Abrir a dois.*, e o Simão recortou-a com a tesoura dos alunos e colou-a ao canto. Por cima, a marcador vermelho, nas maiúsculas com que em junho escrevera «NÃO» num disco: PARA QUANDO JÁ NÃO DER.

A Joana fechou a aba com fita-cola e assinou por cima, de um lado ao outro, para que ninguém a abrisse sem se ver.

Era ali que ele podia dizê-lo. O envelope estava fechado; a noite ainda não. Bastavam três frases: um anúncio no jornal, um homem sentado naquela cadeira a olhar para o frigorífico, seiscentos euros. *Não escolhas a parte que soa melhor.*

Não disse. Não foi esquecimento, nem falta de tempo. Ele contava tudo, e sabia exatamente quantas coisas lhe contara naquela noite: todas menos uma. Escolheu essa, e soube que escolhia.

— Fica comigo — disse a Joana, e dobrou o envelope ao meio para lhe caber na mala. — Em Almada ninguém procura.

Às oito, ouviu-a descer a escada. Lá em baixo, o Clio pegou à primeira.

* * *

O email chegou às oito e doze. Ele ainda estava à janela, com a chávena fria na mão, a ver o barco largar para o Cais do Sodré com meia dúzia de pessoas de sábado lá dentro, e o portátil fez o som pequeno que fazia o correio.

Vinha do endereço do Marr, o mesmo de setembro. Não tinha assunto nem texto, nem uma assinatura, nem o nome de quem o mandava, que não fazia falta. Tinha um anexo.

Abriu-o.

Uma porta de vidro martelado, à noite, numa rua da Cova da Piedade, com um candeeiro e um fio de telefone. Por cima, uma janela acesa, com uma cortina de renda corrida até meio. Conhecia a renda. Conhecia, por trás dela, a mancha cor de laranja do oleado. Na rua, à volta, não havia mais nenhuma janela acesa. Quem tirara aquilo não tivera pressa.

Foi às propriedades do ficheiro, como um físico vai sempre aos rótulos. *19/11/2015, 20:14.* Não precisou de calendário. Era uma quinta-feira.

Às oito e catorze daquela quinta-feira, ele estava do lado de dentro daquela luz, a comer sopa.
