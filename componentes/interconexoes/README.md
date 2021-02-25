# Interconexões

Frequentemente recebo placas de sensores sem as barras de pinos soldadas (foto, placa acima). Infelizmente os contatos não se estabelecem se apenas colocarmos os pinos nas ilhas (foto, placa abaixo). Se o caso é esse, o que dá menos trabalho é soldar a barra de pinos, ou pedir para alguém fazer.

![alt text](h2.jpg)

Existe uma variedade de componentes para conectar eletricamente outros componentes.

Na foto abaixo: 

- à esquerda conector Sindal, frequentemente usado para conectar chuveiro à rede elétrica. As três linhas horizontais de dois parafusos são, cada uma, um contato, os fios a conectar são inseridos pelas laterais, os pararfusos devem ser afrouxados para inserir os fios e apertados para firmar os fios e a conexão. Os outros dois furos são usados para fixar fisicamente o conector em uma caixa ou placa;
- no alto, azuis, conectores parafusados usados em módulos de relé. Os parafusos são afrouxados para permitir a conexão pela lateral e apertados para fixar a conexão;
- em baixo dos conectores parafusados, placa de circuito impresso tipo trilha. As trilhas são de cobre e interconectam as ilhas (furos). Nas ilhas são inseridos e soldados terminais de componentes;
- em verde com ilhas metalizadas, uma placa de circuito impresso tipo ilha. As conexões entre as ilhas são soldadas.
- abaixo, barras de pinos (headers) e barra de conectores. Cada pino corresponde a um contato. Essas barras são soldadas às placas de circuito impresso para conectar circuitos de diferentes placas. Os arduinos UNO e MEGA trazem soldadas barras de conectores, o arduino nano e o Node* trazem soldadas barras de pinos. O suporte plastico dos pinos derrete com a temperatura do ferro de solda, o que dificulta (inviabiliza) usar a barra de pinos sem que ela esteja apoiada numa placa de circuito impresso.
- no centro da foto, branco com traços vermelhos e azuis um protoboard. É uma placa de contatos (como os da barra de conectores), usada para agilizar a construção de protótipos para teste. Referências:
    - [O que é, como é construído (desmontagem), como usar,...](https://portal.vidadesilicio.com.br/protoboard/)
    - [como usar (site robocore)](https://www.robocore.net/tutoriais/como-utilizar-uma-protoboard)
    - [o que é - slides no site da UEL](http://www.uel.br/pessoal/ernesto/arduino/00_Protoboard.pdf)
    - [wikipedia](https://pt.wikipedia.org/wiki/Placa_de_Ensaio)

![interconexões](IMG_20201017_121308263.jpg)

## Soldar barras de pinos

Quando for soldar, nao aqueça o pino por muito tempo pois o plástico (preto) derrete muito fácil e o pino fica torto em relação aos outros, ou se destaca da barra (com o característico cheiro de plástico derretido).

Também, numa barra, quando soldar uma sequência de pinos, dê um tempo entre uma solda e outra, para o plástico esfriar e não derreter.

Barras de pinos soldadas muito inclinadas em relação ao plano da placa podem gerar falta de espaço: O conjunto de placas não encaixa (porque uma placa atrapalha o encaixe da outra), ou o conjunto não cabe na caixa (porque tem uma placa torta que faz o conjunto não caber na caixa). Fora isso, não deve haver maiores problemas. Por via das dúvidas e das mudanças, procure soldar as barras de pinos na posição certa (tem manha para isso). Na foto abaixo, a barra de pinos da placa da esquerda está (razoavelmente) perpendicular à placa, como costuma se esperar. Na placa da direita ela está suficientemente 'torta' para ser fonte potencial de problemas de espaço.

![alt text](torto.jpg)

A manha: quando for soldar uma barra de pinos, comece soldando o pino de alguma das extremidades (um só!). Espere o plástico esfriar, veja se precisa acertar (raramente fica bom de primeira). Se precisar acertar, aqueça o pino novamente (e rapidamente) e acerte a inclinação. Outras plaquinhas, suportes, etc. podem ser úteis para apoiar a placa que vai ter a barra de pinos soldada. Na foto abaixo usei um espelho de caixa de luz como apoio. Depois que a barra estiver acertada e bem apoiada na placa, solde o restante dos pinos (sempre com o cuidado de não derreter o plástico da barra).

![alt text](apoio.jpg)


## Derivações

Em circuitos elétricos existe a noção de hierarquia em função da capacidade de corrente, tensão ou outras características. Esta noção induz a existência de condutores principais e condutores secundários. 

A conexão de um condutor secundário a um condutor principal é chamada derivação. O 'gato' é uma derivação, geralmente inesperada, indesejada ou fora das regras.

Derivações podem ser feitas desencapando um segmento do condutor principal e soldando ou enrolando o condutor secundário. Isto é simples quando o condutor principal é suficientemente resistente, como um fio de 2.5mm^2.

![derivação em fio de 2.5](/projetos/ControlarTomadaPelaInternet/IMG_20201011_162053124.jpg)

Já em jumpers, geralmente fio 26 AWG (American Wire Gauge), aprox. 0,13mm^2, cortar o isolamento sem cortar o fio pode ser difícil...

![derivação em fio 26 AWG](/projetos/ControlarTomadaPelaInternet/IMG_20201012_153949868.jpg)

Uma solução é construir distribuidores com headers soldados em placas de circuito impresso.

![distribuidor](/projetos/ControlarTomadaPelaInternet/IMG_20201012_154010890.jpg)

Conversor de bitola de fio: <https://www.areaseg.com/awg.html>

