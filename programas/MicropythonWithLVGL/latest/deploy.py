import watch_v5
import lvgl as lv
import gc
w=watch_v5.WATCH()
w.setHardware()
w.drawDateTempHourMin()
gc.collect() # in order to drawTimeFace not fail
w.drawTimeFace()
# w.drawExternalFace()

w.drawLogButtons()
w.sleepOnTimer()

