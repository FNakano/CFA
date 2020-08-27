/**
 * MENSAGEM DA BIBLIOTECA DO DISPLAY SSD1306
 * The MIT License (MIT)
 *
 * Copyright (c) 2018 by ThingPulse, Daniel Eichhorn
 * Copyright (c) 2018 by Fabrice Weinberg
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 *
 * ThingPulse invests considerable time and money to develop these open source libraries.
 * Please support us by buying our products (and not the clones) from
 * https://thingpulse.com
 * 
 * 22.03.2019 - parece que gravou no esp32 eletrolab, mas não acionou o display. Tentarei algo mais simples
 * 29.03 - tentei um hello com mensagem via serial que funcionou (quando conectar pela primeira vez, lembrar de pulsar o enable)
 * 29.03 - vou colocar umas mensagens pela serial.
 * 29.03 - o working do setup apareceu no monitor serial.
 * 29.03 - as mensagens no loop apareceram na serial. O display não acende. Visualmente falta o chip 12c para display. Será que é erro de projeto? Pode ser também que o display seja de outro modelo. As trilhas SDA e SCL estáo ok.
 * 25.07.2020 - Compilei, enviei, funcionou.
 * 
 * 
 *
 */

/*
    Video: https://www.youtube.com/watch?v=oCMOYS71NIU
    Based on Neil Kolban example for IDF: https://github.com/nkolban/esp32-snippets/blob/master/cpp_utils/tests/BLE%20Tests/SampleNotify.cpp
    Ported to Arduino ESP32 by Evandro Copercini
   Create a BLE server that, once we receive a connection, will send periodic notifications.
   The service advertises itself as: 4fafc201-1fb5-459e-8fcc-c5c9c331914b
   And has a characteristic of: beb5483e-36e1-4688-b7f5-ea07361b26a8
   The design of creating the BLE server is:
   1. Create a BLE Server
   2. Create a BLE Service
   3. Create a BLE Characteristic on the Service
   4. Create a BLE Descriptor on the characteristic
   5. Start the service.
   6. Start advertising.
   A connect hander associated with the server starts a background task that performs notification
   every couple of seconds.
*/


int estado=100;
long lastInteractionInstant;

#include <WiFi.h>
#include "time.h"

const char* ssid       = "andro";
const char* password   = "AoInfinitoEAl3m";

const char* ntpServer = "pool.ntp.org";
const long  gmtOffset_sec = -3*3600;     // GMT-3
const int   daylightOffset_sec = 0*3600; // horário de verão

void ajustaRelogioWiFi()
{
  //Serial.begin(115200);
  if (xx_time_get_time()<1595635254000LL) {
    // gambiarra para não escrever agora o código para detectar a rede antes de conectar
    // a idéia é testar a manutenção do tempo durante o deep sleep
    //connect to WiFi
    Serial.printf("Connecting to %s ", ssid);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        if (Serial) Serial.print(".");
    }
    if (Serial) Serial.println(" CONNECTED");
  
    //init and get the time
    configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);
    printLocalTime();

    //disconnect WiFi as it's no longer needed
    WiFi.disconnect(true);
    WiFi.mode(WIFI_OFF);
  }
  // https://www.esp32.com/viewtopic.php?t=5398
  // https://remotemonitoringsystems.ca/time-zone-abbreviations.php
  setenv("TZ", "BRST+3BRDT+2,M10.3.0,M2.3.0", 1);
  tzset();  // a informação do timezone não sobrevive ao deep sleep
  int64_t t = xx_time_get_time();
  char buffer[100];
  printLocalTime();

  if (Serial) {
    sprintf(buffer, "%0ld", t/1000000L);
    Serial.print(buffer);  
    sprintf(buffer, "%0ld", t%1000000L);
    Serial.println(buffer);
  }
}

void ajustaRelogioBLE(int64_t agoraEmMillis) {
// https://portal.vidadesilicio.com.br/esp32-utilizando-o-rtc-interno-para-datas/
// Isto é um pedaço de código para quando eu implementar o ajuste de hora por BLE
// a parte do ajuste de timezone está em ajustaRelogioWiFi()
  timeval tv;//Cria a estrutura temporaria para funcao abaixo.
  //timezone tz = {-10800,0};  // menos 3 horas... não deu certo
  char buffer[100];

  if (Serial) {
    sprintf(buffer, "agoraEmMillis = %0ld", agoraEmMillis/1000000L);
    Serial.print(buffer);  
    sprintf(buffer, "%0ld", agoraEmMillis%1000000L);
    Serial.println(buffer);
  }

  /** o ajuste de fuso horário não funcionou, nem com tz, nem com setenv, foi na marra, descontando três horas. */
  tv.tv_sec = agoraEmMillis/1000LL-10800LL;//Atribui minha data atual. Voce pode usar o NTP para isso ou o site citado no artigo!
  tv.tv_usec = 0;
  //tv.tv_usec = (agoraEmMillis % 1000LL) * 1000LL; 
  settimeofday(&tv, NULL);//Configura o RTC para manter a data atribuida atualizada.
/** não deu certo
  // https://www.esp32.com/viewtopic.php?t=5398
  // https://remotemonitoringsystems.ca/time-zone-abbreviations.php
  setenv("TZ", "BRST+3BRDT+2,M10.3.0,M2.3.0", 1);
  tzset();  // a informação do timezone não sobrevive ao deep sleep
  */
}

#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>

BLEServer* pServer = NULL;
BLECharacteristic* pCharacteristic = NULL;
bool deviceConnected = false;
bool oldDeviceConnected = false;
uint8_t value = 0;

// See the following for generating UUIDs:
// https://www.uuidgenerator.net/

#define SERVICE_UUID_NOTIFY        "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define CHARACTERISTIC_UUID_NOTIFY "beb5483e-36e1-4688-b7f5-ea07361b26a8"

class MyServerCallbacks: public BLEServerCallbacks{

    void onConnect(BLEServer* pServer) {
      deviceConnected = true;
    };

    void onDisconnect(BLEServer* pServer) {
      deviceConnected = false;
    }
};

void setupBLENotifica() {
  //Serial.begin(115200);

  // Create the BLE Device
  BLEDevice::init("MyESP32");

  // Create the BLE Server
  pServer = BLEDevice::createServer();
  
  pServer->setCallbacks(new MyServerCallbacks());

  // Create the BLE Service
  BLEService *pService = pServer->createService(SERVICE_UUID_NOTIFY);

  // Create a BLE Characteristic
  pCharacteristic = pService->createCharacteristic(
                      CHARACTERISTIC_UUID_NOTIFY,
                      BLECharacteristic::PROPERTY_READ   |
                      BLECharacteristic::PROPERTY_WRITE  |
                      BLECharacteristic::PROPERTY_NOTIFY |
                      BLECharacteristic::PROPERTY_INDICATE
                    );

  // https://www.bluetooth.com/specifications/gatt/viewer?attributeXmlFile=org.bluetooth.descriptor.gatt.client_characteristic_configuration.xml
  // Create a BLE Descriptor
  pCharacteristic->addDescriptor(new BLE2902());
  // Start the service
  pService->start();
/*

  // Start advertising
  pServer->getAdvertising()->start();
  Serial.println("Waiting a client connection to notify...");
*/
}

touch_pad_t touchPin;
byte p=200;  // item a notificar

void loopBLENotifica() {
    delay (500);
    Serial.print ("deviceConnected=");
    Serial.print (deviceConnected);
    Serial.print (" oldDeviceConnected=");
    Serial.println (oldDeviceConnected);
    // notify changed value
    if (deviceConnected) {
        Serial.print (p);
        Serial.print (" ");
        pCharacteristic->setValue(&p, 1);  // value é um byte
        pCharacteristic->notify(); // este aqui é o método que avisa o envio.
        value++;
        //delay(500); // bluetooth stack will go into congestion, if too many packets are sent
    }
    // disconnecting
    if (!deviceConnected && oldDeviceConnected) {
        //delay(500); // give the bluetooth stack the chance to get things ready
        pServer->startAdvertising(); // restart advertising
        Serial.println("start advertising");
        oldDeviceConnected = deviceConnected;
    }
    // connecting
    if (deviceConnected && !oldDeviceConnected) {
        // do stuff here on connecting
        oldDeviceConnected = deviceConnected;
    }
}

String valor;
int aleatorio;
String alea = "2";

bool recebiResposta;  // V3

#define SERVICE_UUID_SR        "4fafc201-1fb5-459e-8fcc-c5c9c331914c"
#define CHARACTERISTIC_UUID_SR "beb5483e-36e1-4688-b7f5-ea07361b26a9"

/** o callback é assíncrono. não está no loop e não é bloqueado pelo delay.
 *  não sei (não chequei) se perturba a contagem de tempo do delay.
 */

class MyCallbacks: public BLECharacteristicCallbacks {
    void onWrite(BLECharacteristic *pCharacteristic) {
      std::string value = pCharacteristic->getValue();
      pCharacteristic->setValue(alea.c_str()); // Pone el numero aleatorio

      if (value.length() > 0) {
        int64_t agoraEmMillis=0LL;
        valor = "";
        for (int i = 0; i < value.length(); i++){
          // Serial.print(value[i]); // Presenta value.
          valor = valor + value[i];
          agoraEmMillis=(agoraEmMillis*10LL)+(int64_t)(value[i]-'0');
        }
        ajustaRelogioBLE(agoraEmMillis/10LL); // divide por causa do terminador de string

        Serial.println("*********");
        Serial.print("valor = ");
        Serial.println(valor); // Presenta valor.

        recebiResposta=true;
        estado=200;
      }
    }
};

void setupBLESR() {
  //Serial.begin(115200);

  //BLEDevice::init("MyESP32");
  //BLEServer *pServer = BLEDevice::createServer();
  BLEService *pService = pServer->createService(SERVICE_UUID_SR);
  BLECharacteristic *pCharacteristic = pService->createCharacteristic(
                                         CHARACTERISTIC_UUID_SR,
                                         BLECharacteristic::PROPERTY_READ |
                                         BLECharacteristic::PROPERTY_WRITE
                                       );

  pCharacteristic->setCallbacks(new MyCallbacks());
  pCharacteristic->setValue("Iniciado.");
  pService->start();

  BLEAdvertising *pAdvertising = pServer->getAdvertising();
  pAdvertising->start();
}

void loopBLESR() {
  // put your main code here, to run repeatedly:
  Serial.print("ultima palavra recebida = ");
  Serial.println(valor); // Presenta valor.
  aleatorio = random(1,10000); // Crea el numero aleatorio.
  alea = (String) aleatorio; // Lo convierte en String.
  Serial.print("alea atual = ");
  Serial.println(alea); // Presenta valor.
}

#include "SSD1306Wire.h" // legacy include: `#include "SSD1306.h"`

// Include custom images
#include "images.h"
#include "roboto3.h" // roboto 48

#define D3 4  // no ttgo com display em cima do esp
#define D5 15

// Initialize the OLED display using Wire library
SSD1306Wire  display(0x3c, D3, D5);

int demoMode = 0;
int counter = 1;

byte hora=0, minuto=0, segundo=0, ano=0, mes=0, dia=0, dsemana=0;

String strHM () {
  String r="";
  r.concat(hora);
  r.concat(":");
  if (minuto<10) r.concat("0");
  r.concat(minuto);
  return r;
}

String strHMS () {
  String r="";
  r.concat(hora);
  r.concat(":");
  if (minuto<10) r.concat("0");
  r.concat(minuto);
  r.concat(":");
  if (segundo<10) r.concat("0");
  r.concat(segundo);
  return r;
}

String strData () {
  String sem[]={"dom ", "seg ", "ter ", "qua ", "qui ", "sex ", "sab "};
  String r=sem[dsemana];
  r.concat(dia);
  r.concat("/");
  if (mes<10) r.concat("0");
  r.concat(mes+1);  // ajusta indice do array para data convencional
  r.concat("/");
  if (ano<10) r.concat("0");
  r.concat(ano);
  return r;
}

void setupOLED() {
  //Serial.begin(115200);

  // Initialising the UI will init the display too.
  pinMode (16, OUTPUT); // no ttgo com display em cima do esp, o reset do display (active low) é conectado ao pino 16
  digitalWrite (16, HIGH); // reset tem que estar desativado para o display mostrar algo.
  display.init();

  display.flipScreenVertically();
}

void mostraHoraOLED() {
  getSystemDT();
  // clear the display
  display.clear();
    //display.setFont(Roboto_Black_Italic_32);
    //tem um espação emcima e embaixo do número em roboto48
    display.setFont(ArialMT_Plain_10);
    display.setTextAlignment(TEXT_ALIGN_LEFT);
    display.drawStringMaxWidth(0, 0, 128,
      "wWwWmMmMgG" );
    display.setFont(Roboto_Black_Italic_48);
    display.setTextAlignment(TEXT_ALIGN_LEFT);
    display.drawStringMaxWidth(0, 0, 128,
      strHM() );
    display.setFont(ArialMT_Plain_16);
    display.setTextAlignment(TEXT_ALIGN_LEFT);
    display.drawStringMaxWidth(0, 45, 128,
      strData() );
    display.display();
    Serial.print ("mostraHoraOLED: ");
    Serial.println (strHMS());
  
}

// Exemplo que veio com a biblioteca concatenado com xx_time... de https://esp32.com/viewtopic.php?t=5288 e print de https://forum.arduino.cc/index.php?topic=58697.0 
// 24.07.2020 - Imprime a data corretamente e aparentemente o tempo em millis também.



void getSystemDT () {

  /* Ajustado para ligar no código do NTP */
  /* Movido para cá para pegar a declaração de struct tm */
  
  struct tm timeinfo; // http://www.cplusplus.com/reference/ctime/tm/
  /** com NTP
  // https://randomnerdtutorials.com/esp32-date-time-ntp-client-server-arduino/
  if(!getLocalTime(&timeinfo)){ // acho que só funciona com NTP conectado.
    Serial.println("Failed to obtain time");
    return;
  }
  */
  /** com BLE : https://portal.vidadesilicio.com.br/esp32-utilizando-o-rtc-interno-para-datas/ */
  time_t tt = time (NULL);
  timeinfo = *gmtime(&tt);

  int64_t t = tt; // xx_time_get_time();
  char buffer[100];

  if (Serial) {
    sprintf(buffer, "%0ld", t/1000000L);
    Serial.print(buffer);  
    sprintf(buffer, "%0ld", t%1000000L);
    Serial.println(buffer);
  }
  
  
  /***********/
  
  dia=timeinfo.tm_mday;
  mes=timeinfo.tm_mon;
  ano=timeinfo.tm_year % 100;
  hora=timeinfo.tm_hour;
  minuto=timeinfo.tm_min;
  segundo=timeinfo.tm_sec;
  dsemana=timeinfo.tm_wday;
}


void printLocalTime()
{
  struct tm timeinfo;
  if (Serial) {
    if(!getLocalTime(&timeinfo)){
      Serial.println("Failed to obtain time");
      return;
    }
    Serial.println(&timeinfo, "%A, %B %d %Y %H:%M:%S");
  }
}

int64_t xx_time_get_time() {
  struct timeval tv;
  gettimeofday(&tv, NULL);
  return (tv.tv_sec * 1000LL + (tv.tv_usec / 1000LL)); //milissegundos
}

/*
Deep Sleep with Touch Wake Up
=====================================
This code displays how to use deep sleep with
a touch as a wake up source and how to store data in
RTC memory to use it over reboots

This code is under Public Domain License.

Author:
Pranav Cherukupalli <cherukupallip@gmail.com>

Quando retorna do deep sleep ele executa o setup.

*/

RTC_DATA_ATTR int bootCount = 0;  // variável armazenada na memória do RTC

/*
Method to print the reason by which ESP32
has been awaken from sleep
*/
void print_wakeup_reason(){
  esp_sleep_wakeup_cause_t wakeup_reason;

  wakeup_reason = esp_sleep_get_wakeup_cause();

  if (Serial) {
    switch(wakeup_reason)
    {
      case ESP_SLEEP_WAKEUP_EXT0 : Serial.println("Wakeup caused by external signal using RTC_IO"); break;
      case ESP_SLEEP_WAKEUP_EXT1 : Serial.println("Wakeup caused by external signal using RTC_CNTL"); break;
      case ESP_SLEEP_WAKEUP_TIMER : Serial.println("Wakeup caused by timer"); break;
      case ESP_SLEEP_WAKEUP_TOUCHPAD : Serial.println("Wakeup caused by touchpad"); break;
      case ESP_SLEEP_WAKEUP_ULP : Serial.println("Wakeup caused by ULP program"); break;
      default : Serial.printf("Wakeup was not caused by deep sleep: %d\n",wakeup_reason); break;
    }
  }
}

/*
Method to print the touchpad by which ESP32
has been awaken from sleep
*/
void print_wakeup_touchpad(){
  touchPin = esp_sleep_get_touchpad_wakeup_status();
  if (Serial) {
    switch(touchPin)
    {
      case 0  : Serial.println("Touch detected on GPIO 4"); break;
      case 1  : Serial.println("Touch detected on GPIO 0"); break;
      case 2  : Serial.println("Touch detected on GPIO 2"); break;
      case 3  : Serial.println("Touch detected on GPIO 15"); break;
      case 4  : Serial.println("Touch detected on GPIO 13"); break;
      case 5  : Serial.println("Touch detected on GPIO 12"); break;
      case 6  : Serial.println("Touch detected on GPIO 14"); break;
      case 7  : Serial.println("Touch detected on GPIO 27"); break;
      case 8  : Serial.println("Touch detected on GPIO 33"); break;
      case 9  : Serial.println("Touch detected on GPIO 32"); break;
      default : Serial.println("Wakeup not by touchpad"); break;
    }
  }
}

// https://github.com/espressif/arduino-esp32/issues/855
// o post é de 2017, talvez não precise da macro IRAM_ATTR

/*o ESP32 parece permitir interrupção dentro de interrupção e não encontrei como 
 * desabilitar interrupções. A solução foi criar um flag que é consultado dentro
 * da rotina de atendimento de interrupção. Se for true, então é interrupção de 
 * interrupção, aí não faz nada, se for false então atende a interrupção, 
 * incrementando/decrementando o estado.
 * o flag é resetado quando retorna para o loop e mostra a tela correspondente ao
 * estado.
 * Deste jeito evito de avançar ou retroceder muito rápido nos ítens do menu, que
 * é o problema que eu queria resolver.
 */
bool atendendoINT = false;

void IRAM_ATTR callback(){
  //placeholder callback function
}

void IRAM_ATTR callback5(){
  // touch de UP
  if (!atendendoINT) {
    atendendoINT=true;
    if (estado==300) {
      // modo interativo
      estado=10;   // primeira atividade que não está nos atalhos...
    } else if (estado<16) {
        estado++;
    }
    // mostraMenu(estado);
    // lastInteractionInstant=millis();
    Serial.print ("callback5 estado=");
    Serial.println (estado);
  }
}

void IRAM_ATTR callback4(){
  // touch de DOWN
  if (!atendendoINT) {
    atendendoINT=true;
    if (estado==300) {
      // modo interativo
      estado=10;
    } else if (estado>0) {
      estado--;
    }
  //  mostraMenu(estado);
  //  lastInteractionInstant=millis();
    Serial.print ("callback4 estado=");
    Serial.println (estado);
  }
}

void IRAM_ATTR callback6(){
  // touch de UP
  if (!atendendoINT) {
    atendendoINT=true;
//    if (estado==300) {
      // modo interativo
      estado=6;   // primeira atividade que não está nos atalhos...
//    }
    // mostraMenu(estado);
    // lastInteractionInstant=millis();
    Serial.print ("callback6 estado=");
    Serial.println (estado);
  }
}

void IRAM_ATTR callback7(){
  // touch de DOWN
  if (!atendendoINT) {
    atendendoINT=true;
//    if (estado==300) {
      // modo interativo
      estado=7;
//    }
  //  mostraMenu(estado);
  //  lastInteractionInstant=millis();
    Serial.print ("callback7 estado=");
    Serial.println (estado);
  }
}

void IRAM_ATTR callback8(){
  // touch de UP
  if (!atendendoINT) {
    atendendoINT=true;
//    if (estado==300) {
      // modo interativo
      estado=8;   // primeira atividade que não está nos atalhos...
//    }
    // mostraMenu(estado);
    // lastInteractionInstant=millis();
    Serial.print ("callback8 estado=");
    Serial.println (estado);
  }
}

void IRAM_ATTR callback9(){
  // touch de DOWN
  if (!atendendoINT) {
    atendendoINT=true;
//    if (estado==300) {
      // modo interativo
      estado=9;
//    }
  //  mostraMenu(estado);
  //  lastInteractionInstant=millis();
    Serial.print ("callback9 estado=");
    Serial.println (estado);
  }
}


void IRAM_ATTR callback2() {
  if (!atendendoINT) {
    atendendoINT=true;

    if ((estado>=0) && (estado<17)) {
      p=estado;
      estado=500;
    }
  //  lastInteractionInstant=millis();
  //  Serial.print ("callback2 p=");
  //  Serial.println (p);
  }
}

void loopWakeUp() {
  //Print the wakeup reason for ESP32 and touchpad too
  print_wakeup_reason();
  print_wakeup_touchpad();
}

void loopTouch() {
  //Setup interrupt on Touch Pad 8 (GPIO32) - no ttgo com display em cima do ESP32 o T3 está travado no valor 1 então acorda sempre. por isso mudei para T8 que é GPIO32 aí funcionou como esperado.
  touchAttachInterrupt(T8, callback8, 40);
  touchAttachInterrupt(T9, callback9, 40);
  // troquei de 20 para 40 porque conectado ao computador pela USB 20 é sensível o suficiente para disparar ao toque, mas desconectado fica muito insensível. Este valor é meio limite pois conectado o valor sem touch é 43.

  touchAttachInterrupt(T4, callback4, 100);
  touchAttachInterrupt(T5, callback5, 100);
  touchAttachInterrupt(T6, callback6, 105);
  touchAttachInterrupt(T7, callback7, 105);

  touchAttachInterrupt(T2, callback2, 75);
  // troquei de 80 para 75 porque nos dias 19 e 20 de agosto de 2020 (dias nublados, dia 20 com chuva) saía do deep sleep para mostrar hora sem que eu tocasse no touch)
}

void loopInterativo() {
  //Setup interrupt on Touch Pad 8 (GPIO32) - no ttgo com display em cima do ESP32 o T3 está travado no valor 1 então acorda sempre. por isso mudei para T8 que é GPIO32 aí funcionou como esperado.

  touchAttachInterrupt(T4, callback4, 100);
  touchAttachInterrupt(T5, callback5, 100);

  touchAttachInterrupt(T2, callback2, 80);
}

void loopSleep() {
  //Configure Touchpad as wakeup source
  esp_sleep_enable_touchpad_wakeup();

  //Go to sleep now
  if (Serial) Serial.println("Going to sleep now");
  esp_deep_sleep_start();
  if (Serial) Serial.println("This will never be printed");
  
}

void loopBootCount()
{
if (Serial) {
    //Increment boot number and print it every reboot
    ++bootCount;
    Serial.println("Boot number: " + String(bootCount));
  }
}

String atividadesAtalho[] {
"caminha",
"transporte",
"esper/infor",
"pausa",
"atender",
"msg trab"
};

String atividadesMenu[] {
"caminhada (para algum lugar)",
"transpo: ônibus/metrô/carro",
"esperar/informar-se",
"pausa: relaxamento/refeição",
"atendimento/reunião/aula",
"mensagem de trabalho",
"estudo/elaboração/planejamento",
"bem estar/passeio",
"cozinhar/cuidar da casa",
"construir hardware/software",
"organizar informação em arquivos",
"organizar a mente",
"organizar um local",
"lojas/compras com presença física",
"mensagem particular",
"outra atividade/demonstração",
"término"
};

void mostraMenu(int item) {
  display.clear();
  display.setFont(ArialMT_Plain_10);
  display.setTextAlignment(TEXT_ALIGN_LEFT);
  if (item>0) {
    if (atividadesMenu[item-1].length()<18) {
    display.drawStringMaxWidth(0, 0, 128,
      atividadesMenu[item-1]);
    } else {
    display.drawStringMaxWidth(0, 0, 128,
      atividadesMenu[item-1].substring(0,17) );
    }
  }
  if (item<16) {
    if (atividadesMenu[item-1].length()<18) {
    display.drawStringMaxWidth(0, 0, 128,
      atividadesMenu[item-1]);
    } else {
    display.drawStringMaxWidth(0, 52, 128,
      atividadesMenu[item+1].substring(0,17) );
    }
  }
    display.setFont(ArialMT_Plain_16);
    display.setTextAlignment(TEXT_ALIGN_LEFT);
    display.drawStringMaxWidth(0, 16, 128,
      atividadesMenu[item] ); //44 digitos em tamanho 16
  display.display();
}

void mostraAtalho(int item) {
  display.clear();
//  display.setFont(ArialMT_Plain_16);
//  display.setTextAlignment(TEXT_ALIGN_LEFT);
//  if (item>0) {
//    display.drawStringMaxWidth(0, 0, 128,
//      atividadesAtalho[item-1] ); //? digitos em tamanho 24
//  }
//  if (item<5) {
//    display.drawStringMaxWidth(0, 40, 128,
//      atividadesAtalho[item+1] ); //? digitos em tamanho 24
//      
//  }
    display.setFont(ArialMT_Plain_24);
    display.drawStringMaxWidth(0, 16, 128,
      atividadesAtalho[item] ); //? digitos em tamanho 24
  
  
  display.display();
  Serial.println (atividadesAtalho[item]);
}

void mostraOK() {
  // clear the display
  display.clear();
    //display.setFont(Roboto_Black_Italic_32);
    //tem um espação emcima e embaixo do número em roboto48
    display.setFont(ArialMT_Plain_10);
    display.setTextAlignment(TEXT_ALIGN_LEFT);
    display.drawStringMaxWidth(0, 0, 128,
      "wWwWmMmMgG" );
    display.setFont(Roboto_Black_Italic_48);
    display.setTextAlignment(TEXT_ALIGN_LEFT);
    display.drawStringMaxWidth(30, 0, 128,
      "OK" );
    display.setFont(ArialMT_Plain_16);
    display.setTextAlignment(TEXT_ALIGN_LEFT);
    display.drawStringMaxWidth(0, 45, 128,
      "comunicando..." );
    display.display();
    Serial.print ("mostraOK");
}

void mostraACK() {
  // clear the display
  display.clear();
    //display.setFont(Roboto_Black_Italic_32);
    //tem um espação emcima e embaixo do número em roboto48
    display.setFont(ArialMT_Plain_10);
    display.setTextAlignment(TEXT_ALIGN_LEFT);
    display.drawStringMaxWidth(0, 0, 128,
      "wWwWmMmMgG" );
    display.setFont(ArialMT_Plain_24);
    display.setTextAlignment(TEXT_ALIGN_LEFT);
    display.drawStringMaxWidth(20, 15, 128,
      "ACK" );
    display.setFont(ArialMT_Plain_16);
    display.setTextAlignment(TEXT_ALIGN_LEFT);
    display.drawStringMaxWidth(0, 45, 128,
      strData() );
    display.display();
    Serial.print ("mostraACK");
}

void mostraNACK() {
  // clear the display
  display.clear();
    //display.setFont(Roboto_Black_Italic_32);
    //tem um espação emcima e embaixo do número em roboto48
    display.setFont(ArialMT_Plain_10);
    display.setTextAlignment(TEXT_ALIGN_LEFT);
    display.drawStringMaxWidth(0, 0, 128,
      "wWwWmMmMgG" );
    display.setFont(ArialMT_Plain_24);
    display.setTextAlignment(TEXT_ALIGN_LEFT);
    display.drawStringMaxWidth(20, 15, 128,
      "NACK" ); // roboto 48 black italic parece que não tem N
    display.setFont(ArialMT_Plain_16);
    display.setTextAlignment(TEXT_ALIGN_LEFT);
    display.drawStringMaxWidth(0, 45, 128,
      strData() );
    display.display();
    Serial.print ("mostraNACK");
}

void mostraCancelado() {
  display.clear();
    display.setFont(ArialMT_Plain_24);
    display.setTextAlignment(TEXT_ALIGN_LEFT);
    display.drawStringMaxWidth(0, 16, 128,
      "Timeout"); //44 digitos em tamanho 16
    display.setFont(ArialMT_Plain_16);
    display.setTextAlignment(TEXT_ALIGN_LEFT);
    display.drawStringMaxWidth(0, 45, 128,
      "comunicando..." );
  display.display();
}

/** A parte relacionada a NTP está no exemplo SimpleTime. 
 *  O programa não tem mensagem de copyright.
 *  */

void setup () {
  Serial.begin(115200);
  setupBLENotifica();
  setupBLESR();
  //ajustaRelogioWiFi();  // relógio ajustado em onWrite, com millis vindo do BLE.
  setupOLED();
}

void loop () {
  loopWakeUp();
  loopBootCount();
  /*Não interativo - atalhos */
    switch(touchPin) // acões de wakeup, atende teclas de atalho
    {
      //case 0  : Serial.println("Touch detected on GPIO 4"); break;
      case 1  : Serial.println("Touch detected on GPIO 0"); break; // botão
      //case 3  : Serial.println("Touch detected on GPIO 15"); break;
      case 4  : 
      case 5  : 
      case 6  : 
      case 7  : 
      case 8  : 
      case 9  : estado=touchPin-4; p=estado; mostraAtalho(estado); break;
      case 2  :  //touch2
      default : 
        estado=300; 
        mostraHoraOLED();
        /*Interativo, estado==300*/
        lastInteractionInstant=millis();
//        loopInterativo(); // registra callbacks de interação: acima, abaixo e ok.
        loopTouch(); // registra callbacks de interação: acima, abaixo e ok; e callbacks de atalho secundario.
        int estadoAnterior=estado;
        while ((estado!=500)&&((millis()-lastInteractionInstant)<5000)) {
          Serial.println ("estados de interação");
          /* Depende de interrupções, mas o refresh de tela precisa 
             ser feito fora do callback de interrupção para evitar o 'guru meditation error'.
           */
           if ((estado!=estadoAnterior)&&(estado!=300)) {
             estadoAnterior=estado;
             mostraMenu(estado);
             lastInteractionInstant=millis();
      
           }
           atendendoINT=false;
           delay(300); // intervalo entre toques e mudança de tela.
                       // se for muito pequeno, os ítens do menu
                       // são trocados muito rápido.
        }
    }
    if (estado==500) mostraOK();  // interativo com OK
    else if ((estado>5)&&(estado!=300)) mostraCancelado(); // não foi um atalho nem ver hora sem interação
  /* Comunica */
  recebiResposta=false;
  for (int i=0;i<60 && !recebiResposta;i++) {
    loopBLENotifica();
    loopBLESR();
  }
  if (recebiResposta) {
    mostraACK();
  } else {
    mostraNACK();
  }
  delay (2000);   // incluído para deixar o rádio BLE ligado. Se o handshake ocorrer nas últimas voltas do loop. 
                  // Sem este delay, o ESP desliga o rádio antes de terminar a comunicação, o que causa erro de
                  // conexão no app BLE-protocolo
                  
   //delay(30000); // Nos métodos do BLE me parece tudo assíncrono então dar 30s com um delay não vai bloquear a operação do BLE. Vou usar o BLEfromScratchV3 para conectar e receber notificações. Este será o primeiro teste...
                 // consegui conectar, mas o celular não recebeu nenhuma notificação. Quando o ESP foi para deep sleep o celular deu falha ao conectar, connection status was set to OS code 8. Quando o ESP é acordado com o touch não acontece reconexão automática.
                 // mas ele aceita reconexão manual (ié o erro não tem impacto sobre uma conexão futura).  
                 // O código do BLE pressupõe que ele esteja em uma repetição e à medida que os estados se sucedem as ações vão mudando. Por isso vou comentar este delay e acrescentar um loop for fora de loopBLE.
                 // agora as notificações chegaram - de 7 a 42.
                 // acordando do deep sleep com o touch e reconectando manualmente no celular as notificações 
                 // de 7 a 55 chegaram.
   loopTouch();
   loopSleep();  // põe em deep sleep, acordado por touch.
 }

