# teste3V6.py
# Programas de teste para durabilidade da bateria.
# Depende da execução de boot.py

import machine, time
global oled

def piscaLED():
	p2=machine.Pin(2,machine.Pin.OUT)
	while True:
		p2.on()
		time.sleep(1)
		p2.off()
		time.sleep(1)
	

def piscaDisplay(oled):
	while True:
		oled.fill(1)
		oled.show()
		time.sleep(1)
		oled.fill(0)
		oled.show()
		time.sleep(1)
	


