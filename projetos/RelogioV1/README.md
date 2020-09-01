# Relógio V1 - Relatório
**nota**: Este é um teste/exemplo de uso do modelo de relatório. O relatório foi escrito mais de um ano após a execução.

## Introdução

### Contextualização (o que se sabe) e Motivação (por que se quer)

Em 2019 ocorreu o segundo oferecimento concomitante de CFA e e-Textiles. Logo nas primeiras aulas percebeu-se o potencial benefício no ensino e na aprendizagem que traria a construção e apresentação de um dispositivo.

Com a disciplina já em andamento, havia pouco tempo para aproveitar a oportunidade. 

O dispositivo de realização mais oportuna na época era um relógio. Aproveitava a recém adquirida placa controladora com display (ESP32 TTGO-Display) com baterias de [drone H36](https://www.jjrc.com/goodshow/h36-plam-sized-mini-drone.html) que estava sendo usado em uma Iniciação Científica. Não havia teste que mostrasse que a combinação de componentes funcionaria conforme o que se desejava, 

### ~~Revisão Bibliográfica~~

O display do TTGO é um SSD1306, OLED. A biblioteca escolhida foi a thingpulse.
É possível, em determinadas condições, usar as macros `__DATE__` e `__TIME__` para obter uma data de referência <https://forum.arduino.cc/index.php?topic=335765.0>.

#### ~~Conceitos e Terminologia~~
### Organização do relatório
## Objetivos ~~(questão de pesquisa colocada formal e explicitamente)~~ (o que quer fazer)

Construir e apresentar um relógio.

## Métodos
- Instalar Arduino IDE
- Instalar placa ESP32
- Instalar biblioteca SSD1306 da thingpulse
- Gerar fonte Roboto 48
- Laçar a placa TTGO no organizador de cabos <https://netcomputadores.com.br/p/20002-organizador-de-cabos-clone/4671>
- soldar conector JST 1.25 <https://github.com/Heltec-Aaron-Lee/WiFi_Kit_series/issues/5>


## Resultados e indicadores de avaliação
### Entregáveis previstos

![](imagens/IMG-20190923-WA0005.jpg)

![](imagens/IMG-20190923-WA0007.jpg)

![](imagens/IMG-20190923-WA0008.jpg)

[Código-fonte](arquivos/RelogioV1.ino)

O circuito realizado foi a solda do conector JST 1.25.



### Entregáveis não previstos (soluções para problemas colaterais)
    
## Discussão e Conclusão

- dificuldade em obter informações sobre a placa
    - se há restrições conhecidas para as baterias;
    - quais os pinos e protocolo de comunicação com o display.

### Consequências lógicas dos resultados;
### Dificuldades que levaram às soluções colaterais



### Especulações/questionamentos a partir dos resultados;
### Próximos passos

- reduzir consumo de energia
- usar conectividade wifi, bluetooth
    
## Referências

JJRC drone <https://www.jjrc.com/goodshow/h36-plam-sized-mini-drone.html>

## ~~Lista de divulgação dos resultados, quando for o caso.~~


Primeira versão do [Relógio Conectado](../relogioConectado/README.md).


