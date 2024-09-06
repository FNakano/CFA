# Dores

Neste arquivo escreverei sobre problemas frequentes e, quando houver, soluções e mitigações no desenvolvimento de dispositivos IoT.

## Conectar dispositivo à rede e usá-lo

Durante o desenvolvimento de um dispositivo, o que inclui toda cadeia de programas em torno dele, frequentemente é necessário conectar um dispositivo a uma rede pela primeira vez. Isto pode acontecer, por exemplo, quando leva-se o protótipo para um lugar em que a rede é diferente da do local de desenvolvimento usual.

As redes mais simples são administradas através de um, geralmente único, ponto de acesso WiFi.

**nota**: no vocabulário de WiFi, o que é chamado, popularmente, no WiFi doméstico, de roteador WiFi, modem (ADSL), caixinha da Internet, ... é, tecnicamente, chamado Ponto de Acesso WiFi (WiFi Access Point) e os dispositivos conectados a ele através do WiFi são Estações (Stations). Daí, as constantes `network.STA_IF` e `network.AP_IF` do Micropython.

Para um dispositivo conectar-se como estação (STA) a um ponto de acesso (AP) e poder ser alcançado, ele precisa conectar-se ao ponto de acesso e ter/receber ou um endereço IP ou um nome de domínio (algo como github.com). Uma forma de conseguir isso é usando WiFi Protected Setup (WPS) e Domain Name Service - Service Discovery (DNS-SD). O ESP32 suporta ambos, até certo ponto. Há exemplos de código tanto para WPS quanto para DNS-SD na ESP-IDF e no Arduino IDE, mas não há, no Micropyton, API que exponha essas funcionalidades.

Dadas essas lacunas, tenho interesse em desenvolver:
  
1. Uma Estação (dispositivo ESP32), programado usando ESP-IDF ou Arduino IDE que conecte-se a um Ponto de Acesso usando WPS Button e DNS-SD;
2. Uma versão de Micropython ESP32 que exponha WPS e DNS-SD;

Por enquanto só tenho a mitigação para Micropython:
  
Conectar, seja como STA, seja como AP, ajustando o nome do domínio com o comando `network.hostname('espoled')` antes de ativar a interface de rede, ou com o comando `wlan.config(dhcp_hostname='espoled')` depois de ativar a interface de rede (referência em algum link abaixo). Como o SSID e o PASSWORD acabam codificados no programa, então, nos lugares em que for usar o protótipo, configurar uma rede convidada ou um AP com o mesmo SSID e PASSWORD do AP do local de desenvolvimento usual (ié, em casa, tenha uma rede para convidados com nome **lab8** e PASSWORD condizente).

```python
import network

WIFI_NETWORK='lab8'
WIFI_PASSWORD='passwordDolab8'

wlan = network.WLAN(network.STA_IF)
#network.hostname('espoled') # isto funciona
wlan.active(True)
wlan.config(dhcp_hostname='espoled') # isto também funciona
wlan.connect(WIFI_NETWORK, WIFI_PASSWORD)

print()
print("Connected to ",WIFI_NETWORK)
```

Com o código acima a Estação "vai" conectar-se ao Ponto de Acesso. A Estação é acessível pelo nome `espoled.local`. `ping` e `avahi-resolve` vão funcionar, embora `avahi-browse` não vá por conta de um problema na implementação do Micropython (referências abaixo).

<pre><font color="#8AE234"><b>fabio@super</b></font>:<font color="#729FCF"><b>~</b></font>$ ping esp.local
^C
<font color="#8AE234"><b>fabio@super</b></font>:<font color="#729FCF"><b>~</b></font>$ ping espoled.local
PING espoled.local (192.168.0.10) 56(84) bytes of data.
64 bytes from 192.168.0.10: icmp_seq=1 ttl=255 time=94.9 ms
64 bytes from 192.168.0.10: icmp_seq=2 ttl=255 time=110 ms
64 bytes from 192.168.0.10: icmp_seq=3 ttl=255 time=33.4 ms
^C
--- espoled.local ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2002ms
rtt min/avg/max/mdev = 33.405/79.536/110.342/33.226 ms
<font color="#8AE234"><b>fabio@super</b></font>:<font color="#729FCF"><b>~</b></font>$ avahi-resolve espoled.local
Nenhum comando especificado.
<font color="#8AE234"><b>fabio@super</b></font>:<font color="#729FCF"><b>~</b></font>$ avahi-resolve -name espoled.local
avahi-resolve: opção inválida -- “m”
<font color="#8AE234"><b>fabio@super</b></font>:<font color="#729FCF"><b>~</b></font>$ avahi-resolve --name espoled.local
espoled.local	192.168.0.10
<font color="#8AE234"><b>fabio@super</b></font>:<font color="#729FCF"><b>~</b></font>$ 
</pre>
 

## Referências

12. Acrescentar WPS e mDNS no Micropython (clonar Micropython, criar um branch, adicionar código (criar arquivos e concatenar com os originais), testar. Na hora de atualizar a versão do Micropython, atualizar o master e ver como readicionar o código);
   - muitas coisas para explicar/documentar
     - mip, upip (https://docs.micropython.org/en/latest/reference/packages.html) precisam de conexão com internet para baixar arquivos (https://docs.arduino.cc/micropython/basics/installing-modules/)
     - achei uma biblioteca para DNS-SD (https://github.com/cbrand/micropython-mdns) mas quando executo os exemplos tenho o erro `OSError: [Errno 112] EADDRINUSE` em `client.py` na linha (agora) 83 `self.socket.bind(("", MDNS_PORT))` tentei consertar com `self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)` (https://forum.micropython.org/viewtopic.php?t=10412#p57684) mas não deu certo. Talvez se eu fizer donwgrade do Micropython...
     - O que eu não estava notando é que MDNS está implementado na versão 1.23 do Micropython. Aparentemente de um jeito meio torto (https://github.com/micropython/micropython/issues/4912) mas que permite, quando se sabe o hostname atribuído à placa, que se faça ping e se busque pelo hostname (`avahi-resolve --name espressif.local`), MAS avahi-browse não localiza a placa pois falta alguma coisa na implementação do dpgeorge.
     - Acontece que com essa implementação ativa, a porta 5353 está de fato ocupada, então o erro que ocorre quando tento usar os exemplos de cbrand é o esperado (e não a surpresa).
     - para cair a ficha precisei das referências:
        1. https://github.com/micropython/micropython/issues/4912#issuecomment-662600459
        2. https://forum.micropython.org/viewtopic.php?t=8426
        3. https://forum.micropython.org/viewtopic.php?t=10979
        4. https://forum.micropython.org/viewtopic.php?t=9535
        5. https://github.com/cbrand/micropython-mdns
        6. https://forum.micropython.org/viewtopic.php?t=3027
        7. https://forum.micropython.org/viewtopic.php?t=8426



Como inserir um dispositivo em uma rede local:

### 1

Eu gostaria que fosse por WPS button mas essa funcionalidade não existe no ramo principal do port para ESP32 do MicroPython. Não sei qual é o problema, parece que não é de implementação, talvez seja da gestão do código como um todo, talvez seja alguma pessoa travando.

O fork que contém a solução contém este arquivo: https://github.com/eydam-prototyping/micropython/blob/master/ports/esp32/modnetwork2.h - buscar pelo string wps dá alguns resultados NO ARQUIVO COM NÚMERO 2 NO NOME.

Eydam-prototyping tentou um PR mas desistiu (https://github.com/micropython/micropython/pull/7452), em 2023 um outro usuário perguntou o motivo, sem resposta.

Antes do PR acima, uma outra pessoa tentou PR (https://github.com/micropython/micropython/pull/4464) mas foi recusado por DPGeorge (https://github.com/micropython/micropython/pull/4464#issuecomment-467315977), o PR mencionado acima corrigia esses problemas mas também não foi incorporado. 

O PR acima apareceu novamente (porque não foi retirado pelo proponente) em uma refatoração para remover a macro STATIC do código: https://github.com/micropython/micropython/pull/13763. Não houve resposta do proponente - acho que ele também desistiu.

Acho que a implementação de WPS no micropython para ESP32 não será feita...

Acho que se pegar o port https://github.com/eydam-prototyping/micropython/blob/master/ports/esp32/ e reaplicar os PRs do Micropython oficial (são uns três anos de PRs)

Fiz um fork com todos os branches e commit history em https://github.com/FNakano/micropython-with-wps O branch que me interessa é o wps-dev.

### 2

Na falta do WPS, o jeito é levantar um AP para cadastrar as credenciais e reiniciar o ESP. Já fizeram isso: https://randomnerdtutorials.com/micropython-wi-fi-manager-esp32-esp8266/
