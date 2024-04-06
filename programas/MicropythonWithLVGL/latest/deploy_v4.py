import watch_v4
import lvgl as lv
w=watch_v4.WATCH()
w.setHardware()
w.drawTimeFace()
w.drawDateTempHourMin()
w.drawExternalFace()

w.drawLogButtons()
w.sleepOnTimer()

