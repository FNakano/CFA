# ESP8266

Existe uma variedade de placas controladoras baseadas em ESP8266. As que conheço, ou uso, são documentadas nas próximas seções.

## NodeMCU

Diagrama esquemático

![ESP8266 esquemático](NODEMCU_DEVKIT_SCH-esp12.png)

Na minha opinião, este componente foi concebido para prototipagem, nos moldes do Arduino Nano.

Uma pergunta que me fazem frequentemente é como usar protoboard com NodeMCU, já que ele ocupa toda a largura de um protoboard. A resposta é usar um protoboard para cada fileira de pinos. Se seu projeto puder usar os pinos de um lado só, um protoboard é suficiente.

## Wittyboard

Wittyboard é um controlador baseado em ESP8266 composto por duas placas que são conectadas uma sobre a outra, similar a *shields* de Arduino UNO.

Na foto, no plano da frente as duas placas montadas, no plano de trás as duas placas separadas.

![Wittyboard](IMG_20201009_185605093.jpg)

Para programar, as duas placas devem estar conectadas (ou montadas uma sobre a outra) e a conexão deve ser feita pela porta USB da placa de baixo no plano da frente, ou à esquerda no plano de trás.

Na placa de baixo, o componente (que considero) principal é o conversor USB para Serial - CH340. Há na placa um cristal oscilador de 12MHz os capacitores conectados a ele, dois transistores e alguns resistores.

Na placa de cima, o ESP8266-12E, um LED RGB, um LDR e alguns resistores na parte de cima. No verso da placa há um regulador de tensão de 3.3V - AMS1117, alguns resistores e capacitores.

Comparando com o diagrama esquemático do NodeMCU-ESP12, acima, os circuitos nos quadros CORE e POWER estão na placa de cima e os circuitos USBtoUART e KEY estão na placa de baixo. O ADC foi um pouco modificado para receber o LDR. Os LEDs e o botão na placa de cima foram acrescentados.

A pinagem está na tabela abaixo.

| Label | Pin (Arduino) | Purpose
| --- | --- | --- |
| REST | — | Reset |
| ADC | A0 | Analog input, connected to LDR |
| CH_PD | — | Chip Power-Down |
| GPIO16 | D0 | GPIO, freely usable |
| GPIO14 | D5 | GPIO, freely usable |
| GPIO12 | D6 | GPIO, green channel of RGB-LED |
| GPIO13 | D7 | GPIO, blue channel of RGB-LED |
| VCC | — | +5V power |
| TXD | TX | Serial interface |
| RXD | RX | Serial interface |
| GPIO5 | D1 | GPIO, freely usable |
| GPIO4 | D2 | GPIO, connected to pushbutton |
| GPIO0 | D3 | GPIO, connected to flash-button, not really freely usable |
| GPIO2 | D4 | GPIO, connected to blue LED on the ESP-Module |
| GPIO15 | D8 | GPIO, red channel of RGB-LED |
| GND | — | Ground |

Os 3.3V não são acessíveis através dos pinos do componente. É comum precisar dessa conexão pois circuitos que misturam sinais de 3.3V com sinais de 5V são projetados para isso, o que não é o caso aqui. Por exemplo, LEDs ws2812 (os neopixel) necessitam de 5V. Mesmo fornecendo 5V em seu Vcc, usar diretamente uma saída do ESP conectada ao DIN do LED dá resultados inesperados.

A solução mais simples é usar 3.3V em tudo.

Um caso em que misturando, por acaso, funciona é o de conectar ESP com *shield* de relé. O circuito mais comum para esse *shield* tem um transistor para aumentar a corrente controlada e energizar a bobina do relé. Quando usado com ESP, além de aumentar a corrente, ele também ajusta os 3.3V para 5V. Tecnicamente, funciona como *level shifter* ou *level converter* unidirecional (não precisa mais que isso).

## TTGO ESP8266


