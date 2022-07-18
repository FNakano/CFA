# Define uma função para ser executada.
# Baseado em https://forum.micropython.org/viewtopic.php?t=4192#p26506
# alguns links para aprender python

import machine, neopixel, time, random

def apaga():
  np=neopixel.NeoPixel(machine.Pin(12),9)
  # https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html
  b=(0,0,0)
  for i in range(9):
    # https://www.w3schools.com/python/python_for_loops.asp
    np[i]=b
  np.write()

def sem_energia():
  np=neopixel.NeoPixel(machine.Pin(12),9)
  r=(16,0,0)
  for i in range(9):
    np[i]=r
  np.write()

def anima():
  np=neopixel.NeoPixel(machine.Pin(12),9)
  b=(0,0,255)
  z=(0,0,0)
  for i in [0, 1, 2, 5, 9, 8, 7, 6, 3]:
    for j in range(9):
      if i==j :
        # https://www.w3schools.com/python/python_conditions.asp
        np[j]=b
      else :
		np[j]=z
    np.write()
    time.sleep(0.1)
# https://www.tutorialspoint.com/python/time_sleep.htm
# https://www.freecodecamp.org/news/python-sleep-time-sleep-in-python/

def aleatorio():
  np=neopixel.NeoPixel(machine.Pin(12),9)
  for i in range(9):
    # np[i]=(random.getrandbits(8), random.getrandbits(8), random.getrandbits(8))
    # falta energia para ligar todos os leds com brilho alto, por isso limitei
    np[i]=(random.getrandbits(5), random.getrandbits(5), random.getrandbits(5))
# http://docs.micropython.org/en/latest/library/random.html
# https://www.w3schools.com/python/module_random.asp
  np.write()

def animan(n):
  for i in range(n):
    anima()
  apaga()
