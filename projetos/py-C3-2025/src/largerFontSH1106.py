# it works! 2025-06-14

import time
from writer import Writer
import sh1106

from machine import Pin, I2C
i2c=I2C(0, scl=Pin(6), sda=Pin(5)) # ok, neste ESP os pinos são 5 e 6

oled = sh1106.SH1106_I2C(128, 64, i2c)
oled.fill(0)

oled.text('"Hello World"', 28, 12, 1) # test default font size
oled.show()
time.sleep(5)

# adapted from https://forum.micropython.org/viewtopic.php?t=11399
# Large Font
import freesans20

WIDTH = const(128)
HEIGHT = const(64)

# Create the I2C interface.
ssd = oled
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config

wri = Writer(ssd, freesans20)
Writer.set_textpos(ssd, 28, 12)  # verbose = False to suppress console output
wri.printstring('Hello World\n')
ssd.show()