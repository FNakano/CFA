# Raspberry Pi Pico

## Introdução

Comprei um RP Pico Zero (RP2040) e um RP Pico 2 (RP2040 com flash de 4MB). O uso inicial é testar se é boa plataforma para aprender/treinar programação em *assembly*. É só nessa plataforma que Micropython dá suporte para programação em *assembly*.

Pretendo desenvolver o texto mais tarde. Por exemplo, [tenho dúvidas sobre haver um emulador de ARM com Thumb 16 dentro do Micropython ou se o código assembly é convertido para LM e executado]()
... o que exatamente é executado? Deixo uma captura de tela para documentar que funciona no RP Pico Zero:

![Captura de tela, Thonny RP Pico Zero](./Captura%20de%20tela%20de%202025-05-27%2015-05-16.png)

Pretendo desenvolver o texto mais tarde. Deixo uma captura de tela para documentar que funciona no RP Pico 2:

![Captura de tela, Thonny RP Pico 2](./Captura%20de%20tela%20de%202025-05-27%2015-14-50.png)

Referência: https://docs.micropython.org/en/latest/reference/asm_thumb2_index.html

## Curiosidades mais

Além do assembly, saber se RP-Pico trabalha bem com LoRa (SX1276 https://forum.micropython.org/viewtopic.php?t=3871). A frequência de operação padrão no BR é 915MHz mas, segundo um blog, a frequência de 433MHz é permitida para uso não comercial (https://blog.eletrogate.com/rede-lora-integrada-com-web-server/)


## RAM e Flash

A primeira coisa que me ocorre quando instalo micropython é saber quanta memória (RAM e Flash) o controlador tem. Para isso uso:
  
```python
import gc
gc.mem_free()

import os
os.statvfs('/')

```

No RP-Zero:

```
>>> os.statvfs('/')
(4096, 4096, 352, 349, 349, 0, 0, 0, 0, 255)
>>> import gc
>>> gc.mem_free()
170848
```

No RP-2:

```
>>> import gc
>>> gc.mem_free()
216560
>>> import os
>>> os.statvfs('/')
(4096, 4096, 352, 350, 350, 0, 0, 0, 0, 255)
>>> 
```

Interpretando os resultados, há aprox. 170kB ou 216kB de RAM livre e aprox. (350*4)=1.4MB de FLASH livre.

## Programação em assembly

