# Composição de snippets

![](teste.gif)

## Objetivo

Criar um programa que permita acessar o ESP32 quando ele recebe energia de uma bateria de 3.6V conectada a Vin.

## Justificativa

O ESP32 tem tensão de operação nominal de 3.3V, com tensão máxima de 3.6V. Quando conectado à porta USB, usa um regulador de tensão que ajusta os 5V da USB para 3.3V. Entretanto, 5V não é um valor de tensão de alimentação muito prático pois requer ou um gerador stepup (ex. power bank) ou quatro pilhas AA/AAA ou duas baterias LiPo ou LiIon (ex.:18650 e baterias para telefone celular). Essas soluções tornam o dispositivo grande e caro. Existe um agravante pois a tensão dessas baterias pode chegar a 4.2V (LiPo) quando completamente carregadas, logo, algum tipo de regulador de tensão é necessário.

A maioria das placas baseadas em ESP32 usa reguladores de tensão similares a AMS1117. Este tem dropout da ordem de 1.6V. Nestas placas é certo que uma única bateria LiPo ou LiIon não será capaz de ligar o ESP - não por falta de tensão, mas porque o dropout é muito alto.

Há placas com outros modelos de regulador de tensão e há reguladores de tensão com dropout da ordem de 0.3V. Estes outros modelos de placas não tem diagrama esquemático na web, mas o regulador de tensão embutido tem encapsulamento diferente dos AMS1117 e similares, sendo mais parecidos com os de dropout da ordem de 0.3V.

Na dúvida, convém testar se uma bateria com tensão de 3.6V conectada a Vin é capaz de ligar o ESP. 

## Procedimento

- Desenvolver a plataforma de teste;
- Testar;

### Desenvolver a plataforma de teste

Para testar se uma bateria com tensão de 3.6V é capaz de ligar o ESP, a energia não pode ser fornecida pela porta USB. Talvez seja fácil adaptar (quebrar) um cabo USB para fazer esse teste, porém, a comunicação pelo cabo USB ficaria comprometida pois os níveis de tensão do protocolo USB não são atingidos quando fornece-se 3.6V (e não 5V) através de Vin.

Sem comunicação pela USB, uma alternativa seria wifi.

Micropython permite programar o dispositivo por WebREPL. Uma alternativa seria escrever um servidor web que executaria os testes, mas, escrever o servidor web que cobre todas as funcionalidades cobertas por WebREPL seria muito complicado.

A plataforma de teste mais conveniente, então, é composta por um ESP32 executando Micropython e WebREPL. Isto seria suficiente para um teste com um único ESP pois o nome da rede (AP) seria único e, conectado à essa rede, o IP seria o padrão. Em um contexto com vários ESP32, aumenta a chance de erros de conexão de rede, que seriam difíceis de detectar sem algum tipo de mensagem no dispositivo e que fosse legível por pessoas. Por isso acrescentou-se um display.

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

