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
touch = ft6x36(sda=23, scl=32, width=240, height=240, inv_y=True)
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
