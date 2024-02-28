(instructions tested in feb 28, 2024)

Previous in [README](./README.md)

Aiming to get display, touch, event loop and screen button to function.


ft6X36 is in `lv_micropython/lib/lv_bindings/driver/generic/ft6x36.py`

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
