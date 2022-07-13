Existe uma versão de Python que pode ser executada em uma variedade de microcontroladores, incluindo ESP32 e ESP8266-12. É o Micropython (http://micropython.org/).

É necessário instalar Micropython nos microcontroladores. 

A maneira mais comum para executar comandos em Python é digitando no interpretador: um programa em linha de comando que lê o comando digitado, avalia (executa) o comando e imprime o resultado. Interpretadores desse tipo, comumente são designados REPL (Read-Evaluate-Print Loop) (pronúncia: http://www.howtopronounce.cc/repl). Nos microcontroladores com micropyton instalado o interpretador é executado continuamente, "só" precisa ser acessado.

O acesso ao interpretador é feito através de uma ferramenta de comunicação. Se o microcontrolador está conectado  ao computador por uma porta USB, ferramentas comuns são PuTTY (Windows), minicom (Linux), picocom (Linux).

Após instalar, o resultado é este:

![Captura de tela mostrando acender e apagar LED com Python REPL](output.gif)
