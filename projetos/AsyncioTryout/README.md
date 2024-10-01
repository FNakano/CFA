# Trying asyncio in Micropython

There are two examples. The first one blinks leds and serves static pages. The second one plays a song and serves static pages.

## Results 1

In an AI-Thinker ESP32C3 board Red led is connected to IO 3, Green led to IO 4, Blue led to IO 5.

`coro.py`: the example in https://github.com/peterhinch/micropython-async/blob/master/v3/docs/TUTORIAL.md#21-program-structure tested.
`ada.py`: `coro.py` adapted to light LEDs (they are built-in in Ai-Thinker ESP32c3 Dev Kit (

> Wiring of onboard lights: IO5 is connected to RGB blue LED; IO3 is connected to RGB red LED; IO4 is connected to RGB green LED; IO19 is connected to cool color LED; IO18 is connected to warm color LED (active high))

Source: https://rlx.sk/en/esp32-esp8266/9098-esp-c3-13-kit-ai-thinker-esp32-c3-24ghz-wifible50-development-board-er-dpi18877k.html

`servestatic.py`: a version of the Microdot *static* server example (https://github.com/miguelgrinberg/microdot/tree/main/examples/static - the server was called in a different way - using `await`)

`blinkandserve.py`: merged `ada.py` with `serverstatic.py` resulting in a three-threaded program. Two threads controls LEDs, one thread is the web server. Threads are gathered with `asyncio.gather()` and called using `await` (reference in: https://realpython.com/async-io-python/#the-asyncawait-syntax-and-native-coroutines )

## Comments and conclusions 1

It was(is?) really hard for me to understand what was going on.

I am going to write raw opinions and refining them. I apologize if I offend someone at some moment.

### About an abstraction of async/await design pattern 1

It was easier for me to understand asyncio starting by `async def` and `await` for the async defined function, instead of starting by `async.run` and `await` for `asyncio.sleep()`.

In sequence: `asyncio.run()` interfaces the single-threaded REPL with multi-threaded `asyncio` environment. `asyncio.run()` makes REPL actually start executing `asyncio` functions. It is done by awaiting for a `asyncio` task to complete. Programmers write these tasks as `async def` functions. Functions can be gathered to be executed "simultaneously". e.g. `await asyncio.gather(blinkLed1(), blinkLed2(), app.start_server(host='0.0.0.0', port=5000, debug=True,ssl=False))` in `blinkandserve.py`

What makes things hard to understand: Frequently programmers sequentially schedule tasks using `asyncio.create_task()` and await for some time using `await asyncio.sleep()` see `coro.py` for instance. The created tasks have no relation to the time the function is put to sleep (but I expected they were related). Explaining out what happens then is harder:
  
In sequence: `asyncio.run()` interfaces the single-threaded REPL with multi-threaded `asyncio` environment. `asyncio.run()` makes REPL actually start executing `asyncio` functions. It is done by scheduling tasks to be run in an auxiliary `main()` coroutine, using `asyncio.create_task` and awaiting for some time. This awaiting is mandatory, on the contrary, the function `main()`, which is async, finishes almost immediately (cancelling the scheduled tasks) and returns control to REPL. Try commenting out the command `await asyncio.sleep(10)` in function `main()` in coro.py` and executing it.


### About running REPL/WebREPL simultaneously to other threads 1


A) I remember have read a post (2017, perhaps) in Micropython forum about having multiple instances of REPL running simultaneously in a device. The idea of multiple instances of REPL was not adopted. Instead, the group stated that there should be ONE instance of REPL in a given device.

A device contains a processor.

B) On the other hand, `asyncio` depends on tasks giving up control of the processor in order to execute multiple tasks (it is called cooperative multitasking)

In consequence of A, (Micropython) REPL do not give up control of the processor, so asyncio is not able to do multitasking (or multiIO??) with REPL.

**note**: multiple instances of REPL or multitasking with REPL would raise a lot of new demands and new problems, perhaps starting on "how one can ensure that tasks run without interfering each other?", "how can tasks have segregated and shared variables and functions", ...

Makes a lot of sense WebREPL and USB REPL not to operate simultaneously. (Although there were some Micropython version where both shared the same connection and one could see what commands and responses the other got).

Also makes a lot of sense that after a program is started automatically, through `boot.py` or `main.py`, a (later) connection through WebREPL shows a busy terminal which accepts only control signals like CTRL-C and CTRL-D to interrupt the running program.

## Results 2

`music.py` is a synchronous library to play a song. It deals with music concepts (more details in https://github.com/FNakano/CFA/tree/master/projetos/AsyncioTryout#about-musicpy ). 

Attach a passive buzzer between pin 27 and GND to hear the tones.

Copy file to device an play it with:

```python
import music
music.playAquarela()
```

More scores at https://www.unijales.edu.br/library/downebook/id:4

`amusic.py` is the asynchronous program you can assyncronously play it with

```python
import amusic
import asyncio
asyncio.run(loopAquarela())
```

`playandserve.py` is the asynchronous library to play a song and serve static pages. Run it with

```python
import playandserve
import asyncio
asyncio.run(main())
```

## Comments and conclusions 2

I missed something very important. Simply put: "a coroutine must be awaited for."

Explanation: When a programmer defines corroutines (uses `async def func():`), the defined coroutine is not executed by issuing `func()`. Instead, it should be scheduled or awaited for.

For instance, in `amusic.py` I initially wrote:
  
```python
async def loopAquarela():
    while (True):
        playAquarela()

```

I believed `playAquarela()` would execute the function... my mistake! `playAquarela()` is a coroutine, it is not executed this way. It must be awaited for:

```python
async def loopAquarela():
    while (True):
        await playAquarela()

```

So does `playAquarela()` which must await for `playFig()`

```
  print (len(figAquarela))
  for n, f in zip (notasAquarela, figAquarela):
    await playFig(f, n)
    #await asyncio.sleep(0.1)
    await asyncio.sleep(0.1)

```

notice that `print()` is a standard function and that `playFig(...)` is a coroutine (`async def playFig(...))` 

## About `music.py`

The model to calculate musical notes frequencies is in https://en.wikipedia.org/wiki/Musical_note#Pitch_frequency_in_hertz - Notes are fractionary powers of two.

Octaves (https://en.wikipedia.org/wiki/Octave) and note values (https://en.wikipedia.org/wiki/Note_value) are integer powers of two.

Calculate powers of numbers requires processing power. I chose to group powers of numbers into arrays.

`notepow` array contains fractionary powers of two in 1/12 steps - it encodes note pitch (https://en.wikipedia.org/wiki/Pitch_(music)) relations in chromatic scale (https://en.wikipedia.org/wiki/Chromatic_scale). 

`pow2` array encodes octaves and note values.

The fourth octave corresponds to multiply by `pow2[4]`. 

`basefreq` corresponds to f=34.7032Hz - the first octave C. Other notes frequencies derive from base frequency by multiplying `basefreq`, `notepow` and `pow2[octave]`.

I believe the most common way of naming notes is in the diatonic scale with accidentals (https://en.wikipedia.org/wiki/Diatonic_scale https://en.wikipedia.org/wiki/Accidental_(music)). In the program I use `diat` dictionaries to map note names to note frequencies. Flat is represented by sufix '-', sharp is represented by sufix '+'.

`fig` dictionary maps note values to note names (in Portuguese).

Function `def playFig (figure, note, octave=lastoctave)` arguments are `figure` e.g.:  `'colcheia'`, note name e.g.: `'a+'`. `octave` can be ommited if desired octave is the same as the last played note octave resulting in `playFig ('colcheia', 'a+')`. Octave can be passed if it is different from the last, e.g.: `playFig ('colcheia', 'a+', 3)`. On initialization, default octave is the fourth.

