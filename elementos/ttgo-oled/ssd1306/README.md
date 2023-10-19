
![foto ttgo-tdisplay com oled](Captura%20de%20tela%20de%202023-10-19%2015-49-46.png)

## Introdução

TTGO T-Display é uma placa microcontroladora com display embutido. O display pode ser LCD ou OLED. O modelo usado tem display OLED. O controlador do display é o SSD1306.

Nesta placa, o sinal enable do display, que controla se o display é ou não ativado, é conectado ao pino 16 do ESP32. Para ativar o display o sinal deve ser HIGH. A comunicação entre o controlador do display e o ESP32 usa o protocolo I2C. O sinal SDA corresponde ao pino 4 do ESP32 e o sinal SCL corresponde ao pino 15 do ESP32.

A instalação do micropython no TTGO T-Display (ESP32) é documentada em https://micropython.org/download/ESP32_GENERIC/ .

A biblioteca do micropython contendo as funções para desenhar no display pode ser baixada em https://github.com/micropython/micropython-esp32/blob/esp32/drivers/display/ssd1306.py . Exemplos de uso da biblioteca podem ser acessados em: https://docs.micropython.org/en/latest/esp8266/tutorial/ssd1306.html

## Procedimento

1. Instalar micropython no TTGO T-Display (usei o firmware estável mais recente que, na época era v1.21.0 (2023-10-05);
2. Baixar o arquivo ssd1306.py do site (tem cópia local);
3. Copiar o arquivo ssd1306.py no TTGO T-Display (por exemplo, usando Thonny);
4. No REPL do TTGO T-Display (aberto com Thonny ou com algum programa de comunicação serial) digitar os comandos abaixo:

```python
from machine import Pin, I2C
import ssd1306
enableDisplay=Pin(16, Pin.OUT)
enableDisplay.on()
i2c = I2C(sda=Pin(4), scl=Pin(15))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.text('Hello, World!', 0, 0, 1)
display.show()
```

### Resultados

o resultado é ilustrado pela foto acima em que o TTGO T-Display exibe a mensagem *Hello, World!*


