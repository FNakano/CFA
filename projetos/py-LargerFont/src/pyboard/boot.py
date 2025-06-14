# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import webrepl
webrepl.start()
gc.collect()
# created FN 20220713
# modified FN 20250613
import network, time


wifi_if=network.WLAN(network.STA_IF) 
wifi_if.active(True) # conecta ao ap conectado anteriormente no ESP32-S2 e no ESP8266. No ESP32-C3, quando testei, não guardou.
wifi_if.connect('lab8', 'lab8arduino') # preenche se quiser mudar
time.sleep(10)
    
print (wifi_if.ifconfig())