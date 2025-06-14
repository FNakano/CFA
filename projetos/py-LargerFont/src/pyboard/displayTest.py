# it works! 2025-06-13
import machine
from ssd1306 import SSD1306_I2C

i2c=machine.I2C(0)  # the only i2c in esp32 c3 supermini
oled = SSD1306_I2C(72, 40, i2c)
oled.fill(0)

oled.text('"Hello World"', 0, 0, 1)
oled.show()
