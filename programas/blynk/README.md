# Blynk

Uso Blynk para ler/escrever dados nos dispositivos através da internet. Até certo uso, o serviço é gratuito.

[Site oficial do Blynk](https://blynk.io/)

Uso o app para celular ([Android](https://play.google.com/store/apps/details?id=cc.blynk&hl=pt_BR), [iOS](https://apps.apple.com/br/app/blynk-iot-for-arduino-esp32/id808760481)) para desenvolver um app personalizado, contendo elementos como chaves, indicadores, LEDs,... 

O desenvolvimento do app cria automaticamente a infraestrutura de nuvem necessária para conectar os elementos do app aos componentes do dispositivo. A URL da infraestrutura é blynk-cloud.com. O protocolo de comunicação com a infraestrutura é HTTP ([Documentação da API](https://blynkapi.docs.apiary.io/#)) e o acesso a um dispositivo específico é especificado por um token enviado por e-mail para o desenvolvedor do app personalizado.

Exemplos de código para diversas plataformas podem ser personalizados e baixados [aqui](https://examples.blynk.cc/?board=ESP8266&shield=ESP8266%20WiFi&example=GettingStarted%2FBlynkBlink).

Eles têm [tutoriais](https://blynk.io/en/getting-started) que mostram passo-a-passo sobre como usar a ferramenta.

Também há uma [comunidade de desenvolvedores](https://community.blynk.cc/).

Essas facilidades não foram suficientes para eu conseguir usar sem precisar codificar e ler a [documentação](http://docs.blynk.cc/). Em alguns momentos tive que entrar no código-fonte das ferramentas deles. [O repositório é github](https://github.com/blynkkk). Por exemplo, precisei de mais ou menos um dia de trabalho (8h) para achar como enviar dados para o dispositivo através do navegador, ou de `curl`, e que o ADC do ESP8266 é acessado pelo 'pino' `d17`. Mais detalhes no projeto para [controlar tomada pela internet](../../projetos/ControlarTomadaPelaInternet/README.md)

Há vários exemplos de uso de blynk com DHTXX. Eles não mostram como consultar através de `curl`, ou `Java`, ou `C`, o que é contemplado no projeto do Controle de Tomada.

- [Node ESP8266 com DHT, em Português](http://www.blogdarobotica.com/2020/07/14/monitorando-temperatura-e-umidade-pelo-celular-utilizando-a-plataforma-blynk/)
- [Node ESP8266 com DHT, em Inglês](https://www.hackster.io/Manoranjan2050/dht11-and-nodemcu-with-blynk-10e6b1)
- [Node 32s com DHT, sensor de chuva e BMP280](https://www.curtocircuito.com.br/blog/analise-climatica-esp32-blynk)


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
https://examples.blynk.cc/?board=ESP8266&shield=ESP8266%20WiFi&example=Widgets%2FLED%2FLED_Blink
https://github.com/blynkkk/blynkkk.github.io/blob/master/SupportedHardware.md
http://docs.blynk.cc/#blynk-main-operations-get-data-from-hardware-pushing-data-from-hardware
http://docs.blynk.cc/#widgets-controllers-button
https://github.com/FNakano/CFA/tree/master/projetos/ControlarTomadaPelaInternet
https://mjrobot.org/2016/10/15/do-blink-ao-blynk/
https://community.blynk.cc/t/solved-timer-setinterval-best-use/14862/10
https://docs.blynk.cc/#widgets-controllers-timer
https://community.blynk.cc/t/please-help-with-timer/22810/4
https://github.com/blynkkk/blynkkk.github.io/blob/master/Widgets.md

