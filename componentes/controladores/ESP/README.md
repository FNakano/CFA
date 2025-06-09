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
    2. ~~para ESP32: `https://dl.espressif.com/dl/package_esp32_index.json`~~ referência mais recente, da documentação do fabricante: https://espressif-docs.readthedocs-hosted.com/projects/arduino-esp32/en/latest/installing.html, indica para usar `https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json`  
    3. Caso queira os dois, acrescente as duas URLs, separadas por vírgula
3. clique ok;
4. Entre em Ferramentas->placa->gerenciador de placas (talvez leve um tempinho até carregar as placas novas);
5. busque por ESP8266 ou ESP32;
6. instale ESP8266 ou ESP32;

(isto já foi testado em Windows, Linux e Raspbian Stretch no raspberry pi 4)

**IMPORTANTE**

- 2022-09-24: A versão 2.0.X da IDE para Ubuntu tem bugs que me fizeram voltar para 1.8.19, que é distribuída junto com Ubuntu 22.04;
- 2022-09-24: A porta USB (ex. /dev/ttyUSB0) pode não ser acessível no Ubuntu 22.04 pois o teclado braille impede a montagem. Só consegui fazer funcionar removendo o pacote do teclado braille, com `sudo apt remove brltty` e rebootando. Ref.: https://askubuntu.com/questions/1410062/installed-arduino-cant-find-dev-usb0-or-dev-acm0)
- O comando para acrescentar usuário ao grupo dialout é: `sudo usermod -a -G dialout <username>`. Ref.: https://support.arduino.cc/hc/en-us/articles/360016495679-Fix-port-access-on-Linux

Há tutoriais ilustrados para ESP8266 em:

- [filipeflop](https://www.filipeflop.com/blog/programar-nodemcu-com-ide-arduino/) 
- [robocore](https://www.robocore.net/tutorials/como-programar-nodemcu-arduino-ide)
- [Arduino](https://www.robocore.net/tutorials/como-programar-nodemcu-arduino-ide)
- [Instructables](https://www.instructables.com/id/Quick-Start-to-Nodemcu-ESP8266-on-Arduino-IDE/)

## Testar a programação do ESP8266

Consiste em conectar um LED à placa do ESP8266 e fazer o LED acender ou piscar. É uma forma simples, rápida e boa de checar que você achou e ajustou adequadamente as configurações do seu ambiente de desenvolvimento e ele está funcionando bem e se todo seu procedimento para programar o ESP8266 chega ao resultado desejado.

0. monta o circuito;
1. conecta o ESP ao computador usando o cabo USB; 
   - apesar do ESP ter o modem wi-fi embutido, a conexão não é automática e a programação é feita pela USB. É possível atualizar o programa *over the air* (OTA) há exemplo para isso.
   - no linux, um indicador que a conexão foi feita é aparecer em /dev um arquivo ttyUSBn ou ttyACMn onde n é um número;
2. abre IDE do Arduino;
3. seleciona porta;
   - no windows deve aparecer um COMn, onde n é um número. Esta porta representa seu dispositivo. Caso não apareça, pode ser mau-contato no cabo, ou ESP defeituoso, ou falta instalar algum driver no Windows;
   - no linux, deve aparecer ttyUSBn ou ttyACMn; 
4. seleciona placa; 
   - para o ESP8266, costuma funcionar a escolha por `generic ESP8266`;
4. Abre o programa que você deseja executar;
5. compila, 
   - botão com um *checkmark*;
   - se alguma ferramenta de programação não estiver instalada, geralmente ocorre erro nesta etapa;
6. envia programa.
   - botão com uma *seta*;
   - se alguma ferramenta de programação não estiver instalada, ou o cabo estiver com mau-contato, ou o ESP estiver defeituoso, ocorre erro nesta etapa.
   - há modelos de ESP em que, após clicar na *seta*, é necessário apertar o botão de reset no ESP.


Cada um dos tutoriais ilustrados sugere algo ligeiramente diferente. Se você só tem um LED, siga o do filipeflop. Se você tem LED e resistor, siga o do robocore ou o do Instructables. Se você não tem LED e acredita ou sabe que o LED azul embutido no ESP8266 está funcionando, siga o do Arduino.

Lembre de selecionar a placa: No ArduinoIDE, vá em Ferramentas -> placas e selecione generic esp8266.

## Características em comum

Memória de programa do tipo FLASH.

Modo deep-sleep:

- [WeMos D1 0 ESP8266](https://diyprojects.io/esp8266-deep-sleep-mode-test-wake-pir-motion-detector/#.X5IAH5pv9Ks)
- [ESP8266 (Node ESP8266](https://randomnerdtutorials.com/esp8266-deep-sleep-with-arduino-ide/)
- [ESP32](https://diyprojects.io/esp32-arduino-code-for-deep-sleep-and-wake-ups-timer-touch-pad-gpio/#.X5IAIZpv9Ks)

## Uso dos pinos nos ESP

Os ESP são componentes com muitas funcionalidades e, proporcionalmente, poucos pinos externos. Para conciliar essas duas características, os pinos têm múltiplas funções, o que gera restrições de uso em determinadas situações. Esta característica (é uma que) atrapalha o aprendizado. Por isso, na minha opinião, não é o componente preferencial para o primeiro contato com dispositivos. Isto é mais crítico no ESP8266 que no ESP32. Alguns tutoriais apresentam os pinos e usos nos ESP8266:

- [randomnerdtutorials](https://randomnerdtutorials.com/esp8266-pinout-reference-gpios/)
- [tttapa](https://tttapa.github.io/ESP8266/Chap04%20-%20Microcontroller.html)

## Modos de boot

- <https://github.com/esp8266/esp8266-wiki/wiki/Boot-Process#esp-boot-modes>
- <https://www.esp8266.com/viewtopic.php?f=6&t=8386>
- <https://esp8266.ru/esp8266-pin-register-strapping/>



## I2C

I2C é um protocolo de comunicação entre circuitos integrados. Ele permite conectar até 127 dispositivos em um barramento de 2 fios de dados: SCL e SDA (nestes momentos o GND é essencial mas não entra na contagem, e o VCC só é necessário se os dispositivos compartilham a mesma fonte de energia).

A comunicação é feita entre pares de dispositivos e é bi-direcional.

Uma grande variedade de componentes implementam esse protocolo. Por exemplo GY-91 (Acelerômetro), CCS811 (CO2 e temperatura), BMP280 (pressão atmosférica e temperatura), BME280 (pressão atmosférica, temperatura e umidade relativa do ar), DS1307 (RTC).

- [tutorial sobre I2C em diy0t](https://diyi0t.com/i2c-tutorial-for-arduino-and-esp8266/)


### Limite na quantidade de leituras e escritas em memória FLASH



#### Nivelamento de uso de memória FLASH

Tecnologia em evolução. Em 2017 não havia biblioteca para *wear levelling* <https://forum.micropython.org/viewtopic.php?t=3429>. 

Para o ESP32, o fabricante informa que há biblioteca para *wear levelling* <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/storage/wear-levelling.html>

## Uso da memória FLASH como sistema de arquivos

<https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/storage/spiffs.html>

<https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/storage/vfs.html>

<https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/storage/fatfs.html>

## Multiprogramação com ESP32

Multiprogramação é um recurso útil pois permite de, maneira mais ou menos transparente, executar vários programas *simultaneamente*. Por exemplo, um ESP que ao mesmo tempo é Servidor HTTP e cliente HTTP (para transmitir e disponibilizar dados), tem uma quantidade de sensores e atuadores e alguma autonomia (ié, um sistema remoto não tem uma cópia confiável dos estados dos sensores e atuadores pois o controlador pode mudar esses estados). Importante notar que isso pode ser codificado sem o apoio de ferramentas como FreeRTOS, mas o programa fica muito complexo.

O ESP programado em C usando ESP-IDF tem sua própria versão de FreeRTOS (https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/freertos.html)

Multiprogramação em (Micro)Pyton é baseada em `asyncio`, que define co-rotinas e comandos (`async def`, `await`, `run`, `gather`, ...) para trocar tarefas em função do uso de E/S ou de esperas (`sleeps`) comuns em microcontroladores. (https://docs.micropython.org/en/latest/library/asyncio.html)

Eu fui procurar se a pilha de ferramentas que permite MicroPyton usar I2C no ESP32 implementava algo melhor que *polling*. Por exemplo: A unidade de controle (UC) configura a unidade de comunicação I2C (UI2C) para requisitar de um dispositivo algum conteúdo; quando o conteúdo estiver, na UI2C, disponível para a UC, a primeira gera uma interrupção, essa interrupção é atendida por um ISR que grava esse conteúdo em alguma variável do Micropython, Micropython (ou seu programa monitor) tem alguma lista de processos de usuário para saber para qual processo enviar a informação e que este deve ser acordado (de um `await`).

Parece que no ESP32 há tal comportamento da UI2C mas não é como o driver da Espressif funciona. O driver bloqueia a execução ([Captura de tela](./Captura%20de%20tela%20de%202025-06-09%2014-15-55.png)). Ainda conforme o forum do desenvolvedor (https://esp32.com/viewtopic.php?t=37211), isso foi feito para *conveniência de uso*. Independente de juízo, em 2023, o fabricante não oferecia suporte a programas de usuário para funções I2C que não causassem o bloqueio de execução do programa de usuário, mesmo que esse bloqueio pudesse fazer o OS passar o controle para outro programa de usuário.

Pensando o Micropython como um programa de usuário, este é bloqueado. O controle poderia passar para outra instância de Micropython, se ela existisse, mas não passaria para outra co-rotina (de asyncio) dentro da mesma instância de Micropython. Agora dá para entender esta frase: > The blocking nature of the MicroPython I2C device driver is mitigated by hardware synchronisation on two wires. This ensures that the slave is configured for a transfer before the master attempts to access it. ([Captura de tela](./Captura%20de%20tela%20de%202025-06-09%2014-32-34.png) , https://github.com/peterhinch/micropython-async/blob/master/v3/docs/I2C.md ). Desta forma, por enquanto, não há no I2C em Micropython, de evitar coisas como `await asyncio.sleep(...)`.

Note que há problemas reportados em Micropython em 2023 (https://github.com/orgs/micropython/discussions/12527) e em 2020 (https://github.com/micropython/micropython/issues/5714#issuecomment-617838375) e que tentou-se fazer algo melhor, desde 2018 (https://github.com/peterhinch/micropython-async/blob/i2c_hard_irq/i2c/README.md#5-limitations)

Documentação da Espressif sobre I2C no ESP32 (https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/peripherals/i2c.html)

