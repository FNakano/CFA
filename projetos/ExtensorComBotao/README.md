# Extensor com botão

x-special/nautilus-clipboard
copy
file:///home/fabio/Documentos/git/CFA/projetos/ExtensorWiFi/README.md

x-special/nautilus-clipboard
copy
file:///home/fabio/Documentos/git/CFA/projetos/ControlarTomadaPelaInternet/README.md

## Materiais

- Placa baseada em ESP8266 - usei [Witty board](/componentes/controladores/ESP/ESP8266/README.md#wittyboard). Uso os LEDs do Wittyboard para indicar estado e o botão como sensor. Para usar outras placas, como Node8266, TTGO8266, montar ao menos o botão na GPIO4 com um resistor *pull-up*.
- [Arduino IDE](/componentes/controladores/ESP#configurar-arduinoide-para-programar-o-esp8266-ou-o-esp32) - interface de programação.
- Cabo USB para energia e dados, compatível com a placa - usado para conectar a placa ao computador;

## Método

A partir do código do Extensor, adaptar e acrescentar o código de cliente HTTP (dos exemplos da IDE do Arduino), usar a requisição do controle de tomadas.

## Resultados

- [Código Fonte](RangeExtender-NAPTcomBotao-2-limpo-FN.ino)

### Pontos de configuração do código-fonte



- [Vídeo mostrando teste de funcionamento](https://youtu.be/wL4PatjTSWg)

### Explicação do vídeo

https://github.com/FNakano/CFA/tree/master/projetos/ControlarTomadaPelaInternet#curl

https://www.arduino.cc/reference/en/language/variables/data-types/stringobject/

