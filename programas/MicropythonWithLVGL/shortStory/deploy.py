import watch_v5
import lvgl as lv
w=watch_v5.WATCH()
w.setHardware()
w.drawDateTempHourMin()
w.drawTimeFace()
# w.drawExternalFace()

w.drawLogButtons()
w.sleepOnTimer()

