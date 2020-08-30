# Sistemas de Arquivos para ESP

*Sistema de arquivos* é a expressão usada para referenciar-se aos programas e estruturas de dados usados para armazenar arquivos.

O armazenamento de informação pode ser feito de várias formas, dependendo, também, das características físicas do dispositivo de armazenamento.

Uma representação suficientemente genérica de um dispositivo de armazenamento é uma folha em branco.

Nessa representação, escrever na folha corresponde à operação de escrita (armazenamento de informação) no dispositivo. ler o que está escrito na folha corresponde à operação de leitura (recuperação de dados) no dispositivo. Passar borracha na folha corresponde à operação de remoção de informação no dispositivo.

Note que os processos definidos são somente escrita, leitura e remoção. Não há nada definido sobre onde escrever, o que ler, se o que está escrito está sistematizado, por exemplo contém título,...

Desta forma, que será rotulada como 'quase assistemática', mantendo a analogia, procurar algo escrito pode corresponder, por exemplo se o que se procura não estiver lá, a ler tudo o que está na folha - tenha ou não pauta, quadros, esteja escrito na diagonal ou em ondas como nas calçadas de Copacabana (licença poética...)

A analogia ajuda a elicitar que as operações de escrita, leitura e remoção são essenciais. Independente do dispositivo de armazenamento, essas operações, se possíveis, requerem operar o dispositivo com os recursos disponíveis, o que consome tempo e energia. Em geral deseja-se minimizar tempo e energia para efetuar as operações.

Voltando à analogia, usar os recursos: lápis, papel e borracha é conveniente para seres humanos. Para poupar tempo e energia, cada um cria suas sistemática: dividir a folha em quadros; ter vários papeizinhos (ou fichas), um para cada lembrete; dar um nome para cada lembrete; ordenar alfabeticamente pelo nome;... Isto inclusive pode ser feito antes de haver informação armazenada, por exemplo quando a folha é pautada ou quando a ficha tem linhas nomeadas para data, assunto, ... Isto é um *sistema de arquivos* para o dispositivo 'papel' com os recursos 'lápis' e 'borracha'. A sistematização feita antes de haver informação no papel tem analogia com a formatação do dispositivo de armazenamento.

Existe uma variedade de sistemas de arquivos. Por exemplo, o antecessor do Windows, o DOS (Disk Operational System), usava um sistema de arquivos (criado na época) chamado 'File Allocation Table' (FAT). FAT12 para disquetes, FAT16 para HDs. FAT foi atualizado com esse nome até FAT32 E ainda é amplamente usado, por exemplo em pendrives. Atualmente o Windows usa NTFS. UNIX tem outra variedade de sistemas de arquivos, Linux usa ext2, ext3, ext4, com ou sem 'journaling' (acho que é assim que se escreve), ... voltemos ao ESP.

Os ESP têm uma quantidade de memória não volátil do tipo FLASH - é o mesmo tipo de memória do cartão SD que, provavelmente, você tem no telefone celular. Modelos de ESP01 podem ter 256kbytes, modelos de ESP12 podem ter 1Mbytes a 4Mbytes, modelos de ESP32 podem ter de 4Mbytes a 16Mbytes. Esta memória é usada para armazenar programas e pode ser usada para armazenar dados. A comunicação entre memória e processador usa um protocolo genérico, no sentido de poder ser usado por outros dispositivos, chamado SPI. A parte que o usuário destinar a dados é formatada.

Informação, ferramentas e conceitos em TIC, atualmente, mudam rápido, logo, não há como garantir que a a informação postada aqui continuará válida, ou que a terminologia continue com o mesmo significado.

Atualmente existem dois sistemas de arquivos para ESP. O SPIFFS e o LittleFS. Atualmente (2020-08-29) a notícia é que SPIFFS foi descontinuado pelo desenvolvedor e foi marcado como deprecado pela comunidade que mantém as ferramentas de programação para o ESP8266 <https://arduino-esp8266.readthedocs.io/en/latest/filesystem.html#spiffs-deprecation-warning>

> SPIFFS is currently deprecated and may be removed in future releases of the core. Please consider moving your code to LittleFS. SPIFFS is not actively supported anymore by the upstream developer, while LittleFS is under active development, supports real directories, and is many times faster for most operations.

O cenário fica um pouco mais complexo se considerarmos que as ferramentas para ESP8266 são mantidas por uma comunidade de desenvolvedores e as ferramentas para ESP32 são mantidas pela empresa (espressif) que projetou ambos, e que a comunidade já migrou a codificação para usar LitteFS e a empresa ainda não <https://github.com/espressif/arduino-esp32/issues/3765>, <https://github.com/lucadentella/SPIFFS_ImageReader/issues/1>. A notícia, de nove dias atrás, é que talvez na próxima versão da biblioteca para ESP32 o LittleFS seja incluído.

Então aqui temos trabalho dobrado:

[mais sobre SPIFFS](SPIFFS/README.md)

[mais sobre LittleFS](LittleFS/README.md)

