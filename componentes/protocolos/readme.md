# Protocolos

## Níveis Lógicos

Frequentemente pergunta-se qual a correspondência entre tensões nos circuitos digitais e os níveis lógicos {0,1}. Esta correspondência é uma característica elétrica dos componentes e depende da sua construção e da tensão de alimentação do circuito. Em geral, componentes que pertencem à mesma família, tem níveis lógicos compatíveis. Isto torna desnecessário considerar esta característica elétrica em uma grande variedade de aplicações. Por outro lado, em aplicações onde misturam-se blocos com diferentes tensões de alimentação, ou blocos de famílias diferentes (ex. CMOS com TTL, ou com circuitos analógicos,...), esta característica deve ser considerada.

Numa primeira abordagem, pode-se convencionar que, em componentes em condições de operação nominais, existe uma faixa de tensão entre 0V e V1 que é considerado nível 0 e existe uma faixa de operação entre V2 e Vcc que é considerado nível 1. V1 e V2 são informados no manual do componente.

Por exemplo, de acordo com o [manual do ESP32](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf), seção *5.3-DC Characteristics*, para um pino de entrada, a faixa -0,3V a (0,25*Vcc) é considerada nível 0 e a faixa (0.75*Vcc) a Vcc+0,3V é considerada nível 1.

[Captura de tela da especificação do ESP32](Captura%20de%20tela%20de%202021-10-10%2015-08-31.png)

Para um pino de saída em nível 0, a tensão é menor que 0,1*Vcc e em nível 1, a tensão é maior que 0,9*Vcc - lembrando: componente sem defeitos e em condições nominais de funcionamento. O ESP32 tem Vcc entre 2,3V e 3,6V.

Outro exemplo, de acordo com [o *datasheet* de um fabricante](WS2812B-4pinos.pdf), LEDs RGB endereçáveis código WS2812B (mais conhecidos por NEOPIXEL), tem Vcc na faixa 3,5V a 5,3V e tensões abaixo de 0,3Vcc são consideradas nível 0 e tensões acima de 0,7Vcc são consideradas nível 1.

Combinando os dois exemplos, um circuito com o controlador ESP32 operando a 3,3V, por exemplo numa placa Node-32S, usado para controlar LEDs RGB endereçáveis alimentados pelos 5V fornecidos pela porta USB, resulta na seguinte situação para os níveis lógicos:

| Nível | saída do ESP32 (3,3V) | entrada de dados do LED (5V) |
| --- | --- | --- |
| zero | 0,33V(max) | 1,5V(max) |
| um | 3,0V(min) | 3,5V(min) |

Nesta situação, as tensões de nível lógico zero são compatíveis, mas as tensões de nível lógico um não são compatíveis. Isto pode causar instabilidade no funcionamento, por exemplo, leds acendendo com cores inesperadas ou leds não acendendo. (Também existe a possibilidade de uma particular seleção de componentes, em uma particular condição, funcionar corretamente)

Conversores de nível lógico (level shifters), são componentes com a finalidade de compatibilizar os níveis lógicos. Por exemplo, [o oferecido nesta loja](https://www.baudaeletronica.com.br/conversor-de-nivel-logico-bidirecional-de-8-canais-txs0108e.html).  

Existem outras formas, menos gerais, mais simples e mais baratas, de converter níveis lógicos. Em especial em comunicação unidirecional, como no caso do Node-32S com LED RGB endereçável, a conversão de nível lógico pode ser feita com um diodo e um resistor.

![Circuito conversor de nível lógico](Captura%20de%20tela%20de%202021-10-10%2016-04-04.png)

Neste circuito resulta:

| Nível | saída do conversor | entrada de dados do LED (5V) |
| --- | --- | --- |
| zero | 1,03V(max) | 1,5V(max) |
| um | 4,3V(min) | 3,5V(min) |

Os níveis são compatíveis, mas a imunidade a ruído e frequência de operação, provavelmente, são piores comparados a conversores de nível propriamente ditos. (Isto não deve ter repercussão na aplicação do grupo).

[Vídeo ilustrando o funcionamento](https://drive.google.com/file/d/1CXx0jf5LLD1OFlHDYG9Z94WVD7AAV0Im/view?usp=sharing).

[Placa - foto 1](20211010_140349.jpg)


[Placa - foto 2](20211010_141218.jpg)


[Programa do ESP32](strandtest-ParaESP32-2021-10-10.ino)

