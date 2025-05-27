import time
import ssd1306
from machine import Pin, I2C, ADC
import lab8 # again, to get the wifi_if pointer

def testDisplay() :
  i2c=I2C(0, sda=Pin(21), scl=Pin(22))
  print (i2c.scan()) # if 60 is displayed ssd1306 display was found
  disp=ssd1306.SSD1306_I2C(128,32,i2c)
  disp.fill(1)
  disp.show()
  return disp

def testLDR() :
  a=ADC(Pin(36)) # the board has a LDR connected to this pin
  a.atten(ADC.ATTN_11DB)
  global light
  light=a.read()
  return light

from machine import Pin
def testLED() :
  d=Pin(18,Pin.OUT) # this pin is attached to a LED
  d.on()
  time.sleep(1)
  d.off()
  return d

def testMessage() :
  disp.fill(0)
  disp.text(lab8.wifi_if.ifconfig()[0], 0, 0)
  disp.text(str(light), 0, 10)
  disp.text(f"d = {d.value()}", 0, 20)
  disp.show()

disp=testDisplay()
a=testLDR()
d=testLED()
testMessage()
