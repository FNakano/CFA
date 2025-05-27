# ESP32 alimentado por 3V (duas pilhas)

![](teste.gif)

## Objetivo

Criar um programa que permita acessar o ESP32S quando ele recebe energia de duas pilhas comuns (3V) conectada a 3.3V.

## Justificativa

O ESP32 tem tensão de operação nominal de 3.3V, com tensão mínima de 1.8V; 2.3V ou 3.3 V, dependendo do que estiver conectado a ele (ex. memória PSRAM), e máxima de 3.6V (detalhes em https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf). Ligar o ESP32 a mais de 3,6V pode reduzir sua vida útil (o que pode não ser tão ruim) ou pode danificá-lo imediatamente (o que é ruim). Ligá-lo abaixo da tensão mínima causará instabilidade de funcionamento.

As placas de desenvolvimento com o chip ESP32S que conheço expõe os terminais de alimentação do chip no pino marcado 3.3 . Desta forma, injetar 3V nesse pino deve fazer o chip funcionar corretamente. Outros componentes da placa, como o conversor serial-USB (CH340 ou CP210?), o regulador de tensão (AMS1117 ou similar) ficarão desligados. Os LEDs e botões devem funcionar conforme o funcionamento normal. Nesta circunstância, a comunicação através da porta USB não operará. 

Pretende-se testar se o ESP32S, os LEDs e um display OLED com controlador SSD1306 operam adequadamente quando conectados a duas pilhas comuns (3V). 

## Procedimento

- Desenvolver a plataforma de teste;
- Testar;

## Resultados

### Desenvolver a plataforma de teste

A placa que será testada é MH-ET Live ESP32 Minikit (http://esp32.net/images/MH-ET-LIVE/ESP32-MiniKit/MH-ET-LIVE_ESP32-MiniKit.jpg, https://doc.riot-os.org/group__boards__esp32__mh-et-live-minikit.html).

Para testar se as pilhas conectadas ao pino 3.3 ligam o ESP32S e o display, a energia não pode ser fornecida pela porta USB pois a energia fornecida pela porta também passa pelo pino 3.3 . A conexão da porta e das pilhas causaria um curto-circuito que pode danificar a porta USB e/ou o regulador de tensão.

Recebendo 3V os níveis de tensão dos sinais USB não são atingidos. Provavelmente a comunicação pela USB não funciona. Outras formas de comunicação com usuário são necessárias. Há várias alternativas (wifi, bluetooth, LEDs, displays,...). Neste caso escolheu-se wifi no modo *access point*, como em https://github.com/FNakano/CFA/tree/master/programas/Micropython/snippets/configAsAP . Depois de conectar é possível usar WebREPL (https://github.com/FNakano/CFA/tree/master/programas/Micropython/webREPL).

Micropython permite programar o dispositivo por WebREPL. Uma alternativa seria escrever um servidor web que executaria os testes, mas, escrever o servidor web que cobre todas as funcionalidades cobertas por WebREPL seria muito complicado.

A plataforma de teste mais conveniente, então, é composta por um ESP32 executando Micropython e WebREPL. Isto seria suficiente para um teste com um único ESP pois o nome da rede (AP) seria único e, conectado à essa rede, o IP seria o padrão. Como, antes de estabelecer a conexão por WebREPL, podem ocorrer erros e variações nas configurações de wifi, esses erros e variações poderiam passar despercebidos, então acrescentou-se ao circuito um display.

O programa deve ser executado na inicialização do dispositivo, logo, modificou-se `boot.py` para cumprir essa função. O arquivo está em https://github.com/FNakano/CFA/tree/master/projetos/Teste3V6.

O hardware ficou como o do snippet /programas/MicroPython/snippets/configDisplay .

### Materiais

- Duas pilhas AA;
	- preferencialmente novas para eliminar uma fonte de incerteza;
- Um suporte para duas pilhas AA;
- Uma placa MH-ET Live ESP32 Minikit (outras placas devem funcionar);
- Protoboard com 30 pontos ou mais (usei um com 400 pontos por falta de um menor);
- Um display OLED com controlador SSD1306;

### Testar

Precisei de um suporte para duas pilhas e protoboard para conectar o pino 3.3 do ESP, o Vcc do display e o positivo do suporte de pilhas. Após o tempo de boot do ESP32S o display mostrou IP, nome da rede e senha. O ESP32S foi iniciado como Access Point wifi.

Outras maneiras de testar estão em https://github.com/FNakano/CFA/tree/master/projetos/Teste3V6.

Em um segundo teste, um mês depois, para completar esta postagem, religuei as mesmas pilhas, novas no mês passado, e que não usei para outra coisa nesse intervalo. Às vezes os ESP ligava, às vezes o display mostrava mensagens. Funcionamento intermitente.

Chequei o circuito ligando na USB. O wifi ligou, consegui conectar-me ao webrepl e enviar comandos.

Voltei às pilhas, pareceu funcionar, consegui conectar-me ao webrepl e enviar comandos. Quando tentei reproduzir, para gravar um vídeo, não consegui.

Pensei que poderia ser mau contato, até deu essa impressão pois quando desconectei e reconectei um pino de energia, consegui testar com sucesso, mas, novamente, quando montei para gravar o vídeo, o display não acendeu, ou, o ap wifi não iniciou e não apareceu na lista de redes do computador (que usei como apoio).
## Vídeos

https://youtu.be/By90tkBp8Sw - Falha 2

https://youtu.be/pNeKKAd_duc - Falha 1

https://youtu.be/qMzEqPYUp4k - teste ligado na USB


## Discussão e Conclusão

O funcionamento a 3V pode ser intermitente, NÃO recomendo.

A placa MH-ET Live ESP32 Minikit pode até funcionar adequadamente quando recebe energia de duas pilhas (3V) através do pino 3.3 mas com frequência alta, não funciona.

Testes de autonomia não foram realizados. 

Foi realizado um teste com pilhas já gastas. O brilho do LED indicador de energia varia ligeiramente - interpreto esse sinal como o ESP32S tentando inicializar mas *apagando* por falta de energia. A isto se deu o nome de *brown out*, em analogia a um *desmaio*.

## Veja também

[ESP32 a 3V6 (uma bateria LiPo ou LiIon)](https://github.com/FNakano/CFA/tree/master/projetos/Teste3V6)

