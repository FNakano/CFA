# Display OLED e fontes maiores no ESP32-c3 supermini

![Modelos testados](./5073575761197248572.jpg)

Na foto, o da esquerda é o da 01Space (https://github.com/FNakano/CFA/tree/master/componentes/controladores/ESP/ESP32#esp32-c3-042lcd), o da direita é um genérico que encontrei no aliexpress ...

## Conclusão

Sim, é possível usar letras (fontes) maiores no ESP32-C3 supermini e no ESP32-C3 da O1Space.
 
## Objetivo

Verificar se é possível usar fontes maiores sem recompilar Micropython e, se for possível, documentar como fazer. Apresentar todo o código-fonte, referências e comentários (próprios e de terceiros).

## Motivação

Os displays OLED para ESP32 costumam ser menores que 1" diagonal e ter 128x64 pixels. Nos drivers mais comuns a fonte (letra/tipo) disponível tem 8 pixels. A combinação de display e fonte resulta em textos de difícil leitura, por terem letras muito pequenas. 

Usar fontes maiores permite melhorar e expandir a usabilidade do dispositivo. Para isso é desejável usar fontes maiores.

Caso, para usar fontes maiores seja necessário recompilar Micropython, essa solução pode tornar-se pouco prática já que Micropython é um projeto extenso e com muitas variações, logo, recompilá-lo requer um grande conjunto de ferramentas e é um processo trabalhoso. Por isso, deseja-se uma solução que não requeira recompilar Micropython.

O procedimento passa por explorar a Internet à busca de soluções e informação que possam ser combinadas para atingir o objetivo proposto. Caso já exista solução pronta, este trabalho se resume a fazer uma cópia (clonar) e referenciar essa solução.

## Resultado

Foi encontrada a solução https://github.com/peterhinch/micropython-font-to-py/ . *Font to py* contém 

1. um programa que converte fontes no formato `ttf` ou `otf` para mapas de bits em um arquivo-fonte (módulo) Python;
2. esse arquivo é carregado com um `import` e usado em displays que usam a classe `framebuffer` na construção do driver de display. Este é o caso do driver para display OLED SSD1306;
3. para usar o frame buffer dentro do driver de display usa-se a classe Writer (https://github.com/peterhinch/micropython-font-to-py/tree/master/writer) O exemplo simples de uso está em https://github.com/peterhinch/micropython-font-to-py/blob/master/writer/WRITER.md#21-the-writer-class

Esta solução foi testada em um 01Space ESP32-C3 com display OLED de 0.42" e em um ESP32-C3 supermini com display de mesmo tamanho. O código fonte para 01Space está em ./src/pyboard e o código fonte para ESP32-C3 supermini está em ./src-sh1106/pyboard.

Para testar o funcionamento, em um REPL ou em uma IDE como Thonny, depois de conectar a placa, transferir todos os arquivos do /src/pyboard adequado e usar o comando `import largerFontSSD1306` ou o comando `import largerFontSH1106`, conforme a placa e driver de display que estiver usando. Este teste é autocontido no sentido de não necessitar de mais módulos nem mais informação (ex. via web) para ser executado.


## Comentários

Pode ser necessário clonar a solução pois o desenvolvedor original pode modificar seu projeto e fazê-lo incompatível com versões anteriores, isto *quebra* este projeto. A maneira de evitar essa *quebra* é clonar o projeto.

Sobre os componentes, o da 01Space tem a distância entre as fileiras de terminais que não é múltipla de décimo de polegada de maneira que usar esse componente sobre uma placa de circuito impresso padrão é mais difícil. O genérico tem a distância entre as fileiras de terminais múltipla de décimo de polegada.

Tive algum problema com o da 01Space que me impede de atualizar o Micropython - o componenente não aceita ser programado com `esptool` então não tenho como atualizar o Micropython instalado nele. A versão instalada é 1.19.0 . No genérico posso atualizar. A versão instalada é 1.23.0 . Instruções para download e instalação de Micropython em https://micropython.org/download/ESP32_GENERIC_C3/ - para mim esta versão serviu para o ESP32-C3 supermini e para o 01Space.

O da 01Space usa driver de display modelo SSD1306 (https://github.com/micropython/micropython-esp32/blob/esp32/drivers/display/ssd1306.py), o genérico usa driver de display modelo SH1106 (https://github.com/robert-hh/SH1106).

## Outras referências acessadas mas não citadas

- https://forum.micropython.org/viewtopic.php?t=11399
- https://www.reddit.com/r/esp32/comments/1jgxpd8/got_a_super_mini_esp32c3_with_042in_oled_finally/
- https://docs.micropython.org/en/latest/library/machine.I2C.html
- https://forum.arduino.cc/t/make-esp32-c3-super-mini-work-with-oled-displays/1248802/12
- https://www.reddit.com/r/esp32/comments/1boaxjn/esp32c3_super_mini_with_i2c_and_spi_connections/
- https://forum.micropython.org/viewtopic.php?t=10330
- https://forum.micropython.org/viewtopic.php?t=2650
- https://github.com/nickpmulder/ssd1306big
- 
