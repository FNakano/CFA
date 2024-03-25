# python examples: https://docs.lvgl.io/8.1/examples.html
# I believe all hardware components are singletons so it results in
# shorter to source code "create" an object
# the device is short in RAM so destroying graphical object to navigate
# between screen is an option. This requires storing pointers to the
# graphical objects in order to destroy them.

import lvgl as lv
from ili9XXX import st7789
from ili9XXX import REVERSE_PORTRAIT
import axp202c
from ft6x36 import ft6x36 # https://github.com/lvgl/lv_binding_micropython?tab=readme-ov-file#micropython-bindings-usage
import pcf8563
import machine
import esp32

class WATCH:
  tim=None
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
    self.log('VerHora')

  def drawProgrammingFace (self):
    actscr=lv.screen_active()
    lv.obj.clean(actscr)
    self.lblSleep=lv.label(lv.screen_active())
    self.lblSleep.set_style_text_font(lv.font_montserrat_24,0)
    self.lblSleep.align(lv.ALIGN.TOP_MID,0,0)

    #self.lblCharge=lv.label(lv.screen_active())
    #self.lblCharge.align(lv.ALIGN.BOTTOM_LEFT,0,0)
    #self.lblCharge.set_style_text_font(lv.font_montserrat_24,0)
    #self.lblCharge.set_text(str(self.axp.getBattPercentage()))
    # self.axp.isChargeing()
    btn=lv.button(lv.screen_active())
    btn.add_event_cb(lambda e: self.cancelSleep(), lv.EVENT.CLICKED, None) # deploy.w.cancelSleep()
    # btn.add_event_cb(lambda e: print("clicked on play"), lv.EVENT.CLICKED, None) # deploy.w.cancelSleep()
    btn.align(lv.ALIGN.TOP_LEFT, 0, 0)
    label=lv.label(btn)
    label.set_style_text_font(lv.font_montserrat_24,0)
    # label.set_style_text_color(lv.color_hex(0x0), 0) # works!
    label.set_text(lv.SYMBOL.PLAY) # right text
    # label.set_text(str(self.temp)) # temp is not environment temperature
    # label.set_text(str(self.axp.getBattPercentage())+'%')

    btn2=lv.button(lv.screen_active())
    btn2.add_event_cb(lambda e: self.sleepOnTimer(), lv.EVENT.CLICKED, None)
    label=lv.label(btn2)
    label.set_style_text_font(lv.font_montserrat_24,0)
    label.set_text(lv.SYMBOL.STOP) # right text
    # label.set_text(str(self.mday)+"/"+str(self.mon))
    btn2.align(lv.ALIGN.TOP_RIGHT, 0,0)

    btn3=lv.button(lv.screen_active())
    btn3.add_event_cb(lambda e: self.axp.shutdown(), lv.EVENT.CLICKED, None)
    label=lv.label(btn3)
    label.set_style_text_font(lv.font_montserrat_24,0)
    label.set_text("shutdown")
    btn3.align(lv.ALIGN.CENTER, 0,0)

  def drawTimeFace (self):
    btn=lv.button(lv.screen_active())
    btn.set_style_bg_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
    btn.add_event_cb(lambda e: self.drawProgrammingFace(), lv.EVENT.CLICKED, None) # deploy.w.cancelSleep()
    # btn.add_event_cb(lambda e: print("clicked on play"), lv.EVENT.CLICKED, None) # deploy.w.cancelSleep()
    label=lv.label(btn)
    label.set_style_text_color(lv.color_hex(0x0), 0)
    label.set_style_text_font(lv.font_montserrat_24,0)
    # label.set_style_text_color(lv.color_hex(0x0), 0) # works!
    # label.set_text(lv.SYMBOL.PLAY) # right text
    # label.set_text(str(self.temp)) # temp is not environment temperature
    label.set_text(str(self.axp.getBattPercentage())+'%')
    btn.align(lv.ALIGN.TOP_RIGHT, 0, 0)

    btn2=lv.button(lv.screen_active())
    btn2.set_style_bg_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
    # btn2.add_event_cb(lambda e: self.sleepOnTimer(), lv.EVENT.CLICKED, None)
    label=lv.label(btn2)
    label.set_style_text_color(lv.color_hex(0x0), 0)
    label.set_style_text_font(lv.font_montserrat_24,0)
    label.set_text(str(self.mday)+"/"+str(self.mon))
    btn2.align(lv.ALIGN.TOP_LEFT, 0,0)

    self.lbl11=lv.label(lv.screen_active())
    self.lbl11.set_style_text_font(lv.font_montserrat_24,0)
    self.lbl11.set_text("11")
    self.lbl11.align(lv.ALIGN.CENTER,round(-105*0.5),round(-105*0.86))
    self.lbl10=lv.label(lv.screen_active())
    self.lbl10.set_style_text_font(lv.font_montserrat_24,0)
    self.lbl10.set_text("10")
    self.lbl10.align(lv.ALIGN.CENTER,round(-105*0.86),round(-105*0.5))
    #self.lbl9=lv.label(lv.screen_active())
    #self.lbl9.set_style_text_font(lv.font_montserrat_24,0)
    #self.lbl9.set_text("9") 
    #self.lbl9.align(lv.ALIGN.CENTER,round(-105*1),round(-105*0))

    self.lbl7=lv.label(lv.screen_active())
    self.lbl7.set_style_text_font(lv.font_montserrat_24,0)
    self.lbl7.set_text("7")
    self.lbl7.align(lv.ALIGN.CENTER,round(-105*0.5),round(105*0.86))
    self.lbl8=lv.label(lv.screen_active())
    self.lbl8.set_style_text_font(lv.font_montserrat_24,0)
    self.lbl8.set_text("8")
    self.lbl8.align(lv.ALIGN.CENTER,round(-105*0.86),round(105*0.5))
    #self.lbl6=lv.label(lv.screen_active())
    #self.lbl6.set_style_text_font(lv.font_montserrat_24,0)
    #self.lbl6.set_text("6")  
    #self.lbl6.align(lv.ALIGN.CENTER,round(105*0),round(105*1))

    self.lbl1=lv.label(lv.screen_active())
    self.lbl1.set_style_text_font(lv.font_montserrat_24,0)
    self.lbl1.set_text("1")
    self.lbl1.align(lv.ALIGN.CENTER,round(105*0.5),round(-105*0.86))
    self.lbl2=lv.label(lv.screen_active())
    self.lbl2.set_style_text_font(lv.font_montserrat_24,0)
    self.lbl2.set_text("2")
    self.lbl2.align(lv.ALIGN.CENTER,round(105*0.86),round(-105*0.5))
    #self.lbl3=lv.label(lv.screen_active())
    #self.lbl3.set_style_text_font(lv.font_montserrat_24,0)
    #self.lbl3.set_text("3")  
    #self.lbl3.align(lv.ALIGN.CENTER,round(105*1),round(-105*0))

    self.lbl5=lv.label(lv.screen_active())
    self.lbl5.set_style_text_font(lv.font_montserrat_24,0)
    self.lbl5.set_text("5")
    self.lbl5.align(lv.ALIGN.CENTER,round(105*0.5),round(105*0.86))
    self.lbl4=lv.label(lv.screen_active())
    self.lbl4.set_style_text_font(lv.font_montserrat_24,0)
    self.lbl4.set_text("4")
    self.lbl4.align(lv.ALIGN.CENTER,round(105*0.86),round(105*0.5))
    #self.lbl12=lv.label(lv.screen_active())
    #self.lbl12.set_style_text_font(lv.font_montserrat_24,0)
    #self.lbl12.set_text("12")
    #self.lbl12.align(lv.ALIGN.CENTER,round(-105*0),round(-105*1))

  def drawLogButtons (self):
    self.btnBk=lv.button(lv.screen_active())
    self.btnBk.set_style_bg_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
    lbl=lv.label(self.btnBk)
    lbl.set_style_text_font(lv.font_montserrat_24,0)
    lbl.set_style_text_color(lv.color_hex(0x0), 0)
    lbl.set_text(lv.SYMBOL.LEFT)
    self.btnBk.add_event_cb(lambda e: self.log('Voltar'), lv.EVENT.CLICKED, None) # deploy.w.cancelSleep()
    self.btnBk.align(lv.ALIGN.CENTER,round(-90*1),round(-90*0))


    self.btnSt=lv.button(lv.screen_active())
    self.btnSt.set_style_bg_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
    lbl=lv.label(self.btnSt)
    lbl.set_style_text_font(lv.font_montserrat_24,0)
    lbl.set_style_text_color(lv.color_hex(0x0), 0)
    lbl.set_text(lv.SYMBOL.STOP)
    self.btnSt.add_event_cb(lambda e: self.log('Chegar'), lv.EVENT.CLICKED, None) # deploy.w.cancelSleep()
    self.btnSt.align(lv.ALIGN.CENTER,round(90*0),round(90*1))

    self.btnGo=lv.button(lv.screen_active())
    self.btnGo.set_style_bg_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
    lbl=lv.label(self.btnGo)
    lbl.set_style_text_font(lv.font_montserrat_24,0)
    lbl.set_style_text_color(lv.color_hex(0x0), 0)
    lbl.set_text(lv.SYMBOL.RIGHT)
    self.btnGo.add_event_cb(lambda e: self.log('Rodar'), lv.EVENT.CLICKED, None) # deploy.w.cancelSleep()
    self.btnGo.align(lv.ALIGN.CENTER,round(90*1),round(-90*0))

    self.btnWk=lv.button(lv.screen_active())
    self.btnWk.set_style_bg_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
    lbl=lv.label(self.btnWk)
    lbl.set_style_text_font(lv.font_montserrat_24,0)
    lbl.set_style_text_color(lv.color_hex(0x0), 0)
    lbl.set_text(lv.SYMBOL.EJECT)
    self.btnWk.add_event_cb(lambda e: self.log('Caminhar'), lv.EVENT.CLICKED, None) # deploy.w.cancelSleep()
    self.btnWk.align(lv.ALIGN.CENTER,round(-90*0),round(-90*1))

    self.btnWa=lv.button(lv.screen_active())
    self.btnWa.set_style_bg_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
    lbl=lv.label(self.btnWa)
    lbl.set_style_text_font(lv.font_montserrat_24,0)
    lbl.set_text(lv.SYMBOL.PAUSE)
    lbl.set_style_text_color(lv.color_hex(0x0), 0)
    self.btnWa.add_event_cb(lambda e: self.log('Esperar'), lv.EVENT.CLICKED, None) # deploy.w.cancelSleep()
    self.btnWa.align(lv.ALIGN.CENTER,round(-90*0),round(-90*0))

    self.btnAct=lv.button(lv.screen_active())
    self.btnAct.set_style_bg_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
    self.lbl=lv.label(self.btnAct)
    self.lbl.set_style_text_font(lv.font_montserrat_24,0)
    self.lbl.set_style_text_color(lv.color_hex(0x0), 0)
    rtc=machine.RTC() #https://forum.micropython.org/viewtopic.php?t=7261#p41325
    self.lbl.set_text(rtc.memory()) 
    self.btnAct.align(lv.ALIGN.CENTER, 0, 50)
    self.axp.setLDO2Voltage(3300) # turn backlight on

  def drawRing (self, size, value, text):
    arc=lv.arc(lv.screen_active())
    arc.set_size(size,size)
    arc.center()
    arc.remove_flag(lv.obj.FLAG.CLICKABLE)
    # arc.remove_style(None, lv.PART.KNOB)
    arc.set_style_bg_color(lv.color_hex(0x0),lv.PART.KNOB)
    arc.set_style_arc_color(lv.color_hex(0x0),lv.PART.INDICATOR)
    arc.set_style_arc_width(3, lv.PART.INDICATOR)
    arc.set_bg_angles(0,360)
    arc.set_rotation(270)
    arc.set_range(0,60)
    arc.set_value(value)
    
  def drawNeedleAndRing (self, size, value, text):
    arc=lv.arc(lv.screen_active())
    arc.set_size(size,size)
    arc.center()
    arc.set_style_arc_width(0, lv.PART.INDICATOR)
    arc.set_style_arc_width(0, lv.PART.MAIN)
    # arc.set_style_arc_color(lv.color_hex(0xFFFFFF),lv.PART.MAIN)
    # arc.set_style_arc_color(lv.color_hex(0xFFFFFF),lv.PART.INDICATOR)
    arc.remove_flag(lv.obj.FLAG.CLICKABLE)
    arc.remove_style(None, lv.PART.KNOB)
    # arc.set_style_bg_color(lv.color_hex(0x0),lv.PART.KNOB)
    arc.set_bg_angles(0,360)
    arc.set_rotation(270)
    arc.set_range(0,60)
    arc.set_value(value)
    pointer = lv.obj(lv.screen_active())
    pointer.set_size(10,60)
    pointer.set_style_bg_color(lv.color_hex(0x000000),0)
    pointer.center()
    arc.rotate_obj_to_angle(pointer,0)

  def drawDateTempHourMin (self):
    datetime=self.hwrtc.datetime()
    self.temp= self.axp.getTemp()
    hours=datetime[4]
    mins=datetime[5]
    self.mon=datetime[1]
    self.mday=datetime[2]
    self.drawRing (180, mins, str(mins))
    self.drawNeedleAndRing (100, int((hours%12)*5+mins/12), str(hours))

  def sleepNow (self, event):
    # may be called with None as argument
    scr=lv.screen_active()
    lv.obj.clean(scr)
    self.axp.disablePower(axp202c.AXP202_LDO2) # backlight
    self.axp.disablePower(axp202c.AXP202_LDO3) # from my C code
    self.axp.disablePower(axp202c.AXP202_LDO4) # audio
    self.axp.disablePower(axp202c.AXP202_DCDC2) # from my C code
    self.axp.disablePower(axp202c.AXP202_EXTEN) # from my C code
    self.axp.disableADC(axp202c.AXP202_ADC1,axp202c.AXP202_BATT_VOL_ADC1) # https://github.com/lewisxhe/MicroPython-for-TTGO-T-Watch?tab=readme-ov-file#axp202-power-example
    self.axp.disableADC(axp202c.AXP202_ADC1, axp202c.AXP202_BATT_CUR_ADC1)
    self.axp.disableADC(axp202c.AXP202_ADC1, axp202c.AXP202_VBUS_VOL_ADC1)
    self.axp.disableADC(axp202c.AXP202_ADC1, axp202c.AXP202_VBUS_CUR_ADC1)
    touchInt=machine.Pin(38, machine.Pin.IN) # touchscreen interrupt is connected to pin 38 which is a touch pin - this might work
    esp32.wake_on_ext0 (touchInt, esp32.WAKEUP_ALL_LOW) # pin seems to be active low
    machine.deepsleep() # sleep forever, wake on touchscreen 

  def sleepOnTimer (self):
    print ('deep sleep timer started')
    if (hasattr(self, 'lblSleep')):
      self.lblSleep.set_text(lv.SYMBOL.STOP)
    self.tim=lv.timer_create(lambda event: self.sleepNow(event), 20000, None) # https://forum.lvgl.io/t/how-to-delete-one-lv-timer-in-micropython-lgvl-version-8-3/9428/1

  def cancelSleep (self):
    if (self.tim!=None):
      self.tim.delete()
      print ('deep sleep timer cancelled')
    if (hasattr(self, 'lblSleep')):
      self.lblSleep.set_text(lv.SYMBOL.PLAY)

  def log (self, strEv):
    datetime=self.hwrtc.datetime()
    with open('logfile.csv', 'a', encoding='utf-8') as f:
      s='{:02}-{:02}-{:02}T{:02}{:02}{:02}, {:03}, {}\n'.format(datetime[0],datetime[1],datetime[2],datetime[4],datetime[5],datetime[6],self.axp.getBattPercentage(),strEv)
      f.write(s)
    if (strEv!='VerHora') :
      rtc=machine.RTC()
      rtc.memory(strEv)
    if (hasattr(self, 'btnAct')):
      print('poe no botao')
      self.lbl.set_text(strEv)

#bt.set_style_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
# import math
# math.sin(math.pi/3)