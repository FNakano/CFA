# para ESP-C3-32S-Kit da AI-Thinker
# https://docs.ai-thinker.com/_media/esp32/docs/esp-c3-32s-kit-v1.0_specification.pdf

from machine import Pin
pr = Pin(3,Pin.OUT)
pg = Pin(4,Pin.OUT)
pb = Pin(5,Pin.OUT)

pb.on()
