# Extensor com botão

## Materiais

- Placa baseada em ESP8266 - usei [Witty board](/componentes/controladores/ESP/ESP8266/README.md#wittyboard). Uso os LEDs do Wittyboard para indicar estado e o botão como sensor. Para usar outras placas, como Node8266, TTGO8266, montar ao menos o botão na GPIO4 com um resistor *pull-up*.
- [Arduino IDE](/componentes/controladores/ESP#configurar-arduinoide-para-programar-o-esp8266-ou-o-esp32) - interface de programação.
- Cabo USB para energia e dados, compatível com a placa - usado para conectar a placa ao computador;

## Método

A partir do código do [Extensor WiFi](/projetos/ExtensorWiFi/README.md), adaptar e acrescentar o código de cliente HTTP (dos exemplos da IDE do Arduino), usar a requisição do [controle de tomadas](/projetos/ControlarTomadaPelaInternet/README.md).

## Resultados

- [Código Fonte](RangeExtender-NAPTcomBotao-2-limpo-FN.ino)

### Construção do código-fonte

- A partir do código-fonte do [Extensor](/projetos/ExtensorWiFi/README.md), inseri o ajuste de modos dos pinos do botão e dos LEDs: linhas 91 a 93.
- Acrescentei os cabeçalhos das bibliotecas do cliente HTTP: linhas 18 e 20.
- Criei o método *wifiRequest(s)* que contém uma adaptação do método *loop()* do cliente HTTP: linhas 105 a 143.
    - O método *wifiRequest(s)* checa se o wifi está conectado, se sim, faz uma requisição GET ao servidor Blynk, atualizando o valor da variável que representa o botão (virtual) vermelho na tela do celular mostrado no vídeo de funcionamento.
- Preenchi o método *loop()* com a leitura do botão e a chamada a *wifiRequest(s)*: linhas 145 a 156.
    - O botão físico é conectado entre GPIO4 e GND e o resistor *pull-up* (valor típico de 4k7, serve qualquer valor entre 1k e 100k) é conectado entre GPIO4 e 3.3V (ver o esquemático do Witty Board, que ainda não tenho...)
    - Por conta do circuito do botão, quando ele não está pressionado, o valor retornado por `digitalRead` é HIGH(1) e quando está pressionado é LOW(0).
    - O LED vermelho copia o nível lógico do botão, então fica aceso quando o botão não está pressionado e apaga quando o botão é pressionado.
    - O LED verde é apagado na entrada do *loop()*, e é acesso quando *wifiRequest(s)* é executado (agora que vi que seria melhor apagá-lo no *loop()*, logo depois de *wifiRequest(s)*.
    - Este código só funciona sem interromper a comunicação wifi quando o botão é pressionado porque o subsistema do wifi do ESP é assíncrono, ou seja, depois de configurado no *setup()*, funciona independente do programa do usuário (por isso o *loop()* do Extensor wifi está vazio). Eu não tinha certeza que seria assim, mas achava provável que fosse.

### Pontos de configuração do código-fonte

linhas 9 e 10: inserir o nome e a senha do *Access Point* em que este extensor irá conectar-se. [Referência](/projetos/ExtensorWiFi/README.md);
linha 116: inserir a requisição (HTTP:GET) que altera o valor da variável no servidor Blynk. [Referência](/projetos/ControlarTomadaPelaInternet/README.md#curl)

- [Vídeo mostrando teste de funcionamento](https://youtu.be/wL4PatjTSWg)

### Explicação do vídeo

- 0:00 - À esquerda imagem de vídeo capturado por câmera contendo, à esquerda, o witty board, inicialmente desligado, e um telefone celular mostrando as redes wifi disponíveis. A rede extendedAndro não está listada. Ao centro, editor da IDE do Arduino apresentando parte do código-fonte. À direita, terminal executando capturador de tela.
- 0:10 - cabo USB é conectado, ligando o witty board.
- 0:13 - LED acende amarelo: verde porque enviou requisição, vermelho porque botão não está pressionado.
- 0:17 - abre monitor serial;
- 0:19 - a tela do celular atualiza, apresentando a rede `extendedandro`
- a cada segundo uma requisição HTTP:GET é feita, o código de resposta HTTP:200 indica que a mensagem atingiu o servidor;
- 0:33 - o lápis vermelho aponta a rede `extendedandro`, com sinal de aprox. -43dBm;
- 0:48 - tela do app Blynk com o botão (virtual) vermelho ligado em consequência do estado do botão físico não estar pressionado e o nível lógico na GPIO4 ser HIGH.
- 0:58 - o botão físico é pressionado, consequentemente no monitor serial a mensagem muda para `Botao = 0`, a cor do LED vai para verde, em seguida o botão (virtual) vermelho é desligado.
- 1:03 - o botão físico é solto, consequentemente no monitor serial a mensagem volta para `Botao = 1`, a cor do LED vai para amarelo, em seguida o botão (virtual) vermelho é ligado.
- 1:13 - o botão físico é pressionado, consequentemente no monitor serial a mensagem muda para `Botao = 0`, a cor do LED vai para verde, em seguida o botão (virtual) vermelho é desligado.
- 1:16 - o botão físico é solto, consequentemente no monitor serial a mensagem volta para `Botao = 1`, a cor do LED vai para amarelo, em seguida o botão (virtual) vermelho é ligado.



## Referências

[Operações sobre Strings na IDE do Arduino](https://www.arduino.cc/reference/en/language/variables/data-types/stringobject/)

