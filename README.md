# CFA
Computação Física e Aplicações

## Apresentação

A quem ler este trabalho, gostaria de agradecer a visita e desejar boa leitura.

Gostaria, também, de avisar que, a intenção é que este trabalho evolua continuamente, o que, na minha opinião, o caracteriza como um protótipo, um produto mínimo, por isso (sempre) incompleto. Peço que avise se houver aqui algum texto que você considere impreciso, incompleto, ou injusto. (SP, 6 de outubro de 2020).

Esta é uma coleção de assuntos, conteúdos, perguntas e respostas que surgiram, ou que percebi que poderiam ser melhor trabalhadas, nas ocasiões em que ministrei a disciplina do título. A partir desta página, é possível chegar a todas as outras, e, na falta de página mais adequada para anotar algum assunto, este vem para cá. No contexto de projetos, este trabalho é o projeto que visa detalhar assuntos, conteúdos, perguntas e respostas que surgiram durante a preparação e execução das aulas da disciplina.

Minha intenção com este material é fornecer modelos testados de projetos e entregas, referências básicas sobre materiais e ferramentas, um pouco dos modelos teóricos que, combinados, fornecem justificativas para escolhas que fiz no planejamento da disciplina, compõe o conteúdo inicial e podem (devem) ser usados por quem cursar a disciplina. No contexto das consequências imediatas, espero que este material lhes permita direcionar tempo e esforço para o que não está resolvido aqui.

Alguns assuntos que surgiram são muito interessantes e extrapolam (o que eu considero) conteúdos de disciplina pois envolvem escolhas feita no planejamento e teste dos formatos e conteúdos que o ministrante entrega e que o aluno entrega durante a disciplina. Sumariamente, as idéias e experiências sobre organização de equipes, documentação de projetos, gerenciamento da disciplina o conteúdo da discilina: objetivos, conteúdo, material disponível, entregas e seu formato,...

Desejo-lhes 'boa disciplina', com mais momentos gratificantes que frustrações, aprendendo muito e, com sucesso no final!

## Limitações do texto

Este texto objetiva apresentar conceitos e as referências que suportam esses conceitos. Não é intenção apresentar alternativas para as teorias apresentadas, nem fazer revisão de toda a literatura sobre algum assunto.

Há informação parcialmente estruturada e/ou parcialmente detalhada. Em alguns tópicos há estrutura, mas não há detalhamento. É uma meta consolidar estrutura e detalhamento.

Sugestões de ajustes para aumentar a precisão do texto são bemvindas.

À medida em que este texto for aperfeiçoado, serão agregadas referências pertinentes.

## Agradecimentos (Reconhecimentos) gerais

Obrigado a todos que contribuiram para minha formação e contribuem para minha atuação.

## Agradecimentos (Reconhecimentos) específicos

Obrigado a Isabel Italiano, Luciano Araújo, João Marcicano pelo conhecimento compartilhado e trabalho em conjunto.

## Como navegar neste repositório

Caso esteja interessado na documentação de componentes e ferramentas, pode navegar diretamente para a respectiva pasta.

Os componentes são divididos em categorias funcionais: atuadores, controladores, interconexões, protocolos, sensores e vestíveis;

Os programas, no momento, são app Inventor, arduino IDE, fritzing, Linux.

Os projetos completos, no momento, são:
1. [Relógio Conectado](projetos/RelogioConectado/README.md), 
2. [Relógio V1](projetos/RelogioV1/README.md), 
3. [Sensor meteorológico](projetos/SensorMeteorologico/README.md).
1. [Funcionalidades Recorrentes](projetos/FuncionalidadesRecorrentes/README.md), 
2. seu sub-projeto [Servidor de Arquivos](projetos/ServidorDeArquivos/README.md)
3. [Tomada conectada](projetos/ControlarTomadaPelaInternet/README.md)
3. [Prototipagem com Witty board](projetos/PrototipagemWitty/README.md)
3. [ESP32 Crossover](projetos/ESP32Crossover/README.md)
4. [ESP32-CAM](projetos/ESP32-CAM/README.md)
5. [Extensor/Repetidor WiFi](projetos/ExtensorWiFi/README.md)
6. [Extensor com botão](projetos/ExtensorComBotao/README.md)
6. [Sensor meteorológico com ESP32 DevKit](projetos/SensorMeteorologico-ESP32/README.md)

Caso queria saber como é a disciplina, você pode estar interessado em: 

- [visão geral da disciplina](admin/README.md);
    - justificativas;
    - critérios;
    - eventos;
- [modelos de documentação](modelos/README.md)
        - por quê documentar?
        - o que documentar?
        - como documentar?
        - modelo para uso em repositório no github.

[mapa do repositório](tree.md).

Pode interessar dar uma olhada em projetos de Iniciação Científica relacionados ao tema da disciplina:

- [Rede de sensores - 2018](https://github.com/AlexandreZelante/Rede-de-sensores-ic)
- [ImageCV - 2019-2020](https://github.com/camilabezerril/ImageCV)
- [Actímetro - 2019-2020](https://github.com/snorlara/Actimetro)

... ou em projetos apresentados na disciplina em oferecimentos anteriores...

[PopLaserCat](https://poplasercat.wordpress.com): Exercitador de gatos. A maioria dos gatos permanecem por um bom período de tempo sozinhos em casa esperando seu dono chegar. Tudo bem que os gatos são independentes, brincam e realizam suas atividades vitais sozinhos, mas entretê-los enquanto estão sozinhos seria uma boa maneira de deixar os bichinhos e seus donos mais felizes. Assim, pensamos em uma forma inovadora de entreter o pet com laser, utilizando sensor, de forma que ele possa se divertir mesmo em um momento que estiver sozinho.

[Arduvias](http://arduvias.weebly.com/): Medição de fluxo de veículos. Neste projeto temos como objetivo monitorar a passagem de veículos em vias de acesso de grandes avenidas durante um período de tempo, para retirar dados do fluxo de movimentação do local e mostrar para os motoristas qual o acesso menos congestionado. Com essa monitoração pretendemos passar um olhar expandido de acessos das grandes avenidas de cidades com trânsito intenso, a fim de melhorar o fluxo de carro na cidade.


[Cuidador de pessoas](https://projetocoxinha.tumblr.com.br): Medidor de batimentos cardíacos, glicose, assistente digital com comunicação bluetooth.

[Jardim automatizado](http://jardimautomatizado.blogspot.com.br): A ideia é criar um automatizador, usando Arduino que regue as plantas automaticamente e que as ilumine de acordo com o horário que foi programado para tal.

[Xilofone Arduino](http://xilofonearduino.wordpress.com): Xilofone com garrafas PET

[Damas++](https://drive.google.com/open?id=0B7wgT77H3SLxT3hfVnNvcmswbmIwV2ZaY0Y3Yld4ZnVNMi1n): Jogo de damas com assistência do Arduino.

[EACHian Smart Mirror](http://eachiansmartmirror.blogspot.com.br/): Nosso objetivo é a construção de um espelho "inteligente", que exiba informações úteis ao usuário na própria superfície espelhada. Nossa ideia é motivada pela área de IoT (Internet of Things), que cresce a passos largos nos últimos anos, e que são fundamentais para popularizar ainda mais a tecnologia no uso cotidiano.

[Site da disciplina até 2018](http://ach2157.blogspot.com/)

## FAQ

- [Vou levar choque mexendo na placa controladora (Arduino, NodeMCU, ESP8266, ESP32, ...?](eletricidade.md#Choque-elétrico)
- Como posso estragar uma placa controladora?
    - Uma resposta muito precisa não é possível. A resposta vaga é: se a placa não estiver recebendo energia (não estiver ligada), o principal motivo para dano é mecânico: flexionar, torcer, vibrar até interromper o circuito. O mesmo com água: imergir em água, quando desligado, não costuma causar dano. A recuperação pode ser feita secando bem a placa. Caso ela seja ligada molhada, ou molhada enquanto ligada, a chance de dano é maior. Outra forma é conectar um pino de *saída* diretamente a um polo da fonte. Embora na maioria dos controladores os pinos tenham circuitos de proteção, a proteção não é permanente e falha em algum momento. Também conectar a uma tensão mais alta que a permitida. A máxima tensão permitida é informação que está na especificação (*datasheet*) da placa.
- O computador em que conecto a placa controladora pode ser danificado se eu errar alguma conexão na placa controladora?
    - a porta USB dos computadores tem proteção contra sobrecarga mas isto não garante de forma absoluta que a porta USB não seja danificada. Isto é mais provável quando se injeta energia através da porta USB. Por exemplo conectando uma bateria à USB, o que pode acontecer caso o Arduino esteja conectado a pilhas e à USB simultaneamente.
- Tenho uma sequência de 200 LEDs em paralelo em uma fita. Da metade do comprimento para a frente, em relação à ponta que liguei na fonte, o brilho é menor. Qual o motivo? Como fazer para o brilho ser mais uniforme?
    - Isto pode ser explicado usando para o condutor (o fio ou fita) um modelo mais detalhado que o do condutor ideal, com resistência nula. Neste modelo, chamado *Segunda Lei de Ohm*, que é uma aproximação melhor do comportamento do condutor, a resistência elétrica do condutor depende do material que é feito, do comprimento e da área da secção transversal (ou bitola). Isto explica por quê os LEDs mais próximos da fonte têm brilho maior que os LEDs mais distantes da fonte (distância medida em metros de fio). Uma interpretação possível (para deixar menos árido) é que o fio ou fita 'não está dando conta' de conduzir toda a corrente necessária. A solução é acrescentar condutores (fios) com o menor comprimento e maior bitola possível, da fonte até outros pontos do fio ou fita em que os LEDs estão conectados. Isto equivale a aumentar a bitola do fio.
- a placa controladora só funciona conectada a um computador?
    - a placa controladora funciona (executa o programa armazenado mais recentemente) se receber energia, seja pela porta USB (por exemplo com um carregador de celular ou *battery pack*, seja por um conector específico (por exemplo os J4 de algumas placas Arduino). Frequentemente (mas não sempre) é possível fornecer energia através de pinos. Para saber se é realmente possível, melhor **estudar os diagramas esquemáticos da placa que você escolheu**. No arduino UNO, o 5V ou Vcc podem receber 5V.
- Recebi um sensor sem os pinos soldados. Encostar as ilhas da placa de um sensor aos pinos do controlador é uma 'boa maneira' de ligar o sensor ao controlador?
    - Na minha experiência, não. Detalhes em <contatos.md>.
- Há algum projeto completo neste site?
    - [Relógio Conectado](projetos/RelogioConectado/README.md)
- Onde posso aprender como usar git e github?
    - [Tente aqui: explicação no repositório de um projeto de IC](https://github.com/camilabezerril/ImageCV/tree/master/Documentos/sobreGit)
- Há modelos de documentação de projetos neste site?
    - [Modelos e Justificativas para os modelos](modelos/README.md)

A leitura linear do texto apresenta os conceitos na sequência de construção: dos mais elementares, combinando-os, até chegar a aplicações que foram usadas ou apresentadas na disciplina.

## Soluções para gerar este documento 


**nota** Como gerar a árvore de arquivos

<pre><font color="#4E9A06"><b>fabio@fabio-PORTEGE-M400</b></font>:<font color="#3465A4"><b>~/Documentos/Documentos/ACH2157/git/CFA</b></font>$ tree -H . &gt;../tree.md
</pre>

**nota** No commit, o git shell pediu para eu me identificar.

<pre><font color="#4E9A06"><b>abio@fabio-PORTEGE-M400</b></font>:<font color="#3465A4"><b>~/Documentos/Documentos/ACH2157/git/CFA</b></font>$ git commit -m &quot;Estrutura inicial e algum texto&quot;

*** Please tell me who you are.

Run

  git config --global user.email &quot;you@example.com&quot;
  git config --global user.name &quot;Your Name&quot;

to set your account&apos;s default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got &apos;fabio@fabio-PORTEGE-M400.(none)&apos;)
<font color="#4E9A06"><b>fabio@fabio-PORTEGE-M400</b></font>:<font color="#3465A4"><b>~/Documentos/Documentos/ACH2157/git/CFA</b></font>$ ls .git
<font color="#3465A4"><b>branches</b></font>  description  <font color="#3465A4"><b>hooks</b></font>  <font color="#3465A4"><b>info</b></font>  <font color="#3465A4"><b>objects</b></font>      <font color="#3465A4"><b>refs</b></font>
config    HEAD         index  <font color="#3465A4"><b>logs</b></font>  packed-refs
</pre>

**nota** git não põe pastas vazias no repositório remoto, mesmo que existam no repositório local.

**nota** testando com termux no android.

