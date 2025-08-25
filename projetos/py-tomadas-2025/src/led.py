"""
O que é: Arquivo de configuração do hardware dos LEDs.
O que faz:
  Cria variáveis globais (ao aplicativo) para acesso aos LEDs
O que espera-se que esteja neste arquivo:
  Criação das variáveis e funções para uso dos LEDs.
"""
from machine import Pin
import config
config.redled=Pin(3, Pin.OUT);
config.greenled=Pin(4, Pin.OUT);
config.blueled=Pin(5, Pin.OUT);
# LEDs could be configured as PWM and have their brightness controlled

def off ():
    config.redled.off()
    config.greenled.off()
    config.blueled.off()

off()
