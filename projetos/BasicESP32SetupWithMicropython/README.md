
A proposta é armazenar nesta pasta tanto os programas quanto a documentação relativa a um *setup* básico para ESP32 com Micropython de maneira que o ESP32 sirva as páginas ou em HTML ou em Markdown.

1. Como instalar Micropython no ESP32;
  - use um cabo USB para dados e energia em bom estado;
  - se o LED que indica que o ESP está ligado tiver oscilações no brilho, desconfie;
2. Para acessar o Micropyton (linha de comando, REPL - Read, Evaluate, Print Loop) convém instalar uma IDE para Python, por exemplo, Thonny
3. Testar o ESP32: acender e apagar o LED embutido;
4. Como habilitar um console Python (REPL) via WiFi (WebREPL) no ESP32;
5. Limitações no uso concomitante de WebREPL e Thonny;
6. Como conectar e usar um display OLED no ESP32;
  - i2c = I2C(sda=Pin(5), scl=Pin(4))
  - placas difíceis de encontrar documentação
7. Como iniciar o ESP32 como Ponto de Acesso Wi-Fi;
8. Como Implementar um servidor web no ESP32;
9. `boot.py` e `main.py` são arquivos *especiais* - como usá-los;


https://www.google.com/search?q=esp32+micropython+why+simultaneous+use+of+webrepl+and+thonny+is+not+possible&oq=esp32+micropython+why+simultaneous+use+of+webrepl+and+thonny+is+not+possible&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCTQzMzM1ajBqNKgCALACAQ&sourceid=chrome&ie=UTF-8
https://forum.micropython.org/viewtopic.php?t=9187
https://github.com/micropython/micropython/issues/2497
https://github.com/thonny/thonny/issues/2104
https://forum.micropython.org/viewtopic.php?t=8291
https://github.com/thonny/thonny/issues/1762
https://www.google.com/search?q=webrepl+does+not+connect+when+esp32+is+connected+to+usb&oq=webrepl+does+not+connect+when+esp32+is+connected+to+usb&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigAdIBCTI2ODcwajBqN6gCALACAA&sourceid=chrome&ie=UTF-8
https://github.com/thonny/thonny/issues/2104
https://www.google.com/search?q=micropython+async+web+server+esp32&sca_esv=197713b87bf2beb1&ei=XPHVZq3yF_6a1sQPtP7w0QY&ved=0ahUKEwitkICR4KSIAxV-jZUCHTQ_PGoQ4dUDCBA&uact=5&oq=micropython+async+web+server+esp32&gs_lp=Egxnd3Mtd2l6LXNlcnAiIm1pY3JvcHl0aG9uIGFzeW5jIHdlYiBzZXJ2ZXIgZXNwMzIyBhAAGBYYHjIIEAAYgAQYogRIhUFQ_jNYkT9wAngBkAEAmAGcAaABwQaqAQMwLja4AQPIAQD4AQGYAgigAuMGwgIKEAAYsAMY1gQYR5gDAIgGAZAGCJIHAzIuNqAHiQs&sclient=gws-wiz-serp
https://github.com/belyalov/tinyweb/releases
https://github.com/belyalov/tinyweb/blob/master/examples/esp8266.py
https://github.com/orgs/micropython/discussions/12219
https://www.google.com/search?q=micropython+microdot&oq=micropython+microdot&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQABgTGIAEMgoIAhAAGIAEGKIEMgoIAxAAGIAEGKIEMgoIBBAAGIAEGKIEMgoIBRAAGIAEGKIEMgoIBhAAGIAEGKIE0gEINDQwMWowajeoAgCwAgA&sourceid=chrome&ie=UTF-8
https://github.com/miguelgrinberg/microdot/blob/main/src/microdot/microdot.py
https://github.com/miguelgrinberg/microdot/blob/main/examples/hello/hello.py
https://microdot.readthedocs.io/en/latest/intro.html#running-with-micropython
https://github.com/miguelgrinberg/microdot/tree/main
https://www.google.com/search?q=mycropython+asyncio.run&oq=mycropython+asyncio.run&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yCggCEAAYgAQYogQyCggDEAAYgAQYogTSAQg3OTE1ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8
https://docs.micropython.org/en/latest/library/asyncio.html
https://forum.micropython.org/viewtopic.php?t=12953
https://docs.python.org/3/library/asyncio-task.html#creating-tasks
https://www.google.com/search?q=how+to+serve+http+and+websocket+simultaneously+in+micropython+esp32&oq=how+to+serve+http+and+websocket+simultaneously+in+micropython+esp32&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCTIxNjY4ajBqNKgCALACAQ&sourceid=chrome&ie=UTF-8
https://randomnerdtutorials.com/esp32-websocket-server-arduino/
https://stackoverflow.com/questions/65181260/micropython-uasyncio-websocket-server


[wemos esp32 with oled display 0.96 display enable pin - Pesquisa Google](https://www.google.com/search?q=wemos+esp32+with+oled+display+0.96+display+enable+pin&sca_esv=aaaa9a10aaa1b9d1&ei=BAvWZtDgBtvK1sQPp72t4AI&ved=0ahUKEwjQ8t3M-KSIAxVbpZUCHadeCywQ4dUDCBA&uact=5&oq=wemos+esp32+with+oled+display+0.96+display+enable+pin&gs_lp=Egxnd3Mtd2l6LXNlcnAiNXdlbW9zIGVzcDMyIHdpdGggb2xlZCBkaXNwbGF5IDAuOTYgZGlzcGxheSBlbmFibGUgcGluMggQABiABBiiBEjQKFDpC1jdJHABeAGQAQCYAagBoAHtCKoBAzAuOLgBA8gBAPgBAZgCBqAC9gXCAgoQABiwAxjWBBhHmAMAiAYBkAYIkgcDMS41oAeHEQ&sclient=gws-wiz-serp)
[ESP32 Built-in OLED Board (Wemos Lolin32): Pinout, Libraries and OLED Control | Random Nerd Tutorials](https://randomnerdtutorials.com/esp32-built-in-oled-ssd1306/)
[ESP32 OLED Display with Arduino IDE | Random Nerd Tutorials](https://randomnerdtutorials.com/esp32-ssd1306-oled-display-arduino-ide/)
[Wemos TTGO ESP8266 0.91 inch OLED for Arduino and Nodemcu buy online cheap | Funduinoshop](https://funduinoshop.com/en/electronic-modules/wireless-iot/esp-wifi/wemos-ttgo-esp8266-0.91-inch-oled-for-arduino-and-nodemcu)
[Wemos TTGO ESP8266 with 0.91 Inch OLED | Simple Stuff Matters](https://simplestuffmatters.com/wemos-ttgo-esp8266-with-0-91-inch-oled/)
[ESP32 OLED Wemos para Arduino, Módulo WiFi, Bluetooth, Dual ESP-32, ESP-32S, ESP8266, venda quente - AliExpress 502](https://pt.aliexpress.com/item/1005007305914350.html?src=google&src=google&albch=shopping&acnt=768-202-3196&isdl=y&slnk=&plac=&mtctp=&albbt=Google_7_shopping&aff_platform=google&aff_short_key=UneMJZVf&gclsrc=aw.ds&&albagn=888888&&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=pt1005007305914350&ds_e_product_merchant_id=5326656560&ds_e_product_country=BR&ds_e_product_language=pt&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=17283575038&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gclid=CjwKCAjwxNW2BhAkEiwA24Cm9LotZUIIjEs7YygCFEJ-6fgHo1yLFz-I9gy98XlBc8kUJVBtzeuORxoClnIQAvD_BwE)
[NodeMCU-Placa de Desenvolvimento com Display OLED, Módulo WiFi, Micro USB, 0.96 &quot;, CH-340,ESP-12E, Arduino, Micropython, ESP8266 - AliExpress 502](https://pt.aliexpress.com/item/1005006082033773.html?src=google&src=google&albch=shopping&acnt=768-202-3196&isdl=y&slnk=&plac=&mtctp=&albbt=Google_7_shopping&aff_platform=google&aff_short_key=UneMJZVf&gclsrc=aw.ds&&albagn=888888&&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=pt1005006082033773&ds_e_product_merchant_id=5089408953&ds_e_product_country=BR&ds_e_product_language=pt&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=19639392923&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gclid=CjwKCAjwxNW2BhAkEiwA24Cm9FTe84TpxBthDvcwBRX7xHHIn9RiRwW9Ih9O5N7Cyq_sGDRyV2zXphoCeuoQAvD_BwE)
[Placa de desenvolvimento ESP8266 NodeMCU 0,96 polegadas OLED Display,CH-340,ESP-12E Módulo WiFi, Micro USB para Arduino/Micropython ESP8266 - AliExpress](https://pt.aliexpress.com/item/1005006001356138.html?src=google&src=google&albch=shopping&acnt=768-202-3196&isdl=y&slnk=&plac=&mtctp=&albbt=Google_7_shopping&aff_platform=google&aff_short_key=UneMJZVf&gclsrc=aw.ds&&albagn=888888&&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=pt1005006001356138&ds_e_product_merchant_id=107642204&ds_e_product_country=BR&ds_e_product_language=pt&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=17364768653&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gclid=CjwKCAjwxNW2BhAkEiwA24Cm9FOnrSG4kwrSlEQgXTNv_NxjXT6UgCgVUkn-aN4U2Tt-7x9kl-UsixoCgqYQAvD_BwE)
[micropython esp32 ssd1306.py - Pesquisa Google](https://www.google.com/search?q=micropython+esp32+ssd1306.py&sca_esv=aaaa9a10aaa1b9d1&ei=1gvWZr_0Hazc1sQPv-mnwAQ&ved=0ahUKEwi_t4ax-aSIAxUsrpUCHb_0CUgQ4dUDCBA&uact=5&oq=micropython+esp32+ssd1306.py&gs_lp=Egxnd3Mtd2l6LXNlcnAiHG1pY3JvcHl0aG9uIGVzcDMyIHNzZDEzMDYucHkyBRAhGKABMgUQIRigATIFECEYoAFIuRdQygxYvxJwAXgBkAEAmAG0AaABvgOqAQMwLjO4AQPIAQD4AQGYAgSgAtYDwgIKEAAYsAMY1gQYR8ICBhAAGBYYHsICCBAAGIAEGKIEmAMAiAYBkAYIkgcDMS4zoAfkCQ&sclient=gws-wiz-serp)
[14. Using a SSD1306 OLED display — MicroPython latest documentation](https://docs.micropython.org/en/latest/esp8266/tutorial/ssd1306.html)
[MicroPython: OLED Display with ESP32 and ESP8266 | Random Nerd Tutorials](https://randomnerdtutorials.com/micropython-oled-display-esp32-esp8266/)
[micropython-esp32/drivers/display/ssd1306.py at esp32 · micropython/micropython-esp32 · GitHub](https://github.com/micropython/micropython-esp32/blob/esp32/drivers/display/ssd1306.py)
[esp8266 reset cause 4 - Pesquisa Google](https://www.google.com/search?q=esp8266+reset+cause+4&oq=esp8266+reset+cause+4&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yCggCEAAYgAQYogQyCggDEAAYgAQYogQyCggEEAAYgAQYogTSAQkxMDI5MmowajeoAgCwAgA&sourceid=chrome&ie=UTF-8)
[Reset Cause 4 Node MCU - Using Arduino / Programming Questions - Arduino Forum](https://forum.arduino.cc/t/reset-cause-4-node-mcu/651491/6)
[MicroPython - Python for microcontrollers](https://micropython.org/download/ESP8266_GENERIC/)
[1. Getting started with MicroPython on the ESP8266 — MicroPython latest documentation](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#deploying-the-firmware)
[micropython esp8266 wdt reset - Pesquisa Google](https://www.google.com/search?q=micropython+esp8266+wdt+reset&oq=micropython+esp8266+wdt+reset&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigAdIBCDg3MjFqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8)
[unexpected wdt reset on esp8266 nodemcu v3 - MicroPython Forum (Archive)](https://forum.micropython.org/viewtopic.php?t=12890)
[micropython serial connection and websocket connection common - Pesquisa Google](https://www.google.com/search?q=micropython+serial+connection+and+websocket+connection+common&oq=micropython+serial+connection+and+websocket+connection+common&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCTI1OTQ5ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8)
[Use websocket and I/O serial together in python? - Stack Overflow](https://stackoverflow.com/questions/58992017/use-websocket-and-i-o-serial-together-in-python)
[ssd1306 micropython font size - Pesquisa Google](https://www.google.com/search?q=ssd1306+micropython+font+size&oq=ssd1306+micropython+&gs_lcrp=EgZjaHJvbWUqCQgDEAAYExiABDIMCAAQRRgTGBYYHhg5MgkIARAAGBMYgAQyCQgCEAAYExiABDIJCAMQABgTGIAEMgkIBBAAGBMYgAQyBggFEEUYPDIGCAYQRRg8MgYIBxBFGDzSAQkxNzA4N2owajeoAgCwAgA&sourceid=chrome&ie=UTF-8)
[GitHub - nickpmulder/ssd1306big: A font for micropython on 128x64 pixel ssd1306 oled display.](https://github.com/nickpmulder/ssd1306big)
[Larger fonts on SSD1306 OLED displays - MicroPython Forum (Archive)](https://forum.micropython.org/viewtopic.php?t=2650)

python3 -m esptool --port /dev/ttyUSB0 erase_flash

fabio@super:~/.arduino15/packages/esp32/tools/esptool_py/4.5.1$ python3 -m esptool --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect -fm dout 0 ~/Downloads/ESP8266_GENERIC-20240602-v1.23.0.bin

python3 -m esptool --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 ~/Downloads/ESP32_GENERIC-20240602-v1.23.0.bin

