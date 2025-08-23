from machine import Pin, I2C, ADC
import config
config.i2c=I2C(0, sda=Pin(9), scl=Pin(8))
print (config.i2c.scan()) # if 60 is in the list, OLED display is connected to i2c