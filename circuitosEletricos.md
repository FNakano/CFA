## Limitações do texto

Este texto objetiva apresentar conceitos sobre circuitos elétricos úteis na disciplina CFA. Não é intenção apresentar teorias e definições alternativas, nem fazer revisão de toda a literatura sobre o assunto.

Sugestões de ajustes para aumentar a precisão do texto são bemvindas.

À medida em que este texto for aperfeiçoado, serão agregadas referências pertinentes.


# Circuitos Elétricos

## Modelos em geral, eletricidade e conceitos

É possível controlar o ambiente (contexto) onde ocorrem processos de maneira que o processo no ambiente possa ser modelado por simplificações da teoria geral. No desenvolvimento do conhecimento científico, é frequente que modelos para determinadas condições sejam propostos, temporalmente, antes dos modelos gerais, e, baseado nos modelos simplificados, por um processo de generalização, seja proposto um modelo geral.

O (um?) modelo geral sobre eletricidade nos informa que todos os corpos no universo contém cargas elétricas (mesmo que estas se anulem na construção do corpo como um todo). Cargas interagem entre si, mesmo a longas distâncias e através do vácuo. Essa interação é descrita pela teoria de campos escalares. A aplicação dessa teoria sobre (o fenômeno) eletricidade induz conceitos como diferença de potencial elétrico (também chamada tensão elétrica). Uma consequência imediata é que entre dois corpos pode haver diferença de potencial elétrico. Outra é que se há um único corpo, não há diferença de potencial.


 

No contexto de um conjunto de componentes elétricos interconectados aonde os fenômenos elétricos de interesse estão restritos ao que ocorre nos componentes e conexões, o modelo pode ser simplificado e, na opinião do autor, entendido com menos dificuldade por uma audiência mais ampla.

Componente elétrico é um componente que modifica a passagem de corrente de forma significativa para quem observa (estuda, analisa, constrói) o circuito. Os componentes de (inter)conexão (ou, simplesmente, conexões) conectam componentes, sem outro efeito significativo (idealmente, têm resistência, capacitância e indutância nulos). Existe uma grande variedade de componentes e de conexões.

Circuito elétrico é definido como um conjunto de componentes elétricos conectados entre si.

A maioria dos circuitos elétricos de interesse contém ao menos um caminho fechado. Por este pode circular corrente elétrica.

Neste contexto valem modelos baseados em hipóteses de conservação de energia como as [Leis de Kirchoff](https://en.wikipedia.org/wiki/Kirchhoff%27s_circuit_laws), que serão apresentada no momento oportuno.

**nota**: A definição de circuito elétrico apresentada é diferente da proposta no site Brasil Escola <https://brasilescola.uol.com.br/fisica/circuitos-eletricos.htm>

> Circuito elétrico é uma ligação de elementos, como geradores, receptores, resistores, capacitores, interruptores, feita por meio de fios condutores, formando um caminho fechado que produz uma corrente elétrica.

Meu comentário sobre **produz corrente elétrica** é que esta expressão induz o leitor a imaginar que o caminho fechado *gera* corrente elétrica. Poderia ser mais preciso: *é percorrido por uma corrente elétrica*

a definição apresentada também é diferente da apresentada na wikipedia <https://pt.wikipedia.org/wiki/Circuito_el%C3%A9trico>.

> Um circuito elétrico é a ligação de elementos elétricos,[1] tais como resistores, indutores, capacitores, diodos, linhas de transmissão, fontes de tensão, fontes de corrente e interruptores, de modo que formem pelo menos um caminho fechado para a corrente elétrica.

... pois dá a entender que o circuito é a ligação, e que os componentes não fazem parte do circuito.

## Sub-circuitos

Voltando à maioria dos circuitos de interesse, afirma-se que estes têm ao menos um caminho fechado onde a corrente circula. Esta definição permite que a união de vários caminhos fechados seja chamada *circuito*. Neste contexto, pode ser conveniente definir sub-circuitos como subconjuntos próprios dos caminhos de um circuito. Por exemplo, se um circuito tem cem caminhos fechados, pode-se usar *sub-circuito* para referir-se a dois desses cem caminhos.

## Curto-circuito

Curto-circuito é o nome dado à situação em que uma conexão (espúria) é acrescentada ao circuito, encurtando-o. A ocorrência de um curto-circuito pode danificar componentes.


O curto-circuito do gerador de energia (pilha, bateria, tomada, porta USB) pode ser especialmente perigoso.

Nesta situação, a corrente que passa pelos terminais é máxima. Em pouco tempo o gerador e a interconexão esquentam, podendo fundir, pegar fogo, explodir, ... 

A maioria dos (sub-)circuitos por onde passa a energia para alimentar circuitos conta com componentes de proteção (fusíveis, disjuntores, polyfuses, circuitos crowbar, ...).

Sugestão para *makers*: a porta USB de um computador bem construído tem circuitos cuja função é proteger a porta, e o computador, contra curto-circuito e sobrecarga, MAS, os cicuitos podem falhar e os computadores podem não ser tão bem construídos. Por segurança, evite curto-circuitar ou sobrecarregar a porta USB.

## Circuito aberto

É o nome dado à situação em que uma conexão é desfeita. A corrente elétrica deixa de passar por algum (sub-)circuito. Sua ocorrência também pode danificar componentes mas, na minha experiência, é mais fácil danificar componentes com curtos que abrindo circuitos.

São exemplos de circuitos abertos os aparelhos e circuitos domiciliares quando o interruptor está desligado, quando o fusível está queimado, quando o disjuntor está aberto, ...

Quando mede-se a resistência de um resistor com um ohmímetro, o resistor faz parte do circuito do qual o medidor faz parte. O circuito do ohmímetro sem o resistor é um circuito aberto.


## Símbolos, diagramas e linguagem

Representações são criadas para simplificar objetos e processos. Através delas é possível isolar as características que importam para uma determinada finalidade e abstrair, ié desprezar, as que não importam. Descrições, diagramas, desenhos, fotografias são representações. Estas permitem que pessoas comuniquem e elaborem sobre os objetos e processos. Existem representações definidas por normas seguidas pelas comunidades de indivíduos interessados no objeto/processo. É assim, também, com componentes, interconexões e circuitos elétricos.

Em circuitos elétricos, interessa apresentar por onde pode passar corrente. Nos componentes a corrente passa pelos terminais. Num componente, usualmente, cada terminal está conectado em alguma parte de seu circuito interno, por isso, terminais de um particular componente são eletricamente distintos, o que gera a necessidade de identificá-los para serem corretamente conectados externamente.

A fim de documentar e reproduzir um determinado circuito elétrico, é suficiente representá-lo pela lista (completa) de componentes utilizados e pela lista (completa) de conexões, que indica que terminais de que componentes são interconectados.

Outras representações são diagramas esquemáticos, desenhos em programas de computador, ... todas estas contém, explícita ou implicitamente, a lista de componentes e a lista de conexões.

## Dipolos

Dipolos representam componentes com dois terminais, sem maiores detalhes sobre o que é representado e qualidade da representação. Componentes com mais terminais podem ser representados como associações de dipolos, de acordo com o que for conveniente.

## Geradores

Geradores, quando conectados apropriadamente em um circuito, provocam movimento de cargas (ié corrente elétrica) no circuito.

A implementação de um gerador pode ser uma pilha, a tomada de parede, uma bateria de automóvel. Cada uma pode ser representada por um dipolo.

É útil notar que em todos os casos, abstrai-se a construção do gerador, interessando somente a tensão ou a corrente entre os terminais do gerador (dipolo). Por isso, para análise elétrica do circuito, dizer *um gerador de 5V* ou *um gerador de 1A* é suficiente. Isto tem consequências na forma como nos comunicamos, por exemplo: 'Esta tomada é 110V" geralmente é informação suficiente.

### Baterias e pilhas

Baterias são bem especificadas pela tensão que fornece e pela carga armazenada. A carga armazenada é medida em Ampére*hora (Ah). Uma bateria de carga de 1Ah fornece 1A durante 1 hora.  

## Receptores (componentes em geral) parte I

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

Este é um dos primeiros objetivos no aprendizado do uso de microcontroladores. É uma espécie de 'Olá Mundo'.

Três exemplos:

- <https://www.arduino.cc/en/Tutorial/BuiltInExamples/Blink>
- <https://brasilrobotics.blogspot.com/2011/02/pisca-led-o-primeiro-exemplo-para.html>
- <https://learn.adafruit.com/adafruit-arduino-lesson-2-leds/blinking-the-led>

A pergunta que não quer calar:

> Por quê em um exemplo o resisitor tem 220ohm, no outro 270ohm e no outro 1000ohm?

Resposta abaixo...

#### A teoria 

A intensidade de emissão (brilho) de um LED, dentro de uma certa faixa(!), é diretamente proporcional à corrente que passa por ele. 

1. Abaixo de um certo valor de corrente, nossos olhos não percebem o brilho do LED. Vamos convencionar que esse valor seja 1mA. 
2. Acima de um certo valor de corrente, o aumento no brilho torna-se imperceptível, e um pouco mais além, o LED queima.

##### Condições extremas de funcionamento (como queimar um LED).

Em geral peças são fabricadas para funcionar em determinadas condições e suportam algumas condições extremas. Os manuais das peças trazem essas condições. Em componentes eletrônicos, as condições extremas estão em um quadro marcado "Absolute Maximum Ratings". Nessas condições o componente pode queimar ou ter sua vida útil reduzida significativamente.

Em um manual de um LED (https://www.vishay.com/docs/83171/tlur640.pdf) tem-se Vr=6V, ou seja, se esse LED for ligado com os terminais invertidos, a maior tensão que ele suporta é 6V. If=20mA acima de 20mA constante o LED pode queimar ou ter sua vida útil reduzida significativamente. Ifsm=1A caso receba um pico de corrente acima de 1A o LED pode queimar. Pv=60mW a potência sobre o LED deve ser no máximo 60mW. É muito provável que este componente queime imediatamente se conectado com a polaridade certa diretamente na USB (por exemplo os pinos 5V e GND do arduino) pois a USB fornece 5V e até 500mA.

**Questão**: Para que valores de resistor, enxergamos o brilho do LED?
 
1. Se queremos enxergar o LED acender, sem queimá-lo, deduz-se das condições 1 e 2, que a corrente sobre o LED deve estar entre 1mA e 20mA.
2. Segundo o manual, um LED vermelho, na faixa de funcionamento, requer Vf=1,7V (esta aproximação é suficiente para o objetivo, mas existem formas mais acuradas de obter Vf);
3. A tensão que a porta USB fornece é 5V;
4. Então, pela lei das malhas, a tensão no resistor é Vr=5-1,7=3,3V;
5. Pela lei dos nós, a corrente no resistor é a mesma corrente no LED;
6. A lei de Ohm estabelece uma relação linear entre tensão e corrente, portanto só precisamos calcular os valores extremos. Os valores intermediários são obtidos por interpolação linear;
7. No extremo de mínima corrente, R=3,3V/1mA=3300ohm;
8. No extremo de máxima corrente, R=3,3V/20mA=165ohm;
9. Logo, **qualquer resistor entre 165ohm e 3300ohm serve para acender o LED, observadas as condições de funcionamento que convencionamos.**.


### Entradas e Saídas

Outro exemplo: um pino do arduino configurado para saída digital suporta até 5V e 40mA (https://playground.arduino.cc/Main/ArduinoPinCurrentLimitations). Em tese, conectar um LED diretamente ao pino de saída vai queimar ou o LED ou o pino do arduino ou os dois. Não se recomenda fazer isto MAS...
... os pinos do arduino (especificamente do ATMega328 têm proteção contra sobrecorrente, o que geralmente evita que a saída do arduino e o LED queimem.

   Componentes robustos como arduino e boas placas USB têm circuitos que evitam que sofram danos. Usar um hub USB entre o computador e o arduino ou outro componente pode trazer um pouco mais de segurança.

### Circuitos Digitais





#### Referências

- [For a Philosophy of Representation](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiWvb_Bzaf9AhVYLLkGHb26BMEQFnoECAoQAQ&url=https%3A%2F%2Fmdpi-res.com%2Fd_attachment%2Fproceedings%2Fproceedings-01-00857%2Farticle_deploy%2Fproceedings-01-00857.pdf%3Fversion%3D1513936465&usg=AOvVaw0-hfjXks1gvQE6cnJxXVAa)
- [Stoic Logic](https://en.wikipedia.org/wiki/Stoic_logic)
- [modus tollens](https://en.wikipedia.org/wiki/Modus_tollens)
- [modus ponens](https://en.wikipedia.org/wiki/Modus_ponens)
- [Philosophy portal](https://en.wikipedia.org/wiki/Portal:Philosophy)
- [wikipedia:Philosophy ](https://en.wikipedia.org/wiki/Philosophy)
- [what is a model](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiEmYTVz6f9AhWCs5UCHWrFD-kQFnoECAkQAQ&url=https%3A%2F%2Fwww.researchgate.net%2Fpublication%2F30814656_What_is_a_Model&usg=AOvVaw0yxXppDLxWVeEAZjlHHCvu)
- [models in science](https://plato.stanford.edu/entries/models-science/)
- [mathematical model](https://en.wikipedia.org/wiki/Mathematical_model)
- [conceptual model](https://en.wikipedia.org/wiki/Conceptual_model)
- [philosophy of science](https://en.wikipedia.org/wiki/Philosophy_of_science)
- [scientific modelling](https://en.wikipedia.org/wiki/Scientific_modelling)
- [model](https://en.wikipedia.org/wiki/Model)
- [representation theory](https://en.wikipedia.org/wiki/Representation_theory_(linguistics))
- [kr](https://en.wikipedia.org/wiki/Knowledge_representation_and_reasoning)
- [phenomenalism](https://en.wikipedia.org/wiki/Phenomenalism)
- [philosophy of mind](https://en.wikipedia.org/wiki/Philosophy_of_mind)
- [mental representation](https://en.wikipedia.org/wiki/Mental_representation)
- [representation](https://en.wikipedia.org/wiki/Representation)
- [representação (CC)](https://pt.wikipedia.org/wiki/Representa%C3%A7%C3%A3o_(ci%C3%AAncia_da_computa%C3%A7%C3%A3o))
- [teoria da representação](https://pt.wikipedia.org/wiki/Teoria_de_representa%C3%A7%C3%A3o)
- [representação (filosofia)](https://pt.wikipedia.org/wiki/Representa%C3%A7%C3%A3o_(filosofia))
- [representação](https://pt.wikipedia.org/wiki/Representa%C3%A7%C3%A3o)




