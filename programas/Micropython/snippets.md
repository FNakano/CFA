# índice de snippets

- [configAsAP](snippets/configAsAP/configAsAP.py)
	- https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html#network-basics
- [configAsSta](snippets/configAsSta/configAsSta.py)
	- https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html#network-basics
- [configI2C](snippets/configI2C/configI2C.py)
	- Detalhes em snippets/configI2C
- [configDisplay](snippets/configDisplay/configDisplay.py)
	- Detalhes em snippets/configDisplay

## funcionalidades que precisei e que ainda não foram implementadas

### Conexão com EDUROAM

EDUROAM, a rede que autentica usuários de Internet em (muitas) universidades no mundo sem necessidade do usuário requisitar à instituição (que está visitando) o acesso, usa WPA2 Enterprise para fazer a autenticação e, como segundo método de autenticação, EAP ou MSChapV2.

Existe código em C para conectar ESP8266 ou ESP32 a EDUROAM (https://github.com/martinius96/ESP32-eduroam/blob/master/2022/eduroam/eduroam.ino), mas, em 2022, não existe biblioteca MicroPython que faça isso:
	
	- https://github.com/micropython/micropython/issues/8819
	- https://forum.micropython.org/viewtopic.php?t=12299
	- https://forum.micropython.org/viewtopic.php?f=18&t=10543&start=20
	- https://www.google.com/search?channel=fs&client=ubuntu&q=esp32+micropython+eduroam+authentication
