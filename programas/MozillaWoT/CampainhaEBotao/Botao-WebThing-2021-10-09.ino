#define LARGE_JSON_BUFFERS 1

#include <Arduino.h>
#include <ESPDateTime.h>
#include <Thing.h>
#include <WebThingAdapter.h>

char *ssid="NameOfNetworkTP";
char *password="0123456789";


const uint8_t buttonPin = 4;

WebThingAdapter *adapter;
//https://webthings.io/schemas/#PushButton
const char *remoteTypes[] = {"PushButton", nullptr};
ThingDevice remote("urn:dev:ops:mypushbutton", "Push Button I", remoteTypes);

ThingEvent pressed("pressed",
                   "PressedEvent",
                   BOOLEAN, "PressedEvent");

ThingProperty button("button", "PushButton", BOOLEAN, "PushedProperty");

int ledAzul=13;
int ledVermelho=15;

void setup(void)
{
  pinMode(buttonPin, INPUT);
  pinMode(ledVermelho, OUTPUT);
  pinMode(ledAzul, OUTPUT);
  
  Serial.begin(115200);
  Serial.setDebugOutput(true);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  Serial.println("");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    digitalWrite(ledVermelho, HIGH); // ACENDE LED VERMELHO ENQUANTO ESTIVER PROCURANDO REDE
  }
  digitalWrite(ledVermelho, LOW); // APAGA LED VERMELHO

  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  adapter = new WebThingAdapter("push-button", WiFi.localIP());

  remote.description = "A Webthings PushButton";

  button.title = "PushButton";

  remote.addProperty(&button);
  remote.addEvent(&pressed);
  adapter->addDevice(&remote);
  adapter->begin();

  Serial.println("HTTP server started");
  Serial.print("http://");
  Serial.print(WiFi.localIP());
  Serial.print("/things/");
  Serial.println(remote.id);

  randomSeed(analogRead(0));

  DateTime.begin();
  if (!DateTime.isTimeValid()) {
    Serial.println("Failed to get time from server.");
  }
}

unsigned long oldMillis = 0;
bool lastTest = false;
void loop(void)
{
  if (digitalRead(4)==LOW) {
    // botão apertado
    digitalWrite(ledAzul, HIGH);
    if (lastTest == false) {
      // mudança de estado de não apertado para apertado
      lastTest=true;
      if (!DateTime.isTimeValid()) {
        Serial.println("Failed to get time from server, retry.");
        DateTime.begin();
      } else {
        // Serial.println("Force Event!");
        oldMillis = millis();
        
        button.setValue({.boolean = lastTest});
        
        ThingEventObject *ev = new ThingEventObject(
          "pressed",
          BOOLEAN,
          {.boolean = true},
          DateTime.formatUTC(DateFormatter::ISO8601)
        );
        remote.queueEventObject(ev);
    
        Serial.println("Mudou para pressionado.");
      }
    }
  } else {
    // botão solto
    digitalWrite(ledAzul, LOW);
    if (lastTest == true) {
      // mudança de estado de apertado para não apertado
      lastTest=false;
      if (!DateTime.isTimeValid()) {
        Serial.println("Failed to get time from server, retry.");
        DateTime.begin();
      } else {
        // Serial.println("Force Event!");
        oldMillis = millis();
    
        button.setValue({.boolean = lastTest});
        
        ThingEventObject *ev = new ThingEventObject(
          "pressed",
          BOOLEAN,
          {.boolean = true},
          DateTime.formatUTC(DateFormatter::ISO8601)
        );
        remote.queueEventObject(ev);
    
        Serial.println("Mudou para solto");
      }
    }
  }
  
  adapter->update();
}
