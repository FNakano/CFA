import config
import network
import time

config.wifi_if=network.WLAN(network.STA_IF)
config.wifi_if.active(True) 
config.wifi_if.config(hostname=config.myhostname)
config.wifi_if.connect(config.wifi_id, config.wifi_password)
config.blueled.on() # indicate that wifi is being connected
time.sleep(3) # wait for 3 seconds to wifi to connect
config.blueled.off() # finished 
if config.wifi_if.isconnected() :
    config.greenled.on() # wifi connected
else :
    config.redled.on() # wifi not connected
