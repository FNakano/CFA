# Diário do projeto Controlar tomada pela Internet.

Faz parte do projeto [Controlar tomada pela Internet](README.md)

## início 2020-10-08-150708

Começando proposta, para não esquecer de que se trata....

## interrompido 2020-10-08-151732

## início 2020-10-08-171032

## interrompido 2020-10-08-172820

## início 2020-10-08-200500
(estimado pelo timestamp da cópia)

Decidi usar wittyboard. Passei das 19h às 20h procurando placas e componentes e programas.

Decidi usar blynk para encaminhar as requsições.
Busquei meus projetos com LEDs do wittyboard, para saber os pinos. Vou começar com LEDs e então vou conectar o relé.

Criei o app TresLED no blynk, tirei vários screenshots do celular e do computador.

O elemento posto na GUI do Blynk no celular é o elemento no celular. Por exemplo: se quiser um botão no celular para controlar um LED conectado à placa, coloque um botão no celular, não um LED.

A atribuição dos pinos através dos gp* da GUI do blynk é automática. Não é necessário adicionar código.

A leitura através de get:

<pre><font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~</b></font>$ curl -X GET -i &apos;http://blynk-cloud.com/o08E8QWoQlbKcuiS-LIGpqyXyooRft5x/get/d15&apos;
HTTP/1.1 200 OK
<b>connection</b>: keep-alive
<b>content-type</b>: application/json;charset=utf-8
<b>access-control-allow-origin</b>: *
<b>content-length</b>: 5

[&quot;0&quot;]<font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~</b></font>$ curl -X GET -i &apos;http://blynk-cloud.com/o08E8QWoQlbKcuiS-LIGpqyXyooRft5x/get/d15&apos;
HTTP/1.1 200 OK
<b>connection</b>: keep-alive
<b>content-type</b>: application/json;charset=utf-8
<b>access-control-allow-origin</b>: *
<b>content-length</b>: 5

[&quot;1&quot;]<font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~</b></font>$ 

</pre>

É possível escrever usando get. 

`curl -X GET -i 'http://blynk-cloud.com/o08E8QWoQlbKcuiS-LIGpqyXyooRft5x/update/d15?value=0'`


<pre><font color="#859900"><b>abio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~</b></font>$ curl -X GET -i &apos;http://blynk-cloud.com/o08E8QWoQlbKcuiS-LIGpqyXyooRft5x/update/d15?value=1&apos;
HTTP/1.1 200 OK
<b>connection</b>: keep-alive
<b>access-control-allow-origin</b>: *
<b>content-length</b>: 0
</pre>

Não consegui sacar como usar PUT:

<pre>
<font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:
<font color="#268BD2"><b>~</b></font>$ 
curl -X PUT &apos;http://blynk-cloud.com/o08E8QWoQlbKcuiS-LIGpqyXyooRft5x/update/d15&apos; -H &apos;Content-Type: application/json&apos; -d &apos;{&quot;value&quot;:&quot;0&quot;}&apos;
Error parsing body param. {&quot;value&quot;:&quot;0&quot;}<font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~</b></font>$ 
</pre>

Existe uma página web para criar a requisição: <https://blynkapi.docs.apiary.io/#reference/0/get-pin-value/get-pin-value?console=1>

Enfim, dá para ler e escrever pela aplicação, por CURL e pelo navegador (deduzi, não testei).

SUCESSO com LEDs.

blynkTresLED.ino

## interrompido: 2020-10-08-221957

## iniciado: 2020-10-09-090940

Ontem à noite percebi que só de colocar o blynk para rodar, posso, sem adicionar código no ESP, controlar as GPIOs. Funciona com o ADC também.

Sobre o PUT, acho que achei a sintaxe correta em <>

<pre><font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~</b></font>$ curl -X PU<font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~</b></font>$ curl -X GET -i &apos;http://blynk-cloud.com/o08E8QWoQlbKcuiS-LIGpqyXyooRft5x/get/adc&apos;
HTTP/1.1 400 Bad Request
<b>connection</b>: keep-alive
<b>content-type</b>: text/plain;charset=utf-8
<b>access-control-allow-origin</b>: *
<b>content-length</b>: 17

Wrong pin format.<font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~</b></font>$ curl -X GET -i &apos;http://blynk-cloud.com/o08E8QWoQlbKcuiS-LIGpqyXyooRft5x/get/d15&apos;
HTTP/1.1 200 OK
<b>connection</b>: keep-alive
<b>content-type</b>: application/json;charset=utf-8
<b>access-control-allow-origin</b>: *
<b>content-length</b>: 5

[&quot;1&quot;]<font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~</b></font>$ curl -X GET -i &apos;http://blynk-cloud.com/o08E8QWoQlbKcuiS-LIGpqyXyooRft5x/get/a0&apos;
HTTP/1.1 400 Bad Request
<b>connection</b>: keep-alive
<b>content-type</b>: text/plain;charset=utf-8
<b>access-control-allow-origin</b>: *
<b>content-length</b>: 39

Requested pin doesn&apos;t exist in the app.<font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~</b></font>$ curl -X PU<font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~</b></font>$ curl -X PUT &apos;http://blynk-cloud.com/o08E8QWoQlbKcuiS-LIGpqyXyooRft5x/update/d15&apos; -H &apos;Content-Type: application/json&apos; -d &apos;[\n&quot;1&quot;\n]&apos;
<font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~</b></font>$ curl -X PUT &apos;http://blynk-cloud.com/o08E8QWoQlbKcuiS-LIGpqyXyooRft5x/update/d15&apos; -H &apos;Content-Type: application/json&apos; -d &apos;[\\n&quot;1&quot;\\n]&apos;
<font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~</b></font>$ 
</pre>

Consegui ler o pino analógico do ESP8266 com curl. O pino é o d17. Informado [neste post](https://community.blynk.cc/t/http-api-restful/8844/23) do fórum do blynk.

<pre>Requested pin doesn&apos;t exist in the app.<font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~</b></font>$ curl -X GET -i &apos;http://blynk-cloud.com/o08E8QWoQlbKcuiS-LIGpqyXyooRft5x/get/d17&apos;
HTTP/1.1 200 OK
<b>connection</b>: keep-alive
<b>content-type</b>: application/json;charset=utf-8
<b>access-control-allow-origin</b>: *
<b>content-length</b>: 7

[&quot;358&quot;]<font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~</b></font>$ 

</pre>

sites em que pesquisei:

https://mail.google.com/mail/u/0/#search/blynk/FMfcgxwKhqdfPzCwMRlrvRhFRJqQdzMW
https://examples.blynk.cc/?board=ESP8266&shield=ESP8266%20WiFi&example=Widgets%2FLED%2FLED_Blink
https://blynk.io/
https://blynk.io/en/getting-started
https://github.com/blynkkk/blynkkk.github.io/blob/master/SupportedHardware.md
https://github.com/blynkkk/blynk-library
http://docs.blynk.cc/#blynk-firmware
http://docs.blynk.cc/#widgets-controllers-button
https://docs.blynk.cc/#blynk-firmware-digital-analog-pins-control
https://github.com/blynkkk/blynk-server/find/master
http://docs.blynk.cc/#blynk-firmware
http://help.blynk.cc/en/
http://help.blynk.cc/en/collections/349312-faq
https://mail.google.com/mail/u/1/#inbox
https://blynk.io/
https://www.google.com/search?client=ubuntu&hs=rKP&channel=fs&sxsrf=ALeKk015n6E_Q0L16MBxwL7MEC6qlPCVNg%3A1602204242797&ei=UrJ_X6aIMPGpytMPpueMoAk&q=blynk+esp8266+url+for+gpio&oq=blynk+esp8266+url+for+gpio&gs_lcp=CgZwc3ktYWIQAzoECAAQRzoECCMQJzoCCAA6BQgAEMsBOgYIABAWEB46BQghEKABOggIIRAWEB0QHjoHCCEQChCgAVCdvgJYsJEDYOqTA2gAcAJ4AIAB6wKIAd4mkgEGMi0xNC41mAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab&ved=0ahUKEwim-f71o6bsAhXxlHIEHaYzA5QQ4dUDCAw&uact=5
https://community.blynk.cc/t/esp8266-gpio-pins-info-restrictions-and-features/22872/19
https://community.blynk.cc/t/webhook-from-browser-does-not-work-though-i-can-control-the-pin-from-blynk-app/34967
https://blynkapi.docs.apiary.io/#reference/0/write-pin-value-via-put/write-pin-value-via-put?console=1
https://www.google.com/search?channel=fs&client=ubuntu&q=send+put+with+curl
https://stackoverflow.com/questions/13782198/how-to-do-a-put-request-with-curl
https://www.google.com/search?client=ubuntu&hs=2Ca&channel=fs&sxsrf=ALeKk006W7kfAtNuyv4gQK1B7QQhBCE_dQ%3A1602246040782&ei=mFWAX5SoL9LC5OUP9eepkAg&q=blynk+url+for+esp8266&oq=blynk+url+for+esp8266&gs_lcp=CgZwc3ktYWIQAzoECAAQR1DdnQ5YgrQOYIq-DmgBcAN4AIABkgGIAf4GkgEDMC43mAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab&ved=0ahUKEwiU1OnQv6fsAhVSIbkGHfVzCoIQ4dUDCAw&uact=5
https://gist.github.com/agungsugiarto/8e2030465cbf5638162e855306f5209d
https://blynkapi.docs.apiary.io/#reference/0/write-pin-value-via-put/write-pin-value-via-put
https://docs.blynk.cc/#hardware-set-ups-esp8266-standalone
https://github.com/blynkkk/blynk-library/blob/master/src/Blynk/BlynkProtocolDefs.h
http://docs.blynk.cc/#blynk-firmware
https://www.instructables.com/ESP8266-12-blynk-wireless-temperature-LM35-sensor/
https://examples.blynk.cc/?board=NodeMCU&shield=ESP8266%20WiFi&example=Widgets%2FWebHook%2FWebHook_GET
https://www.instructables.com/Blynk-With-ESP8266/
https://autocorerobotica.blog.br/monitoramento-de-ambiente-com-nodemcu/
https://mjrobot.org/2016/10/15/do-blink-ao-blynk/
https://mjrobot.org/from-blink-to-blynk/
https://web.whatsapp.com/
https://www.google.com/search?channel=fs&client=ubuntu&q=esp8266+adc+gpio+pin
https://randomnerdtutorials.com/esp8266-adc-reading-analog-values-with-nodemcu/
https://www.google.com/search?channel=fs&sxsrf=ALeKk01re0YMh02MacbVSnFD4qrflynoxg:1602247109499&source=univ&tbm=isch&q=esp8266+adc+gpio+pin&client=ubuntu&sa=X&ved=2ahUKEwjq7rbOw6fsAhUpILkGHbMwCy4Q7Al6BAgJEF8#imgrc=bF3MDYvnicyjeM
https://www.google.com/search?client=ubuntu&hs=CxF&channel=fs&sxsrf=ALeKk00KhldHL6oQfLyEPHsoQqUikEOpKg%3A1602247619058&ei=w1uAX8z7Auax5OUPh7q2qAM&q=blynk+analog+adc+url&oq=blynk+analog+adc+url&gs_lcp=CgZwc3ktYWIQAzoECAAQR1Cr9AxYuoANYIKHDWgAcAJ4AIABjQKIAfAHkgEFMC42LjGYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=psy-ab&ved=0ahUKEwiM6bPBxafsAhXmGLkGHQedDTUQ4dUDCAw&uact=5
https://learn.sparkfun.com/tutorials/blynk-board-project-guide/project-5-gauging-the-analog-to-digital-converter
https://www.google.com/search?channel=fs&client=ubuntu&q=blynk+list+existing+pins
https://github.com/blynkkk/blynkkk.github.io/blob/master/Widgets.md
https://stackoverflow.com/questions/61801098/how-to-read-analog-pin-data-from-the-blynk-http-restful-api
https://community.blynk.cc/t/http-api-restful/8844/23

## interrompido: 2020-10-09-111550

## início: 2020-10-09-130000

(estimado de memória)

Fazendo vídeos de demonstração, encontrei algo que pode ser um problema: Até onde consegui entender,usando o código padrão (Blynk/blink), a leitura da entrada analógica não é atualizada em blynk-cloud quando não há cliente conectado. Tentei resolver isso colocando um Blynk.timer com uma função que imprime uma mensagem no monitor serial. Não resolveu. Então a solução que vi foi incluir um Blink.virtualWrite, como no código do DHT. Isto faz atualizar a informação no blynk-cloud.

## 2020-10-09-145437

Terminei de gravar os vídeos. 
Divulgado para os colaboradores.

## interrompido: 2020-10-09-161952

## início: 2020-10-09-165006

começando relatório.


