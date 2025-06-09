# Raspberry Pi Pico

## Introdução

Comprei um RP Pico Zero (RP2040) e um RP Pico 2 (RP2040 com flash de 4MB). O uso inicial é testar se é boa plataforma para aprender/treinar programação em *assembly*. É só nessa plataforma que Micropython dá suporte para programação em *assembly*.

Pretendo desenvolver o texto mais tarde. Por exemplo, [tenho dúvidas sobre haver um emulador de ARM com Thumb 16 dentro do Micropython ou se o código assembly é convertido para LM e executado](https://github.com/FNakano/CFA/tree/master/componentes/controladores/RP-Pico#programa%C3%A7%C3%A3o-em-assembly)
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

Em principio, a parte de Micropython que trata assembly não é um emulador. Ele parece emitir instruções que são executadas pelo controlador. Por exemplo, para ARM, o arquivo fonte do código do Micropython é https://gitlab.rtems.org/contrib/micropython/-/blob/v1.24.0-preview/py/asmarm.c . Para RISC-V (novidade) o arquivo fonte é https://gitlab.rtems.org/contrib/micropython/-/blob/v1.25.0-preview/py/asmrv32.c . Não achei esses dois arquivos no github do Micropython (https://github.com/micropython/micropython) mas algo que parece ser o arquivo é mencionado em um release note ([Captura de tela](./Captura%20de%20tela%20de%202025-06-09%2013-19-46.png) da página https://github.com/micropython/micropython/releases ) então eu poderia dizer que com alta probabilidade esses emissores de código assembly são os usados.

Há publicações que se propõe a ensinar assembly usando Micropython (https://smist08.wordpress.com/2022/02/18/adding-assembly-language-to-micropython/)

Há publicações relatando ganho de desempenho através do uso de assembly: https://ioprog.com/2022/11/21/speeding-up-some-micropython-with-a-touch-of-inline-assembly-on-the-raspberry-pi-pico/

Há publicações sobre o uso de assembly com C: https://blog.smittytone.net/2022/06/19/get-started-with-arm-assembly-on-the-pi-pico/ , https://smist08.wordpress.com/2021/04/16/assembly-language-on-the-raspberry-pi-pico/ , http://kofa.mmto.arizona.edu/rpi/pico/inline.html  )

 

