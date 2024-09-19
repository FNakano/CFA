import asyncio
from machine import Pin
import time

led=[Pin(4, Pin.OUT), Pin(3, Pin.OUT), Pin(5, Pin.OUT)]

async def bar(x):
    count = 0
    while True:
        count += 1
        print('Instance: {} count: {}'.format(x, count))
        if (led[x].value()):
            led[x].value(0)
        else:
            led[x].value(1)
        time.sleep(0)
        await asyncio.sleep(1)  # Pause 1s

async def main():
    tasks = [None] * 3  # For CPython compaibility must store a reference see Note
    for x in range(3):
        tasks[x] = asyncio.create_task(bar(x))
    print('Tasks are running')
    # await asyncio.sleep(10)

asyncio.run(main())

# adapted from
# https://github.com/peterhinch/micropython-async/blob/master/v3/docs/TUTORIAL.md#22-coroutines-and-tasks