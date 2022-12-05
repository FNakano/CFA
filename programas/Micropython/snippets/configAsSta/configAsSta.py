import network, time
staif=network.WLAN(network.STA_IF) 
staif.active(True) # conecta ao ap conectado anteriormente
staif.connect('NameOfNetworkTP', '0123456789') # preenche se quiser mudar
time.sleep(5)
staif.isconnected() # True se conectou
staif.ifconfig()    # Mostra o IP para conexão da parte "C" - anotar o IP
