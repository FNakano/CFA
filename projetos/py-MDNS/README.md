Multicast Domain Name Service (mDNS) [RFC 6762](https://datatracker.ietf.org/doc/html/rfc6762) is essencial for Domain Name Service based Service Discovery (DNS-SD) [RFC 6763](https://datatracker.ietf.org/doc/html/rfc6763) to work.

Official Micropython firmware for ESP32 boards have (some of) mDNS support enabled but it is not enough to do service advertisement and discovery. 

There exists a Micropython package to do service advertisement (not yet tested) and service discovery (tested). It is in https://github.com/cbrand/micropython-mdns . I'm going to use it.

There is some incompatibility between mDNS package and official Micropython firmware for ESP32 so to use mDNS package, a modified version of Micropython should be flashed into ESP32 board. The package creator deploys the modified versions of Micropython in https://github.com/cbrand/micropython-mdns/releases

**note**: mDNS package uses `asyncio`. Currently, `asyncio` is distributed within Micropython (official and modified versions).

mDNS package use examples are kept in https://github.com/cbrand/micropython-mdns/tree/main/examples

The straight recipe to run an example is:
  
1. Download one modified version of Micropython from https://github.com/cbrand/micropython-mdns/releases
  - I downloaded https://github.com/cbrand/micropython-mdns/releases/download/1.5.0/firmware.mp.1.23.esp32.bin
2. Flash it to ESP32 board (instructions at https://micropython.org/download/ESP32_GENERIC/)
  - `python3 -m esptool --chip esp32 --port /dev/ttyACM0 erase_flash`
  - `python3 -m esptool --chip esp32 --port /dev/ttyACM0  --baud 460800 write_flash -z 0x1000 ~/Downloads/firmware.mp.1.23.esp32.bin `
3. Install mDNS package in ESP32 board (enter commands in ESP32 REPL - eg.: Thonny shell) (instructions in https://github.com/cbrand/micropython-mdns?tab=readme-ov-file#installation)
  - `import mip`
  - `mip.install("github:cbrand/micropython-mdns")`
4. Copy file `service_discovery_constant.py` in ESP32 board (file is in https://github.com/cbrand/micropython-mdns/blob/main/examples/service_discovery_constant.py)
  - I modified SSID and PASSWORD and service names. Modified file is in this folder
5. run the example in ESP32 board (enter commands in ESP32 REPL - eg.: Thonny shell) 
  - `import service_discovery_constant`

### Result

![](./Captura%20de%20tela%20de%202024-10-19%2012-07-44.png))

**note**: I have thing-directory (https://github.com/narcisoleedev/thing-directory/blob/master/customInstall.md) configured and running. It responds to mDNS so running the example does not return an empty list.
