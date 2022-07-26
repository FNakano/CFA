**em construção**

## Resumo do resultado

Consegui usar o ESPCAM, emulado como IP webcam, como fonte de vídeo para o google meet.

Programa no ESPCAM: `CameraWebServer-20220726.ino`
Programas no Linux:

```
sudo modprobe v4l2loopback
sudo ffmpeg -f mjpeg  -i http://192.168.1.100:81/stream -vf format=yuv420p -f v4l2 -an /dev/video2
```

Camera no google Meet: `Dummy video device (0x0000)`

## Objetivo

Usar ESP-CAM com Google Meet.

## Motivação

Na minha percepção, captação e processamento de vídeo atrai muitos desenvolvedores, mas envolve complexidades (ou seriam complicações?) técnicas e dificuldade em conseguir informação útil para resolver questões de dispositivos específicos.

Em 2021, um colega propôs construir um dispositivo que capta uma imagem, envia para uma IA (treinada por ele) no Reckognition (https://aws.amazon.com/pt/rekognition/) e informa se a imagem contém um rosto com uma máscara. Trabalhamos bastante no projeto que chegou à captação da imagem pelo dispositivo (uma pessoa tira uma foto com o dispositivo), envio da foto para a IA (uma pessoa envia para a IA) e resposta com o dispositivo (recebe resposta pela web e acende um LED). Apesar do trabalho investido, o resultado foi pouco.

<!--- Existes produtos prontos com funções similares. Não vem ao caso se considero suas características boas ou ruins, mas relaciono algumas: são caros, não programáveis, código fechado, podem ser descontinuados,... --->


O que é ESP CAM

## Materiais

Foto da ESP CAM usada, link do fornecedor: https://pt.aliexpress.com/item/1005001597435442.html?spm=a2g0o.order_list.0.0.3669caa4xUPnhV&gatewayAdapt=glo2bra - CUSTA UNS R$40 cada câmera.

Tenho outra, com grande angular e night vision, não testei: https://pt.aliexpress.com/item/4000589847400.html?spm=a2g0o.order_list.0.0.3669caa4xUPnhV&gatewayAdapt=glo2bra

Pinagem: https://www.circuitschools.com/how-to-program-upload-the-code-to-esp32-cam-using-arduino-or-programmer/

Como adivinhei o tipo de câmera? https://randomnerdtutorials.com/esp32-cam-troubleshooting-guide/

## Procedimento
- Conectar ESP CAM à placa de comunicação (geralmente é FTDI. No caso, usei a do wittyboard)

| aaa | ESP CAM | witty |
| --- | --- | --- |
| --- | UOTXD | txd |
| --- | U0RXD | rxd |
| --- | 5V | VCC |
| --- | GND | GND |

- Programar ESP CAM com o programa certo
   - Configurar IDE para programar WROOVER com programa grande (3M app, 1M SPIFFS);
   - Conectar com a placa de comunicação e esta à USB, GPIO0 conectado ao GND provoca entrada no modo de programação (https://randomnerdtutorials.com/esp32-cam-troubleshooting-guide/);
      - não ter acesso ao pino de RESET não é problema, mas, talvez, na programação, mesmo com GPIO0=GND, em algumas ocasiões seja necessário pressionar o botão de reset para iniciar a programação;
      - Exemplo `CameraWebServer` da IDE do Arduino, selecionando `CAMERA_MODEL_AI_THINKER` e configurando SSID e senha
         - `CameraWebServer-20220726.ino`
      - no monitor serial o IP atribuído à ESP CAM é escrito;
   - checar funcionamento usando um navegador para acessar `<IP>:80`
      - habilitar o stream de vídeo
      - consequentemente o stream é acessado em `http://<IP>/81/stream`
      - só um cliente pode acessar.
- Emular uma webcam com `sudo modprobe v4l2loopback` (só cria o dispositivo)
- Transcodificar o stream vindo do dispositivo e encaminhar (forward) para o emulador de webcam com `sudo ffmpeg -f mjpeg  -i http://192.168.1.100:81/stream -vf format=yuv420p -f v4l2 -an /dev/video2`
   - no `ffmpeg`, o que vem antes de `-i` é configuração de entrada e o que vem depois do argumento de `-i` e antes do nome do dispositivo de saída é configuração de saída;
   - a ESP CAM gera o stream em mpeg, yuv422;
   - por isso `-f mjpeg` antes de `-i`;
   - a maioria das câmeras para consumidor usa yuv420 (https://stackoverflow.com/questions/69132155/conversion-to-yuv422p-pixel-format-is-incorrect), então o formato de saída, provavelmente, deve ser ajustado para yuv420, por isso o `-vf format=yuv420p` antes do nome do dispositivo de saída (https://stackoverflow.com/questions/60808333/unknown-v4l2-pixel-format-equivalent-for-yuvj420p).
- Abrir um google meet, especificando como fonte de vídeo a câmera emulada (geralmente, Dummy video device (0x0000))   

## Resultados

### Pinagem 

### Comandos

### Referências consultadas

file:///home/fabio/Documentos/Anotacoes/OAC1/aula-2021-04-13/Arquitetura%20e%20organiza%C3%A7%C3%A3o%20de%20computadores.pdf
https://www.google.com/search?q=mjpeg+amazon+recognition&client=ubuntu&hs=8ph&channel=fs&ei=rNbfYvKjGaTZ5OUP3bG-6AU&ved=0ahUKEwjyqaGLwJb5AhWkLLkGHd2YD10Q4dUDCA0&uact=5&oq=mjpeg+amazon+recognition&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsAM6BAghEApKBAhBGABKBAhGGABQsjtYrUJgrnJoAXABeACAAZEBiAH0BJIBAzAuNZgBAKABAcgBBsABAQ&sclient=gws-wiz
https://stackoverflow.com/questions/41228649/aws-rekognition-invalidimageformatexception-when-jpeg-source-is-mjpeg-stream
https://aws.amazon.com/pt/rekognition/
https://www.networkwebcams.co.uk/blog/2008/12/01/mjpeg/
https://en.wikipedia.org/wiki/Motion_JPEG
https://stackoverflow.com/questions/63539799/how-to-forward-mjpg-webcam-to-virtual-video-device-using-ffmpeg
http://192.168.1.100/
https://github.com/geeksville/Micro-RTSP
https://github.com/geeksville/Micro-RTSP/blob/master/test/RTSPTestServer.cpp
https://github.com/geeksville/Micro-RTSP/blob/master/test/README.md
https://askubuntu.com/questions/881305/is-there-any-way-ffmpeg-send-video-to-dev-video0-on-ubuntu
https://stackoverflow.com/questions/63539799/how-to-forward-mjpg-webcam-to-virtual-video-device-using-ffmpeg
https://trac.ffmpeg.org/wiki/StreamingGuide
https://superuser.com/questions/1293783/ffmpeg-stream-video-file-to-fake-webcam
https://www.google.com/search?q=ffmpeg+forward+http+mjpeg+to+v4l2&client=ubuntu&hs=ilN&channel=fs&ei=m9_fYvaeI8P21sQPgou9sAc&ved=0ahUKEwi22O7NyJb5AhVDu5UCHYJFD3YQ4dUDCA0&uact=5&oq=ffmpeg+forward+http+mjpeg+to+v4l2&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsANKBAhBGABKBAhGGABQvCdY5ERg_E1oAXABeACAAZQBiAHGDJIBBDAuMTKYAQCgAQHIAQjAAQE&sclient=gws-wiz
https://gist.github.com/peterhellberg/ebfc72147c2009ee720aafe57ce9c141
https://superuser.com/questions/751568/use-a-ip-camera-as-a-virtual-camera
https://www.google.com/search?channel=fs&client=ubuntu&q=%5Bvideo4linux2%2Cv4l2+%40+0x55b741312e00%5D+Unknown+V4L2+pixel+format+equivalent+for+yuvj422p+Could+not+write+header+for+output+file+%230+%28incorrect+codec+parameters+%3F%29%3A+Invalid+argument+Error+initializing+output+stream+0%3A0+--++
https://stackoverflow.com/questions/60808333/unknown-v4l2-pixel-format-equivalent-for-yuvj420p
https://docs.kernel.org/userspace-api/media/v4l/pixfmt-intro.html
https://github.com/baresip/baresip/issues/639
https://stackoverflow.com/questions/69132155/conversion-to-yuv422p-pixel-format-is-incorrect
https://meet.google.com/

