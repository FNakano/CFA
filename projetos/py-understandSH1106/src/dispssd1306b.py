from machine import Pin, I2C
i2c=I2C(0, scl=Pin(6), sda=Pin(5)) # ok, neste ESP os pinos são 5 e 6

print('Scan i2c bus...')
devices = i2c.scan()  # ok, ele acha o display em 0x3c

if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))

  for device in devices:  
    print("Decimal address: ",device," | Hexa address: ",hex(device))

import ssd1306
disp=ssd1306.SSD1306_I2C(128, 64, i2c) # https://goldenmorninglcd.com/pt/exibi%C3%A7%C3%A3o-oled/0.42-polegadas-oled-72x40-ssd1306-branco-gme7240-01/
disp.text("DDDDDDDDDD", 27, 24, 1)
disp.text("ABCDEFGHIJ", 27, 32, 1)
disp.text("DDDDDDDDDD", 27, 40, 1)
disp.text("MMMMMMMMMM", 27, 48, 1)
disp.text("DDDDDDDDDD", 27, 56, 1)
disp.show()
