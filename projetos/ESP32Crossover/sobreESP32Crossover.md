# Crossover Placa de interface do wittyboard para programar ESP32.

## Motivação

A placa TTGO Display com ESP32 é cara, a placa ESP32-NodeMCU é grande e vem com os headers soldados. Existe uma placa TTGO Display com ESP32 e inteface serial separada, mas é cara também.

O wittyboard tem os circuitos de interface separados do ESP8266.

À primeira vista, a comunicação e o reset do ESP32 e do ESP8266 são iguais. É possível checar comparando os esquemáticos.

origem da figura abaixo: <https://www.instructables.com/id/Witty-Cloud-Module-Adapter-Board/>

![](sobreESPCrossover/FTNJHCRIYOQCBSN.jpg)

![esquemático do Node32s baixado de um link em esp32.net](sobreESPCrossover/Ai-Thinker_NodeMCU-32S_DiagramSchematic.png)

## Resultado

O circuito mínimo é apenas o ESP32 (detalhes no diário).

![circuito mínimo](sobreESPCrossover/IMG_20200905_170007003.jpg)

## Anotações

Achei um esquema bonitinho do wittyboard, consegui fazer uma proposta muito parecida funcionar no começo deste ano, mas apanhei dos pinos do header, que dão mau-contato. A comunicação só funcionou bem quando deixei de usar os pinos longos para inserção em header fêmea. Os pinos longos são achatados, o que prejudica o contato com o header fêmea.

Há modelos que parecem ter pinos de secção quadrada <https://pt.aliexpress.com/i/32957025575.html>. Talvez resolvam o problema de contato, mas não pretendo comprar e esperar vir.

origem da figura abaixo: <https://www.instructables.com/id/Witty-Cloud-Module-Adapter-Board/>

![](sobreESPCrossover/FTNJHCRIYOQCBSN.jpg)

Esta é uma outra fonte de informação: <https://www.schatenseite.de/en/2016/04/22/esp8266-witty-cloud-module/>

origem das figuras abaixo: <https://www.14core.com/wiring-and-flashing-programming-esp-32-esp32s-with-usb-ttl-uart/>

![circuito mínimo?](sobreESPCrossover/ESP32-Flash-USB-UART-Wiring-Guide-diagram-768x706.jpg)

![pinagem](sobreESPCrossover/ESP32-Pinout-DIagram-768x454.jpg)


## Diário

{
"data" : "sex 2020-09-04 14:13:33 -0300"
"texto" : "
Tremenda bagunça... muita calma nesta hora...

![Bagunça](sobreESPCrossover/IMG_20200904_134532194.jpg)


Comecei a escrever este arquivo ontem - já imaginava que ia gerar muita informação e muito trabalho... vamos ver se no final consigo gerar algum valor, que compense o trabalho...

... no momento estou me torturando com essa história de 'eu já sabia...'

Uma coisa de cada vez... (respire...)

---

Reflexão:

Ter o ESP32 funcionando com circuito mínimo, para mim, implica em ter uma bateria fornecendo energia para ele. Ter uma bateria implica em ter o carregador para a bateria e, talvez, o regulador de tensão entre a bateria e o ESP32.

A bateria eu tenho. é uma LiPo de 3,7V 720mAh. Que eu me lembre tenho três dessas, mas só encontrei duas.

O carregador, lembro que comprei 16, pois é o mesmo que vai dentro de battery packs a achei barato no 'atacado'. O modelo é TP4056 com o DW01 e 8205. O que eu não lembrava é que tinha dois montados, inclusive com o conector para a bateria.

![carregador montado e bateria](sobreESPCrossover/IMG_20200904_142639339.jpg)

---

Experimentação:

Noite passada conectei a bateria ao carregador, o carregador ao carregador de celular. Em menos de meia hora o monitor de carga foi para 'carregado'. Infiro que a bateria estava carregada (fiz isso quando comprei e recebi, deve fazer um ano).

Reflexão durante experimentação:

O circuito mínimo do ESP8266 conecta TX, RX, VCC, GND, `CH_PD` e GPIO0 [esquemático](sobreESPCrossover/FTNJHCRIYOQCBSN.jpg). O circuito mínimo do ESP32, um tanto forçadamente, parece ser o mesmo [esquemático](sobreESPCrossover/ESP32-Flash-USB-UART-Wiring-Guide-diagram-768x706.jpg). Talvez o LED na GPIO16 seja necessário. Analisando o [esquemático do NodeMCU](sobreESPCrossover/Ai-Thinker_NodeMCU-32S_DiagramSchematic.png) talvez os pull-ups de 12k mostrados juntos aos botões RST e EN também sejam necessários. MAS eu queria apenas soldar os fios no ESP32, o que fiz.

![ESP32 com fios soldados](sobreESPCrossover/IMG_20200904_180147503.jpg) - falha de continuidade: tirada no fim do dia 

... agora vamos às suposições...

Eu supus que o carregador tinha um regulador de tensão de 3.3V embutido, mas, de manhã, quando medi a tensão nos pinos de saída tinha 4.2V - a mesma tensão da bateria, que, no momento, estava carregada.

Para testar se a bateria sustentava a tensão mesmo com algum dreno de corrente, conectei um LED vermelho com um resistor de 330ohm. Foi para 4.18V.

Lembro de memória que a tensão nominal do ESP32 é 3.3V e que a máxima é 3.6V, precisava diminuir um pouco a tensão. Fui almoçar pensando se usaria um regulador low-drop (ams1117) ou um diodo retificador. 

Também de memória, lembro que a queda de tensão mínima para o ams1117 regular a tensão de saída era alta. Então escolhi o diodo.

![tudo conectado ficou assim](sobreESPCrossover/IMG_20200904_134129168.jpg) 

Na foto já tem o jumper conectando os GND, que faltou da primeira vez que liguei (e não funcionou).

O monitor serial mostrou algumas tentativas de boot e finalmente um boot como soft_AP.

![mensagens de boot no monitor serial](sobreESPCrossover/Captura%20de%20tela%20de%202020-09-04%2013-29-37.png)

Um softAP é detectável na varredura de redes wifi do celular. De fato, foi detectado:

![screenshot do celular](sobreESPCrossover/Screenshot_20200904-132951.png)

Quando tentei enviar um programa recebi uma mensagem de erro:

![mensagem de erro](sobreESPCrossover/Captura%20de%20tela%20de%202020-09-04%2013-31-04.png)

Um problema irritante de testar ESP tão perto é que ele derruba a conexão wifi dos aparelhos que estiverem próximo:celular, computador, ... 

---

Estudo, posterior à experimentação:

O blog do Gustavo Murta [apresenta alguns modelos de carregador de bateria](https://jgamblog.wordpress.com/2017/01/05/projeto-carregador-de-bateria-li-ion/).

**nota**: Gustavo Murta referencia <https://batteryuniversity.com/index.php/learn/>. Pode ser elucidativo dar uma espiada.

![Figura do esquemático do site do Gustavo Murta](sobreESPCrossover/tp4056-dw01-GustavoMurta.jpg)

Segundo a referência, DW01 é um protetor de sobrecorrente e sub-tensão. Se a tensão da bateria for acima de 4.3V ou a tensão da bateria ir abaixo de 2.4V, a bateria é desconectada pelo chaveamento de algum dos MOSFETS - são dois no 8205, que é um driver/buffer. Isto é feito para (tentar) previnir danos à bateria.

A corrente de carga pode ser controlada mudando o valor de R3. Copiei a figura abaixo de [arduino e cia](https://www.arduinoecia.com.br/como-usar-carregador-de-bateria-de-litio-tp4056/)

![mostrando R3](sobreESPCrossover/Modulo-TP-4056-Detalhe-638.png)

[Datasheet de diodo Schottky](sobreESPCrossover/1N5817) baixado de <pdf.datasheetcatalog.com/datasheet/bytes/1N5817.pdf>


[Datasheet do AMS1117](sobreESPCrossover/ds1117.pdf) baixado de <http://www.advanced-monolithic.com/pdf/ds1117.pdf>

[Datasheel do ESP32](sobreESPCrossover/esp32_datasheet_en-1223853.pdf) baixado de <https://br.mouser.com/ProductDetail/Espressif-Systems/ESP32-D0WDQ6?qs=chTDxNqvsykWgzfXx0gR%252BQ==>, <https://br.mouser.com/datasheet/2/891/esp32_datasheet_en-1223853.pdf>

[O verbete da wikipedia sobre ESP32 contém uma lista de placas baseadas em ESP32, de alguma forma mais organizada que a de esp32.net.](https://en.wikipedia.org/wiki/ESP32)

---

Agora terminei de anotar toda a informação que consegui até agora. Próximo passo, depois do café, colocar os resistores pull up e testar.

Reorganizei o circuito.

Ligando e tocando no reset deu mensagem no monitor serial.

![mensagem no monitor serial](sobreESPCrossover/Captura%20de%20tela%20de%202020-09-04%2018-15-55.png)

Errei a conexão do GPIO0, deu timeout na programação.

![timeout](sobreESPCrossover/Captura%20de%20tela%20de%202020-09-04%2018-16-58.png)

Testei com pull up de 10k em GPIO0 e EN, sem e com LED em GPIO2 e em GPIO13. A mensagem continua a mesma:

![mesma mensagem](sobreESPCrossover/Captura%20de%20tela%20de%202020-09-04%2018-17-54.png)

Usei um NodeMCU-ESP32 para ver qual é a mensagem quando programa sem erros:

![Node32s](sobreESPCrossover/Captura%20de%20tela%20de%202020-09-04%2018-23-11.png)

Depois do stub rodando (não sei o que é isso), a mensagem `time out waiting for packet content` é a primeira diferença.

Testei com diferentes ajustes de placa: ESP32 DevKit, Node32s - a mesma mensagem.

GENTE! FUNCIONOU!!!!

![Funcionou](sobreESPCrossover/Captura%20de%20tela%20de%202020-09-04%2019-13-05.png)

Com node32s, baixando a velocidade de upload para 115200

[A dica veio daqui](https://github.com/espressif/arduino-esp32/issues/333)

![Funcionou](sobreESPCrossover/Captura%20de%20tela%20de%202020-09-04%2019-18-39.png)

[arquivos eagle do ESP32](https://esp32.com/viewtopic.php?t=7004)

[Cópia local](sobreESPCrossover/ESP32-DEVKITV1.lbr.zip)

"
}
{
"data" : "sáb 2020-09-05 15:30:48 -0300"
"texto" : "
Finalizando...

Desconectei o pulldown da gpio13, comunicou e programou bem.

Desconectei o pulldown da gpio02, para minha surpresa, comunicou e programou bem. Testei colocando pullup em gpio2 - deu a mesma mensagem de erro. Aparentemente tem um pulldown interno pois liguei o pullup, o programa não carregou, deixei o pino flutuando e o programa carregou.

Medi corrente no pino, conectado a um resistor de 4k7: 60uA a VCC=3,1 pelas contas, há um pulldown interno de 47k.

Tirei os pullups de 10K de GPIO0 e EN e tanto comunicou quanto programou. Acho meio inacreditável pois com o ESP8266 esses pullups (que, no wittyboard, estão na placa do controlador, eram essenciais).
"
}
{
"data" : "sáb 2020-09-05 17:35:58 -0300"
"texto" : "

Sobre energia para o ESP32.

Fiquei invocado com a queda de tensão de 1.1V no ams1117. Isso inviabiliza seu uso para regular tensão de bateria de celular (3.7V) para o celular e ESP32 (3.3V).

Lembro que vi reguladores com dropout menor, então fui atrás, achei o TDA3663:

[datasheet TDA3663](https://www.nxp.com/docs/en/data-sheet/TDA3663.pdf?)

[Cópia local](sobreESPCrossover/TDA3663.pdf)

mas não era esse que eu lembrava. Aí me toquei que no wemos com bateria 18650 tem algo. Fui checar o código do componente (com uma lupa) e li TP5400. É uma evolução do TP4056 que integra os circuitos de proteção e a fonte stepup para 5V. Tem um produto na amazon. Parece a mim que a idéia é ter um circuito compacto para um battery pack. *Não tem regulador para 3.3V*

[TP5400 na Amazon](https://www.amazon.co.uk/AZDelivery-TP5400-Micro-Port-Parent/dp/B082NZX73V)

[datasheet TP5400](https://datasheetspdf.com/pdf-file/1311594/TopPower/TP5400/1)

[Cópia local](sobreESPCrossover/TP5400-TopPower.pdf)

Parece que a escolha de projeto é carregar a bateria de 3.7V com 5V e usar a bateria para gerar 5V. O ESP32 recebe energia de um AMS1117. O circuito desperdiça 1/3 da energia que recebe.

Aí fui no TTGO T-Display:

[esquemático do TTGO T-Display](https://raw.githubusercontent.com/Xinyuan-LilyGO/TTGO-T-Display/master/schematic/ESP32-TFT(6-26).pdf)

[Cópia local](sobreESPCrossover/ESP32-TFT(6-26).pdf)

Ele tem um TP4056, um AP2112K-3.3V e uns MOSFETs. Aparentemente os MOSFETs controlam o fornecimento de energia em função de PWR EN e da conexão de várias fontes (5V, 3.7V, 3.3V, 3V(!?)). Do que consegui entender, não protegem a bateria de descarga excessiva, o que faz o DW01 (tem um site no instructables que diz o mesmo).

O AP2112K-3.3V tem dropout de 0.25 a 0.4V - Os outros valores de saída regulada têm dropouts diferentes, maiores.

[datasheet AP2112](https://www.diodes.com/assets/Datasheets/AP2112.pdf)

[Cópia local](sobreESPCrossover/AP2112.pdf)

O que eu queria saber é o AP2112K-3.3V - não tem no mercado livre, só tem no shopee

"
}
{
"data" : "dom 2020-09-06 14:03:02 -0300"
"texto" : "
Display,
PCB,
Regulador,
I2C,
Touch

"
}

## 2020-12-22-174702

Retornei a este projeto. Tenho grandes novidades



