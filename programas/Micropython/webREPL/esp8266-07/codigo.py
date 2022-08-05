import machine, time
def curtissimo (pino, aceso=True) :
	# curto demais não dá para enxergar
	pino.value(aceso)
	time.sleep(0.02)
	pino.value(not aceso)
	time.sleep(0.3)

def curto (pino, aceso=True) :
	pino.value(aceso)
	time.sleep(0.1)
	pino.value(not aceso)
	time.sleep(0.3)

def longo (pino, aceso=True) :
	pino.value(aceso)
	time.sleep(0.5)
	pino.value(not aceso)
	time.sleep(0.3)

def longuissimo (pino, aceso=True) :
	# confunde com o longo
	pino.value(aceso)
	time.sleep(2)
	pino.value(not aceso)
	time.sleep(1)
	
def pausa (pino, aceso=True) :
	pino.value(not aceso)
	time.sleep(1)

def enviaDigito(digito, pino, aceso=True) :
	if (digito==0) :
		longo(pino, aceso=aceso)
		longo(pino, aceso=aceso)
	else :
		if (digito>=5) :
			longo(pino, aceso=aceso)
			digito=digito-5
		for i in range(0,digito) :
			curto(pino, aceso=aceso)

def enviaNumero(numero, pino, aceso=True) :
	while (numero>0) :
		digito=numero % 10
		numero=numero//10
		enviaDigito(digito, pino, aceso=aceso)
		pausa(pino, aceso=aceso)

def enviaIP(strIP, pino, aceso=True) :
	for i in range(len(strIP)) :
		# https://realpython.com/python-range/
		if (strIP[i]=='.') :
			longuissimo(pino, aceso=aceso)
		else :
			digito=int(strIP[i])
			enviaDigito(digito, pino, aceso=aceso)
		pausa(pino, aceso=aceso)

