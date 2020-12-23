# ESP8266

ESP8266 refere-se a uma família de System on Chip (SoC) produzidos(?) pela Espressif. Há vários modelos com diferentes pinagens, quantidades de pinos usáveis, capacidades de processamento, quantidade de memória.

A cadeia de ferramentas de programação (toolchain) tem grande participação de comunidades de desenvolvedores autônomos.

Na figura abaixo, da esquerda para a direita: ESP8266-01, ESP8266-07, ESP8266-12. Em certos contextos, o 8266 pode ser omitido sem perda de especificidade do termo. Então tem-se ESP-01, ESP-07 e ESP-12. Caso seja necessário ser mais preciso para apontar o componente, o chip quadrado com terminais pelos quatro lados (encapsulamento [QFP](https://en.wikipedia.org/wiki/Quad_flat_package)), visível no ESP-01 é o SoC. Nos outros modelos, removendo a capa metálica é possível ver o SoC.

![Modelos de ESP8266 que tenho](IMG_20201223_115720998.jpg)

Existe uma variedade de placas controladoras baseadas em ESP8266. As que conheço, ou uso, são documentadas nas próximas seções.

## NodeMCU-ESP12

É a placa de ESP8266-12 que costumo encontrar nas lojas com maior frequência. 

Diagrama esquemático

![ESP8266 esquemático](NODEMCU_DEVKIT_SCH-esp12.png)

Na minha opinião, esta placa foi concebida para prototipagem, nos moldes do Arduino Nano.

Uma pergunta que me fazem frequentemente é como usar protoboard com NodeMCU, já que ele ocupa toda a largura de um protoboard. A resposta é usar um protoboard para cada fileira de pinos. Se seu projeto puder usar os pinos de um lado só, um protoboard é suficiente.

## Wittyboard

Wittyboard é um controlador baseado em ESP8266 composto por duas placas que são conectadas uma sobre a outra, similar a *shields* de Arduino UNO.

Na foto, no plano da frente as duas placas montadas, no plano de trás as duas placas separadas.

![Wittyboard](IMG_20201009_185605093.jpg)

Para programar, as duas placas devem estar conectadas (ou montadas uma sobre a outra) e a conexão deve ser feita pela porta USB da placa de baixo no plano da frente, ou à esquerda no plano de trás.

Na placa de baixo, o componente (que considero) principal é o conversor USB para Serial - CH340. Há na placa um cristal oscilador de 12MHz os capacitores conectados a ele. Os dois transistores e alguns resistores fazem parte do circuito de reset.

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

Os 3.3V não são acessíveis através dos pinos do wittyboard. Por outro lado, a saída do regulador de tensão é conectada ao seu dissipador de calor, logo, soldando um jumper ao dissipador do regulador permite usar 3,3V.

A mistura de circuitos que operam a 5V com circuitos que operam a 3,3V é possível, até comum, mas os circuitos precisam ser projetados para isso. Logo, é mais simples usar 3.3V em tudo. Seguem dois exemplos de mistura de tensão de operação. O primeiro, com LEDs neopixel, costuma falhar, o segundo com shield de relé, costuma funcionar.

LEDs WS2812 (os neopixel) necessitam de 5V em Vcc para operar, mas isso não é suficiente para funcionar conforme a operação normal, quando conectado ao ESP: Fornecendo 5V no Vcc do LED, o nível lógico alto em Din corresponde a aprox. 0,7*Vcc (dado de manual), o que resulta em 3,5V. A saída do ESP em nível lógico alto fornece 3,3V, o que não é suficiente para Din do LED. Ou seja, alguns '1' serão trocados por '0', em função de características de construção do LED e do circuito que não são controladas. Consequentemente, ocorrem resultados inesperados.

Um caso em que, misturando, funciona conforme normalmente se espera, é o de conectar ESP com *shield* de relé. O circuito mais comum para esse *shield* tem um transistor para aumentar a corrente controlada e energizar a bobina do relé. Quando usado com ESP, além de aumentar a corrente, ele também ajusta os 3.3V para 5V. Tecnicamente, funciona como *level shifter* ou *level converter* unidirecional, o que é suficiente para que o relé ligue e desligue conforme o esperado.

Projetos neste repositório que usam esta placa:

1. [Tomada conectada](../../../../projetos/ControlarTomadaPelaInternet/README.md)
3. [Prototipagem com Witty board](../../../../projetos/PrototipagemWitty/README.md)
3. [ESP32 Crossover](../../../../projetos/ESP32Crossover/README.md)

## TTGO ESP8266

Esta placa tem um display OLED.

![](../../../../projetos/SensorMeteorologico/Documentos/imagens/ttgo.jpg)

Projetos neste repositório que usam esta placa:

1. [Sensor meteorológico](../../../../projetos/SensorMeteorologico/README.md).

