# ESP32-CAM

## 2020-10-14-193232

Escrevi proposta. Queria escrever parte do relatório, mas não vai dar tempo hoje...



[Servidor de fotos usando RasPi ou Bluehost](https://randomnerdtutorials.com/esp32-cam-post-image-photo-server/)


[Pinagem do ESP32-CAM](https://randomnerdtutorials.com/esp32-cam-ai-thinker-pinout/): O RESET não é acessível por pino. Tem um diagrama esquemático que vale a pena ver e copiar.

[Comparação entre modelos de ESP32 com câmera](https://makeradvisor.com/esp32-camera-cam-boards-review-comparison/)

[Revisão do modelo que tenho no site da comparação entre modelos](https://makeradvisor.com/esp32-cam-ov2640-camera/)

[Código fonte do exemplo mais atual](https://github.com/espressif/arduino-esp32/tree/master/libraries/ESP32/examples/Camera/CameraWebServer)

[Video streamming web server para home assistante e NodeRED](https://randomnerdtutorials.com/esp32-cam-video-streaming-web-server-camera-home-assistant/)

[Reconhecimento facial](https://randomnerdtutorials.com/esp32-cam-video-streaming-face-recognition-arduino-ide/)

[setup para WROOVER](https://www.instructables.com/Getting-Started-With-ESP32-CAM-Streaming-Video-Usi/)

[Em Português (Fernando K)](https://www.fernandok.com/2019/04/esp32-com-camera-e-reconhecimento-facial.html)

[Em Português do bit ao byte](https://www.dobitaobyte.com.br/esp32-cam-esp32-com-camera-intercambiavel/)

Notas minhas: Ao invés de FTDI usei a interface serial do WittyBoard. Olhando na placa do ESP8266 para referência dos pinos, a conexão é TX com TX e RX com RX.

O RSSI a 5m de distância é -80dBm. Na minha opinião é muito baixo. Isto compromete a qualidade da conexão e a taxa de transmissão. A 1m RSSI=-70dBm.

## 2020-10-14-201856

Por hoje é só.

## 2020-10-15-103646

Desde as 8:30 pesquisando.

Resultados:

1. [Blynk, em 2017, não tinha streamming server](https://github.com/blynkkk/blynkkk.github.io/blob/master/mobile/video.md). Não achei atualização.
2. Os projetos de vídeo usando blynk, que encontrei, usam rede local:
    - <https://community.blynk.cc/t/video-streaming-widget-instructions/20015/4>
    - <https://community.blynk.cc/t/blynk-video-streaming-success/8846/34>
    - <https://community.blynk.cc/t/video-streaming-widget-instructions/20015/10>
    - <https://community.blynk.cc/t/any-info-on-converting-ip-cam-streams-into-video-widget/23007>
    - [Blynk para fazer streaming](https://www.youtube.com/watch?v=XRcTUiXUxEM): só em modo local.
3. Há algumas alternativas de formato de vídeo e servidor web com ESP32
    - <https://github.com/BugerDread/esp32-mjpeg-ipcam>
    - <https://www.hackster.io/anatoli-arkhipenko/multi-client-mjpeg-streaming-from-esp32-47768f#toc-practical-application-6>
    - <https://github.com/arkhipenko/esp32-cam-mjpeg-multiclient>
4. O framerate da ordem de 1fps para 320x240QVGA e de menos de 0.5fps para VGA e o RSSI de -70dBm a 3m do AP parece ser consequência da falta de antena externa.
    - <https://dronebotworkshop.com/esp32-cam-intro/> - mostra resistor de conexão com antena
    - <https://randomnerdtutorials.com/esp32-cam-connect-external-antenna/> - mostra resistor de conexão com antena - este, em especial, avisa que os projetos podem fracassar por questão de antena.
5. A antena no [ML](https://produto.mercadolivre.com.br/MLB-1373532127-antena-para-esp32-cam-24gb-wireless-com-cabo-conector-ipex-_JM?matt_tool=79246729&matt_word=&matt_source=google&matt_campaign_id=6542746973&matt_ad_group_id=82254694281&matt_match_type=&matt_network=u&matt_device=c&matt_creative=385099301982&matt_keyword=&matt_ad_position=&matt_ad_type=&matt_merchant_id=146967446&matt_product_id=MLB1373532127&matt_product_partition_id=472057081367&matt_target_id=pla-472057081367&gclid=CjwKCAjw5p_8BRBUEiwAPpJO6wGm4cz01TBbHopXv41DMtZXjH2byl3en7pkNHRNbmcr0nftPUT6ShoCmk8QAvD_BwE) custa 24+18; o [WROOVER com antena](https://produto.mercadolivre.com.br/MLB-1613323063-modulo-esp32-wifi-e-bluetooth-esp-wroom-32u-antena-24-_JM#reco_item_pos=0&reco_backend=machinalis-domain-pads&reco_backend_type=low_level&reco_client=vip-pads&reco_id=03a163e5-54c4-4c5f-8bd5-e639c90b85fc&is_advertising=true&ad_domain=VIPCORE_RECOMMENDED&ad_position=1&ad_click_id=N2ZmNjEzMTQtY2M3ZC00NzRjLTg2YmUtMGNlMTQ5NDVhYTdi) 60+15

Vou testar com o outro módulo e o exemplo mais recente. Para isto estou clonando o repositõrio: <https://github.com/espressif/arduino-esp32.git>

Usei alguma informação deste repositório: <https://www.dobitaobyte.com.br/ttgo-t-camera-com-esp32-wrover/> e clonei este repositório: <https://github.com/lewisxhe/esp32-camera-series.git>. É este que estou usando como `TTGO-Camera-FN.ino` placa esp32-wrover-module.

Da primeira vez que tentei carregar o sketch deu erro de conexão. Achei que ia ter um problemão, mas não - era mau contato no cabo USB na ponta micro-USB (eliminei desconectando e conectando de volta). Aí o programa tranferiu direitinho e tenho framerate de 3fps com resolução de 1600x1200 e 10fps em VGA.

A transmissão da imagem pela internet envolve questões mais complicadas. 
Achei servidor na internet que simplesmente recebe o stream e encaminha para clientes que se conectarem. O Blynk não faz isso, [o nabto diz que faz - ainda não testei](https://www.nabto.com/esp32/). O que encontrei é abrir uma VPN, ou um túnel ou um proxy e ter um computador ligado 24h em casa...:

- <https://www.zerotier.com/>
- [Usando um túnel IP](https://www.elementzonline.com/blog/Accessing-ESP32-CAM-Video-Streaming-from-anywhere-in-the-world)
     - <https://medium.com/better-programming/ngrok-make-your-localhost-accessible-to-anyone-333b99e44b07>
     - <https://ngrok.com/>
     - <https://www.itexto.com.br/site/receita-expondo-seu-localhost-ao-mundo-com-ngrok/>
     - <https://www.twilio.com/blog/2015/09/6-awesome-reasons-to-use-ngrok-when-testing-webhooks.html>
     - mas tem questões de segurança
         - <https://stackoverflow.com/questions/36552950/is-ngrok-safe-to-use-or-can-it-be-compromised>
         - <https://www.reddit.com/r/learnprogramming/comments/de2f8c/is_ngrok_safe/>
         - <https://www.vpnmentor.com/blog/top-really-free-vpn-services/>

[Como um túnel IP funciona (wikipedia)](https://pt.wikipedia.org/wiki/T%C3%BAnel_IP)

Achei também esta página com os problemas mais comuns de ESP32-CAM: <https://randomnerdtutorials.com/esp32-cam-troubleshooting-guide/>

Esta com comparativo e programas de várias câmeras: <https://github.com/lewisxhe/esp32-camera-series>, inclusive é daqui que peguei o TTGO-Camera-FN.ino.



Todas as alternativas que encontrei expõe toda a rede local.






    


