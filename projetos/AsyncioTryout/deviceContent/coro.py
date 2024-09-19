import asyncio
async def bar(x):
    count = 0
    while True:
        count += 1
        print('Instance: {} count: {}'.format(x, count))
        await asyncio.sleep(1)  # Pause 1s

async def main():
    tasks = [None] * 3  # For CPython compaibility must store a reference see Note
    for x in range(3):
        tasks[x] = asyncio.create_task(bar(x))
    print('Tasks are running')
    await asyncio.sleep(10) #try commenting this out

asyncio.run(main())
# https://github.com/peterhinch/micropython-async/blob/master/v3/docs/TUTORIAL.md#22-coroutines-and-tasks