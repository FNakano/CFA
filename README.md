# CFA
Computação Física e Aplicações

## Apresentação

Neste momento, acredito que a característica mais importante deste texto é que ele é um protótipo, um produto mínimo, por isso incompleto, talvez contendo afirmações 'injustas', que talvez necessitem de ajuste contínuo que, espero, venham através de colaborações e sugestões (SP, 20 de agosto de 2020).

Esta é uma coleção de assuntos, perguntas e respostas que surgiram, ou que percebi que poderiam ser melhor trabalhadas, nas ocasiões em que ministrei esta disciplina.

Os assuntos são mais relacionados à eletricidade, eletrônica e computação, que são os que conheço melhor. 

Gostaria de encorajar os leitores a usar os ítens da coleção como referencia nos relatórios de projeto da disciplina, ou mesmo em projetos mais amplos e ambiciosos, bem como aproveitar o formato de documentação dos projetos, apresentados aqui como exemplos, como inspiração para a construção de seus próprios relatórios.

## Limitações do texto

Este texto objetiva apresentar conceitos e as referências que suportam esses conceitos. Não é intenção apresentar teorias e definições alternativas, nem fazer revisão de toda a literatura sobre o assunto.

Sugestões de ajustes para aumentar a precisão do texto são bemvindas.

À medida em que este texto for aperfeiçoado, serão agregadas referências pertinentes.

## Agradecimentos (Reconhecimentos) gerais

Obrigado a todos que contribuiram para minha formação e contribuem para minha atuação.

## Agradecimentos (Reconhecimentos) específicos

Obrigado a Isabel Italiano, Luciano Araújo, João Marcicano pelo conhecimento compartilhado e trabalho em conjunto.

## Organização da informação

Pode ser mais rápido encontrar uma página usando o [mapa do repositório](tree.md).

... ou procurar alguma dúvida similar à sua:

- [Vou levar choque mexendo na placa controladora (Arduino, NodeMCU, ESP8266, ESP32, ...?](eletricidade.md#Choque-elétrico)
- Como posso estragar uma placa controladora?
- O computador em que conecto a placa controladora pode ser danificado se eu errar alguma conexão na placa controladora?
- Tenho uma sequência de 200 LEDs em paralelo em uma fita. Da metade do comprimento para a frente, em relação à ponta que liguei na fonte, o brilho é menor. Qual o motivo? Como fazer para o brilho ser mais uniforme?
- a placa controladora só funciona conectada a um computador?
- Recebi um sensor sem os pinos soldados. Encostar as ilhas da placa de um sensor aos pinos do controlador é uma 'boa maneira' de ligar o sensor ao controlador?

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

