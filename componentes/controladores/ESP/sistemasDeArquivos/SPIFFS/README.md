# SPIFFS

Em 2020-08-29 17:06 busquei, 'assistematicamente' por SPIFFS para completar este post com informação atualizada. Pelo que entendi, SPIFFS é um projeto: <https://github.com/pellepl/spiffs>, sua incorporação em ESP8266 é outro projeto e sua incorporação em ESP32 é ainda outro projeto - cada um desses resulta em uma biblioteca incorporada ao *core* do código para a placa (fica em .arduino15/packages/ESPxx/...) . Os utilitários, que facilitam tarefas como transferir arquivos, são ainda outros projetos.

**nota** [o FAQ sobre SPIFFS](https://github.com/pellepl/spiffs/wiki/FAQ#how-long-will-my-spi-flash-live) pode ser útil.

**Vi em <https://arduino-esp8266.readthedocs.io/en/latest/filesystem.html> que SPIFFS não é mais mantido ativamente. Esta informação foi atualizada na documentação do ESP8266 em 2020-05-04.**

Uma explicação detalhada do sistema de arquivos é devida, por exemplo em organização e arquitetura de computadores. Neste texto é possível ficar somente na parte utilizada pelo programador.

Os arquivos podem ser escritos, lidos e removidos através de programas executados no ESP, ou através de utilitários. Usa-se o que for mais conveniente. Procurei por ferramentas para gravar arquivos no SPIFFS diferentes da que conheço, não encontrei. A forma que conheço foi atualizada para o ESP8266 em 2019-11-25 e para o ESP32 em 2019-01-15. Os links de release são:

<https://github.com/me-no-dev/arduino-esp32fs-plugin/releases/tag/1.0>

<https://github.com/esp8266/arduino-esp8266fs-plugin/releases/tag/0.5.0>

Segundo <https://www.onetransistor.eu/2019/12/upload-files-esp8266-esp32-spiffs.html>, os nomes dos arquivos podem ter 32 caracteres (31+'\0'). Não procurei por referências sobre como lida com caracteres acentuados nos nomes dos arquivos. Caso não queira arriscar ou testar, melhor ficar com letras, números, barra, ponto e traços [a..zA..Z0..9-_].

Segundo <https://www.onetransistor.eu/2019/12/upload-files-esp8266-esp32-spiffs.html>, não há diretórios e / (barra, ou slash) é permitido no nome do arquivo. Já segundo <https://www.dobitaobyte.com.br/como-escrever-arquivos-no-spiffs-com-esp32/>, há diretórios.

Há vários tutoriais ensinando como instalar os utilitários na IDE do Arduino:

<https://www.instructables.com/id/Using-ESP8266-SPIFFS/>
<https://randomnerdtutorials.com/install-esp32-filesystem-uploader-arduino-ide/>

A instrução é praticamente a mesma:

1. Baixar o zip dos links de release;
2. Descompactar o conteúdo;
3. Mover o conteúdo para a pasta tools em arduino-<versão> ou para a pasta ~/Arduino, criando a pasta, se necessário;
    - a diferença é que ~/Arduino é uma pasta pessoal, onde os seus sketches são armazenados e
    - arduino-<versão> é a pasta onde a IDE está instalada;
    - considere se, para você, convém fazer backup da ferramenta.    
4. Se Arduino IDE estiver aberto, fechar e abrir novamente. Aparece um ítem novo no menu 'Ferramentas';

O utilitário transfere todos os arquivos da pasta 'Data' dentro do seu projeto na IDE para o ESP. Logo, ou esta pasta já existe no exemplo (WebServer/FSBrowser é um exemplo) ou você pode criá-la.


SPIFFS não foi construído para aplicações em tempo real. Isto quer dizer que as operações, que levam algum tempo para executar, ou bloqueiam o restante da execução, ou, se não bloqueiam, podem não ser completadas. Este segundo caso resulta em escritas não realizadas, arquivos que 'desaparecem' ou que ganham trechos que não lhes pertenciam, chegando à perda de todos os arquivos armazenados ...

As funções usadas nos programas do ESP para acessar os arquivos são 

<referência para spiffs>

