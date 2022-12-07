# Composição de snippets

![](teste.gif)

## Objetivo

Criar um programa que permita acessar o ESP32 quando ele recebe energia de uma bateria de 3.6V conectada a Vcc.

## Justificativa

O ESP32 tem tensão de operação nominal de 3.3V, com tensão máxima de 3.6V. Quando conectado à porta USB, usa um regulador de tensão que ajusta os 5V da USB para 3.3V. Entretanto, 5V não é um valor de tensão de alimentação muito prático pois requer ou um gerador stepup (ex. power bank) ou quatro pilhas AA/AAA ou duas baterias LiPo ou LiIon (ex.:18650 e baterias para telefone celular). Essas soluções tornam o dispositivo grande e caro. Existe um agravante pois a tensão dessas baterias pode chegar a 4.2V (LiPo) quando completamente carregadas, logo, algum tipo de regulador de tensão é necessário.

A maioria das placas baseadas em ESP32 usa reguladores de tensão similares a AMS1117. Este tem dropout da ordem de 1.6V. Nestas placas é certo que uma única bateria LiPo ou LiIon não será capaz de ligar o ESP - não por falta de tensão, mas porque o dropout é muito alto.

Há placas com outros modelos de regulador de tensão e há reguladores de tensão com dropout da ordem de 0.3V. Estes outros modelos de placas não tem diagrama esquemático na web, mas o regulador de tensão embutido tem encapsulamento diferente dos AMS1117 e similares, sendo mais parecidos com os de dropout da ordem de 0.3V.

Na dúvida, convém testar se uma bateria com tensão de 3.6V conectada a Vcc é capaz de ligar o ESP. 

## Procedimento

- Desenvolver a plataforma de teste;
- Testar;

## Resultados

### Desenvolver a plataforma de teste

A placa que será testada é MH-ET Live ESP32 Minikit (http://esp32.net/images/MH-ET-LIVE/ESP32-MiniKit/MH-ET-LIVE_ESP32-MiniKit.jpg, https://doc.riot-os.org/group__boards__esp32__mh-et-live-minikit.html).

Para testar se uma bateria com tensão de 3.6V conectada a Vcc é capaz de ligar o ESP, a energia não pode ser fornecida pela porta USB pois a energia fornecida pela porta também passa pelo pino Vcc. A conexão da bateria causaria um curto-circuito que pode danificar a porta USB.

Com Vcc a 3.6V os níveis de tensão dos sinais USB não são atingidos. Provavelmente a comunicação pela USB não funcionaria. Outras formas de comunicação com usuário são necessárias. Há várias alternativas (wifi, bluetooth, LEDs, displays,...). Neste caso escolheu-se wifi, pela flexibilidade (wifi modos access point e station; web server e client; webREPL). 

Micropython permite programar o dispositivo por WebREPL. Uma alternativa seria escrever um servidor web que executaria os testes, mas, escrever o servidor web que cobre todas as funcionalidades cobertas por WebREPL seria muito complicado.

A plataforma de teste mais conveniente, então, é composta por um ESP32 executando Micropython e WebREPL. Isto seria suficiente para um teste com um único ESP pois o nome da rede (AP) seria único e, conectado à essa rede, o IP seria o padrão. Como, antes de estabelecer a conexão por WebREPL, podem ocorrer erros e variações nas configurações de wifi, esses erros e variações poderiam passar despercebidos, então acrescentou-se ao circuito um display.

O programa deve ser executado na inicialização do dispositivo, logo, modificou-se `boot.py` para cumprir essa função. O arquivo está na mesma pasta deste README.

O hardware ficou como o do snippet /programas/MicroPython/snippets/configDisplay .

### Testar

Ligar o hardware à bateria. No caso usei uma Li-Ion que, sem carga, fornecia um pouco mais de 4.0V. Conectei em Vcc e GND. Em pouco tempo o ESP32 iniciou e o display mostrou IP, nome da rede e senha. O ESP32 foi iniciado como Access Point wifi.

Às 8:28 conectei ao webREPL, pelo wifi, usando um desktop como estação wifi (cliente) e executando um navegador. Pelo webREPL enviei os comandos abaixo:

```python
import machine, time
p2=machine.Pin(2,machine.Pin.OUT)
while True :
	p2.on()
	time.sleep(1)
	p2.off()
	time.sleep(1)

```

às 9:50 interrompi e digitei estes:

```python
while True :
	oled.fill(1)
	oled.show()
	time.sleep(1)
	oled.fill(0)
	oled.show()                                                                                                                                   
	time.sleep(1)
```

- Chequei às 10:28 e a placa continua respondendo a comandos enviados através de webREPL.
- Chequei às 13:10 e a placa apagada.

Novo teste, começando às 7:55, após carga completa da bateria;
Continua piscando às 11:48
Continua piscando e conectado com webREPL às 12:30
- Chequei às 13:58 e a placa apagada.

Para facilitar, encapsulei os snippets acima em funções que defino em `teste3V6.py`. Desta forma posso importar o módulo e executar com uma chamada de função. As funções que defino são:
	
- piscaLED()
	- A maioria dos ESP32 tem um LED conectado à GPIO2.
	- Esta função configura a GPIO2 como saída e, a cada segundo, alterna entre HIGH e LOW, fazendo o LED piscar.
- piscaDisplay(oled)
	- o paraâmetro oled é a referência para o display. Corresponde à variável `oled` definida em `boot.py`;
	- acende e apaga todos os pixels do display a intervalos de 1 segundo;

## Discussão e Conclusão

A placa MH-ET Live ESP32 Minikit funciona adequadamente quando recebe energia de uma bateria de 3V6 através do pino Vcc. A autonomia da bateria testada supera duas horas. 

- mantém comunicação por wifi;
- recebe comandos através de webREPL;
- executa comandos de GPIO e display (SSD1306);

