## IP por piscadas

(piscou 192.168.1.102 - funcionou)

Arquivo

## "Testes unitários"

import codigo
p=machine.Pin(2,machine.Pin.OUT)
p.on()

codigo.curto(p,aceso=False)

codigo.longo(p,aceso=False)

codigo.enviaDigito(9, p, aceso=False)

codigo.enviaNumero(91, p, aceso=False)

strip=wifi_if.ifconfig()[0]

codigo.enviaIP(strip, p, aceso=False) 
