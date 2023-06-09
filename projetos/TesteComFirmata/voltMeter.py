import pyfirmata
import time
import myDT

nCanais = 6   # quantidade de canais a ativar. Os canais ativados são enumerados sequencialmente a partir de ZERO.
nomeDoLog='log.csv'  # nome do arquivo onde armazenar as medidas
intervalo = 10     # intervalo entre amostras, em segundos. Uma amostra corresponde a uma linha da tabela. A linha da tabela consiste em data/hora e nCanais leituras de tensão. A primeira leitura é feita após um intervalo.

board = pyfirmata.ArduinoMega('/dev/ttyACM0')
it = pyfirmata.util.Iterator(board)
it.start()


for i in range (0,nCanais-1)
	board.analog[i].enable_reporting()

while (true) :
	time.sleep(intervalo # espera 10 segundos
	[posixt, t]=myDT.requestTimefromNtp()
	isot=myDT.isoformat(t)
	linha=[isot]
	for i in range (0,nCanais-1)
		volt=board.analog[i].read()
		linha= linha + volt]
	# https://www.geeksforgeeks.org/how-to-append-a-new-row-to-an-existing-csv-file/
	# https://realpython.com/python-csv/
	with open(nomeDoLog, 'a') as f_object:
 
		# Pass this file object to csv.writer()
		# and get a writer object
		writer_object = writer(f_object)
		# Pass the list as an argument into
		# the writerow()
		writer_object.writerow(linha)

# não precisa de close: https://stackoverflow.com/questions/45954214/python-automatically-closing
