# CFA
Computação Física e Aplicações

## Apresentação

A quem ler este trabalho, gostaria de agradecer a visita e desejar boa leitura.

Gostaria, também, de avisar que, a intenção é que este trabalho evolua continuamente, o que, na minha opinião, o caracteriza como um protótipo, um produto mínimo, por isso (sempre) incompleto. Peço que avise se houver aqui algum texto que você considere impreciso, incompleto, ou injusto. (SP, 6 de outubro de 2020).

Esta é uma coleção de assuntos, conteúdos, perguntas e respostas que surgiram, ou que percebi que poderiam ser melhor trabalhadas, nas ocasiões em que ministrei a disciplina do título. A partir desta página, é possível chegar a todas as outras, e, na falta de página mais adequada para anotar algum assunto, este vem para cá. No contexto de projetos, este trabalho é o projeto que visa detalhar assuntos, conteúdos, perguntas e respostas que surgiram durante a preparação e execução das aulas da disciplina.

Minha intenção com este material é fornecer modelos testados de projetos e entregas, referências básicas sobre materiais e ferramentas, um pouco dos modelos teóricos que, combinados, fornecem justificativas para escolhas que fiz no planejamento da disciplina, compõe o conteúdo inicial e podem (devem) ser usados por quem cursar a disciplina. No contexto das consequências imediatas, espero que este material lhes permita direcionar tempo e esforço para o que não está resolvido aqui.

Alguns assuntos que surgiram são muito interessantes e extrapolam (o que eu considero) conteúdos de disciplina pois envolvem escolhas feita no planejamento e teste dos formatos e conteúdos que o ministrante entrega e que o aluno entrega durante a disciplina. Sumariamente, as idéias e experiências sobre organização de equipes, documentação de projetos, gerenciamento da disciplina o conteúdo da discilina: objetivos, conteúdo, material disponível, entregas e seu formato,...

Desejo-lhes 'boa disciplina', com mais momentos gratificantes que frustrações, aprendendo muito, e, com sucesso no final!

## Limitações do texto

Este texto objetiva apresentar conceitos e as referências que suportam esses conceitos. Não é intenção apresentar alternativas para as teorias apresentadas, nem fazer revisão de toda a literatura sobre algum assunto.

Há informação parcialmente estruturada e/ou parcialmente detalhada. Em alguns tópicos há estrutura, mas não há detalhamento. É uma meta consolidar estrutura e detalhamento.

Sugestões de ajustes para aumentar a precisão do texto são bemvindas.

À medida em que este texto for aperfeiçoado, serão agregadas referências pertinentes.

## Agradecimentos (Reconhecimentos) gerais

Obrigado a todos que contribuiram para minha formação e contribuem para minha atuação.

## Agradecimentos (Reconhecimentos) específicos

Obrigado a Isabel Italiano, Luciano Araújo, João Marcicano pelo conhecimento compartilhado e trabalho em conjunto.

(2023-09-06) Obrigado a [Giane](https://github.com/Anemaygi) e a [Otávio](https://github.com/bambans) pelas contribuições e ao [PET-SI](http://www.each.usp.br/petsi/) por várias iniciativas, como o OWLficinas.


## Como navegar neste repositório

Caso esteja interessado na documentação de componentes e ferramentas, pode navegar diretamente para a respectiva pasta.

Os componentes são divididos em categorias funcionais: atuadores, controladores, interconexões, protocolos, sensores e vestíveis;

Os programas, no momento, são app Inventor, arduino IDE, fritzing, Linux.

Os projetos completos, no momento, são:
1. [Relógio Conectado](projetos/RelogioConectado), 
2. [Relógio V1](projetos/RelogioV1), 
3. [Sensor meteorológico](projetos/SensorMeteorologico).
1. [Funcionalidades Recorrentes](projetos/FuncionalidadesRecorrentes), 
2. seu sub-projeto [Servidor de Arquivos](projetos/ServidorDeArquivos)
3. [Tomada conectada](projetos/ControlarTomadaPelaInternet)
3. [Prototipagem com Witty board](projetos/PrototipagemWitty)
3. [ESP32 Crossover](projetos/ESP32Crossover)
4. [ESP32-CAM](projetos/ESP32-CAM)
5. [Extensor/Repetidor WiFi](projetos/ExtensorWiFi)
6. [Extensor com botão](projetos/ExtensorComBotao)
6. [Sensor meteorológico com ESP32 DevKit](projetos/SensorMeteorologico-ESP32)
7. [Suporte para "janela" de texto rolável com display OLED SSD 1306](/projetos/DisplayRolavel)
8. [Programando ESP em Python](/projetos/ProgramandoESPEmPython)


Estes são projetos incompletos - em andamento ou abortados
1. [Suporte de peito para dispositivos](projetos/suportePeitoCostas)
2. [Color Timer](projetos/colorTimer)
3. [Usar celular como câmera IP que emula uma webcam no Linux](/projetos/webcam)

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

... ou em projetos do [OWLficinas](#OWLficinas) ...

... ou em projetos apresentados na disciplina no oferecimento corrente ou nos anteriores...

### 2023

- [GuitarHand - Luva com sensores nos dedos](https://github.com/Fabriciolk/GuitarHand)
- [Medidor de corrente elétrica](https://github.com/rodrigo-birocchi/ESP32-medidor-eletricidade)
- [Tamagochi remixed](https://github.com/edufiedler/AndreEduardoEzequiel)
- [MeshNetGame](https://github.com/ViniciusHenriq1402/Projeto-CFA)
- [WebCar](https://github.com/vitormrts/webcar)
- [e-Plant](https://github.com/jribeiroabrahao/ep-cfa-usp)


### 2022

[Jaqueta para proteção pessoal](https://github.com/Raposo4/jaqueta_protecao_pessoal)

[Brinquedo vestível](https://github.com/AdrianoFA/WearableGenius)

[Módulo de segurança para malas e mochilas](https://github.com/IgorAugst/Mochila)

[EcoPee](https://github.com/bambans/EcoPee)

[SMAC - Sistema de Monitoramento para Assentos de Cadeiras de Rodas](https://github.com/Anemaygi/SMAC/tree/master/projeto)

[Projeto Protetor Solar](https://github.com/T16K/ACH2157)

[Baby Alarm](https://github.com/SystemGuuh/Computacao-Fisica/tree/main/BabyAlarm)

[Dispositivo de Sobrevivência](https://github.com/raphancusp/DispositivoDeSobrevivencia)

[Seta e alerta de som para corredores, ciclistas e motociclistas](https://github.com/tio-bryan/wearables-2022)

[Bolt - tornozeleira inteligente](https://github.com/JadnoABS/bolt)

### 2021

[UOLI](https://github.com/artcupelli/uoli)

[Dragão do tempo](https://github.com/dudagarcia/environment-meter-dragon)

[Injeção eletrônica](https://github.com/TsuHub/ComputacaoFisica)

[Reconhecedor de máscara com ESPCAM e Amazon IoT](https://github.com/JgSeike/cf-each)

[Campainha com câmera e assistência remota usando WebThings](https://github.com/danielyujiyamada/CFA-Projetos/projects/1)

[TwitchCar](https://github.com/rokrz/CompFisi_Nakano)




### Anteriores

[PopLaserCat](https://poplasercat.wordpress.com): Exercitador de gatos. A maioria dos gatos permanecem por um bom período de tempo sozinhos em casa esperando seu dono chegar. Tudo bem que os gatos são independentes, brincam e realizam suas atividades vitais sozinhos, mas entretê-los enquanto estão sozinhos seria uma boa maneira de deixar os bichinhos e seus donos mais felizes. Assim, pensamos em uma forma inovadora de entreter o pet com laser, utilizando sensor, de forma que ele possa se divertir mesmo em um momento que estiver sozinho.

[Arduvias](http://arduvias.weebly.com/): Medição de fluxo de veículos. Neste projeto temos como objetivo monitorar a passagem de veículos em vias de acesso de grandes avenidas durante um período de tempo, para retirar dados do fluxo de movimentação do local e mostrar para os motoristas qual o acesso menos congestionado. Com essa monitoração pretendemos passar um olhar expandido de acessos das grandes avenidas de cidades com trânsito intenso, a fim de melhorar o fluxo de carro na cidade.


[Cuidador de pessoas](https://projetocoxinha.tumblr.com.br): Medidor de batimentos cardíacos, glicose, assistente digital com comunicação bluetooth.

[Jardim automatizado](http://jardimautomatizado.blogspot.com.br): A ideia é criar um automatizador, usando Arduino que regue as plantas automaticamente e que as ilumine de acordo com o horário que foi programado para tal.

[Xilofone Arduino](http://xilofonearduino.wordpress.com): Xilofone com garrafas PET

[Damas++](https://drive.google.com/open?id=0B7wgT77H3SLxT3hfVnNvcmswbmIwV2ZaY0Y3Yld4ZnVNMi1n): Jogo de damas com assistência do Arduino.

[EACHian Smart Mirror](http://eachiansmartmirror.blogspot.com.br/): Nosso objetivo é a construção de um espelho "inteligente", que exiba informações úteis ao usuário na própria superfície espelhada. Nossa ideia é motivada pela área de IoT (Internet of Things), que cresce a passos largos nos últimos anos, e que são fundamentais para popularizar ainda mais a tecnologia no uso cotidiano.

[Site da disciplina até 2018](http://ach2157.blogspot.com/)

## OWLficinas

- https://github.com/biatrizch/ESP32-Projeto-Final
- https://github.com/RafaCaminag/CaixaDeMusica/tree/main

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

## Alternativas para programar ESP32

- Espressif Integrated Development Framework (IDF);
- Arduino Integrated Development Environment (IDE) (https://arduino.cc);
- Micro Pyton (https://www.micropython.org);
- ESPruino (https://www.espruino.com/ESP32#firmware-updates);

## Altenrnativas para programar Arduino UNO/MEGA/NANO

- Arduino IDE;

## Fontes de energia

Na minha opinião, a falha no fornecimento de energia a um dispositivo é uma das causas de mau-funcionamento (comportamento/funcionamento inesperado) mais difíceis de detectar pois:

- Eventos com a mesma causa tem diferentes efeitos, mesmo para um particular dispositivo (ex. o particular Arduino UNO que alguém possui);
- Algumas causas são eliminadas com um simples manuseio (ex. um conector levemente desencaixado que com um pequeno movimento permite que energia suficiente chege ao dispositivo);
- Os efeitos são difíceis de reproduzir, logo, a estratégia de provocar o mesmo tipo de erro para, então, depurar o sistema, geralmente não é eficaz;
- Frequentemente requer conhecimento mais detalhado sobre eletro-eletrônica (ex. entender os diagramas esquemáticos do dispositivo, identificar componentes, entender a documentação (datasheet, manuais,...) de cada componente.

Isto posto, vamos compartilhar experiências

### Pilha fraca

Geralmente as pilhas são desconectadas do circuito e mede-se a tensão entre os polos - a corrente drenada da pilha é quase zero, como num circuito aberto. Por isso também chama-se teste *em aberto*. Se a tensão medida está perto da tensão nominal, admite-se que elas estão boas.

... mas esse teste falha em um caso: Quando as pilhas estão fracas, elas podem ter carga suficiente para apresentar tensão perto da nominal em um teste em aberto, mas a tensão da pilha cai bastante quando a corrente drenada da pilha é significativa.

É difícil apresentar uma demonstração crível de um argumento tão qualitativo, por outro lado, aproveitando um acidente, consegui uma demonstração que me parece muito razoável: <a id="2023-02-14-161757" href="/projetos/Teste3V/README.md">Teste3V</a>

### Fio corroído

Frequentemente componentes de baixo custo têm esse custo porque foram recuperados de equipamentos descartados ou porque estão no estoque (da cadeia de venda) há muito tempo. Nos dois casos, os elementos do componente podem deteriorar. Por exemplo, os fios e conectores podem oxidar.

Em várias ocasiões usei pilhas para fornecer energia, mas o circuito não funcionava. As pilhas eram recém adquiridas, mas comecei a acreditar que estavam sem carga e que o vendedor das pilhas havia me enganado. Mas, mesmo trocando as pilhas (sair do lab, comprar, voltar), o circuito não funcionou. Depolis de mais uns minutos checando o circuito notei que os contatos do suporte com as pilhas estavam oxidados. Girei (várias vezes) as pilhas no suporte para gastar a camada de óxido, então o circuito funcionou.

Noutra ocasião com pilhas, o circuito não funcionava. Desta vez era mau contato entre o ilhós e o fio. Explico: o contato do suporte no lado positivo da pilha é um ilhós. Geralmente ele é prensado no corpo plástico do suporte junto com o fio que conectará o suporte ao resto do circuito. Essa prensagem foi feita na parte do fio que estava encapada, então não havia contato elétrico.

Ainda com pilhas, recuperei um suporte de pilhas de um aparelho quebrado e montei o circuito, que não funcionava. Desta vez tinha um multímetro à mão e vi que não havia tensão entre os fios do suporte. Liguei as pontas de prova do multímetro nos contatos (ilhós e mola) do suporte e havia tensão. Tirei as pilhas e testei a continuidade (elétrica) dos fios. Um deles estava interrompido. MAS o contato parecia bem prensado. Quando fui desencapar um pouco mais do fio para continuar testando, usei um alicate e puxei a capa. O condutor saiu "inteiro" da capa. Sobre o condutor, pó branco e verde. O fio sofreu corrosão e estava interrompido, mas, por fora, parecia bem.

### Porta USB - limites conforme a norma

### Carregadores "turbo" (micro USB)

### Carregadores USB-C


## Cabos, mau-contato e efeitos experimentados

### Cabos de energia e cabos de dados

### Conector micro USB (V8)

### Conector USB (tipo A)

