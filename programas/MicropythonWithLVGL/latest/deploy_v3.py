import watch_v3
import lvgl as lv
w=watch_v3.WATCH()
w.setHardware()

btn=lv.button(lv.screen_active())
btn.align(lv.ALIGN.CENTER, 0, 50)
label=lv.label(btn)
label.set_style_text_font(lv.font_montserrat_24,0)
label.set_text("Atividade") 

w.drawDateTempHourMin()
w.sleepOnTimer()
btn=lv.button(lv.screen_active())
btn.add_event_cb(lambda e: w.cancelSleep(), lv.EVENT.CLICKED, None) # deploy.w.cancelSleep()
# btn.add_event_cb(lambda e: print("clicked on play"), lv.EVENT.CLICKED, None) # deploy.w.cancelSleep()
btn.align(lv.ALIGN.TOP_LEFT, 0, 0)
label=lv.label(btn)
label.set_style_text_font(lv.font_montserrat_24,0)
# label.set_text(lv.SYMBOL.PLAY) # right text
label.set_text(str(w.temp)) # temporary text

btn2=lv.button(lv.screen_active())
btn2.add_event_cb(lambda e: w.sleepOnTimer(), lv.EVENT.CLICKED, None)
btn2.align(lv.ALIGN.TOP_RIGHT, 0,0)
label=lv.label(btn2)
label.set_style_text_font(lv.font_montserrat_24,0)
# label.set_text(lv.SYMBOL.STOP) # right text
label.set_text(str(w.mday)+"/"+str(w.mon))

