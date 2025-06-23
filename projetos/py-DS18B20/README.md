# Sensor de temperatura DS18B20 e protocolo OneWire

## Objetivo

Escrever um exemplo de uso do DS18B20 com boa documentação dos elementos usados 
e boas referências.

## Resultados

DS18B20 é um sensor de temperatura (falta referência para o datasheet ) 
para ser conectado a um microcontrolador e 
se comunica com este através do protocolo OneWire. A definição do protocolo 
OneWire é feita pela Dallas, fabricante dos componentes que usam esse 
protocolo. (falta referência para a definição do protocolo)

Para conectar (eletricamente) o DS18B20 ao ESP32 é necessário um resistor 
de pull-up - usou-se um de $4k7\Omega$:
  
| ESP32 | resistor $4k7\Omega$ | DS18B20 |
| --- | --- | --- |
| 5V | A | Vcc |
| GND | --- | GND |
| IO19 | B | DQ |

Usa-se o pino 19 do ESP32 para transmitir/receber dados.

No Micropython para ESP32 o driver para One Wire é feito em software 
(https://docs.micropython.org/en/latest/esp32/quickref.html#onewire-driver) . 
O programa abaixo mostra como usar o pino 19:
  
```
import machine
import onewire
import time
ow = onewire.OneWire(machine.Pin(19)) # create a OneWire bus on GPIO19
ow.scan()               # return a list of devices on the bus
```

A função `scan()` busca por dispositivos conectados ao pino. Mais de um 
dispositivo pode ser conectado ao mesmo pino. Cada dispositivo tem um 
identificador de 64 bits. `ow.scan()` retorna um array de byte arrays 
(https://docs.micropython.org/en/latest/genrst/builtin_types.html#bytearray) 
em  que cada byte array corresponde a um identificador.

DS18B20 é um dos componentes que se comunica através desse protocolo. Mensagens 
específicas para esse componente são encapsuladas no módulo `ds18x20`. Há muitas
versões de Micropython e muitas mudanças na API de One Wire e de ds18x20. 
Não achei a informação sobre qual arquivo é o usado em alguma específica 
versão do Micropython. Fica para a lista de coisas a fazer/(não fazer).
Baseado em https://forum.micropython.org/viewtopic.php?t=8279 , que é muito 
antigo, `ds.convert_temp()` sinaliza a todos os DS18X20 conectados para
realizar uma medida. O processo de medir leva até 750ms.
A medida de um determinado sensor é lida com a função
`ds.read_temp(rom)` onde `rom` é um byte array que identifica um particular
sensor. O programa (que deve seguir o anterior) é:

```
ds=ds18x20.DS18X20(ow)
roms=ds.scan()
ds.convert_temp()
time.sleep(1)
ds.read_temp(roms[0])
```

