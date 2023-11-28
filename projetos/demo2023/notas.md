Há momentos em que por mais que se pense e se aja para evitar acidentes, algo passa despercebido e, consequentemente, quebra-se algo...

![Mesmo pensando...](./b89cc0c5-bd41-40ba-bfc8-abe96239301c.jpeg)

# Anotações feitas durante a construção

1. Muitas funcionalidades juntas, difícil pensar de maneira organizada, a idéia mais fácil é a que domina, pensamentos circulares, saltando de problema em problema, sem resolver nada.
	- Sugestão: faça um [esquema](./Irriga.jpg), escreva os detalhes.
	No caso, sei que componentes usar então o esquema com nomes de componentes é o caminho. Quando não se sabe que componente usar, pode compensar fazer um esquema com funcionalidades (análise de requisitos);
2. Nesses projetos um problema comum é a falta de pinos 5V e GND para fornecer energia a todos os componentes, então fiz uma [placa auxiliar](./c289f522-1022-4ce8-b70a-801b4493aef2.jpeg) [frente](./5bce53eb-ee5d-4659-9164-7bf15ba11e90.jpeg)
3. Inclui um resistor de 2,2\(\Omega\) para impedir que a corrente suba muito (com este resistor o limite é de cerca de 6A)
4. Tenho os componentes, então [os disponho sobre o que escolhi como base para montagem](./43340fa7-92b3-49b4-8f2d-a6a808e76eb1.jpeg)
5. Tenho dúvidas sobre como usar alguns componentes. Fui atrás da especificação deles;
	- https://os.mbed.com/users/mikeb/notebook/acs712-hall-effect-current-sensor/
	- file:///home/fabio/Downloads/ACS712_AllegroMicroSystems.pdf
	- O código do componente, impresso sobre ele, permite acessar mais detalhes (ACS712ELCTR-05B-T) é o componente que tenho e que mede corrente elétrica até 5A
	- https://os.mbed.com/teams/TVZ-Mechatronics-Team/code/L298N-Breakout-Test/
	- O L298 tem um regulador de tensão de 5V (LM78M05) então posso usá-lo no lugar da fonte de 5V, desde que forneça corrente suficiente;
	- https://www.alldatasheet.com/view.jsp?Searchword=78m05
	- LM78M05 fornece até 0.5A. O ESP com wifi ligado consome cerca de 0,2A. Até onde sei, é seguro confiar que o restante não passa de 0,3A.
	- para usar o regulador o jumper J5 deve estar colocado e deve se fornecer 12V no pino apropriado (se olhar a especificação com cuidado, algo entre 6V e 12V deve ser ok. Mais de 12V, embora o LM78M05 suporte tensões de até 35V, considerando a corrente consumida, fará ele esquente demais e queimar.
6. [Novo esquema](./529f38c9-492b-47de-b30e-7c4bd8c231f5.jpeg)
7. Gravar micropython no ESP32
	- fiquei irritado porque senti que gastei muito tempo procurando os arquivos e o comando para transferir; 
8. Configurar ESP32 com WebREPL e como Access Point
	- fiquei irritado porque senti que gastei muito tempo procurando os arquivos e o comando para transferir; 
	- Não funcionou de primeira;
	- O monte de fios espalhados me dá nos nervos;
	- Com o Thonny conectado o WebREPL não envia os caracteres que digito na página web;
	- O access point (AP) não inicia e o ESP não dá sinal;
		- Incluí no programa um comando para acender o LED se, ao iniciar o ESP, a interface AP é ativada;
		- parece que precisa esperar um pouco (sleep) para o AP entrar no ar;
9. Montar o circuito e testar o funcionamento ANTES DE FIXAR OS COMPONENTES;
	- Refatorei o código de configAsAP.py para definir funções (estas podem ser chamadas mais de uma vez);
	- `configAsAP.pot.read()` lê do ADS712;
	- `configAsAP.moist.read()` lê do sensor de umidade;
	- `configAsAP.pump.on()` liga a bomba;
	- `configAsAP.pump.off()` desliga a bomba;
