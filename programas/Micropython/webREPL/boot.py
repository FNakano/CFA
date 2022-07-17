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
#staif.connect('SSID', 'PASSWORD') # preenche se quiser mudar
wifi_if.active(True) # conecta ao ap conectado anteriormente
time.sleep(5)
if (wifi_if.isconnected() == False) :
   wifi_if.active(False)
   wifi_if=network.WLAN(network.AP_IF) 
   wifi_if.config('esp8266', '');
   wifi_if.active(True)
wifi_if.ifconfig()
