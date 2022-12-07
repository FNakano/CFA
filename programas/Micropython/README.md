Existe uma versão de Python que pode ser executada em uma variedade de microcontroladores, incluindo ESP32 e ESP8266-12. É o Micropython (http://micropython.org/).

É necessário instalar Micropython nos microcontroladores. Após instalar, os comandos em Python são enviados e executados no microcontrolador, como se vê na animação abaixo:

![Captura de tela mostrando acender e apagar LED com Python REPL](output.gif)

Esta forma de programar o microcontrolador é diferente da forma de programar que usa Arduino IDE. Algumas dessas diferenças, na minha opinião, facilitam o aprendizado da linguagem de programação e a criação de protótipos:

1. A interação do programador com o dispositivo pode ser explicada com menos etapas "difíceis de entender", como compilar e enviar o programa para o dispositivo;
2. O resultado da execução do comando *aparece* mais rápido;
3. Alguns usos tecnicamente sofisticados, como o envio dos comandos por WiFi, podem ser configurados por um programador mais experiente e usados, de maneira transparente, por outros programadores (ex. webREPL).

Por outro lado, há diferenças que podem dificultar certos usos e a criação de produtos.

1. O código-fonte de um programa é uma especificação de alguma atividade ou processo. Essa especificação é explícita, autocontida e essencial (ou mandatória), mas não completa, nem amigável. O código-fonte é armazenado em arquivo texto, o que permite repassar o trabalho de programação a outros programadores (ao custo de muito trabalho para os programadores que receberão o trabalho). Na linguagem popular, é *melhor que zero*. No ciclo de desenvolvimento em linguagem interpretada, se o programador memorizar os comandos (ou usar o histórico de comandos), não é necessário haver um arquivo contendo o código-fonte. Nesta situação, o trabalho se perde com o programador original;
2. Um interpretador acumula informação como que bibliotecas foram carregadas, que variáveis foram criadas, que valores essas variáveis contém,... e "transporta" essa informação entre os programas que executar. Nesse contexto, é muito fácil usar funções e variáveis criadas para um programa em outro programa. Isto cria dependências implícitas entre os programas. Em um novo uso de algum programa, pode ser necessário reproduzir todo o histórico de comandos, algo que o programador terá dificuldade em lembrar;
3. Usar linguagem interpretada em um produto implica em embarcar no produto tanto o interpretador quanto o código-fonte (script) (portanto, é essencial que o programador que criou o produto saiba administrar o código-fonte que criou) e
4. Embarcar interpretador e código-fonte pode não ser desejado, dependendo do produto. 

Ainda assim, o uso de linguagem interpretada acelera a criação de protótipos. Tendo em vista aproveitar esta vantagem, segue-se, com as instruções de instalação do MicroPython. 

### Como instalar Micropython no ESP8266

Este procedimento deve ser feito quando o dispositivo não tem MicroPython instalado ou o Micropython apresenta mau funcionamento. Ou seja, geralmente, só é feito uma vez durante o ciclo de vida do dispositivo.

1. Instalar `esptool` com `pip install esptool`; (https://docs.espressif.com/projects/esptool/en/latest/esp32/);
2. Baixar a imagem do micropython de https://micropython.org/download/?port=esp8266 (eu usei a de 1MB, a de 2MB não executou, embora o ESP8266 que usei tenha 4MB);
3. Conectar o ESP (seja Node-MCU, seja outro) pela porta USB;
4. Checar em que porta o ESP foi detectado (ex. /dev/ttyUSB0);
5. Limpar o conteúdo da memória FLASH do ESP com `esptool.py --port /dev/ttyUSB0 erase_flash`
6. Transferir a imagem com `esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-v1.8.7.bin` (ajustar o nome do arquivo, se necessário).

Caso seu usuário não tenha acesso a `/dev/ttyUSB0` (permission denied) pode ser que precise acrescentar o seu usuário ao grupo `dialout`. No Ubuntu e no Mint isto é feito como o comando: `sudo usermod -a -G dialout <your-username>`. Talvez funcione em outras distribuições baseadas em Debian.

Detalhes em: https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html

### Como instalar Micropython no ESP32

Para instalar Micropython do ESP32, o passo 6 deve ser algo como: `esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180511-v1.9.4.bin`. Ref.: https://docs.micropython.org/en/latest/esp32/tutorial/intro.html

Testei esse procedimento com NodeMCU-32s e com MH-ET Live ESP32-MiniKit.

### Como comunicar com Micropython no ESP8266 e no ESP32

Micropython e seu interpretador são executados no (pelo) dispositivo. O envio de comandos para o dispositivo, usando um computador, é feito através de um programa de comunicação como PuTTy (Windows) ou ~~Minicom (Linux)~~ (ver NOTA). Seguem as instruções para Linux:

7. Instalar `minicom` com `sudo apt install minicom`;
8. Conectar o dispositivo ao computador usando um cabo de dados USB;
8. Conectar com o dispositivo usando o comando `minicom -D /dev/ttyUSB0 -b 115200` (ajustar se necessário);
9. No minicom, se não aparecer o prompt (>>>) digitar ENTER (para aparecer o prompt).

Maiores detalhes em: https://docs.micropython.org/en/latest/esp8266/tutorial/repl.html , https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/console.html

NOTA: Em outro computador, com Ubuntu 22.04LTS, estou apanhando para encontrar uma configuração do minicom que o faça *enviar o que digito no teclado para o ESP*. Achei curioso que alguns colaboradores usavam o monitor serial da IDE do Arduino para comunicar-se com o ESP32 rodando Micropython. Mais curioso ainda é que o minicom (depois de ajustar e salvar os ajustes feitos com `sudo mincom -s` - se não for sudo não salva a configuração) e depois do ESP32 ser acessado usando o monitor serial, passou a comuncar-se com o `minicom`. Os ajustes foram na seção de teclado, adicionar quebra de linha e adicionar carriage return.

Começo a achar que programas de comunicação serial (minicom, picocom) não são boas escolhas para programar placas com Micropython embarcado... A vantagem desses programas é que os executáveis são pequenos, necessitam de poucas bibliotecas adicionais e precisam de poucos recursos da máquina para executar. MAS, até onde vi, não há atualizações há anos (hoje=2022-10-03). Isto, para mim, indica que o programa foi "abandonado". Usando esse mesmo critério, descartei `uPyCraft´ pois o repositório https://github.com/DFRobot/uPyCraft teve o commit mais recente em 2018. Já `Mu-editor` (https://codewith.mu/) parece ativo, mas requer download de mais de 1GB (no momento meu sistema está bem enxuto). Então fui com `Thonny IDE` (https://github.com/thonny/thonny), que tem pacote para Linux (`apt install thonny` - dowload de 24MB). Thonny inicia usando o REPL do Ubuntu. Para usar o REPL do ESP, ir em Tools->Options->Interpreter e selecionar MicroPython(ESP32).

Nota: no windows a porta é algo como `comN:`, como `com3:`, `com4:`, ...

Bibliotecas podem ser acrescentadas usando `upip` (https://docs.micropython.org/en/v1.15/reference/packages.html#upip-package-manager) ou `mip` (https://docs.micropython.org/en/latest/reference/packages.html#installing-packages-with-mip)

### Problemas

1. Sintaxe: codificação do caracter "espaço", espaços depois dos comandos, copiar do webrepl;
	- Quando uso webREPL, copiar código do frame que emula o terminal com CTRL-C e colar em um editor de texto local com CTRL-V carrega espaços depois dos comandos, fazendo as linhas ficarem muito mais longas do que o necessário. Caso essa linha seja devolvida para o webREPL, ou colocada dentro de um script, a presença dos espaços pode causar erro de sintaxe na linha posterior pois python depende de espaços (white spaces) para definir escopo.
	- Em alguns comandos, por exemplo, `while True:`, o espaço entre `while` e `True` é substituido por algum outro caracter que também representa um whitespace, mas quando copia do webREPL e cola em um editor de texto, esse caracter "some", causando um erro.
2. Mensagens de erro de sintaxe dentro de módulos (import);
	- como Python é linguagem interpretada e a interpretação só ocorre quando da execução do comando em uma linha do código, há erros de sintaxe que só são reportados quando a linha contendo sintaxe inválida é executada. 
3. Escopo de variáveis;
	- Há algo entre o escopo do webREPL, o escopo do `boot.py` e o escopo dos módulos que escrevo (e importo), que não entendi. Consequentemente, não sei explicar por que uma variável criada em `boot.py` pode ser usada no webREPL (depois da execução do `boot.py`), mas não pode ser usada dentro de outro módulo. O erro que ocorre é o de variável inexistente. Os autores e mantenedores de Micropython fogem de dar explicações sobre o assunto com o argumento que variáveis globais não devem ser usadas: https://forum.micropython.org/viewtopic.php?t=4638, https://forum.micropython.org/viewtopic.php?t=4814. Concordo que variáveis globais, geralmente, causam problemas, mas isso não serve como desculpa para não explicar direito o outro assunto (escopo de variáveis entre webREPL, `boot.py` e outros módulos).
	- Na falta de explicações, sou forçado a usar a receita dada pelos desenvolvedores.


### Desdobramentos

- [Guia mostrando como usar webREPL](./webREPL).
   - Usar webREPL permite enviar comandos para o dispositivo através de WiFi, prescindindo da conexão cabeada entre o computador e o dispositivo (ex. USB);
- Projeto Efeitos coloridos (dispositivo feito, [documentação iniciada](/projetos/py-efeitos))
- Projeto controlar tomadas (dispositivo feito, [documentação iniciada](/projetos/py-tomadas))
- Projeto ler sensores (dispositivo feito, [documentação iniciada](/projetos/py-sensores-witty))
- snippets (./snippets.md)
	- snippets são fragmentos de código;

A maneira mais comum para executar comandos em Python é digitando no interpretador: um programa em linha de comando que lê o comando digitado, avalia (executa) o comando e imprime o resultado. Interpretadores desse tipo, comumente são designados REPL (Read-Evaluate-Print Loop) (pronúncia: http://www.howtopronounce.cc/repl). Nos microcontroladores com micropyton instalado o interpretador é executado continuamente, "só" precisa ser acessado.

O acesso ao interpretador é feito através de uma ferramenta de comunicação. Se o microcontrolador está conectado  ao computador por uma porta USB, ferramentas comuns são PuTTY (Windows), minicom (Linux), picocom (Linux).

### Informação adicional

- Captura da tela feita com `recordmydesktop --fps=15 --no-sound --v_quality=32`
- Conversão para gif animado feita com `ffmpeg -i out.ogv -s 640x480 -r 7 -ss 00:00:01 -t 00:00:16.5 output.gif`
- Referências sobre vídeo:
   - https://linuxhint.com/make-animated-gif-ubuntu/
   - https://superuser.com/questions/556029/how-do-i-convert-a-video-to-gif-using-ffmpeg-with-reasonable-quality
   - https://trac.ffmpeg.org/wiki/ChangingFrameRate


- Site do micropyton: http://micropython.org/
- Tutorial de micropyton para ESP8266: https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html
- Download do micropyton para ESP8266 de 2MB: https://micropython.org/download/esp8266/
- Download do micropyton para ESP8266 de 1MB (é o que funcionou no wittyboard): https://micropython.org/download/esp8266-1m/
- `help('modules')`: 
   - https://forum.micropython.org/viewtopic.php?t=3298
   - https://docs.micropython.org/en/latest/library/index.html
- como usar os pinos do ESP8266: https://docs.micropython.org/en/latest/esp8266/tutorial/pins.html
- Sistema de arquivos no ESP8266:
   - https://docs.micropython.org/en/latest/reference/filesystem.html#fat
   - https://forum.pycom.io/topic/1358/get-free-flash-space/3
   - https://forum.micropython.org/viewtopic.php?f=16&t=2361&hilit=statvfs&start=10
   - https://docs.micropython.org/en/latest/esp8266/tutorial/filesystem.html
   - https://www.google.com/search?channel=fs&client=ubuntu&q=micropython+os+module+documentation
   - documentação do módulo os: https://docs.micropython.org/en/latest/library/os.html
```python
import os
curdir=os.getcwd()
os.listdir(curdir)
os.statvfs(curdir)
```
<pre>&gt;&gt;&gt; import os
&gt;&gt;&gt; curdir=os.getcwd()
&gt;&gt;&gt; os.listdir(curdir)
[&apos;boot.py&apos;]
&gt;&gt;&gt; os.statvfs(curdir)
(4096, 4096, 866, 863, 863, 0, 0, 0, 0, 255)
&gt;&gt;&gt; 
</pre>
- pronúncia de REPL
   - http://www.howtopronounce.cc/repl
   - https://coderanch.com/t/680914/pronounce-REPL
   - https://replit.com/talk/ask/How-do-you-pronounce-replit/4490
- Memória RAM
   - https://docs.micropython.org/en/latest/develop/memorymgt.html
   - https://forum.micropython.org/viewtopic.php?t=1747
```python
import gc
gc.collect()
gc.mem_free()
```
<pre>&gt;&gt;&gt; import gc
&gt;&gt;&gt; gc.collect()
&gt;&gt;&gt; gc.mem_free()
35920
&gt;&gt;&gt; </pre>

### Processo para instalar micropython e webrepl - resumo, sem explicações

No terminal

```
esptool.py --port /dev/ttyUSB0 erase_flash
cd ~/Documentos/Anotacoes/ESP32MicroPython/
cd esp8266/
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-1m-20220618-v1.19.1.bin 
minicom -D /dev/ttyUSB0 -b 115200
```

No REPL do ESP

```python
import webrepl_setup
```

Responder E, ajustar password, responder para carregar ao reiniciar, deixar reiniciar

```python
import network, time
staif=network.WLAN(network.STA_IF) 
staif.active(True) # conecta ao ap conectado anteriormente
staif.connect('NameOfNetworkTP', '0123456789') # preenche se quiser mudar
time.sleep(5)
staif.isconnected() # True se conectou
staif.ifconfig()    # Mostra o IP para conexão da parte "C" - anotar o IP
CTRL-A X yes
```

No terminal

```
firefox ~/Documentos/git/webrepl/webrepl.html
```

No webrepl

Preenche IP com IP mostrado; clica em connect; digita senha

```python
import os
os.listdir()
os.rename('boot.py', 'originalboot.py')
# envia novo boot.py pela página web
```
