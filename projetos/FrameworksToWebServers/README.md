# Frameworks to Web Servers

There is a variety of frameworks to help implement web servers in Micropython. One can even build his(her) own one, or, just build a web server directly using sockets.

Each framework (and other build approaches) have its characteristics.

I intend to list some frameworks and its relevant (to me) features. Features were compiled in 2024-Sep. I just grabbed information from the sites. I didn't test them on devices.

| download/instructions site | name | creation date | date last updated | supported devices | async | route definition syntax | comment | has function to send files | distribution format |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/ | ESP32/ESP8266 MicroPython Web Server – Control Outputs | 2018-Nov (oldest comment on page) | 2023-Jun (most recent comment on page ) | ESP32, ESP8266 | No mention | string in function argument | --- | --- | python file |
| https://github.com/miguelgrinberg/microdot | Microdot | 2019-Apr (first commit) | 2024-Aug (latest commit) | ESP32 (tested on ESP8266 - lacks memory) | uasyncio | annotations (flask-like) | database integration, Socket.IO support | yes | python package |
| https://github.com/belyalov/tinyweb | TinyWeb | 2017-Dec | 2024-May (latest commit) | ESP32, ESP8266 | uasyncio | annotations (flask-like) | database integration, Socket.IO support | yes | need to install custom firmware and package |
| https://github.com/pfalcon/picoweb | picoWeb | 2014-May (first commit) | 2020-Jul (latest commit) | from 36k heap space (suitable to ESP32, ESP8266) 64k heap for "trivial web app" | uasyncio | annotations (flask-like) | logging, potential manteinance issue (https://github.com/orgs/micropython/discussions/10247#discussioncomment-4447295) microdot is preferred | --- | python package |
| https://github.com/troublegum/micropyserver | micropyserver | 2029-Nov (first commit) | 2022-Aug (latest commit) | ESP32, ESP8266 | No mention | string in function argument | - | --- | python file |
| https://github.com/wybiral/micropython-aioweb | micropython-aioweb | 2029-Nov (first commit) | 2022-Aug (latest commit) | minimal overhead in terms of code size or memory use (ESP32, ESP8266?) | asyncio | annotations (flask-like) | support websockets | --- | python file |

Early discussions in Micropython forum: https://forum.micropython.org/viewtopic.php?t=7058

It looks like, by 2022, there was not known async functions to make client requests (https://forum.micropython.org/viewtopic.php?t=11895) but there existed a library: https://github.com/StevenRuest/async_urequests (I just forked it...)

There is a modified Micropython version with async requests: https://software.open-dev.ru/docs/online/micropython/library/arequests.html - it is from a development company in russia.


