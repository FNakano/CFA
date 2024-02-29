(instructions tested in feb 29, 2024)

Previous in [README](./README.md)

Aiming to get display, touch, event loop and screen button and roller (lvgl widget) to function.


ft6X36 is in `lv_micropython/lib/lv_bindings/driver/generic/ft6x36.py`

### current code

```
import lvgl as lv
from ili9XXX import st7789
import axp202c
axp=axp202c.PMU()
axp.enablePower(axp202c.AXP202_LDO2) # this line from lilly.LILY()
axp.setLDO2Voltage(2800)
disp = st7789(
  mosi=19, clk=18, cs=5, dc=27, rst=-1, backlight=12, power=-1,
  width=240, height=240, factor=4)
from ft6x36 import ft6x36 # https://github.com/lvgl/lv_binding_micropython?tab=readme-ov-file#micropython-bindings-usage
touch = ft6x36(sda=23, scl=32, width=240, height=240, inv_y=True, inv_x=True)
# Create a button with a label - https://docs.lvgl.io/master/get-started/quick-overview.html#micropython
scr = lv.obj()
btn = lv.button(scr)
btn.align(lv.ALIGN.CENTER, 0, -70)
label = lv.label(btn)
label.set_text('Hello World!')
roll=lv.roller(scr)
roll.align(lv.ALIGN.CENTER, 0, 30)
names = ['one','two','three','four','five']
text = '\n'.join(names)
roll.set_options(text, lv.roller.MODE.INFINITE)
lv.screen_load(scr)

```

Reference to lvgl.roller: https://baxterbuilds.com/micropython-lvgl-roller-example/

Next in [changeButtonFont](./changeButtonFont.md)


**note**: when swipe down, roller scrolls up. Screen touch area and button image also are "inverted". This is about INVERSE_PORTRAIT mentioned in https://github.com/lvgl/lv_binding_micropython/tree/master?tab=readme-ov-file#ttgo-twatch-2020-st7789-configuration-example 

**note**: tried `disp = st7789(mosi=19, clk=18, cs=5, dc=27, rst=-1, backlight=12, power=-1, width=240, height=240, factor=4, rot=st7789.INVERSE_PORTRAIT)`, `REVERSE_PORTRAIT`, `FLIP_VERTICAL`, 0, 2. None flipped the image. I gave up and decided to flip the touch panel. It was much easier to find out what to do, just edited `ft6X33.py` file. 
`

### old code

```
import lily
li=lily.LILY() # there is some command(s) in lily.LILY() which is needed by LVGL example code.
import lvgl as lv
from ili9XXX import st7789
import axp202c
axp=axp202c.PMU()
axp.setLDO2Voltage(2800)
disp = st7789(
  mosi=19, clk=18, cs=5, dc=27, rst=-1, backlight=12, power=-1,
  width=240, height=240, factor=4)
from ft6x36 import ft6x36 # https://github.com/lvgl/lv_binding_micropython?tab=readme-ov-file#micropython-bindings-usage
touch = ft6x36(sda=23, scl=32, width=240, height=240)
# Create a button with a label - https://docs.lvgl.io/master/get-started/quick-overview.html#micropython
scr = lv.obj()
btn = lv.button(scr)
btn.align(lv.ALIGN.CENTER, 0, 0)
label = lv.label(btn)
label.set_text('Hello World!')
lv.screen_load(scr)
```

Above code creates a button. button press event is detected (button appearance changes on press)

**note**: started to get a memory allocation error (not enough RAM with DMA access) dug into `lily.LILY()` got what was necessary to get the display working. This resulted in the current code (versus old code).

```
* initializing pins
* initializing i2c
Warning: I2C(-1, ...) is deprecated, use SoftI2C(...) instead
* initializing mpu
* Detect PMU Type is AXP202
Traceback (most recent call last):
  File "<stdin>", line 7, in <module>
  File "ili9XXX.py", line 760, in __init__
  File "ili9XXX.py", line 136, in __init__
RuntimeError: Not enough DMA-capable memory to allocate display buffer. Needed: 28800 bytes, largest free block: 23552 bytes
>>> 
```


Messages from touch screen driver initialization:

```
>>> from ft6x36 import ft6x36
>>> touch = ft6x36(sda=23, scl=32, width=240, height=240)
FT6X36 touch IC ready (fw id 0x4 rel 1, lib 300A)
>>> 
```

Event loop was already running

```
>>> from lv_utils import event_loop
event_loop = event_loop()
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "lv_utils.py", line 74, in __init__
RuntimeError: Event loop is already running!
```
