# success

import lvgl as lv
from ili9XXX import st7789
from ili9XXX import REVERSE_PORTRAIT
import axp202c
from ft6x36 import ft6x36
import pcf8563
import machine
import esp32
import math

class RFACE:
  def setHardware (self):
    print("LVGL version:"+str(lv.version_major())+"."+str(lv.version_minor()))
    self.axp=axp202c.PMU()
    self.axp.enableADC(axp202c.AXP202_ADC1,axp202c.AXP202_BATT_VOL_ADC1) # https://github.com/lewisxhe/MicroPython-for-TTGO-T-Watch?tab=readme-ov-file#axp202-power-example
    self.axp.enableADC(axp202c.AXP202_ADC1, axp202c.AXP202_BATT_CUR_ADC1)
    self.axp.enableADC(axp202c.AXP202_ADC1, axp202c.AXP202_VBUS_VOL_ADC1)
    self.axp.enableADC(axp202c.AXP202_ADC1, axp202c.AXP202_VBUS_CUR_ADC1)
    self.axp.enablePower(axp202c.AXP202_LDO2) # this line from lilly.LILY()
    self.axp.enablePower(axp202c.AXP202_LDO3) # turn something on
    self.axp.enablePower(axp202c.AXP202_LDO4) # turn audio on
    self.axp.enablePower(axp202c.AXP202_DCDC2) # turn something on
    self.axp.enablePower(axp202c.AXP202_EXTEN) # turn something on
    self.disp = st7789(
      mosi=19, clk=18, cs=5, dc=27, rst=-1, backlight=12, power=-1,
      width=240, height=240, factor=4, invert=True, rot=REVERSE_PORTRAIT, start_x=0, start_y=80)
    # got REVERSE_PORTRAIT to work!
    self.touch = ft6x36(sda=23, scl=32, width=240, height=240)
    self.hwrtc=pcf8563.PCF8563(self.axp.bus)

  def unsetHardware (self):
    del self.disp
    del self.touch
    del self.axp

  def drawFace (self):
    actscr=lv.screen_active()
    lv.obj.clean(actscr)
    r=105
    self.lbl11=lv.label(actscr)
    self.lbl11.set_style_text_font(lv.font_montserrat_24,0)
    self.lbl11.set_text("11")
    self.lbl11.align(lv.ALIGN.CENTER,round(-r*0.5),round(-r*0.86))
    self.lbl10=lv.label(lv.screen_active())
    self.lbl10.set_style_text_font(lv.font_montserrat_24,0)
    self.lbl10.set_text("10")
    self.lbl10.align(lv.ALIGN.CENTER,round(-r*0.86),round(-r*0.5))
    self.lbl9=lv.label(lv.screen_active())
    self.lbl9.set_style_text_font(lv.font_montserrat_24,0)
    self.lbl9.set_text("9") 
    self.lbl9.align(lv.ALIGN.CENTER,round(-r*1),round(-r*0))

    self.lbl7=lv.label(lv.screen_active())
    self.lbl7.set_style_text_font(lv.font_montserrat_24,0)
    self.lbl7.set_text("7")
    self.lbl7.align(lv.ALIGN.CENTER,round(-r*0.5),round(r*0.86))
    self.lbl8=lv.label(lv.screen_active())
    self.lbl8.set_style_text_font(lv.font_montserrat_24,0)
    self.lbl8.set_text("8")
    self.lbl8.align(lv.ALIGN.CENTER,round(-r*0.86),round(r*0.5))
    self.lbl6=lv.label(lv.screen_active())
    self.lbl6.set_style_text_font(lv.font_montserrat_24,0)
    self.lbl6.set_text("6")  
    self.lbl6.align(lv.ALIGN.CENTER,round(r*0),round(r*1))

    self.lbl1=lv.label(lv.screen_active())
    self.lbl1.set_style_text_font(lv.font_montserrat_24,0)
    self.lbl1.set_text("1")
    self.lbl1.align(lv.ALIGN.CENTER,round(r*0.5),round(-r*0.86))
    self.lbl2=lv.label(lv.screen_active())
    self.lbl2.set_style_text_font(lv.font_montserrat_24,0)
    self.lbl2.set_text("2")
    self.lbl2.align(lv.ALIGN.CENTER,round(r*0.86),round(-r*0.5))
    self.lbl3=lv.label(lv.screen_active())
    self.lbl3.set_style_text_font(lv.font_montserrat_24,0)
    self.lbl3.set_text("3")  
    self.lbl3.align(lv.ALIGN.CENTER,round(r*1),round(-r*0))

    self.lbl5=lv.label(lv.screen_active())
    self.lbl5.set_style_text_font(lv.font_montserrat_24,0)
    self.lbl5.set_text("5")
    self.lbl5.align(lv.ALIGN.CENTER,round(r*0.5),round(r*0.86))
    self.lbl4=lv.label(lv.screen_active())
    self.lbl4.set_style_text_font(lv.font_montserrat_24,0)
    self.lbl4.set_text("4")
    self.lbl4.align(lv.ALIGN.CENTER,round(r*0.86),round(r*0.5))
    self.lbl12=lv.label(lv.screen_active())
    self.lbl12.set_style_text_font(lv.font_montserrat_24,0)
    self.lbl12.set_text("12")
    self.lbl12.align(lv.ALIGN.CENTER,round(-r*0),round(-r*1))

    stp= math.pi/30
 
    for i in range (0,59):
      lbl=lv.label(lv.screen_active())
      lbl.set_style_text_font(lv.font_montserrat_24,0)
      lbl.set_text(".")
      lbl.align(lv.ALIGN.CENTER,round(math.cos(stp*i)*r),round(math.sin(stp*i)*r))
# draw context does not work.
  def drawHands(self):
    scr=lv.screen_active()
    scr.add_event_cb(self.drawHandsCB,lv.EVENT.DRAW_MAIN_END,None)

  def drawHandsCB(self, data):
    rect = lv.draw_rect_dsc_t()
    rect.init()
    rect.bg_color = lv.color_hex(0x00ff00)
    
    size_and_spot = lv.area_t()
    size_and_spot.x1 = 0
    size_and_spot.y1 = 20
    size_and_spot.x2 = 200
    size_and_spot.y2 = 100
    
    draw_ctx = data.get_draw_task()
    draw_ctx.rect(rect,size_and_spot)
"""
import roundface
f=roundface.RFACE()
f.setHardware()
f.drawFace()
"""