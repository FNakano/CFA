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
print(wifi_if.config('hostname')
