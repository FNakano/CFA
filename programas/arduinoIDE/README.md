# ArduinoIDE

É um ambiente integrado de desenvolvimento (construção e teste de programas).

Inicialmente, em 2009, destinava-se a programar apenas controladores Arduino. Versões posteriores foram incorporando atualizações automáticas ou através da internet, programação de outros controladores,... 

É o ambiente de programação de escolha para a disciplina, tanto para Arduino quanto para ESP.

Atualmente há versões web (usado através do navegador, não é necessário instalar programas - o autor ainda não testou) e *standalone*. Esta pode ser obtida gratuitamente em <https://www.arduino.cc/en/Main/Software>. 

Após baixar a versão da IDE compatível com seu computador, siga as instruções para instalação que estão no site.


## Uso da IDE - sequência básica de programação do controlador

Aqui você aprende como escrever seu primeiro programa (com o material no site arduino.cc).

[Começando com Arduino UNO e ArduinoIDE](https://www.arduino.cc/en/Guide/ArduinoUno)
[Lista de exemplos para Arduino (não para ESP)](https://www.arduino.cc/en/Tutorial/BuiltInExamples)
[Piscando um LED - um dos mais simples programas para Arduino](https://www.arduino.cc/en/Tutorial/Blink)

Executar um programa simples é uma forma simples de checar se ArduinoIDE, seu computador, seu Arduino e você 'estão fazendo tudo certo'. No desenvolvimento de um dispositivo, há etapas em que o dispositivo deixa de funcionar e há muitas causas prováveis. O programa simples diminui substancialmente a quantidade de causas prováveis.

Um programa, no paradigma imperativo, é uma sequência de comandos em uma determinada linguagem. A linguagem utilizada na IDE é C.

O usuário escreve seu programa no editor de texto da IDE, salva e compila. O processo de compilação pode ser entendido como a tradução do programa escrito pelo usuário na linguagem C para a linguagem que o controlador foi construído para executar. Este processo gera o programa compilado.

O programa compilado é enviado para o controlador. Após o envio, o controlador é automaticamente reiniciado e passa a executar o programa compilado.

No Linux, é necessário dar permissão de uso da porta USB ao usuário, caso contrário, o programa compilado não pode ser enviado para o controlador. Para isto, no Ubuntu e no Raspbian, usar `sudo chmod -a -G dialout <usuário>`


