This is a backup of all latest files in TTGO T-Watch with micropyton (1.20) and LVGL (9.0). Micropython image is ../micropython.bin .

I used [rshell](https://github.com/dhylands/rshell) to dowload all files at once. Notice: started rshell with `rshell -p /dev/ttyACM0`, watch filesystem is in `\pyboard`. Get board name with `boards` rshell command.

My Watch flash size is 16MB.

<pre><font color="#33DA7A"><b>fabio@super</b></font>:<font color="#2A7BDE"><b>~</b></font>$ esptool.py -p /dev/ttyACM0 flash_id
esptool.py v4.3
Serial port /dev/ttyACM0
Connecting....
Detecting chip type... Unsupported detection protocol, switching and trying again...
Connecting.....
Detecting chip type... ESP32
Chip is ESP32-D0WDQ6-V3 (revision v3.0)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
Crystal is 40MHz
MAC: 44:17:93:8f:31:74
Uploading stub...
Running stub...
Stub running...
Manufacturer: ef
Device: 4018
Detected flash size: 16MB
Hard resetting via RTS pin...
</pre>

### Opinions

T-Watch with Micropython and LVGL is a nice idea but it is hard to use.

There are not many Micropython+LVGL code examples. Function and contant names differ from the ones in C. 

T-Watch with MicroPython + LVGL and an instance of ST7789 leave too little RAM for python autocomplete to run.

Power consumption is also an issue. Micropython + LVGL, even using `machine.deepsleep()`, results in battery life of roughly one day. Too small compared to six days I get when running a C + LVGL code.

Boot time: I configured the watch to boot on touch screen interrupt. C code boots in approx 3s, Micropython code boots in approx. 10 s.

I give up (for now). Justified by low boot speed, high RAM usage and high power consumption.


