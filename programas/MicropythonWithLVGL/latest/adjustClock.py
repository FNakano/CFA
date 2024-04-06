import machine
import pcf8563
import axp202c
import time

axp=axp202c.PMU()
hwrtc=pcf8563.PCF8563(axp.bus)
datetime=hwrtc.datetime()
dt=machine.RTC().datetime()
hwrtc.write_all(dt[6], dt[5], dt[4], dt[3], dt[2], dt[1], dt[0]%100)

