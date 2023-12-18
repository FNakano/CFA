# Título

**nota**: em 2021-09-11 usei este projeto como referência. Senti falta de alguma informação (que está no diário, felizmente). Aproveitei e fiz a revisão deste documento.

## Introdução (parte já foi feita na proposta)

[Proposta](proposta.md)

### Contextualização (o que se sabe) e Motivação (por que se quer)  (desnecessário, se for o mesmo da proposta)

[Proposta](proposta.md)

### Revisão Bibliográfica (informação que foi encontrada durante a execução)

- [Comparativo entre modelos de ESP32 com câmera](https://makeradvisor.com/esp32-camera-cam-boards-review-comparison/)
- [Outro comparativo - este com exemplos de programas](https://github.com/lewisxhe/esp32-camera-series)
- [Revisão do ESP32-CAM](https://makeradvisor.com/esp32-cam-ov2640-camera/)
- [Tutorial em Português para ESP32-CAM (Fernando K.)](https://www.fernandok.com/2019/04/esp32-com-camera-e-reconhecimento-facial.html)
- [Tutorial em Portuguès para TTGO-Camera](https://www.dobitaobyte.com.br/ttgo-t-camera-com-esp32-wrover/)
- [Repositório com exemplo para TTGO-Camera](https://github.com/lewisxhe/esp32-camera-series.git)

#### Conceitos e Terminologia (glossário)
### Organização do relatório (links, please)
## Objetivos (os gerais foram escritos na proposta, os específicos podem ser acrescentados)

Colocar o ESP32-CAM e o TTGO-Camera para funcionar.

## Materiais e Métodos ( quais são os ingredientes e o que fazer com eles para chegar nos resultados)

ESP-CAM

![espcam](IMG_20201016_201734966.jpg)

TTGO-Camera

![ttgo-camera](IMG_20201016_141507330.jpg)

## Resultados e indicadores de avaliação (resultados dos testes dos entregáveis - cada resultado como uma subseção, para facilitar links para o resultado específico)
### Entregáveis previstos (há informação adicional, dependendo do tipo de entregável)

Código-fonte do exemplo que funcionou para ESP-CAM - usei o exemplo que vem com a biblioteca da placa ESP32. A placa que selecionei é ESP-CAM. Para programar, conectar GPIO0 a GND, clicar no upload do programa e resetar o ESP-CAM (apertar o botão de reset), [conforme a referência](https://randomnerdtutorials.com/esp32-cam-ai-thinker-pinout/).

[Código-fonte do programa que usei para ESP-CAM](CameraWebServer-FN)

Para o TTGO-CAM usei [este código](https://github.com/lewisxhe/esp32-camera-series/tree/master/sketch), [desta referência](https://github.com/lewisxhe/esp32-camera-series).

###### <a id="2021-12-03-153820" href="#2021-12-03-153820">2021-12-03-153820</a> 

Com ajuda de JgSeike: para o programa TTGO-CAM compilar, precisa das bibliotecas [OneButton](https://github.com/mathertel/OneButton)
 e [ESP8266 and ESP32 OLED driver for SSD1306 displays](https://github.com/ThingPulse/esp8266-oled-ssd1306)
. Uma busca no gerenciador de bibliotecas deve permitir que sejam identificadas univocamente e instaladas. Os links são os mesmos apresentados no gerenciador de bibliotecas (em *more info*) e são fornecidos aqui para maior detalhamento.


[Código-fonte do exemplo que funcionou para TTGO-CAMERA](TTGO-Camera-FN)

No código do exemplo, ajustar nome da rede e senha.

```c
/***************************************
 *  WiFi
 **************************************/
#define WIFI_SSID   "NOME DA SUA REDE WIFI"
#define WIFI_PASSWD "SENHA DA SUA REDE WIFI"
```

### Entregáveis não previstos (soluções para problemas colaterais)

#### Programação do ESP-CAM

Para enviar programa, conectar GPIO0 a GND, clicar no upload do programa e resetar o ESP-CAM (apertar o botão de reset).

#### Conexão do ESP-CAM à porta USB

O ESP-CAM não tem porta USB (não tem a interface USB-Serial, feita através do chip CH340, CP2102 ou FTDI232). A solução mais frequente é conectar através do FTDI232, que é um módulo separado.

É possível usar a placa de comunicação do WittyBoard (placa de baixo), ou um Arduino UNO, removendo o chip ATMEGA328P e conectando o ESP-CAM - TX com TX e RX com RX, 5V e GND.

#### Intensidade do sinal Wi-Fi

O ESP-CAM que tenho, a cerca de três metros do Access Point, indica intensidade de sinal (RSSI) de -80dBm. Pesquisei e segundo <https://randomnerdtutorials.com/esp32-cam-connect-external-antenna/>, está configurado para usar a antena externa, que não vem no pacote - acredito que a maioria dos ESP-CAM seja configurada desta forma. 

Isto faz o framerate em resolução VGA ser aprox. 1fps.

Foi isto que me fez passar para o TTGO-Camera.

**novidade**: Mudei a conexão da antena. Foi escolha melhor que comprar antena (prazo,tempo), encostar o componente (desperdício), ou jogá-lo no lixo - tive vontade pois nessa mudança de conexão sofri para desconectar o 'jumper' e sofri mais ainda para colocar o fio que serve como jumper para a antena F invertida. Arranquei um pod da PCI. Só valeu a pena porque deu certo. A intensidade do sinal foi de -80 para -60. Agora consegui -50dBm, framerate em VGA de 12fps.

![jumper](IMG_20201017_193522844.jpg)

![RSSI](Captura%20de%20tela%20de%202020-10-17%2019-32-08.png)

#### mDNS

Em redes com suporte a [mDNS](/componentes/protocolos/Ethernet/README.md#mdns), é possível associar um nome ao IP. No caso deste código, o nome é `esp32-cam.local`. Digitando esse nome na barra de endereços do navegador, se a rede tiver suporte, a página da câmera será mostrada.

[Código-fonte](/projetos/ESP32-CAM/CameraWebServerMDNS-FN)

Dispositivos Android não oferecem suporte para mDNS. Neste caso é necessário acessar por IP. Para saber o IP, fazer ping para a câmera a partir de um computador que tenha acessado a câmera através do nome mDNS.

## Discussão e Conclusão

Na minha opinião, dificultam o uso do ESP-CAM.

- a falta da conexão USB
- a falta de pino de RESET no header
- o posicionamento do botão de reset no lado do header ('costas') da placa.

### Consequências lógicas dos resultados (resultados deduzidos);
### Dificuldades que levaram às soluções colaterais
### Especulações/questionamentos a partir dos resultados (resultados induzidos);
### Desdobramentos possíveis (próximos passos, possibilidades, *spin-offs*);

Fazer vídeos de teste e demonstração como [este](https://youtu.be/AKbXOdZNY_E) do projeto de [tomada conectada](/projetos/ControlarTomadaPelaInternet/README.md). O vídeo no *picture-in-picture* foi feito com TTGO-Camera.

## Referências

[Proposta](proposta.md)

[Diário](diario.md)


## Usando placa de conexão do witty board para comunicar com ESP-CAM

| Pino Witty (Marcação na placa do ESP8266) | Pino ESP-CAM | descrição |
| --- | --- | --- |
| Vcc | 5V | Atenção, não é Vcc nem 3V3 no lado do ESP-CAM |
| GND | GND | --- |
| TXD | UOT | --- |
| RXD | UOR | --- |

O reset automático não funciona, para programar o ESP-CAM tem que conectar IO0 ao GND, conforme as instruções.

## Outra câmera de outro fornecedor, com lente wide

Em 2023-12-18 montei e testei outra ESP-CAM de outro fornecedor, com lente wide. O primeiro teste foi ligar e ver se há alguma mensagem reconhecível:

Mensagem de boot do ESP-CAM com lente wide, anes de qualquer programação:
	
```
rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
configsip: 0, SPIWP:0xee
clk_drv:0x00,q_drv:0x00,d_drv:0x00,cs0_drv:0x00,hd_drv:0x00,wp_drv:0x00
mode:DIO, clock div:2
load:0x3fff0018,len:4
load:0x3fff001c,len:6916
load:0x40078000,len:14368
load:0x40080400,len:4248
entry 0x400806e0
[0;32mI (72) boot: Chip Revision: 1[0m
[0;32mI (72) boot_comm: chip revision: 1, min. bootloader chip revision: 0[0m
[0;32mI (40) boot: ESP-IDF v4.0-beta2-174-g99fb9a3f7 2nd stage bootloader[0m
[0;32mI (40) boot: compile time 07:55:04[0m
[0;32mI (40) boot: Enabling RNG early entropy source...[0m
[0;32mI (46) boot: SPI Speed      : 40MHz[0m
[0;32mI (50) boot: SPI Mode       : DIO[0m
[0;32mI (54) boot: SPI Flash Size : 4MB[0m
[0;32mI (58) boot: Partition Table:[0m
[0;32mI (62) boot: ## Label            Usage          Type ST Offset   Length[0m
[0;32mI (69) boot:  0 phy_init         RF data          01 01 0000f000 00001000[0m
[0;32mI (77) boot:  1 otadata          OTA data         01 00 00010000 00002000[0m
[0;32mI (84) boot:  2 nvs              WiFi data        01 02 00012000 0000e000[0m
[0;32mI (92) boot:  3 at_customize     unknown          40 00 00020000 000e0000[0m
[0;32mI (99) boot:  4 ota_0            OTA app          00 10 00100000 00180000[0m
[0;32mI (106) boot:  5 ota_1            OTA app          00 11 00280000 00180000[0m
[0;32mI (114) boot: End of partition table[0m
[0;32mI (118) boot_comm: chip revision: 1, min. application chip revision: 0[0m
[0;32mI (125) esp_image: segment 0: paddr=0x00100020 vaddr=0x3f400020 size=0x28178 (164216) map[0m
[0;32mI (193) esp_image: segment 1: paddr=0x001281a0 vaddr=0x3ffbdb60 size=0x032ec ( 13036) load[0m
[0;32mI (198) esp_image: segment 2: paddr=0x0012b494 vaddr=0x40080000 size=0x00400 (  1024) load[0m
[0;32mI (200) esp_image: segment 3: paddr=0x0012b89c vaddr=0x40080400 size=0x04774 ( 18292) load[0m
[0;32mI (216) esp_image: segment 4: paddr=0x00130018 vaddr=0x400d0018 size=0x102acc (1059532) map[0m
[0;32mI (593) esp_image: segment 5: paddr=0x00232aec vaddr=0x40084b74 size=0x134c0 ( 79040) load[0m
[0;32mI (626) esp_image: segment 6: paddr=0x00245fb4 vaddr=0x400c0000 size=0x00064 (   100) load[0m
[0;32mI (641) boot: Loaded app from partition at offset 0x100000[0m
[0;32mI (641) boot: Disabling RNG early entropy source...[0m
2.0.0

max tx power=78,ret=0


```

Como não vi mensagem reconhecível, usei o código do exemplo (versão melhorada da que guardei faz uns anos), fiz ajustes no define do modelo, no ssid e no password, . O stream funciona bem. Usei Arduino IDE 1.8.19 com biblioteca ESPTOOL 4.5.1, placa esp32-wrover module com esquema de partição Huge App (3M App, No OTA, 1M spiffs) mensagens de compilação e gravação abaixo:
	
```
O sketch usa 1510545 bytes (48%) de espaço de armazenamento para programas. O máximo são 3145728 bytes.
Variáveis globais usam 70388 bytes (21%) de memória dinâmica, deixando 257292 bytes para variáveis locais. O máximo são 327680 bytes.
esptool.py v4.5.1
Serial port /dev/ttyUSB0
Connecting..................................
Chip is ESP32-D0WD (revision v1.0)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
Crystal is 40MHz
MAC: 08:3a:f2:1a:be:b0
Uploading stub...
Running stub...
Stub running...
Changing baud rate to 921600
Changed.
Configuring flash size...
Flash will be erased from 0x00001000 to 0x00005fff...
Flash will be erased from 0x00008000 to 0x00008fff...
Flash will be erased from 0x0000e000 to 0x0000ffff...
Flash will be erased from 0x00010000 to 0x00182fff...
Compressed 18992 bytes to 13110...
Writing at 0x00001000... (100 %)
Wrote 18992 bytes (13110 compressed) at 0x00001000 in 0.4 seconds (effective 376.6 kbit/s)...
Hash of data verified.
Compressed 3072 bytes to 137...
Writing at 0x00008000... (100 %)
Wrote 3072 bytes (137 compressed) at 0x00008000 in 0.0 seconds (effective 585.4 kbit/s)...
Hash of data verified.
Compressed 8192 bytes to 47...
Writing at 0x0000e000... (100 %)
Wrote 8192 bytes (47 compressed) at 0x0000e000 in 0.1 seconds (effective 800.3 kbit/s)...
Hash of data verified.
Compressed 1516848 bytes to 990081...
Writing at 0x00010000... (1 %)
Writing at 0x00014322... (3 %)
Writing at 0x0001a998... (4 %)
...

```

A qualidade da imagem e a velocidade de transmissão dos frames é bastante decente. Embora uma foto não seja bom indicador, [aí vai](./Images-2023/Captura%20de%20tela%20de%202023-12-18%2016-33-08.png)...

## Outra câmera do mesmo fornecedor


Em 2023-12-18 peguei uma ESP-CAM do mesmo fornecedor e liguei. Parece que tem um programa de demonstração carregado. 

```
⸮栦B⸮Lx!⸮޼^⸮⸮⸮⸮2N⸮⸮`z1⸮⸮[0;32mI (4121) camera_demo: Detected OV2640 camera, using JPEG format[0m
test_mode=1

[0;32mI (4621) system_api: Base MAC address is not set, read default base MAC address from BLK0 of EFUSE[0m
[0;32mI (4621) system_api: Base MAC address is not set, read default base MAC address from BLK0 of EFUSE[0m
[0;33mW (4661) phy_init: failed to load RF calibration data (0x1102), falling back to full calibration[0m
[0;32mI (4791) phy: phy_version: 4100, 6fa5e27, Jan 25 2019, 17:02:06, 0, 2[0m
[0;32mI (4791) camera_demo: Please connect to "ESP32_CAM"[0m
[0;32mI (4791) camera_demo: Open http://192.168.4.1/jpg for single image/jpg image[0m
[0;32mI (4791) camera_demo: Open http://192.168.4.1/jpg_stream for multipart/x-mixed-replace stream of JPEGs[0m
[0;32mI (4801) camera_demo: Free heap: 76052[0m
[0;32mI (4811) camera_demo: Camera demo ready[0m

```
O programa de demonstração configura o ESP como AP e passa algumas instruções.

Conectando ao AP ESP32_CAM e abrindo a pagina http://192.168.4.1/jpg_stream o ESP envia para a serial uma mensagem informando o frame enviado:
	
```
[0;32mI (475921) camera: Frame 792 done in 288 ms[0m
[0;32mI (476241) camera: Frame 793 done in 296 ms[0m
[0;32mI (476561) camera: Frame 794 done in 305 ms[0m
[0;32mI (476881) camera: Frame 795 done in 307 ms[0m
[0;32mI (477201) camera: Frame 796 done in 308 ms[0m
[0;32mI (477521) camera: Frame 797 done in 303 ms[0m
[0;32mI (477841) camera: Frame 798 done in 301 ms[0m
[0;32mI (478161) camera: Frame 799 done in 295 ms[0m
[0;32mI (478481) camera: Frame 800 done in 307 ms[0m
[0;32mI (478801) camera: Frame 801 done in 301 ms[0m
[0;32mI (479121) camera: Frame 802 done in 306 ms[0m
...
```
A página é muito simples, veja [captura de tela](./Images-2023/Captura%20de%20tela%20de%202023-12-18%2016-47-24.png)

A qualidade da imagem e taxa de transmissão são ruins. Talvez seja um hardware mais barato (ex. sem PSRAM) e com programa personalizado. Pode ser que esteja publicado mas, neste momento, não tenho motivo para procurar.
