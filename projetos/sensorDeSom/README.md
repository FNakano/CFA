# Esboço de documentação sobre construção de um "sensor de som".

![Som](Som2022-10-11.png)

## Motivação

Apresentar uma alternativa para os sensores de som mais comuns para Arduino (e que são difíceis de trabalhar).

Figura 2: Sensor proposto neste projeto. Sua montagem e uso serão detalhados a seguir.

![montagem](fisico.jpeg)

Os sensores de som para arduino mais comuns, como o desta foto do site da eletrogate: 

![Sensor de som](https://blog.eletrogate.com/wp-content/webpc-passthru.php?src=https://blog.eletrogate.com/wp-content/uploads/2020/07/detalhamento-sensor-de-som.png), segundo 

https://oshwlab.com/adrirobot/KY_038_Microphone_sound_sensor_module-283a631354c24d129bca349e77da0d18, tem este circuito: 

![Schematics](https://image.easyeda.com/histories/1d9fba31b4c049af8964b4b309c44646.png).

O circuito usa os amplificadores sem realimentação e com o microfone acoplado em DC (sem capacitor de desacoplamento), o que o faz muito sensível (provavelmente, inclusive a mudanças de temperatura) e, na minha opinião, difícil de calibrar e trabalhar.

Por outro lado, há demanda por sensores de som, baratos, para Arduino, e preferencialmente que permitam medidas proporcionais, comparáveis entre si, ainda que um pouco distorcidas.

Ligar diretamente um microfone de computador a uma entrada analógica do arduino, até funciona, mas a variação do valor lido na entrada analógica é muito pequena (para alguma aplicação, isso pode ser suficiente).

O seguinte circuito capta som e gera sinais com amplitude maior. Talvez seja um "sensor de som" mais adequado.

## Montagem

### Lista de peças

| Quantidade | Código | orientação adicional |
| --- | --- | --- |
| 1 | Transistor BC548 | --- |
| 1 | Resistor 2,7MOhm | verm-lilas-verde |
| 1 | Resistor 10kOhm | marrom-preto-laranja |
| 1 | Resistor 2,2kOhm | vermelho-vermelho-vermelho |
| 1 | Resistor 100Ohm | marrom-preto-marrom |
| 1 | Capacitor cerâmico, poliéster ou outro não eletrolítico, de 330nF | --- |
| --- | Jumpers | --- |
| --- | Protoboard | para facilitar a conexão dos componentes |

### Ferramentas

Arduino UNO e IDE do Arduino

### Programa

O exemplo sobre entrada analógica foi adaptado para gerar o programa abaixo:

```c
/*
  Analog Input

  Demonstrates analog input by reading an analog sensor on analog pin 0 and
  turning on and off a light emitting diode(LED) connected to digital pin 13.
  The amount of time the LED will be on and off depends on the value obtained
  by analogRead().

  The circuit:
  - potentiometer
    center pin of the potentiometer to the analog input 0
    one side pin (either one) to ground
    the other side pin to +5V
  - LED
    anode (long leg) attached to digital output 13 through 220 ohm resistor
    cathode (short leg) attached to ground

  - Note: because most Arduinos have a built-in LED attached to pin 13 on the
    board, the LED is optional.

  created by David Cuartielles
  modified 30 Aug 2011
  By Tom Igoe

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/AnalogInput
*/

int sensorPin = A0;    // select the input pin for the potentiometer
int ledPin = 13;      // select the pin for the LED
int sensorValue = 0;  // variable to store the value coming from the sensor
int sensMin = 1023;
int sensMax = 0;

void setup() {
  // declare the ledPin as an OUTPUT:
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  // read the value from the sensor:
  sensorValue = analogRead(sensorPin);
  sensMin=(sensorValue<sensMin)?sensorValue:sensMin;
  sensMax=(sensorValue>sensMax)?sensorValue:sensMax;
  Serial.print(sensorValue);
  Serial.print(" ");
  Serial.print(sensMin);
  Serial.print(" ");
  Serial.println(sensMax);
}
```

### Montagem do circuito

![esquemático](esquematico.jpeg)

## Resultado


