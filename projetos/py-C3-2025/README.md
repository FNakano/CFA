# ?

Em 2025 pretendo que 5 grupos de alunos explorem o ESP32-C3 com display OLED de 0.42 e Micropython.

Este projeto permite gravar rapidamente o firmware micropython e testar a placa. Isto resolve a questão que há fabricantes que usam SH1106 e há fabricantes que usam SSD1306.

### Para gravar o firmware

Na linha de comando: `esptool.py --port /dev/ttyACM0 erase_flash` e `esptool.py --port /dev/ttyACM0 --baud 460800 write_flash 0 ESP32_GENERIC_C3-20250415-v1.25.0.bin`

ié seguir as recomendações da página de download do micropython: https://micropython.org/download/ESP32_GENERIC_C3/

### Para transferir os programas para o dispositivo

1. Clonar esta pasta
2. Instalar rshell com o comando `pip3 install rshell` (o SO do computador deve ter python3 e pip3 instalados)
3. Executar `rshell -p /dev/ttyACM0 ` (verificar qual é o nome da pasta raiz do dispositivo, geralmente é pyboard)
4. Ir para o subdir `src` com `cd src`
5. Copiar os arquivos para o dispositivo executando `cp * /pyboard` quando terminar digitar `exit` para sair do `rshell`
6. Testar o driver SSD1306
  1. Abrir o Thonny
  2. executar no REPL: `import largerFontSSD1306`, caso não mostre nada no display, teste o driver SH1106
7. Testar o driver SH1106
  1. Abrir o Thonny
  2. executar no REPL: `import largerFontSH1106`
8. Um dos drivers deve mostrar algo, caso não mostre, é um caso que está fora do previsto/conhecido neste projeto.

### Informação adicional

Os dois drivers usam protocolo I2C e os dois drivers estão no endereço 0x3C (em decimal, 60), o código abaixo busca todos os dispositivos I2C conectados ao ESP, deve ser executado no dispositivo (ESP) usando Thonny.

```python
from machine import Pin, I2C, ADC

# i2c=I2C(0, sda=Pin(21), scl=Pin(22)) # este é para ESP32S na Plataforma de teste
i2c=I2C(0, scl=Pin(6), sda=Pin(5)) # no ESP32-C3 supermini com display OLED de 0.42" embutido os pinos são 5 e 6

print (i2c.scan()) # if 60 is displayed ssd1306 display was found

```


