# Usar celular como câmera IP que emula uma webcam no Linux
**primeira, por enquanto única parte de uma série sobre câmeras.**
*em colaboração com LucasFerrazBR*

## Objetivos

1. Entender/apresentar um pouco mais sobre o conjunto de ferramentas e conceitos em torno de *streaming*;
   1. Com isso, talvez, ajustar o addon do [WebThings](https://github.com/WebThingsIO) para [câmera ONVIF](https://github.com/WebThingsIO/onvif-adapter).
2. Dar uso para um celular antigo;

## Motivação

*ainda muito primária, mas serve como início.*

Deseja-se usar WebthingsIO como ferramenta de coordenação de dispositivos inteligentes.

Um dispositivo útil é a câmera.

O addon do WebThings para câmeras foi testado e funciona em alguns modelos de câmeras, mas são modelos dificeis de encontrar no Brasil. Modelos encontrados no Brasil tem alguma incompatibilidade com o WebThings, que faz com que este não consiga exibir o vídeo gerado pela câmera.

O exame do código-fonte do add-on mostra como a informação da câmera é *desempacotada*. Partes dessa informação são protocolo e IP usados pela câmera e ferramentas externas. Para mostrar o vídeo, há indicações de que é usado  [ffmpeg](https://www.ffmpeg.org/) e [Mozilla DASH](https://developer.mozilla.org/en-US/docs/Web/Media/DASH_Adaptive_Streaming_for_HTML_5_Video)

Isto mostra que é conveniente entender melhor essas ferramentas. À medida que estas foram sendo estudadas, percebeu-se a possibilidade e a conveniência de *aproveitar um celular antigo como webcam* como objetivo intermediário.

## Lista de materiais

1. Celular antigo - no teste usou-se um [galaxy young 2](https://www.tudocelular.com/Samsung/fichas-tecnicas/n2682/Samsung-Galaxy-Young-2.html);
2. App [IP webcam para Android](https://play.google.com/store/apps/details?id=com.pas.webcam);
3. Computador com Linux - no teste usou-se um notebook com Ubuntu 20.04;
4. Ferramentas para Linux:
   1. ffmpeg
   2. v4l2loopback
   3. Navegador web - no teste usou-se Firefox 95.0.1
   4. Google Meet - a câmera será testada em uma videochamada de google meet;
   
## Procedimento

1. Instalar no computadro ffmpeg
   - Executar `sudo apt install ffmpeg`;
2. Instalar no computador v4l2loopback
   - Executar `sudo apt install v4l2loopback-dkms`
   - Executar `sudo apt install v4l2-utils`
3. Instalar no celular IP webcam
   - entrar no Google Play, localizar o app e instalar
4. Testar celular e computador
   - Certifique-se que o computador e o celular estão conectados ao mesmo Ponto de Acesso (roteador) WiFi;
   - No celular, executar o app, entrar em network configuration, ajustar o nome do usuário para `admin` e a senha para `admin`, depois, iniciar o servidor (nos três pontos do topo-direita da tela);
   - A tela do celular passa a mostrar a imagem da câmera e um conjunto de IPs. Clique em *more* e anote a URL de RTSP.
   - No computador, abra um terminal e digite `ffplay <URL de RTSP>`. Uma janela é aberta e o vídeo da câmera é mostrado. No teste usou-se `ffplay rtsp://admin:admin@192.168.1.103:8080/h264_ulaw.sdp`
   - Caso a imagem apareça distorcida, com artefatos, provavelmente a velocidade do celular ou da rede não é suficiente. Neste caso, tente diminuir o framerate (por exemplo de 30 para 10 fps), e/ou a resolução;
   - Se isto aconteceu, celular e computador estão configurados corretamente, pode encerrar o `ffplay`;
5. Verificar que dispositivos de vídeo existem no computador;
   - No linux, todo dispositivo é representado por um arquivo na pasta `/dev`. O arquivo é necessário para que os programas acessem o dispositivo;
   - Executar `v4l2-ctl --list-devices`;
   - Anotar ou lembrar que dispositivos já existem;
6. Criar o arquivo que representa uma câmera *dummy*;
   - Executar `sudo modprobe v4l2loopback`;
      - Para criar dois dispositivos, usar `sudo modprobe v4l2loopback devices=2`
7. Verificar se o dispositivo foi criado;
   - Executar `v4l2-ctl --list-devices`;
   - Comparar com o resultado do passo 5;
      - No teste, o arquivo/dispositivo criado é `/dev/video3`;
8. Associar o *stream RTSP* com o arquivo/dispositivo;
   - Executar `sudo ffmpeg -i <URL de RTSP> -f v4l2 <DISPOSITIVO>`
      - No teste: `sudo ffmpeg -i rtsp://admin:admin@192.168.1.105:8080/h264_ulaw.sdp -f v4l2 /dev/video3`
9. (Opcional) Testar se o vídeo pode ser acessado através de <DISPOSITIVO>
   - Executar `ffplay <DISPOSITIVO>`
      - No teste `ffplay /dev/video3`
      - abre uma janela e mostra o vídeo;
      - encerrar `ffplay`;
10. Iniciar uma video-chamada no google meet;
   - O google meet vai pedir acesso ao microfone e dispositivo de vídeo.
   - [Captura de tela mostrando a tela do meet](./Captura de tela de 2022-01-04 19-50-23.png)

Referências em ordem de relevância (decidida pelos autores):

- https://rmsol.de/2020/04/25/v4l2/
- https://atinkerholic.wordpress.com/2018/10/10/how-to-use-a-virtual-webcam-with-static-image-or-video-ffmpeg-v4l-utils-and-v4l2loopback/
- https://github.com/umlaeute/v4l2loopback/issues/151
- https://askubuntu.com/questions/1314501/can-you-create-a-virtual-dev-video-that-contains-either-dev-video0-or-dev-vid
- https://superuser.com/questions/411897/using-desktop-as-fake-webcam-on-linux
- https://askubuntu.com/questions/881305/is-there-any-way-ffmpeg-send-video-to-dev-video0-on-ubuntu

Conclusões:

- v4l2loopback cria um endpoint que permite que permite a conexão entre o gerador e o consumidor do *stream*;
- `ffmpeg` serve para transcodificar e encaminhar o *stream* para um endpoint já existente;
- `ffplay` recebe como argumento um endpoint e mostra o *stream*;
- (suposição) DASH, no servidor, cria um endpoint (URL), que acessada por DASH, no navegador, abre uma janela (seria um popup?) para exibir o *stream*.
