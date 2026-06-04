"""
O que é: Arquivo de ativação do hardware wifi.
O que faz:
  Cria variáveis globais (ao aplicativo) para acesso ao wifi
  Ativa o wifi
  Usa led.py através das variáveis config.redled,
  config.greenled, config.blueled
  Usa os LEDs para indicar estado
O que espera-se que esteja neste arquivo:
  Criação e ativação do wifi
Referências:
https://stackoverflow.com/questions/3965104/not-none-test-in-python
"""
import config
import network
import time

config.wifi_if=network.WLAN(network.STA_IF)
config.wifi_if.active(True) 
config.wifi_if.config(hostname=config.myhostname)
config.wifi_if.connect(config.wifi_id, config.wifi_password)
if config.blueled is not None : config.blueled.on() # indicate that wifi is being connected
time.sleep(3) # wait for 3 seconds to wifi to connect
if config.blueled is not None : config.blueled.off() # finished 
if config.wifi_if.isconnected() :
    if config.greenled is not None : config.greenled.on() # wifi connected
else :
    if config.redled is not None : config.redled.on() # wifi not connected
print (f'hostname: {config.myhostname} wifi configuration: {config.wifi_if.ifconfig()} notice: wifi is activated and may connect to an AP without message')
