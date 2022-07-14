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

staif=network.WLAN(network.STA_IF) 
#staif.connect('SSID', 'PASSWORD') # preenche se quiser mudar
staif.active(True) # conecta ao ap conectado anteriormente
time.sleep(5)
staif.isconnected()
staif.ifconfig()
