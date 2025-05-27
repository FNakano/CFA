from machine import Pin, I2C
import time
import ssd1306 # https://github.com/micropython/micropython-esp32/blob/esp32/drivers/display/ssd1306.py


i2c=I2C(sda=Pin(5), scl=Pin(4))
display=ssd1306.SSD1306_I2C(128,64,i2c)
while True:
  display.fill(1)
  display.show()
  time.sleep(1)
  display.fill(0)
  display.text("Am I blinking?",10,10,1)
  display.show()
  time.sleep(1)
  display.fill(0)