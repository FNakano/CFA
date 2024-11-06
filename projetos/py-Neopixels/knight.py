import neopixel
import machine
import time

def fade (np, f):
    aux=[0,0,0]
    for i in range(0,np.n):
        aux[0]=np[i][0]//f
        aux[1]=np[i][1]//f
        aux[2]=np[i][2]//f
        np[i]=tuple(aux)

def knightRider(np, f, color=(200,0,0)):
    for i in range(0,np.n):
        fade(np, f)
        np[i]=color
        np.write()
        time.sleep(0.2)
    for i in reversed(range(0, np.n)):
        fade(np, f)
        np[i]=color
        np.write()
        time.sleep(0.2)

def cKnight(np, f, color=(200,0,0)):
    while (True):
        knightRider(np, f, color)

nnp=5 # number of neopixels
npp=2 # neopixels data pin

np=neopixel.NeoPixel(machine.Pin(npp), nnp)
