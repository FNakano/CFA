"""
O que é: Arquivo de configuração do hardware I2C.
O que faz:
  Cria variáveis globais (ao aplicativo) para acesso ao
  barramento I2C
O que espera-se que esteja neste arquivo:
  Criação das variáveis e funções para uso do I2C.
"""
from machine import Pin, I2C
import config
config.i2c=I2C(0, sda=Pin(9), scl=Pin(8))
print (config.i2c.scan()) # if 60 is in the list, OLED display is connected to i2c