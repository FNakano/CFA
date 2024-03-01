(instructions tested in mar 01, 2024)

Previous in [deepSleep.md](./deepSleep.md)

## Motivation

- Look for the most visible, effortless way to show time.


My lvgl port seems not to have a meter widget. https://baxterbuilds.com/micropython-lvgl-meter-examples/ . It does have an arc widget (https://baxterbuilds.com/micropython-lvgl-arc-example/)

### Resulting code

```
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

arc_main = lv.arc(lv.screen_active())
arc_main.set_size(200,200)
arc_main.set_bg_angles(180,90)
arc_main.center()

min_arc = lv.arc(lv.screen_active())
min_arc.set_size(100,100)
min_arc.set_bg_angles(0,270)
min_arc.set_mode(lv.arc.MODE.SYMMETRICAL)
min_arc.center()
# min_arc.remove_style(None,lv.PART.KNOB)

label = lv.label(lv.screen_active())
label.set_text('0')

pointer = lv.obj(lv.screen_active())
pointer.set_size(10,40)
pointer.set_style_bg_color(lv.color_hex(0x000000),0)
pointer.center()

label.set_text('91')
min_arc.set_value(91)
arc_main.set_value(91)

arc_main.align_obj_to_angle(label,0)
arc_main.rotate_obj_to_angle(pointer,-80)

def new_val(data):
    arc = data.get_target()
    
    label.set_text(str(arc.get_value()))
    
    min_arc.set_value(arc.get_value())
    
    arc_main.set_value(arc.get_value())
    arc_main.align_obj_to_angle(label,0)
    arc_main.rotate_obj_to_angle(pointer,-80)

arc_main.add_event_cb(new_val,lv.EVENT.VALUE_CHANGED,None)
min_arc.add_event_cb(new_val,lv.EVENT.VALUE_CHANGED,None)
```

Reference: https://baxterbuilds.com/micropython-lvgl-arc-example/ - just changed some identifiers.

Next in [bigMess.md](./bigMess.md)
