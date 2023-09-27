import network
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="ESP8266-0001", password='123456789')
# https://randomnerdtutorials.com/micropython-esp32-esp8266-access-point-ap/
# FN 2023-09-22: I believe essid should be more than three characters long
# to connect to Ubuntu (some strange constraint on wifi essid on Ubuntu)