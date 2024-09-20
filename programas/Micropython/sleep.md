There are AFAIK, 3 functions named `sleep`.

From package `asyncio` (https://docs.micropython.org/en/latest/library/asyncio.html#asyncio.sleep). This sleep function, in the scope of asyncio, puts a task to sleep (consequently enables asyncto to switch tasks).

From package `timer` (https://docs.micropython.org/en/latest/library/time.html#time.sleep) *Sleep for the given number of seconds.*. The sleep mechanism is not specified. It may use hardware timers, processor clock, ... It is not stated how it interacts with `asyncio.sleep` - probably it does not interact since it is not `async def`, one can expect that it blocks `asyncio`.

From package `machine` (https://docs.micropython.org/en/latest/library/machine.html#machine.sleep). Although deprecated, *If time_ms is specified then this will be the maximum time in milliseconds that the sleep will last for. Otherwise the sleep can last indefinitely.* . This function put the processor to sleep (enter a low power state, like sleep mode in OSes like Linux and Windows).
 
