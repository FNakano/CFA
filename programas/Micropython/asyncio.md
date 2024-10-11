# asyncio library

## The problem

Apply the capitalist way to computer systems: A computer system costs resources (time, money, ...) performs some tasks and provide results (which are profitable). It is reasonable to maximize profit= result/cost. This is achiavable by reducing costs or by improving results. To improve resuts, the computer system should provide more results using the same (or less) resources (time). Considering the hardware cost as already spent, how can one *use the maximum of the hardware?*

## More context

Textbooks like STALLINGS, W. Computer Organization and Architecture state that *...I/O devices are slow compared to the processor...*  (Sec 8.1 p. 283 of the 10th Ed.). This is more frequent than I/O devices which are faster than the processor.

To overcome the speed difference, designers (programmers) use techniques in multiprogramming (also named multitasking). Nice examples are given in STALLINGS textbook.

The microcontroller on a board is a processor connected to sensors and actuators which can be considered I/O devices. Sensor/Actuator management is equivalent to run an I/O-bound program. In I/O-bound programs, processor speed is best used by the processor make an I/O request, performing other tasks and returning (or being interrupted) when the I/O request is complete (it means data is available). This can be achieved by many ways. `asyncio` is one of them.

Limiting to Python programming, asyncio is a package which implements *functions* to perform asynchronous I/O operations. This enables the program (or the programmer) to run many functions *cooperatively*. eg.: a running function starts an I/O operation and await for its result. Meanwhile, asyncio can switch to (execute) other functions. It is cooperative because all functions *must* await in order to asyncio switch functions.

## Python and Micropython evolution of asyncio

In CPython, according to https://realpython.com/async-io-python/#async-ios-roots-in-generators , asyncio derives from generators ([PEP255-Generators](https://peps.python.org/pep-0255/)). According to https://mleue.com/posts/yield-to-async-await/ , generators are iterators which, instead of contain all values and iterate, generate one value on demand. The ideia (design pattern) was extended to IO and multitasking ([PEP342-Generators and Coroutines](https://peps.python.org/pep-0342/)) AND also continued to evolve as generator. This started out in 2001 and Python adopted the gen/yield syntax, which became too complicated. In 2015, the syntax was changed to async/await ([PEP492-Coroutines with async and await syntax](https://www.python.org/dev/peps/pep-0492/))

A little later (2019?), Micropython adopted the same solution (https://forum.micropython.org/viewtopic.php?t=7075)

The change from gen/yield to async/await caused some confusion: https://stackoverflow.com/questions/44251045/what-does-the-yield-from-syntax-do-in-asyncio-and-how-is-it-different-from-aw . Also this change happened at the same period of Python 2 to Python 3 change. Also, Micropython dropped the 'u' prefix to its libraries (https://docs.micropython.org/en/v1.14/library/uasyncio.html#core-functions https://docs.micropython.org/en/latest/library/asyncio.html)

## Conclusions

- async/await syntax is preferable;
- Micropython libraries dropped 'u' prefix;


## Examples

https://github.com/FNakano/CFA/tree/master/projetos/AsyncioTryout contains two examples of asyncio use. The first one blinks LEDs and (simultaneously) serves static web pages. The second one plays a song (with a passive buzzer) and serves static web pages.

