# Ethernet

IEEE 802

IEEE 802.11 = wifi

IEEE 802.14 = Zigbee

## mDNS

Domain Name System (DNS) é o sistema que associa nomes de domínio, por exemplo voce.com.br, com um IP, por exemplo 192.168.1.1 .

Na World Wide Web (WWW), há alguns servidores que armazenam essa informação.

mDNS significa multicast DNS e é um protocolo para resolução de nomes de domínio baseado em multicast. Simplificadamente, um cliente que acessar um servidor através do nome do domínio "pergunta" ao gateway a que está conectado, 'qual o IP correspondente a este nome de domínio'. O gateway que 'conhecer' o nome de domínio envia o IP como resposta, o gateway que não conhecer, encaminha a "pergunta" para o gateway acima, e assim por diante.

O ESP32 tem suporte a mDNS. 

Linux tem suporte através de avahi;
macOS tem suporte através de Bonjour;
Windows tem suporte através de ???

Numa rede com suporte a mDNS, o nome substitui o IP, o que é mais prático que usar (memorizar) o IP. Ainda se a rede não tiver IPs fixos, que é a regra em redes com DHCP (Dynamic Host Configuration Protocol), em que os IPs são distribuídos por um servidor (em redes domésticas, geralmente o Ponto de Acesso Internet é o servidor DHCP).

No ESP32, acrescenta-se uma biblioteca e chama-se uma função no setup, após a conexão com o AP <https://techtutorialsx.com/2020/04/17/esp32-mdns-address-resolution/>:

```
#include <ESPmDNS.h>
...

void setup(){
  Serial.begin(115200);
  
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
 
  if(!MDNS.begin("esp32")) {                    // o nome do domínio é esp32.local
     Serial.println("Error starting mDNS");
     return;
  }
  
  Serial.println(WiFi.localIP());
  
  server.on("/hello", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send(200, "text/plain", "Hello World");
  });
  
  server.begin();
}
```



## Referências

- [ESPRESSIF mDNS](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/protocols/mdns.html)
- [Wikipedia em Português](https://pt.wikipedia.org/wiki/Sistema_de_Nomes_de_Dom%C3%ADnio)
- [Wikipedia em Inglês](https://en.wikipedia.org/wiki/Domain_Name_System)
- [mDNS - RFC6762](https://tools.ietf.org/html/rfc6762)

