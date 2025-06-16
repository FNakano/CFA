#import uasyncio as asyncio
import asyncio

# webserver part

from microdot import Microdot, send_file
app = Microdot()

htmlstart = '''<!DOCTYPE html>
<html>
    <head>
        <title>Microdot Example Page</title>
        <meta charset="UTF-8">
    </head>
    <body>
        <div>
            <h1>Microdot Example Page</h1>
            <p>Hello from Microdot!</p>
'''

htmlend ='''
        </div>
    </body>
</html>
'''

@app.route('/')
async def index(request):
    return send_file('src/index.html')

@app.route('/ldr')
async def ldr(request):
    return htmlstart+str(config.light)+htmlend, 200, {'Content-Type': 'text/html'}

@app.route('/lamp/on')
async def lon(request):
    d=Pin(18,Pin.OUT) # this pin is attached to a LED
    d.value(1)
    return send_file('static/index.html')

@app.route('/lamp/off')
async def loff(request):
    d=Pin(18,Pin.OUT) # this pin is attached to a LED
    d.value(0)
    return send_file('static/index.html')

@app.route('/mute/on')
async def mon(request):
    config.mute=True
    return send_file('static/index.html')

@app.route('/mute/off')
async def moff(request):
  config.mute=False
  return send_file('static/index.html')

@app.route('/src/<path:path>')
async def static(request, path):
    if '..' in path:
        # directory traversal is not allowed
        return 'Not found', 404
    return send_file('src/' + path)

import time

async def breakForWebrepl ():
    time.sleep_ms (1)
    await asyncio.sleep(0.01)

import asyncio
import aiorepl # https://github.com/micropython/micropython-lib/tree/master/micropython/aiorepl

async def demo():
    await asyncio.sleep_ms(1000)
    print("async demo")

state = 20

async def task1():
    while state:
        #print("task 1")
        await asyncio.sleep_ms(500)
    print("done")


from machine import I2C, Pin, ADC
import ssd1306
import network

## joint web server and LED:
async def main():
    await app.start_server(host='0.0.0.0', port=5000, debug=True,ssl=False)

async def main3():
    await asyncio.gather(message(), qb(), buttonLibertango(), app.start_server(host='0.0.0.0', port=5000, debug=True,ssl=False))

#async def main2(): this did not work
#    await asyncio.gather(breakForWebrepl(), app.start_server(host='0.0.0.0', port=5000, debug=True,ssl=False))

async def main2():
    # Start the aiorepl task.
    repl = asyncio.create_task(aiorepl.task())
    await asyncio.gather(repl, app.start_server(host='0.0.0.0', port=5000, debug=True,ssl=False))


#async def main():
#    await asyncio.gather(qb())

#asyncio.run(main())

#import asyncio
#import amusic
#asyncio.run(amusic.loopAquarela())

#import asyncio
#import playandserve
#asyncio.run(playandserve.app.start_server (host='0.0.0.0', port=5000, debug=True,ssl=False))
