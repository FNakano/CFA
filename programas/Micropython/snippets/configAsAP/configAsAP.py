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

# https://randomnerdtutorials.com/micropython-esp32-esp8266-access-point-ap/
# este funcionou no ubuntu 22.04 para conectar no web repl.
# Quando conectado ao AP, o IP do ESP32 é 192.168.4.1 . Para enviar comandos REPL, conectar a ws://192.168.4.1:8266
# 2022-12-05-111502
