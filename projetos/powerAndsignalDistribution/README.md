# Power and signal distribution

## Motivation

In som projects there is not enough pins to connect components. For example, connect ESP32 3V3 pin to three other components, say, a SSD1306 OLED Display, a MPU-6050 accelerometer and a BMP280 atmospheric pressure and temperature sensor.

On early stages of development, protoboard and jumpers are used to connect these pins. On a little later stages, when prototypes should be embedded on clothes, protoboards can be bulky and uncomfortable. It this project we proppose an alternative to protoboards.

## Context

There are some standard designed Printed Circuit Boards (stdPCB) as in the left side of figure 1. They can be bought in almost any electronic components shop.

Figure 1
![](./5028552426487132015.jpg)

### Method

1. Plan circuit connections
2. Count the number of connections
3. Cut stdPCB as necessary
4. Solder pin headers
5. Add straps when necessary.

#### Mounting

For the two examples, stdPCB (figure 1 left) is cut in two pieces. One piece (figure 1 middle) has four rows the other has six rows (figure 1 right). One row has four eyelets (holes) connected by a copper line.

All holes in a row are soldered to a header pin consequently all pins are electrically connected. One row with header pins inserted can be seen on figure 1 middle.

### Examples


#### 1: ESP32, two accelerometers, two addressable LED strands, one power bank

Connection table - each column except the last one correspond to a component. The first row contains component designation (ESP is the dev kit, ac-1 and ac-2 are accelerometers, fl-1 and fl-2 are addressable LED strands, PB is a power bank). Other rows contain all the pins that are connected together. The pin name (designation in the component of the column) is written in the cell. (*)USB cable **must be disconnected** when Power bank is connected. (**) If only two pins should be connected, the pins can be connected using a jumper - no need to be distributed. 

| ESP | ac-1 | ac-2 | fl-1 | fl-2 | PB | Number of distribution rows |
| --- | --- | --- | --- | --- | --- | --- |
| 5V | --- | --- | 5V | 5V | 5V* | 1 |
| 3V3 | 3V3 | 3V3, AD0 | --- | --- | --- | 1 |
| GND | GND | GND | GND | GND | GND | 2 |
| GPIO (used as SCL) | SCL | SDA | --- | --- | --- | 1 |
| GPIO (used as SDA) | SCL | SDA | --- | --- | --- | 1 |
| GPIO (used to send data to LEDs) | --- | --- | Di | --- | --- | 0** |
| GPIO (used to send data to LEDs) | --- | --- | --- | Di | --- | 0** |

One distribution row has four (4) pins. If more than four connections are necessary, two (or more) rows are tied together with a strap.

In this case 6 distribution rows are necessary, two of them are connected with a strap. 

#### 2: ESP32, one vibration motor, one LDR, one UV sensor, one touch sensor, one OLED display

Connection table - each column except the last one correspond to a component. The first row contains component designation (ESP is the dev kit, VIB is a vibration motor). Other rows contain all the pins that are connected together. The pin name (designation in the component of the column) is written in the cell. (**) If only two pins should be connected, the pins can be connected using a jumper - no need to be distributed. 

| ESP | VIB | LDR | UV | Touch | Display | Number of distribution rows |
| --- | --- | --- | --- | --- | --- | --- |
| 3V3 | --- | 3V3 | 3V3 | 3V3 | 3V3 | 2 |
| GND | BLACK | GND | GND | GND | GND | 2 |
| GPIO (used as digital output) | RED | --- | --- | --- | --- | 0** |
| GPIO (used as analog input) | --- | LDR signal output | --- | --- | --- | 0** |
| GPIO (used as analog input) | --- | --- | UV signal output | --- | --- | 0** |
| GPIO (used as digital input) | --- | --- | --- | Touch Signal Output | --- | 0** |
| GPIO (used as SCL) | --- | --- | --- | --- | SCL | 0** |
| GPIO (used as SDA) | --- | --- | --- | --- | SDA | 0** |

In this case 4 distribution rows are necessary, two pairs of them are connected with one strap each. 

Figure 2 - Finished distributors. Six row distributor above, with its left-side rows 2 and 3 connected with a strap; four row distributor below, with left side rows connected with a strap and right side rows connected with another strap.
![](./5028552426487132021.jpg)

