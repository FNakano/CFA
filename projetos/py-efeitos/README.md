## Objetivo

Apresentar um dispositivo computacional vestível.

## Objetivos específicos

- Propor uma forma de documentar dispositivos vestíveis;
- Mostrar um uso combinado dos recursos de desenvolvimento (projetos anteriores, vestíveis, microPython, ESP8266)

## Introdução 

Um dispositivo vestível é ...

Construir um dispositivo vestível traz desafios multidisciplinares: têxtil (materiais e modelagem) e computação (hardware, software, redes, sistemas de informação)

(introdução sobre têxteis, materiais e modelagem)

O dispositivo eletrônico propriamente dito é um conjunto de componentes, geralmente, montado sobre uma placa de circuito impresso. Os componentes implementam sensores, atuadores, transceptores de rádio (usados em redes sem fio). A coordenação do funcionamento desses componentes é feito por um microcontrolador (que também é um componente). Microcontroladores são programáveis.

Python é uma linguagem de programação muito popular entre programadores e público em geral. A linguagem é de *tipagem fraca* e construída para ser interpretada, o que a torna fácil de aprender e executar. Em consequência, resultados perceptíveis (e motivadores) são obtidos rapidamente, o que permite dizer, por exemplo: 

> Python is a programming language that lets you work more quickly and integrate your systems more effectively. You can learn to use Python and see almost immediate gains in productivity and lower maintenance costs (https://www.python.org/about/). 

MicroPython é uma implementação de Python 3 para microcontroladores e outros ambientes com recursos computacionais limitados (http://micropython.org/).

Este artigo é um esboço, extensível, da apresentação de uma cinta (suporte) peitoral em que um dispositivo programável, que controla luzes, mede temperatura, umidade do ar e intensidade de luz, é ancorado.

Referencial, produtos similares, diferenciais, ... em detalhes

## Materiais e métodos

### Listas de equipamentos e materiais

| Quantidade | Nome | Exemplo |
| --- | --- | --- |
| 1 | Witty Board | https://github.com/FNakano/CFA/tree/master/componentes/controladores/ESP/ESP8266#wittyboard |
| 1 | DHT22 | https://www.baudaeletronica.com.br/sensor-de-temperatura-e-umidade-dht22.html |
| 1 | Header 90 graus | https://www.baudaeletronica.com.br/barra-de-pinos-1x40-vias-15mm-90-graus.html |
| 1 | Placa de circuito impresso | https://www.curtocircuito.com.br/placa-de-circuito-impresso-ilhada-de-fibra-de-vidro-5x10-cm.html |
| 1 | Power Bank | https://www.daisojapan.com/p-38028-mobile-battery-pack-35-x-73-x-1-in-12pks.aspx |
| 1 | Passador / Regulador| https://produto.mercadolivre.com.br/MLB-1082468221-regulador-passador-plastico-preto-50mm-100-un-_JM |
| 1m | Alça CA 30mm |  https://produto.mercadolivre.com.br/MLB-996570080-alca-cadarco-ca-bolsas-mochilas-preto-30mm-rolo-50-metros-_JM?quantity=1&variation_id=33082744624 |
| 1m | Alça CA 50mm |  https://produto.mercadolivre.com.br/MLB-1307623290-alca-cadarco-ca-polipropileno-50mm-rolo-50m-escolha-a-cor-_JM#reco_item_pos=10&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=a6100f98-58ef-4710-b944-8aa776ec3a62 |

### Etapas do desenvolvimento

- Instalar Micropython, conforme https://github.com/FNakano/CFA/tree/master/programas/Micropython;
- Instalar WebREPL, conforme https://github.com/FNakano/CFA/tree/master/programas/Micropython/webREPL
- Construir programa inicial;
- Construir vestível inicial;
- Refinar (ou usar SCRUM,...)
- ...

## Resultados

### Testes executados

Fotos, vídeos e instruções sobre como reproduzir os testes e usar o produto

### Vestível

Diagramas e fotos: Baseado neste outro projeto: https://github.com/FNakano/CFA/tree/master/projetos/suportePeitoCostas.

O fecho foi mudado para a lateral da cinta, tornando o uso da cinta mais confortável, mas traz alguma dificuldade para vestir. As medidas e a forma de fixação das tiras por alfinete de segurança foi mantido. 

A placa de circuito impresso é alinhavada na cinta, próximo à axila, o powerbank também. A matriz de LEDs é costurada na cinta, no centro do peito.

### Dispositivo

Apresentar diagrama ou tabela de ligações e foto. Caso seja idêntico a algum projeto anterior, citar o projeto anterior, que DEVE conter esta informação.

Usa um wittyboard: https://github.com/FNakano/CFA/tree/master/componentes/controladores/ESP/ESP8266#wittyboard

| Wittyboard | DHT22 | Matriz de LEDs |
| --- | --- | --- |
| Vcc (5V) | Vcc | Vcc |
| GND | GND | GND |
| GPIO5 | D |  |
| GPIO12 |  | Din (do LED 1) |

Na matriz de LEDs todos os Vcc são interconectados e todos os GND são interconectados. O pod Dout do primeiro LED é conectado ao Din do segunodo LED e repetido para os LEDs seguintes (ié Dout do LED 2 conectado no Din do LED 3, Dout do LED 3 conectado no Din do LED 4, ..., até o LED 8. Dout do LED 9 é deixado desconectado).


### Programa

História sobre o desenvolvimento do programa, resumo de sua organização e arquitetura, ou, interface (API);

- [Manual de Referência](Ref.md)
- [Manual do Usuário (API)](API.md)

## Discussão e Conclusão

