# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import webrepl
webrepl.start()
import sys
sys.path = sys.path + ['/lib/microdot', '/lib/aiorepl']
