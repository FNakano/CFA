# História

## 2020-10-06-141025

> A escolha de organização do *hardware* contribui para que os membros da equipe dediquem-se ao que se interessam, o que contribui para ter relações pessoais melhores e o sucesso do projeto.

Fui consultado por dois colegas sobre a viabilidade de construir um conjunto de LEDs, cujo padrão de acendimento representaria emoções. A seleção de emoções seria feita através de uma página web aberta em um navegador. Um desse colegas tinha/tem experiência com programação e Arduino.

Na época eu já havia experimentado com um servidor web e um LED, e com LEDs endereçáveis. Isto para mim era evidência suficiente para dizer que o projeto era viável, embora não soubesse quanto tempo seria necessário para concluí-lo.

Uns dias depois tivemos nova reunião em que percebi (ou me mostraram) que seriam muitos LEDs, formando padrões elaborados. Preocupei-me pois, para mim, havia três fontes de incerteza:

- conexão wifi
- implementar os padrões de acendimento
- energia para os LEDs.

Éramos dois programadores. Meu colega tinha mais interesse nos padrões de acendimento que nas outras partes e na integração delas. Seria muito proveitoso para todos se houvesse uma forma de dividir em partes fracamente acopladas. Passei uns dias até encontrar a solução:

- Os LEDs seriam controlados por um Arduino. Meu colega desenvolveria os padrões, cada um em um método. Usaria Arduino, Arduino IDE, teria liberdade de montar os LEDs como quisesse e programar como preferisse;
- Eu cuidaria da infraestrutura wifi/web, em que usaria ESP8266, e 'puxei para mim' o planejamento das partes e interconexões;
    - a comunicação entre Arduino e ESP8266 tinha várias soluções possíveis. Neste caso particular usei I2C.
- Nosso outro colega definiria aspectos visuais ligados à disposição dos LEDs e à página web.
- Os três juntos, em reuniões, executaríamos as interconexões e testes gerais;

Para nossa felicidade, nossa equipe organizou-se bem por adaptação às iniciativas de cada indivíduo (o tal do jogo de cintura, ou, sistemas auto-organizados). Entregamos no prazo. É um caso de sucesso.

Hoje, analisando o caso, reforçando que é uma percepção particular sobre a escolha de dividir em partes fracamente acopladas, posso dizer com segurança:

- não foi a escolha de menor gasto com materiais, mas permitiu aproveitar melhor a capacidade de trabalho disponível.
- teve o resultado esperado: desenvolvimento mais ágil, sem 'regiões críticas', execução da interconexão aconteceu como planejado, testes aconteceram como planejado.

[Painel flexível de LEDs - achei enquanto estava escrevendo o texto acima](https://pt.aliexpress.com/item/33018595434.html)


