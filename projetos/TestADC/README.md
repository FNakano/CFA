# Test ESP32-C3 ADC

## Motivation


Many sensors output an analogic signal (e.g.: LDR, LM35, Dust Sensors (GP2Y1014AU0F ), ...) 

Microcontrollers can acquire analog signals and convert them to digital signals (numbers and sequence of numbers). The peripheral (microcontroller unit) which does it usually is an Analog to Digital Converter (ADC).

Different microcontrollers have different ADCs, resulting in different ways to use them. It might reach OpCode level (implement a specific machine code to start/stop data acquisition).

Micropython is a firmware that enables (compatible) microcontrollers to interpret Python language and interface them to a programming environment (e.g.: Thonny, rshell, ampy, ...) either wired (USB) or wireless (WiFi + HTTP + Web Sockets + WebREPL).

There are many microcontrollers (e.g.: RP2040, ESP32, ESP8266, STM32, ...) compatible with Micropyhon. Each microcontroller has its ADC hardware.

Micropython API to ADC is {equal/quite similar} among (compatible) microcontrollers, thus Micropython sets a *compatibility layer*. In other words, a properly written Python program can run on different microcontrollers without modifications.

Microcontrollers have their particularities. For exemple, ESP32 (S, C3) usually have two ADC units on a chip. One of them is used by the Wi-Fi unit when 
