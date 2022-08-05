# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import webrepl
webrepl.start()
gc.collect()
# FN 20220713
import network, time

wifi_if=network.WLAN(network.STA_IF) 
wifi_if.active(True) # conecta ao ap conectado anteriormente no ESP32-S2 e no ESP8266. No ESP32-C3, quando testei, não guardou.
wifi_if.connect('NameOfNetworkTP', '0123456789') # preenche se quiser mudar
time.sleep(5)
if (wifi_if.isconnected() == False) :
   wifi_if.active(False)
   wifi_if=network.WLAN(network.AP_IF) 
   wifi_if.active(True)
   wifi_if.config(ssid='esp8266')
wifi_if.ifconfig()

from machine import Pin, I2C
import time
from ssd1306 import SSD1306_I2C

# Init Display
# scl and sda can be any pin on i2c bus 1
i2c  = I2C(0, scl=Pin(6), sda=Pin(5), freq=40000)
oled = SSD1306_I2C(72, 40, i2c)
# Title Screen
oled.fill(0)

oled.text(wifi_if.ifconfig()[0], 0, 0, 1)
oled.text(wifi_if.ifconfig()[0][6:], 0, 20, 1)
oled.show()
