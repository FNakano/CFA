dd

## BH1750FVI - Sensor de luz, I2C, calibrado:

- [blog masterwalker](https://blogmasterwalkershop.com.br/arduino/como-usar-com-arduino-sensor-de-luminosidade-gy-302-bh1750/)
- [blog filipeflop](https://www.filipeflop.com/produto/sensor-de-luz-bh1750fvi-lux/)

### Testes

Testei duas bibliotecas:

- <https://github.com/RobTillaart/BH1750FVI_RT>

Esta, é bem documentada, mas deu erro de compilação para o ESP8266 - falta uma variável `_factor` na biblioteca. 
Não testei para Arduino.

- <https://github.com/wollewald/BH1750_WE>

Esta outra compila e executa, aparentemente, bem. No exemplo padrão, a medida de iluminância vai até 54612.5 lux. Descomentando as linhas abaixo, no momento, estou com 113985.1875lux, às 10:33, com sol incidindo diretamente. Acredito que a precisão não seja tão alta quanto número faz presumir, mas a medida nessa faixa de iluminância é útil (para a aplicação que tenho em mente).

```c
  myBH1750.setMode(CLM);  // uncomment if you want to change default values
  myBH1750.setMeasuringTimeFactor(0.45); // uncomment for selection of value between 0.45 and 3.68
```

![biblioteca que escolhi na IDE do Arduino](Captura%20de%20tela%20de%202020-10-23%2010-42-29.png)

[Recomendação baseada na leitura da norma feita por outra pessoa](https://engplanilhas.com.br/a-nbr-5413-e-os-niveis-de-iluminancia-nos-ambientes-de-trabalho/)

De 500 a 750 lux para tarefa de escritório normais, até 1000lux. Mais que isso se visualização foi crítico para a realização da tarefa.

[Recomendação de níveis de iluminância em escritórios](http://www.forumdaconstrucao.com.br/conteudo.php?a=3&Cod=1859).

Acima de 500 lux para tarefas que requerem média atenção, entre 2k e 5klux para trabalho com monitor com alto brilho por tempo prolongado.


