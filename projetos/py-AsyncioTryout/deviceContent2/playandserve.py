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

import amusic

## joint web server and LED:
async def main():
    await asyncio.gather(amusic.loopAquarela(), app.start_server(host='0.0.0.0', port=5000, debug=True,ssl=False))

#asyncio.run(main())

#import asyncio
#import amusic
#asyncio.run(amusic.loopAquarela())

#import asyncio
#import playandserve
#asyncio.run(playandserve.app.start_server (host='0.0.0.0', port=5000, debug=True,ssl=False))
