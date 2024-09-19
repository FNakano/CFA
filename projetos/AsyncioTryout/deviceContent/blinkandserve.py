#import uasyncio as asyncio
import asyncio

# webserver part

from microdot import Microdot, send_file
app = Microdot()


@app.route('/')
async def index(request):
    return send_file('static/index.html')


@app.route('/static/<path:path>')
async def static(request, path):
    if '..' in path:
        # directory traversal is not allowed
        return 'Not found', 404
    return send_file('static/' + path)


# blink led part

import time
from machine import Pin
q=Pin(4, Pin.OUT)

async def blinkLed1 ():
  while (True) :
    q.on()
    await asyncio.sleep_ms(1000)
    time.sleep_ms(100)
    q.off()
    await asyncio.sleep_ms(1000)
    time.sleep_ms(100)

p=Pin(3, Pin.OUT)

async def blinkLed2 ():
  while (True) :
    p.on()
    time.sleep_ms(100)
    await asyncio.sleep_ms(666)
    p.off()
    await asyncio.sleep_ms(666)

## joint web server and LED:
async def main():
    await asyncio.gather(blinkLed1(), blinkLed2(), app.start_server(host='0.0.0.0', port=5000, debug=True,ssl=False))

asyncio.run(main())
