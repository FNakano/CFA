import network
import time
from machine import Pin

wifi_if=network.WLAN(network.STA_IF)
wifi_if.active(True) 
wifi_if.connect('lab8', 'lab8arduino')
dois=Pin(2, Pin.OUT)
dois.on() # indicate that this program is being executed
time.sleep(2) # wait for 2 seconds to wifi to connect
if not (wifi_if.isconnected()) :
    dois.off() # no wifi
