import network
import time
from machine import Pin

wifi_if=network.WLAN(network.STA_IF)
wifi_if.active(True) 
wifi_if.connect('lab8', 'lab8arduino')
o=Pin(3, Pin.OUT)
o.on() # indicate that this program is being executed
time.sleep(2) # wait for 2 seconds to wifi to connect
if not (wifi_if.isconnected()) :
    o.off() # no wifi
# print(wifi_if.config('hostname'))
# wifi_if.config('hostname') esse parâmetro não existia em micropython 1.19
# query version using import sys, sys.version
# on version 3.4.0; MicroPython v1.19.1 on 2022-06-18 use
# command wifi_if.config('dhcp_hostname') to query hostname
# tested successfully pinging espressif.local on a desktop
# 2025-08-17

# looks like a dead end (for now)
# micropython default async webserver is microdot
# micropython async repl is aiorepl
# aiohttp is necessary to run aiorepl.
# aiohttp has no http server for micropyton
# microdot fails when aiorepl/aiohttp is in the device.
# https://github.com/micropython/micropython-lib/tree/master/micropython/aiorepl
# https://github.com/miguelgrinberg/microdot/issues/201
# https://github.com/micropython/micropython-lib/issues/788
# https://github.com/pfalcon/picoweb
# https://github.com/micropython/micropython-lib/tree/master/micropython/uaiohttpclient
# https://github.com/aio-libs/aiohttp/issues/6584
# https://docs.aiohttp.org/en/stable/web.html#aiohttp-web
