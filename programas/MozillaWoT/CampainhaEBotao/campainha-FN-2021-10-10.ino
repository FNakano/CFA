/**
 * Simple server compliant with Mozilla's proposed WoT API
 * Originally based on the HelloServer example
 * Tested on ESP8266, ESP32, Arduino boards with WINC1500 modules (shields or
 * MKR1000)
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

#define LARGE_JSON_BUFFERS 1

#include <Arduino.h>
#include <Thing.h>
#include <WebThingAdapter.h>

#ifdef ESP32
#include <analogWrite.h>
#endif

const char *ssid = "NameOfNetworkTP";
const char *password = "0123456789";

const int campainhaPin = 12; 

ThingActionObject *action_generator(DynamicJsonDocument *);

WebThingAdapter *adapter;

const char *plugTypes[] = {"OnOffSwitch", "campainha", nullptr};
ThingDevice plug("urn:dev:ops:my-campainha", "campainha", plugTypes);

ThingProperty plugOn("on", "Whether campainha is turned on", BOOLEAN,
                     "OnOffProperty");

bool lastOn = true;

void setup(void) {
  pinMode(campainhaPin, OUTPUT);
  //digitalWrite(lampPin, HIGH);
  Serial.begin(115200);
  Serial.println("");
  Serial.print("Connecting to \"");
  Serial.print(ssid);
  Serial.println("\"");
#if defined(ESP8266) || defined(ESP32)
  WiFi.mode(WIFI_STA);
#endif
  WiFi.begin(ssid, password);
  Serial.println("");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  adapter = new WebThingAdapter("campainha", WiFi.localIP());

  plug.description = "campainha";

  plugOn.title = "On/Off";
  plug.addProperty(&plugOn);


  adapter->addDevice(&plug);
  adapter->begin();

  Serial.println("HTTP server started");
  Serial.print("http://");
  Serial.print(WiFi.localIP());
  Serial.print("/things/");
  Serial.println(plug.id);

#ifdef analogWriteRange
  analogWriteRange(255);
#endif

  // set initial values
  ThingPropertyValue initialOn = {.boolean = true};
  plugOn.setValue(initialOn);
  (void)plugOn.changedValueOrNull();

  randomSeed(analogRead(0));
}

void loop(void) {
  adapter->update();
  bool on1 = plugOn.getValue().boolean;
  if (on1) {
    digitalWrite(campainhaPin, HIGH);
  } else {
    digitalWrite(campainhaPin, LOW);
  }
}
