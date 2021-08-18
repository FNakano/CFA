#include <WiFi.h>
#include <ESPmDNS.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>

 const char *ssid         = "..............";
 const char *password     = ".............";

#include <DisplayRolavel.h>

DisplayRolavel tela(0x3c, 4, 15);

int operacaoPendente=0;

void IRAM_ATTR callback1(){
  if (operacaoPendente==0) operacaoPendente=1;
}

void IRAM_ATTR callback2(){
  if (operacaoPendente==0) operacaoPendente=2;
}

long lastEventInstant = 0L;
long now=0L;

void setup() {
#ifdef DEBUG
  Serial.begin(115200);
#endif
  tela.init(4,15);
  tela.concatenaMensagem("É verdade que também na história do pensamento filosófico a regra de ouro é mencionada com regularidade impressionante, desde Santo Agostinho até o século XVIII. " );
                   //     ^1       ^10       ^20       ^30       ^40        ^50       ^60       ^70       ^80       ^90       ^100      ^110      ^120      ^130      ^140      ^150
  operacaoPendente=0;
  touchAttachInterrupt(T8, callback1, 30);
  touchAttachInterrupt(T9, callback2, 30);
  WiFi.begin ( ssid, password );
  // Wait for connection
  int nTentativas=0;
  while ( WiFi.status() != WL_CONNECTED ) {
    tela.concatenaMensagem(">Procurando Wi-fi " + String(++nTentativas, DEC) + " ");
    delay ( 5000 );
  }

  ArduinoOTA.begin();
  ArduinoOTA.onStart([]() {
    tela.concatenaMensagem(">OTA Update ");
    operacaoPendente=3;
  });

  ArduinoOTA.onProgress([](unsigned int progress, unsigned int total) {
    operacaoPendente=3;
    tela.clear();
    tela.drawProgressBar(4, 32, 120, 8, progress / (total / 100) );
    tela.display();
  });

  ArduinoOTA.onEnd([]() {
    operacaoPendente=0;
    tela.concatenaMensagem(">Restart ");
  });

  // Align text vertical/horizontal center
  tela.concatenaMensagem(">Ready for OTA: " + WiFi.localIP().toString());
  lastEventInstant=millis();
}

void loop() {
  now=millis();
  switch (operacaoPendente) {
    case 0: break;
    case 1:
#ifdef DEBUG
      Serial.println("Atendendo touch para anterior");      
#endif
      tela.mostraJanelaAnterior();
      delay(200); // atraso para não ter várias interrupções em um único toque.
      operacaoPendente=0;
      lastEventInstant=now;
      break;
    case 2:
#ifdef DEBUG
      Serial.println("Atendendo touch para posterior");      
#endif
      tela.mostraJanelaPosterior();
      delay(200); // atraso para não ter várias interrupções em um único toque.
      operacaoPendente=0;
      lastEventInstant=now;
      break;
    case 3: // OTA em execução
      lastEventInstant=now;
      break;
  }
  ArduinoOTA.handle();
  if ((now-lastEventInstant)>60000l) {
    esp_sleep_enable_touchpad_wakeup();
    esp_deep_sleep_start();
  }
}


