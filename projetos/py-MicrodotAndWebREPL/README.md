(2025-08-19) This project is formatted as an informal note/log/diary it could be reordered as a report (with intro, obj, method, result and comments/conclusions.

# Is it possible to run Microdot and WebREPL in parallel?

![](./Captura%20de%20tela%20de%202025-06-16%2018-41-27.png)


YES!

(2025-08-19) There is some loosely defined limitation. AFAIK ten routes, two I2C devices and five processes. To be investigated.

### Motivation

Achieved it with `aiorepl` - https://github.com/micropython/micropython-lib/tree/master/micropython/aiorepl

I was trying it in the wrong way...

#### I thought it was not possible to run Microdot and WebREPL in parallel ... Proved wrong!
 
As far as I tried, I did not achieve it.

In my last try, I followed https://github.com/orgs/micropython/discussions/13161#discussioncomment-7809437 and wrote a small coroutine to run alongside Microdot.

Up to Micropython 1.18 (I believe), USB REPL and WebREPL could be used simultaneously but they shared the I/O streams so that what was typed on REPL could be seen in WebREPL and vice-versa. From 1.19 on, only one end is usable at a time. Consequently, if USB REPL is connected via Thonny, WebREPL accepts password and freezes at the prompt `>>>`. It does not accept nor echoes keyboard input.

I designed the following test:

- Program the platform (an esp32-c3 supermini) to connect to wi-fi as client, start microdot and the small coroutine on `main.py`;
- Supply power to the platform with a mobile phone charger;
- Browse webrepl WEB pages stored in the platform;
- Start webREPL from the browsed pages;

 When I typed in webREPL password, I got the frozen promt. Then I opened a new tab in the browser and accessed IP:5000. The message GET / 200 popped in webREPL terminal. Then I got back to the webREPL and typed CTRL-C. This interrupted Microdot and activated webREPL.
 
![](./Captura%20de%20tela%20de%202025-06-16%2018-05-23.png)

In my interpretation, there is a single REPL. In my test it is running `main.py`. REPL can be accessed through (only one) USB or Web (not both simultaneously). A keyboard interrupt (CTRL-C) will interrupt `main.py` and reactivate REPL.

### Results (the right way)

Install `aiorepl` with 

```
import mip
mip.install('aiorepl')
```

Install microdot (go to https://github.com/miguelgrinberg/microdot , copy files to the microcontroler, try https://github.com/miguelgrinberg/microdot/tree/main/examples/static example.

Merge `static.py` from Microdot with aiorepl example (https://github.com/micropython/micropython-lib/tree/master/micropython/aiorepl#usage). This is done in `playandserve.py`

Get files `term.js`, `webrepl.css`, `webrepl.html`, `webrepl.js`, `FileSaver.js` from https://github.com/micropython/webrepl copy them to the `static` folder in the microcontroller.

Write `main.py` to start Microdot and aiorepl. This is done in `main.py`.

See `main.py` and `playandserve.py`

The files in this test are in ./src/pyboard folder. The route was changed from `static` to `src` (it was a typo)

### Comments

I searched for a solution again in 2025-06-16. Got https://github.com/orgs/micropython/discussions/17133 . It then was straightforward.
see another instance of this *same* project at https://github.com/FNakano/CFA/tree/master/projetos/py-aiorepl-microdot



