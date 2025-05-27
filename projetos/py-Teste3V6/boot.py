# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import webrepl
webrepl.start()

# configAP.py
try:
  import usocket as socket
except:
  import socket

import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'MicroPython-AP'
password = '123456789'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

# configDisplay.py
import machine, time

i2c = machine.I2C(sda=machine.Pin(21), scl=machine.Pin(22))
i2c.scan() # writes I2C address of each responding device (slaves) SSD1306 address is 60=0x3C
from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 32, i2c)
oled.fill(1)
oled.show()
time.sleep(1)
oled.fill(0)
oled.show()
time.sleep(1)

oled.text(ap.ifconfig()[0],0,0,1)
oled.text(ssid, 0, 10, 1)
oled.text(password, 0, 20, 1)
oled.show()

