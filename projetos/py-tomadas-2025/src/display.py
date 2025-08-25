"""
O que é:
  Arquivo de configuração do hardware display OLED
  com controlador SSD1306.
O que faz:
  Cria variáveis globais (ao aplicativo) uso do display OLED
  Usa i2c.py através da variável config.i2c
O que espera-se que esteja neste arquivo:
  Criação das variáveis e funções para uso do display.
"""
import config
import ssd1306
from machine import Pin, I2C, ADC

config.disp=ssd1306.SSD1306_I2C(config.disp_width,config.disp_height,config.i2c)

# mess is a list
def message(mess) :
  config.messages=mess
  config.disp.fill(0)
  lin=0
  for m in mess :
    config.disp.text(m, 0, lin,1)
    lin=(lin+10)%config.disp_height
  config.disp.show()