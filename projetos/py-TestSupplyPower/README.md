# Testing ways to supply power to various ESP32 development boards

### Next steps

1. Define and run battery endurance tests.
   - some cells output voltage may have large variations due to cell charge and age.

### Conclusions and Comments 

2. Some dev boards pass tests with three alkaline AAA cells (nom. 4.5V)
3. Some dev boards pass tests with one LiPo cell (nom. 3.7V)
3. Some dev boards pass tests with one 16340 cell (nom. 3.7V)
4. Poor quality contacts (eg. too oxidized, too loose, iil soldered, ...) may result in test fail
5. Changes in dev board specs (eg. change voltage regulator model) may result in test fail

### Introduction

BJT based voltage regulators (eg. AMS1117-3.3) have, at least 0.6V dropout voltage (information from datasheet).
MOSFET based voltage regulators (eg. AP2112-3.3) have, at leaast 0.3V dropout voltage (information from datasheet).
maximum current may not be sufficient to microcontroler's operation. It might fail in specific situations (eg. boot is ok but wifi activation (peak current) surpass voltage regulator maximum current, resulting in microcontroler's shutoff (brownout))

make it difficult to choose from specs without experimental tests.

Actual component characteristics may have small deviations from its datasheet.

Datasheets may not bring desired information (eg. microcontrolers peak current (value and duration) during wifi activation/operation)

Microcontroler power consumption may vary depending on firmware/programming language.

Experimental tests are necessary

### Method

1. Choose some widespread dev boards based on ESP32;
2. Design and build tests;
   - hardware;
   - firmware and software;
3. Run the tests;
