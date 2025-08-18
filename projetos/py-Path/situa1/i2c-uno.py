# Exemplo de https://docs.micropython.org/en/latest/library/machine.I2C.html
# adaptado para comunicar com arduino UNO

from machine import I2C

i2c = I2C(scl=Pin(8), sda=Pin(9), freq=100000)          # create I2C peripheral at frequency of 100kHz (https://www.arduino.cc/reference/en/language/functions/communication/wire/)
                                # depending on the port, extra parameters may be required
                                # to select the peripheral and/or pins to use

i2c.scan()                      # scan for peripherals, returning a list of 7-bit addresses

i2c.writeto(42, b'123')         # write 3 bytes to peripheral with 7-bit address 42
i2c.readfrom(42, 4)             # read 4 bytes from peripheral with 7-bit address 42

i2c.readfrom_mem(42, 8, 3)      # read 3 bytes from memory of peripheral 42,
                                #   starting at memory-address 8 in the peripheral
i2c.writeto_mem(42, 2, b'\x10') # write 1 byte to memory of peripheral 42
                                #   starting at address 2 in the peripheral