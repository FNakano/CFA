# python examples: https://docs.lvgl.io/8.1/examples.html
import lvgl as lv
from ili9XXX import st7789
import axp202c
from ft6x36 import ft6x36 # https://github.com/lvgl/lv_binding_micropython?tab=readme-ov-file#micropython-bindings-usage
import pcf8563
import machine
import esp32

def hardwareConfig ():
  global datetime
  axp=axp202c.PMU()
  axp.enablePower(axp202c.AXP202_LDO2) # this line from lilly.LILY()
  axp.setLDO2Voltage(3300)
  disp = st7789(
    mosi=19, clk=18, cs=5, dc=27, rst=-1, backlight=12, power=-1,
    width=240, height=240, factor=4)
  touch = ft6x36(sda=23, scl=32, width=240, height=240, inv_y=True, inv_x=True)
  hwrtc=pcf8563.PCF8563(axp.bus)
  datetime=hwrtc.datetime()

def drawRing (size, value, text):
  arc=lv.arc(lv.screen_active())
  arc.set_size(size,size)
  arc.center()
  arc.set_bg_angles(0,360)
  arc.set_rotation(270)
  arc.set_range(0,60)
  arc.set_value(value)
  lbl1=lv.label(lv.screen_active())
  lbl1.set_style_text_font(lv.font_montserrat_24,0)
  lbl1.set_text(text)
  arc.rotate_obj_to_angle(lbl1, 20)

def drawHourMin (hours, mins):
  # cannot destroy hourArc, minArc, ... objects from another function
  drawRing (190, mins, str(mins))
  drawRing (100, (hours%12)*5, str(hours))
  # machine.freq(20000000) too slow

def sleepCB (event):
  axp=axp202c.PMU()
  axp.disablePower(axp202c.AXP202_LDO2) # backlight
  axp.disablePower(axp202c.AXP202_LDO4) # audio
  touchInt=machine.Pin(38, machine.Pin.IN) # touchscreen interrupt is connected to pin 38 which is a touch pin - this might work
  esp32.wake_on_ext0 (touchInt, esp32.WAKEUP_ALL_LOW) # pin seems to be active low
  machine.deepsleep() # sleep forever
  
hardwareConfig()
drawHourMin(datetime[4], datetime[5])
tim=lv.timer_create(watch.sleepCB, 200000, None) # https://forum.lvgl.io/t/how-to-delete-one-lv-timer-in-micropython-lgvl-version-8-3/9428/1
