# ESP

Família de microcontroladores projetada pela espressif. Os modelos mais utilizados na disciplina são ESP8266-12 e ESP32. 

A tensão de alimentação destes controladores é 3.3V. A estratégia de trabalho mais simples e menos arriscada para este componente é ter o circuito todo trabalhando a 3.3V. Caso não seja possível, usar conversores de nível nas interconexões em que for necessário.

A vida útil dos componentes pode diminuir significativamente se este for usado fora das condições de funcionamento. A conexão de saídas do ESP a entradas de componentes que trabalhem a 5V pode causar resultados inesperados (ver considerações sobre níveis lógicos), mas é segura. Já a conexão de entradas do ESP a saídas de componentes que trabalhem a 5V deve ser feita com conversores de nível lógico.

O ESP8266 tem wi-fi integrado, até 4Mbytes de memória FLASH. A capacidade de processamento é tal que conexões HTTPS e EDUROAM não são possíveis.

O ESP32 tem wi-fi, bluetooth low-energy e pinos touch. Sua capacidade de processamento permite conexões HTTPS e EDUROAM.

### Configurar ArduinoIDE para programar o ESP8266 ou o ESP32

Atualmente isto está mais estável e com referências consistentes, assim, quem precisa fazer um tutorial não precisa aplicar muito tempo. Considerando como ponto de partida que ArduinoIDE versão 1.6.5 ou mais recente já esteja instalado:

1. Entre em Arquivo->preferências;
2. na linha **URLs adicionais de gerenciador de placas** acrescente 
    1. para ESP8266: `http://arduino.esp8266.com/stable/package_esp8266com_index.json`
    2. para ESP32: `https://dl.espressif.com/dl/package_esp32_index.json`
    3. Caso queira os dois, acrescente as duas URLs, separadas por vírgula
3. clique ok;
4. Entre em Ferramentas->placa->gerenciador de placas (talvez leve um tempinho até carregar as placas novas);
5. busque por ESP8266 ou ESP32;
6. instale ESP8266 ou ESP32;

(isto já foi testado em Windows, Linux e Raspbian Stretch no raspberry pi 4)

Há tutoriais ilustrados para ESP8266 em:

- [filipeflop](https://www.filipeflop.com/blog/programar-nodemcu-com-ide-arduino/) 
- [robocore](https://www.robocore.net/tutorials/como-programar-nodemcu-arduino-ide)
- [Arduino](https://www.robocore.net/tutorials/como-programar-nodemcu-arduino-ide)
- [Instructables](https://www.instructables.com/id/Quick-Start-to-Nodemcu-ESP8266-on-Arduino-IDE/)

## Testar a programação do ESP8266

Consiste em conectar um LED à placa do ESP8266 e fazer o LED acender ou piscar. É uma forma simples, rápida e boa de checar que você achou e ajustou adequadamente as configurações do seu ambiente de desenvolvimento e ele está funcionando bem e se todo seu procedimento para programar o ESP8266 (conecta o ESP, seleciona porta, seleciona placa, compila, envia programa, ...) chega ao resultado desejado.

Cada um dos tutoriais ilustrados sugere algo ligeiramente diferente. Se você só tem um LED, siga o do filipeflop. Se você tem LED e resistor, siga o do robocore ou o do Instructables. Se você não tem LED e acredita ou sabe que o LED azul embutido no ESP8266 está funcionando, siga o do Arduino.

Lembre de selecionar a placa: No ArduinoIDE, vá em Ferramentas -> placas e selecione generic esp8266.

