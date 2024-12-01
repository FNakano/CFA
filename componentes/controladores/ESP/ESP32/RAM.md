# Random Access Memory (RAM) no ESP32

Memória é um dos recursos importantes em microprocessadores e microcontroladores. A distinção inicial entre tipos de memória é se é armazenamento primário ou armazenamento secundário onde, em geral, primário refere-se a memória de acesso aleatório (RAM) e secundário a memória conectada ao processador como dispositivo de entrada e saída (ROM, EPROM, cartões de memória, SSDs, HDs,... Microcontroladores podem ter ROM, EPROM e podem gerenciar cartões de memória (geralmente o protocolo de comunicação é SPI, que é um protocolo que pode ser implementado em um microcontrolador. Protocolos mais complexos e velozes, como o PCIe usado em SSDs e HDs, dificilmente estão presentes.

Em geral, em microcontroladores, os programadores frequentemente queixam-se que há pouca RAM física. Mecanismos para "aumentar o tamanho da RAM", como memória virtual, são pouco frequentes.

O ESP32 tem 520kBytes de RAM estática (https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/memory-types.html#dram-data-ram) e tem limitações para sua alocação. 

Alguns modelos de ESP32 têm Pseudo-Static-RAM (PSRAM). Trata-se de um módulo de memória externo, adicional, com tamanho de 8MB (veja https://docs.espressif.com/projects/esp-idf/en/release-v3.3/hw-reference/modules-and-boards.html#wroom-solo-and-wrover-modules). A presença dessa memória é configurada na compilação do firmware e o funcionamento é quase transparente para o programador de aplicação.


**nota**: A maioria dos ESP32 têm armazenamento secundário que pode variar de 4MB até 16MB, mas isto não é RAM, está mais para armazenamento secundário.

A quantidade de PSRAM em alguns modelos de ESP32 está no datasheet (https://docs.espressif.com/projects/esp-idf/en/release-v3.3/hw-reference/modules-and-boards.html , https://www.reddit.com/r/esp32/comments/10ikyoq/determining_amount_of_psram_using_esptoolpython/), em outros modelos é apresentada usando `esptool flash_id` (https://github.com/espressif/arduino-esp32/issues/8700#issue-1926334351) Este comando também retorna a quantidade de armazenamento secundário.

Um firmware muito comum é Micropython. Com Micropython instalado, apenas 150k de RAM fica disponível para aplicações (`import gc gc.mem_free()`). O detalhe do uso de memória pode ser acessado com `import micropython micropython.mem_info()` (https://github.com/orgs/micropython/discussions/12316). Caso o ESP32 usado tenha PSRAM, uma versão de Micropython corretamente configurada precisa ser compilada e instalada. Este é o caso em https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo . 

Esta versão de firmware chamou minha atenção pois é usada como base para https://github.com/WebThingsIO/webthing-upy . Esse projeto é de um pacote para criar uma Thing com ESP32 e Micropython. Sua criação precede, em algum sentido, a definição de W3C-WoT. Isto elicita a ligação histórica entre Mozilla Web of Things e W3C-WoT. Note que WebThingsIO é a organização que contém o repositório webthing-upy e também contém o Mozilla Web of Things gateway (https://github.com/WebThingsIO/gateway/). Especificamente, em https://github.com/WebThingsIO/wot-adapter

> Note: This adapter consumes W3C compliant Thing Descriptions and will eventually supercede the thing-url-adapter which consumes Web Thing Descriptions conforming to Mozilla's legacy Web Thing API specification.

conclui-se que os projetos em WebthingIO não seguem W3C-WoT. Logo, faz sentido que, por exemplo, webthing, tanto em Micropython (https://github.com/WebThingsIO/webthing-upy/tree/master)  quanto em Python (https://github.com/WebThingsIO/webthing-python) não contém a associação com HTTP (HTTP binding), mas as chaves do escopo do dispositivo (como actions e properties) parecem seguir o padrão (https://github.com/WebThingsIO/webthing-python).


