## Procedimento

- instalar a biblioteca SSD1306
- conectar o display à placa controladora
- enviar comandos ao display através de REPL

## Introdução

O modelo específico de display é SSD1306. É um display gráfico, monocromático, OLED. A rigor, o controlador do display é SSD1306 e uma variedade de displays gráficos OLED podem ser conectados a ele. O que usei tem 0.91 pol. e resolução de 128x32 pixels. Como geralmente o display e o controlador compõe uma mesma placa, por simplicidade, usa-se SSD1306 para designar o modelo do conjunto.

A comunicação entre placa controladora e display é feita através de I2C (snippets/configI2C). As configurações de I2C são resolvidas na biblioteca apropriada e as configurações de display são resolvidas na biblioteca SSD1306.py. Esta biblioteca já fez parte do (projeto) Micropython mas não está mais listada na documentação (https://docs.micropython.org/en/latest/library/index.html). Atualmente (2022-12-05), ela pode ser instalada usando o gerenciador de pacotes `upip` (https://docs.micropython.org/en/v1.15/reference/packages.html#upip-package-manager), que é uma versão do `pip` para Micropython. 

`upip` é um módulo de Micropython, logo, para ser usado precisa ser importado. No REPL da placa controladora, o comando `import upip` faz isso.

Tal como `pip`, `upip` baixa a biblioteca do display (e/ou qualquer outra) da Internet. Para isso, a placa controladora precisa de conexão à internet, geralmente feita por wifi, através de um AP (snippets/configAsSta/configAsSta.py)

Depois, para instalar a biblioteca do display, usar o comando `upip.install('micropython-ssd1306')`. O repositório que contém a biblioteca é https://github.com/stlehmann/micropython-ssd1306. A biblioteca é instalada na placa controladora, localmente, no diretório `/lib`.

## Instalar a biblioteca SSD1306

Em suma, o código para instalar a biblioteca é:
	
```
import network, time
staif=network.WLAN(network.STA_IF) 
staif.active(True) # conecta ao ap conectado anteriormente
staif.connect('NameOfNetworkTP', '0123456789') # preenche se quiser mudar
time.sleep(5)
staif.isconnected() # True se conectou
staif.ifconfig()    # Mostra o IP para conexão da parte "C" - anotar o IP
# depois da conexão com a Internet estabelecida
import upip                                                                 
upip.install('micropython-ssd1306')   
```

## Conectar o display à placa controladora

No ESP32S, os pinos usuais para I2C são 21=SDA e 22=SCL. Mais informação sobre I2C em snippets/configI2C. A placa microcontroladora também fornece energia para o display, logo, além de conectar esses pinos, os pinos 3.3V e GND também devem ser conectados. O GND serve tanto para energia quanto como tensão de referência (por exemplo, corresponde ao nível lógico ZERO).

| Display | Placa Microcontroladora (ESP32S) | ccc |
| --- | --- | --- |
| VCC | 3.3 | --- |
| GND | GND | --- |
| SDA | 21 | --- |
| SCL | 22 | --- |

## Enviar os comandos através de REPL

Os comandos estão em configDisplay.py

## Referências

- https://docs.micropython.org/en/latest/esp8266/tutorial/ssd1306.html
- 
