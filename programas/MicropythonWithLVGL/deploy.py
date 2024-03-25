import watch_v2
import lvgl as lv
w=watch_v2.WATCH()
w.setHardware()
w.drawHourMin()
w.sleepOnTimer()
btn=lv.button(lv.screen_active())
btn.add_event_cb(lambda e: w.cancelSleep(), lv.EVENT.CLICKED, None) # deploy.w.cancelSleep()
btn.align(lv.ALIGN.TOP_LEFT, 0, 0)
label=lv.label(btn)
label.set_style_text_font(lv.font_montserrat_24,0)
label.set_text(lv.SYMBOL.PLAY)

btn2=lv.button(lv.screen_active())
btn2.add_event_cb(lambda e: w.sleepOnTimer(), lv.EVENT.CLICKED, None)
btn2.align(lv.ALIGN.TOP_RIGHT, 0,0)
label=lv.label(btn2)
label.set_style_text_font(lv.font_montserrat_24,0)
label.set_text(lv.SYMBOL.STOP)

