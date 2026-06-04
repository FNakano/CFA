import machine
import esp32
import time

# 1. Choose an RTC GPIO pin (e.g., GPIO 0). Use a pull-up or pull-down resistor.
WAKEUP_PIN = 0  
button = machine.Pin(WAKEUP_PIN, machine.Pin.IN, machine.Pin.PULL_UP)

# 2. Check why the device just reset
wake_reason = machine.wake_reason()

if wake_reason == machine.DEEPSLEEP_RESET:
    print("Woke up from deep sleep by GPIO pin!")
    # Optional: Toggle a different pin (e.g. built-in LED) to show activity
    # led = machine.Pin(8, machine.Pin.OUT)
    # led.value(1)
    # time.sleep(1)
    # led.value(0)
    
else:
    print("Power-on reset or manual reset.")
    print("Configuring GPIO wakeup...")
    
    # Configure the ESP32-C3 to wake on the button (ALL_LOW for active-low button)
    esp32.wake_on_gpio(pins=(button,), level=esp32.WAKEUP_ALL_LOW)
    
    print("Entering deep sleep. Press the button to wake up.")
    time.sleep(1) # Wait slightly to allow serial output to finish before sleeping
    machine.deepsleep()