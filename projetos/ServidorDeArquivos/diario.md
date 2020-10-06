# Diário do projeto de ServidorDeArquivos.

Faz parte do projeto [FuncionalidadesRecorrentes](../FuncionalidadesRecorrentes/README.md)

## 2020-10-02-213534

temperatura no quarto: `curl -X GET -i 'http://blynk-cloud.com/DxFTQgXdhAy1BUlz1Friw1sL5afAvJDr/get/v6'`

Resolvi analisar com mais detalhe o que vem no pacote do exemplo FSBrowser. Fiquei impressionado... com a minha falta de visão.

O servidor recebe requisições e as responde. Se a resposta for um html, o navegador, no cliente, renderiza. O html pode conter javascript, pode solicitar para baixar javascript de outros sites, exibir fotos armazenadas em outros sites, ...

Há muita coisa feita em javascript. Por exemplo, AJAX. E sobre AJAX muitas outras coisas, como o AJAX Cloud9 Editor (ACE). Um editor de código todo feito em javascript!!

[ACE site oficial](https://ace.c9.io/)

[ACE na Wikipedia](https://en.wikipedia.org/wiki/Ace_(editor))

[ACE no github](https://github.com/ajaxorg/ace)

Há repositórios que armazenam os javascripts, como [cdnjs](https://cdnjs.com/libraries/ace/1.1.9)

O editor embutido no ESP32 é o ACE.

Esse é um exemplo que permite dizer que a internet é um grande HD e o processamento da aplicação do usuário é feito na ponta, no seu computador pessoal. A infraestrutura Web (os servidores), neste caso, são componentes que encaminham a informação, sem executá-la nem transformá-la.

Há casos em que os servidores são co-processadores, como no caso do mermaid e do katex, que recebem as descrições dos grafos, ou das fórmulas, e devolvem as imagens.

Voltando ao FSBrowser, resta entender como enviar arquivos para o servidor.

Consegui apagar arquivos:

`curl -v -X "DELETE" http://esp32fs.local/edit?file=/README.md`
[referência](https://stackoverflow.com/questions/2539394/rest-http-delete-and-parameters)

**nota importantíssima**: O nome do argumento pode ser qualquer pois o handleFileDelete usa o argumento de índice zero e usa como nome do arquivo.

Para listar os arquivos:

`curl -v   http://esp32fs.local/list?dir=/`

**nota importantíssima**: O nome do argumento deve ser `dir` pois o handlaFileList usa o argumento com esse nome.

Para baixar um arquivo:

`curl -v http://esp32fs.local/README.md`

Para enviar um arquivo do diretório corrente:

`curl -v -F 'data=@retamgulo-se.svg' http://esp32fs.local/edit`

[referencia](https://medium.com/@petehouston/upload-files-with-curl-93064dcccc76) COM O CUIDADO DE SUBSTITUIR AS FANCY-ASPAS PELAS ASPAS COMUNS.

**nota**: desconfio que o nome do argumento (no exemplo é `data`) não faz diferença para este FSBrowser específico.

Enfim, poderia ter resolvido isto em dez minutos, lendo o comentário e usando as aspas comuns. Como não fiz nem uma coisa nem outra suficientemente bem, levei até as 16:30 de hoje para colocar a funcionar o upload, download e o delete.

O código do arduino é: FSBrowser-FN.ino.

## 2020-10-04-194400 

(estimado a partir do timestamp código FSBeLOG.ino)

Notei que o servidor de arquivos recebe dados dos sensores e permite que quem for analisar os dados copie os arquivos. (Isto estava na cara quando escrevi a [proposta das FuncionalidadesRecorrentes](../FuncionalidadesRecorrentes/proposta.md#Caso-seja parte-de-uma-sequência/cadeia/rede,-quais-relações-com-as-outras-atividades/elos-são-conhecidas.)

São duas interfaces independentes: uma com os sensores e uma com o analista de dados.

A interface com o analista de dados pode ser implementada com o [servidor HTTP e curl](diario.md#2020-10-02-213534).

Fui ver se havia exemplo sobre leitura/escrita de arquivos no SPIFFS, o que serviria como modelo para a interface com sensores. Tem o SPIFFS_Test. Adaptei o exemplo para criar um arquivo com nome gerado pelo instante em millis e acrescentar ao arquivo um número gerado aleatoriamente aproximadamente a cada segundo. Isto simula o funcionamento de um sensor. Salvei como SPIFFS_Test-FN. A questão de *memory wear out* começou a me preocupar.

Meu passo seguinte foi juntar o servidor HTTP com o sensor simulado. 

Ter todo o código-fonte em um arquivo só, quando há muito código, deixa-o difícil de ler, de encontrar os trechos para ajustar. Resolvi checar se uma solução simples funciona: 

A maioria dos exemplos na IDE do Arduino contém apenas um arquivo de extensão `.ino` dentro de uma pasta de mesmo nome. Testei o que ocorre se houver mais de um arquivo. A resposta é: os dois são compilados juntos.

Caso os dois contenham os métodos `setup()` e `loop()`, ocorre erro de compilação. Isto indica que os métodos de um arquivo são acessáveis no outro.

Resolvi isso renomeando os dois métodos em um dos arquivos. No teste que fiz, `setupFSB()` e `loopFSB()`. O compilador voltou a compilar o código sem erros.

Isto feito, invoquei `setupFSB()` de dentro de `setup()` e `loopFSB()` de dentro de `loop()`, compilei e o programa combinado desta forma funcionou como eu esperava: Cria um arquivo e vai armazenando números e, simultaneamente, esse arquivo está na lista de arquivos do sistema e pode ser baixado usando `curl`. O resultado é a pasta Arduino/FSBeLOG.

## 2020-10-05-094248

(estimado)

Durante os testes de SPIFFS_Test-FN, vi que o ESP32 que uso tem 16MB (128Mb) de memória FLASH, mas os esquemas de memória usando SPIFFS aproveitavam apenas 4MB. Isto me incomoda.

A primeira idéia que me ocorreu foi trocar SPIFFS por FAT (previamente, eu sabia que as opções de sistemas de arquivos são SPIFFS, LittleFS e FAT).

Migrar para FAT necessitaria migrar o código do FSBeLOG (eu tinha esperança que a API de FAT fosse igual à API de SPIFFS) e encontrar uma ferramenta para transferência de arquivos, como o ESP32 sketch data uploader.

Cheguei a buscar informação, procurar se havia algo pronto. Se existe, não achei.

https://www.google.com/search?channel=fs&client=ubuntu&q=esp32+fsbrowser+using+fat
https://www.google.com/search?channel=fs&client=ubuntu&q=esp32+fat+fsbrowser
https://github.com/espressif/arduino-esp32/issues/312
https://www.google.com/search?channel=fs&client=ubuntu&q=esp32+async+web+server
https://github.com/me-no-dev/ESPAsyncWebServer
https://randomnerdtutorials.com/esp32-async-web-server-espasyncwebserver-library/
https://techtutorialsx.com/2017/12/01/esp32-arduino-asynchronous-http-webserver/

A ferramenta para transferir arquivos para FAT existe <https://github.com/marcmerlin/esp32_fatfsimage/blob/master/fatfsimage.cpp> mas não consegui usar.

https://github.com/marcmerlin/esp32_fatfsimage
http://marc.merlins.org/perso/arduino/post_2019-03-30_Using-FatFS-FFat-on-ESP32-Flash-With-Arduino.html

Em outras IDEs há outras ferramenta para trabalhar com sistema de arquivos, mas aprender a usar outra IDE está meio fora de consideração.

https://github.com/espressif/arduino-esp32/issues/3230
https://github.com/espressif/arduino-esp32/issues/312
https://esp32.com/viewtopic.php?t=8619
https://www.google.com/search?channel=fs&client=ubuntu&q=spiffs+on+16M+esp32
https://github.com/espressif/arduino-esp32/issues/1793
https://github.com/espressif/esp-idf/tree/release/v3.1/examples/storage/sd_card#note-about-gpio12
https://desire.giesecke.tk/index.php/2018/07/06/reserved-gpios/
https://github.com/espressif/arduino-esp32/pull/1943
https://www.google.com/search?client=ubuntu&hs=gqr&channel=fs&sxsrf=ALeKk02bIBnpXT87Ez_sePc1brmATrsK0Q%3A1601916645353&ei=5U57X5egFYDC5OUPlZWLwAY&q=arduino+ide+fatfs+data+upload+esp32&oq=arduino+ide+fatfs+data+upload+esp32&gs_lcp=CgZwc3ktYWIQAzoECCMQJzoFCCEQoAE6BAghEBU6BwghEAoQoAFQrb4BWLTdAWDa3wFoBXAAeACAAb8CiAHQDpIBBzAuNy4yLjGYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=psy-ab&ved=0ahUKEwjXpuzE9J3sAhUAIbkGHZXKAmgQ4dUDCAw&uact=5
https://community.platformio.org/t/esp32-arduino-framework-ffat-fs-upload-insted-of-spiffs/7997
https://techtutorialsx.com/2018/10/06/esp32-arduino-fat-file-system/

Nessa busca achei informação que me leva a acreditar que a Espressif prefere FAT, mas sistema de arquivos mais usado ainda é SPIFFS. 

https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/storage/fatfs.html

**apesar da escolha contrária, saber usar FAT seria uma boa adição à base de conhecimento.**

Eu lembrava que SPIFFS tinha limitação de tamanho de sistema de arquivos, mas essas coisas mudam rápido e eu poderia estar enganado. Procurei e não encontrei essa limitação, aliás, encontrei informação dizendo que alguns projetos tinham SPIFFS para 16M.

https://www.google.com/search?channel=fs&client=ubuntu&q=spiffs+size+limit
https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/storage/spiffs.html
https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/storage/spiffs.html

Como SPIFFS não tem limitação de tamanho de sistema de arquivos, então parti para saber como criar um novo esquema de particão de memória na IDE do Arduino:

https://gitmemory.com/issue/espressif/arduino-esp32/3230/534879072
https://www.google.com/search?channel=fs&client=ubuntu&q=create+new+partition+scheme+for+esp32+on+arduinoide
https://forum.arduino.cc/index.php?topic=640945.0

Existe uma ferramenta com GUI para criar esquemas de partição, até clonei o repo github, mas não consegui funcionar...

<https://github.com/francis94c/ESP32Partitions>

Acabei usando a abordagem de <https://robotzero.one/arduino-ide-partitions/> - é bem explicado, não vou replicar aqui.

outros sites que consultei:
https://github.com/espressif/arduino-esp32/issues/703
https://github.com/espressif/arduino-esp32/issues/2553
https://desire.giesecke.tk/index.php/2018/04/20/change-partition-size-arduino-ide/

## 2020-10-05-155032

...mas darei a minha interpretação e mostrarei o que fiz no meu computador.

A solução consiste em criar a descrição da partição em um arquivo e referenciar essa descrição na informação da placa. A informação da placa é usada para compor o menu ferramentas. Como o esquema de 2M para APP e 9.5M para arquivos me atendia bem, exceto por ser FAT, criei uma cópia do arquivo na pasta referenciada abaixo:

<pre><font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~/.arduino15/packages/esp32/hardware/esp32/1.0.4/tools/partitions</b></font>$ </pre>

Nome do arquivo: spiffs12M-FN.csv

```
# Name,   Type, SubType, Offset,  Size, Flags
nvs,      data, nvs,     0x9000,  0x5000,
otadata,  data, ota,     0xe000,  0x2000,
app0,     app,  ota_0,   0x10000, 0x200000,
app1,     app,  ota_1,   0x210000,0x200000,
spiffs,     data, spiffs,     0x410000,0xBF0000,
```

Depois editei boards.txt para referenciar o arquivo. Foi copiar e colar as três linhas do esquema que usei como base e modificar o nome do esquema e o nome do arquivo:

<pre><font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~/.arduino15/packages/esp32/hardware/esp32/1.0.4</b></font>$ gedit boards.txt &amp;
[1] 4986
<font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~/.arduino15/packages/esp32/hardware/esp32/1.0.4</b></font>$ 
</pre>

fragmento de boards.txt contendo minha definição de memória

```
...
esp32.menu.PartitionScheme.app3M_fat9M_16MB.upload.maximum_size=3145728
# FN 2020-10-05
esp32.menu.PartitionScheme.fnflash=16M Flash (2MB APP/12.5MB SPIFFS)
esp32.menu.PartitionScheme.fnflash.build.partitions=spiffs12M-FN
esp32.menu.PartitionScheme.fnflash.upload.maximum_size=2097152

...

```

Fechar e abrir a IDE, selecionar o novo esquema de memória e transferir o arquivo e o programa. **nota** a transferência leva mais de 70 segundos e não termina quando mostra 100%. Espere a ferramenta sinalizar o reset do ESP32.

![sucesso](Captura%20de%20tela%20de%202020-10-05%2015-38-08.png)

## 2020-10-06-193628

Terminei de escrever o relatório. Comecei aprox. 15:30 (horário da primeira foto). Gastei 4 horas. 

