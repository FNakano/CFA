import machine, time

i2c = machine.I2C(sda=machine.Pin(21), scl=machine.Pin(22))                 
i2c.scan() # writes I2C address of each responding device (slaves) SSD1306 address is 60=0x3C
from ssd1306 import SSD1306_I2C                                             
oled = SSD1306_I2C(128, 32, i2c)                                            
oled.fill(1)
oled.show()
time.sleep(1)
oled.fill(0)
oled.show()
time.sleep(1)

# if the device is connected to wifi using configSta.py code, the code below will display device's IP address.
                                                                                
oled.text(staif.ifconfig()[0],0,0,1)
oled.show()
