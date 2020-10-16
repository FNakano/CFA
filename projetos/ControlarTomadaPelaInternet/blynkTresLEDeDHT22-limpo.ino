/*************************************************************
  Download latest Blynk library here:
    https://github.com/blynkkk/blynk-library/releases/latest

  Blynk is a platform with iOS and Android apps to control
  Arduino, Raspberry Pi and the likes over the Internet.
  You can easily build graphic interfaces for all your
  projects by simply dragging and dropping widgets.

    Downloads, docs, tutorials: http://www.blynk.cc
    Sketch generator:           http://examples.blynk.cc
    Blynk community:            http://community.blynk.cc
    Follow us:                  http://www.fb.com/blynkapp
                                http://twitter.com/blynk_app

  Blynk library is licensed under MIT license
  This example code is in public domain.

 *************************************************************

  Blynk using a LED widget on your phone!

  App project setup:
    LED widget on V1
 *************************************************************/
/* 2020-10-13: Adaptação do exemplo do blink widget para o 
 * controlador de tomada. Dados de acesso limpos para
 * privacidade. */

/* Comment this out to disable prints and save space */
#define BLYNK_PRINT Serial

#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>
#include <DHTesp.h>   // beegeetokyo

DHTesp dht;

// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";

// curl -X GET -i 'http://blynk-cloud.com/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/get/v0'

// Your WiFi credentials.
// Set password to "" for open networks.
char ssid[] = "REDE-";   // coloque o nome da sua rede aqui
char pass[] = "SENHASENHASENH";  // coloque a senha da sua rede aqui

BlynkTimer timer;

// This function sends Arduino's up time every second to Virtual Pin (5).
// In the app, Widget's reading frequency should be set to PUSH. This means
// that you define how often to send data to Blynk App.
void sendSensor()
{
  float h = dht.getHumidity();
  float t = dht.getTemperature(); // or dht.readTemperature(true) for Fahrenheit

  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  // You can send any value at any time.
  // Please don't send more that 10 values per second.
  Blynk.virtualWrite(V5, h);
  Blynk.virtualWrite(V6, t);
}

void vivo() {
  Serial.println ("Estou vivo");
  // desconfio que sem o timer, não há atualização dos dados quando um cliente (telefone celular) não está conectado.
  // criei esta função apenas para ter algo para o timer executar. NAO DEU CERTO - INTERROMPE COMUNICAÇÃO DO MESMO JEITO.
  // vou usar um pino virtual...
  Blynk.virtualWrite (V1, analogRead(A0));
  sendSensor();
}
void setup()
{
  // Debug console
  Serial.begin(115200);

  Blynk.begin(auth, ssid, pass);
  dht.setup(5, DHTesp::DHT22); // Connect DHT sensor to GPIO 5

  timer.setInterval(1000L, vivo);

}

void loop()
{
  Blynk.run();
  timer.run();
}
