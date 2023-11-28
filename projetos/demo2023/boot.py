# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import webrepl
webrepl.start()
import configAsAP
from time import sleep
sleep(2)
configAsAP.apUp()
configAsAP.setup()

