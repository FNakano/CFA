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

## I2C in asyncio 

I expected I2C with asyncio would be tricky... because the async program should (efficiently) await for the bytes to arrive from or to be sent through I2C bus. BUT, in Micropython, one of the I2C layers is treated with the synchronous module.


I inferred a layer model based on searched documentation:
  
<pre>
-------------------
| User program    |
-------------------
| API asi2c       |
-------------------
| API machine.I2C |
-------------------
| FreeRTOS I2C API|
-------------------
| Hardware        |
-------------------
| I2C bus         |
-------------------
</pre>

I2C bus signals consists on two wires, usually named SCL and SDA. A connection to GND (logic level reference) must also be provided.

The wires are connected to ESP32 SoC pins. Most of ESP32 SoC are multiplexed (https://docs.espressif.com/projects/arduino-esp32/en/latest/tutorials/io_mux.html#id1) so almost any pin can be connected (muxed) to I2C dedicated hardware inside ESP32 SoC.

ESP32 SoC has two I2C hardware ports (https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/peripherals/i2c.html https://docs.micropython.org/en/latest/esp32/quickref.html#hardware-i2c-bus) 

ESP32 SoC and FreeRTOS are, somehow, bound: *FreeRTOS is an open source RTOS (real-time operating system) kernel that is integrated into ESP-IDF as a component.* (https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/freertos.html?highlight=freertos#freertos-overview). If one uses ESP-IDF to develop applications, he/she should use the API provided through FreeRTOS. Particularly, I2C FreeRTOS API is documented here: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/peripherals/i2c.html?highlight=freertos%20i2c

Some information and references: ESP-IDF do not provide I2C by software (softI2C). Hardware I2C transmission/reception buffer sizes can be configured (https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/peripherals/i2c.html?highlight=freertos%20i2c#_CPPv4N23i2c_master_bus_config_t17trans_queue_depthE) FreeRTOS provide ring buffers (https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/freertos_additions.html#ring-buffers). Ring buffers are part of I2C and UART firm(?)ware (https://www.esp32.com/viewtopic.php?t=10661 https://esp32.com/viewtopic.php?t=30581) 

IO buffers are necessary to improve SoC performance. It is expected that I2C and UART have hardware buffers. Buffer sizes are an important parameter because, considering transmission rate, they limit the time interval that the peripheral can operate without processor intervention. This is the maximum time slot a process can exclusively use the processor, or, the interval between interrupts. BUT ESP peripheral hardware buffer sizes are not available (AFAIK). Some people tried to estimate buffer size, without success. It happens that ESP uses double-buffers: O the top of hardware buffers there are ring buffers (auxiliary software data structures) which extend buffer sizes and intervals between interrupts (https://esp32.com/viewtopic.php?t=30581). Ring buffers used in I2C and UART probably have 256 bytes. DMA enables the processor and peripherals to share RAM transparently.

At this point is clear that asynchronous IO has a role and `asyncio` could start from here BUT Micropython is in between.

Micropython has its syncronous `machine.I2C` API and `asyncio` is put on top of it. It is hard to estimate performance impact of this organization. (I'm going to leave this to a next step) . The Micropython I2C API documentation is here: https://docs.micropython.org/en/latest/library/machine.I2C.html#primitive-i2c-operations . These are syncronous functions, they are expected to block until the operation completes.

`asyncio` has async I2C modules: `asi2c.py asi2c_i.py i2c_esp.py i2c_init.py i2c_resp.py` (https://github.com/peterhinch/micropython-async/tree/master/v3/as_drivers/i2c). The files implement a sender/receiver example documented in https://github.com/peterhinch/micropython-async/blob/master/v3/docs/I2C.md 

An easier (for me) to understand example builds a class to comunicate (asyncrhonously) to an I2C sensor. The documentation is here: https://github.com/peterhinch/micropython-async/blob/master/v3/docs/HTU21D.md .  Notice that the author needed to estimate the time to complete reading.
