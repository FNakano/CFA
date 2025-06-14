# it works! 2025-06-13

import machine
import time
from writer import Writer
from ssd1306 import SSD1306_I2C

i2c=machine.I2C(0)  # the only i2c in esp32 c3 supermini
oled = SSD1306_I2C(72, 40, i2c)
oled.fill(0)

oled.text('"Hello World"', 0, 0, 1) # test default font size
oled.show()
time.sleep(5)

# adapted from https://forum.micropython.org/viewtopic.php?t=11399
# Large Font
import freesans20

WIDTH = const(72)
HEIGHT = const(40)

# Create the I2C interface.
ssd = oled
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config

wri = Writer(ssd, freesans20)
Writer.set_textpos(ssd, 0, 0)  # verbose = False to suppress console output
wri.printstring('Hello World\n')
ssd.show()