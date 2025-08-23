from machine import Pin
import config
config.redled=Pin(3, Pin.OUT);
config.greenled=Pin(4, Pin.OUT);
config.blueled=Pin(5, Pin.OUT);
# LEDs could be configured as PWM and have their brightness controlled

def off ():
    config.redled.off()
    config.greenled.off()
    config.blueled.off()

off()
