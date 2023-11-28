try:
  import usocket as socket
except:
  import socket

import network

import esp

import gc

from machine import Pin, ADC
from time import sleep

def apUp ():
    esp.osdebug(None)
    gc.collect()
    ssid = 'irrigador-AP'
    password = ''

    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=ssid, password=password)
    print (ssid + " " +password + " star")
    sleep(5)
    led=Pin(2,Pin.OUT)
    led.value(ap.active())
# https://randomnerdtutorials.com/micropython-esp32-esp8266-access-point-ap/
# este funcionou no ubuntu 22.04 para conectar no web repl.
# Quando conectado ao AP, o IP do ESP32 é 192.168.4.1 . Para enviar comandos REPL, conectar a ws://192.168.4.1:8266
# 2022-12-05-111502

def setup ():
    global pot
    global moist
    global pump
    pot = ADC(Pin(34))
    pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v
    moist = ADC(Pin(35))
    moist.atten(ADC.ATTN_11DB)       #Full range: 3.3v
    pump=Pin(33, Pin.OUT)
    print ('to read power use pot.read(), to read moisture use moist.read(), to turn water pump on use pump.on(), to turn pump off use pump.off()')
