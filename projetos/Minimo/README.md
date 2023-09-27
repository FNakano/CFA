# Circuito mínimo para ESP8266

## Motivação

Todo ano aparecem pessoas que afirmam que as placas de desenvolvimento são grandes, que as baterias são grandes e assim por diante.

Pretendo apresentar uns poucos motivos técnicos/tecnológicos para embasar os argumentos que pretendo apresentar para chegar a um circuito mínimo para ESP8266.

## Requisitos

1. O circuito deve permitir programar o microcontrolador;
2. O mínimo de componentes adicionais;

## Fundamentos

Componentes eletrônicos têm suas especificações em *datasheets* que podem ter uma página A4 a vários volumes com centenas de páginas cada. A informação que interessa, neste momento, é qual a tensão e a corrente mínimos que devem ser fornecidos ao ESP(8266/32).


- [Datasheet do ESP8266](https://www.espressif.com/sites/default/files/documentation/0a-esp8266ex_datasheet_en.pdf)
- [Datasheet do ESP32](https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32_datasheet_en.pdf)

| aaa | ESP8266 | ESP32 |
| --- | --- | --- |
| Tensão mínima de operação | 2,5V | 3,0V |
| Corrente média de operação | 80mA | 500mA |

### Algumas observações que talvez interessem

- Boa parte da corrente de operação é usada para transmissão via Wi-Fi;
- Usei pilhas AA comuns (duas, para fornecer 3V) e um pouco gastas - elas não sustentaram o ESP8266;
- Usei pilhas AA alcalinas de boa marca e novas - elas sustentaram o ESP8266 (com certeza duram mais de 5 minutos);

O ESP8266 parece não ter ajuste de potência de transmissão (https://www.espressif.com/sites/default/files/9b-esp8266-low_power_solutions_en_0.pdf).

## Circuito para ESP8266

O circuito mínimo para o ESP8266 precisa fornecer energia para o ESP e definir alguns sinais para o ESP iniciar no modo correto.

| ESP8266 | bbb | ccc |
| --- | --- | --- |
| Vcc | Pilhas + | essencial |
| GND | Pilhas - | essencial |
| GPIO0 | Pull-up | necessária no boot |
| GPIO15 | Pull-down | necessária no boot |
| EN | Pull-up | essencial |
| RST | Pull-up | opcional - melhora estabilidade |

Fonte dos dados da tabela: http://arduino.esp8266.com/Arduino/versions/2.0.0/doc/boards.html

- Pull-up é um resistor de 10kOhm, de um lado ligado ao pino do ESP, do outro, ligado ao Vcc. Sua função é fornecer nível lógico 1 ao pino em que está conectado.
- Pull-down é um resistor de 10kOhm, de um lado ligado ao pino do ESP, do outro, ligado ao GND. Sua função é fornecer nível lógico 0 ao pino em que está conectado.
- A conexão é essencial quando sem ela o ESP não inicia (nem em um modo alternativo);
- A conexão é necessária no boot quando com ela o ESP inicia no modo desejado e sem ela o ESP inicia em um modo alternativo (que não é desejável);
   - Sobre modos alternativos de boot: https://docs.espressif.com/projects/esptool/en/latest/esp8266/advanced-topics/boot-mode-selection.html , https://github.com/esp8266/esp8266-wiki/wiki/Boot-Process
- A conexão é opcional quando não é essencial;

## Software

O ESP pode ser acessado ou por sua interface serial, padrão RS232, ou pelo Wi-Fi. A primeira necessita de mais componentes (pelo menos um conversor serial para USB do tipo FTDI-232, CH340, CP2102 ou equivalentes), então optou-se por acessá-lo pelo Wi-Fi.

O acesso por Wi-Fi é feito através de Micropyton e WebREPL. A gravação do Micropython e a configuração do Wi-Fi são feitas com o auxílio de um gravador para ESP8266 [Foto do programador com um ESP07 encaixado](./2023-09-27-161310.jpg): 
	
1. Encaixe o ESP no gravador, 
2. conecte o gravador ao computador através da porta USB, 
3. grave o MicroPython (mais detalhes na [postagem sobre MicroPython](https://github.com/FNakano/CFA/tree/master/programas/Micropython)), 
4. configure o Wi-Fi.

A configuração do Wi-Fi é feita de modo que o ESP funcione como ponto de acesso (https://github.com/FNakano/CFA/tree/master/programas/Micropython/webREPL#esp-como-access-point-ap), ou seja, quando o ESP for ligado, ele disponibilizará uma rede Wi-Fi, com nome e senha definidos na configuração. Um computador (com duas conexões à rede, uma para o ESP, outra para a Internet) pode conectar-se a ele.

No ESP o arquivo `boot.py` foi modificado para importar o arquivo `setAsAP.py`. Ambos são fornecidos neste projeto. 

Através do computador, acesse o github do WebREPL e conecte-se a ws://192.168.4.1, aparecerá uma mensagem solicitando a senha de acesso ao webREPL, digite a senha. A partir daí, comandos em Python podem ser enviados ao ESP. Mais detalhes na [postagem sobre WebREPL](https://github.com/FNakano/CFA/tree/master/programas/Micropython/webREPL)


### Notas sobre software

Há alguns reports que informam que webrepl para de funcionar quando o ESP está conectado ao Thonny através de cabo USB. Isto não acontece se o ESP estiver conectado à IDE do Arduino (comandos podem ser enviados pelo monitor serial a 115200-8N1 e CRLF.

## Fotos e vídeos do circuito funcionando

[Vídeo no Youtube](https://youtu.be/9JnDZj8tckg). As legendas contém texto explicativo.

### Trabalho futuro

Pretendo apresentar um circuito mínimo com ESP32. Tenho algumas referências:
	
- https://thecustomizewindows.com/2019/06/required-circuit-for-bare-minimum-esp32-module/
- https://electronics.stackexchange.com/questions/448187/esp32-with-ftdi-programmer
- https://forum.arduino.cc/t/minimum-required-for-esp32/1100515/10
- https://mischianti.org/2021/03/06/esp32-practical-power-saving-manage-wifi-and-cpu-1/




