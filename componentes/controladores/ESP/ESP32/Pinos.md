# Entrada e Saída

Os pinos em que dispositivos de entrada e saída podem ser conectados ao ESP32 são denominados General Purpose Input Output (GPIO). Nem todos os pinos são expostos nas placas de prototipagem (como NodeMCU, Node32S, ESP32-C3 supermini, ...).

Apesar da denominação, esses pinos não podem ser usados de qualquer maneira. Alguns são usados para configurar o boot do microcontrolador, outros servem somente como entrada, outros somente como saídas, alguns têm funcionalidade de botão touch, outros permitem despertar o processador de estados de baixo consumo de energia.

A documentação do fabricante do ESP32 está melhorando e seus guias no site trazem essa informação melhor detalhada (comparada com alguns anos atrás). 

Em Computação Física uso frequentemente os microcontroladores ESP32 e ESP32-C3. Os links para a documentação dos pinos de entrada e saída são https://docs.espressif.com/projects/esp-idf/en/v6.0.1/esp32/api-reference/peripherals/gpio.html e https://docs.espressif.com/projects/esp-idf/en/stable/esp32c3/api-reference/peripherals/gpio.html , respectivamente.

Para manter referências, apresento as capturas de tela abaixo:
  
![](./Captura%20de%20tela%20de%202026-06-01%2012-50-53.png)

![](./Captura%20de%20tela%20de%202026-06-01%2012-51-07.png)

Use os pinos de acordo com a recomendação do fabricante. Em especial, não usar *strapping pins* sem saber bem como usá-los.

