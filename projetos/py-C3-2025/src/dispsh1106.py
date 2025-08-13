# SH1106 funcionou!
# acho que a versão de micropython que uso (1.23.0)
# 1) tem algum bug, talvez na classe framebuffer, então
# para o display mostrar texto precisa declarar um
# tamanho diferente e escrever a mensagem com um offset,
# como feito abaixo.
# 2) parece ter outro bug, de vazamento de memória, que só
# recupera quando tira o ESP da USB e devolve (um hard reset)
# FAZENDO O HARD RESET E EXECUTANDO O CÓDIGO O DISPLAY MOSTRA A MENSAGEM!
# REFERÊNCIA:
# https://www.reddit.com/r/esp32/comments/1jgxpd8/got_a_super_mini_esp32c3_with_042in_oled_finally/
# https://github.com/robert-hh/SH1106 (driver e exemplo de uso)

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

import sh1106
disp=sh1106.SH1106_I2C(132, 64, i2c) # este comando acende parte do display o que não é esperado e há muitos pixels mortos

disp.fill(0)
disp.text("Hello", 30, 12, 1)
disp.show() # estes comandos para apagar o display não funcionam.
# https://github.com/01Space/ESP32-C3-0.42LCD/blob/main/micropython/image/9.png
# https://pt.aliexpress.com/item/1005007701655528.html?spm=a2g0o.detail.pcDetailBottomMoreOtherSeller.1.7b6dymPSymPSrT&gps-id=pcDetailBottomMoreOtherSeller&scm=1007.40196.366991.0&scm_id=1007.40196.366991.0&scm-url=1007.40196.366991.0&pvid=839c3e2b-e8b3-4154-a477-c8b4ab01fe87&_t=gps-id:pcDetailBottomMoreOtherSeller,scm-url:1007.40196.366991.0,pvid:839c3e2b-e8b3-4154-a477-c8b4ab01fe87,tpp_buckets:668%232846%238107%231934&pdp_npi=4%40dis%21BRL%2132.74%2117.34%21%21%215.38%212.85%21%402103205117317077694484558e61f3%2112000041910607242%21rec%21BR%21822079684%21X&utparam-url=scene%3ApcDetailBottomMoreOtherSeller%7Cquery_from%3A

print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config
