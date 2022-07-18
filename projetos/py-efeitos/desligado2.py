# Define uma função para ser executada.
# Baseado em https://forum.micropython.org/viewtopic.php?t=4192#p26506


import machine, neopixel

def my_test():
  np=neopixel.NeoPixel(machine.Pin(12),9)
  r=(16,0,0)
  for i in range(9):
    np[i]=r
  np.write()

# importa com import desligado2
# executa com desligado2.my_test()

