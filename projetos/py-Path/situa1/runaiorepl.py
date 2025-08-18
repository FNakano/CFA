import asyncio
import aiorepl

async def demo():
    await asyncio.sleep_ms(1000)
    print("async demo")

state = 20

async def task1():
    while state:
        #print("task 1")
        await asyncio.sleep_ms(500)
    print("done")

async def main():
    print("Starting tasks...")

    # Start other program tasks.
    t1 = asyncio.create_task(task1())

    # Start the aiorepl task.
    repl = asyncio.create_task(aiorepl.task())

    await asyncio.gather(t1, repl)

asyncio.run(main())