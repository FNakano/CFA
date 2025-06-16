from machine import Pin, I2C
# i2c=I2C(0) # aqui tem os pinos de comunicação com o display. Há comunicação (o endereço i2c responde)
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
disp=ssd1306.SSD1306_I2C(72,40,i2c) # este comando acende parte do display o que não é esperado e há muitos pixels mortos
# com 72,40 acende parte do display com um monte de pixels mortos
# com 72,32 acende o display todo com um monte de pixels mortos
disp.fill(1)
# disp.text("Hello", 0, 0, 1)
disp.show() # estes comandos para apagar o display não funcionam.
# https://github.com/01Space/ESP32-C3-0.42LCD/blob/main/micropython/image/9.png
# https://pt.aliexpress.com/item/1005007701655528.html?spm=a2g0o.detail.pcDetailBottomMoreOtherSeller.1.7b6dymPSymPSrT&gps-id=pcDetailBottomMoreOtherSeller&scm=1007.40196.366991.0&scm_id=1007.40196.366991.0&scm-url=1007.40196.366991.0&pvid=839c3e2b-e8b3-4154-a477-c8b4ab01fe87&_t=gps-id:pcDetailBottomMoreOtherSeller,scm-url:1007.40196.366991.0,pvid:839c3e2b-e8b3-4154-a477-c8b4ab01fe87,tpp_buckets:668%232846%238107%231934&pdp_npi=4%40dis%21BRL%2132.74%2117.34%21%21%215.38%212.85%21%402103205117317077694484558e61f3%2112000041910607242%21rec%21BR%21822079684%21X&utparam-url=scene%3ApcDetailBottomMoreOtherSeller%7Cquery_from%3A
