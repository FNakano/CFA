# Sensor atmosférico

Um exemplo de dispositivo IoT

   - no momento, a replicação do dispositivo dificilmente iniciará sem erros pois há configurações a fazer. 

Hardware:

ESP32C3 (microcontrolador/placa microcontroladora)
BME280 (sensor de temperatura, pressão atmosférica e umidade do ar)
Display OLED SSH1106 (display de 1.3", resolução de 128x64, chip driver SH1106)
Dois resistores de 4k7 pull-up para os sinais SDA e SCL 
Jumpers
Protoboard

Software e serviços web:

Thing Speak (serviço da mathworks para armazenar e exibir dados IoT)
micropython 1.28, 
scripts python na pasta `pyboard` deste repositório

O que faz:
  
Mede temperatura, pressão atmosférica e umidade do ar locais com o sensor BME280, envia os valores medidos para o serviço Thing Speak e mostra no display a informação armazenada no serviço.

Veja os gráficos em https://thingspeak.mathworks.com/channels/3399532

Imagem:
  
![](./4972496802561068064.jpg)

Display OLED mostra na primeira linha a data em que informação foi armazenada no Thing Speak, nas linhas subsequentes temperatura, pressão e umidade. A placa abaixo do display contém o BME280. A placa à direita do BME280 é a placa microcontroladora ESP32C3.

## Circuito e explicações

Tabela de conexões:

| Pino no BME280| Pino no display | Pino do ESP32C3 |
| --- | --- | --- |
| SCL | SCL ou SCK | 6 |
| SDA | SDA | 5 |
| GND | GND | GND |
| VCC | VCC | 3.3 |

Mais sobre o display em https://github.com/FNakano/CFA/tree/master/projetos/py-OLED

## Scripts

Os scripts necessários estão na pasta `pyboard` deste repositório.

## Como replicar

1. Instalar o aplicativo Thonny no computador (https://thonny.org/)
   - Thonny é um IDE Python que será usado para comunicar com o REPL do Micropython 
2. Instalar o aplicativo `rshell` no computador (https://pypi.org/project/rshell/)
   - `rshell` é um aplicativo para gerenciar dispositivos com Micropython instalado. Será usado para transferir arquivos para o ESP32C3. Thonny pode ser usado para isso mas os arquivos precisarão ser transferidos um por um.
3. Ajustar as permissões do usuário para acesso à porta USB: `sudo usermod -aG dialout $USER`
3. Gravar o firmware Micropython no ESP32C3 
   - siga as instruções em https://micropython.org/download/ESP32_GENERIC_C3/
4. Copiar a pasta `pyboard` e sub-pastas neste projeto
   - o repositório CFA é muito grande, considere se vale a pena cloná-lo...
5. Transferir o conteúdo da pasta pyboard para o microcontrolador
   - execute no terminal do computador `rshell -p /dev/ttyACM0`
   - entre na pasta pyboard: `cd pyboard` 
   - execute no rshell `cp -r * /pyboard`
   - saia do rshell `CTRL-D` 
   - nota: no rshell, a pasta `/pyboard` refere-se ao sistema de arquivos do microcontrolador, a pasta `pyboard` é uma pasta local.
6. Reinicie o microcontrolador pressionando o botão RESET na placa ou desconectando e reconectando o cabo USB do computador.
   - se o programa iniciar com sucesso, em menos de um minuto o display mostrará os valores enviados para o repositório. 
   - no momento, o programa dificilmente reiniciará sem erros pois há configurações a fazer. 
     - use Thonny para navegar pelos arquivos no microcontrolador.

Scripts explicados:

ToDocument
## Simulacao local sem hardware

Para testar o fluxo no Windows/Linux/macOS sem ESP32, BME280 e display, use o script [simulate.py](simulate.py).

O que ele simula:
- `machine` (GPIO/I2C/deepsleep)
- `network` (conexao Wi-Fi)
- `bme280_float` (leituras de sensor)
- `requests` (resposta HTTP no formato ThingSpeak)
- `sh1106` (saida do display no terminal)

Execucao:

```bash
python3 simulate.py
```

Para publicar no ThingSpeak de verdade (sem hardware), use:

```bash
python3 simulate.py --real-http
```

No Windows (PowerShell), pode usar:

```powershell
python simulate.py
```

No Windows (PowerShell), para publicar de verdade:

```powershell
python simulate.py --real-http
```

Links diretos para validar publicacao no ThingSpeak:

- Canal (graficos): https://thingspeak.mathworks.com/channels/3399532
- Ultimo registro (JSON): https://api.thingspeak.com/channels/3399532/feeds/last.json
- Feed recente (JSON, 100 pontos): https://api.thingspeak.com/channels/3399532/feeds.json?results=100

Graficos diretos por campo:

- Temperatura (field1): https://thingspeak.mathworks.com/channels/3399532/charts/1
- Pressao (field2): https://thingspeak.mathworks.com/channels/3399532/charts/2
- Umidade (field3): https://thingspeak.mathworks.com/channels/3399532/charts/3

Saida esperada (resumo):
- linha com configuracao Wi-Fi
- lista de dispositivos I2C encontrados
- bloco `[sim-display]` com data/temperatura/pressao/umidade
- mensagem `[sim] deepsleep called: 60000 ms`

Observacao:
- a simulacao valida o fluxo de software, mas nao valida hardware real (pinos, eletrica, temporizacao e sensor/display fisicos).

### Projetos relacionados neste repositório

https://github.com/FNakano/CFA/tree/master/projetos/SensorMeteorologico-ESP32

Diagrama de blocos de um uso típico: https://github.com/FNakano/CFA/tree/master/projetos/ControlarTomadaPelaInternet#resultados-e-indicadores-de-avalia%C3%A7%C3%A3o

https://github.com/FNakano/CFA/tree/master/projetos/SensorMeteorologico

https://github.com/FNakano/CFA/tree/master/projetos/py-ProgramandoESPEmPython

