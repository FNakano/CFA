## Limitações do texto

Este texto objetiva apresentar os conceitos e as referências que suportam esses conceitos. Não é intenção apresentar teorias e definições alternativas, nem fazer revisão de toda a literatura sobre o assunto.

Sugestões de ajustes para aumentar a precisão do texto são bemvindas.

À medida em que este texto for aperfeiçoado, serão agregadas referências pertinentes.

# Circuitos Elétricos

Processos, em determinadas condições, podem ser modelados por simplificações da teoria geral. No desenvolvimento do conhecimento científico, é frequente que modelos para determinadas condições sejam propostos, temporalmente, antes dos modelos gerais, e, baseado nos modelos simplificados, por um processo de generalização, o modelo geral seja proposto.

No contexto de um conjunto de componentes elétricos interconectados e com ao menos um caminho fechado, onde os fenômenos elétricos de interesse estão restritos ao que ocorre nos componentes e inteconexões, o modelo pode ser simplificado de tal forma que, na opinião do autor, pouco se parece com o modelo geral.

Um circuito elétrico é definido como um conjunto de componentes elétricos e suas interconexões, com ao menos um caminho fechado por onde pode circular corrente elétrica.

Componente elétrico é um componente que modifica a passagem de corrente de forma significativa para quem observa (estuda, analisa, constrói) o circuito. Os componentes de interconexão conectam componentes, sem outro efeito significativo. 

**nota**: esta definição é diferente da proposta no site Brasil Escola <https://brasilescola.uol.com.br/fisica/circuitos-eletricos.htm>

> Circuito elétrico é uma ligação de elementos, como geradores, receptores, resistores, capacitores, interruptores, feita por meio de fios condutores, formando um caminho fechado que produz uma corrente elétrica.

Meu comentário sobre **produz corrente elétrica** é que esta expressão induz o leitor a imaginar que o caminho fechado *gera* corrente elétrica. Poderia ser mais preciso: *é percorrido por uma corrente elétrica*

a definição que dei também é diferente da apresentada na wikipedia <https://pt.wikipedia.org/wiki/Circuito_el%C3%A9trico>.

> Um circuito elétrico é a ligação de elementos elétricos,[1] tais como resistores, indutores, capacitores, diodos, linhas de transmissão, fontes de tensão, fontes de corrente e interruptores, de modo que formem pelo menos um caminho fechado para a corrente elétrica.

... pois dá a entender que o circuito é a ligação, e que os componentes não fazem parte do circuito.

## Dipolos

Dipolos são componentes com dois terminais. Componentes com mais terminais podem ser construídos com dipolos, ou, aproximações úteis dos componentes podem ser construídas como uma associação de dipolos.

## Geradores

Geradores, quando conectados em um circuito, provocam movimento de cargas (ié corrente elétrica) no circuito.

O gerador mais simples é um dipolo. Pode ser uma pilha, a tomada de parede, uma bateria de automóvel.

É útil notar que em todos os casos, abstrai-se a construção do gerador, interessando somente a tensão ou a corrente entre os terminais do gerador. Por isso, para análise elétrica do circuito, dizer *um gerador de 5V* ou *um gerador de 1A* é suficiente. Isto tem consequências na forma como nos comunicamos, por exemplo: 'Esta tomada é 110V" geralmente é informação suficiente.

### Curto-circuito

Curto-circuito é o nome dado à situação em que os terminais do gerador são diretamente conectados.

Nesta situação, a corrente que passa pelos terminais é máxima. Em pouco tempo o gerador e a interconexão esquentam, podendo fundir, pegar fogo, explodir. O gerador é inutilizado.

No modelo usual (ingênuo) para circuitos elétricos, um gerador em curto entregaria corrente infinita. Isto não ocorre em casos reais. Pode-se usar isto como um exemplo de caso em que o modelo não corresponde adequadamente ao processo.

Para *makers*: a porta USB de um computador bem construído tem circuitos cuja função é proteger a porta contra curto-circuito e sobrecarga, MAS, os cicuitos podem falhar e os computadores podem não ser tão bem construídos. Por segurança, evite curto-circuitar ou sobrecarregar a porta USB.

## Receptores (componentes em geral)

### Resistor

Resistor é o receptor mais básico.

#### Resistência elétrica

A fim de simplificar, vamos limitar os circuitos àqueles mais comuns, por exemplo o da lâmpada da sala, há um gerador e um receptor, lembre que os fios que conectam lâmpada à tomada são parte do circuito. Depende de você avaliar se são ou não significativos e isto depende do seu objetivo nesse estudo. Aqui deseja-se apresentar a Lei de Ohm.

Diferentes materiais deixam as cargas passar através deles com maior ou menor facilidade. Em geral metais deixam as cargas passar com mais facilidade, plásticos e borrachas deixam as cargas passar com menos facilidade. Essa característica dos materiais é chamada resistência elétrica, geralmente denotada por R e medida em Ohms).

### Lei de Ohm

Em uma grande variedade de materiais (mas não em todos!), tensão, corrente e resistência relacionam-se pela fórmula V=R*I (Lei de Ohm). 
   
Experimentando com esta fórmula, num mesmo material, ou seja, a resistência é a mesma, submetido a uma determinada tensão, passa uma determinada corrente. Se dobrarmos a tensão, a corrente dobra também.

Usando a fórmula de outra forma possível, diferentes materiais submetidos à mesma tensão deixam passar diferentes correntes. Quanto maior a resistência elétrica, menor a corrente, quanto menor a resistência elétrica, maior a corrente. Materiais com "baixa" resistência elétrica são chamados condutores elétricos e material com "alta" resistência elétrica são chamados isolantes elétricos.


#### Resistores comerciais, código de cores, tolerância, potência máxima


### LED

### Prática: Acender um LED

#### A teoria 

Condições extremas de funcionamento (como queimar um LED).

    Em geral peças são fabricadas para funcionar em determinadas condições e suportam algumas condições extremas. Os manuais das peças trazem essas condições. Em componentes eletrônicos, as condições extremas estão em um quadro marcado "Absolute Maximum Ratings". Nessas condições o componente pode queimar ou ter sua vida útil reduzida significativamente.

    Em um manual de um LED (https://www.vishay.com/docs/83171/tlur640.pdf) tem-se Vr=6V, ou seja, se esse LED for ligado com os terminais invertidos, a maior tensão que ele suporta é 6V. If=20mA acima de 20mA constante o LED pode queimar ou ter sua vida útil reduzida significativamente. Ifsm=1A caso receba um pico de corrente acima de 1A o LED pode queimar. Pv=60mW a potência sobre o LED deve ser no máximo 60mW. É muito provável que este componente queime imediatamente se conectado com a polaridade certa diretamente na USB (por exemplo os pinos 5V e GND do arduino) pois a USB fornece 5V e até 500mA.

### Entradas e Saídas

   Outro exemplo: um pino do arduino configurado para saída digital suporta até 5V e 40mA (https://playground.arduino.cc/Main/ArduinoPinCurrentLimitations). Em tese, conectar um LED diretamente ao pino de saída vai queimar ou o LED ou o pino do arduino ou os dois. Não se recomenda fazer isto MAS...
... os pinos do arduino (especificamente do ATMega328 têm proteção contra sobrecorrente, o que geralmente evita que a saída do arduino e o LED queimem.

   Componentes robustos como arduino e boas placas USB têm circuitos que evitam que sofram danos. Usar um hub USB entre o computador e o arduino ou outro componente pode trazer um pouco mais de segurança.

## Relações Básicas

## Componentes em geral

### Pilha







### Circuitos Digitais






