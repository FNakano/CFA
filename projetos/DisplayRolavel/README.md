# Display rolável e biblioteca na IDE do Arduino.

## Motivação

Gostaria de apresentar como criar bibliotecas na IDE do Arduino e fazer isso com uma aplicação que considero útil.

## Informação preliminar

Na linguagem C e variantes, em geral, *headers* (arquivo de extensão .h) contém os protótipos (declarações) das classes e funções, comandos *inline*, constantes e macros de pré-processador (#define). O compilador C necessita desta informação para gerar corretamente as chamadas de funções e alocação de memória para variáveis estáticas no executável. O corpo das funções é colocado em arquivo contendo código-fonte (arquivo de extensão .cpp).

Uma biblioteca para a IDE do Arduino é composta por pelo menos um *header* e zero ou mais arquivos contendo código-fonte . Ambos armazenados no diretório ARDUINO_HOME/libraries/<sua biblioteca>.

Quando um *sketch* (programa) inclui um *header*, durante a compilação do *sketch* o *header* é procurado e incluído. O código-fonte (arquivo .cpp) é incluído no processo de compilação, num processo semelhante à inclusão de uma classe no CLASSPATH de Java.

## Resultados

### Biblioteca

Todos os arquivos estão no diretório [DisplayRolavel](./DisplayRolavel/)

O *header* é [`DisplayRolavel.h`](./DisplayRolavel/DisplayRolavel.h) ele contém nos comentários a documentação da API.

O *código-fonte* é [`DisplayRolavel.cpp`](./DisplayRolavel/DisplayRolavel.cpp) ele contém alguma informação sobre o histórico de desenvolvimento.

O tipo Lato tamanho 13 não é padrão da biblioteca gráfica. Ele foi gerado com o site http://oleddisplay.squix.ch/#/home e o código foi armazenado no arquivo [`Lato13.h`](./DisplayRolavel/Lato13.h)

No sistema de teste o código-fonte da biblioteca ficou em: `/home/fabio/Arduino/libraries/DisplayRolavel/DisplayRolavel.cpp`

Caso a constante `DEBUG_ROLAVEL` seja definida, são habilitadas mensagens que são apresentadas no monitor Serial (veja nos exemplos como isso funciona).

### Exemplos

O [`ExemploDisplayRolavel.ino`](./ExemploDisplayRolavel.ino) demomonstra a rolagem da tela acionada por botões. Para isso, habilita os pinos 32 e 33 como botões touch. Talvez valha a pena visitar o exemplo ESP32->TouchInterrupt.

O [`DisplayRolavelOTADemo-2021-08-18.ino`](./DisplayRolavelOTADemo-2021-08-18.ino) integra elementos da interface gráfica feita pela ThingPulse com a rolagem da tela e atualização OTA. Para isso, habilita os pinos 32 e 33 como botões touch. Talvez valha a pena visitar o exemplo ESP32->TouchInterrupt, ArduinoOTA->BasicOTA, ESP8266_ESP32_OLED_Driver_for_SSD1306_Displays->SSD1306OTADemo. Para usar, configurar o acesso ao wi-fi ajustando no *sketch* as linhas:

```
 const char *ssid         = "..............";
 const char *password     = ".............";
```


