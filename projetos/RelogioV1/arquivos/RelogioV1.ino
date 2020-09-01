/**
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
 * 
 * 
 * 
 *
 */

// Include the correct display library
// For a connection via I2C using Wire include
//#include <Wire.h>  // Only needed for Arduino 1.6.5 and earlier
#include "SSD1306Wire.h" // legacy include: `#include "SSD1306.h"`
// or #include "SH1106Wire.h", legacy include: `#include "SH1106.h"`
// For a connection via I2C using brzo_i2c (must be installed) include
// #include <brzo_i2c.h> // Only needed for Arduino 1.6.5 and earlier
// #include "SSD1306Brzo.h"
// #include "SH1106Brzo.h"
// For a connection via SPI include
// #include <SPI.h> // Only needed for Arduino 1.6.5 and earlier
// #include "SSD1306Spi.h"
// #include "SH1106SPi.h"

// Include custom images
#include "images.h"
#include "roboto3.h" // roboto 48

// Initialize the OLED display using SPI
// D5 -> CLK
// D7 -> MOSI (DOUT)
// D0 -> RES
// D2 -> DC
// D8 -> CS
// SSD1306Spi        display(D0, D2, D8);
// or
// SH1106Spi         display(D0, D2);

// Initialize the OLED display using brzo_i2c
// D3 -> SDA
// D5 -> SCL
// SSD1306Brzo display(0x3c, D3, D5);
// or
// SH1106Brzo  display(0x3c, D3, D5);

//FN 
//#define D3 21
//#define D5 22
//#define D3 5  // no wemos e no ttgo com bateria de lanterna tática
//#define D5 4

#define D3 4  // no ttgo com display em cima do esp
#define D5 15

// Initialize the OLED display using Wire library
SSD1306Wire  display(0x3c, D3, D5);
// SH1106 display(0x3c, D3, D5);


#define DEMO_DURATION 3000
typedef void (*Demo)(void);

int demoMode = 0;
int counter = 1;

byte hora=0, minuto=0, segundo=0, ano=0, mes=0, dia=0;  // data registrada
long tcurr;  // data registrada em milissegundos;

void getSystemDT () {
  String meses[]={"Jan","Feb","Mar","Apr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dec"};
  String sd, st;
  tcurr=millis();
  sd=__DATE__;
  st=__TIME__;
  Serial.println (sd);
  Serial.println (st);
  String buf=sd.substring(0,3); // [ini,fim[: o índice do final é exclusivo.
  Serial.println (buf);
  for (int i=0;i<12;i++) {
    if (meses[i].equalsIgnoreCase(buf)) mes=i;
  }
  
  
  dia=sd.substring(4,6).toInt();
  ano=sd.substring(9,11).toInt(); // o 11 pode estar fora da string se não tiver/contar o '\0' do final mas isto é consequencia de ser exclusivo...

  hora=st.substring(0,2).toInt();
  minuto=st.substring(3,5).toInt();
  segundo=st.substring(6,8).toInt();
}

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
  String r="";
  r.concat(dia);
  r.concat("/");
  if (mes<10) r.concat("0");
  r.concat(mes+1);  // ajusta indice do array para data convencional
  r.concat("/");
  if (ano<10) r.concat("0");
  r.concat(ano);
  return r;
}

void atualizaHora () {
  byte diasNoMes[]={31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 30}; // falha nos bissextos.
  long tnow=millis();
  long dt=tnow-tcurr;
  dt/=1000; // segundos
  segundo+=dt%60;
  if (segundo>=60) {
    segundo-=60;
    minuto++;
  }
  dt/=60; // minutos
  minuto+=dt%60;
  if (minuto>=60) {
    minuto-=60;
    hora++;
  }
  dt/=60; // horas
  hora+=dt%24;
  if (hora>24) {
    hora-=24;
    dia++;
  }
  dt/=24; // dias;
  dia+=dt; // resolve na propagação.
  while (dia>diasNoMes[mes]) {
    dia-=diasNoMes[mes];
    mes++;
    if (mes>11){
      ano++;
      mes=0;
    }
  }
  tcurr=tnow;
}

int iShow=0;
int threshold=20;

void gotTouch() {
  iShow=0;
}

void setup() {
  Serial.begin(115200);
  getSystemDT();
  Serial.println(strHMS());
  Serial.println(strData());

  // Initialising the UI will init the display too.
  pinMode (16, OUTPUT); // no ttgo com display em cima do esp, o reset do display (active low) é conectado ao pino 16
  digitalWrite (16, HIGH); // reset tem que estar desativado para o display mostrar algo.
  display.init();

  display.flipScreenVertically();
  touchAttachInterrupt (T8, gotTouch, threshold);
}

void drawTextFlowDemo() {
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
}



void loop() {
  if (iShow==0) {
    atualizaHora();
    // draw the current demo method
    drawTextFlowDemo();

    Serial.println (strData());
    Serial.println (strHMS());
  }
  if (iShow==10) {
    // apaga o display
    display.clear();
    display.display();
  }
  iShow++; //quando vira o inteiro acende um pouco...
  //Serial.println (iShow);
  //Serial.println (touchRead(T8));
  delay (1000);
}
