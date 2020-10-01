# CFA
Computação Física e Aplicações

## Apresentação

Neste momento, acredito que a característica mais importante deste texto é que ele é um protótipo, um produto mínimo, por isso incompleto, talvez contendo afirmações 'injustas', que talvez necessitem de ajuste contínuo que, espero, venham através de colaborações e sugestões (SP, 20 de agosto de 2020).

Esta é uma coleção de assuntos, perguntas e respostas que surgiram, ou que percebi que poderiam ser melhor trabalhadas, nas ocasiões em que ministrei esta disciplina.

Os assuntos são mais relacionados à eletricidade, eletrônica e computação, que são os que conheço melhor. 

Há muitos trechos de texto que trazem a opinião ou a experiência do autor na execução de alguma tarefa. São relatos de experiência, recomendações ou orientações que podem ser usados enquanto não há algo melhor. Na opinião do autor, *quem faz escolhe o que e como fazer*.

Gostaria de encorajar os leitores a usar os ítens da coleção como referencia nos relatórios de projeto da disciplina, ou mesmo em projetos mais amplos e ambiciosos, bem como aproveitar o formato de documentação dos projetos, apresentados aqui como exemplos, como inspiração para a construção de seus próprios relatórios.

## Limitações do texto

Este texto objetiva apresentar conceitos e as referências que suportam esses conceitos. Não é intenção apresentar alternativas para as teorias apresentadas, nem defender uma posição (apresentar argumentos, fazer análise crítica), nem fazer revisão de toda a literatura sobre o assunto.

Por enquanto há informação, parte estruturada, parte não estruturada. Em alguns tópicos há estrutura, mas não há detalhamento. É uma meta consolidar estrutura e detalhamento.

Sugestões de ajustes para aumentar a precisão do texto são bemvindas.

À medida em que este texto for aperfeiçoado, serão agregadas referências pertinentes.

## Agradecimentos (Reconhecimentos) gerais

Obrigado a todos que contribuiram para minha formação e contribuem para minha atuação.

## Agradecimentos (Reconhecimentos) específicos

Obrigado a Isabel Italiano, Luciano Araújo, João Marcicano pelo conhecimento compartilhado e trabalho em conjunto.

## Organização da informação

Este texto é o ponto de partida. As ramificações são:

- componentes;
    - contém informação sobre os componentes utilizados nos projetos;
- [modelos](modelos/README.md);
    - contém modelos para documentação para esta disciplina;
- programas;
    - contém informação sobre os programas, ou, ferramentas, utilizadas nos projetos e na documentação
- projetos;
    - contém as aplicações, algumas feitas para testar os modelos.

Os componentes são divididos em categorias funcionais: atuadores, controladores, interconexões, protocolos, sensores e vestíveis;

Os [modelos](modelos/README.md) estão em fase final de elaboração.

Os programas, no momento, são app Inventor, arduino IDE, fritzing, Linux.

Os projetos, no momento, são Relógio Conectado e Relógio V1.

Pode interessar dar uma olhada em projetos de Iniciação Científica relacionados ao tema da disciplina:

- [Rede de sensores - 2018](https://github.com/AlexandreZelante/Rede-de-sensores-ic)
- [ImageCV](https://github.com/camilabezerril/ImageCV)
- [Actímetro](https://github.com/snorlara/Actimetro)
- [Outra rede de sensores (ainda não público](https://github.com/FNakano/SensoresRemotos)


Pode ser mais rápido encontrar uma página usando o [mapa do repositório](tree.md).

... ou procurar alguma dúvida similar à sua (esta seção será ampliada e as explicações melhor embasadas):

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

