(instructions tested in mar 01, 2024)

Previous in [grid.md](./grid.md)

## Motivation

- Reduce battery drain in T-Watch 2020 v.3
- Provide an alternative to turning the watch off (explanation below)
- Deep Sleep is a bit complicated when the device is composed of various sensors/actuators (explanation below)

### Why turn the watch off?

Looks like instantiating the display (ST7899) more than once results in error listed below:
	

```
Traceback (most recent call last):
  File "<stdin>", line 7, in <module>
  File "ili9XXX.py", line 760, in __init__
  File "ili9XXX.py", line 136, in __init__
RuntimeError: Not enough DMA-capable memory to allocate display buffer. Needed: 28800 bytes, largest free block: 23552 bytes
>>> 
```

Soft reset (Thonny stop button, REPL CTRL-D) and instantiating results in the same error. I suppose soft reset cleans up variable names but do not clean up (free) allocated memory. A hard reset (such as turning the whatch off) cleans up variables and free allocated memory (I tested).

It is not convenient to turn the watch on/off every program start.

I found out that deep sleep also cleans up variables and allocated memory.

More on soft reset and hard reset with micropython: https://docs.micropython.org/en/latest/wipy/tutorial/reset.html

### Why deep sleep is a bit complicated

Because there are some peripherals connected to ESP32 and system's power management is provided by a dedicated chip (AXP202) configured through I2C and ESP32. Consequently, disabling ESP32 power in AXP202 (if possible) would brick the watch (did not try it).

Interrupt sources should be set and corresponding sensor should be enabled. T-Watch v.3 hardware pinout is in: https://github.com/Xinyuan-LilyGO/TTGO_TWatch_Library/blob/master/docs/watch_2020_v3.md

**note**: According to the documentation (https://github.com/Xinyuan-LilyGO/TTGO_TWatch_Library/blob/master/docs/watch_2020_v3.md) it is not possible to shut ESP32 off in T-Watch 2020 v3. Backlight and audio are controlled by AXP202. 

### Objective

Try out deep sleep with touch panel as wakeup source, disabling other peripherals.

### Procedure (plan)

- disable accelerometer;
- disable screen;
- enable touch panel;
- disable audio;
- set touch panel as interrupt source;
- deep sleep for some time (a minute);
- before some time pass, try to wake it up with touch event;

### Resulting code

- create a working screen, config and deep sleep.

```
import machine
import esp32
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
  print('woke from deep sleep')
import lvgl as lv
from ili9XXX import st7789
import axp202c
from ft6x36 import ft6x36 # https://github.com/lvgl/lv_binding_micropython?tab=readme-ov-file#micropython-bindings-usage
axp=axp202c.PMU()
axp.enablePower(axp202c.AXP202_LDO2) # this line from lilly.LILY()
axp.setLDO2Voltage(3300)
disp = st7789(
  mosi=19, clk=18, cs=5, dc=27, rst=-1, backlight=12, power=-1,
  width=240, height=240, factor=4)
touch = ft6x36(sda=23, scl=32, width=240, height=240, inv_y=True, inv_x=True)

#you can replace the lvgl.grid_fr(x) with pixel width/height
row = [ lv.grid_fr(1), lv.grid_fr(1), lv.GRID_TEMPLATE_LAST ]
column = [ lv.grid_fr(1), lv.grid_fr(1), lv.GRID_TEMPLATE_LAST ]

cont = lv.obj() # cont is the screen
cont.set_size( 240, 240 )
cont.center()
cont.set_layout( lv.LAYOUT.GRID )
cont.set_style_grid_row_dsc_array( row, 0 ) 
cont.set_style_grid_column_dsc_array( column, 0 )

def butt( text, row_x, column_y ):
    btn = lv.button( cont )
    
    label = lv.label( btn )
    label.set_text( text )
    label.center()
    
    btn.set_grid_cell( lv.GRID_ALIGN.STRETCH, row_x, 1, lv.GRID_ALIGN.CENTER, column_y, 1 )
    
    return btn

butt( 'hi1', 0, 0 )
butt( 'hi2', 1, 0 )
butt( 'hi3', 0, 1 )
butt( 'hi4', 1, 1 )

lv.screen_load(cont)

axp.disablePower(axp202c.AXP202_LDO2) # backlight
axp.disablePower(axp202c.AXP202_LDO4) # audio
touchInt=machine.Pin(38, machine.Pin.IN) # touchscreen interrupt is connected to pin 38 which is a touch pin - this might work
# esp32.wake_on_ext0 (touchInt, esp32.WAKEUP_ANY_HIGH) # turned on immediately  
esp32.wake_on_ext0 (touchInt, esp32.WAKEUP_ALL_LOW) # pin seems to be active low
machine.deepsleep(60000)

```

Next in [watchFace.md](./watchFace.md)
