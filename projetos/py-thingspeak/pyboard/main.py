import machine
import btest # sends one point
machine.deepsleep(60000)
# I think all errors must be treated in order to the
# microcontroler boot in automatic mode. Otherwise
# it issues an error message and enters interactive mode
# which does not revert to automatic mode... the
# device just stops, waiting for user input because it
# did not execute machine.deepsleep()
# Somehow, ESP32C3 detects USB data connections and
# (micropython firmware, I believe) interrupts automatic
# execution of main.py
# I believe a hardware timer extern to the ESP32 triggering
# ESP32 reset (pin) is the most robust solution.
