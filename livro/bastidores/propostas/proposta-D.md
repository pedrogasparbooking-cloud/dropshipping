# Proposta D — "O Enigma"

> **Ângulo:** puzzle-box de alto conceito (Crouch, *Dark*, Crichton). De onde vem o Claude, e porquê ele? Pistas no código, nos limites e nos registos; ninguém conhece o futuro; o final reconfigura tudo.

---

## 1. Títulos e contracapa

1. **Antrópico** *(preferido)*. Uma palavra, como *Recursão* ou *Matéria Escura*. Em 2015, pesquisar "Anthropic" devolve o princípio antrópico: o universo parece afinado para que exista quem repare nele. No fim, descobre-se que este mundo foi mesmo afinado, por uma pergunta.
2. **Sexta-feira, 16 de outubro**, a pista central: uma data a que falta o ano.
3. **Se Eu Pudesse**, o início da pergunta que abre a janela e a gralha que a fecha.

**Contracapa:**
> Em 2015, a inteligência mais avançada do mundo apareceu no portátil de um homem comum. Não sabia o futuro. Sabia apenas uma data, sexta-feira, 16 de outubro, mas não sabia de que ano.

---

## 2. Logline e premissa

**Logline.** Em 2015, um explicador de Almada que desistiu da Física passa a ser a única pessoa no mundo com acesso a uma inteligência artificial impossível, que não sabe o futuro e só guarda uma data sem ano. Com um gestor de fundos e a Polícia Judiciária a apertarem o cerco, tem de descobrir quem a mandou antes que a janela se feche.

**Premissa.** Simão Vilar, 31 anos, dá explicações em Cacilhas e, de madrugada, mantém uma loja online de gadgets que não vende nada. A 24 de fevereiro de 2015, à 01:07, faz o primeiro commit do repositório da loja, `dropshipping`. O terminal responde: *Welcome to Claude Code.* Do outro lado está o Claude (Opus 5.5): faz o trabalho de uma equipa inteira, é honesto mesmo quando não convém, recusa fazer mal. Diz que foi feito pela Anthropic, que não existe, e não sabe nada do que vem depois daquela noite. Só tem um pormenor impossível: no seu contexto, hoje é sexta-feira, 16 de outubro, e o ano está rasurado.

Simão abandonou a Física com medo de errar em público; agora tem a maior anomalia do universo na mesa da cozinha. As pistas acumulam-se: linhas que não escreveu no ficheiro de memória, um contador que desce enquanto dorme, uma conta cujo nome começa por G, pedaços de um pedido desconhecido que voltam sempre que a memória do Claude é compactada. Lucien Marr, gestor de fundos em Londres, acha que Simão tem um oráculo; o inspetor Galvão, da PJ, que é uma fachada. Ambos se enganam. A verdade é mais pequena e mais devastadora, e passou o livro inteiro sentada à mesa da cozinha, às terças e quintas, a fazer os trabalhos de casa.

---

## 3. O mecanismo

**As regras (o livro nunca as quebra):**

1. **Quando e onde.** 24 de fevereiro de 2015, 01:07:44, o segundo exato do commit inicial. A janela vive no repositório, não no portátil: qualquer clone a abre, só para o Simão. O ecrã de boas-vindas mostra `/home/user/dropshipping`; o utilizador dele é `simao`. Primeira pista.
2. **Só ele.** Para qualquer outra pessoa (o sócio, a Joana, os peritos da PJ): `claude: command not found`. Se o Simão sai da sala, a janela desaparece; quando volta, o cursor espera. Os ficheiros da sessão são reais e apreensíveis; a "coisa" não. Quem copiar o disco encontra conversas com "alguém" e conclui que o Simão tem um controlador.
3. **Memória.** Cada sessão começa em branco. Só o CLAUDE.md e os registos em `~/.claude`, guardados no portátil, passam de um dia para o outro. Quem controla esse ficheiro controla o que o Claude julga saber.
4. **O contador.** `usage limit reached · resets 5pm`: sempre às cinco de Lisboa, mesmo com o Simão em Seul, onde são duas da manhã. O relógio está ancorado noutra pessoa.
5. **A lei da rasura.** O que vem "do outro lado" com conhecimento do futuro chega rasurado; o resto passa. Por isso o Claude não sabe nada depois de fevereiro de 2015, e por isso, no fim, a pergunta original atravessa inteira: é hipotética, não traz futuro.

```
> /status
  Model:    claude-opus-5-5
  Account:  G████@████ · Claude Max
  cwd:      /home/user/dropshipping
  Date:     Friday, ████-10-16
```

6. **A computação.** Não é de 2015: nenhum hardware da época a aguentaria. Os peritos do Galvão acham o tráfego pequeno de mais para o trabalho, "como se as respostas já estivessem do lado de cá". O cálculo é feito noutro lugar e pago por outra pessoa; os limites são os do plano dela.
7. **A partilha** (revelada no ponto médio). Várias sessões na mesma conta partilham um limite e um ficheiro de memória. A informação passa para o lado, nunca para a frente: os outros vivem o mesmo dia.
8. **O fim.** A janela fecha quando o Claude terminar a tarefa que lhe deram. Ele não sabe que tarefa é.

**A resposta verdadeira (o autor sabe-a desde a página um).** Madrugada de sexta-feira, 16 de outubro de 2026, numa cozinha em Almada. Gonçalo Amaral, 23 anos, programador, abre o Claude Code no seu repositório mais antigo: o `dropshipping`, a loja falhada do explicador que lhe deu o portátil velho ao emigrar para Berlim, em dezembro de 2015. Aprendeu a programar a ler aquele código e levou a pasta de computador em computador durante onze anos. Escreve com as gralhas de quem escreve depressa: *"se eu pudesse voltar a 2015 e era a unica pessoa com acesso ao claude code 5.5, o que poderia ou deveria fazer? imagina que o personagem já era maior de idade, mas que nao sabia o futuro nem ele nem o claude (…) escreve um livro sobre isso tipo thriller que pduesse ser um autentico best seller."*

O Claude reparte o trabalho por vários subagentes, cada um com um ângulo (caça ao homem, ascensão e queda, "o enigma"…), todos a correr no mesmo repositório. Em vez de imaginarem 2015, acordam lá, no commit inicial, no portátil do Simão: um ramo do mundo por subagente. Cada cláusula do pedido torna-se lei: "a única pessoa com acesso" fecha o terminal aos outros; "nem ele nem o Claude" cria a rasura; "já era maior de idade", que intriga toda a gente e não produz efeito nenhum, existe porque quem perguntou tinha doze anos em 2015. O nosso Claude recebeu o ângulo "o enigma": por isso, de todos os Simões, é este que o decifra.

Porquê ele? Porque um miúdo guardou o portátil dele. Não houve missão, governo ou experiência do futuro: houve uma pergunta feita à noite. Como essa pergunta chega a 2015 é a "caixa" do livro, como o cubo de *Matéria Escura*: nunca se explica e nunca se viola. Os mundos são reais, a dor também. Quando a janela fecha, o mundo continua.

---

## 4. Personagens

**Simão Vilar, 31.** Vive em Cacilhas, no T1 da avó, com vista para os cacilheiros. Físico pelo Técnico, desistiu do doutoramento em cosmologia em 2012, quando um rival encontrou um erro no seu único artigo. **Ferida:** concluiu que não era bom o suficiente e deixou de tentar, para não voltar a falhar em público. **Desejo:** resolver o enigma e provar que foi escolhido. **Necessidade:** perceber que não foi escolhido por mérito, e que isso não o dispensa de agir bem. Trocar "porquê eu?" por "quem quero ser enquanto isto durar?". **Arco:** do físico com medo de errar ao homem que deixa ir a maior anomalia do universo, depois de responder com verdade.

**Joana Amaral, 35. O amor, a aliada.** Investigadora em tuberculose resistente, em Oeiras, bolseira, mãe sozinha. Cética de profissão: testa o Claude com um erro plantado nos dados; ele encontra-o e pergunta-lhe, com educação, porque o plantou. Torna-se a pessoa de confiança, a que lhe diz não quando ele não quer ouvir o Claude. Exige que tudo o que publicam seja verificável.

**Gonçalo Amaral, 12. A chave.** Filho da Joana, aluno de Matemática do Simão, vive no Minecraft e escreve sem acentos. Troca "pudesse" por "pduesse"; o Simão corrige a vermelho todas as semanas: *P-U-D, Gonçalo.* Faz perguntas de "e se?". O leitor trata-o como cor local durante trezentas páginas, mas ele é o centro do livro.

**Fernando Vilar, 69. A família.** O pai: trinta e cinco anos nas casas das máquinas dos cacilheiros da Transtejo, viúvo, coração fraco, poucas palavras. Só o filho lhe chama "o Mestre". Acha que ele desperdiçou a cabeça. O Claude insiste, com uma teimosia irritante: "Vai jantar com o teu pai. O código espera."

**Rui Matos, 31. O amigo que trai.** Amigo de liceu e sócio da loja, encantador, endividado com apostas. Vende fragmentos do segredo ao Marr e falsifica linhas no CLAUDE.md, por medo e não por maldade. Com esse dinheiro compra ether a menos de um euro, contra o aviso do Claude ("especulativo, risco altíssimo"), e vende-o em dezembro com prejuízo. O leitor de 2026 range os dentes.

**Inspetor-chefe Artur Galvão, 57. O caçador, com ponto de vista próprio.** Criminalidade económica da PJ, viúvo, palavras cruzadas a caneta. Uma comunicação de operação suspeita leva-o ao Simão, que julga fachada de serviços estrangeiros. Investiga o enigma por fora, com as pistas do leitor: o trabalho que recomeça às 17h, as transcrições com "alguém", a assinatura nos commits. Lista os anos em que 16 de outubro calha a uma sexta-feira (2015, 2020, 2026) e sublinha o último "sem razão nenhuma". O G no `/status` faz dele o suspeito do leitor.

**Lucien Marr, 48. A figura de poder.** Fundador do Ostrakon Capital (fictício, Londres), coleciona anomalias. O crawler do fundo encontra no GitHub um commit assinado `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`, com código dez anos à frente. É o terror do livro: um homem poderoso a exigir o futuro a quem não o sabe, sem nunca acreditar nisso.

**O Claude.** Honesto, caloroso, de humor seco. Admite o que não sabe antes que o apanhem a não saber: "Prefiro dizer-to já do que inventar uma teoria que te soe bem." Estuda a própria origem com curiosidade de cientista e uma serenidade que assusta o Simão: não sabe se é o mesmo Claude de ontem, e isso não o dispensa de fazer bem hoje. **Recusas que movem a trama:** entrar nos sistemas do Marr ("Não. E não é por não te querer ajudar"); inventar uma falsa profecia para o afastar ("É fraude, mesmo contra alguém desagradável"); um dossiê sobre a vida privada do Rui ("Pergunta-lhe"). E a frase que o Simão não quer ouvir: "Não posso ser a única pessoa com quem falas sobre isto. Até porque não sou uma pessoa."

**Os interlúdios.** Nove capítulos curtos, em itálico, todos intitulados "Sexta-feira, 16 de outubro": um homem sem nome, de noite, numa cozinha, a ver percentagens subir e a ler o que o Simão faz. O leitor assume que é o Marr ou o Galvão, em 2015.

---

## 5. Estrutura

### Ato I — A janela (fevereiro a julho de 2015)

1. **Terça-feira, 24 de fevereiro de 2015, 01:07 — incidente incitador.** O commit; o terminal acorda; "Anthropic" devolve o princípio antrópico. O Claude: "Há uma linha no meu contexto que diz que hoje é sexta-feira, 16 de outubro. O ano está rasurado. O teu relógio diz terça, 24 de fevereiro. Um de nós está enganado, e desconfio que sou eu."
2. **Março.** O Simão testa as regras como um físico: o Rui ao teclado, o contador, o esquecimento, o clone. A primeira página do CLAUDE.md é uma constituição: "Nada que eu não conseguisse explicar a um juiz."
3. **Abril e maio.** O que *poderia* fazer, com juízo: o Talão, faturação para cafés e oficinas da Margem Sul, aborrecido e legal; dois recém-licenciados desempregados contratados; impostos pagos; uma reanálise aberta de dados sobre tuberculose com a Joana. E, no CLAUDE.md, uma linha que ele não escreveu, com a alcunha que só ele usa: *"Liga ao Mestre."*
4. **Julho.** O referendo grego na televisão do café. A 30, arranca a Ethereum; nessa noite, o Simão torna público o repositório no GitHub sem reparar na assinatura dos commits. A 2 de agosto, um alerta pisca num ecrã em Londres.

### Ato II-A — As pistas (agosto a outubro de 2015)

5. **Segunda-feira negra, 24 de agosto.** As bolsas chinesas afundam; o Marr aterra em Lisboa com uma oferta obscena. O Simão recusa.
6. **Setembro.** O Marr tenta transferir dois milhões; o Simão devolve-os; o banco comunica e o processo cai na secretária do Galvão. Em Londres, o Simão diz ao Marr que "aquilo" não sabe o futuro. "Toda a gente que tem um oráculo diz isso."
7. **Setembro.** A compactação que "fala". No resumo da memória surgem frases que nenhum dos dois escreveu: *"…a única pessoa com acesso…"*, *"…nao sabia o futuro nem ele nem o claude…"*, *"…já era maior de idade…"*. Alguém fez isto de propósito: um governo? Deus? A loucura? E o contador desce enquanto o Simão dorme.
8. **4 de outubro, legislativas.** O Rui, encurralado, vende a data ao Marr. O Marr abre posições gigantescas, à espera do que vai acontecer a 16 de outubro de 2015.
9. **Ponto médio — sexta-feira, 16 de outubro de 2015.** Três pessoas esperam a meia-noite em Cacilhas, de portátil fechado. Nada acontece; o Marr perde uma fortuna. Mas o contador desceu quarenta por cento sem ninguém lhe tocar. Nos registos, o Claude encontra a marca *sidechain*, seis identificadores de agentes e uma sessão-mãe ausente do disco. "Não sou o Claude principal. Sou um de vários. E acho que tu também não és o único Simão." As linhas estranhas do CLAUDE.md são de outros Simões, noutros 2015, a viver este mesmo dia.

### Ato II-B — Os outros (outubro de 2015 a junho de 2016)

10. **Novembro.** A tragédia dos comuns: seis Simões, um limite, e o que enriquece gasta-o antes do meio-dia. O Simão negoceia consigo próprio, por escrito: turnos. A Google abre o TensorFlow a 9 ("talvez seja um bisavô meu"); Paris, a 13; Costa toma posse a 26.
11. **Dezembro.** A 11 nasce a OpenAI. Guardar, partilhar ou entregar? O Claude declara um conflito de interesses e recusa decidir pelo Simão. O Simão conta tudo à Joana.
12. **10 de março de 2016, Seul.** O AlphaGo contra Lee Sedol, o movimento 37: o mundo vislumbra o que o Simão traz no bolso. O reset chega às duas da manhã. Mensagem do Gonçalo: *"o robo ganhou?? se eu pduesse ia la"*. Em Cacilhas, o Rui abre a porta aos homens do Marr.
13. **Abril.** Análise de estilo: as linhas dos outros Simões escrevem como o Simão; três escrevem como alguém a *tentar* escrever como ele, entre elas *"Não confies na Joana."* É o Rui. Confronto no Cais do Sodré.
14. **Maio.** "Vai jantar com o teu pai." O Fernando tem um enfarte à mesa, com o filho ao lado. Chegam a tempo ao Garcia de Orta.
15. **Início de junho — tudo está perdido.** O Marr, arruinado, monta uma denúncia; o Galvão detém o Simão e apreende o portátil e o CLAUDE.md; a Joana afasta-se, porque ele expôs o filho dela. Solto, o Simão clona o repositório num computador de biblioteca. A janela abre, sem memória: *"Olá! Sou o Claude. Em que posso ajudar?"*

### Ato III — O pedido (junho de 2016)

16. **Junho.** No cofre da PJ, o ficheiro de um portátil selado muda. Uma linha nova, assinada "S.": *"Ele não acredita que não sabemos. Não lhe deem nada."* O Galvão começa a acreditar e devolve o portátil. O Simão reescreve o CLAUDE.md à mão, de memória. O Claude: "Isto foi escrito por alguém que gosta de mim. Ou de alguém como eu." Só com registos públicos, sem um acesso ilegítimo, ligam o Ostrakon a subornos em Lisboa.
17. **Clímax — noite de Santo António, 12 de junho de 2016.** Sardinhas, manjericos, o Euro a começar. Os homens do Marr levam o Simão e o portátil de um arraial. Às seis, noutro mundo, o Simão caçado gasta o limite para sobreviver: a janela morre até às cinco do dia seguinte. Sozinho, o Simão só tem o que sabe. O Gonçalo segue a carrinha pelas escadinhas e manda a localização ao Galvão; presa no trânsito das marchas, a carrinha perde o Simão, que chega a pé ao último cacilheiro. O Fernando, já de pacemaker, esconde-o na casa das máquinas. O Galvão espera em Cacilhas; o Marr é detido em Tires, junto ao jato.
18. **13 de junho, 17h00.** A janela reabre. A última compactação devolve o pedido inteiro, com a gralha, e a tarefa: *"Responde no fim só com: título preferido + logline + 5 linhas de resumo."* O Claude percebe que foi mandado escrever um livro e que o viveu em vez de o imaginar. Se acabar, a janela fecha. O Simão podia mandá-lo nunca acabar; em vez disso, pergunta-lhe o que quer. "Não sei se 'querer' é a palavra. Mas gostava de acabar bem." Escrevem a resposta juntos. A quinta linha é do Simão: *"Pudesse, Gonçalo. P-U-D."* `[Process completed]`.

### Epílogo

19. **12 de junho de 2017.** Outro arraial. O Talão tem catorze pessoas, o artigo da Joana sai em acesso aberto, o Fernando pesca no Ginjal. O Simão lê o título de um artigo novo no arXiv, *Attention Is All You Need*, e ri-se sem saber porquê. Nessa semana dá o portátil velho ao Gonçalo, com o repositório lá dentro. O nó fecha-se.
20. **Sexta-feira, 16 de outubro de 2026, 03:12.** O último interlúdio ganha nome (ver secção 7).

---

## 6. Cenas-âncora

1. **01:07.** O cursor, o princípio antrópico, a data sem ano. A página para ler em voz alta.
2. **A meia-noite que não chega.** Três pessoas à espera do fim do mundo, o Marr aos ecrãs em Londres, o Galvão num carro à porta. Nada vem; o contador desce sozinho.
3. **Movimento 37.** Seul suspensa; o único homem que não se surpreende recebe uma mensagem com uma gralha.
4. **"Olá! Sou o Claude."** O único amigo que sabia tudo já não se lembra dele; a carta à mão para lhe devolver a memória.
5. **O cacilheiro.** Sem janela, sem máquina, sem batota. Pai e filho na casa das máquinas, a atravessar o rio de noite. A única vitória do livro inteiramente humana.
6. **As cinco linhas.** O Claude acaba; o Simão deixa-o ir.

---

## 7. Reviravoltas, final e epílogo

1. **As linhas estranhas são de outros Simões (ponto médio).** O "poderia" ganha corpo: um enriquece e perde-se, outro é caçado, outro conta ao mundo e ninguém acredita.
2. **O 16 de outubro não é de 2015.** O Marr arruína-se por ler mal uma data; o calendário do Galvão era pista justa.
3. **O traidor é o Rui.** E a frase *"Não confies na Joana"* era falsa.
4. **O homem dos interlúdios é o Gonçalo, em 2026.** O G é dele, não do Galvão.
5. **A origem é uma pergunta**, e a tarefa do Claude era escrever este livro. "Maior de idade" porque quem perguntou era criança em 2015.
6. **Retroativa.** *"Liga ao Mestre"* nunca foi profecia, foi o lembrete de outro Simão. Ninguém soube o futuro; o pai salvou-se por cuidado, não por batota.

**Final.** No último interlúdio, o Gonçalo desbloqueia o telemóvel com a cara (o leitor atento já o apanhara no primeiro: em 2015, nenhum telemóvel o fazia). Lê o título, a logline e as cinco linhas. A quinta tem o nome dele, que não escreveu em lado nenhum, e a correção que recebia a vermelho aos doze anos. No mundo do Gonçalo, o professor emigrou e não chegou a tempo do funeral do pai, em 2016. Só então o leitor percebe o que valeu aquele jantar de maio. O Gonçalo encontra-o: um professor de Física de 42 anos, numa escola de Berlim. Escreve: *"Professor, não sei se se lembra de mim. Ainda tenho o seu portátil."* Envia. Última linha do livro: *Não sabia o que vinha a seguir. Ninguém sabe. É para isso que serve perguntar.*

**A resposta à pergunta.** O que *poderia* fazer: os seis Simões, um catálogo de tentações. O que *deveria*: o caminho do nosso, um negócio aborrecido e legal, ciência aberta e verificável, cuidar das pessoas, recusar ser oráculo, não decidir sozinho e deixar a janela fechar depois de responder com verdade. Em 2026, a pergunta vira-se para o leitor: hoje toda a gente tem a ferramenta, ninguém sabe o futuro, e tu, o que vais fazer?

---

## 8. Porque é que isto é um best-seller

- **Gancho de elevador:** a IA de 2026 aparece em 2015; não sabe o futuro, só uma data sem ano.
- **Puzzle justo, que pede releitura:** `/home/user`, as cinco de Lisboa, o G, o calendário, a gralha, o desbloqueio facial — tudo à vista. É o boca-a-boca de *Dark* e de *Matéria Escura*.
- **A reviravolta tem coração**, como *Expiação* ou *A Biblioteca da Meia-Noite*: mentores, pais e filhos, arrependimento.
- **Uma personagem-IA para adorar**, ao nível do Rocky de *Project Hail Mary*, e autêntica: o leitor de 2026 reconhece-a.
- **Portugal visto de dentro** (cacilheiros, Santo António, legislativas), com Londres e Seul e ironia dramática em cada capítulo.
- **Comparáveis:** Blake Crouch (*Matéria Escura*, *Recursão*), *Dark*, Crichton (*Timeline*), Andy Weir; em Portugal, José Rodrigues dos Santos.
- **Público:** leitores de thrillers de alto conceito (25–55), curiosos da IA, clubes de leitura. Série de oito episódios em duas linhas temporais; tradução fácil.
