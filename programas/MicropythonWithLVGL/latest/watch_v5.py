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
import math

class WATCH:
  tim=None
  def setHardware (self):
    print("LVGL version:"+str(lv.version_major())+"."+str(lv.version_minor()))
    axp=axp202c.PMU()
    axp.enableADC(axp202c.AXP202_ADC1,axp202c.AXP202_BATT_VOL_ADC1) # https://github.com/lewisxhe/MicroPython-for-TTGO-T-Watch?tab=readme-ov-file#axp202-power-example
    axp.enableADC(axp202c.AXP202_ADC1, axp202c.AXP202_BATT_CUR_ADC1)
    axp.enableADC(axp202c.AXP202_ADC1, axp202c.AXP202_VBUS_VOL_ADC1)
    axp.enableADC(axp202c.AXP202_ADC1, axp202c.AXP202_VBUS_CUR_ADC1)
    axp.enablePower(axp202c.AXP202_LDO3) # turn something on
    axp.enablePower(axp202c.AXP202_LDO4) # turn audio on
    axp.enablePower(axp202c.AXP202_DCDC2) # turn something on
    axp.enablePower(axp202c.AXP202_EXTEN) # turn something on
    disp = st7789(
      mosi=19, clk=18, cs=5, dc=27, rst=-1, backlight=12, power=-1,
      width=240, height=240, factor=4, invert=True, rot=REVERSE_PORTRAIT, start_x=0, start_y=80)
    # got REVERSE_PORTRAIT to work!
    touch = ft6x36(sda=23, scl=32, width=240, height=240)
    self.hwrtc=pcf8563.PCF8563(axp.bus)
    self.log('VerHora')

  def drawProgrammingFace (self):
    actscr=lv.screen_active()
    lv.obj.clean(actscr)
    self.lblSleep=lv.label(lv.screen_active())
    self.lblSleep.set_style_text_font(lv.font_montserrat_24,0)
    self.lblSleep.align(lv.ALIGN.TOP_MID,0,0)
    # self.axp.isChargeing()
    btn=lv.button(lv.screen_active())
    btn.add_event_cb(lambda e: self.cancelSleep(), lv.EVENT.CLICKED, None) # deploy.w.cancelSleep()
    btn.align(lv.ALIGN.TOP_LEFT, 0, 0)
    label=lv.label(btn)
    label.set_style_text_font(lv.font_montserrat_24,0)
    label.set_text(lv.SYMBOL.PLAY)

    btn2=lv.button(lv.screen_active())
    btn2.add_event_cb(lambda e: self.sleepOnTimer(), lv.EVENT.CLICKED, None)
    label=lv.label(btn2)
    label.set_style_text_font(lv.font_montserrat_24,0)
    label.set_text(lv.SYMBOL.STOP)
    btn2.align(lv.ALIGN.TOP_RIGHT, 0,0)

    btn3=lv.button(lv.screen_active())
    btn3.add_event_cb(lambda e: self.axp.shutdown(), lv.EVENT.CLICKED, None)
    label=lv.label(btn3)
    label.set_style_text_font(lv.font_montserrat_24,0)
    label.set_text("shutdown")
    btn3.align(lv.ALIGN.CENTER, 0,0)

  def drawTimeFace (self):
    axp=axp202c.PMU()
    scr=lv.screen_active()
    btn=lv.button(scr)
    btn.set_style_bg_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
    btn.add_event_cb(lambda e: self.drawProgrammingFace(), lv.EVENT.CLICKED, None) # deploy.w.cancelSleep()
    label=lv.label(btn)
    label.set_style_text_color(lv.color_hex(0x0), 0)
    label.set_style_text_font(lv.font_montserrat_24,0)
    label.set_text(str(axp.getBattPercentage())+'%')
    btn.align(lv.ALIGN.TOP_RIGHT, 0, 0)

    btn2=lv.button(scr)
    btn2.set_style_bg_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
    label=lv.label(btn2)
    label.set_style_text_color(lv.color_hex(0x0), 0)
    label.set_style_text_font(lv.font_montserrat_24,0)
    label.set_text(str(self.mday)+"/"+str(self.mon))
    btn2.align(lv.ALIGN.TOP_LEFT, 0,0)
    r=105
    stp= math.pi/30
    
    for i in range (1,61):
      lbl=lv.label(scr)
      if ((i%5==0) & (i%15!=0)):
        lbl.set_style_text_font(lv.font_montserrat_24,0)
        lbl.set_text(str(round(i/5)))
      else:
        lbl.set_text("+")
      lbl.align(lv.ALIGN.CENTER,round(math.sin(stp*(i))*r),round(-math.cos(stp*(i))*r))
          

  def drawLogButtons (self):
    scr=lv.screen_active()
    pl=90
    btnBk=lv.button(scr)
    btnBk.set_style_bg_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
    lbl=lv.label(btnBk)
    lbl.set_style_text_font(lv.font_montserrat_24,0)
    lbl.set_style_text_color(lv.color_hex(0x0), 0)
    lbl.set_text(lv.SYMBOL.LEFT)
    btnBk.add_event_cb(lambda e: self.log('Voltar'), lv.EVENT.CLICKED, None) # deploy.w.cancelSleep()
    btnBk.align(lv.ALIGN.CENTER,-pl,0)


    btnSt=lv.button(scr)
    btnSt.set_style_bg_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
    lbl=lv.label(btnSt)
    lbl.set_style_text_font(lv.font_montserrat_24,0)
    lbl.set_style_text_color(lv.color_hex(0x0), 0)
    lbl.set_text(lv.SYMBOL.STOP)
    btnSt.add_event_cb(lambda e: self.log('Chegar'), lv.EVENT.CLICKED, None) # deploy.w.cancelSleep()
    btnSt.align(lv.ALIGN.CENTER,0,pl)

    btnGo=lv.button(scr)
    btnGo.set_style_bg_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
    lbl=lv.label(btnGo)
    lbl.set_style_text_font(lv.font_montserrat_24,0)
    lbl.set_style_text_color(lv.color_hex(0x0), 0)
    lbl.set_text(lv.SYMBOL.RIGHT)
    btnGo.add_event_cb(lambda e: self.log('Rodar'), lv.EVENT.CLICKED, None) # deploy.w.cancelSleep()
    pl=90
    btnGo.align(lv.ALIGN.CENTER,pl,0)

    btnWk=lv.button(scr)
    btnWk.set_style_bg_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
    lbl=lv.label(btnWk)
    lbl.set_style_text_font(lv.font_montserrat_24,0)
    lbl.set_style_text_color(lv.color_hex(0x0), 0)
    lbl.set_text(lv.SYMBOL.EJECT)
    btnWk.add_event_cb(lambda e: self.log('Caminhar'), lv.EVENT.CLICKED, None) # deploy.w.cancelSleep()
    btnWk.align(lv.ALIGN.CENTER,0,-pl)

    btnWa=lv.button(scr)
    btnWa.set_style_bg_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
    lbl=lv.label(btnWa)
    lbl.set_style_text_font(lv.font_montserrat_24,0)
    lbl.set_text(lv.SYMBOL.PAUSE)
    lbl.set_style_text_color(lv.color_hex(0x0), 0)
    btnWa.add_event_cb(lambda e: self.log('Esperar'), lv.EVENT.CLICKED, None) # deploy.w.cancelSleep()
    btnWa.align(lv.ALIGN.CENTER,0,0)

    self.btnAct=lv.button(scr)
    self.btnAct.set_style_bg_opa(lv.STATE.DEFAULT, lv.OPA.TRANSP)
    self.lbl=lv.label(self.btnAct)
    self.lbl.set_style_text_font(lv.font_montserrat_24,0)
    self.lbl.set_style_text_color(lv.color_hex(0x0), 0)
    rtc=machine.RTC() #https://forum.micropython.org/viewtopic.php?t=7261#p41325
    self.lbl.set_text(rtc.memory()) 
    self.btnAct.align(lv.ALIGN.CENTER, 0, 50)
    axp=axp202c.PMU()
    axp.enablePower(axp202c.AXP202_LDO2) # turn backlight on
    axp.setLDO2Voltage(3300) # max brightness

  def drawRing (self, size, value, text):
    arc=lv.arc(lv.screen_active())
    arc.set_size(size,size)
    arc.center()
    arc.remove_flag(lv.obj.FLAG.CLICKABLE)
    arc.set_style_arc_width(0, lv.PART.MAIN)
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
    pointer.set_size(10,50)
    pointer.set_style_bg_color(lv.color_hex(0x000000),0)
    pointer.center()
    arc.rotate_obj_to_angle(pointer,0)

  def drawDateTempHourMin (self):
    datetime=self.hwrtc.datetime()
    hours=datetime[4]
    mins=datetime[5]
    self.mon=datetime[1]
    self.mday=datetime[2]
    self.drawRing (230, mins, str(mins))
    self.drawNeedleAndRing (100, int((hours%12)*5+mins/12), str(hours))

  def sleepNow (self, event):
    # may be called with None as argument
    scr=lv.screen_active()
    lv.obj.clean(scr)
    axp=axp202c.PMU()
    axp.disablePower(axp202c.AXP202_LDO2) # backlight
    axp.disablePower(axp202c.AXP202_LDO3) # from my C code
    axp.disablePower(axp202c.AXP202_LDO4) # audio
    axp.disablePower(axp202c.AXP202_DCDC2) # from my C code
    axp.disablePower(axp202c.AXP202_EXTEN) # from my C code
    axp.disableADC(axp202c.AXP202_ADC1,axp202c.AXP202_BATT_VOL_ADC1) # https://github.com/lewisxhe/MicroPython-for-TTGO-T-Watch?tab=readme-ov-file#axp202-power-example
    axp.disableADC(axp202c.AXP202_ADC1, axp202c.AXP202_BATT_CUR_ADC1)
    axp.disableADC(axp202c.AXP202_ADC1, axp202c.AXP202_VBUS_VOL_ADC1)
    axp.disableADC(axp202c.AXP202_ADC1, axp202c.AXP202_VBUS_CUR_ADC1)
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
    axp=axp202c.PMU()
    with open('logfile.csv', 'a', encoding='utf-8') as f:
      s='{:02}-{:02}-{:02}T{:02}{:02}{:02}, {:03}, {}\n'.format(datetime[0],datetime[1],datetime[2],datetime[4],datetime[5],datetime[6],axp.getBattPercentage(),strEv)
      f.write(s)
    if (strEv!='VerHora') :
      rtc=machine.RTC()
      rtc.memory(strEv)
    if (hasattr(self, 'lbl')):
      print('poe no botao')
      self.lbl.set_text(strEv)
