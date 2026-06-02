# Modos de baixo consumo de energia.

Ferramenta usada: micropython v. 1.28.0 para ESP32C3 genérico (veja [Notas](#notas))


Microcontroladores têm modos de operação de baixo consumo de energia. O fabricante do microcontrolador define a quantidade de modos de baixa energia; as características de cada modo, por exemplo se o clock é reduzido, se partes do microcontrolador como WiFi, Bluetooth ou o núcleo de processamento são desligados; e como o microcontrolador retorna desse modo para a operação *normal*.

O ESP32-C3 tem dois modos de baixo consumo (no jargão, *sleep modes*), chamados *light sleep* e *deep sleep*. Expressões envolvendo *dormir* e *acordar* o processador fazem parte do jargão.

Neste projeto testa-se o modo *deep sleep* do ESP32-C3 com firmware Micropython 1.28.0.

Importante destacar que testar modos de baixa energia pode não ser óbvio. Por exemplo, o botão STOP do Thonny força o reset do microcontrolador. Por sua vez, esse reset muda uma variável do processador que indica como ele foi desativado/reiniciado (se por um hard reset ou por um deep sleep) e, às vezes, essa informação importa (por exemplo quando estamos testando os modos de baixo consumo). 

### Dormir por um tempo pré-definido



```python
# Este snippet faz o ESP32 dormir por dez segundos... isto é suficiente para
# a conexão do REPL ser desfeita. Thonny vai sinalizar que o dispositivo foi
# desconectado, mpremote vai terminar a execução.
# Depois dos dez segundos o ESP32 volta a se conectar mas Thonny só tentará
# ser reconectar se (não faça isso) apertar o botão STOP ou se (faça isso) 
# fechar e reabrir o Thonny. Se o prompt do REPL não aparecer, entrar no REPL e
# teclar ENTER para o prompt aparecer.

import machine
import time
 
print("Waking up...")
time.sleep(1)  # simulate some task
 
# Set a deep sleep timer for 10 seconds (10,000 milliseconds)
print("Going to deep sleep for 10 seconds...")
machine.deepsleep(10000)

```

![](./Captura%20de%20tela%20de%202026-06-02%2012-12-56.png)


```
# Este snippet informa como o ESP32 foi reiniciado - se por hard reset ou por
# deep sleep.
# No Thonny, se apertar o botão STOP, o motivo será sempre hard reset. Pois
# o botão STOP envia RESET para o microcontrolador. 
# Fechar e reabrir o Thonny e teclar ENTER evita o envio do reset, então, se
# o processador retornou de deep sleep, isso será mostrado.

from machine import reset_cause, DEEPSLEEP_RESET
 
if reset_cause() == DEEPSLEEP_RESET:
    print("Woke up from deep sleep")
else:
    print("Power on or hard reset")

```

![](./Captura%20de%20tela%20de%202026-06-02%2012-09-59.png)



### Dormir e acordar quando um pino é ativado

Os pinos que podem ser usados para acordar o ESP32C3 são, na documentação do ESP32, pinos de RTC e são os pinos de 0 a 5. Veja as características dos pinos do ESP32C3 em: /componentes/controladores/ESP/ESP32/Pinos.md . Aqui vamos usar o pino 0. Ele será configurado com pull-up interno então o ESP32C3 posto em deep sleep deve ficar estável nesse estado e será acordado se conectar (transitoriamente, como o apertar e soltar de um botão) o pino 0 ao GND. O código foi fornecido por Gemini...

![](./Captura%20de%20tela%20de%202026-06-02%2012-56-30.png)

```python
import machine
import esp32
import time

# 1. Choose an RTC GPIO pin (e.g., GPIO 0). Use a pull-up or pull-down resistor.
WAKEUP_PIN = 0  
button = machine.Pin(WAKEUP_PIN, machine.Pin.IN, machine.Pin.PULL_UP)

# 2. Check why the device just reset
wake_reason = machine.wake_reason()

if wake_reason == machine.DEEPSLEEP_RESET:
    print("Woke up from deep sleep by GPIO pin!")
    # Optional: Toggle a different pin (e.g. built-in LED) to show activity
    # led = machine.Pin(8, machine.Pin.OUT)
    # led.value(1)
    # time.sleep(1)
    # led.value(0)
    
else:
    print("Power-on reset or manual reset.")
    print("Configuring GPIO wakeup...")
    
    # Configure the ESP32-C3 to wake on the button (ALL_LOW for active-low button)
    esp32.wake_on_gpio(pins=(button,), level=esp32.WAKEUP_ALL_LOW)
    
    print("Entering deep sleep. Press the button to wake up.")
    time.sleep(1) # Wait slightly to allow serial output to finish before sleeping
    machine.deepsleep()
```

O código põe o ESP32C3 em deep sleep. Depois de executar o código (digamos que seja através do Thonny), o REPL é desconectado. Conectando transitoriamente um jumper, interligando os pinos GPIO0 e GND, o ESP32C3 é acordado. Fechar e reabrir o Thonny reestabelece a conexão do REPL.

Executando o código (veja o motivo do despertar)
![](./Captura%20de%20tela%20de%202026-06-02%2013-07-25.png)

Conectando (e desconectando) o jumper e reiniciando Thonny:
![](./Captura%20de%20tela%20de%202026-06-02%2013-10-55.png)

Executando o código novamente (veja o motivo do despertar):
![](./Captura%20de%20tela%20de%202026-06-02%2013-12-28.png)




### Notas

Fazer este projeto funcionar deu mais trabalho que o previsto e vai dar mais trabalho para documentar, mas vale documentar.

A versão que eu estava usando era micropython 1.25.0 e iniciei seguindo o tutorial em https://www.oceanlabz.in/esp32-esp32-c3-deep-sleep-mode-in-micropython-save-power-the-smart-way/ . Acredito que essas instruções devam ter funcionado em algum momento. Para balizar essa crença, o módulo `esp32` (não o módulo `machine`) tinha as funções `wake_on_ext0(...)` e `wake_on_ext1(...)` e o despertar através do timer explicado em https://www.oceanlabz.in/esp32-esp32-c3-deep-sleep-mode-in-micropython-save-power-the-smart-way/#Deep_Sleep_with_MicroPython_Getting_Started funcionava como indicado no tutorial. MAS as funções `wake_on_ext0(...)` e `wake_on_ext1(...)`  não funcionavam como se esperava no tutorial.

Eu preciso que o despertar através de um botão funcione então fui atrás de outras referências aí me senti como se entrasse em uma floresta (ou um cipoal) de informação desencontrada (da qual esta página fará parte...).

Tentarei dar alguma ordem e interpretação à informação que encontrei. Começo informando que houve uma época (lá por 2014) em que a palavra ESP32 era suficiente para especificar um modelo de microcontrolador mas atualmente (2026) já não é mais. O ESP32 inicial passou (por alguns) a ser designado ESP32S, enquanto os novos modelos foram surgindo: ESP32S2, ESP32S3, ESP32C3, ESP32C6, ESP32H6, ... Os ambientes de desenvolvimento: ESP-IDF, ArduinoIDE, Micropython, ... , apesar da explosão da quantidade de trabalho, não tinham como não acompanhar e dar suporte a esses novos modelos, mas bibliotecas novas, APIs novas, documentação nova, ... demanda muita capacidade de trabalho para evoluir com "alta" confiabilidade (ié poucos *bugs*, poucas mudanças "grandes", ...)

Destaco o ESP32C3, que tem arquitetura diferente do ESP32 original. O primeiro é um RISCV e o segundo é eXtensa. Portar as bibliotecas e módulos do ESP32 original para o  ESP32C3 pode não ser óbvio pois, embora em aspectos gerais arquiteturas diferentes oferecem funcionalidades iguais ou bastante semelhantes, no detalhe, que é até onde o implementador vai, a maneira de implementar funcionalidades pode ser bastante diferente, o que pode resultar em APIs diferentes ou incongruentes entre si. Parece que foi esse o caso dos modos de baixo consumo de energia.

No ESP32 original esses modos foram expostos ao programador através de uma API que, suspeito, em alguma versão antiga do micropython, estavam no módulo `machine` e que em uma (grande) refatoração do código do micropython foram, pelo menos em parte, movidas para o módulo `esp32`. Depois dessa refatoração, o suporte a ESP32C3 foi implementado sobre o código do ESP32 original (ié, `#define` e novas funções aos montes). Uso ESP32C3 com micropython desde a versão 1.19 A primeira vez que fui usar modos de baixo consumo de energia foi ano passado com a versão 1.25 . Não verifiquei com o detalhamento de agora, então, à época, atendia o que eu precisava e nem me dei conta que havia problemas.

Vi que houve muita discussão em torno do assunto: 

  - https://esp32.com/viewtopic.php?t=39007
  - https://forum.seeedstudio.com/t/esp32c3-will-not-wake-up-after-deepsleep-time/269513/8
  - https://github.com/micropython/micropython/issues/16839
  - https://stackoverflow.com/questions/76823215/deep-sleep-with-ext0-or-ext1-on-esp32-c3-mini-1
  - https://github.com/micropython/micropython/issues/16839
  - https://github.com/orgs/micropython/discussions/9482
  - https://github.com/micropython/micropython/pull/8995
  - https://github.com/micropython/micropython/pull/9583
  - https://github.com/micropython/micropython/pull/17518
  - https://github.com/orgs/micropython/discussions/17336
  - https://forum.arduino.cc/t/esp32-c3-interrupt-wakeup-not-working/1116952/2
  - https://forum.seeedstudio.com/t/esp32c6-using-micropython-will-not-wake-up-from-external-signal/293457/7

Consegui seguir a história a partir de https://github.com/orgs/micropython/discussions/9482 , que apontava para https://github.com/micropython/micropython/pull/8995 e para https://github.com/micropython/micropython/pull/9583 e terminou em https://github.com/micropython/micropython/pull/17518 , em dezembro de 2025, onde o pull request com o ajuste que ativa corretamente os pinos de "acordar" foi incorporado. Então, versões de micropython para ESP32C3 posteriores a dezembro de 2025 devem funcionar. Por isso instalei a versão 1.28.0
  

### Referências

- https://docs.espressif.com/projects/esp-idf/en/stable/esp32c3/api-reference/peripherals/gpio.html
- https://www.oceanlabz.in/esp32-esp32-c3-deep-sleep-mode-in-micropython-save-power-the-smart-way/

### Outra informação

Max17048 mede a carga de uma bateria LiPo  (https://github.com/adafruit/Adafruit_MAX1704X)

Existe um módulo da Adafruit que conecta um painel solar a uma célula LiPo e a uma carga. A saída do módulo não é regulada então pode ir da tensão da bateria até a tensão da célula solar (aprox. de 2,7V até 6V) - https://learn.adafruit.com/usb-dc-and-solar-lipoly-charger/using-the-charger?view=all#load-sharing-1887758 . Para mim isso é um problema...

