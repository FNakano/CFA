# Multitarefa (e interrupções) no MicroPython

**nota**: Existem funcionalidades implementadas na linguagem (micropython) e outras que são dependentes de plataforma. Faz-se o possível para marcar qual é o caso e quais são as referências.

### Introdução

No contexto de um programador de aplicação na linguagem Python, quando é apresentado o *prompt* do REPL (read-evaluate-print-loop), você pode supor que o computador está *parado, aguardando uma tecla ser pressionada, ou, um comando ser digitado*.

Saltando para o funcionamento do computador e seu componente de interesse neste texto, o processador: Um processador, na tecnologia atual, é uma máquina de estados, ou, autômato finito, construído para executar instruções continuamente (detalhes do funcionamento podem ser obtidos em textos sobre organização e arquitetura de computadores, como STALLINGS). Uma consequência disso é que quando um sistema baseado em processador (ié, computador) está *parado, aguardando o usuário pressionar uma tecla*, o processador consulta, periodicamente, direta ou indiretamente, se a tecla foi pressionada. Esta consulta pode não estar codificada no programa escrito por você, por exemplo num loop que testa alguma variável. Ela pode estar codificada no hardware do processador, que, em um de seus estados, testa se uma interrupção, gerada pelo teclado, ocorreu.

Consequentemente, no contexto do primeiro parágrafo, é possível dizer que o processador está *preso* em um loop.

Uma idéia (no sentido de concepção do ser humano), subjacente nesse contexto, é que o computador executa um único programa. Isto era a situação usual quando computadores tinham *pouca* capacidade de processamento -  havia pouco o que desperdiçar. Capacidade de processamento foi crescendo com o tempo e esse desperdício tornou-se significativo. A fim de abordar esse desperdício, criou-se a multiprogramação e implementou-se o MULTICS. Entre outras consequência, motivando a distinção entre uniprogramação e multiprogramação.

Atualmente, a maior parte dos sistemas computacionais capaz de executar um programa de interface com usuário humano, como REPL, é capaz de suportar multiprogramação. O ESP32 é um desses sistemas, e este tem algum tipo de multiprogramação implementada.

Há muitas camadas de programas e programação que vão do processador até o REPL, logo, há muitas oportunidades e maneiras para implementar multiprogramação, o que torna o entendimento de uma particular implementação algo desafiador.

### Objetivo

Entender e explicar como multiprogramação é implementada em ESP32 e Micropython.

### Resultados

#### FreeRTOS, Micropython

Nem todo dispositivo que executa micropython o faz sobre FreeRTOS: https://forums.freertos.org/t/pyhton-on-free-rtos/10619

ESP32 faz:

> MicroPython is implemented on top of the ESP-IDF, Espressif’s development framework for the ESP32. This is a FreeRTOS based system. See the ESP-IDF Programming Guide for details. (https://docs.micropython.org/en/latest/esp32/general.html?highlight=freertos#technical-specifications-and-soc-datasheets)

Em 2015, Micropython sobre FreeRTOS era um problema (https://forum.micropython.org/viewtopic.php?t=559)


#### REPL, WebREPL, uasyncio

API de REPL: https://docs.micropython.org/en/latest/reference/repl.html

A implementação de REPL pressupõe uniprogramação:

> In Python (Cpython and MicroPython) while a program is running the REPL is inactive. You can interrupt execution with ctrl-C but any other typing is ignored. In this respect a uasyncio program is no different from any other.
(https://forum.micropython.org/viewtopic.php?t=12843&p=69872#p69923)

A implementação de REPL roda em uma camada abaixo de `uasyncio`: 

> There are a few specialist applications which can run in the background but they are very much the exception. Anything you write will not unless you've mastered some tricky programming techniques. Simply using uasyncio does not achieve background running.
(https://forum.micropython.org/viewtopic.php?t=12843&p=69872#p69923)

REPL, no ESP32, é conectado a `UART(0)`: 
> The UART0 is by default attached to Web REPL. 
(https://www.engineersgarage.com/micropython-esp8266-esp32-uart/)
 
WebREPL usa `uos.dupterm()`: https://docs.micropython.org/en/v1.15/library/uos.html#uos.dupterm

Um tutorial sobre `uasyncio`: https://gpiocc.github.io/learn/micropython/esp/2020/06/13/martin-ku-asynchronous-programming-with-uasyncio-in-micropython.html

módulo `_thread`: Contém exemplo de uso. Seria uma alternativa? será que permite acessar o RTOS? Iniciar outra instância de REPL?: https://forum.micropython.org/viewtopic.php?t=4867#p27999

#### Interrupções

É independente de, e, numa camada abaixo de `uasyncio`.

Timers: https://docs.micropython.org/en/latest/library/machine.Timer.html

Timers e multiprogramação (tipo uasyncio) explícita (apresenta explicitamente um loop de eventos e comunicação entre ISR e loop de eventos através de variáveis globais): https://techtotinker.blogspot.com/2020/09/008-micropython-tutorial-hardware-timer.html

Orientação para escrever ISRs: https://docs.micropython.org/en/latest/reference/isr_rules.html#isr-rules

`schedule` em Micropyton internals: https://docs.micropython.org/en/latest/library/micropython.html#micropython.schedule.

### Referências

https://www.google.com/search?q=micropython+uos.dupterm+how+it+works&client=ubuntu&hs=r5V&channel=fs&ei=-7kEY4DkOZyz5OUPjeqeuAE&ved=0ahUKEwjAzZL37dz5AhWcGbkGHQ21BxcQ4dUDCA0&uact=5&oq=micropython+uos.dupterm+how+it+works&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEB4QsAM6BggAEB4QFjoFCCEQoAE6BwghEKABEApKBAhBGAFKBAhGGABQ7UlYs2dgj2loAXAAeACAAaYCiAGJFpIBBjAuMy4xMJgBAKABAcgBAcABAQ&sclient=gws-wiz
https://www.engineersgarage.com/micropython-esp8266-esp32-uart/
https://docs.micropython.org/en/v1.15/library/uos.html
https://www.google.com/search?channel=fs&client=ubuntu&q=micropython+how+repl+works
https://docs.micropython.org/en/latest/reference/repl.html
https://www.google.com/search?channel=fs&client=ubuntu&q=micropython+repl+internals
https://docs.micropython.org/en/latest/library/micropython.html#micropython.schedule
https://docs.micropython.org/en/latest/reference/isr_rules.html#isr-rules
https://docs.micropython.org/en/latest/reference/repl.html
https://www.google.com/search?channel=fs&client=ubuntu&q=micropython+main+loop
https://forum.micropython.org/viewtopic.php?t=5199
https://www.google.com/search?channel=fs&client=ubuntu&q=hazard+tradu%C3%A7%C3%A3o
https://www.google.com/search?channel=fs&client=ubuntu&q=micropython+repl+and+uasyncio
https://forum.micropython.org/viewtopic.php?t=4867
https://gpiocc.github.io/learn/micropython/esp/2020/06/13/martin-ku-asynchronous-programming-with-uasyncio-in-micropython.html
about:newtab
https://www.google.com/search?channel=fs&client=ubuntu&q=micropython+esp32+timer+interrupt
https://techtotinker.blogspot.com/2020/09/008-micropython-tutorial-hardware-timer.html
https://docs.micropython.org/en/latest/wipy/quickref.html#heart-beat-led
https://www.google.com/search?channel=fs&client=ubuntu&q=micropython+timer+object
https://docs.micropython.org/en/latest/library/machine.Timer.html
https://github.com/01Space/ESP32-C3-0.42LCD/blob/main/Schematic/ESP32-C3-0.42OED%20Schematic.pdf
https://www.google.com/search?channel=fs&client=ubuntu&q=micropython+webrepl+and+uasyncio
https://forum.micropython.org/viewtopic.php?t=12843&p=69872
https://www.google.com/search?channel=fs&client=ubuntu&q=micropython+built+on+freertos
https://forum.micropython.org/viewtopic.php?t=559
https://forums.freertos.org/t/pyhton-on-free-rtos/10619
https://docs.micropython.org/en/latest/esp32/general.html?highlight=freertos
https://docs.espressif.com/projects/esp-idf/en/latest/esp32/index.html
https://www.google.com/search?channel=fs&client=ubuntu&q=subjacente